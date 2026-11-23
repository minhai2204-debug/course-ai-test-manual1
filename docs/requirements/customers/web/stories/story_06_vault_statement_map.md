# STORY-CUST-06 — Vault · Statement · Map

> ← [Index module `REQUIREMENTS_CUSTOMERS_SUMMARY.md`](../../REQUIREMENTS_CUSTOMERS_SUMMARY.md) · [File web](../requirements_customers_web.md)
>
> **Phạm vi:** tab `Vault` (`?group=vault`) · `Statement` (`?group=statement`) · `Map` (`?group=map`) của hồ sơ KH.
> **REQ:** `REQ-CUST-96` → `REQ-CUST-104` (9 REQ) · **AMB:** AMB-CUST-13 · **RISK:** RISK-CUST-06

## 1. Yêu cầu chức năng

| REQ ID | Tên yêu cầu | Mô tả | Acceptance Criteria | Trạng thái | Cập nhật lần cuối | Nguồn |
|---|---|---|---|---|---|---|
| REQ-CUST-96 | Vault trống hiển thị thông báo và nút tạo | Kho thông tin truy cập của KH | KH chưa có vault → `?group=vault` → nút `New Vault Entry` (`data-target="#entryModal"`) và dòng nguyên văn **"Vault entries not found for this customer."** | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-97 | Modal Vault Entry có 5 trường và 3 mức hiển thị | Form tạo mục vault | `New Vault Entry` → modal `Vault Entry` (form `POST /admin/clients/vault_entry_create/<id>`): `* Server Address` · `Port` (`type=number`) · `* Username` · `* Password` (`type=password`) · `Short Description`; radio `visibility` 3 mức: **"Visible to all staff member who have access to this customer"** (chọn sẵn) · "Visible only to administrators" · "Visible only to me (administrators are not excluded)"; checkbox "Share this vault entry in projects with project members" (không tick) | 🟢 | — | Kiểm chứng thực tế (DOM) · `cust_vault_new_entry_empty_submit_viewport.png` |
| REQ-CUST-98 | Bỏ trống → 3 thông báo bắt buộc | Validation vault | Modal trống → `Save` → `#server_address-error`, `#username-error`, `#password-error` đều **"This field is required."**; modal không đóng | 🟢 | — | Kiểm chứng thực tế (DOM) · `cust_vault_new_entry_empty_submit_viewport.png` |
| REQ-CUST-99 | Lưu mục vault và chỉ người được phép xem lại mật khẩu | Tác tạo của Vault — được tạo **và** dùng được | Nhập đủ trường (mật khẩu **giả**, không dùng mật khẩu thật) → `Save` → mục xuất hiện ở tab Vault; mật khẩu che mặc định, xem lại theo mức `visibility`. **Chưa kiểm chứng** — agent không nhập mật khẩu vào ô; tester tự thao tác (AMB-CUST-13, RISK-CUST-06) | ⚪ | — | Chưa kiểm chứng |
| REQ-CUST-100 | Statement mặc định kỳ This Month, tóm tắt số dư theo địa chỉ Billing | Sao kê công nợ của KH | `?group=statement` → bộ chọn kỳ hiển thị `This Month`; tiêu đề **"Customer Statement For `<Company>`"**; khối `To:` lấy Company + **địa chỉ Billing** (+ `VAT Number: <vat>`); `Account Summary` ghi `<ngày đầu tháng> To <ngày cuối tháng>` dạng `DD-MM-YYYY`; 4 dòng `Beginning Balance` · `Invoiced Amount` · `Amount Paid` · `Balance Due`. KH test chưa có giao dịch → cả 4 = `$0.00`, bảng chi tiết có đúng 1 dòng `Beginning Balance` | 🟢 | — | Kiểm chứng thực tế · `cust_statement_this_month_viewport.png` |
| REQ-CUST-101 | Statement có 7 lựa chọn kỳ | Đổi khoảng thời gian | `select[name=range]` có đúng 7 option: `Today · This Week · This Month · Last Month · This Year · Last Year · Period`. Số liệu khi đổi kỳ chưa kiểm | 🟢 | — | UI thực tế (DOM) |
| REQ-CUST-102 | Statement có nút In, Xem PDF, Gửi email | Xuất sao kê | 3 nút biểu tượng: `Print` (→ `/admin/clients/statement_pdf?customer_id=<id>&from=<DD-MM-YYYY>&to=<DD-MM-YYYY>&print=true`) · `View PDF` (cùng URL không có `print`) · gửi email (`data-target="#statement_send_to_client"`); tham số `from`/`to` khớp kỳ đang chọn. Nội dung PDF và việc gửi email chưa kiểm | 🟢 | — | UI thực tế (DOM) · `cust_statement_this_month_viewport.png` |
| REQ-CUST-103 | Tab Map có ô Latitude/Longitude và báo thiếu Google API key | Vị trí KH trên bản đồ | `?group=map` → ô `latitude`, `longitude` (text) + nút `Save`; môi trường hiện tại chưa cấu hình key → dòng nguyên văn **"Setup google api key in order to view to customer map"**, không có bản đồ | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-104 | Lưu toạ độ KH | Tác tạo của tab Map | Nhập Latitude/Longitude → `Save` → giá trị giữ sau tải lại. **Chưa kiểm chứng**; hiển thị bản đồ cần API key ở Setup (BLOCKED) | ⚪ | — | Chưa kiểm chứng |

## 2. Đặc tả trường dữ liệu — Vault Entry

| Field (Label) | Tên field | Loại UI | Required | Mặc định | REQ liên quan |
|---|---|---|---|---|---|
| `* Server Address` | `server_address` | text | ✅ | rỗng | REQ-CUST-98 |
| `Port` | `port` | number | — | rỗng | REQ-CUST-97 |
| `* Username` | `username` | text | ✅ | rỗng | REQ-CUST-98 |
| `* Password` | `password` | password | ✅ | rỗng | REQ-CUST-98, 99 |
| `Short Description` | `description` | textarea | — | rỗng | REQ-CUST-97 |
| Hiển thị | `visibility` | radio ×3 | — | Visible to all staff… | REQ-CUST-97, 99 |
| `Share this vault entry in projects with project members` | `share_in_projects` | checkbox | — | không tick | REQ-CUST-97 |
| *(chống autofill)* | `fakeusernameremembered` · `fakepasswordremembered` | text/password | — | — | — |

## 3. Business Rules & Validation Messages

| REQ ID | Rule / Trigger | Thông báo (nguyên văn) |
|---|---|---|
| REQ-CUST-96 | Vault trống | "Vault entries not found for this customer." |
| REQ-CUST-98 | Server Address / Username / Password trống | "This field is required." |
| REQ-CUST-103 | Chưa cấu hình Google API key | "Setup google api key in order to view to customer map" |
