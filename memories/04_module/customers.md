---
name: customers
description: Lịch sử và trạng thái module CUST (Customers · Contacts) — phạm vi recon, Story đã có TC, bản ghi test còn sót
type: project
cập nhật: 17-11-2026
---

# Module CUST (Customers · Contacts)

**Thư mục:** `customers/` · **Prefix:** `CUST` · **TC ID:** `CRM_CUST_TC_`
**Tài liệu:** [requirements](../../docs/requirements/customers/REQUIREMENTS_CUSTOMERS_SUMMARY.md) · [test cases](../../docs/testcases/customers/TEST_CASES_CUSTOMERS_SUMMARY.md) · bản Excel `docs/testcases/customers/web/test_cases_customers_web.xlsx`

## Dòng thời gian

| Ngày | Việc | Ghi chú cần nhớ |
|---|---|---|
| 16-11 | `/generate-requirements-from-website CUST` mode UI, phạm vi *Lõi + tab riêng* → 115 REQ, 7 Story | Được tạo + sửa + xoá bản ghi `auto_cust_<timestamp>` của mình. Xoá khách hàng bị bộ kiểm duyệt chặn → REQ xoá ⚪, 2 khách hàng test còn sót (xem [[moi-truong-crm-dung-chung]]) — user: *"Cứ để lại"*. Recon ở viewport 973×853 (AMB-CUST-16) |
| 16-11 | `/generate-testcases-manual-rbt module CUST story_02` — GỘP, Assumption tạm cho Q1–Q10 → **66 TC** cho STORY-CUST-02 | Rủi ro Cao, đủ 4 vòng. Q9 (đổi tiền tệ sau khi có giao dịch) và Q6 (xoá KH có hoá đơn) ⏭️ chuyển E2E khi có bộ `INV`. TC không kiểm bố cục theo vị trí; có 1 TC Responsive 1600 & 973 |
| 16-11 | Xuất Excel `test_cases_customers_web.xlsx` (thêm cột thứ 14), giữ `.md` gốc | Chưa commit |

## Việc còn dở

- Story 01, 03 → 07 chưa có TC → chế độ **bổ sung**, nối từ `CRM_CUST_TC_067`, ghi vào **cùng** `test_cases_customers_web.md`.
- 32 TC `@NeedsVerify`: nên recon bổ sung 3–4 vùng chưa có ảnh trước lần chạy đầu — tab Profile chế độ sửa · tab Customer Admins + modal Assign Admin · menu thả xuống cạnh tiêu đề (Delete) · phần dưới form tạo.
- 5 TC phân quyền BLOCKED (chờ tài khoản role khác — AMB-CUST-08) · 6 TC `@DBCheck` chờ kết nối CSDL (AMB-SYS-05).
- Toàn bộ `docs/requirements/customers/` và `docs/testcases/customers/` **chưa commit**.

Liên quan: [[quy-uoc-test-case]] · [[kiem-thu-csdl]] · [[backlog]]
