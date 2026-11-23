# scripts/db-check — truy vấn kiểm chứng CSDL chỉ đọc

Công cụ chạy khối `🗄️ Truy vấn kiểm chứng (chỉ SELECT):` của TC `@DBCheck` (skill [`skills-rbt-manual-testing`](../../.claude/skills/skills-rbt-manual-testing/SKILL.md) mục 3b) và khảo sát schema cho `_discovery/db_map.md`. Luật: [`.claude/rules/database_rules.md`](../../.claude/rules/database_rules.md). Không gắn với hệ thống nào.

| File | Chạy ở đâu | Làm gì |
|---|---|---|
| `db_check.py` | Python 3.9+. Chốt chặn **không cần thư viện ngoài**; chạy thật cần driver của engine | Chặn mọi câu không phải `SELECT` → chạy trong transaction read-only → lấy tối đa `--max-rows` dòng → che cột bí mật/cá nhân → xuất evidence Markdown/JSON · 3 loại truy vấn (`--mode`) · tham số `{{…}}` · so trước–sau (`--snapshot`/`--diff`) · tự chấm kỳ vọng (`--expect`) |
| `test_db_check.py` | `python -m unittest scripts/db-check/test_db_check.py` | Kiểm chốt chặn: câu được phép, câu bị chặn (kể cả mẹo né bằng comment / chuỗi), che giá trị · kiểm loại C (tổng hợp) · tham số · trước–sau · kỳ vọng — không cần CSDL |

## Cấu hình — `.env` ở gốc project

```dotenv
DB_ENGINE = mysql          # mysql (cả MariaDB) · postgres · mssql
DB_HOST = <host>
DB_PORT = <port>           # bỏ trống = mặc định của engine
DB_NAME = <tên CSDL>
DB_USER = <tài khoản — nên là tài khoản CHỈ ĐỌC do DBA cấp>
DB_PASSWORD = <mật khẩu>
# chỉ SQL Server:
DB_ODBC_DRIVER = ODBC Driver 18 for SQL Server
DB_ODBC_EXTRA = Encrypt=yes;
```

| Engine | Driver cần cài | Chế độ chỉ đọc phía phiên |
|---|---|---|
| `mysql` | `pip install pymysql` | `START TRANSACTION READ ONLY` + `MAX_EXECUTION_TIME` / `max_statement_time` |
| `postgres` | `pip install "psycopg[binary]"` (hoặc `psycopg2-binary`) | `default_transaction_read_only=on` + `statement_timeout` |
| `mssql` | `pip install pyodbc` + ODBC Driver | `ApplicationIntent=ReadOnly` — **không** có transaction read-only thật; chỉ dựa vào chốt chặn + `ROLLBACK` → càng cần tài khoản chỉ đọc |

Mọi lần chạy đều kết thúc bằng `ROLLBACK`.

## Lệnh

> Tên bảng / cột trong ví dụ chỉ để minh hoạ — dùng tên ở mục *Ánh xạ dữ liệu* của tài liệu requirements module.

