# Module 02 — Khách hàng (`CUST`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc

## `CUST` — Customers (gồm Contacts)

| Mục | Giá trị |
|---|---|
| Route | Danh sách `/admin/clients` · Tạo mới `/admin/clients/client` · Chi tiết `/admin/clients/client/{id}?group=<tab>` |
| Loại màn hình | Danh sách + màn chi tiết nhiều tab |
| Thanh công cụ | New Customer · Import Customers · Contacts · Export · Bulk Actions · bộ lọc lưu được (New Filter / Clear Filter / Edit) |
| Cột bảng `#clients` | # · Company · Primary Contact · Primary Email · Phone · Active · Groups · Date Created (25 dòng/trang mặc định) |
| Khối summary | "Customers Summary" — 6 bộ đếm: Total Customers · Active Customers · Inactive Customers · Active Contacts · Inactive Contacts · Contacts Logged In Today (giá trị biến động, không ghi) |
| Status flow | Cờ `Active` (bật/tắt) — không phải chuỗi trạng thái |
| Tab chi tiết (19) | Profile · Contacts · Notes · Statement · Invoices · Payments · Proposals · Credit Notes · Estimates · Subscriptions · Expenses · Contracts · Projects · Tasks · Tickets · Files · Vault · Reminders · Map |
| Tab con trong Profile (3) | Customer Details · Billing & Shipping · Customer Admins |
| Ước lượng | 19 tab + form 3 tab con + Contacts + Import → 60–80 REQ |
| Risk | 🔴 — dữ liệu khách hàng, entity trung tâm (≥ 12 module tham chiếu), Vault chứa thông tin nhạy cảm |

### Ranh giới đã chốt
Contacts **gộp** vào `CUST` (chốt với user 02-11-2026). Đăng nhập của contact thuộc cổng khách hàng — ngoài phạm vi.

### Phát hiện tầng network
- `POST /admin/clients/table` → 200 — DataTables server-side cho bảng danh sách
- Link trong bảng: `/admin/clients/client/{id}?contactid={id}` và `?group=contacts`

### Vùng chưa xác minh
- Hầu hết tab chỉ đọc được tên; nội dung từng tab — việc của recon module
- Bộ lọc nâng cao (phone, active state, invoice, estimates, proposals, projects, contract type, city, zip code…) — chỉ thấy tên
- Import Customers — chưa mở
- Môi trường có ~2.800 khách hàng do người khác tạo → không dựa vào bản ghi cụ thể làm dữ liệu kiểm thử

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [cust_overview_fullpage.png](../evidence/cust_overview_fullpage.png) | Danh sách Customers + Customers Summary |
