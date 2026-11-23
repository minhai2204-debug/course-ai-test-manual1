#!/usr/bin/env python3
"""db_check.py — chạy truy vấn kiểm chứng CHỈ ĐỌC cho TC @DBCheck.

Luật: .claude/rules/database_rules.md. Chốt chặn chỉ cho phép một câu SELECT / WITH … SELECT,
chạy trong transaction read-only (MySQL/MariaDB, PostgreSQL), giới hạn số dòng, che cột bí mật.

Python 3.9+. Chốt chặn không cần thư viện ngoài; driver chỉ cần khi chạy thật:
  mysql    → pymysql        postgres → psycopg (hoặc psycopg2)        mssql → pyodbc

Ba loại truy vấn (database_rules.md mục 2): --mode record (A · bản ghi) · set (B · tập kết quả)
· aggregate (C · tổng hợp — chỉ trả số tổng hợp, tối đa 50 nhóm). Tham số {{ten}} thay bằng --param ten=giatri.
--snapshot / --diff so bản ghi trước–sau · --expect tự chấm theo file kỳ vọng JSON.

Mã thoát: 0 chạy được · 2 câu lệnh bị chặn · 3 lỗi cấu hình / driver / kết nối · 4 lỗi khi chạy truy vấn
· 5 kết quả lệch kỳ vọng (--expect)
"""
import argparse
import datetime as _dt
import hashlib
import json
import re
import sys
from pathlib import Path

DIALECTS = ('mysql', 'postgres', 'mssql')
ENGINE_ALIASES = {
    'mysql': 'mysql', 'mariadb': 'mysql',
    'postgres': 'postgres', 'postgresql': 'postgres', 'pg': 'postgres',
    'mssql': 'mssql', 'sqlserver': 'mssql', 'sql_server': 'mssql',
}

# Từ khoá có thể gây ghi / khoá khi nằm GIỮA một câu bắt đầu bằng SELECT / WITH
BANNED_WORDS = {
    'INSERT', 'UPDATE', 'DELETE', 'MERGE', 'INTO', 'OUTFILE', 'DUMPFILE',
    'LOCK', 'UNLOCK', 'PROCEDURE', 'CREATE', 'ALTER', 'DROP', 'GRANT', 'REVOKE',
    'EXEC', 'EXECUTE', 'CALL', 'WAITFOR', 'SHUTDOWN', 'KILL',
    'OPENROWSET', 'OPENQUERY', 'OPENDATASOURCE',
    'UPDLOCK', 'XLOCK', 'HOLDLOCK', 'TABLOCK', 'TABLOCKX', 'PAGLOCK',
}
# Hàm có tác dụng phụ (ghi, khoá, ngủ, đọc file hệ thống, gọi ra ngoài)
BANNED_FUNCS = {
    'SLEEP', 'BENCHMARK', 'GET_LOCK', 'RELEASE_LOCK', 'RELEASE_ALL_LOCKS', 'LOAD_FILE',
    'PG_SLEEP', 'PG_SLEEP_FOR', 'PG_SLEEP_UNTIL', 'NEXTVAL', 'SETVAL', 'SET_CONFIG',
    'PG_TERMINATE_BACKEND', 'PG_CANCEL_BACKEND', 'PG_RELOAD_CONF', 'PG_ROTATE_LOGFILE',
    'PG_SWITCH_WAL', 'PG_READ_FILE', 'PG_READ_BINARY_FILE', 'PG_LS_DIR',
    'LO_IMPORT', 'LO_EXPORT', 'LO_UNLINK', 'DBLINK', 'DBLINK_EXEC',
}
BANNED_FUNC_PREFIXES = ('PG_ADVISORY', 'PG_TRY_ADVISORY')

AGG_FUNCS = {'COUNT', 'SUM', 'AVG', 'MIN', 'MAX'}
MAX_GROUPS = 50
PERSONAL_COL = re.compile(r'email|phone|mobile|address|first_?name|last_?name|full_?name|contact|dia_?chi|dien_?thoai', re.I)
PARAM = re.compile(r'\{\{\s*([A-Za-z_][A-Za-z0-9_]*)\s*\}\}')

