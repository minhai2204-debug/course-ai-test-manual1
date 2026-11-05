# Requirements — Đăng nhập (`LOGIN`)

> **INDEX module — tên file bất biến.** Phần dùng chung · phân quyền · trạng thái phiên · AMB/RISK · phân rã Story · Nhật ký. REQ chi tiết của từng nền tảng nằm ở file nền tảng (xem **Bản đồ tài liệu**).
> ← [Danh mục hệ thống](../README.md) · [Bản đồ khám phá — module 01](../_discovery/modules/module_01_dang_nhap.md)

## 1. Metadata & Tổng quan

| Thuộc tính | Giá trị |
|---|---|
| **Module** | Đăng nhập khu admin — Login · Forgot Password · Logout |
| **Prefix** | `LOGIN` (cấp bởi `/discover-system` 02-11-2026) |
| **Hệ thống** | `CRM` — Perfex CRM 3.1.6, khu admin `/admin/*` |
| **Nền tảng** | Web ✅ · Android — chưa có · iOS — chưa có · API — chưa có |
| **Dải mã đã dùng** | `REQ-LOGIN-01` → `REQ-LOGIN-34` · `AMB-LOGIN-01` → `AMB-LOGIN-18` · `RISK-LOGIN-01` → `RISK-LOGIN-06` (đợt 1: UI recon 02-11-2026, 01 → 28 · đợt 2: Assumption tạm do user chốt 05-11-2026, 29 → 34) |
| **Mã kế tiếp** | Đợt phân tích sau bắt đầu từ `REQ-LOGIN-35` · `AMB-LOGIN-19` · `RISK-LOGIN-07` — **KHÔNG đánh lại từ 01** |
| **Nguồn** | Khảo sát UI thực tế (mode UI theo chỉ định của user — không dùng tài liệu) · trả lời của user cho AMB-LOGIN-01 (05-11-2026) |
| **Môi trường** | 🔒 Dùng chung — không đăng nhập sai bằng email thật (tránh khoá tài khoản chung), không gửi email đặt lại tới hộp thư thật |
| **Ngày khảo sát** | 02-11-2026 |

**Mục đích:** cổng vào khu quản trị. Người dùng nội bộ đăng nhập bằng email + mật khẩu, có tuỳ chọn ghi nhớ đăng nhập, có luồng yêu cầu đặt lại mật khẩu, và đăng xuất từ menu avatar.

**Trong phạm vi:** trang `/admin/authentication` · trang `/admin/authentication/forgot_password` · điều hướng bảo vệ route admin (chưa đăng nhập / đã đăng nhập) · cookie ghi nhớ đăng nhập · đăng xuất.

**Ngoài phạm vi:** cổng khách hàng (`/clients/*` — URL/tài khoản khác, khảo sát sau) · màn đặt mật khẩu mới qua link email (cần token — xem `REQ-LOGIN-24` ⚪) · cấu hình 2FA ở Edit Profile (module `PROF`) · cấu hình chính sách đăng nhập ở Setup (module `SETTING`, BLOCKED).

### Bản đồ phủ tài liệu

Không có tài liệu — toàn bộ REQ sinh từ khảo sát UI thực tế. Repo có `SRS_Login_Module.md` trong lịch sử git nhưng **không dùng** theo chỉ định của user (02-11-2026).

## Bản đồ tài liệu

| Nền tảng | File | Story | REQ bao phủ |
|---|---|---|---|
| Chung ≥ 2 nền tảng | chính file này | — | Không có — module mới có một nền tảng |
| Web | [web/requirements_login_web.md](web/requirements_login_web.md) | STORY-LOGIN-01 → 05 | `REQ-LOGIN-01` → `REQ-LOGIN-34` |

**Tổng: 34 REQ** = 0 ở index + 34 ở `web/`.

## 2. Yêu cầu dùng chung nhiều nền tảng

Không áp dụng — module mới khảo sát trên Web. Khi khảo sát app/API, rule trùng sẽ được chuyển lên đây (giữ nguyên mã, mở rộng cột `Nền tảng`).

## 3. Ma trận Phân quyền

| Hành động | Admin (tài khoản `.env`) | Super Admin | Nhân viên role khác | Contact khách hàng |
|---|---|---|---|---|
| Đăng nhập vào khu admin | ✅ | — | — | ❔ |
| Yêu cầu đặt lại mật khẩu (email tồn tại) | ❔ | — | — | ❔ |
| Đăng xuất | ✅ | — | — | ❔ |

