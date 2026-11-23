# Requirements Web — Đăng nhập (`LOGIN`)

> ← [Index module `REQUIREMENTS_LOGIN_SUMMARY.md`](../REQUIREMENTS_LOGIN_SUMMARY.md) — phân quyền · trạng thái phiên · AMB/RISK · Story · Nhật ký nằm ở index.

## 1. Metadata khảo sát

| Thuộc tính | Giá trị |
|---|---|
| **Nền tảng** | Web — khu admin |
| **REQ trong file** | `REQ-LOGIN-01` → `REQ-LOGIN-47` (47 REQ) |
| **Trình duyệt khảo sát** | Google Chrome 146 (headed, máy local, profile tạm), viewport `1598×790`, điều khiển qua Chrome DevTools Protocol. Mọi AC dựa trên thông báo mặc định của trình duyệt **chỉ đúng với trình duyệt này** |
| **Phiên khảo sát** | Cửa sổ Chrome **tách biệt, không cookie** (browser context riêng) — không ảnh hưởng phiên khác. Các bước cần gõ mật khẩu do **user tự thao tác**; agent đọc DOM + chụp ảnh |
| **Tầng network** | Quan sát thụ động request do UI phát sinh (`Network.*` của CDP). Không gọi API trực tiếp |
| **Ngày** | 02-11-2026 |

**Quy ước cột `Nguồn`:** `Kiểm chứng thực tế` = đã thao tác và xác nhận · `UI thực tế` = chỉ quan sát · `API · <method> <route> · <status>` = từ tầng network · `User thao tác` = bước do user gõ, agent quan sát kết quả.
**Trạng thái ⚪ trong file này** = chưa kiểm chứng được trên môi trường dùng chung (skill 4.3.8), luôn kèm AMB. REQ-LOGIN-29 → 34 mô tả **Assumption tạm do user chốt** (05-11-2026), chưa ai quan sát hành vi này trên hệ thống — TC gắn nhãn `assumption-based`. REQ-LOGIN-35 → 41 lấy từ ticket khoá tài khoản do PO chốt (`LOGIN-LOCKOUT-11112026`, ghi nhận 11-11-2026): **chưa kiểm chứng, chưa biết hệ thống đã build hay chưa**. Nguồn ghi `Ticket LOGIN-LOCKOUT-11112026 · AC#n` theo thứ tự gạch đầu dòng của ticket.

## 2. Yêu cầu chức năng

### STORY-LOGIN-01 — Màn hình & validation đăng nhập

