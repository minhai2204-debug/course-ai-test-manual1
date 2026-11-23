# STORY-CUST-03 — Liên hệ của khách hàng (Contacts)

> ← [Index module `REQUIREMENTS_CUSTOMERS_SUMMARY.md`](../../REQUIREMENTS_CUSTOMERS_SUMMARY.md) · [File web](../requirements_customers_web.md)
>
> **Phạm vi:** tab `Contacts` của hồ sơ KH (`?group=contacts`) · modal thêm/sửa contact (`/admin/clients/form_contact/{customer_id}`) · trang tổng `/admin/clients/all_contacts`. Đăng nhập của contact thuộc cổng khách hàng — **ngoài phạm vi** (đã chốt khi `/discover-system`).
> **REQ:** `REQ-CUST-53` → `REQ-CUST-72` (20 REQ) · **AMB:** AMB-CUST-17, 18 · **RISK:** — (RISK-CUST-03 dùng chung với Story 01)

## 1. Yêu cầu chức năng

| REQ ID | Tên yêu cầu | Mô tả | Acceptance Criteria | Trạng thái | Cập nhật lần cuối | Nguồn |
|---|---|---|---|---|---|---|
| REQ-CUST-53 | Tab Contacts có nút New Contact và bảng 6 cột | Danh sách liên hệ của một KH | `?group=contacts` → nút `New Contact` (`onclick="contact(<customer_id>)"`), bảng cột `Full Name · Email · Position · Phone · Active · Last Login`; KH chưa có contact → `No entries found`. Ở viewport 973×853 bảng cuộn ngang, cột Active/Last Login nằm ngoài khung (AMB-CUST-16) | 🟢 | — | Kiểm chứng thực tế · `cust_contacts_tab_after_add_viewport.png` |
| REQ-CUST-54 | Modal Add new contact có đủ trường, phụ đề là tên KH | Form tạo liên hệ | `New Contact` → modal `#contact`, tiêu đề `Add new contact`, phụ đề = Company của KH; trường theo thứ tự: `Profile image` (file) · `* First Name` · `* Last Name` · `Position` · `* Email` (`type=email`) · `Phone` · `Direction` (System Default/LTR/RTL) · `* Password` (nút hiện mật khẩu + nút sinh mật khẩu) · `Primary Contact` · `Do not send welcome email` · `Send SET password email` · khối `Permissions` · khối `Email Notifications`; nút `Close`, `Save` | 🟢 | — | Kiểm chứng thực tế (DOM) · `cust_contact_new_modal_empty_submit_viewport.png` |
| REQ-CUST-55 | Bỏ trống → 4 thông báo bắt buộc | Validation tạo contact | Modal trống → `Save` → đúng 4 lỗi **"This field is required."** tại `#firstname-error`, `#lastname-error`, `#email-error`, `#password-error`; modal không đóng | 🟢 | — | Kiểm chứng thực tế (DOM) · `cust_contact_new_modal_empty_submit_viewport.png` |
| REQ-CUST-56 | Email sai định dạng → "Please enter a valid email address." | Kiểm định dạng email do ứng dụng (jQuery Validate) | Nhập `abc` vào Email → `$(email).valid() === false`, `#email-error` nội dung **"Please enter a valid email address."** | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-57 | Email đã thuộc contact khác → "Email already exists" | Email contact là duy nhất toàn hệ thống | Nhập email của một contact đã có → rời ô → request `POST /admin/misc/contact_email_exists` → `#email-error` **"Email already exists"**, form không hợp lệ | 🟢 | — | Kiểm chứng thực tế · API · POST /admin/misc/contact_email_exists · 200 |
| REQ-CUST-58 | Ô Phone điền sẵn mã quốc gia của KH | Gợi ý đầu số | KH có Country `Vietnam` → mở `New Contact` → `phonenumber.value === '+84'`. Trường hợp KH không có Country chưa kiểm (AMB-CUST-18) | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-59 | Tick "Send SET password email" bỏ yêu cầu nhập mật khẩu | Contact tự đặt mật khẩu qua email | Tick `Send SET password email` → khối Password bị tổ tiên `client_password_set_wrapper hide` ẩn, `$(password).valid() === true` khi trống; bỏ tick → Password hiện lại và bắt buộc | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-60 | Nút sinh mật khẩu điền mật khẩu ngẫu nhiên 12 ký tự | Tạo mật khẩu nhanh | Bấm biểu tượng làm mới (`a.generate_password`) → ô Password có giá trị dài **12** ký tự, vẫn `type=password` (không chép giá trị) | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-61 | Contact đầu tiên của KH mặc định là Primary Contact | Liên hệ chính | KH chưa có contact → `New Contact` → `is_primary.checked === true` | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-62 | 6 quyền của contact bật sẵn | Quyền ở cổng khách hàng | Khối `Permissions` (ghi chú "Make sure to set appropriate permissions for this contact") gồm 6 công tắc `permissions[]`: `Invoices` (1) · `Estimates` (2) · `Contracts` (3) · `Proposals` (4) · `Support` (5) · `Projects` (6), cả 6 `checked` khi tạo mới. Mặc định lấy từ cấu hình Setup (module `SETTING`, BLOCKED) | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-63 | 7 loại email thông báo bật sẵn | Email gửi tới contact | Khối `Email Notifications` gồm 7 công tắc `invoice_emails · estimate_emails · credit_note_emails · project_emails · ticket_emails · task_emails · contract_emails` (nhãn Invoice/Estimate/Credit Note/Project/Tickets/Task/Contract), cả 7 `checked` khi tạo mới | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-64 | Lưu contact hợp lệ → báo thành công, dòng mới trong bảng | Kết quả tạo contact | Điền First/Last Name, Email `auto_cust_contact_<timestamp>@auto.test`, sinh mật khẩu, tick `Do not send welcome email` → `Save` → request `POST /admin/clients/form_contact/<customer_id>` 200, thông báo **"Contact added successfully."**, modal đóng, bảng có dòng `<First> <Last>` + email + position + phone | 🟢 | — | Kiểm chứng thực tế · `cust_contacts_tab_after_add_viewport.png` |
| REQ-CUST-65 | Danh sách KH hiện tên và email của Primary Contact | Liên kết KH ↔ contact chính | Sau REQ-CUST-64 → `/admin/clients` lọc KH test → cột `Primary Contact` = `<First> <Last>`, `Primary Email` = email contact. KH tạo bằng Import (REQ-CUST-76) cũng vậy | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-66 | Sửa contact: Password không bắt buộc, có ghi chú đổi mật khẩu | Không buộc nhập lại mật khẩu | Bấm tên contact → modal tiêu đề = tên contact; ô Password không có rule `required`; ghi chú nguyên văn **"Note: if you populate this field, password will be changed on this contact."** | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-67 | Contact chính duy nhất không bỏ được cờ Primary | Luôn có một liên hệ chính | Sửa contact chính duy nhất → `is_primary.checked === true` và `is_primary.disabled === true` | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-68 | Sửa contact và lưu → báo cập nhật thành công | Kết quả sửa | Đổi `Position` thành `QA auto sửa` → `Save` → **"Contact updated successfully."**, bảng hiển thị giá trị mới (giữ dấu tiếng Việt) | 🟢 | — | Kiểm chứng thực tế |
| REQ-CUST-69 | Công tắc Active của contact đổi trạng thái ngay, lưu bền | Bật/tắt liên hệ | Bấm công tắc Active trên dòng contact test → `GET /admin/clients/change_contact_status/<contact_id>/0` trả 200; tải lại → công tắc tắt; bấm lại → bật | 🟢 | — | Kiểm chứng thực tế · API · GET /admin/clients/change_contact_status/{id}/{0\|1} · 200 |
| REQ-CUST-70 | Trang Contacts tổng liệt kê mọi contact | Tra cứu liên hệ toàn hệ thống | Nút `Contacts` ở danh sách KH → `/admin/clients/all_contacts`, `document.title` **chứa** `Contacts`; bảng cột `First Name · Last Name · Email · Company · Phone · Position · Last Login · Active`, sắp xếp mặc định `First Name` tăng dần; tổng `Showing … of N entries` = `Active Contacts + Inactive Contacts` của Summary (đo: 409 = 404 + 5) | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-71 | Hiệu lực của cờ Active, welcome email và Set password email ở cổng khách hàng | Tác tạo của contact — **dùng được** | (a) contact Inactive không đăng nhập được cổng KH; (b) bỏ tick `Do not send welcome email` → contact nhận email chào mừng; (c) tick `Send SET password email` → nhận email đặt mật khẩu. **Chưa kiểm chứng** — cổng KH ngoài phạm vi, chưa có hộp thư test (AMB-CUST-17) | ⚪ | — | Chưa kiểm chứng |
| REQ-CUST-72 | Xoá contact sau khi xác nhận | Gỡ liên hệ | Dòng contact có `Delete` (→ `/admin/clients/delete_contact/<customer_id>/<contact_id>`, lớp `_delete`) → xác nhận → dòng biến mất. Xoá contact **chính** khi còn contact khác chưa rõ. **Chưa kiểm chứng** | ⚪ | — | UI thực tế — chưa bấm |

