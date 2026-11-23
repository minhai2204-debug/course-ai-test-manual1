"""Kiểm chốt chặn của db_check.py — không cần CSDL.

Chạy: python -m unittest scripts/db-check/test_db_check.py
"""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from db_check import (GuardError, _match, check_aggregate, check_expect, check_sql,  # noqa: E402
                      diff_snapshot, save_snapshot, shape, substitute_params)

ALLOWED = [
    "SELECT 1",
    "SELECT email, active FROM tblstaff WHERE email = 'auto_login_1731571200@auto.test' LIMIT 5",
    "select count(*) as n from tblclients where company = 'auto_cust_1' limit 1",
    "WITH c AS (SELECT id FROM t WHERE name = 'auto_x') SELECT id FROM c WHERE id > 0 LIMIT 5",
    "SELECT TOP 5 name FROM t WHERE name = N'auto_x'",
    "SELECT name FROM t WHERE name = 'auto_x' ORDER BY id FETCH FIRST 5 ROWS ONLY",
    "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'tblstaff'",
    "SELECT name FROM t WHERE note = 'đã xoá; DELETE FROM t' LIMIT 5",
    "SELECT a * b AS total FROM t WHERE id = 1 LIMIT 1",
    "SELECT name FROM t WHERE id = 1 LIMIT 1;",
    "(SELECT a FROM t WHERE id = 1) UNION (SELECT a FROM u WHERE id = 2)",
    "SELECT updated_at, description FROM t WHERE id = 1 LIMIT 1",
]

BLOCKED = {
    "DELETE FROM t WHERE id = 1": 'chỉ cho phép',
    "UPDATE t SET a = 1 WHERE id = 1": 'chỉ cho phép',
    "SHOW TABLES": 'chỉ cho phép',
    "SELECT 1; DELETE FROM t": 'MỘT câu',
    "WITH d AS (DELETE FROM t WHERE id = 1 RETURNING id) SELECT id FROM d WHERE id = 1": 'DELETE',
    "SELECT a INTO newtable FROM t WHERE id = 1": 'INTO',
    "SELECT a FROM t WHERE id = 1 INTO OUTFILE '/tmp/x'": 'INTO',
    "SELECT a FROM t WHERE id = 1 FOR UPDATE": 'UPDATE',
    "SELECT a FROM t WHERE id = 1 FOR SHARE": 'SHARE',
    "SELECT a FROM t WHERE id = 1 LOCK IN SHARE MODE": 'LOCK',
    "SELECT a FROM t WITH (UPDLOCK) WHERE id = 1": 'UPDLOCK',
    "SELECT pg_sleep(10)": 'pg_sleep'.upper(),
    "SELECT nextval('seq')": 'NEXTVAL',
    "SELECT * FROM t WHERE id = 1": 'SELECT *',
    "SELECT t.* FROM t WHERE id = 1": 'SELECT *',
    "SELECT a FROM t": 'WHERE',
    "SELECT a FROM t WHERE id = 1 /*! ; DELETE FROM t */": 'MySQL',
    # MySQL: '\'' là một chuỗi — phần sau là mã thật
    "SELECT '\\'' ; DELETE FROM t WHERE '1'": 'MỘT câu',
    # PostgreSQL: '\' kết thúc chuỗi — phần sau là mã thật
    "SELECT 'a\\' ; DELETE FROM t; --'": 'MỘT câu',
    # PostgreSQL: # là toán tử, không phải comment
    "SELECT 1 # 2\n; DELETE FROM t": 'MỘT câu',
    "SELECT a FROM t WHERE id = 1 /* chưa đóng": 'chưa đóng',
    "EXEC xp_cmdshell 'dir'": 'chỉ cho phép',
}


class GuardTest(unittest.TestCase):
    def test_allowed(self):
        for sql in ALLOWED:
            with self.subTest(sql=sql):
                check_sql(sql)

    def test_blocked(self):
        for sql, hint in BLOCKED.items():
            with self.subTest(sql=sql):
                with self.assertRaises(GuardError) as ctx:
                    check_sql(sql)
                self.assertIn(hint.lower(), str(ctx.exception).lower())

    def test_warn_without_limit(self):
        self.assertTrue(check_sql("SELECT a FROM t WHERE id = 1"))
        self.assertFalse(check_sql("SELECT a FROM t WHERE id = 1 LIMIT 1"))


