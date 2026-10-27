# SRS – Module Login (Perfex CRM | Anh Tester Demo)

| Mục | Nội dung |
|---|---|
| Tài liệu | Software Requirements Specification – Module Login |
| Hệ thống | Perfex CRM – Anh Tester Demo |
| URL | https://crm.anhtester.com/admin/authentication |
| Phiên bản | 1.1 (Draft) |
| Ngày | 2026-10-27 |
| Nguồn | Khảo sát giao diện trang Login và Forgot Password (reverse-engineering) |

> **Ghi chú về độ tin cậy.** Các yêu cầu được đánh dấu **[Quan sát]** được xác nhận trực tiếp từ giao diện/DOM của trang, hoặc từ phiên đăng nhập do người dùng tự thực hiện (Claude không nhập mật khẩu). Các yêu cầu đánh dấu **[Giả định]** (thông báo lỗi, khóa tài khoản, thời hạn Remember me...) **chưa được kiểm chứng**; cần QA xác nhận lại trên hệ thống trước khi dùng làm căn cứ nghiệm thu.
>
> **Phiên bản 1.1:** bổ sung kết quả sau đăng nhập (mục 3.3): Dashboard, menu, menu người dùng và hành vi chuyển hướng khi đã đăng nhập.

---

## 1. Giới thiệu

### 1.1 Mục đích
Mô tả yêu cầu chức năng và phi chức năng của module Login, cho phép người dùng quản trị (Admin/Staff) xác thực để truy cập khu vực `/admin` của Perfex CRM. Tài liệu dùng làm đầu vào để thiết kế test case.

### 1.2 Phạm vi
Bao gồm:
- Màn hình đăng nhập (Login)
- Tùy chọn "Remember me"
- Liên kết và màn hình "Forgot Password"

Không bao gồm: đăng ký tài khoản, đăng nhập khách hàng (Client portal), phân quyền chi tiết sau đăng nhập, đăng xuất, 2FA (không quan sát thấy trên giao diện).

### 1.3 Định nghĩa
| Thuật ngữ | Ý nghĩa |
|---|---|
| Staff/Admin | Người dùng nội bộ truy cập `/admin` |
| CSRF | Cross-Site Request Forgery – token chống giả mạo request |
| Dashboard | Trang chính sau khi đăng nhập thành công |

### 1.4 Đối tượng sử dụng
Staff, Admin của hệ thống CRM.

---

## 2. Mô tả tổng quan

### 2.1 Bối cảnh sản phẩm
Module Login là cổng vào duy nhất của khu vực quản trị. Hệ thống xây dựng trên Perfex CRM (PHP/CodeIgniter), form gửi bằng HTTP POST kèm CSRF token.

### 2.2 Ràng buộc & giả định
- Trình duyệt hiện đại hỗ trợ HTML5 (input `type="email"` có validate định dạng sẵn).
- Hệ thống dùng chung một trang login cho mọi tài khoản staff.
- Dữ liệu demo công khai, có thể bị thay đổi bởi nhiều người.

---

## 3. Giao diện người dùng

### 3.1 Màn hình Login `/admin/authentication` **[Quan sát]**

| # | Thành phần | Loại | Thuộc tính quan sát được |
|---|---|---|---|
| 1 | Logo Anh Tester | Image + link | Liên kết về `https://crm.anhtester.com/` |
| 2 | Tiêu đề "Login" | Heading | – |
| 3 | Email Address | Input `type=email` | `name=email`, `id=email`, autofocus, không có `required`/`maxlength`/placeholder/autocomplete |
| 4 | Password | Input `type=password` | `name=password`, `id=password`, không có `required`/`maxlength`, giá trị bị che |
| 5 | Remember me | Checkbox | `name=remember`, `id=remember`, mặc định bỏ chọn |
| 6 | Nút Login | Button `type=submit` | Nhãn "Login" |
| 7 | Forgot Password? | Link | → `/admin/authentication/forgot_password` |
| 8 | CSRF token | Input hidden | `name=csrf_token_name` |