## 2. Đặc tả trường dữ liệu — modal contact

| Field (Label) | Tên field | Loại UI | Required | Ràng buộc quan sát được | Mặc định | REQ liên quan |
|---|---|---|---|---|---|---|
| `Profile image` | `profile_image` | file | — | — | — | REQ-CUST-54 |
| `* First Name` | `firstname` | text | ✅ | Không `maxlength` | rỗng | REQ-CUST-55 |
| `* Last Name` | `lastname` | text | ✅ | Không `maxlength` | rỗng | REQ-CUST-55 |
| `Position` | `title` | text | — | — | rỗng | REQ-CUST-68 |
| `* Email` | `email` | email | ✅ | Định dạng email · duy nhất (`remote`) | rỗng | REQ-CUST-55 → 57 |
| `Phone` | `phonenumber` | text (`autocomplete=off`) | — | — | mã quốc gia của KH (VD `+84`) | REQ-CUST-58 |
| `Direction` | `direction` | select | — | `''` System Default · `ltr` · `rtl` | System Default | REQ-CUST-54 |
| `* Password` | `password` | password | ✅ khi tạo, trừ khi tick Send SET password email · ❌ khi sửa | Sinh tự động 12 ký tự | rỗng | REQ-CUST-55, 59, 60, 66 |
| `Primary Contact` | `is_primary` | checkbox | — | Khoá khi là contact chính duy nhất | tick (contact đầu tiên) | REQ-CUST-61, 67 |
| `Do not send welcome email` | `donotsendwelcomeemail` | checkbox | — | — | không tick | REQ-CUST-71 |
| `Send SET password email` | `send_set_password_email` | checkbox | — | Ẩn ô Password khi tick | không tick | REQ-CUST-59 |
| Permissions | `permissions[]` (1 → 6) | 6 công tắc | — | — | bật cả 6 | REQ-CUST-62 |
| Email Notifications | `*_emails` (7 trường) | 7 công tắc | — | — | bật cả 7 | REQ-CUST-63 |
| *(chống autofill)* | `fakeusernameremembered` · `fakepasswordremembered` | text/password | — | Trường mồi, không phải dữ liệu nghiệp vụ | — | — |

## 3. Business Rules & Validation Messages

| REQ ID | Rule / Trigger | Thông báo (nguyên văn) |
|---|---|---|
| REQ-CUST-55 | First Name / Last Name / Email / Password trống | "This field is required." |
| REQ-CUST-56 | Email sai định dạng | "Please enter a valid email address." |
| REQ-CUST-57 | Email trùng contact khác | "Email already exists" |
| REQ-CUST-64 | Tạo thành công | "Contact added successfully." |
| REQ-CUST-66 | Ghi chú ô Password khi sửa | "Note: if you populate this field, password will be changed on this contact." |
| REQ-CUST-68 | Sửa thành công | "Contact updated successfully." |

## 4. User Flow — thêm liên hệ chính

1. Hồ sơ KH → tab `Contacts` → `New Contact`
2. Nhập First/Last Name, Email duy nhất; sinh mật khẩu **hoặc** tick `Send SET password email`
3. `Save` → contact là Primary (REQ-CUST-61, 64) → danh sách KH hiện Primary Contact (REQ-CUST-65)
