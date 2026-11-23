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
| **Dải mã đã dùng** | `REQ-LOGIN-01` → `REQ-LOGIN-47` · `AMB-LOGIN-01` → `AMB-LOGIN-26` · `RISK-LOGIN-01` → `RISK-LOGIN-08` (đợt 1: UI recon 02-11-2026, 01 → 28 · đợt 2: Assumption tạm do user chốt 05-11-2026, 29 → 34 · đợt 3: ticket `LOGIN-LOCKOUT-11112026` 11-11-2026, REQ 35 → 41 · AMB 19 → 26 · RISK 07 → 08 · đợt 4: Assumption tạm do user chốt 11-11-2026, REQ 42 → 47) |
| **Mã kế tiếp** | Đợt phân tích sau bắt đầu từ `REQ-LOGIN-48` · `AMB-LOGIN-27` · `RISK-LOGIN-09` — **KHÔNG đánh lại từ 01** |
| **Nguồn** | Khảo sát UI thực tế (mode UI theo chỉ định của user — không dùng tài liệu) · trả lời của user cho AMB-LOGIN-01 (05-11-2026) · ticket khoá tài khoản do PO chốt, ghi nhận 11-11-2026 — ticket không mang mã, dùng mã nội bộ `LOGIN-LOCKOUT-11112026` |
| **Môi trường** | 🔒 Dùng chung — không đăng nhập sai bằng email thật (tránh khoá tài khoản chung), không gửi email đặt lại tới hộp thư thật. TC khoá tài khoản (STORY-LOGIN-06) dùng tài khoản **Project Manager**, **không** dùng Admin — PO chốt trong ticket `LOGIN-LOCKOUT-11112026` |
| **Ngày khảo sát** | 02-11-2026 |

**Mục đích:** cổng vào khu quản trị. Người dùng nội bộ đăng nhập bằng email + mật khẩu, có tuỳ chọn ghi nhớ đăng nhập, có luồng yêu cầu đặt lại mật khẩu, và đăng xuất từ menu avatar.

**Trong phạm vi:** trang `/admin/authentication` · trang `/admin/authentication/forgot_password` · điều hướng bảo vệ route admin (chưa đăng nhập / đã đăng nhập) · cookie ghi nhớ đăng nhập · đăng xuất · khoá tài khoản khi đăng nhập sai nhiều lần (⚪ theo ticket, chưa kiểm chứng).

**Ngoài phạm vi:** cổng khách hàng (`/clients/*` — URL/tài khoản khác, khảo sát sau) · màn đặt mật khẩu mới qua link email (cần token — xem `REQ-LOGIN-24` ⚪) · cấu hình 2FA ở Edit Profile (module `PROF`) · cấu hình chính sách đăng nhập ở Setup (module `SETTING`, BLOCKED).

### Bản đồ phủ tài liệu

Không có tài liệu — toàn bộ REQ sinh từ khảo sát UI thực tế. Repo có `SRS_Login_Module.md` trong lịch sử git nhưng **không dùng** theo chỉ định của user (02-11-2026).

## Bản đồ tài liệu

| Nền tảng | File | Story | REQ bao phủ |
|---|---|---|---|
| Chung ≥ 2 nền tảng | chính file này | — | Không có — module mới có một nền tảng |
| Web | [web/requirements_login_web.md](web/requirements_login_web.md) | STORY-LOGIN-01 → 06 | `REQ-LOGIN-01` → `REQ-LOGIN-47` |

**Tổng: 47 REQ** = 0 ở index + 47 ở `web/`.

## 2. Yêu cầu dùng chung nhiều nền tảng

Không áp dụng — module mới khảo sát trên Web. Khi khảo sát app/API, rule trùng sẽ được chuyển lên đây (giữ nguyên mã, mở rộng cột `Nền tảng`).

## 3. Ma trận Phân quyền

| Hành động | Admin (tài khoản `.env`) | Super Admin | Nhân viên role khác (Project Manager) | Contact khách hàng |
|---|---|---|---|---|
| Đăng nhập vào khu admin | ✅ | — | ❔ | ❔ |
| Yêu cầu đặt lại mật khẩu (email tồn tại) | ❔ | — | ❔ | ❔ |
| Đăng xuất | ✅ | — | ❔ | ❔ |

