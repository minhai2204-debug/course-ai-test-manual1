# Module 18 — Cấu hình hệ thống (`SETTING`) — ⏸️ BLOCKED

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc

## `SETTING` — Setup

| Mục | Giá trị |
|---|---|
| Lý do BLOCKED | Tài khoản trong `.env` không được phép vào (user xác nhận 05-11-2026) — menu Setup (`#setup-menu`) **rỗng**, mọi route dưới đây → `/admin/access_denied` |
| Route đã thử (02-11-2026) | `/admin/settings` · `/admin/utilities/activity_log` · `/admin/emails` · `/admin/custom_fields` · `/admin/departments` · `/admin/currencies` · `/admin/taxes` · `/admin/paymentmodes` → **Access denied** · `/admin/modules` → chuyển về Dashboard |
| Nguồn route | Thử điều hướng trực tiếp (URL chỉ đọc). Route trả `access_denied` thay vì 404 → có tồn tại |
| Loại màn hình | ❔ chưa thấy UI |
| Ước lượng | ❔ |
| Risk | 🔴 — dữ liệu master (thuế, tiền tệ, phương thức thanh toán, phòng ban, custom field, mẫu email) được mọi module bán hàng / hỗ trợ dùng; Activity Log là nguồn kiểm Logging/Audit |

### Vùng chưa xác minh
Toàn bộ module — **route tồn tại nhưng bị chặn quyền**, chưa nhìn thấy nội dung. Danh sách route ở trên là các route đã thử, chưa chắc đủ toàn bộ khu Setup.

### Mở khoá
AMB-SYS-01 ✅ — tài khoản `.env` không được phép vào. Chỉ mở lại khi có tài khoản được phép: có account → chạy `/discover-system` mode ADD cho module này trước khi recon.

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [setting_access_denied_viewport.png](../evidence/setting_access_denied_viewport.png) | /admin/settings → trang Access denied; viewport vì trang chỉ có 1 thông báo |
