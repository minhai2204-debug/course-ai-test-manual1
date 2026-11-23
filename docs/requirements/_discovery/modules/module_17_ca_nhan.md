# Module 17 — Cá nhân (`PROF`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc

## `PROF` — My Profile · To Do · Reminders · Notifications · Newsfeed

| Mục | Giá trị |
|---|---|
| Route | My Profile `/admin/profile` · Edit Profile `/admin/staff/edit_profile` · To Do `/admin/todo` · Reminders `/admin/misc/reminders` · Đổi ngôn ngữ `/admin/staff/change_language/<ngôn-ngữ>` |
| Loại màn hình | Trang cá nhân + form |
| My Profile | 5 ô thời gian: Total · Last Month · This Month · Last Week · This Week Logged Time · Khối thông tin · Projects · Notifications (Mark all as read) · Export · Load More |
| Edit Profile — trường | `* First Name` · `* Last Name` · `* Email` · Phone · Default Language · Direction · Facebook · LinkedIn · Skype · Email Signature · `* Old password` · `* New password` · Repeat new password · Enable Email Two Factor Authentication · Enable Google Authenticator |
| To Do | "Unfinished to do's" · "Latest finished to do's" · New To Do · Load More (badge số ở header) |
| Reminders | Cột: Related to · Description · Date · Remind · Is notified? |
| Header | Newsfeed ("Share documents, ideas..") · Notifications · Language (26 ngôn ngữ + System Default) |
| Ước lượng | 15–20 REQ |
| Risk | 🟢 — riêng phần đổi mật khẩu và 2FA nên nâng 🟡 khi recon (bảo mật tài khoản, liên quan `LOGIN`) |

### Vùng chưa xác minh
- Đổi mật khẩu, bật 2FA, đổi ngôn ngữ — **không thử**: đổi trên tài khoản dùng chung sẽ ảnh hưởng người khác
- Newsfeed (đăng bài, đính kèm) — chưa mở

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [prof_overview_fullpage.png](../evidence/prof_overview_fullpage.png) | My Profile — ảnh có email và số điện thoại của tài khoản đang dùng; user chấp nhận giữ nguyên (02-11-2026) |