Form: `method=POST`, `action=/admin/authentication`, **không** có `novalidate` (validate HTML5 của trình duyệt hoạt động).

Tiêu đề trang: `Perfex CRM | Anh Tester Demo - Login`. Ngôn ngữ: `en`.

### 3.2 Màn hình Forgot Password `/admin/authentication/forgot_password` **[Quan sát]**

| # | Thành phần | Loại | Ghi chú |
|---|---|---|---|
| 1 | Tiêu đề "Forgot Password" | Heading | – |
| 2 | Email Address | Input `type=email` | – |
| 3 | Nút Confirm | Button submit | – |
| 4 | CSRF token | Input hidden | – |

### 3.3 Màn hình sau khi đăng nhập thành công `/admin/` **[Quan sát]**

- URL đích: `https://crm.anhtester.com/admin/`, tiêu đề trang "Dashboard".
- Thanh menu bên trái: Dashboard, Customers, Projects, Tasks, Contracts, Sales (có menu con), Subscriptions, Expenses, Support, Leads, Estimate Request, Knowledge Base, Utilities (có menu con), Reports (có menu con).
- Thanh trên cùng: ô tìm kiếm, biểu tượng thông báo, avatar người dùng.
- Menu avatar gồm: My Profile (`/admin/profile`), Edit Profile (`/admin/staff/edit_profile`), Logout.
- Dashboard hiển thị các widget Invoice overview, Estimate overview, Proposal overview.
- Truy cập lại `/admin/authentication` khi đã đăng nhập → tự chuyển về `/admin/`.

---

## 4. Yêu cầu chức năng

### 4.1 Đăng nhập

| ID | Yêu cầu | Độ ưu tiên | Trạng thái |
|---|---|---|---|
| FR-LG-01 | Hệ thống hiển thị form Login gồm Email, Password, Remember me, nút Login, link Forgot Password khi truy cập `/admin/authentication`. | Cao | [Quan sát] |
| FR-LG-02 | Con trỏ tự động focus vào trường Email khi tải trang. | Thấp | [Quan sát] |
| FR-LG-03 | Trường Email chỉ chấp nhận chuỗi đúng định dạng email (validate HTML5 `type=email`). | Cao | [Quan sát] |
| FR-LG-04 | Trường Password hiển thị dạng che ký tự (mask). | Cao | [Quan sát] |
| FR-LG-05 | Khi nhập đúng email và mật khẩu của tài khoản hợp lệ và nhấn Login, hệ thống xác thực và chuyển người dùng tới Dashboard tại `/admin/` (tiêu đề trang "Dashboard"). | Cao | [Quan sát – người dùng tự đăng nhập, đã thấy Dashboard] |
| FR-LG-06 | Khi email không tồn tại hoặc mật khẩu sai, hệ thống ở lại trang Login và hiển thị thông báo lỗi chung (không tiết lộ email hay mật khẩu sai). | Cao | [Giả định] |
| FR-LG-07 | Khi để trống Email hoặc Password và nhấn Login, hệ thống không đăng nhập và hiển thị thông báo bắt buộc nhập (từ trình duyệt hoặc từ server). | Cao | [Giả định] |
| FR-LG-08 | Khi tài khoản bị vô hiệu hóa (inactive), hệ thống từ chối đăng nhập và hiển thị thông báo phù hợp. | Trung bình | [Giả định] |
| FR-LG-09 | Người dùng có thể nhấn Enter ở trường Email/Password để submit form. | Trung bình | [Giả định] |
| FR-LG-10 | Mỗi lần submit form gửi kèm CSRF token hợp lệ; request thiếu hoặc sai token bị từ chối. | Cao | [Quan sát: có token; Giả định: từ chối] |
| FR-LG-11 | Người dùng đã đăng nhập mà truy cập lại `/admin/authentication` được chuyển hướng về `/admin/` (Dashboard). | Thấp | [Quan sát] |
| FR-LG-12 | Truy cập trực tiếp URL trong `/admin` khi chưa đăng nhập bị chuyển hướng về trang Login. | Cao | [Giả định] |

