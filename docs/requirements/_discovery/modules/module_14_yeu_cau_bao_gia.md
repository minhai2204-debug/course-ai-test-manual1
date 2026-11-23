# Module 14 — Yêu cầu báo giá (`EREQ`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc

## `EREQ` — Estimate Request

| Mục | Giá trị |
|---|---|
| Route | `/admin/estimate_request` |
| Loại màn hình | Danh sách yêu cầu + quản lý Form |
| Thanh công cụ | New Form · Export |
| Cột bảng `#table-estimate-request` | # · Email · Tags · Assigned · Status · Created |
| Status flow | Có cột Status — danh sách giá trị chốt ở recon |
| Dữ liệu | **0 bản ghi** ("No entries found") |
| Ước lượng | 10–15 REQ |
| Risk | 🟢 — tiếp nhận yêu cầu, ít phụ thuộc |

### Vùng chưa xác minh
- Trình dựng form (New Form) và form công khai mà người ngoài điền — chưa mở
- Quan hệ với `EST` (chuyển yêu cầu thành báo giá) — ❔

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [ereq_overview_fullpage.png](../evidence/ereq_overview_fullpage.png) | Danh sách Estimate Request — rỗng |
