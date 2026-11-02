# Module 06 — Hoá đơn (`INV`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc

## `INV` — Invoices

| Mục | Giá trị |
|---|---|
| Route | `/admin/invoices` · `/admin/invoices/list_invoices` · Xem `/admin/invoices/list_invoices/{id}` · Tạo mới `/admin/invoices/invoice` |
| Loại màn hình | Danh sách + form + màn xem chứng từ |
| Thanh công cụ | Create New Invoice · Batch Payments · Recurring Invoices · Filter by status · Export |
| Cột bảng `#invoices` | Invoice # · Amount · Total Tax · Date · Customer · Project · Tags · Due Date · Status |
| Status flow | 6 trạng thái (widget "Invoice overview" của Dashboard): **Draft · Not Sent · Unpaid · Partially Paid · Overdue · Paid**; bảng danh sách thấy Paid · Partially Paid · Unpaid |
| Tính năng phụ | Recurring Invoices (hoá đơn định kỳ) · Batch Payments (ghi nhận thanh toán hàng loạt → tạo bản ghi `PAY`) |
| Ước lượng | 35–45 REQ |
| Risk | 🔴 — tiền, thuế, công nợ; Payments và Credit Notes phụ thuộc |

### Vùng chưa xác minh
- Form tạo hoá đơn, Recurring Invoices, Batch Payments — chưa mở (Batch Payments là thao tác ghi — chỉ mở xem ở môi trường dùng chung)
- Trạng thái **Cancelled**: báo cáo Sales ghi "Cancelled invoices are excluded from the report" nhưng widget Dashboard không có Cancelled — kiểm ở recon xem Cancelled có phải trạng thái thứ 7
- Thuế, tiền tệ, phương thức thanh toán lấy từ Setup (BLOCKED)

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [inv_overview_fullpage.png](../evidence/inv_overview_fullpage.png) | Danh sách Invoices |