```bash
# Chỉ kiểm câu lệnh (không kết nối) — dùng khi review TC / code
python scripts/db-check/db_check.py --check-only --sql "SELECT active FROM <bảng> WHERE email = 'auto_login_1731571200@auto.test' LIMIT 5"

# Chạy thật, ghi evidence cạnh ảnh của lần chạy
python scripts/db-check/db_check.py --tc CRM_LOGIN_TC_031 \
  --sql "SELECT active, last_login FROM <bảng> WHERE email = 'auto_login_1731571200@auto.test' LIMIT 5" \
  -o docs/executions/login/web/run_<timestamp>/evidence/CRM_LOGIN_TC_031_db.md

# Loại A · SỬA — chụp trước, sửa qua UI, so sau (chỉ cột được sửa được đổi)
python scripts/db-check/db_check.py --tc CRM_CUST_TC_031 --param ma=1532 --snapshot cust1532_truoc \
  --sql "SELECT id, company, phonenumber, address, datecreated FROM <bảng KH> WHERE id = {{ma}} LIMIT 1"
python scripts/db-check/db_check.py --tc CRM_CUST_TC_031 --param ma=1532 --diff cust1532_truoc --key id --expect ky_vong_tc031.json \
  --sql "SELECT id, company, phonenumber, address, datecreated FROM <bảng KH> WHERE id = {{ma}} LIMIT 1" \
  -o docs/executions/customers/web/run_<timestamp>/evidence/CRM_CUST_TC_031_db.md

# Loại B · TÌM KIẾM — tập bản ghi trong bộ dữ liệu đối soát của lượt chạy
python scripts/db-check/db_check.py --mode set --param run=auto_cust_1731650000 \
  --sql "SELECT id FROM <bảng KH> WHERE company LIKE CONCAT({{run}}, '%') AND company LIKE '%Hà Nội%' ORDER BY datecreated DESC LIMIT 50"

# Loại C · BÁO CÁO / DASHBOARD — chỉ trả số tổng hợp, ≤ 50 nhóm
python scripts/db-check/db_check.py --mode aggregate --param dau_ky=2026-11-01 --param dau_ky_sau=2026-12-01 \
  --sql "SELECT SUM(total) AS doanh_thu, COUNT(*) AS so_hoa_don FROM <bảng hoá đơn> WHERE status = 2 AND datepaid >= {{dau_ky}} AND datepaid < {{dau_ky_sau}}"

# Khảo sát schema cho db_map.md / mục Ánh xạ dữ liệu
python scripts/db-check/db_check.py --no-mask --max-rows 200 \
  --sql "SELECT table_name, column_name, data_type, is_nullable, column_default FROM information_schema.columns WHERE table_schema = '<tên CSDL>' AND table_name = '<bảng>'"
```

| Tham số | Nghĩa |
|---|---|
| `--sql` / `--file` | Đúng **một** câu `SELECT` / `WITH … SELECT` |
| `--mode` | Loại truy vấn (`database_rules.md` mục 2): `record` (A · bản ghi — mặc định) · `set` (B · tập kết quả — cảnh báo nếu thiếu `ORDER BY`) · `aggregate` (C · tổng hợp — mọi cột là `COUNT`/`SUM`/`AVG`/`MIN`/`MAX` hoặc cột `GROUP BY`, không `GROUP BY` cột cá nhân, không `WITH`, tối đa 50 nhóm) |
| `--param TEN=GIATRI` | Thay `{{TEN}}` trong câu bằng giá trị đã escape (số giữ nguyên, chuỗi bọc `'…'`). Lặp lại được. Thiếu tham số → bị chặn. Chốt chặn chạy **sau** khi thay, trên câu cuối cùng |
| `--snapshot TEN` · `--diff TEN` · `--key COT` | Lưu kết quả làm mốc *trước* vào `reports/db-check/snapshots/TEN.json` (đổi bằng `--snap-dir`) · chạy lại sau thao tác với `--diff TEN` → bảng ô đổi, dòng thêm / mất, ghép dòng theo `--key` (mặc định cột đầu). Cột bị che chỉ lưu **dấu vân tay** (12 ký tự sha256) — biết đổi hay không mà không lưu giá trị |
| `--expect FILE` | File JSON kỳ vọng — công cụ tự chấm, in bảng ✅/❌, lệch thì mã thoát `5`. Xem mẫu ngay dưới |
| `--tc` | TC ID ghi vào evidence |
| `--max-rows` | Mặc định `50`. Nhiều hơn → cắt và cảnh báo *"câu lọc chưa đủ hẹp"* |
| `--timeout` | Giây, mặc định và tối đa `30` |
| `--mask` | Regex tên cột cần che. Mặc định: `pass · pwd · hash · token · secret · salt · otp · api_key · session · cookie · email · phone · mobile · address` |
| `--no-mask` | Tắt che — **chỉ** cho truy vấn `information_schema` hoặc CSDL không có dữ liệu thật |
| `--check-only` | Chỉ chạy chốt chặn |
| `--json` | Xuất JSON (automation / script khác đọc) |
| `-o` | Ghi file thay vì in ra |

