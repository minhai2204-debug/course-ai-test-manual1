# Module 08 — Giấy báo có (`CRN`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc

## `CRN` — Credit Notes

| Mục | Giá trị |
|---|---|
| Route | `/admin/credit_notes` · Tạo mới `/admin/credit_notes/credit_note` |
| Loại màn hình | Danh sách + form |
| Thanh công cụ | New Credit Note · Export |
| Cột bảng `#credit_notes` | Credit Note # · Credit Note Date · Customer · Status · Project · Reference # · Amount · Remaining Amount |
| Status flow | Có cột Status — danh sách giá trị chốt ở recon |
| Dữ liệu | **0 bản ghi** ("No entries found") |
| Ước lượng | 20–25 REQ |
| Risk | 🔴 — tiền; cột `Remaining Amount` cho thấy credit được trừ dần (nghi áp vào Invoice — ❔ chưa quan sát) |

### Vùng chưa xác minh
- Luồng áp credit vào hoá đơn, hoàn tiền — chưa quan sát
- Form tạo mới — chưa mở

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [crn_overview_fullpage.png](../evidence/crn_overview_fullpage.png) | Danh sách Credit Notes — rỗng |