### 4.2 Remember me

| ID | Yêu cầu | Độ ưu tiên | Trạng thái |
|---|---|---|---|
| FR-RM-01 | Checkbox "Remember me" mặc định không được chọn. | Thấp | [Quan sát] |
| FR-RM-02 | Khi chọn Remember me và đăng nhập thành công, phiên đăng nhập được duy trì lâu hơn (cookie persistent) sau khi đóng và mở lại trình duyệt. | Trung bình | [Giả định] |
| FR-RM-03 | Khi không chọn Remember me, phiên đăng nhập kết thúc khi đóng trình duyệt/hết hạn session. | Trung bình | [Giả định] |

### 4.3 Quên mật khẩu

| ID | Yêu cầu | Độ ưu tiên | Trạng thái |
|---|---|---|---|
| FR-FP-01 | Link "Forgot Password?" điều hướng tới `/admin/authentication/forgot_password`. | Cao | [Quan sát] |
| FR-FP-02 | Màn hình Forgot Password gồm trường Email (`type=email`) và nút Confirm. | Cao | [Quan sát] |
| FR-FP-03 | Khi nhập email hợp lệ của tài khoản tồn tại và nhấn Confirm, hệ thống gửi email hướng dẫn đặt lại mật khẩu và hiển thị thông báo xác nhận. | Cao | [Giả định] |
| FR-FP-04 | Khi email không tồn tại hoặc để trống, hệ thống hiển thị thông báo lỗi tương ứng và không gửi email. | Trung bình | [Giả định] |

---

## 5. Yêu cầu phi chức năng

| ID | Loại | Yêu cầu | Trạng thái |
|---|---|---|---|
| NFR-SEC-01 | Bảo mật | Mật khẩu không được hiển thị plaintext trên giao diện và không xuất hiện trong URL (form dùng POST). | [Quan sát] |
| NFR-SEC-02 | Bảo mật | Toàn bộ trang Login phải được truyền qua HTTPS. | [Quan sát: URL https] |
| NFR-SEC-03 | Bảo mật | Chống CSRF bằng token trên cả form Login và Forgot Password. | [Quan sát] |
| NFR-SEC-04 | Bảo mật | Thông báo lỗi đăng nhập không cho biết email tồn tại hay không (chống user enumeration). | [Giả định] |
| NFR-SEC-05 | Bảo mật | Đầu vào email/password phải được xử lý chống SQL Injection và XSS. | [Giả định] |
| NFR-SEC-06 | Bảo mật | Có cơ chế hạn chế brute-force (giới hạn số lần đăng nhập sai / khóa tạm). | [Giả định – cần xác minh] |
| NFR-USA-01 | Khả dụng | Giao diện responsive, hiển thị đúng trên desktop, tablet, mobile. | [Giả định] |
| NFR-USA-02 | Khả dụng | Có thể thao tác bằng bàn phím (Tab qua các trường, Enter để submit); label gắn với input. | [Quan sát: có label] |
| NFR-USA-03 | Khả dụng | Ngôn ngữ giao diện: tiếng Anh. | [Quan sát] |
| NFR-PER-01 | Hiệu năng | Trang Login tải trong ≤ 3 giây, xử lý đăng nhập phản hồi ≤ 3 giây trong điều kiện mạng bình thường. | [Giả định] |
| NFR-CMP-01 | Tương thích | Hoạt động trên Chrome, Firefox, Edge, Safari bản mới nhất. | [Giả định] |

---

## 6. Luồng nghiệp vụ