| REQ ID | Tên yêu cầu | Mô tả | Acceptance Criteria | Trạng thái | Cập nhật lần cuối | Nguồn |
|---|---|---|---|---|---|---|
| REQ-LOGIN-01 | Trang Login hiển thị form đăng nhập khi chưa đăng nhập | Là người dùng chưa đăng nhập, tôi thấy form để vào khu admin | Mở `/admin/authentication` trong phiên không cookie → thấy tiêu đề `Login`, ô `Email Address`, ô `Password`, checkbox `Remember me`, nút `Login`, link `Forgot Password?`; cả 5 phần tử có `offsetParent !== null` ở viewport 1598×790. `document.title` **chứa** `- Login` (phần trước là tên công ty, cấu hình được — không assert khớp tuyệt đối) | 🟢 | — | Kiểm chứng thực tế · `login_default_viewport.png` |
| REQ-LOGIN-02 | Ô Email Address được focus sẵn khi tải trang | Người dùng gõ email ngay không cần bấm chuột | Tải `/admin/authentication` → `#email` có thuộc tính `autofocus` và `document.activeElement.id === 'email'` | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-LOGIN-03 | Email sai định dạng bị trình duyệt chặn, không gửi form Login | Ô Email là `type=email`, trình duyệt kiểm định dạng trước khi gửi | Nhập `abc` vào Email → bấm `Login` → `form.checkValidity() === false`, `#email.validity.typeMismatch === true`, **không** có request `POST /admin/authentication`. Thông báo tham khảo (Chrome 146, tiếng Anh): "Please include an '@' in the email address. 'abc' is missing an '@'." — **CẤM assert chuỗi này** (do trình duyệt sinh) | 🟢 | — | Kiểm chứng thực tế (DOM + network) |
| REQ-LOGIN-04 | Ô Password che ký tự nhập | Mật khẩu không hiển thị dạng rõ | `#password` có `type === 'password'` | 🟢 | — | UI thực tế (DOM) |
| REQ-LOGIN-05 | Bỏ trống Email → thông báo bắt buộc nhập Email | Server từ chối khi Email trống | Bỏ trống Email (và Password) → bấm `Login` → trang ở lại `/admin/authentication`, hiển thị khối `.alert-danger` có nội dung **"The Email Address field is required."**. Chưa kiểm riêng trường hợp có Password (AMB-LOGIN-17) | 🟢 | — | Kiểm chứng thực tế · API · POST /admin/authentication · 200 · `login_empty_submit_viewport.png` |
| REQ-LOGIN-06 | Bỏ trống Password → thông báo bắt buộc nhập Password | Server từ chối khi Password trống | Email `recon.khongtontai@example.invalid`, Password trống → bấm `Login` → hiển thị **đúng một** khối `.alert-danger` nội dung **"The Password field is required."** | 🟢 | — | Kiểm chứng thực tế · API · POST /admin/authentication · 200 · `login_password_empty_viewport.png` |
| REQ-LOGIN-07 | Email không tồn tại → thông báo chung "Invalid email or password" | Thông báo không cho biết sai email hay sai mật khẩu | Email `recon.khongtontai@example.invalid` + mật khẩu bất kỳ → bấm `Login` → ở lại `/admin/authentication`, khối `.alert-danger` nội dung **"Invalid email or password"**. Trường hợp email tồn tại + sai mật khẩu chưa thử (AMB-LOGIN-11) | 🟢 | — | User thao tác · `login_invalid_credentials_viewport.png` |
| REQ-LOGIN-08 | Máy chủ không giữ lại giá trị Email sau khi đăng nhập lỗi | Sau mỗi lần server trả lỗi, ô Email trống | Trong profile **không có autofill**: gửi form có Email hợp lệ nhưng lỗi (REQ-LOGIN-06 hoặc 07) → trang tải lại → `#email.value === ''`. Lưu ý: trình duyệt có autofill có thể tự điền lại — TC phải chạy trên profile sạch | 🟢 | — | Kiểm chứng thực tế (DOM) · `login_password_empty_viewport.png` |
| REQ-LOGIN-14 | Form Login gửi kèm CSRF token | Chống giả mạo request | Form có `input[type=hidden][name=csrf_token_name]` với giá trị độ dài 32 ký tự (không chép giá trị). Request `POST /admin/authentication` có body gồm đúng các khoá `csrf_token_name, email, password` (khi không tick Remember me) | 🟢 | — | API · POST /admin/authentication · 200 |
| REQ-LOGIN-29 | Contact khách hàng không đăng nhập được vào khu admin | Tài khoản cổng khách hàng không dùng được cho `/admin` | Dùng email + mật khẩu của một Contact → bấm `Login` ở `/admin/authentication` → ở lại trang, khối `.alert-danger` nội dung **"Invalid email or password"**. **Chưa kiểm chứng** — chưa có account Contact | ⚪ | 05-11-2026 · Giải quyết AMB-LOGIN-03 | Assumption tạm AMB-LOGIN-03 |
| REQ-LOGIN-30 | Email tồn tại + sai mật khẩu → thông báo chung "Invalid email or password" | Không lộ email có tồn tại hay không | Email tồn tại + mật khẩu sai → bấm `Login` → ở lại trang, khối `.alert-danger` nội dung **"Invalid email or password"**. **Chưa kiểm chứng**. Chỉ chạy trên tài khoản test riêng (RISK-LOGIN-01). Áp khi tài khoản **chưa bị khoá** và chưa sai tới lần thứ 5 — từ ngưỡng khoá trở đi xem REQ-LOGIN-35, 37 (AMB-LOGIN-19). Không gửi quá 4 lần sai liên tiếp trong một lượt chạy | ⚪ | 11-11-2026 · ✏️ ghi rõ phạm vi theo LOGIN-LOCKOUT-11112026 | Assumption tạm AMB-LOGIN-11 |
| REQ-LOGIN-31 | Bỏ trống Email, có Password → chỉ hiện thông báo Email | Rule đối xứng với REQ-LOGIN-06 | Email trống + Password có giá trị → bấm `Login` → hiển thị **đúng một** khối `.alert-danger` nội dung **"The Email Address field is required."**. **Chưa kiểm chứng** | ⚪ | 05-11-2026 · Giải quyết AMB-LOGIN-17 | Assumption tạm AMB-LOGIN-17 |
| REQ-LOGIN-32 | Tài khoản bật 2FA phải nhập mã sau mật khẩu | Nhánh đăng nhập khi bật Email 2FA hoặc Google Authenticator | Tài khoản test đã bật 2FA + đăng nhập đúng mật khẩu → hiển thị bước nhập mã, **chưa** vào Dashboard. **Chưa kiểm chứng**: nội dung màn hình và luồng chi tiết chưa từng được quan sát | ⚪ | 05-11-2026 · Giải quyết AMB-LOGIN-15 | Assumption tạm AMB-LOGIN-15 |

### STORY-LOGIN-02 — Phiên & điều hướng

| REQ ID | Tên yêu cầu | Mô tả | Acceptance Criteria | Trạng thái | Cập nhật lần cuối | Nguồn |
|---|---|---|---|---|---|---|
| REQ-LOGIN-09 | Đăng nhập đúng → vào Dashboard | Người dùng hợp lệ vào khu admin | Đăng nhập bằng tài khoản admin hợp lệ → URL cuối là `/admin/`, `document.title` **chứa** `Dashboard` (không assert khớp tuyệt đối — tiêu đề có thể chèn số đếm), sidebar hiển thị | 🟢 | — | User thao tác · `login_success_landing_viewport.png` |
| REQ-LOGIN-10 | Sau đăng nhập luôn vào Dashboard, kể cả khi trước đó bị chặn ở trang khác | Hệ thống không nhớ trang đích ban đầu | Phiên không cookie → mở `/admin/clients` → bị đưa về trang Login → đăng nhập đúng → URL cuối là `/admin/` (không phải `/admin/clients`). Cố ý hay không: AMB-LOGIN-08 | 🟢 | — | User thao tác |
| REQ-LOGIN-11 | Chưa đăng nhập mở route admin → về trang Login | Route admin được bảo vệ | Phiên không cookie → mở `/admin/clients` (và `/admin/`) → điểm dừng là `/admin/authentication`, form Login hiển thị, **không** có thông báo. Chỉ assert điểm dừng — mã chuyển hướng quan sát được là 307 (AMB-LOGIN-09) | 🟢 | — | Kiểm chứng thực tế · API · GET /admin/clients → /admin/authentication |
| REQ-LOGIN-12 | Đã đăng nhập mở trang Login → về Dashboard | Không hiện lại form cho người đã đăng nhập | Đang đăng nhập → mở `/admin/authentication` → điểm dừng `/admin/`, title **chứa** `Dashboard`. Chỉ assert điểm dừng (AMB-LOGIN-09) | 🟢 | — | Kiểm chứng thực tế · API · GET /admin/authentication → /admin/ |
| REQ-LOGIN-13 | Đã đăng nhập mở trang Forgot Password → về Dashboard | Như trên cho trang quên mật khẩu | Đang đăng nhập → mở `/admin/authentication/forgot_password` → điểm dừng `/admin/`. Chỉ assert điểm dừng (AMB-LOGIN-09) | 🟢 | — | Kiểm chứng thực tế · API · GET /admin/authentication/forgot_password → /admin/ |

