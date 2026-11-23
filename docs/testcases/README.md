# Danh mục Test Cases — Hệ thống CRM (Perfex CRM · khu admin)

> **Điểm vào cấp hệ thống cho test case.** Đọc file này trước khi sinh TC cho bất kỳ module nào: biết module nào đã có bộ TC, **prefix TC ID nào đã bị chiếm**, độ phủ REQ ra sao.
> Requirements tương ứng: [`../requirements/README.md`](../requirements/README.md)

## 1. Bảng danh mục module

| Module | Prefix TC ID | Nền tảng | Index | Số TC | Số part | Độ hạt | REQ bao phủ | Dải TC ID đã dùng | Cập nhật |
|---|---|---|---|---|---|---|---|---|---|
| Đăng nhập (Login / Forgot Password / Logout) | `CRM_LOGIN_TC_` | Web 84 | [`login/TEST_CASES_LOGIN_SUMMARY.md`](login/TEST_CASES_LOGIN_SUMMARY.md) | 84 (156 biến thể) | 1 | GỘP | REQ-LOGIN-01 → 47 (47/47) | 001 → 084 | 14-11-2026 |
| Khách hàng (Customers · Contacts) | `CRM_CUST_TC_` | Web 66 | [`customers/TEST_CASES_CUSTOMERS_SUMMARY.md`](customers/TEST_CASES_CUSTOMERS_SUMMARY.md) | 66 (81 biến thể + 16 mục bảng kiểm) | 1 | GỘP | REQ-CUST-28 → 52 (25/115 — chỉ STORY-CUST-02) | 001 → 066 | 16-11-2026 |

**Tổng: 2 module có bộ TC** — 150 TC.

### Prefix TC ID đã chiếm

`CRM_LOGIN_TC_` · `CRM_CUST_TC_` — trùng prefix REQ của `docs/requirements/README.md`. Module mới dùng `CRM_<PREFIX_REQ>_TC_`.

## 2. Độ phủ so với requirements

| Module | REQ trong requirements | REQ có TC | REQ ngoài phạm vi | REQ thiếu TC |
|---|---|---|---|---|
| `LOGIN` | 47 | 47 (Web) — 22 REQ ⚪ chưa kiểm chứng (15 theo Assumption tạm). REQ-LOGIN-35 → 47 cần tài khoản Project Manager mới chạy được | 0 | 0 |
| `CUST` | 115 | 25 (Web) — STORY-CUST-02. 5 TC phân quyền BLOCKED (chờ tài khoản role khác — AMB-CUST-08), 6 TC `@DBCheck` chờ kết nối CSDL (AMB-SYS-05) | 0 | 90 — Story 01, 03 → 07 chưa sinh (lượt sau: chế độ BỔ SUNG, từ `CRM_CUST_TC_067`) |

## 3. Cấu trúc thư mục chuẩn

```
docs/testcases/
├── README.md                                          ← DANH MỤC (file này)
└── <module>/
    ├── TEST_CASES_<TÊN_MODULE>_SUMMARY.md             ← INDEX — tên bất biến, không chứa dòng TC
    ├── web/ · mobile/ · api/                          ← tầng nền tảng (chỉ 3 tên này)
    │   └── test_cases_<module>_<nền-tảng>.md          ← MỘT file duy nhất mỗi nền tảng, mọi số lượng TC
    └── impact/                                        ← Mode DELTA
```

## 4. Kết quả thực thi

Kết quả chạy TC ghi ở `docs/executions/<module>/<nền-tảng>/` (do `/execute-test-cases` sinh). `LOGIN` web: 1 lần chạy — [`run_1794303621`](../executions/login/web/run_1794303621/execution_report.md).

## 5. Quy trình sử dụng

| Tình huống | Workflow |
|---|---|
| Sinh TC nhanh từ requirements đã rõ | `/generate-testcases-from-requirements` |
| Sinh TC theo quy trình RBT 6 bước | `/generate-testcases-manual-rbt` |
| Requirements đổi theo ticket — sửa TC đã có | `/update-testcases-from-impact` |
| Rà chất lượng bộ TC | `/review-testcases` |
| Chạy TC trên trình duyệt | `/execute-test-cases` |
| Ma trận truy vết REQ ↔ TC ↔ script | `/generate-traceability-matrix` |

## 6. Nhật ký danh mục

| Ngày | Thay đổi | Nguồn |
|---|---|---|
| 09-11-2026 | Khởi tạo danh mục | `/generate-testcases-from-requirements` |
| 09-11-2026 | `LOGIN`: sinh mới 55 TC web (`CRM_LOGIN_TC_001` → `055`), độ hạt GỘP, 2 part — phủ 34/34 REQ | `/generate-testcases-from-requirements` |
| 10-11-2026 | `LOGIN`: 55 → 59 TC · 125 → 129 biến thể (TC_056 → 059) — bổ sung vào danh mục ngày 11-11-2026, trước đó danh mục chưa được cập nhật | `/review-testcases` FIX · sửa theo `run_1794303621` |
| 11-11-2026 | `LOGIN`: đồng bộ theo ticket khoá tài khoản — sửa 6 TC (dữ liệu test / Pre-Condition), không thêm TC. Requirements lên 47 REQ → phủ 34/47 | `/update-testcases-from-impact` APPLY · [`delta_tc_LOGIN-LOCKOUT-11112026.md`](login/impact/delta_tc_LOGIN-LOCKOUT-11112026.md) |
| 11-11-2026 | `LOGIN`: sinh bổ sung 12 TC (`CRM_LOGIN_TC_060` → `071`) cho khoá tài khoản — Part 03 mới. 59 → 71 TC · 129 → 142 biến thể · phủ 47/47 REQ | `/generate-testcases-from-requirements` (BỔ SUNG) |
| 14-11-2026 | `LOGIN`: gộp 3 part web về một file [`login/web/test_cases_login_web.md`](login/web/test_cases_login_web.md) theo quy ước mới — mỗi nền tảng một file TC, không tách part. Không đổi TC nào (71 TC · 142 biến thể) | Gộp file theo skill rbt — Quy Tắc Xuất File mục 2 |
| 14-11-2026 | `LOGIN`: bổ sung 13 TC kiểm CSDL (`CRM_LOGIN_TC_072` → `084`, `@DBCheck`, chỉ SELECT) vào mục Vòng 3c của file web. 71 → 84 TC · 142 → 156 biến thể · vẫn phủ 47/47 REQ. Tên bảng/cột giữ chỗ — chờ kết nối CSDL (AMB-SYS-05) | `/generate-testcases-from-requirements` (BỔ SUNG) |
| 16-11-2026 | `CUST`: sinh mới 66 TC web (`CRM_CUST_TC_001` → `066`) cho STORY-CUST-02 — độ hạt GỘP, rủi ro Cao → Đầy đủ, phủ 25/25 REQ của Story (25/115 module). Prefix `CRM_CUST_TC_` được cấp | `/generate-testcases-manual-rbt` (FULL RBT) |