### 6.1 Đăng nhập thành công
1. Người dùng mở `/admin/authentication`.
2. Nhập Email và Password hợp lệ (tùy chọn: chọn Remember me).
3. Nhấn **Login**.
4. Hệ thống kiểm tra CSRF token, xác thực thông tin.
5. Thành công → chuyển tới Dashboard.

### 6.2 Đăng nhập thất bại
1–3. Như trên.
4. Hệ thống xác thực không thành công.
5. Giữ nguyên trang Login, hiển thị thông báo lỗi; các trường được xử lý theo hành vi thực tế của hệ thống (cần xác nhận có giữ lại email hay không).

### 6.3 Quên mật khẩu
1. Người dùng nhấn **Forgot Password?**.
2. Nhập Email, nhấn **Confirm**.
3. Hệ thống gửi email đặt lại mật khẩu (nếu email tồn tại) và thông báo kết quả.

---

## 7. Quy tắc nghiệp vụ & ràng buộc dữ liệu

| ID | Trường | Quy tắc |
|---|---|---|
| BR-01 | Email | Bắt buộc (nghiệp vụ); phải đúng định dạng `local@domain`. Không giới hạn độ dài phía client (`maxlength` không đặt). |
| BR-02 | Password | Bắt buộc (nghiệp vụ); phân biệt hoa/thường; không giới hạn độ dài phía client. |
| BR-03 | Remember me | Boolean, mặc định `false`. |

---

## 8. Dữ liệu kiểm thử gợi ý

> Thông tin đăng nhập tài khoản demo do người yêu cầu cung cấp **không** được ghi vào tài liệu này; QA lấy từ nguồn nội bộ khi chạy test.

| Nhóm | Ví dụ giá trị |
|---|---|
| Email hợp lệ | Tài khoản admin demo (lấy từ nguồn nội bộ) |
| Email sai định dạng | `abc`, `abc@`, `@abc.com`, `a b@c.com` |
| Email không tồn tại | `notexist@example.com` |
| Password sai | Chuỗi bất kỳ khác mật khẩu đúng |
| Biên | Chuỗi rỗng, toàn khoảng trắng, 255+ ký tự, ký tự Unicode |
| Bảo mật | `' OR '1'='1`, `<script>alert(1)</script>` |

---

## 9. Ma trận truy vết (Requirement → Kịch bản kiểm thử gợi ý)

| Yêu cầu | Kịch bản kiểm thử |
|---|---|
| FR-LG-01, FR-LG-02 | Kiểm tra UI và focus mặc định |
| FR-LG-03 | Nhập email sai định dạng → bị chặn |
| FR-LG-04 | Password bị che |
| FR-LG-05 | Đăng nhập hợp lệ |
| FR-LG-06 | Sai email / sai password |
| FR-LG-07 | Bỏ trống từng trường / cả hai |
| FR-LG-08 | Tài khoản inactive |
| FR-LG-09 | Submit bằng Enter |
| FR-LG-10 | Gửi request không có / sai CSRF token |
| FR-LG-11, FR-LG-12 | Điều hướng khi đã/chưa đăng nhập |
| FR-RM-01..03 | Chọn/không chọn Remember me, mở lại trình duyệt |
| FR-FP-01..04 | Luồng quên mật khẩu |
| NFR-SEC-04..06 | Enumeration, injection, brute-force |
| NFR-USA/CMP | Responsive, trình duyệt, bàn phím |

---

## 10. Câu hỏi mở

1. Thông báo lỗi chính xác khi sai thông tin đăng nhập, khi bỏ trống trường?
2. Có cơ chế khóa tài khoản/giới hạn đăng nhập sai không, ngưỡng bao nhiêu?
3. Thời gian sống của session và của cookie Remember me?
4. Có 2FA / captcha cho tài khoản staff không?
5. Link reset mật khẩu có hiệu lực bao lâu; thông báo khi email không tồn tại?
6. Trang đích sau đăng nhập có phụ thuộc quyền (role) của tài khoản không?