### STORY-LOGIN-03 — Ghi nhớ đăng nhập

| REQ ID | Tên yêu cầu | Mô tả | Acceptance Criteria | Trạng thái | Cập nhật lần cuối | Nguồn |
|---|---|---|---|---|---|---|
| REQ-LOGIN-15 | Tick Remember me khi đăng nhập tạo cookie `autologin` | Tác tạo của tính năng ghi nhớ — **được tạo đúng hình thái** | (1) Phiên không cookie, (2) xác nhận chưa có cookie `autologin` (chỉ có `csrf_cookie_name`, `sp_session`), (3) tick `Remember me` + đăng nhập đúng, (4) có cookie `autologin`: domain của hệ thống, path `/`, `Secure = true`, hạn ≈ **62 ngày** kể từ lúc đăng nhập, giá trị dài 110 ký tự (không chép giá trị) | 🟢 | — | User thao tác · cookie đọc qua CDP |
| REQ-LOGIN-16 | Cookie `autologin` khôi phục phiên khi phiên chính hết hạn | Tác tạo **dùng được đúng mục đích** | Có `autologin` hợp lệ, xoá `sp_session` (hoặc đợi hết hạn) → mở `/admin/` → vào Dashboard không cần nhập lại mật khẩu. **Chưa kiểm chứng** (AMB-LOGIN-12) | ⚪ | — | Suy từ tên cookie — chưa kiểm chứng |
| REQ-LOGIN-33 | Không tick Remember me thì không tạo cookie `autologin` | Ghi nhớ chỉ bật khi người dùng chọn | (1) Phiên không cookie, (2) xác nhận chưa có cookie `autologin`, (3) **không** tick `Remember me` + đăng nhập đúng, (4) không có cookie `autologin`. **Chưa kiểm chứng** | ⚪ | 05-11-2026 · Giải quyết AMB-LOGIN-18 | Assumption tạm AMB-LOGIN-18 |

### STORY-LOGIN-04 — Quên mật khẩu

| REQ ID | Tên yêu cầu | Mô tả | Acceptance Criteria | Trạng thái | Cập nhật lần cuối | Nguồn |
|---|---|---|---|---|---|---|
| REQ-LOGIN-17 | Link "Forgot Password?" mở trang quên mật khẩu | Lối vào luồng đặt lại mật khẩu | Ở trang Login bấm `Forgot Password?` → URL `/admin/authentication/forgot_password`, tiêu đề trang hiển thị `Forgot Password` | 🟢 | — | Kiểm chứng thực tế · API · GET /admin/authentication/forgot_password · 200 |
| REQ-LOGIN-18 | Trang Forgot Password hiển thị form nhập email | Form yêu cầu đặt lại | Thấy tiêu đề `Forgot Password`, ô `Email Address` (`type=email`), nút `Confirm`. Không có link quay lại Login — chỉ có logo trỏ về `/` (AMB-LOGIN-16) | 🟢 | — | Kiểm chứng thực tế · `forgot_password_default_viewport.png` |
| REQ-LOGIN-19 | Email sai định dạng bị trình duyệt chặn, không gửi form Forgot Password | Như REQ-LOGIN-03 cho form quên mật khẩu | Nhập `abc` → bấm `Confirm` → `form.checkValidity() === false`, `validity.typeMismatch === true`, không có request `POST /admin/authentication/forgot_password`. Cấm assert chuỗi thông báo của trình duyệt | 🟢 | — | Kiểm chứng thực tế (DOM + network) |
| REQ-LOGIN-20 | Forgot Password bỏ trống Email → thông báo "Email not found" | Hành vi hiện tại khi gửi form trống (nghi lỗi — AMB-LOGIN-05) | Bỏ trống Email → bấm `Confirm` → ở lại trang, khối `.alert-danger` nội dung **"Email not found"** | 🟢 | — | Kiểm chứng thực tế · API · POST /admin/authentication/forgot_password · 200 · `forgot_password_empty_submit_viewport.png` |
| REQ-LOGIN-21 | Forgot Password với email không tồn tại → thông báo "Email not found" | Hệ thống báo rõ email không có trong hệ thống (rủi ro dò tài khoản — AMB-LOGIN-06, RISK-LOGIN-02) | Email `recon.khongtontai@example.invalid` → bấm `Confirm` → khối `.alert-danger` nội dung **"Email not found"** | 🟢 | — | Kiểm chứng thực tế · API · POST /admin/authentication/forgot_password · 200 · `forgot_password_unknown_email_viewport.png` |
| REQ-LOGIN-22 | Forgot Password giữ lại giá trị Email sau lỗi | Người dùng không phải gõ lại | Sau REQ-LOGIN-21 → `#email.value === 'recon.khongtontai@example.invalid'` (khác REQ-LOGIN-08 — AMB-LOGIN-07) | 🟢 | — | Kiểm chứng thực tế (DOM) · `forgot_password_unknown_email_viewport.png` |
| REQ-LOGIN-23 | Forgot Password với email tồn tại gửi email đặt lại mật khẩu | Tác tạo của luồng quên mật khẩu — **được tạo** | Email tồn tại (hộp thư test riêng) → bấm `Confirm` → có thông báo thành công trên UI và hộp thư nhận email chứa link đặt lại. **Chưa kiểm chứng** (AMB-LOGIN-13, RISK-LOGIN-06) | ⚪ | — | Chưa kiểm chứng — môi trường dùng chung |
| REQ-LOGIN-24 | Link trong email đặt lại mở màn đặt mật khẩu mới | Tác tạo **dùng được** | Mở link trong email của REQ-LOGIN-23 → hiển thị màn đặt mật khẩu mới; đặt xong đăng nhập được bằng mật khẩu mới. **Chưa kiểm chứng** (AMB-LOGIN-13) | ⚪ | — | Chưa kiểm chứng — môi trường dùng chung |