DEFAULT_MASK = r'pass|pwd|hash|token|secret|salt|otp|api_?key|session|cookie|email|phone|mobile|address'
SAFE_VALUE = re.compile(r'^auto_|@auto\.test$|@example\.com$', re.I)


class GuardError(Exception):
    pass


# ---------------------------------------------------------------- chốt chặn

def _tokens(sql, dialect):
    """Tách token NGOÀI chuỗi / định danh có ngoặc / comment, theo đúng cú pháp của dialect.

    Trả về list (loại, giá trị): 'w' từ (đã viết HOA) · 'p' ký tự đơn · 's' literal.
    """
    out, i, n = [], 0, len(sql)
    while i < n:
        c = sql[i]
        if c.isspace():
            i += 1
            continue
        if sql.startswith('/*', i):
            if dialect == 'mysql' and i + 2 < n and sql[i + 2] in '!+':
                raise GuardError('comment thực thi được của MySQL (/*! … */, /*+ … */) — bỏ đi')
            j = sql.find('*/', i + 2)
            if j < 0:
                raise GuardError('comment /* chưa đóng')
            i = j + 2
            continue
        if sql.startswith('--', i):
            # MySQL chỉ coi "--" là comment khi theo sau là khoảng trắng / hết dòng
            if dialect != 'mysql' or i + 2 >= n or sql[i + 2].isspace():
                j = sql.find('\n', i)
                i = n if j < 0 else j + 1
                continue
        if c == '#' and dialect == 'mysql':
            j = sql.find('\n', i)
            i = n if j < 0 else j + 1
            continue
        if c == '$' and dialect == 'postgres':
            m = re.match(r'\$([A-Za-z_][A-Za-z0-9_]*)?\$', sql[i:])
            if m:
                tag = m.group(0)
                j = sql.find(tag, i + len(tag))
                if j < 0:
                    raise GuardError('chuỗi $…$ chưa đóng')
                out.append(('s', ''))
                i = j + len(tag)
                continue
        closers = {"'": "'", '"': '"'}
        if dialect == 'mysql':
            closers['`'] = '`'
        if dialect == 'mssql':
            closers['['] = ']'
        if c in closers:
            close = closers[c]
            backslash = (dialect == 'mysql' and c in "'\"") or (
                dialect == 'postgres' and c == "'" and i > 0 and sql[i - 1] in 'eE'
                and (i < 2 or not (sql[i - 2].isalnum() or sql[i - 2] == '_')))
            j = i + 1
            while True:
                if j >= n:
                    raise GuardError('chuỗi / định danh mở bằng %s chưa đóng' % c)
                ch = sql[j]
                if backslash and ch == '\\':
                    j += 2
                    continue
                if ch == close:
                    if j + 1 < n and sql[j + 1] == close:
                        j += 2
                        continue
                    break
                j += 1
            out.append(('s', ''))
            i = j + 1
            continue
        m = re.match(r'[^\W]+', sql[i:]) if (c.isalnum() or c == '_' or c == '$') else None
        if m:
            word = m.group(0)
            out.append(('w', word.upper()))
            i += len(word)
            continue
        out.append(('p', c))
        i += 1
    return out


