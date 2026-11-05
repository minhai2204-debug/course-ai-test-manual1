# Module 13 — Hỗ trợ (`TICK`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc

## `TICK` — Support (Support Tickets)

| Mục | Giá trị |
|---|---|
| Route | `/admin/tickets` · Tạo mới `/admin/tickets/add` |
| Loại màn hình | Danh sách + form |
| Thanh công cụ | New Ticket · Export · Bulk Actions |
| Cột bảng `#tickets` | # · Subject · Tags · Department · Service · Contact · Status · Priority · Last Reply · Created |
| Status flow | 5 trạng thái ở "Tickets Summary": **Open · In Progress · Answered · On Hold · Closed** + cột Priority |
| Dữ liệu | **0 bản ghi** (02-11-2026) — được tạo dữ liệu thử khi recon (AMB-SYS-03 ✅) |
| Ước lượng | 25–35 REQ |
| Risk | 🟡 — status flow 5 trạng thái, gắn với Contact; chưa thấy màn chi tiết |

### Vùng chưa xác minh
- Màn chi tiết ticket (reply, đổi trạng thái, gán) — **chưa xem được vì không có bản ghi**; tạo ticket thử khi recon
- Department · Service · Priority · Predefined Replies cấu hình ở Setup (BLOCKED)

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [tick_overview_fullpage.png](../evidence/tick_overview_fullpage.png) | Danh sách Tickets — rỗng + Tickets Summary |