### STORY-LOGIN-05 — Đăng xuất

| REQ ID | Tên yêu cầu | Mô tả | Acceptance Criteria | Trạng thái | Cập nhật lần cuối | Nguồn |
|---|---|---|---|---|---|---|
| REQ-LOGIN-25 | Menu avatar có mục Logout | Lối đăng xuất trên giao diện | Đang đăng nhập, bấm avatar ở header → dropdown mở gồm `My Profile · My Timesheets · Edit Profile · Language · Logout`; mục `Logout` (`a[onclick*="logout"]` trong dropdown) có `offsetParent !== null` sau khi mở, ở viewport 1598×790. Trước khi mở dropdown, mục này **không** hiển thị | 🟢 | — | Kiểm chứng thực tế · `logout_menu_open_viewport.png` |
| REQ-LOGIN-26 | Bấm Logout → về trang Login | Kết thúc phiên ngay, không hỏi xác nhận | Bấm `Logout` (khi không có timer đang chạy) → điểm dừng `/admin/authentication`, form Login hiển thị, không có hộp thoại xác nhận. Chỉ assert điểm dừng (AMB-LOGIN-09). Nhánh có timer đang chạy: AMB-LOGIN-14 | 🟢 | — | Kiểm chứng thực tế · API · GET /admin/authentication/logout → /admin/authentication · `logout_redirect_login_viewport.png` |
| REQ-LOGIN-27 | Sau Logout, route admin yêu cầu đăng nhập lại | Phiên thật sự bị huỷ | Sau REQ-LOGIN-26 → mở `/admin/` → điểm dừng `/admin/authentication` | 🟢 | — | Kiểm chứng thực tế · API · GET /admin/ → /admin/authentication |
| REQ-LOGIN-28 | Sau Logout, cookie `autologin` còn sót không khôi phục phiên | Đăng xuất vô hiệu hoá ghi nhớ đăng nhập dù cookie chưa bị xoá | (1) Đăng nhập có tick Remember me, (2) xác nhận cookie `autologin` tồn tại, (3) Logout, (4) xác nhận `autologin` **vẫn còn** trong trình duyệt, (5) mở `/admin/` → điểm dừng `/admin/authentication` (không tự đăng nhập lại). Việc cookie còn sót là RISK-LOGIN-03 | 🟢 | — | Kiểm chứng thực tế · cookie đọc qua CDP |
| REQ-LOGIN-34 | Logout khi có timer đang chạy hiện popup cảnh báo, không đăng xuất | Tránh mất thời gian đang tính | Có timer đang chạy → bấm `Logout` → hiện popup cảnh báo, URL không đổi, vẫn đang đăng nhập. **Chưa kiểm chứng trên UI** — mới đọc mã JS `logout()` | ⚪ | 05-11-2026 · Giải quyết AMB-LOGIN-14 | Assumption tạm AMB-LOGIN-14 · mã JS phía client |

### STORY-LOGIN-06 — Khoá tài khoản khi đăng nhập sai nhiều lần

> Nguồn: ticket do PO chốt, ghi nhận 11-11-2026 — mã nội bộ `LOGIN-LOCKOUT-11112026` (ticket không mang mã). Giải quyết AMB-LOGIN-10. **Toàn bộ ⚪ — chưa kiểm chứng trên hệ thống.**
> **Ràng buộc kiểm thử (gạch đầu dòng 6 của ticket, không phải hành vi hệ thống nên không cấp REQ):** môi trường dùng chung → TC của Story này dùng tài khoản **Project Manager**, **KHÔNG** dùng tài khoản Admin. Hiện chưa có tài khoản PM trong `.env` (AMB-LOGIN-24). Trước mỗi lượt: đăng nhập đúng một lần rồi Logout để đưa bộ đếm về 0 (REQ-LOGIN-39) — RISK-LOGIN-07.

