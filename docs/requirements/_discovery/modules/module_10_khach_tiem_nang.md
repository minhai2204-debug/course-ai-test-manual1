# Module 10 — Khách tiềm năng (`LEAD`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc

## `LEAD` — Leads

| Mục | Giá trị |
|---|---|
| Route | `/admin/leads` |
| Loại màn hình | Danh sách (chế độ Kanban — ❔ chưa quan sát) |
| Thanh công cụ | New Lead · Export · Bulk Actions |
| Cột bảng `#leads` | # · Name · Company · Email · Phone · Value · Tags · Assigned · Status · Source · Last Contact · Created |
| Status flow | Quan sát: Status **Customer · Active** (dropdown đổi trực tiếp trên dòng), Source **Facebook**; danh sách đầy đủ cấu hình ở Setup (BLOCKED) |
| Ước lượng | 12 cột + status flow → 30–40 REQ |
| Risk | 🟡 — dữ liệu liên hệ cá nhân; trạng thái `Customer` gợi ý lead đã được chuyển thành khách hàng (luồng chuyển ❔) |

### Vùng chưa xác minh
- Chuyển đổi Lead → Customer — ❔ chưa quan sát
- Màn chi tiết lead (thường là hộp thoại) — chưa mở
- Báo cáo Leads (`/admin/reports/leads`) thuộc `RPT`

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [lead_overview_fullpage.png](../evidence/lead_overview_fullpage.png) | Danh sách Leads |
