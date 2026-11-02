# Module 12 — Gói định kỳ (`SUBS`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc

## `SUBS` — Subscriptions

| Mục | Giá trị |
|---|---|
| Route | `/admin/subscriptions` · Tạo mới `/admin/subscriptions/create` |
| Loại màn hình | Danh sách + form |
| Thanh công cụ | New Subscription · Export |
| Cột bảng `#subscriptions` | # · Subscription Name · Customer · Project · Status · Next Billing Cycle · Date Subscribed · Last Sent |
| Status flow | 8 trạng thái ở "Subscriptions Summary": **Not Subscribed · Active · Future · Past Due · Unpaid · Incomplete · Canceled · Incomplete Expired** |
| Dữ liệu | **0 bản ghi** ("No entries found") |
| Ước lượng | 15–20 REQ |
| Risk | 🟡 — status flow 8 trạng thái; tên trạng thái giống mô hình của cổng thanh toán — khối Summary có logo **stripe**: tích hợp Stripe đã quan sát được |

### Vùng chưa xác minh
- Không có bản ghi → chưa thấy màn chi tiết
- Hành vi tích hợp Stripe (tạo subscription, đồng bộ trạng thái) — chưa xác minh, phụ thuộc AMB-SYS-04

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [subs_overview_fullpage.png](../evidence/subs_overview_fullpage.png) | Danh sách Subscriptions — rỗng, Summary có logo stripe |