| REQ ID | Tên yêu cầu | Mô tả | Acceptance Criteria | Trạng thái | Cập nhật lần cuối | Nguồn |
|---|---|---|---|---|---|---|
| REQ-LOGIN-35 | Sai mật khẩu 5 lần liên tiếp với cùng một email thì tài khoản bị khoá | Ngưỡng khoá là 5 lần sai liên tiếp | Tài khoản PM test: (1) đăng nhập đúng rồi Logout (bộ đếm = 0), (2) gửi form với email PM + mật khẩu sai **5 lần liên tiếp**, (3) lần thứ 6 gửi email PM + mật khẩu sai → hiển thị thông báo khoá (REQ-LOGIN-37), không vào Dashboard. **Biên dưới:** sau đúng 4 lần sai, lần thứ 5 nhập đúng mật khẩu → vào Dashboard. Thông báo của **chính** lần sai thứ 5: REQ-LOGIN-42. Lần gửi nào được tính là "sai": REQ-LOGIN-44 → 46 | ⚪ | 11-11-2026 · LOGIN-LOCKOUT-11112026 · Giải quyết AMB-LOGIN-10 | Ticket LOGIN-LOCKOUT-11112026 · AC#1 |
| REQ-LOGIN-36 | Khoá tự hết hiệu lực sau 15 phút | Tài khoản được thử đăng nhập lại sau thời hạn khoá | Tài khoản PM bị khoá theo REQ-LOGIN-35 ở thời điểm T (lần sai thứ 5) → **không** gửi thêm lần đăng nhập nào → ở T + 16 phút (15 phút + 1 phút biên an toàn) đăng nhập đúng mật khẩu → vào Dashboard. Không thử trong lúc khoá ở TC này — có thể gia hạn khoá (AMB-LOGIN-20). Bộ đếm sau khi hết khoá: AMB-LOGIN-25 | ⚪ | 11-11-2026 · LOGIN-LOCKOUT-11112026 | Ticket LOGIN-LOCKOUT-11112026 · AC#1 |
| REQ-LOGIN-37 | Tài khoản đang khoá → trang Login hiển thị thông báo khoá | Người dùng biết lý do không đăng nhập được và lúc nào thử lại | Tài khoản PM đang khoá → gửi form Login với email đó → ở lại `/admin/authentication`, trang hiển thị thông báo nguyên văn **"Your account is locked. Please try again in 15 minutes."** — số phút là chữ cố định theo Assumption tạm AMB-LOGIN-21 (TC gắn nhãn `assumption-based`; nếu thực tế là thời gian còn lại thì chỉ phần số đổi — skill 4.3.7). Vị trí, kiểu khối thông báo chưa quan sát — chưa assert class | ⚪ | 11-11-2026 · LOGIN-LOCKOUT-11112026 · Assumption tạm AMB-LOGIN-21 | Ticket LOGIN-LOCKOUT-11112026 · AC#2 |
| REQ-LOGIN-38 | Trong thời gian khoá, nhập đúng mật khẩu vẫn không đăng nhập được | Khoá chặn cả mật khẩu đúng | Tài khoản PM đang khoá (chưa đủ 15 phút) → nhập email PM + **mật khẩu đúng** → bấm `Login` → ở lại `/admin/authentication` kèm thông báo khoá (REQ-LOGIN-37), **không** vào Dashboard; mở tiếp `/admin/` → điểm dừng `/admin/authentication` (không có phiên). Lần thử này có thể gia hạn khoá (AMB-LOGIN-20) — TC tính thời gian chờ từ lần thử cuối | ⚪ | 11-11-2026 · LOGIN-LOCKOUT-11112026 | Ticket LOGIN-LOCKOUT-11112026 · AC#3 |
| REQ-LOGIN-39 | Đăng nhập thành công trước khi đủ 5 lần sai đặt bộ đếm lần sai về 0 | Lần sai cũ không cộng dồn qua một lần đăng nhập đúng | Tài khoản PM: (1) đăng nhập đúng rồi Logout, (2) sai mật khẩu 4 lần liên tiếp, (3) đăng nhập đúng → vào Dashboard → Logout, (4) sai mật khẩu thêm 4 lần liên tiếp, (5) đăng nhập đúng → **vào Dashboard** (tổng 8 lần sai nhưng không quá 4 lần liên tiếp → không bị khoá) | ⚪ | 11-11-2026 · LOGIN-LOCKOUT-11112026 | Ticket LOGIN-LOCKOUT-11112026 · AC#4 |
| REQ-LOGIN-40 | Khoá chỉ áp cho email bị sai — email khác đăng nhập được từ cùng máy | Không khoá theo IP: người khác cùng mạng không bị ảnh hưởng | Tài khoản PM-A đang khoá → trên **cùng máy, cùng mạng** (cùng IP), cửa sổ ẩn danh mới → đăng nhập tài khoản PM-B (không phải Admin) bằng mật khẩu đúng → vào Dashboard. Cần tài khoản PM thứ hai (AMB-LOGIN-24) | ⚪ | 11-11-2026 · LOGIN-LOCKOUT-11112026 | Ticket LOGIN-LOCKOUT-11112026 · AC#5 |
| REQ-LOGIN-41 | Tài khoản đang khoá cũng không đăng nhập được từ IP khác | Khoá gắn với email, không gắn với nơi đăng nhập | Tài khoản PM bị khoá từ máy/mạng 1 → trong 15 phút, từ máy/mạng có **IP khác** (VD mạng di động) đăng nhập email PM + mật khẩu đúng → không vào Dashboard, hiển thị thông báo khoá (REQ-LOGIN-37). Cần mạng thứ hai — chưa xác nhận QA có | ⚪ | 11-11-2026 · LOGIN-LOCKOUT-11112026 | Ticket LOGIN-LOCKOUT-11112026 · AC#5 |
| REQ-LOGIN-42 | Lần sai thứ 5 vẫn hiện thông báo chung; thông báo khoá hiện từ lần gửi thứ 6 | Lần sai làm tài khoản bị khoá chưa báo khoá | Tài khoản PM, bộ đếm = 0 (đăng nhập đúng rồi Logout) → sai mật khẩu 4 lần → **lần sai thứ 5**: ở lại trang Login, khối thông báo **"Invalid email or password"**, **không** có chữ `Your account is locked.` → lần gửi thứ 6 (mật khẩu bất kỳ): thông báo khoá (REQ-LOGIN-37). **Chưa kiểm chứng** | ⚪ | 11-11-2026 · Giải quyết AMB-LOGIN-19 | Assumption tạm AMB-LOGIN-19 |
| REQ-LOGIN-43 | Thử đăng nhập trong lúc khoá không gia hạn thời gian khoá | Khoá 15 phút tính cố định từ lần sai thứ 5 | Tài khoản PM bị khoá ở thời điểm T (lần sai thứ 5) → ở T + 10 phút gửi 1 lần đăng nhập (bị từ chối, thông báo khoá) → **không** gửi thêm → ở T + 16 phút đăng nhập đúng → vào Dashboard (nếu khoá trượt thì phải chờ tới T + 25 phút). **Chưa kiểm chứng** | ⚪ | 11-11-2026 · Giải quyết AMB-LOGIN-20 | Assumption tạm AMB-LOGIN-20 |
| REQ-LOGIN-44 | Gửi form với Password trống không tính là một lần đăng nhập sai | Lỗi bắt buộc nhập không cộng vào bộ đếm khoá | Tài khoản PM, bộ đếm = 0 → sai mật khẩu 4 lần → gửi email PM + Password **trống** 2 lần (mỗi lần hiện "The Password field is required.") → đăng nhập đúng → vào Dashboard (không bị khoá). **Chưa kiểm chứng** | ⚪ | 11-11-2026 · Giải quyết AMB-LOGIN-22 | Assumption tạm AMB-LOGIN-22 (a) |
| REQ-LOGIN-45 | Lần gửi bị từ chối do mã chống giả mạo sai không tính là một lần đăng nhập sai | Từ chối CSRF xảy ra trước khi kiểm mật khẩu | Tài khoản PM, bộ đếm = 0 → sai mật khẩu 4 lần → gửi form với mã `csrf_token_name` bị sửa (DevTools — cách làm như CRM_LOGIN_TC_043) 2 lần, bị từ chối → mở lại trang Login, đăng nhập đúng → vào Dashboard (không bị khoá). **Chưa kiểm chứng** | ⚪ | 11-11-2026 · Giải quyết AMB-LOGIN-22 | Assumption tạm AMB-LOGIN-22 (b) |
| REQ-LOGIN-46 | Lần sai ở email khác xen giữa không làm đứt chuỗi sai liên tiếp của một email | Bộ đếm lần sai riêng từng email | Tài khoản PM-A, bộ đếm = 0 → sai mật khẩu PM-A 3 lần → sai 1 lần với email không tồn tại riêng của TC (VD `recon.khongtontai+tc<nnn>@example.invalid`) → sai mật khẩu PM-A thêm 2 lần (tổng 5 lần sai của PM-A) → lần gửi tiếp theo với PM-A: thông báo khoá (REQ-LOGIN-37). **Chưa kiểm chứng** | ⚪ | 11-11-2026 · Giải quyết AMB-LOGIN-22 | Assumption tạm AMB-LOGIN-22 (c) |
| REQ-LOGIN-47 | Hết khoá thì bộ đếm lần sai về 0 | Sau khi được mở khoá, người dùng lại có đủ 5 lần thử | Tài khoản PM bị khoá rồi hết khoá (REQ-LOGIN-36, chờ ≥ 16 phút, không thử trong lúc khoá) → sai mật khẩu **1** lần → hiện **"Invalid email or password"**, không phải thông báo khoá → đăng nhập đúng → vào Dashboard. **Chưa kiểm chứng** | ⚪ | 11-11-2026 · Giải quyết AMB-LOGIN-25 | Assumption tạm AMB-LOGIN-25 |

