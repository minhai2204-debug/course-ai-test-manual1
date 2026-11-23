# Module 07 — Thanh toán (`PAY`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc

## `PAY` — Payments

| Mục | Giá trị |
|---|---|
| Route | `/admin/payments` |
| Loại màn hình | Danh sách (không có nút tạo mới trên trang này) |
| Thanh công cụ | Export |
| Cột bảng | Payment # · Invoice # · Payment Mode · Transaction ID · Customer · Amount · Date |
| Status flow | Không có cột trạng thái |
| Ước lượng | 10–15 REQ |
| Risk | 🔴 — tiền; mỗi payment gắn với một Invoice (cột `Invoice #`) |

### Ranh giới đã chốt
Tách riêng khỏi `INV` (chốt với user 02-11-2026). Thanh toán được tạo từ Invoice (Record Payment / Batch Payments) — luồng tạo nằm ở `INV`, xem/sửa/xoá payment nằm ở đây.

### Vùng chưa xác minh
- Màn chi tiết payment (receipt, sửa, xoá) — chưa mở
- Payment Mode lấy từ Setup → Payment Modes (BLOCKED)

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [pay_overview_fullpage.png](../evidence/pay_overview_fullpage.png) | Danh sách Payments |
