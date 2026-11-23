# Ma Trận Truy Vết (RTM) — Perfex CRM (khu admin) · Tổng hợp

> **Tóm tắt:** 47/47 REQ trong phạm vi đã có TC (100%) · **0/84 TC có script automation** · 54/84 TC đã có kết quả (37 PASS · 6 FAIL · 11 BLOCKED) · 17/47 REQ chưa có TC nào được chạy · **chỉ 1/24 module** nằm trong RTM này — `CUST` có REQ + TC nhưng chưa sinh RTM, 22 module chưa khảo sát

| Thông tin | Nội dung |
|---|---|
| Ngày cập nhật | 18-11-2026 15:43 |
| Lần sinh gần nhất | `login` — sinh lại sau lần chạy `run_1794989188`; mục đích: báo cáo độ phủ trước release. Chưa có dòng module khác |
| Mốc git | `cb8ea3a` — từng module có mốc riêng ở Bản đồ tài liệu |
| Nguồn đã quét | Automation: không tìm thấy script · Checklist: `docs/checklists/login/web/checklist_regression_20261118.md` · Kết quả chạy: `docs/executions/login/web/` (2 lần chạy — `run_1794303621`, `run_1794989188`; lấy kết quả mới nhất của từng TC) · Bug: `docs/bugs/README.md` |

## ⬛ Ngoài tầm nhìn của RTM — đọc trước mọi con số

| Nhóm | Số module | Module | Ý nghĩa |
|---|:-:|---|---|
| ⬜ Chưa khảo sát | 22 | `ITEM` · `PRJ` · `TASK` · `PROP` · `EST` · `INV` · `PAY` · `CRN` · `CTR` · `LEAD` · `EXP` · `SUBS` · `TICK` · `EREQ` · `DASH` · `RPT` · `CAL` · `KBASE` · `UTIL` · `PROF` · `SETTING` ⏸️ · `STAFF` ⏸️ | Không có REQ — không xuất hiện trong mọi %. `SETTING`, `STAFF` hoãn vì tài khoản `.env` không được phép vào |
| 📄 Có REQ, chưa có TC | 0 | — | — |
| 🕓 Chưa sinh RTM | 1 | `CUST` (115 REQ · 66 TC) | Có REQ + TC nhưng chưa chạy `/generate-traceability-matrix customers` — 115/162 REQ toàn hệ thống (71%) nằm ngoài RTM này |

> Con số 100% bên dưới chỉ nói về `LOGIN` (47/162 REQ đã có của hệ thống, 1/24 module). **Không** dùng làm độ phủ của bản release nếu release gồm module khác.

## 1. Độ phủ theo module

| Module | REQ trong phạm vi | Requirement Coverage | TC | Automation | Lần chạy gần nhất |
|---|:-:|---|:-:|---|---|
| **Đăng nhập** `LOGIN` | 47 | `▰▰▰▰▰` 47/47 | 84 | `▱▱▱▱▱` 0/84 | `▰▰▰▱▱` 37 PASS · ❌ 6 FAIL · 🚫 11 BLOCKED · 30 TC chưa chạy |
| **Tổng** | **47** | `▰▰▰▰▰` **47/47** | **84** | `▱▱▱▱▱` **0/84** | 37 PASS · ❌ 6 FAIL · 🚫 11 BLOCKED · 30 TC chưa chạy |

## 2. Việc cần làm — gộp mọi module, xếp theo mức nghiêm trọng

| # | Việc | Module | Số lượng | Command |
|:-:|---|---|:-:|---|
| 1 | ❌ Retest TC FAIL đã có bug đang mở (`BUG_login_1794305372_TC050`) | `LOGIN` | 2 TC | `/retest-fixed-bugs` |
| 2 | ❌ Chạy lại TC FAIL theo Expected cũ (Expected đã sửa sau lần chạy, không phải lỗi) | `LOGIN` | 3 TC | `/execute-test-cases` |
| 3 | ❌ TC FAIL chưa có bug — trang 403 của máy chủ web, chờ DevOps / PO quyết | `LOGIN` | 1 TC | `/create-bug-report` hoặc `/review-testcases` |
| 4 | ▶️ Chạy TC chưa từng chạy — chờ tài khoản PM (12) · CSDL (13) · tài khoản test (5) | `LOGIN` | 30 TC | `/execute-test-cases` |
| 5 | 🚫 Chạy lại TC BLOCKED bằng tester / Playwright MCP (pane không làm được) | `LOGIN` | 11 TC | `/execute-test-cases` |
| 6 | 📝 Cập nhật Expected theo kết quả 18-11 (`419 Page Expired!`, cảnh báo timer, gỡ `@NeedsVerify`) | `LOGIN` | 6 TC | `/review-testcases` |
| 7 | 🕓 Sinh RTM cho module đã có REQ + TC | `CUST` | 1 module | `/generate-traceability-matrix customers` |
| 8 | 🟡 Automate TC Critical/High đã chấm `Automation = Yes` | `LOGIN` | 35 TC | `/generate-automation-from-testcases` |

## Bản đồ tài liệu

| Module | File RTM | Ngày sinh | Mốc git |
|---|---|---|---|
| `LOGIN` | [login/traceability_matrix_login.md](login/traceability_matrix_login.md) | 18-11-2026 15:43 | `cb8ea3a` (TC, checklist, kết quả chạy chưa commit) |
| `CUST` | — chưa sinh | — | — |