> REQ-LOGIN-42 → 47 mô tả **Assumption tạm do user chốt** (11-11-2026) cho AMB-LOGIN-19, 20, 22, 25 — chưa ai quan sát; TC gắn nhãn `assumption-based`. AMB-LOGIN-23 (email không tồn tại có bị khoá) và AMB-LOGIN-26 (mở khoá sớm) chốt không cấp REQ — xem index.

> Tổng file: 47 REQ = 🟢 25 · ⚪ 22 (`REQ-LOGIN-16, 23, 24, 29 → 47`).

## 3. Đặc tả trường dữ liệu

### Form Login — `/admin/authentication` (`POST` cùng URL)

| Field (Label) | Loại UI | Required | Ràng buộc (min/max/format/default) | REQ liên quan | Ghi chú |
|---|---|---|---|---|---|
| Email Address | `input type=email` · `name=email` · `id=email` | Bắt buộc phía server (không có thuộc tính `required`) | Định dạng email do trình duyệt kiểm; không `maxlength`/`minlength`/`pattern`; `autofocus` | 01, 02, 03, 05, 08 | Bị xoá trống sau lỗi server |
| Password | `input type=password` · `name=password` · `id=password` | Bắt buộc phía server (không có thuộc tính `required`) | Không `maxlength`/`minlength` | 01, 04, 06 | — |
| Remember me | `input type=checkbox` · `name=remember` · `id=remember` | Không | Mặc định **không tick**; không tick thì không có trong body POST | 01, 15 | — |
| Login | `button type=submit` | — | — | 01 | — |
| Forgot Password? | link → `/admin/authentication/forgot_password` | — | — | 01, 17 | — |
| (ẩn) `csrf_token_name` | `input type=hidden` | — | Độ dài 32 ký tự, đổi theo phiên | 14 | Không chép giá trị |
| Logo | link → `/` | — | — | — | Trỏ về gốc site (ngoài khu admin) |