Tổng 12 ô = Đã kiểm chứng 2 · Suy diễn 0 · Chưa rõ 7 · Không áp dụng 3.
Ô "không áp dụng" là toàn bộ cột Super Admin (3 ô) — User xác nhận 05-11-2026: tạm thời không có role Super Admin riêng (AMB-LOGIN-01). Cột *Nhân viên role khác* trước đây cũng "không áp dụng" (AMB-LOGIN-02); **mở lại thành ❔ ngày 11-11-2026** theo Assumption tạm AMB-LOGIN-24: có role Project Manager. Ô [Yêu cầu đặt lại mật khẩu × Admin] là ❔ vì cố ý không gửi email đặt lại tới hộp thư thật của tài khoản dùng chung (AMB-LOGIN-13). Contact khách hàng chưa có account: test theo Assumption tạm "không đăng nhập được" (AMB-LOGIN-03 ⏭️, REQ-LOGIN-29 ⚪), ô ma trận **giữ ❔** vì chưa kiểm chứng.
⚠️ Ticket `LOGIN-LOCKOUT-11112026` (11-11-2026) yêu cầu TC dùng tài khoản **Project Manager** — trái với kết luận tạm "chỉ có role admin" của AMB-LOGIN-01, 02. User chốt Assumption tạm AMB-LOGIN-24: có role PM → 3 ô của cột PM là ❔ (**chưa có tài khoản PM để kiểm chứng**). Khoá tài khoản áp theo email, không theo role — không thêm hàng vào ma trận này.

## 4. Ma trận Trạng thái phiên

Không có entity mang status flow. Bảng dưới mô tả **trạng thái phiên đăng nhập** quan sát được trên Web, và từ 11-11-2026 thêm trạng thái **khoá** của tài khoản theo ticket `LOGIN-LOCKOUT-11112026` (các dòng có REQ-LOGIN-35 → 47 — ⚪ chưa kiểm chứng):

