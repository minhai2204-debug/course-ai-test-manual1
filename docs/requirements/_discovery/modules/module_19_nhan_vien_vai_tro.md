# Module 19 — Nhân viên & Vai trò (`STAFF`) — ⏸️ BLOCKED

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc

## `STAFF` — Staff · Roles

| Mục | Giá trị |
|---|---|
| Lý do BLOCKED | Tài khoản trong `.env` không được phép vào (user xác nhận 05-11-2026), đo được `Access denied` |
| Route đã thử (02-11-2026) | `/admin/staff` · `/admin/roles` → **Access denied** |
| Nguồn route | Thử điều hướng trực tiếp (URL chỉ đọc). Route trả `access_denied` thay vì 404 → có tồn tại |
| Dấu vết gián tiếp | Cột "Members" (Projects), "Assigned to" (Tasks), "Assigned" (Leads, Estimate Request), "Staff Member" (Timesheets) → nhân viên là entity được nhiều module tham chiếu |
| Loại màn hình | ❔ chưa thấy UI |
| Ước lượng | ❔ |
| Risk | 🔴 — quản lý tài khoản và quyền; quyết định ma trận phân quyền của mọi module (tạm thời chỉ có role admin — AMB-SYS-02 ✅) |

### Vùng chưa xác minh
Toàn bộ module, kể cả danh sách role của hệ thống.

### Mở khoá
AMB-SYS-01 ✅ — tài khoản `.env` không được phép vào. Chỉ mở lại khi có tài khoản được phép: có account → chạy `/discover-system` mode ADD cho module này.

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [staff_access_denied_viewport.png](../evidence/staff_access_denied_viewport.png) | /admin/staff → trang Access denied; viewport vì trang chỉ có 1 thông báo |
