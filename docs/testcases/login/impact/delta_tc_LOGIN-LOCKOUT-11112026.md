# Delta TC List — LOGIN-LOCKOUT-11112026 · module `login`

| Mục | Giá trị |
|---|---|
| Ticket | Khoá tài khoản khi đăng nhập sai nhiều lần — mã nội bộ `LOGIN-LOCKOUT-11112026` (ticket không mang mã) |
| Ngày áp | 11-11-2026 |
| Impact Report nguồn | [`impact_LOGIN-LOCKOUT-11112026.md`](../../../requirements/login/impact/impact_LOGIN-LOCKOUT-11112026.md) · [`impact_LOGIN-ASSUMPTIONS-11112026.md`](../../../requirements/login/impact/impact_LOGIN-ASSUMPTIONS-11112026.md) (chốt Assumption tạm cho AMB của chính ticket này) |
| Kế hoạch đã duyệt | [`impact_plan_LOGIN-LOCKOUT-11112026.md`](impact_plan_LOGIN-LOCKOUT-11112026.md) — user duyệt 11-11-2026, giữ `TK-TEST-01` cho TC_018 |
| Mốc git trước khi sửa | web → `web/parts/part_01_web_chuc_nang.md` · `web/parts/part_02_web_ky_thuat_phi_chuc_nang.md` @ **chưa có trong git** (`docs/testcases/` chưa được theo dõi) — không chạy được `git diff`; cột *Đổi cái gì* ghi đủ ô đã đổi |
| Trạng thái | ⚠️ CÒN VIỆC NGOÀI PHẠM VI |

## TC đã xử lý

| TC ID | Nền tảng | Vòng · Nhánh | Hành động đã làm | Đổi cái gì (cho automation) |
|---|---|---|---|---|
| CRM_LOGIN_TC_018 | web | V2 · Validation (Password) · Business Rule | ✏️ Đã sửa | **Pre-Condition:** trước bước 1, đăng nhập đúng `TK-TEST-01` rồi Logout để đưa bộ đếm lần sai về 0 (REQ-LOGIN-39) → script thêm bước setup này. Cấm thêm biến thể thứ 5 → data-driven giữ đúng 4 dòng `a`–`d`. **Bước 6** (dọn dẹp, không chấm): đăng nhập đúng để đưa bộ đếm về 0 — dự kiến vào Dashboard. Assertion của bước 1–5 không đổi |
| CRM_LOGIN_TC_017 | web | V2 · EP / BVA (Password) | ✏️ Đã sửa | Test Data: mỗi biến thể một email riêng `recon.khongtontai.tc017{a…f}@example.invalid` (trước: chung `recon.khongtontai@example.invalid`). Assertion không đổi. File dữ liệu automation [`web/test_data_login_web.json`](../web/test_data_login_web.json) (`BND_08`, `EDGE_02 → 04`…) **đã** dùng email riêng `auto_tc017*` → không cần sửa dữ liệu script |
| CRM_LOGIN_TC_047 | web | V3 · Security (SQLi/XSS Password) | ✏️ Đã sửa | Test Data: mỗi biến thể một email riêng `recon.khongtontai.tc047{a…e}@example.invalid`. Assertion không đổi. `test_data_login_web.json` (`EDGE_08 → 12`) đã dùng `auto_tc047*` riêng → không cần sửa |
| CRM_LOGIN_TC_013 | web | V2 · Validation · EP (Email) | ✏️ Đã sửa | Test Data biến thể `a`, `c`, `e`: email riêng của TC `recon.khongtontai.tc013@example.invalid` (và dạng viết hoa / có khoảng trắng của chính email đó). Assertion không đổi. `test_data_login_web.json` đã dùng `auto_tc013*` → không cần sửa |
| CRM_LOGIN_TC_039 | web | V2 · Use Case | ✏️ Đã sửa | Bước 2, 6 + Test Data: `recon.khongtontai.tc039@example.invalid`. Assertion không đổi. ⚠️ `test_data_login_web.json` dòng `NEG_13` (`tcRef` gồm TC_039) và `NEG_31` dùng chung email với TC_013-a / TC_024-a — xem lại khi chạy song song |
| CRM_LOGIN_TC_056 | web | V2 · Error Guessing | ✏️ Đã sửa | Bước 2 + Test Data: `recon.khongtontai.tc056@example.invalid`. Assertion không đổi |

> Quy ước chung của Part 01 cũng đổi: mỗi TC một email riêng; TC gửi sai từ 4 lần trở lên/lượt dùng email riêng cho từng biến thể; không bao giờ gửi mật khẩu sai cho email admin. Đây là luật chung cho data automation.

**Đã rà, không sửa** (automation không cần chạm): TC_009, 021 (chỉ gửi Password trống — không tính là lần sai, REQ-LOGIN-44) · TC_010 · TC_014, 046, 059 · TC_027 · TC_042 · TC_043, 058 — lý do ở kế hoạch mục 2.

## Ngoài phạm vi

| REQ | Việc còn lại | Command |
|---|---|---|
| REQ-LOGIN-35 → 47 (STORY-LOGIN-06) | 13 REQ mới chưa có TC. Sinh ở chế độ BỔ SUNG, TC ID từ `CRM_LOGIN_TC_060`, độ hạt GỘP, tài khoản Project Manager, nhóm chạy tuần tự, nên mở `web/parts/part_03_web_khoa_tai_khoan.md` | `/generate-testcases-from-requirements` |
| *PM × đăng nhập / đăng xuất* (V3 · Permission 🟡) | Chưa có REQ — bổ sung REQ trước rồi viết TC | `/update-requirements-from-ticket` |
| Tài khoản Project Manager | 2 tài khoản chỉ dành cho kiểm thử, lưu ở `.env` — chặn mọi TC của Story 06 | Người quản trị hệ thống |

## Nhật ký

| Ngày | Thay đổi |
|---|---|
| 11-11-2026 | Áp lần đầu theo `impact_plan_LOGIN-LOCKOUT-11112026.md` đã duyệt |