| Trạng thái hiện tại | Hành động | Trạng thái kế tiếp | REQ |
|---|---|---|---|
| Chưa đăng nhập | Mở route admin bất kỳ | Chưa đăng nhập — đứng ở trang Login | REQ-LOGIN-11 |
| Chưa đăng nhập | Đăng nhập đúng | Đã đăng nhập — Dashboard `/admin/` | REQ-LOGIN-09, 10 |
| Chưa đăng nhập | Đăng nhập sai / bỏ trống | Chưa đăng nhập — trang Login kèm thông báo | REQ-LOGIN-05 → 08 |
| Đã đăng nhập | Mở trang Login hoặc Forgot Password | Đã đăng nhập — Dashboard `/admin/` | REQ-LOGIN-12, 13 |
| Đã đăng nhập | Logout | Chưa đăng nhập — trang Login | REQ-LOGIN-26, 27 |
| Đã đăng nhập (có ghi nhớ) | Logout | Chưa đăng nhập — cookie ghi nhớ còn sót nhưng không khôi phục phiên | REQ-LOGIN-28 |
| Đã đăng nhập (có timer đang chạy) | Logout | Đã đăng nhập — popup cảnh báo (⚪ theo Assumption tạm) | REQ-LOGIN-34 |
| Chưa đăng nhập · bộ đếm sai 1 → 4 | Đăng nhập đúng | Đã đăng nhập — bộ đếm về 0 | REQ-LOGIN-39 |
| Chưa đăng nhập · bộ đếm sai 4 | Gửi Password trống / mã chống giả mạo sai / sai ở email khác | Không đổi — bộ đếm vẫn 4 (Assumption tạm) | REQ-LOGIN-44, 45, 46 |
| Chưa đăng nhập · bộ đếm sai 4 | Sai mật khẩu lần thứ 5 | **Tài khoản bị khoá** 15 phút — lần này vẫn báo "Invalid email or password" (Assumption tạm) | REQ-LOGIN-35, 42 |
| Tài khoản bị khoá | Đăng nhập (đúng hoặc sai mật khẩu) từ bất kỳ IP nào | Tài khoản bị khoá — thông báo khoá, không gia hạn thời gian khoá (Assumption tạm) | REQ-LOGIN-37, 38, 41, 43 |
| Tài khoản bị khoá | Hết 15 phút | Chưa đăng nhập — đăng nhập được, bộ đếm về 0 (Assumption tạm) | REQ-LOGIN-36, 47 |

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
| AMB-LOGIN-10 | Có khoá tài khoản / giới hạn số lần đăng nhập sai không? Ngưỡng bao nhiêu? (không thử trên tài khoản dùng chung) | Thiếu chống brute-force (RISK-LOGIN-04) hoặc khoá nhầm tài khoản chung (RISK-LOGIN-01) | 🔴 | Chưa rõ — không viết TC khoá tài khoản cho tới khi có môi trường riêng | ✅ Đã trả lời 11-11-2026 | PO chốt trong ticket `LOGIN-LOCKOUT-11112026`: sai mật khẩu 5 lần liên tiếp cùng email → khoá 15 phút, khoá theo email không theo IP → sinh REQ-LOGIN-35 → 41 (⚪ chưa kiểm chứng). **Khác Assumption tạm:** TC khoá tài khoản **được viết** trên môi trường dùng chung, bằng tài khoản Project Manager (không dùng Admin) — không chờ môi trường riêng. (Trước đó: ⏭️ Bỏ qua 05-11-2026) |
| AMB-LOGIN-11 | Email tồn tại + sai mật khẩu có trả cùng thông báo "Invalid email or password" không? (chưa thử — tránh khoá tài khoản chung) | Nếu khác thông báo → lộ email tồn tại ở Login | 🟡 | Cùng thông báo với REQ-LOGIN-07 | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm → REQ-LOGIN-30 ⚪ |
| AMB-LOGIN-12 | Cookie `autologin` có thật sự khôi phục phiên khi phiên chính hết hạn? Thời hạn 62 ngày đo được có đúng cấu hình mong muốn? | Ghi nhớ đăng nhập hỏng âm thầm — REQ-LOGIN-16 ⚪ | 🔴 | Khôi phục được trong 62 ngày | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm: REQ-LOGIN-16 giữ ⚪, chưa kiểm chứng |
| AMB-LOGIN-13 | Forgot Password với email tồn tại: email có được gửi, link có mở màn đặt mật khẩu mới, link hết hạn khi nào? Cần hộp thư test riêng | REQ-LOGIN-23, 24 ⚪ không kiểm chứng được | 🟡 | Gửi email kèm link đặt lại | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm: REQ-LOGIN-23, 24 giữ ⚪, vẫn cần hộp thư test |
| AMB-LOGIN-14 | Mã JS `logout()` chặn đăng xuất và hiện popup cảnh báo khi có timer đang chạy — chưa quan sát trên UI. Xác nhận hành vi? | Thiếu TC cho nhánh đăng xuất có timer | 🟡 | Có popup cảnh báo, không đăng xuất | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm → REQ-LOGIN-34 ⚪ |
| AMB-LOGIN-15 | Luồng đăng nhập khi tài khoản bật 2FA (Email / Google Authenticator — tuỳ chọn ở Edit Profile) chưa quan sát | Thiếu toàn bộ nhánh 2FA | 🟡 | Có bước nhập mã sau mật khẩu | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm → REQ-LOGIN-32 ⚪ |
| AMB-LOGIN-16 | Trang Forgot Password không có link quay lại Login (chỉ logo → `/`), tiêu đề trang vẫn kết thúc bằng "- Login". Cố ý? | Trải nghiệm điều hướng | 🟢 | Hành vi hiện tại | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm: REQ-LOGIN-18 giữ nguyên |
| AMB-LOGIN-17 | Bỏ trống Email nhưng có Password: chỉ hiện thông báo Email? (chưa quan sát riêng — cần gõ mật khẩu) | REQ-LOGIN-05 mới kiểm với cả hai ô trống | 🟢 | Chỉ hiện "The Email Address field is required." | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm → REQ-LOGIN-31 ⚪ |
| AMB-LOGIN-18 | Không tick Remember me thì có tạo cookie `autologin` không? (chưa đăng nhập lần nào không tick) | Ghi nhớ bật ngoài ý muốn | 🟡 | Không tạo | ⏭️ Bỏ qua 05-11-2026 | User chốt. Dùng Assumption tạm → REQ-LOGIN-33 ⚪ |
| AMB-LOGIN-19 | Ở **chính** lần sai thứ 5, trang hiện "Invalid email or password" hay đã hiện thông báo khoá? (ticket: "khi bị khoá, trang đăng nhập hiển thị…" — không nói rõ lần thứ 5 hay lần thứ 6) | Expected của TC ngưỡng khoá sai một bên là FAIL oan | 🔴 | Lần thứ 5 vẫn "Invalid email or password"; thông báo khoá hiện từ lần gửi thứ 6. REQ-LOGIN-35 không assert thông báo của lần thứ 5 | ⏭️ Bỏ qua 11-11-2026 | User chốt. Dùng Assumption tạm → REQ-LOGIN-42 ⚪ |
| AMB-LOGIN-20 | Mốc 15 phút tính từ lần sai thứ 5, hay tính lại mỗi lần thử đăng nhập trong lúc khoá (khoá trượt)? | TC thời hạn khoá (REQ-LOGIN-36) chờ sai mốc; người dùng thử lại liên tục bị khoá mãi | 🟡 | Tính từ lần sai thứ 5, thử lại không gia hạn. TC REQ-LOGIN-36 không thử trong lúc khoá; TC REQ-LOGIN-38 tính thời gian chờ từ lần thử cuối | ⏭️ Bỏ qua 11-11-2026 | User chốt. Dùng Assumption tạm → REQ-LOGIN-43 ⚪. TC REQ-LOGIN-36, 38 vẫn giữ cách chờ an toàn (không thử trong lúc khoá / tính từ lần thử cuối) để không phụ thuộc giả định |
| AMB-LOGIN-21 | "15 minutes" trong thông báo khoá là chữ cố định, hay là **thời gian còn lại** (đổi theo lúc thử)? | Assert nguyên văn sẽ đỏ khi thử ở phút thứ 10 | 🟡 | Chữ cố định. Trong lúc chờ, REQ-LOGIN-37 chỉ assert **chứa** `Your account is locked.` | ⏭️ Bỏ qua 11-11-2026 | User chốt. Dùng Assumption tạm: chữ cố định → REQ-LOGIN-37 assert **nguyên văn**, TC gắn nhãn `assumption-based` |
| AMB-LOGIN-22 | Lần gửi nào được tính là "đăng nhập sai"? (a) Password trống — server báo "The Password field is required." (b) lần bị từ chối do mã CSRF hết hạn/bị sửa (c) lần sai với email **khác** xen giữa có làm đứt chuỗi "liên tiếp" của email này không? | Ngưỡng khoá đến sớm/muộn hơn TC tính; TC validation (TC_009, 043, 058) vô tình làm tăng bộ đếm | 🟡 | Chỉ lần gửi có email + mật khẩu và mật khẩu sai mới được tính; (a), (b) không tính; bộ đếm riêng từng email, sai ở email khác không làm đứt chuỗi | ⏭️ Bỏ qua 11-11-2026 | User chốt. Dùng Assumption tạm → REQ-LOGIN-44 (a) · 45 (b) · 46 (c), cả ba ⚪ |
| AMB-LOGIN-23 | Email **không tồn tại** sai 5 lần có hiện thông báo khoá không? Nếu email tồn tại thì khoá còn email không tồn tại thì không → thông báo khoá cho biết email nào có trong hệ thống | Dò tài khoản qua thông báo khoá (gắn RISK-LOGIN-02); TC dùng lặp `recon.khongtontai@example.invalid` bị khoá giữa chừng | 🔴 | Không biết — TC dùng email không tồn tại phải đổi sang email riêng từng TC/biến thể để không phụ thuộc câu trả lời | ⏭️ Bỏ qua 11-11-2026 | User chốt. Dùng Assumption tạm: **hành vi vẫn chưa biết** — không cấp REQ; né bằng dữ liệu test (email không tồn tại riêng từng TC/biến thể). Rủi ro dò tài khoản qua thông báo khoá **chưa xử lý** — gắn RISK-LOGIN-02 |
| AMB-LOGIN-24 | Hệ thống có role **Project Manager** không, tài khoản test PM ở đâu? Ticket bắt TC dùng tài khoản PM nhưng `.env` chỉ có tài khoản admin, và AMB-LOGIN-01, 02 kết luận tạm "chỉ có role admin". Cần **2** tài khoản PM (REQ-LOGIN-40). Tài khoản PM có dùng chung với người khác không? | Toàn bộ STORY-LOGIN-06 không chạy được; nếu PM dùng chung thì mỗi lượt chạy khoá người khác 15 phút (RISK-LOGIN-07) | 🔴 | Người quản trị cấp 2 tài khoản PM chỉ dành cho kiểm thử, lưu ở `.env` (VD `EMAIL_PM_1`, `PASSWORD_PM_1`, `EMAIL_PM_2`, `PASSWORD_PM_2`). Chưa có → TC của Story 06 BLOCKED | ⏭️ Bỏ qua 11-11-2026 | User chốt. Dùng Assumption tạm: có role Project Manager, sẽ có 2 tài khoản PM chỉ dành cho kiểm thử ở `.env`. Cột *Nhân viên role khác* của ma trận phân quyền mở lại thành ❔. **Tài khoản PM chưa thật sự có** trong `.env` — tới lúc đó TC Story 06 vẫn BLOCKED |
| AMB-LOGIN-25 | Hết 15 phút khoá, bộ đếm lần sai về 0 hay vẫn giữ (sai 1 lần nữa là khoá lại)? | Thiếu TC cho hành vi sau khi mở khoá | 🟡 | Về 0 | ⏭️ Bỏ qua 11-11-2026 | User chốt. Dùng Assumption tạm → REQ-LOGIN-47 ⚪ |
| AMB-LOGIN-26 | Tài khoản đang khoá có mở được sớm không — đặt lại mật khẩu qua Forgot Password, hoặc admin mở khoá thủ công? | Người dùng bị khoá không có lối thoát; QA không dọn được tài khoản PM sau TC | 🟢 | Không có cách mở sớm — chờ đủ 15 phút | ⏭️ Bỏ qua 11-11-2026 | User chốt. Dùng Assumption tạm: không cấp REQ (khẳng định "không có tính năng" không kiểm chứng được bằng quyền hiện có — đặt lại mật khẩu cần hộp thư test, AMB-LOGIN-13). Bước dọn dẹp của TC Story 06 = chờ đủ 15 phút |

