# Module 11 — Chi phí (`EXP`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc

## `EXP` — Expenses

| Mục | Giá trị |
|---|---|
| Route | `/admin/expenses` · Tạo mới `/admin/expenses/expense` |
| Loại màn hình | Danh sách + form |
| Thanh công cụ | Record Expense · Import Expenses · Export · Bulk Actions |
| Cột bảng `#expenses` | Category · Amount · Name · Receipt · Date · Project · Customer · Invoice · Reference # · Payment Mode |
| Status flow | Không có cột Status; cột `Invoice` cho thấy chi phí có thể được lập hoá đơn (❔ luồng chưa quan sát) |
| Ước lượng | 20–25 REQ |
| Risk | 🟡 — tiền nhưng không phải công nợ khách hàng; có upload Receipt |

### Vùng chưa xác minh
- Form Record Expense, upload receipt, Import — chưa mở
- Expense Category lấy từ Setup (BLOCKED)

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [exp_overview_fullpage.png](../evidence/exp_overview_fullpage.png) | Danh sách Expenses |