def _check_dialect(sql, dialect):
    toks = _tokens(sql, dialect)
    while toks and toks[-1] == ('p', ';'):
        toks.pop()
    if not toks:
        raise GuardError('câu lệnh rỗng')
    if ('p', ';') in toks:
        raise GuardError('chỉ được MỘT câu lệnh — bỏ dấu ; ở giữa')
    first = next((v for k, v in toks if k == 'w'), None)
    lead = toks[:toks.index(('w', first))] if first else toks
    if first not in ('SELECT', 'WITH') or any(t != ('p', '(') for t in lead):
        raise GuardError('chỉ cho phép SELECT hoặc WITH … SELECT (gặp: %s)' % (first or toks[0][1]))
    words = [v for k, v in toks if k == 'w']
    if first == 'WITH' and 'SELECT' not in words:
        raise GuardError('WITH phải kết thúc bằng SELECT')
    for idx, (k, v) in enumerate(toks):
        prev = toks[idx - 1] if idx else ('', '')
        nxt = toks[idx + 1] if idx + 1 < len(toks) else ('', '')
        if k == 'w':
            if v in BANNED_WORDS:
                raise GuardError('từ khoá bị cấm: %s' % v)
            if v == 'SHARE' and prev[1] in ('FOR', 'KEY'):
                raise GuardError('khoá dòng (FOR SHARE / FOR KEY SHARE) bị cấm')
            if nxt == ('p', '(') and (v in BANNED_FUNCS or v.startswith(BANNED_FUNC_PREFIXES)):
                raise GuardError('hàm có tác dụng phụ bị cấm: %s()' % v)
        elif (k, v) == ('p', '*'):
            if prev[1] in ('SELECT', 'DISTINCT', 'ALL', ',', '.'):
                raise GuardError('không SELECT * — liệt kê đúng cột cần kiểm')
    if 'FROM' in words and 'WHERE' not in words:
        raise GuardError('thiếu WHERE — lọc theo dữ liệu do test tạo (auto_…) hoặc mã bản ghi đọc trên UI')
    return words


def check_sql(sql):
    """Kiểm câu lệnh theo CẢ BA dialect — chỉ qua khi cả ba cùng thấy đây là một câu SELECT an toàn.

    Trả về danh sách cảnh báo (không chặn). Vi phạm thì ném GuardError.
    """
    words = None
    for d in DIALECTS:
        try:
            words = _check_dialect(sql, d)
        except GuardError as e:
            raise GuardError('%s (cú pháp %s)' % (e, d))
    warnings = []
    if not ({'LIMIT', 'TOP', 'FETCH'} & set(words)):
        warnings.append('câu không tự giới hạn số dòng (LIMIT / TOP / FETCH FIRST) — công cụ chỉ lấy tối đa --max-rows dòng')
    return warnings


def _split_depth0(toks, sep=('p', ',')):
    """Tách danh sách token theo dấu phân cách nằm ngoài mọi cặp ngoặc."""
    parts, cur, depth = [], [], 0
    for t in toks:
        if t == ('p', '('):
            depth += 1
        elif t == ('p', ')'):
            depth -= 1
        if t == sep and depth == 0:
            parts.append(cur)
            cur = []
        else:
            cur.append(t)
    parts.append(cur)
    return [p for p in parts if p]


def _strip_alias(item):
    """Bỏ bí danh cuối mục SELECT: `expr AS ten` · `expr ten`. Trả về (biểu thức, bí danh)."""
    if len(item) >= 3 and item[-2] == ('w', 'AS'):
        return item[:-2], item[-1][1]
    if len(item) >= 2 and item[-1][0] in ('w', 's') and (item[-2][0] in ('w', 's') or item[-2] == ('p', ')')):
        return item[:-1], item[-1][1]
    return item, None