**Thứ tự focus (Tab):** Logo → Email Address → Password → Remember me → Login → Forgot Password?
**Không có:** reCAPTCHA · link đăng ký · hiển thị/ẩn mật khẩu.

### Form Forgot Password — `/admin/authentication/forgot_password` (`POST` cùng URL)

| Field (Label) | Loại UI | Required | Ràng buộc | REQ liên quan | Ghi chú |
|---|---|---|---|---|---|
| Email Address | `input type=email` · `name=email` · `id=email` | Không có thuộc tính `required`; server trả "Email not found" khi trống | Định dạng email do trình duyệt kiểm; không `maxlength`; **không** `autofocus` | 18, 19, 20, 21, 22 | Giữ giá trị sau lỗi |
| Confirm | `button type=submit` | — | — | 18 | — |
| (ẩn) `csrf_token_name` | `input type=hidden` | — | Độ dài 32 ký tự | — | Không chép giá trị |
| Logo | link → `/` | — | — | 18 | Không có link quay lại Login |

## 4. Business Rules & Validation Messages

| REQ ID | Rule / Trigger | Thông báo (nguyên văn) | Nơi hiển thị |
|---|---|---|---|
| REQ-LOGIN-05 | Login — Email trống | The Email Address field is required. | Khối `.alert.alert-danger` trên form |
| REQ-LOGIN-06 | Login — Password trống | The Password field is required. | Khối `.alert.alert-danger` trên form |
| REQ-LOGIN-05, 06 | Login — cả hai trống | Hai khối theo thứ tự: "The Password field is required." rồi "The Email Address field is required." | Thứ tự ngược ô trên form — AMB-LOGIN-04, TC không assert thứ tự |
| REQ-LOGIN-07 | Login — email không tồn tại | Invalid email or password | Khối `.alert.alert-danger` |
| REQ-LOGIN-30 | Login — email tồn tại, sai mật khẩu | Invalid email or password — ⚪ theo Assumption tạm, chưa quan sát | Khối `.alert.alert-danger` |
| REQ-LOGIN-31 | Login — Email trống, có Password | The Email Address field is required. — ⚪ theo Assumption tạm, chưa quan sát | Khối `.alert.alert-danger` |
| REQ-LOGIN-37 | Login — tài khoản đang bị khoá (sau 5 lần sai liên tiếp) | Your account is locked. Please try again in 15 minutes. — ⚪ nguyên văn theo ticket, chưa quan sát. Số phút là chữ cố định — Assumption tạm AMB-LOGIN-21 |
| REQ-LOGIN-42 | Login — lần sai mật khẩu thứ 5 (chính lần làm tài khoản bị khoá) | Invalid email or password — ⚪ Assumption tạm AMB-LOGIN-19; thông báo khoá hiện từ lần gửi thứ 6 |
| REQ-LOGIN-44 | Login — Password trống khi bộ đếm đang ở 4 | The Password field is required. — ⚪ không cộng vào bộ đếm (Assumption tạm AMB-LOGIN-22) | Chưa quan sát |
| REQ-LOGIN-20 | Forgot — Email trống | Email not found | Khối `.alert.alert-danger` |
| REQ-LOGIN-21 | Forgot — email không tồn tại | Email not found | Khối `.alert.alert-danger` |
| REQ-LOGIN-03, 19 | Email sai định dạng (cả hai form) | Thông báo của **trình duyệt** (Chrome 146): "Please include an '@' in the email address. 'abc' is missing an '@'." — **chỉ tham khảo, cấm assert** | Tooltip trình duyệt, không gửi request |

## 5. Luồng xử lý

**Đăng nhập thành công:** mở `/admin/authentication` → nhập Email + Password (tuỳ chọn tick Remember me) → `Login` → `POST /admin/authentication` → Dashboard `/admin/` (REQ-LOGIN-09). Nếu bắt đầu từ route khác, vẫn về Dashboard (REQ-LOGIN-10).

**Đăng nhập thất bại:** gửi form thiếu/sai → `POST /admin/authentication` trả lại trang Login kèm khối thông báo đỏ, ô Email và Password trống (REQ-LOGIN-05 → 08). Email sai định dạng thì trình duyệt chặn, không gửi request (REQ-LOGIN-03).

**Khoá tài khoản (⚪ theo ticket, chưa kiểm chứng):** sai mật khẩu 5 lần liên tiếp với cùng email → tài khoản bị khoá 15 phút (REQ-LOGIN-35, 36); trong lúc khoá, mọi lần đăng nhập — kể cả đúng mật khẩu — đều bị từ chối kèm "Your account is locked. Please try again in 15 minutes." (REQ-LOGIN-37, 38); đăng nhập đúng trước khi đủ 5 lần sai đặt bộ đếm về 0 (REQ-LOGIN-39); khoá theo email, không theo IP (REQ-LOGIN-40, 41). Theo Assumption tạm (11-11-2026): lần sai thứ 5 vẫn báo "Invalid email or password", thông báo khoá từ lần thứ 6 (REQ-LOGIN-42); thử trong lúc khoá không gia hạn khoá (REQ-LOGIN-43); Password trống và lần bị từ chối do mã chống giả mạo không tính là lần sai (REQ-LOGIN-44, 45); bộ đếm riêng từng email (REQ-LOGIN-46); hết khoá thì bộ đếm về 0 (REQ-LOGIN-47).