Tổng 12 ô = Đã kiểm chứng 2 · Suy diễn 0 · Chưa rõ 4 · Không áp dụng 6.
Ô "không áp dụng" là toàn bộ cột Super Admin và Nhân viên role khác (6 ô) — User xác nhận 05-11-2026: tạm thời hệ thống chỉ có role admin (AMB-LOGIN-01, AMB-LOGIN-02). Có thêm role thì phải mở lại hai cột này. Ô [Yêu cầu đặt lại mật khẩu × Admin] là ❔ vì cố ý không gửi email đặt lại tới hộp thư thật của tài khoản dùng chung (AMB-LOGIN-13). Contact khách hàng chưa có account: test theo Assumption tạm "không đăng nhập được" (AMB-LOGIN-03 ⏭️, REQ-LOGIN-29 ⚪), ô ma trận **giữ ❔** vì chưa kiểm chứng.

## 4. Ma trận Trạng thái phiên

Không có entity mang status flow. Bảng dưới mô tả **trạng thái phiên đăng nhập** quan sát được trên Web:

| Trạng thái hiện tại | Hành động | Trạng thái kế tiếp | REQ |
|---|---|---|---|
| Chưa đăng nhập | Mở route admin bất kỳ | Chưa đăng nhập — đứng ở trang Login | REQ-LOGIN-11 |
| Chưa đăng nhập | Đăng nhập đúng | Đã đăng nhập — Dashboard `/admin/` | REQ-LOGIN-09, 10 |
| Chưa đăng nhập | Đăng nhập sai / bỏ trống | Chưa đăng nhập — trang Login kèm thông báo | REQ-LOGIN-05 → 08 |
| Đã đăng nhập | Mở trang Login hoặc Forgot Password | Đã đăng nhập — Dashboard `/admin/` | REQ-LOGIN-12, 13 |
| Đã đăng nhập | Logout | Chưa đăng nhập — trang Login | REQ-LOGIN-26, 27 |
| Đã đăng nhập (có ghi nhớ) | Logout | Chưa đăng nhập — cookie ghi nhớ còn sót nhưng không khôi phục phiên | REQ-LOGIN-28 |
| Đã đăng nhập (có timer đang chạy) | Logout | Đã đăng nhập — popup cảnh báo (⚪ theo Assumption tạm) | REQ-LOGIN-34 |

## 5. Điểm Mơ Hồ & Rủi Ro

### Ambiguities

