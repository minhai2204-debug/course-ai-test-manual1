# Module 03 — Hàng hoá (`ITEM`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc

## `ITEM` — Items (Sales → Items)

| Mục | Giá trị |
|---|---|
| Route | `/admin/invoice_items` (tiêu đề trang: "Invoice Items") |
| Loại màn hình | Danh sách (tạo/sửa qua hộp thoại — chưa mở) |
| Thanh công cụ | New Item · Import Items · Groups · Export · Bulk Actions |
| Cột bảng | Description · Long Description · Rate · Tax 1 · Tax 2 · Unit · Group Name |
| Status flow | Không |
| Ước lượng | 7 cột + Groups + Import → 15–20 REQ |
| Risk | 🟡 — CRUD danh mục, nhưng là đầu vào của Proposal / Estimate / Invoice / Credit Note (giá, thuế) |

### Vùng chưa xác minh
- Form New Item, quản lý Groups, Import Items — chưa mở
- Danh sách thuế (Tax 1 / Tax 2) lấy từ Setup → Taxes (BLOCKED)

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [item_overview_fullpage.png](../evidence/item_overview_fullpage.png) | Danh sách Items |