| Mã thoát | Nghĩa |
|---|---|
| `0` | Chạy được (hoặc qua chốt chặn với `--check-only`) |
| `2` | Câu lệnh bị chặn — lý do in ra stderr |
| `3` | Thiếu cấu hình, thiếu driver, không kết nối được |
| `4` | CSDL báo lỗi khi chạy (sai tên bảng/cột, hết thời gian) |
| `5` | Chạy được nhưng kết quả **lệch kỳ vọng** (`--expect`) |

### File kỳ vọng (`--expect`)

```json
{
  "row_count": 1,
  "unchanged_except": ["phonenumber", "updated_at"],
  "rows": [
    {
      "phonenumber": "0901234567",
      "company": {"unchanged": true},
      "updated_at": {"between": ["2026-11-15 09:00:00", "2026-11-15 09:05:00"]},
      "password": {"hash_prefix": "$2y$"},
      "last_login": {"not_null": true},
      "deleted_at": null
    }
  ]
}
```

| Khoá | Nghĩa |
|---|---|
| `row_count` | Số dòng trả về |
| `rows[n].<cột>` | Giá trị: chuỗi so nguyên văn (giữ số 0 đầu) · số so theo giá trị (`1000000` khớp `1000000.00`) · `null` · `{"not_null": true}` · `{"between": [a, b]}` · `{"starts_with": "…"}` · `{"hash_prefix": "$2y$"}` (cột bị che) · `{"changed": true}` / `{"unchanged": true}` (cần `--diff`) |
| `unchanged_except` | Cần `--diff`: ngoài các cột liệt kê, **không** cột nào được đổi — dùng cho TC sửa (nhóm D8) |

## Chốt chặn chặn gì

- Câu không bắt đầu bằng `SELECT` / `WITH` (cho phép `(` mở đầu cho `UNION`) · nhiều câu (`;` ở giữa)
- Từ khoá ghi / khoá ở giữa câu: `INSERT` `UPDATE` `DELETE` `MERGE` `INTO` (`SELECT … INTO`, `INTO OUTFILE`) `LOCK` `FOR UPDATE` `FOR SHARE` `PROCEDURE` `EXEC` `CALL` `WAITFOR` · gợi ý khoá của SQL Server (`UPDLOCK`, `XLOCK`, `HOLDLOCK`, `TABLOCK`…) · `OPENROWSET` / `OPENQUERY`
- Hàm có tác dụng phụ: `sleep` `benchmark` `get_lock` `load_file` `pg_sleep` `nextval` `setval` `set_config` `pg_terminate_backend` `pg_read_file` `lo_import` `dblink` `pg_advisory_*`…
- `SELECT *` / `bảng.*` · có `FROM` mà không có `WHERE`
- Comment thực thi được của MySQL (`/*! … */`, `/*+ … */`) · comment / chuỗi chưa đóng

Câu lệnh được tách token theo **cả ba** cú pháp MySQL · PostgreSQL · SQL Server (backslash trong chuỗi, `#`, `--`, `$$`, `[…]` khác nhau giữa engine) và chỉ qua khi **cả ba** cùng thấy một câu `SELECT` an toàn — để mẹo giấu lệnh trong chuỗi hay comment của engine này không lọt qua.

⚠️ **Giới hạn đã biết:** chốt chặn không biết hàm do người dùng tự định nghĩa trong CSDL có ghi dữ liệu hay không (`SELECT my_func()`). MySQL và PostgreSQL chặn thêm bằng transaction read-only; SQL Server thì không — đây là lý do phải xin **tài khoản chỉ đọc** ở phía DB.
