# STORY-CUST-07 — Tab liên kết sang module khác

> ← [Index module `REQUIREMENTS_CUSTOMERS_SUMMARY.md`](../../REQUIREMENTS_CUSTOMERS_SUMMARY.md) · [File web](../requirements_customers_web.md)
>
> **Phạm vi:** 11 tab của hồ sơ KH chỉ **hiển thị danh sách chứng từ của module khác, lọc theo KH** và cung cấp nút tạo mới điền sẵn KH. Nghiệp vụ của từng chứng từ (tạo hoá đơn, báo giá…) thuộc module sở hữu (`INV`, `PAY`, `PROP`, `CRN`, `EST`, `SUBS`, `EXP`, `CTR`, `PRJ`, `TASK`, `TICK`) — **không** viết lại ở đây (chốt với user 16-11-2026: "Lõi + tab riêng").
> **REQ:** `REQ-CUST-105` → `REQ-CUST-115` (11 REQ) · **AMB:** — · **RISK:** —
>
> Mọi REQ trong file đo trên KH test chưa có chứng từ: bảng `No entries found`. Việc lọc đúng theo KH (chỉ chứng từ của KH này) **chưa kiểm** — sẽ kiểm khi recon từng module sở hữu, có dữ liệu thật.

## 1. Yêu cầu chức năng

| REQ ID | Tên yêu cầu | Mô tả | Acceptance Criteria | Trạng thái | Cập nhật lần cuối | Nguồn |
|---|---|---|---|---|---|---|
| REQ-CUST-105 | Tab Invoices liệt kê hoá đơn của KH, tạo mới điền sẵn KH | Liên kết `INV` | `?group=invoices` → nút `Create New Invoice` (→ `/admin/invoices/invoice?customer_id=<id>`), `Zip Invoices`, bộ chọn năm (mặc định năm hiện tại), `Export`; bảng cột `Invoice # · Amount · Total Tax · Date · Project · Tags · Due Date · Status` | 🟢 | — | UI thực tế (DOM) |
| REQ-CUST-106 | Tab Payments liệt kê thanh toán của KH | Liên kết `PAY` | `?group=payments` → `Zip Payments`, `Export` (không có nút tạo); bảng cột `Payment # · Invoice # · Payment Mode · Transaction ID · Amount · Date` | 🟢 | — | UI thực tế (DOM) |
| REQ-CUST-107 | Tab Proposals liệt kê đề xuất, tạo mới điền sẵn KH | Liên kết `PROP` | `?group=proposals` → `New Proposal` (→ `/admin/proposals/proposal?rel_type=customer&rel_id=<id>`), `Export`; bảng cột `Proposal # · Subject · Total · Date · Open Till · Tags · Date Created · Status` | 🟢 | — | UI thực tế (DOM) |
| REQ-CUST-108 | Tab Credit Notes liệt kê giấy báo có, tạo mới điền sẵn KH | Liên kết `CRN` | `?group=credit_notes` → `New Credit Note` (→ `/admin/credit_notes/credit_note?customer_id=<id>`), `Zip Credit Notes`, `Export`; bảng cột `Credit Note # · Credit Note Date · Status · Project · Reference # · Amount · Remaining Amount` | 🟢 | — | UI thực tế (DOM) |
| REQ-CUST-109 | Tab Estimates liệt kê báo giá, tạo mới điền sẵn KH | Liên kết `EST` | `?group=estimates` → `Create New Estimate` (→ `/admin/estimates/estimate?customer_id=<id>`), `Zip Estimates`, bộ chọn năm, `Export`; bảng cột `Estimate # · Amount · Total Tax · Project · Tags · Date · Expiry Date · Reference # · Status` | 🟢 | — | UI thực tế (DOM) |
| REQ-CUST-110 | Tab Subscriptions liệt kê gói định kỳ, tạo mới điền sẵn KH | Liên kết `SUBS` | `?group=subscriptions` → `New Subscription` (→ `/admin/subscriptions/create?customer_id=<id>`), `Export`; bảng cột `# · Subscription Name · Project · Status · Next Billing Cycle · Date Subscribed · Last Sent` | 🟢 | — | UI thực tế (DOM) |
| REQ-CUST-111 | Tab Expenses liệt kê chi phí, ghi chi phí điền sẵn KH | Liên kết `EXP` | `?group=expenses` → `Record Expense` (→ `/admin/expenses/expense?customer_id=<id>`), bộ chọn năm, `Export`; bảng cột `# · Category · Amount · Name · Receipt · Date · Project · Invoice · Reference # · Payment Mode` | 🟢 | — | UI thực tế (DOM) |
| REQ-CUST-112 | Tab Contracts liệt kê hợp đồng, tạo mới điền sẵn KH | Liên kết `CTR` | `?group=contracts` → `New Contract` (→ `/admin/contracts/contract?customer_id=<id>`), `Export`; bảng cột `# · Subject · Contract Type · Contract Value · Start Date · End Date · Project · Signature` | 🟢 | — | UI thực tế (DOM) |
| REQ-CUST-113 | Tab Projects liệt kê dự án, tạo mới điền sẵn KH | Liên kết `PRJ` | `?group=projects` → `New Project` (→ `/admin/projects/project?customer_id=<id>`), `Export`; bảng cột `# · Project Name · Tags · Start Date · Deadline · Members · Status` | 🟢 | — | UI thực tế (DOM) |
| REQ-CUST-114 | Tab Tasks liệt kê công việc liên kết KH | Liên kết `TASK` | `?group=tasks` → `New Task` (mở form task trên trang, `href="#"`), `Export`; bảng cột `# · Name · Status · Start Date · Due Date · Assigned to · Tags · Priority` | 🟢 | — | UI thực tế (DOM) |
| REQ-CUST-115 | Tab Tickets liệt kê ticket, tạo mới điền sẵn KH và contact chính | Liên kết `TICK` | `?group=tickets` → `New Ticket` (→ `/admin/tickets/add?contact_id=<contact chính>&userid=<id>`), `Export`; bảng cột `# · Subject · Tags · Department · Service · Contact · Status · Priority · Last Reply · Created` | 🟢 | — | UI thực tế (DOM) |