class ShapeTest(unittest.TestCase):
    def test_shape(self):
        self.assertEqual(shape(None), 'NULL')
        self.assertEqual(shape('auto_login_1@auto.test'), 'auto_login_1@auto.test')
        self.assertIn('$2y$10$', shape('$2y$10$' + 'a' * 53))
        self.assertNotIn('nguyen', shape('nguyen.van.a@company.vn'))
        self.assertEqual(shape(3), 3)


AGG_ALLOWED = [
    "SELECT COUNT(*) AS n FROM tblinvoices WHERE status = 2",
    "SELECT SUM(total) AS doanh_thu, COUNT(*) so_hd FROM tblinvoices WHERE datepaid >= '2026-11-01' AND datepaid < '2026-12-01'",
    "SELECT status, COUNT(*) AS n FROM tblinvoices WHERE datecreated >= '2026-11-01' GROUP BY status",
    "SELECT i.status AS trang_thai, ROUND(SUM(i.total), 0) AS tong FROM tblinvoices i WHERE i.deleted = 0 GROUP BY i.status",
]

AGG_BLOCKED = {
    "SELECT id, total FROM tblinvoices WHERE status = 2": 'tổng hợp',
    "SELECT email, COUNT(*) FROM tblclients WHERE active = 1 GROUP BY email": 'cá nhân',
    "WITH x AS (SELECT total FROM t WHERE a = 1) SELECT SUM(total) FROM x WHERE total > 0": 'with',
}


class AggregateTest(unittest.TestCase):
    def test_allowed(self):
        for sql in AGG_ALLOWED:
            with self.subTest(sql=sql):
                check_sql(sql)
                check_aggregate(sql)

    def test_blocked(self):
        for sql, hint in AGG_BLOCKED.items():
            with self.subTest(sql=sql):
                with self.assertRaises(GuardError) as ctx:
                    check_aggregate(sql)
                self.assertIn(hint.lower(), str(ctx.exception).lower())


class ParamTest(unittest.TestCase):
    def test_substitute(self):
        out = substitute_params("SELECT a FROM t WHERE c = {{ten}} AND id = {{id}} LIMIT 1",
                                {'ten': "auto_o'neil", 'id': '42'}, 'postgres')
        self.assertEqual(out, "SELECT a FROM t WHERE c = 'auto_o''neil' AND id = 42 LIMIT 1")

    def test_injection_still_blocked(self):
        sql = substitute_params("SELECT a FROM t WHERE c = {{v}} LIMIT 1", {'v': "x\\'; DELETE FROM t; --"}, 'mysql')
        check_sql(sql)  # backslash đã được nhân đôi → cả chuỗi vẫn là một literal

    def test_missing(self):
        with self.assertRaises(GuardError):
            substitute_params("SELECT a FROM t WHERE c = {{v}}", {}, None)


class SnapshotExpectTest(unittest.TestCase):
    def test_diff_and_expect(self):
        cols = ['id', 'name', 'phone', 'password', 'updated_at']
        before = [[7, 'auto_cust_1', '0900000000', '<đã che · bắt đầu "$2y$10$" · 60 ký tự>', '2026-11-15 09:00:00']]
        after = [[7, 'auto_cust_1', '0901234567', '<đã che · bắt đầu "$2y$10$" · 60 ký tự>', '2026-11-15 09:05:00']]
        fps = [[None, None, None, 'aaaaaaaaaaaa', None]]
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'truoc.json'
            save_snapshot(p, 'SELECT 1', cols, before, fps)
            _, changed, added, removed = diff_snapshot(p, cols, after, fps, 'id')
        self.assertEqual(set(changed), {('7', 'phone'), ('7', 'updated_at')})
        self.assertEqual((added, removed), ([], []))
        spec = {'row_count': 1, 'unchanged_except': ['phone', 'updated_at'],
                'rows': [{'phone': '0901234567', 'name': {'unchanged': True}, 'password': {'hash_prefix': '$2y$'}}]}
        _, failed = check_expect(spec, cols, after, changed, ['7'])
        self.assertEqual(failed, 0)
        _, failed = check_expect({'rows': [{'phone': '901234567'}]}, cols, after, changed, ['7'])
        self.assertEqual(failed, 1)  # số 0 đầu số điện thoại không được mất

    def test_match(self):
        self.assertTrue(_match('1000000.00', 1000000))
        self.assertTrue(_match('2026-11-15 09:01:00', {'between': ['2026-11-15 09:00:00', '2026-11-15 09:02:00']}))
        self.assertTrue(_match(None, None))
        self.assertFalse(_match(None, {'not_null': True}))


if __name__ == '__main__':
    unittest.main()