def check_aggregate(sql):
    """Loại C: mọi cột SELECT là hàm tổng hợp hoặc cột GROUP BY; GROUP BY không theo cột cá nhân."""
    toks = _tokens(sql, 'postgres')
    while toks and toks[-1] == ('p', ';'):
        toks.pop()
    words = [v for k, v in toks if k == 'w']
    if not words or words[0] != 'SELECT':
        raise GuardError('loại C (tổng hợp) phải bắt đầu bằng SELECT — không dùng WITH')
    depth, frm = 0, None
    for i, t in enumerate(toks):
        if t == ('p', '('):
            depth += 1
        elif t == ('p', ')'):
            depth -= 1
        elif t == ('w', 'FROM') and depth == 0:
            frm = i
            break
    if frm is None:
        raise GuardError('loại C phải có FROM … WHERE')
    start = toks.index(('w', 'SELECT')) + 1
    while start < frm and toks[start][1] in ('DISTINCT', 'ALL', 'TOP'):
        start += 2 if toks[start][1] == 'TOP' else 1
    items = _split_depth0(toks[start:frm])

    group, depth, i = [], 0, frm
    while i < len(toks):
        t = toks[i]
        if t == ('p', '('):
            depth += 1
        elif t == ('p', ')'):
            depth -= 1
        elif depth == 0 and t == ('w', 'GROUP') and i + 1 < len(toks) and toks[i + 1] == ('w', 'BY'):
            j = i + 2
            while j < len(toks) and not (toks[j][0] == 'w' and toks[j][1] in ('HAVING', 'ORDER', 'LIMIT', 'FETCH', 'OFFSET', 'UNION')):
                j += 1
            group = _split_depth0(toks[i + 2:j])
            break
        i += 1
    group_keys = {' '.join(v for _, v in g) for g in group}
    for g in group:
        name = ' '.join(v for k, v in g if k == 'w')
        if PERSONAL_COL.search(name):
            raise GuardError('loại C không được GROUP BY theo cột cá nhân: %s' % name.lower())

    for it in items:
        expr, alias = _strip_alias(it)
        has_agg = any(expr[n][0] == 'w' and expr[n][1] in AGG_FUNCS and n + 1 < len(expr) and expr[n + 1] == ('p', '(')
                      for n in range(len(expr)))
        key = ' '.join(v for _, v in expr)
        if not has_agg and key not in group_keys and (alias or '') not in group_keys:
            raise GuardError('loại C chỉ trả số tổng hợp — cột "%s" không phải hàm %s và không nằm trong GROUP BY'
                             % (key.lower(), '/'.join(sorted(AGG_FUNCS))))


def substitute_params(sql, params, engine):
    """Thay {{ten}} bằng literal đã escape. Chốt chặn chạy SAU bước này, trên câu cuối cùng."""
    def lit(v):
        if re.fullmatch(r'-?\d+(\.\d+)?', v):
            return v
        v = v.replace("'", "''")
        if engine in (None, 'mysql'):
            v = v.replace('\\', '\\\\')
        return "'%s'" % v
    missing = sorted({m.group(1) for m in PARAM.finditer(sql)} - set(params))
    if missing:
        raise GuardError('thiếu --param cho: %s' % ', '.join(missing))
    return PARAM.sub(lambda m: lit(params[m.group(1)]), sql)


# ---------------------------------------------------------------- kết nối