| Mã | Câu hỏi | Nguy cơ | Mức độ | Assumption tạm | Trạng thái | Kết luận |
|---|---|---|---|---|---|---|
| AMB-LOGIN-01 | Xin account Super Admin để kiểm chứng 3 ô phân quyền đang ❔ (gắn AMB-SYS-01) | Không biết Super Admin có luồng đăng nhập khác (VD bắt buộc 2FA) | 🔴 | Giống Admin | ✅ Đã trả lời 05-11-2026 | User xác nhận 05-11-2026: tạm thời hệ thống chỉ có role admin — không có role Super Admin riêng, cột Super Admin thành không áp dụng. Kết luận mang tính tạm thời: có thêm role thì mở lại. Việc tài khoản admin vẫn bị chặn ở khu Setup tách sang AMB-SYS-01 |
| AMB-LOGIN-02 | Xin account nhân viên role khác để kiểm chứng 3 ô phân quyền (gắn AMB-SYS-02) | Không biết nhân viên bị vô hiệu / role hạn chế có đăng nhập được không | 🔴 | Đăng nhập được, vào Dashboard | ✅ Đã trả lời 05-11-2026 | Cùng câu trả lời với AMB-LOGIN-01: chưa có role nhân viên nào khác, cột này thành không áp dụng. Có thêm role thì mở lại |
| AMB-LOGIN-03 | Contact của khách hàng có đăng nhập được vào `/admin` bằng tài khoản cổng khách hàng không? | Lỗ hổng phân tách hai cổng nếu đăng nhập được | 🔴 | Không đăng nhập được — "Invalid email or password" | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm. Chưa kiểm chứng → REQ-LOGIN-29 ⚪; ô phân quyền giữ ❔ |
| AMB-LOGIN-04 | Khi bỏ trống cả hai ô, thông báo Password hiện **trước** thông báo Email — ngược thứ tự ô trên form. Cố ý? | TC assert thứ tự sẽ đỏ nếu dev sửa | 🟡 | Không assert thứ tự, chỉ assert có đủ 2 thông báo | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm: TC không assert thứ tự thông báo |
| AMB-LOGIN-05 | Forgot Password bỏ trống Email trả **"Email not found"** thay vì thông báo bắt buộc nhập. Thiếu validation required? | Thông báo gây hiểu nhầm cho người dùng | 🔴 | Ghi nhận như hành vi hiện tại (REQ-LOGIN-20), nghi là lỗi | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm: REQ-LOGIN-20 giữ nguyên. **Vẫn nghi lỗi** — TC PASS không có nghĩa hành vi đúng |
| AMB-LOGIN-06 | Forgot Password báo **"Email not found"** khi email không tồn tại — tiết lộ email nào có trong hệ thống, trong khi Login dùng thông báo chung. Cố ý? | Dò tài khoản (user enumeration) — RISK-LOGIN-02 | 🔴 | Hành vi hiện tại là thật, đánh dấu rủi ro bảo mật | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm: REQ-LOGIN-21 giữ nguyên. **Rủi ro bảo mật chưa xử lý** — RISK-LOGIN-02 giữ nguyên |
| AMB-LOGIN-07 | Sau lỗi, trang Login **xoá** Email đã nhập (REQ-LOGIN-08) còn Forgot Password **giữ lại** (REQ-LOGIN-22). Không nhất quán — cố ý? | Trải nghiệm người dùng; TC hai bên kỳ vọng ngược nhau | 🟡 | Test đúng hành vi hiện tại từng màn | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm: REQ-LOGIN-08 và REQ-LOGIN-22 giữ nguyên |
| AMB-LOGIN-08 | Sau đăng nhập luôn vào Dashboard, **không** quay về trang bị chặn trước đó (REQ-LOGIN-10). Cố ý? | Người dùng mở link sâu phải điều hướng lại | 🟡 | Hành vi hiện tại là đúng | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm: REQ-LOGIN-10 giữ nguyên |
| AMB-LOGIN-09 | Mọi chuyển hướng xác thực quan sát được trả **307** thay vì 302/303 (REQ-LOGIN-11, 12, 13, 26). Cấu hình cố ý hay sai? | 307 giữ nguyên method — POST tới route bị bảo vệ có thể bị lặp lại | 🟡 | AC chỉ assert **điểm dừng**, không assert mã HTTP (skill 4.3.9) | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm: AC chỉ assert điểm dừng |
| AMB-LOGIN-10 | Có khoá tài khoản / giới hạn số lần đăng nhập sai không? Ngưỡng bao nhiêu? (không thử trên tài khoản dùng chung) | Thiếu chống brute-force (RISK-LOGIN-04) hoặc khoá nhầm tài khoản chung (RISK-LOGIN-01) | 🔴 | Chưa rõ — không viết TC khoá tài khoản cho tới khi có môi trường riêng | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm: không viết TC khoá tài khoản cho tới khi có môi trường riêng. **Chính sách vẫn chưa biết** — RISK-LOGIN-01, 04 giữ nguyên |
| AMB-LOGIN-11 | Email tồn tại + sai mật khẩu có trả cùng thông báo "Invalid email or password" không? (chưa thử — tránh khoá tài khoản chung) | Nếu khác thông báo → lộ email tồn tại ở Login | 🟡 | Cùng thông báo với REQ-LOGIN-07 | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm → REQ-LOGIN-30 ⚪ |
| AMB-LOGIN-12 | Cookie `autologin` có thật sự khôi phục phiên khi phiên chính hết hạn? Thời hạn 62 ngày đo được có đúng cấu hình mong muốn? | Ghi nhớ đăng nhập hỏng âm thầm — REQ-LOGIN-16 ⚪ | 🔴 | Khôi phục được trong 62 ngày | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm: REQ-LOGIN-16 giữ ⚪, chưa kiểm chứng |
| AMB-LOGIN-13 | Forgot Password với email tồn tại: email có được gửi, link có mở màn đặt mật khẩu mới, link hết hạn khi nào? Cần hộp thư test riêng | REQ-LOGIN-23, 24 ⚪ không kiểm chứng được | 🟡 | Gửi email kèm link đặt lại | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm: REQ-LOGIN-23, 24 giữ ⚪, vẫn cần hộp thư test |
| AMB-LOGIN-14 | Mã JS `logout()` chặn đăng xuất và hiện popup cảnh báo khi có timer đang chạy — chưa quan sát trên UI. Xác nhận hành vi? | Thiếu TC cho nhánh đăng xuất có timer | 🟡 | Có popup cảnh báo, không đăng xuất | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm → REQ-LOGIN-34 ⚪ |
| AMB-LOGIN-15 | Luồng đăng nhập khi tài khoản bật 2FA (Email / Google Authenticator — tuỳ chọn ở Edit Profile) chưa quan sát | Thiếu toàn bộ nhánh 2FA | 🟡 | Có bước nhập mã sau mật khẩu | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm → REQ-LOGIN-32 ⚪ |
| AMB-LOGIN-16 | Trang Forgot Password không có link quay lại Login (chỉ logo → `/`), tiêu đề trang vẫn kết thúc bằng "- Login". Cố ý? | Trải nghiệm điều hướng | 🟢 | Hành vi hiện tại | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm: REQ-LOGIN-18 giữ nguyên |
| AMB-LOGIN-17 | Bỏ trống Email nhưng có Password: chỉ hiện thông báo Email? (chưa quan sát riêng — cần gõ mật khẩu) | REQ-LOGIN-05 mới kiểm với cả hai ô trống | 🟢 | Chỉ hiện "The Email Address field is required." | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm → REQ-LOGIN-31 ⚪ |
| AMB-LOGIN-18 | Không tick Remember me thì có tạo cookie `autologin` không? (chưa đăng nhập lần nào không tick) | Ghi nhớ bật ngoài ý muốn | 🟡 | Không tạo | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm → REQ-LOGIN-33 ⚪ |