**Quên mật khẩu:** Login → `Forgot Password?` → nhập Email → `Confirm` → `POST /admin/authentication/forgot_password`. Email trống hoặc không tồn tại → "Email not found", email được giữ lại (REQ-LOGIN-20 → 22). Email tồn tại → ⚪ chưa kiểm chứng (REQ-LOGIN-23, 24).

**Đăng xuất:** avatar → `Logout` → `GET /admin/authentication/logout` → trang Login; route admin bị khoá lại (REQ-LOGIN-25 → 28).

## 6. Phát hiện tầng network

| Request | Kết quả quan sát | REQ |
|---|---|---|
| `POST /admin/authentication` | 200, trả lại trang (server-render); body khoá `csrf_token_name, email, password` (+ `remember` khi tick — chưa quan sát trực tiếp body có tick) | 05, 06, 07, 14 |
| `POST /admin/authentication/forgot_password` | 200, trả lại trang; body khoá `csrf_token_name, email` | 20, 21 |
| `GET /admin/clients`, `GET /admin/` khi chưa đăng nhập | Chuyển hướng 307 → `/admin/authentication` | 11, 27 |
| `GET /admin/authentication`, `GET …/forgot_password` khi đã đăng nhập | Chuyển hướng 307 → `/admin/` | 12, 13 |
| `GET /admin/authentication/logout` | Chuyển hướng 307 → `/admin/authentication` | 26 |

Không có endpoint JSON cho đăng nhập; không thấy request tới dịch vụ CAPTCHA. Trang Dashboard sau đăng nhập có tải `accounts.google.com/gsi/client` (Google Sign-In script) — không thấy nút đăng nhập Google trên trang Login.

## 7. Yêu cầu phi chức năng (quan sát được)

| Hạng mục | Quan sát |
|---|---|
| Giao thức | Toàn bộ qua HTTPS; cookie đều có cờ `Secure` |
| Cookie phiên `sp_session` | `HttpOnly`, `Secure`, `SameSite=Lax`, hạn **8 giờ trượt** (gia hạn mỗi request) |
| Cookie `csrf_cookie_name` | `HttpOnly`, `Secure`, `SameSite=Lax`, hạn ≈ 1 giờ trượt |
| Cookie `autologin` | `Secure`, **không** `HttpOnly`, **không** đặt `SameSite`, hạn ≈ 62 ngày; còn trong trình duyệt sau Logout — RISK-LOGIN-03 |
| Ngôn ngữ trang | `<html lang="en">`; chữ trên trang Login tiếng Anh |
| Chống tự động hoá | Không có CAPTCHA. Giới hạn số lần sai: theo ticket `LOGIN-LOCKOUT-11112026` khoá 15 phút sau 5 lần sai liên tiếp, theo email (REQ-LOGIN-35 → 47) — ⚪ chưa kiểm chứng |
| Viewport | Chỉ khảo sát ở 1598×790 — chưa kiểm responsive |

## 8. Danh mục Evidence

Thư mục [`evidence/`](evidence/) — Chrome 146, viewport 1598×790. Hậu tố `_viewport` vì form nằm trọn trong màn hình.

| Tệp | Màn hình | Trạng thái | REQ |
|---|---|---|---|
| [login_default_viewport.png](evidence/login_default_viewport.png) | Login | Mặc định, phiên không cookie | 01, 02 |
| [login_empty_submit_viewport.png](evidence/login_empty_submit_viewport.png) | Login | Gửi form trống — 2 thông báo | 05 |
| [login_password_empty_viewport.png](evidence/login_password_empty_viewport.png) | Login | Email hợp lệ, Password trống — 1 thông báo, Email bị xoá | 06, 08 |
| [login_invalid_credentials_viewport.png](evidence/login_invalid_credentials_viewport.png) | Login | Email không tồn tại — "Invalid email or password" | 07 |
| [login_success_landing_viewport.png](evidence/login_success_landing_viewport.png) | Dashboard | Ngay sau đăng nhập đúng | 09, 10 |
| [forgot_password_default_viewport.png](evidence/forgot_password_default_viewport.png) | Forgot Password | Mặc định | 17, 18 |
| [forgot_password_empty_submit_viewport.png](evidence/forgot_password_empty_submit_viewport.png) | Forgot Password | Gửi trống — "Email not found" | 20 |
| [forgot_password_unknown_email_viewport.png](evidence/forgot_password_unknown_email_viewport.png) | Forgot Password | Email không tồn tại — "Email not found", email giữ lại | 21, 22 |
| [logout_menu_open_viewport.png](evidence/logout_menu_open_viewport.png) | Dashboard | Dropdown avatar đang mở | 25 |
| [logout_redirect_login_viewport.png](evidence/logout_redirect_login_viewport.png) | Login | Ngay sau Logout | 26 |

Mọi ảnh đã được mở lại xác nhận đúng trạng thái. REQ không có ảnh (02, 03, 04, 11–15, 19, 27, 28) dựa trên đọc DOM / network / cookie có ghi số liệu trong AC; REQ ⚪ (16, 23, 24, 29 → 47) chưa có bằng chứng.