def load_env(root):
    env, path = {}, Path(root) / '.env'
    if path.is_file():
        for line in path.read_text(encoding='utf-8').splitlines():
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            k, v = line.split('=', 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def connect(env, engine, timeout):
    host, port = env.get('DB_HOST'), env.get('DB_PORT')
    user, pwd, name = env.get('DB_USER'), env.get('DB_PASSWORD', ''), env.get('DB_NAME')
    if not (host and user and name):
        raise RuntimeError('.env thiếu DB_HOST / DB_USER / DB_NAME')
    if engine == 'mysql':
        import pymysql
        conn = pymysql.connect(host=host, port=int(port or 3306), user=user, password=pwd,
                               database=name, connect_timeout=10, read_timeout=timeout,
                               charset='utf8mb4', autocommit=False)
        cur = conn.cursor()
        for stmt in ('SET SESSION MAX_EXECUTION_TIME = %d' % (timeout * 1000),
                     'SET SESSION max_statement_time = %d' % timeout):
            try:
                cur.execute(stmt)
            except Exception:
                pass
        cur.execute('START TRANSACTION READ ONLY')
        return conn, cur
    if engine == 'postgres':
        opts = '-c default_transaction_read_only=on -c statement_timeout=%d' % (timeout * 1000)
        try:
            import psycopg as pg
        except ImportError:
            import psycopg2 as pg
        conn = pg.connect(host=host, port=int(port or 5432), user=user, password=pwd,
                          dbname=name, connect_timeout=10, options=opts)
        return conn, conn.cursor()
    if engine == 'mssql':
        import pyodbc
        driver = env.get('DB_ODBC_DRIVER', 'ODBC Driver 18 for SQL Server')
        cs = 'DRIVER={%s};SERVER=%s,%s;DATABASE=%s;UID=%s;PWD=%s;ApplicationIntent=ReadOnly;%s' % (
            driver, host, port or 1433, name, user, pwd, env.get('DB_ODBC_EXTRA', ''))
        conn = pyodbc.connect(cs, timeout=10, autocommit=False)
        conn.timeout = timeout
        return conn, conn.cursor()
    raise RuntimeError('DB_ENGINE không hỗ trợ: %s' % engine)


# ---------------------------------------------------------------- kết quả

def shape(v):
    """Hình thái của giá trị bị che — không lộ giá trị."""
    if v is None:
        return 'NULL'
    if isinstance(v, (bytes, bytearray, memoryview)):
        return '<đã che · %d byte>' % len(bytes(v))
    if not isinstance(v, str):
        return v
    if SAFE_VALUE.search(v):
        return v
    m = re.match(r'^(\$[0-9a-z]+\$(?:\d+\$)?)', v, re.I)
    if m:
        return '<đã che · bắt đầu "%s" · %d ký tự>' % (m.group(1), len(v))
    return '<đã che · %d ký tự>' % len(v)


def cell(v):
    if v is None:
        return 'NULL'
    if isinstance(v, (bytes, bytearray, memoryview)):
        return '<%d byte>' % len(bytes(v))
    return str(v).replace('|', '\\|').replace('\n', ' ')




def plain(v):
    """Giá trị dạng chuỗi để lưu snapshot / so kỳ vọng (None giữ nguyên)."""
    if v is None:
        return None
    if isinstance(v, (bytes, bytearray, memoryview)):
        return '<%d byte>' % len(bytes(v))
    if isinstance(v, (int, float, str)):
        return v
    return str(v)


def fingerprint(v):
    """Dấu vân tay của giá trị bị che — biết có đổi hay không mà không lưu giá trị."""
    raw = bytes(v) if isinstance(v, (bytes, bytearray, memoryview)) else str(v).encode('utf-8')
    return hashlib.sha256(raw).hexdigest()[:12]


# ---------------------------------------------------------------- trước / sau

def save_snapshot(path, sql, cols, rows, fps):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({'sql': sql.strip(), 'columns': cols, 'rows': [[plain(v) for v in r] for r in rows],
                                'fingerprints': fps, 'time': _dt.datetime.now().strftime('%d-%m-%Y %H:%M:%S')},
                               ensure_ascii=False, indent=2), encoding='utf-8')


def diff_snapshot(path, cols, rows, fps, key):
    """So kết quả hiện tại với snapshot theo cột khoá. Trả về (dòng markdown, {(khoá, cột) đã đổi}, thêm, bớt)."""
    old = json.loads(path.read_text(encoding='utf-8'))
    if old['columns'] != cols:
        raise ValueError('cột của snapshot (%s) khác câu hiện tại (%s)' % (', '.join(old['columns']), ', '.join(cols)))
    k = cols.index(key) if key else 0

    def index(rs, fs):
        return {str(r[k]): (r, f) for r, f in zip(rs, fs)}
    before = index(old['rows'], old['fingerprints'])
    after = index([[plain(v) for v in r] for r in rows], fps)
    changed, lines = {}, []
    for kv in sorted(set(before) & set(after)):
        (rb, fb), (ra, fa) = before[kv], after[kv]
        for i, c in enumerate(cols):
            if fb[i] or fa[i]:
                if fb[i] != fa[i]:
                    changed[(kv, c)] = True
                    lines.append('| %s | %s | *(đã che)* | *(đã che — giá trị đổi)* |' % (kv, c))
            elif rb[i] != ra[i]:
                changed[(kv, c)] = True
                lines.append('| %s | %s | %s | %s |' % (kv, c, cell(rb[i]), cell(ra[i])))
    added = sorted(set(after) - set(before))
    removed = sorted(set(before) - set(after))
    out = ['', '## So với snapshot (chụp %s)' % old.get('time', '?'), '',
           '- Khoá so: `%s` · dòng thêm: %s · dòng mất: %s · ô đổi: **%d**' % (
               cols[k], ', '.join(added) or '—', ', '.join(removed) or '—', len(changed)), '']
    if lines:
        out += ['| Khoá | Cột | Trước | Sau |', '|---|---|---|---|'] + lines
    else:
        out.append('*Không ô nào thay đổi.*')
    return out, changed, added, removed