### Risks

| Mã | Rủi ro | Mô tả | Mitigation |
|---|---|---|---|
| RISK-LOGIN-01 | Khoá tài khoản dùng chung | Môi trường dùng chung một tài khoản admin; theo ticket `LOGIN-LOCKOUT-11112026`, 5 lần sai liên tiếp khoá tài khoản 15 phút — TC đăng nhập sai bằng email admin sẽ khoá tài khoản của mọi người | Case sai dùng email không tồn tại (`@example.invalid`), mỗi TC/biến thể một email riêng (AMB-LOGIN-23); **không bao giờ** gửi mật khẩu sai cho email admin; TC khoá tài khoản chỉ dùng tài khoản Project Manager (PO chốt 11-11-2026) |
| RISK-LOGIN-02 | Dò email qua Forgot Password | "Email not found" cho biết email nào tồn tại (AMB-LOGIN-06) | TC bảo mật riêng; báo PO/dev |
| RISK-LOGIN-03 | Cookie ghi nhớ kém an toàn | `autologin` không có cờ HttpOnly, không đặt SameSite, còn trong trình duyệt sau Logout | TC kiểm cờ cookie; báo dev; không chép giá trị cookie vào bất kỳ tài liệu nào |
| RISK-LOGIN-04 | Brute-force | Không có CAPTCHA. Theo ticket có khoá 15 phút sau 5 lần sai (REQ-LOGIN-35 → 47, ⚪ chưa kiểm chứng) — nhưng khoá theo email, **không** theo IP: một nguồn thử ít mật khẩu trên rất nhiều email (password spraying) không bị chặn | TC STORY-LOGIN-06 kiểm ngưỡng khoá bằng tài khoản PM; password spraying ngoài khả năng kiểm của QA — báo PO/đội Security |
| RISK-LOGIN-05 | Thông báo phụ thuộc trình duyệt | Kiểm tra định dạng email là của trình duyệt (`type=email`), chuỗi thông báo đổi theo trình duyệt/ngôn ngữ | AC chỉ assert `checkValidity() === false` + không có request; cấm assert chuỗi |
| RISK-LOGIN-06 | Side-effect khi test Forgot Password | Email tồn tại sẽ gửi thư đặt lại thật | Chỉ dùng hộp thư test riêng; không dùng email tài khoản dùng chung |
| RISK-LOGIN-07 | TC khoá tài khoản giẫm lên nhau | Mỗi lượt TC STORY-LOGIN-06 khoá tài khoản PM 15 phút. Chạy song song, chạy lại trong 15 phút, hoặc lần sai còn sót từ TC trước (bộ đếm chưa về 0) làm TC sau bị khoá sớm → FAIL oan; nếu tài khoản PM dùng chung thì khoá luôn người khác | TC Story 06 chạy **tuần tự**, không song song; mỗi TC bắt đầu bằng 1 lần đăng nhập đúng + Logout (đặt bộ đếm về 0 — REQ-LOGIN-39) và kết thúc bằng chờ hết khoá; tài khoản PM chỉ dành cho kiểm thử (AMB-LOGIN-24) |
| RISK-LOGIN-08 | Cố ý khoá tài khoản người khác | Khoá theo email: ai biết email của người dùng đều có thể gửi 5 mật khẩu sai để khoá họ 15 phút, lặp lại để khoá liên tục (từ chối dịch vụ) | Báo PO (đánh đổi của chính sách khoá theo email); TC REQ-LOGIN-41 chứng minh khoá áp từ mọi IP |