### Risks

| Mã | Rủi ro | Mô tả | Mitigation |
|---|---|---|---|
| RISK-LOGIN-01 | Khoá tài khoản dùng chung | Môi trường dùng chung một tài khoản admin; TC đăng nhập sai bằng email thật có thể khoá tài khoản của mọi người | Case sai dùng email không tồn tại (`@example.invalid`); case khoá tài khoản chỉ chạy trên môi trường riêng |
| RISK-LOGIN-02 | Dò email qua Forgot Password | "Email not found" cho biết email nào tồn tại (AMB-LOGIN-06) | TC bảo mật riêng; báo PO/dev |
| RISK-LOGIN-03 | Cookie ghi nhớ kém an toàn | `autologin` không có cờ HttpOnly, không đặt SameSite, còn trong trình duyệt sau Logout | TC kiểm cờ cookie; báo dev; không chép giá trị cookie vào bất kỳ tài liệu nào |
| RISK-LOGIN-04 | Brute-force | Không có CAPTCHA, chưa rõ giới hạn số lần sai (AMB-LOGIN-10) | Chờ môi trường riêng để test rate limit / khoá |
| RISK-LOGIN-05 | Thông báo phụ thuộc trình duyệt | Kiểm tra định dạng email là của trình duyệt (`type=email`), chuỗi thông báo đổi theo trình duyệt/ngôn ngữ | AC chỉ assert `checkValidity() === false` + không có request; cấm assert chuỗi |
| RISK-LOGIN-06 | Side-effect khi test Forgot Password | Email tồn tại sẽ gửi thư đặt lại thật | Chỉ dùng hộp thư test riêng; không dùng email tài khoản dùng chung |

## 6. Phân rã Epic / Story

**Epic:** Xác thực khu admin (`LOGIN`).

| Story ID | Tên Story | REQ bao phủ | Số REQ | AMB / RISK liên quan | Ghi chú phạm vi |
|---|---|---|---|---|---|
| STORY-LOGIN-01 | Màn hình & validation đăng nhập | REQ-LOGIN-01 → 08, 14, 29 → 32 | 13 | AMB-LOGIN-04, 07, 10, 11, 17 · RISK-LOGIN-01, 04, 05 | Form, focus, định dạng email, thông báo server, CSRF |
| STORY-LOGIN-02 | Phiên & điều hướng | REQ-LOGIN-09 → 13 | 5 | AMB-LOGIN-08, 09 | Đích sau đăng nhập, bảo vệ route |
| STORY-LOGIN-03 | Ghi nhớ đăng nhập | REQ-LOGIN-15, 16, 33 | 3 | AMB-LOGIN-12, 18 · RISK-LOGIN-03 | Cookie `autologin` — tạo ra và dùng được |
| STORY-LOGIN-04 | Quên mật khẩu | REQ-LOGIN-17 → 24 | 8 | AMB-LOGIN-05, 06, 13, 16 · RISK-LOGIN-02, 06 | Form, validation, email đặt lại |
| STORY-LOGIN-05 | Đăng xuất | REQ-LOGIN-25 → 28, 34 | 5 | AMB-LOGIN-14 | Menu, chuyển hướng, vô hiệu phiên |