# ---------------------------------------------------------------- kỳ vọng

def _match(actual, exp):
    """Một ô kỳ vọng: giá trị · null · {"not_null"} · {"between": [a, b]} · {"starts_with": "…"} · {"hash_prefix": "$2y$"}."""
    if exp is None:
        return actual is None
    if isinstance(exp, dict):
        if exp.get('not_null'):
            return actual is not None
        if 'between' in exp:
            lo, hi = exp['between']
            try:
                return actual is not None and float(lo) <= float(actual) <= float(hi)
            except (TypeError, ValueError):
                return actual is not None and str(lo) <= str(actual) <= str(hi)
        if 'starts_with' in exp:
            return actual is not None and str(actual).startswith(exp['starts_with'])
        if 'hash_prefix' in exp:
            # cột bị che chỉ còn hình thái: '<đã che · bắt đầu "$2y$10$" · 60 ký tự>'
            return isinstance(actual, str) and ('bắt đầu "%s' % exp['hash_prefix']) in actual
        return False
    if isinstance(exp, (int, float)) and not isinstance(exp, bool):
        try:
            return float(actual) == float(exp)
        except (TypeError, ValueError):
            return False
    return actual is not None and str(actual) == str(exp)


def check_expect(spec, cols, display_rows, changed, key_vals):
    """Chấm theo file kỳ vọng. Trả về (dòng markdown, số mục lệch)."""
    res = []
    if 'row_count' in spec:
        res.append((len(display_rows) == spec['row_count'], 'Số dòng = %s' % spec['row_count'], len(display_rows)))
    for n, row_exp in enumerate(spec.get('rows', [])):
        if n >= len(display_rows):
            res.append((False, 'Dòng %d tồn tại' % (n + 1), 'không có'))
            continue
        for c, exp in row_exp.items():
            if c not in cols:
                res.append((False, 'Cột `%s` có trong kết quả' % c, 'không có'))
                continue
            act = display_rows[n][cols.index(c)]
            if isinstance(exp, dict) and ('changed' in exp or 'unchanged' in exp):
                was = changed.get((key_vals[n], c), False)
                res.append((was == bool(exp.get('changed')), 'Dòng %d · `%s` %s' % (
                    n + 1, c, 'đổi' if exp.get('changed') else 'giữ nguyên'), 'đổi' if was else 'giữ nguyên'))
            else:
                res.append((_match(act, exp), 'Dòng %d · `%s` = %s' % (n + 1, c, json.dumps(exp, ensure_ascii=False)),
                            cell(act)))
    if 'unchanged_except' in spec:
        allowed = set(spec['unchanged_except'])
        extra = sorted({c for (_, c) in changed} - allowed)
        res.append((not extra, 'Ngoài %s không cột nào đổi' % ', '.join('`%s`' % c for c in sorted(allowed)),
                    ', '.join(extra) or 'không cột nào'))
    lines = ['', '## So với kỳ vọng', '', '| | Kỳ vọng | Thực tế |', '|---|---|---|']
    lines += ['| %s | %s | %s |' % ('✅' if ok else '❌', what, act) for ok, what, act in res]
    return lines, sum(1 for ok, _, _ in res if not ok)


# ---------------------------------------------------------------- xuất

