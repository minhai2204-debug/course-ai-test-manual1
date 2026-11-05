# Requirements Web — Đăng nhập (`LOGIN`)

> ← [Index module `REQUIREMENTS_LOGIN_SUMMARY.md`](../REQUIREMENTS_LOGIN_SUMMARY.md) — phân quyền · trạng thái phiên · AMB/RISK · Story · Nhật ký nằm ở index.

## 1. Metadata khảo sát

| Thuộc tính | Giá trị |
|---|---|
| **Nền tảng** | Web — khu admin |
| **REQ trong file** | `REQ-LOGIN-01` → `REQ-LOGIN-34` (34 REQ) |
| **Trình duyệt khảo sát** | Google Chrome 146 (headed, máy local, profile tạm), viewport `1598×790`, điều khiển qua Chrome DevTools Protocol. Mọi AC dựa trên thông báo mặc định của trình duyệt **chỉ đúng với trình duyệt này** |
| **Phiên khảo sát** | Cửa sổ Chrome **tách biệt, không cookie** (browser context riêng) — không ảnh hưởng phiên khác. Các bước cần gõ mật khẩu do **user tự thao tác**; agent đọc DOM + chụp ảnh |
| **Tầng network** | Quan sát thụ động request do UI phát sinh (`Network.*` của CDP). Không gọi API trực tiếp |
| **Ngày** | 02-11-2026 |

**Quy ước cột `Nguồn`:** `Kiểm chứng thực tế` = đã thao tác và xác nhận · `UI thực tế` = chỉ quan sát · `API · <method> <route> · <status>` = từ tầng network · `User thao tác` = bước do user gõ, agent quan sát kết quả.
**Trạng thái ⚪ trong file này** = chưa kiểm chứng được trên môi trường dùng chung (skill 4.3.8), luôn kèm AMB. REQ-LOGIN-29 → 34 mô tả **Assumption tạm do user chốt** (05-11-2026), chưa ai quan sát hành vi này trên hệ thống — TC gắn nhãn `assumption-based`.

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
| REQ-LOGIN-30 | Email tồn tại + sai mật khẩu → thông báo chung "Invalid email or password" | Không lộ email có tồn tại hay không | Email tồn tại + mật khẩu sai → bấm `Login` → ở lại trang, khối `.alert-danger` nội dung **"Invalid email or password"**. **Chưa kiểm chứng**. Chỉ chạy trên tài khoản test riêng (RISK-LOGIN-01) | ⚪ | 05-11-2026 · Giải quyết AMB-LOGIN-11 | Assumption tạm AMB-LOGIN-11 |
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

> Tổng file: 34 REQ = 🟢 25 · ⚪ 9 (`REQ-LOGIN-16, 23, 24, 29 → 34`).

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
| REQ-LOGIN-20 | Forgot — Email trống | Email not found | Khối `.alert.alert-danger` |
| REQ-LOGIN-21 | Forgot — email không tồn tại | Email not found | Khối `.alert.alert-danger` |
| REQ-LOGIN-03, 19 | Email sai định dạng (cả hai form) | Thông báo của **trình duyệt** (Chrome 146): "Please include an '@' in the email address. 'abc' is missing an '@'." — **chỉ tham khảo, cấm assert** | Tooltip trình duyệt, không gửi request |

## 5. Luồng xử lý

**Đăng nhập thành công:** mở `/admin/authentication` → nhập Email + Password (tuỳ chọn tick Remember me) → `Login` → `POST /admin/authentication` → Dashboard `/admin/` (REQ-LOGIN-09). Nếu bắt đầu từ route khác, vẫn về Dashboard (REQ-LOGIN-10).

**Đăng nhập thất bại:** gửi form thiếu/sai → `POST /admin/authentication` trả lại trang Login kèm khối thông báo đỏ, ô Email và Password trống (REQ-LOGIN-05 → 08). Email sai định dạng thì trình duyệt chặn, không gửi request (REQ-LOGIN-03).

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
| Chống tự động hoá | Không có CAPTCHA; giới hạn số lần sai chưa rõ (AMB-LOGIN-10) |
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

Mọi ảnh đã được mở lại xác nhận đúng trạng thái. REQ không có ảnh (02, 03, 04, 11–15, 19, 27, 28) dựa trên đọc DOM / network / cookie có ghi số liệu trong AC; REQ ⚪ (16, 23, 24, 29 → 34) chưa có bằng chứng.