**Tổng: 5 Story / 34 REQ — mọi REQ thuộc đúng một Story, không mồ côi, không trùng.** `13 + 5 + 3 + 8 + 5 = 34 ✔`

| Nhóm | Mã | Nằm ở đâu |
|---|---|---|
| AMB thuộc Story | AMB-LOGIN-04 → 14, 16 → 18 | phân bổ ở bảng Story |
| AMB cấp Epic | AMB-LOGIN-01, 02, 03, 15 | Ma trận Phân quyền (01–03) · luồng 2FA cắt ngang mọi Story đăng nhập (15) |
| RISK thuộc Story | RISK-LOGIN-01 → 06 | phân bổ ở bảng Story |
| RISK cấp Epic | — | — |

Kiểm: AMB 14 (Story) + 4 (Epic) = 18 ✔ · RISK 6 + 0 = 6 ✔

**Hạng mục cấp Epic** (cố ý không gán vào Story): Ma trận Phân quyền (mục 3) — cắt ngang mọi Story · Ma trận Trạng thái phiên (mục 4) — cắt ngang Story 02, 05 · Yêu cầu phi chức năng (file `web/`, mục 7) — áp toàn module · AMB-LOGIN-15 (2FA).

**Thứ tự triển khai đề xuất:** STORY-LOGIN-01 → 02 → 05 → 03 → 04.
- Mọi AMB của module đã ⏭️ (05-11-2026), không còn Story chờ câu trả lời. TC viết theo Assumption tạm phải gắn nhãn `assumption-based`
- REQ ⚪ vẫn **chưa chạy kiểm chứng được** nếu thiếu điều kiện: REQ-LOGIN-16, 33 (đăng nhập riêng, xoá cookie) · REQ-LOGIN-23, 24 (hộp thư test) · REQ-LOGIN-29 (account Contact) · REQ-LOGIN-30 (môi trường riêng, tránh khoá tài khoản chung) · REQ-LOGIN-31 (user tự gõ mật khẩu) · REQ-LOGIN-32 (tài khoản bật 2FA) · REQ-LOGIN-34 (timer đang chạy)

## 7. Nhật ký thay đổi

| Ngày | Nguồn | REQ ảnh hưởng | Loại | Tóm tắt thay đổi | TC cần xử lý |
|---|---|---|---|---|---|
| 05-11-2026 | User chốt dùng Assumption tạm | REQ-LOGIN-29 → 34 | 🟢 Thêm | 6 REQ ⚪ cho hành vi giả định chưa có REQ phủ. Chưa kiểm chứng. Xem [impact/impact_LOGIN-ASSUMPTIONS-05112026.md](impact/impact_LOGIN-ASSUMPTIONS-05112026.md) | ➕ viết mới, nhãn `assumption-based` — chưa có bộ TC |
| 05-11-2026 | User chốt dùng Assumption tạm | AMB-LOGIN-03 → 18 ❓ → ⏭️ · không REQ cũ nào đổi | ✏️ Biên tập | 16 AMB còn treo chuyển sang Bỏ qua, test theo Assumption tạm và chấp nhận rủi ro | Không tác động — chưa có bộ TC |
| 05-11-2026 | User trả lời AMB-LOGIN-01 | Không REQ nào đổi · AMB-LOGIN-01, 02 ❓ → ✅ | ✏️ Biên tập | User xác nhận 05-11-2026: tạm thời hệ thống chỉ có role admin: 6 ô phân quyền chuyển sang không áp dụng. Xem [impact/impact_AMB-LOGIN-01.md](impact/impact_AMB-LOGIN-01.md) | Không tác động — chưa có bộ TC |
| 02-11-2026 | UI recon | REQ-LOGIN-01 → 28 · AMB-LOGIN-01 → 18 · RISK-LOGIN-01 → 06 | 🟢 Thêm | Khởi tạo tài liệu từ khảo sát UI thực tế trên Chrome local (mode UI) | — (viết mới) |