## 6. Phân rã Epic / Story

**Epic:** Xác thực khu admin (`LOGIN`).

| Story ID | Tên Story | REQ bao phủ | Số REQ | AMB / RISK liên quan | Ghi chú phạm vi |
|---|---|---|---|---|---|
| STORY-LOGIN-01 | Màn hình & validation đăng nhập | REQ-LOGIN-01 → 08, 14, 29 → 32 | 13 | AMB-LOGIN-04, 07, 11, 17 · RISK-LOGIN-01, 05 | Form, focus, định dạng email, thông báo server, CSRF |
| STORY-LOGIN-02 | Phiên & điều hướng | REQ-LOGIN-09 → 13 | 5 | AMB-LOGIN-08, 09 | Đích sau đăng nhập, bảo vệ route |
| STORY-LOGIN-03 | Ghi nhớ đăng nhập | REQ-LOGIN-15, 16, 33 | 3 | AMB-LOGIN-12, 18 · RISK-LOGIN-03 | Cookie `autologin` — tạo ra và dùng được |
| STORY-LOGIN-04 | Quên mật khẩu | REQ-LOGIN-17 → 24 | 8 | AMB-LOGIN-05, 06, 13, 16 · RISK-LOGIN-02, 06 | Form, validation, email đặt lại |
| STORY-LOGIN-05 | Đăng xuất | REQ-LOGIN-25 → 28, 34 | 5 | AMB-LOGIN-14 | Menu, chuyển hướng, vô hiệu phiên |
| STORY-LOGIN-06 | Khoá tài khoản khi đăng nhập sai nhiều lần | REQ-LOGIN-35 → 47 | 13 | AMB-LOGIN-10, 19 → 26 · RISK-LOGIN-04, 07, 08 | Ngưỡng 5 lần, thời hạn 15 phút, thông báo khoá, đặt lại bộ đếm, khoá theo email. Nguồn: ticket `LOGIN-LOCKOUT-11112026` |