def to_markdown(meta, cols, rows, sql, warnings, extra=()):
    lines = ['# Truy vấn kiểm chứng CSDL', '', '| | |', '|---|---|']
    for k, v in meta.items():
        lines.append('| **%s** | %s |' % (k, v))
    lines += ['', '```sql', sql.strip(), '```', '']
    for w in warnings:
        lines.append('> ⚠️ %s' % w)
    if warnings:
        lines.append('')
    if cols:
        lines.append('| ' + ' | '.join(cols) + ' |')
        lines.append('|' + '---|' * len(cols))
        for r in rows:
            lines.append('| ' + ' | '.join(cell(v) for v in r) + ' |')
        if not rows:
            lines.append('| *(0 dòng)* |' + ' |' * (len(cols) - 1))
    lines += list(extra)
    return '\n'.join(lines) + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description='Chạy truy vấn kiểm chứng CHỈ ĐỌC (SELECT) cho TC @DBCheck')
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument('--sql', help='Câu SELECT')
    src.add_argument('--file', help='File .sql chứa đúng một câu SELECT')
    ap.add_argument('--mode', choices=('record', 'set', 'aggregate'), default='record',
                    help='Loại truy vấn: record (A · bản ghi) · set (B · tập kết quả) · aggregate (C · tổng hợp)')
    ap.add_argument('--param', action='append', default=[], metavar='TEN=GIATRI',
                    help='Thay {{TEN}} trong câu bằng giá trị (lặp lại được)')
    ap.add_argument('--root', default='.', help='Gốc project chứa .env (mặc định thư mục hiện tại)')
    ap.add_argument('--engine', help='Ghi đè DB_ENGINE: mysql · postgres · mssql')
    ap.add_argument('--tc', default='—', help='TC ID ghi vào evidence')
    ap.add_argument('--max-rows', type=int, default=50)
    ap.add_argument('--timeout', type=int, default=30, help='Giây, tối đa 30')
    ap.add_argument('--mask', default=DEFAULT_MASK, help='Regex tên cột cần che (không phân biệt hoa thường)')
    ap.add_argument('--no-mask', action='store_true', help='Tắt che — chỉ dùng trên CSDL không có dữ liệu thật')
    ap.add_argument('--snapshot', metavar='TEN', help='Lưu kết quả làm mốc "trước" vào --snap-dir/TEN.json')
    ap.add_argument('--diff', metavar='TEN', help='So kết quả với mốc TEN đã lưu, in các ô đổi')
    ap.add_argument('--key', help='Cột khoá để ghép dòng khi --diff (mặc định cột đầu tiên)')
    ap.add_argument('--snap-dir', default='reports/db-check/snapshots', help='Thư mục lưu mốc (đã .gitignore qua reports/)')
    ap.add_argument('--expect', metavar='FILE', help='File JSON kỳ vọng — công cụ tự chấm, lệch thì mã thoát 5')
    ap.add_argument('--check-only', action='store_true', help='Chỉ chạy chốt chặn, không kết nối')
    ap.add_argument('--json', action='store_true', help='In JSON thay cho Markdown')
    ap.add_argument('-o', '--out', help='Ghi evidence ra file (.md hoặc .json)')
    a = ap.parse_args(argv)

    sql = a.sql if a.sql is not None else Path(a.file).read_text(encoding='utf-8')
    env = {} if a.check_only else load_env(a.root)
    engine = ENGINE_ALIASES.get((a.engine or env.get('DB_ENGINE', '')).lower())
    try:
        params = dict(p.split('=', 1) for p in a.param)
    except ValueError:
        print('⛔ --param phải có dạng TEN=GIATRI', file=sys.stderr)
        return 3
    try:
        sql = substitute_params(sql, params, engine)
        warnings = check_sql(sql)
        if a.mode == 'aggregate':
            check_aggregate(sql)
        elif a.mode == 'set' and 'ORDER' not in {v for k, v in _tokens(sql, 'postgres') if k == 'w'}:
            warnings.append('loại B không có ORDER BY — chỉ so được tập bản ghi, không so được thứ tự')
    except GuardError as e:
        print('⛔ BỊ CHẶN: %s' % e, file=sys.stderr)
        return 2
    if a.check_only:
        print('✅ Qua chốt chặn (loại %s)' % a.mode + ''.join('\n⚠️ ' + w for w in warnings))
        return 0

    if not engine:
        print('⛔ Thiếu / sai DB_ENGINE trong .env (mysql · postgres · mssql)', file=sys.stderr)
        return 3
    max_rows = min(a.max_rows, MAX_GROUPS) if a.mode == 'aggregate' else a.max_rows
    timeout = max(1, min(a.timeout, 30))
    try:
        conn, cur = connect(env, engine, timeout)
    except ImportError as e:
        print('⛔ Chưa cài driver cho %s: %s' % (engine, e), file=sys.stderr)
        return 3
    except Exception as e:
        print('⛔ Không kết nối được (%s): %s' % (engine, type(e).__name__), file=sys.stderr)
        return 3
    try:
        cur.execute(sql)
        cols = [d[0] for d in (cur.description or [])]
        rows = [list(r) for r in cur.fetchmany(max_rows + 1)] if cols else []
    except Exception as e:
        print('⛔ Lỗi khi chạy truy vấn: %s' % e, file=sys.stderr)
        return 4
    finally:
        try:
            conn.rollback()
        finally:
            conn.close()

    truncated = len(rows) > max_rows
    rows = rows[:max_rows]
    if truncated and a.mode == 'aggregate':
        print('⛔ BỊ CHẶN: loại C trả quá %d nhóm — thu hẹp kỳ / bộ lọc' % MAX_GROUPS, file=sys.stderr)
        return 2
    masked = [] if a.no_mask else [i for i, c in enumerate(cols) if re.search(a.mask, c, re.I)]
    fps = [[fingerprint(r[i]) if i in masked and r[i] is not None else None for i in range(len(cols))] for r in rows]
    for r in rows:
        for i in masked:
            r[i] = shape(r[i])
    if truncated:
        warnings.append('kết quả bị cắt ở %d dòng — câu lọc chưa đủ hẹp' % max_rows)

    extra, changed, failed = [], {}, 0
    snap_dir = Path(a.root) / a.snap_dir
    if a.key and a.key not in cols:
        print('⛔ --key `%s` không có trong kết quả' % a.key, file=sys.stderr)
        return 3
    if a.diff:
        try:
            lines, changed, _, _ = diff_snapshot(snap_dir / ('%s.json' % a.diff), cols, rows, fps, a.key)
        except (OSError, ValueError) as e:
            print('⛔ Không so được với snapshot `%s`: %s' % (a.diff, e), file=sys.stderr)
            return 3
        extra += lines
    if a.snapshot:
        save_snapshot(snap_dir / ('%s.json' % a.snapshot), sql, cols, rows, fps)
        extra += ['', '> 📌 Đã lưu mốc `%s` — chạy lại câu này với `--diff %s` sau thao tác để so' % (a.snapshot, a.snapshot)]
    if a.expect:
        k = cols.index(a.key) if a.key else 0
        lines, failed = check_expect(json.loads(Path(a.expect).read_text(encoding='utf-8')), cols,
                                     [[plain(v) for v in r] for r in rows], changed, [str(plain(r[k])) for r in rows])
        extra += lines

    meta = {
        'TC ID': a.tc,
        'Thời điểm chạy': _dt.datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
        'Loại truy vấn': {'record': 'A · bản ghi', 'set': 'B · tập kết quả', 'aggregate': 'C · tổng hợp'}[a.mode],
        'Engine': engine,
        'CSDL': env.get('DB_NAME'),
        'Số dòng': '%d%s' % (len(rows), ' (đã cắt)' if truncated else ''),
        'Cột đã che': ', '.join(cols[i] for i in masked) or '—',
    }
    if a.expect:
        meta['Kết quả so kỳ vọng'] = '✅ khớp' if not failed else '❌ lệch %d mục' % failed
    if a.json:
        text = json.dumps({'meta': meta, 'sql': sql.strip(), 'warnings': warnings, 'columns': cols,
                           'rows': [[plain(v) for v in r] for r in rows],
                           'changed': ['%s.%s' % kc for kc in changed]}, ensure_ascii=False, indent=2)
    else:
        text = to_markdown(meta, cols, rows, sql, warnings, extra)
    if a.out:
        Path(a.out).parent.mkdir(parents=True, exist_ok=True)
        Path(a.out).write_text(text, encoding='utf-8')
        print('Đã ghi %s · %d dòng%s' % (a.out, len(rows), '' if not a.expect else ' · ' + meta['Kết quả so kỳ vọng']))
    else:
        sys.stdout.write(text)
    return 5 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
