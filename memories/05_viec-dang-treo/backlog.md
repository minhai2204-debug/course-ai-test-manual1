---
name: backlog
description: Danh sách việc user đã nói "Để sau" hoặc còn chờ người khác — gom một chỗ để đề xuất bước kế tiếp
type: project
cập nhật: 20-11-2026
---

# Việc đang treo

Chi tiết từng module ở [[login]] và [[customers]]. File này chỉ gom **đầu việc** — xoá dòng khi đã làm, ghi ngày.

## Chờ user / PO / DBA cung cấp

| Việc | Mở khoá được gì |
|---|---|
| 2 tài khoản Project Manager trong `.env` | Chạy TC khoá tài khoản LOGIN (REQ-LOGIN-35 → 47) |
| Tài khoản test `TK-TEST-*`, Contact test, tài khoản role khác | TC sai mật khẩu, 2FA, phân quyền LOGIN/CUST |
| Hộp thư test | REQ-LOGIN-23/24 (email đặt lại mật khẩu) |
| Thông tin CSDL + biến `DB_*` (AMB-SYS-05) + cài Python | Chạy khối 🗄️ của TC `@DBCheck`, khảo sát `db_map.md` |
| URL + tài khoản cổng khách hàng | `/discover-system` mode ADD |
| Tài khoản vào được Setup / Staff | Recon `SETTING`, `STAFF` |

## User đã nói "Để sau" / chưa làm

- Commit các thư mục chưa theo dõi (`docs/testcases/`, `docs/requirements/customers/`, `memories/`, `.claude/`…) — xem [[nhanh-commit-va-don-worktree]].
- Merge nhánh Master Test Plan `claude/generate-master-test-plan-180f8e` (plan đã lạc hậu so với số liệu hiện tại).
- LOGIN: sinh lại test data JSON · `/review-testcases` FIX theo mục 6 của `run_1794989188` · 11 TC BLOCKED cần tester chạy tay hoặc Playwright MCP · xoá task sót `QA-LOGIN-TC034-TIMER` (id 2193).
- CUST: `/generate-traceability-matrix customers` — file chung `docs/traceability/traceability_matrix.md` đang xếp CUST vào 🕓.
- CUST: sinh TC Story 01, 03 → 07 · recon bổ sung vùng thiếu ảnh.
- Module kế tiếp theo thứ tự đã chốt: `ITEM` → `PRJ` → `TASK` …
- Dọn worktree còn sót trong `.claude/worktrees/`.