**Tổng: 6 Story / 47 REQ — mọi REQ thuộc đúng một Story, không mồ côi, không trùng.** `13 + 5 + 3 + 8 + 5 + 13 = 47 ✔`

| Nhóm | Mã | Nằm ở đâu |
|---|---|---|
| AMB thuộc Story | AMB-LOGIN-04 → 14, 16 → 26 | phân bổ ở bảng Story |
| AMB cấp Epic | AMB-LOGIN-01, 02, 03, 15 | Ma trận Phân quyền (01–03) · luồng 2FA cắt ngang mọi Story đăng nhập (15) |
| RISK thuộc Story | RISK-LOGIN-01 → 08 | phân bổ ở bảng Story |
| RISK cấp Epic | — | — |

Kiểm: AMB 22 (Story) + 4 (Epic) = 26 ✔ · RISK 8 + 0 = 8 ✔

**Hạng mục cấp Epic** (cố ý không gán vào Story): Ma trận Phân quyền (mục 3) — cắt ngang mọi Story · Ma trận Trạng thái phiên (mục 4) — cắt ngang Story 02, 05 · Yêu cầu phi chức năng (file `web/`, mục 7) — áp toàn module · AMB-LOGIN-15 (2FA).

**Thứ tự triển khai đề xuất:** STORY-LOGIN-01 → 02 → 05 → 03 → 04 → 06.
- STORY-LOGIN-01 → 05: mọi AMB đã ⏭️ (05-11-2026), không chờ câu trả lời. TC viết theo Assumption tạm phải gắn nhãn `assumption-based`
- STORY-LOGIN-06: AMB-LOGIN-19 → 26 đã ⏭️ (11-11-2026), không còn AMB chờ trả lời — viết TC được ngay theo Assumption tạm, gắn nhãn `assumption-based`. **Chạy vẫn BLOCKED** cho tới khi `.env` có tài khoản Project Manager (TC không được dùng Admin)
- REQ ⚪ vẫn **chưa chạy kiểm chứng được** nếu thiếu điều kiện: REQ-LOGIN-16, 33 (đăng nhập riêng, xoá cookie) · REQ-LOGIN-23, 24 (hộp thư test) · REQ-LOGIN-29 (account Contact) · REQ-LOGIN-30 (môi trường riêng, tránh khoá tài khoản chung) · REQ-LOGIN-31 (user tự gõ mật khẩu) · REQ-LOGIN-32 (tài khoản bật 2FA) · REQ-LOGIN-34 (timer đang chạy) · REQ-LOGIN-35 → 47 (tài khoản PM; REQ-LOGIN-40, 46 cần tài khoản PM thứ hai hoặc email không tồn tại riêng; REQ-LOGIN-41 cần máy/mạng có IP khác; REQ-LOGIN-45 cần DevTools; mỗi lượt chờ ≥ 15 phút)

