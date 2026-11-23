# Module 01 — Đăng nhập (`LOGIN`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc

## `LOGIN` — Login / Forgot Password

| Mục | Giá trị |
|---|---|
| Route | `/admin/authentication` (truy cập `/admin/` khi chưa đăng nhập → chuyển về đây) · `/admin/authentication/logout` |
| Tiêu đề trang | `Perfex CRM \| Anh Tester Demo - Login` |
| Loại màn hình | Form |
| Phần tử quan sát | Email Address · Password · Remember me · nút Login · link Forgot Password? |
| Liên quan | Edit Profile có `Enable Email Two Factor Authentication` · `Enable Google Authenticator` (thuộc `PROF`) → luồng đăng nhập có thể có bước 2FA |
| CRUD | Không |
| Status flow | Không |
| Ước lượng | 4 phần tử form + luồng quên mật khẩu → 15–20 REQ |
| Risk | 🔴 — cửa vào mọi module, liên quan quyền và bảo mật tài khoản |

### Vùng chưa xác minh
- Message lỗi khi sai email/mật khẩu, khoá tài khoản sau N lần sai — chưa trigger (việc của recon module)
- Luồng Forgot Password — chưa mở
- Bước 2FA khi bật ở Edit Profile — chưa thấy
- Đăng nhập của cổng khách hàng là luồng khác — ngoài phạm vi đợt này

### Tài liệu có sẵn
`SRS_Login_Module.md` (gốc repo) và `docs/SRS_Login_Module.txt` — chưa nạp ở đợt khám phá (mode UI). Recon module này nên chạy HYBRID.

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [login_overview_viewport.png](../evidence/login_overview_viewport.png) | Trang đăng nhập — chụp trong browser context không cookie (không đăng xuất phiên đang dùng); viewport vì form nằm trọn trong màn hình |