## 7. Nhật ký thay đổi

| Ngày | Nguồn | REQ ảnh hưởng | Loại | Tóm tắt thay đổi | TC cần xử lý |
|---|---|---|---|---|---|
| 11-11-2026 | User chốt dùng Assumption tạm | REQ-LOGIN-42 → 47 | 🟢 Thêm | 6 REQ ⚪ cho hành vi giả định chưa có REQ phủ: thông báo của lần sai thứ 5 (42) · thử trong lúc khoá không gia hạn (43) · Password trống (44) và mã chống giả mạo sai (45) không tính là lần sai · bộ đếm riêng từng email (46) · hết khoá thì bộ đếm về 0 (47). Chưa kiểm chứng. Xem [impact/impact_LOGIN-ASSUMPTIONS-11112026.md](impact/impact_LOGIN-ASSUMPTIONS-11112026.md) | ➕ viết mới, nhãn `assumption-based` |
| 11-11-2026 | User chốt dùng Assumption tạm | AMB-LOGIN-19 → 26 ❓ → ⏭️ · REQ-LOGIN-35, 37 (giữ ⚪) · ma trận phân quyền mở lại cột Project Manager thành ❔ | ✏️ Biên tập | 8 AMB của ticket khoá tài khoản chuyển sang Bỏ qua, test theo Assumption tạm. REQ-LOGIN-37 assert nguyên văn thông báo khoá (AMB-LOGIN-21); REQ-LOGIN-35 trỏ sang REQ-LOGIN-42, 44 → 46. AMB-LOGIN-23, 26 không cấp REQ | Không tác động TC hiện có — chưa có TC cho REQ-LOGIN-35 → 41. CRM_LOGIN_TC_009 hết phụ thuộc AMB-LOGIN-22 nhưng vẫn ⚠️ review dữ liệu theo AMB-LOGIN-23 |
| 11-11-2026 | LOGIN-LOCKOUT-11112026 (ticket PO chốt, không mang mã) | REQ-LOGIN-35 → 41 | 🟢 Thêm | 7 REQ ⚪ cho khoá tài khoản: ngưỡng 5 lần sai liên tiếp (35) · hết khoá sau 15 phút (36) · thông báo khoá (37) · mật khẩu đúng vẫn bị chặn khi khoá (38) · đăng nhập đúng đặt bộ đếm về 0 (39) · khoá theo email, không theo IP (40, 41). Thêm STORY-LOGIN-06. Chưa kiểm chứng. Xem [impact/impact_LOGIN-LOCKOUT-11112026.md](impact/impact_LOGIN-LOCKOUT-11112026.md) | ➕ viết mới TC cho REQ-LOGIN-35 → 41 |
| 11-11-2026 | LOGIN-LOCKOUT-11112026 | AMB-LOGIN-10 ⏭️ → ✅ · thêm AMB-LOGIN-19 → 26 ❓ · thêm RISK-LOGIN-07, 08 · sửa mô tả/mitigation RISK-LOGIN-01, 04 · ma trận trạng thái thêm trạng thái khoá | ✏️ Biên tập | Ticket trả lời AMB-LOGIN-10, **khác Assumption tạm**: TC khoá tài khoản được viết trên môi trường dùng chung bằng tài khoản Project Manager, không dùng Admin. 8 câu hỏi mới về ngưỡng, thời hạn, thông báo, tài khoản PM | ⚠️ review CRM_LOGIN_TC_018 (bước dọn dẹp + ASM-07 dựa trên AMB-LOGIN-10 cũ) · index TC (đối soát loại kiểm thử đang ghi khoá tài khoản ⏭️ Cố ý bỏ) |
| 11-11-2026 | LOGIN-LOCKOUT-11112026 | REQ-LOGIN-30 (giữ ⚪) | ✏️ Biên tập | Ghi rõ phạm vi AC: áp khi tài khoản chưa bị khoá, không gửi quá 4 lần sai liên tiếp. Hành vi không đổi | ⚠️ review CRM_LOGIN_TC_018 · ⚠️ review dữ liệu test của CRM_LOGIN_TC_009, 013, 017, 021, 039, 047, 056 (gửi lặp email không tồn tại — AMB-LOGIN-22, 23) |
| 05-11-2026 | User chốt dùng Assumption tạm | REQ-LOGIN-29 → 34 | 🟢 Thêm | 6 REQ ⚪ cho hành vi giả định chưa có REQ phủ. Chưa kiểm chứng. Xem [impact/impact_LOGIN-ASSUMPTIONS-05112026.md](impact/impact_LOGIN-ASSUMPTIONS-05112026.md) | ➕ viết mới, nhãn `assumption-based` — chưa có bộ TC |
| 05-11-2026 | User chốt dùng Assumption tạm | AMB-LOGIN-03 → 18 ❓ → ⏭️ · không REQ cũ nào đổi | ✏️ Biên tập | 16 AMB còn treo chuyển sang Bỏ qua, test theo Assumption tạm và chấp nhận rủi ro | Không tác động — chưa có bộ TC |
| 05-11-2026 | User trả lời AMB-LOGIN-01 | Không REQ nào đổi · AMB-LOGIN-01, 02 ❓ → ✅ | ✏️ Biên tập | User xác nhận 05-11-2026: tạm thời hệ thống chỉ có role admin: 6 ô phân quyền chuyển sang không áp dụng. Xem [impact/impact_AMB-LOGIN-01.md](impact/impact_AMB-LOGIN-01.md) | Không tác động — chưa có bộ TC |
| 02-11-2026 | UI recon | REQ-LOGIN-01 → 28 · AMB-LOGIN-01 → 18 · RISK-LOGIN-01 → 06 | 🟢 Thêm | Khởi tạo tài liệu từ khảo sát UI thực tế trên Chrome local (mode UI) | — (viết mới) |
