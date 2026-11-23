# STORY-CUST-02 — Tạo, sửa & hồ sơ khách hàng

> ← [Index module `REQUIREMENTS_CUSTOMERS_SUMMARY.md`](../../REQUIREMENTS_CUSTOMERS_SUMMARY.md) · [File web](../requirements_customers_web.md)
>
> **Phạm vi:** form tạo `/admin/clients/client` · màn chi tiết `/admin/clients/client/{id}` (menu 19 tab, tab Profile với 3 tab con: Customer Details · Billing & Shipping · Customer Admins) · xoá khách hàng.
> **REQ:** `REQ-CUST-28` → `REQ-CUST-52` (25 REQ) · **AMB:** AMB-CUST-01, 02, 09, 12 · **RISK:** RISK-CUST-07

## 1. Yêu cầu chức năng

| REQ ID | Tên yêu cầu | Mô tả | Acceptance Criteria | Trạng thái | Cập nhật lần cuối | Nguồn |
|---|---|---|---|---|---|---|
| REQ-CUST-28 | Form tạo khách hàng có 2 tab | Màn thêm mới | `New Customer` → URL `/admin/clients/client`, `document.title` **chứa** `Add new customer`; có đúng 2 tab `Customer Details` (`#contact_info`) và `Billing & Shipping` (`#billing_and_shipping`). Tab `Customer Admins` **không** có ở form tạo (chỉ có khi sửa — REQ-CUST-50) | 🟢 | — | Kiểm chứng thực tế · `cust_new_form_default_viewport.png` |
| REQ-CUST-29 | Ô Company được đặt focus sẵn | Gõ tên ngay khi mở form | `#company` có thuộc tính `autofocus` | 🟢 | — | UI thực tế (DOM) |
| REQ-CUST-30 | Bỏ trống Company → thông báo bắt buộc, không gửi form | Company là trường bắt buộc duy nhất | Form trống → bấm `Save` → dưới ô Company hiện `#company-error` nội dung **"This field is required."**, nhãn Company đổi màu đỏ, URL giữ `/admin/clients/client`, **không** có request `POST /admin/clients/client` | 🟢 | — | Kiểm chứng thực tế (DOM + network) · `cust_new_form_empty_submit_viewport.png` |
| REQ-CUST-31 | Company chỉ gồm khoảng trắng vượt qua kiểm tra phía trình duyệt | Hành vi hiện tại — nghi lỗi | Nhập `'   '` (3 khoảng trắng) vào Company → `$('#company').valid() === true` (không hiện lỗi). Dữ liệu môi trường có sẵn bản ghi Company toàn khoảng trắng (id 9330) → phía server cũng đã từng chấp nhận. Không tạo thêm bản ghi để thử (tên không nhận diện được). AMB-CUST-01 🔴, RISK-CUST-07 | 🟢 | — | Kiểm chứng thực tế (DOM) · API · POST /admin/clients/table · 200 (bản ghi 9330) |
| REQ-CUST-32 | Các ô văn bản không có giới hạn độ dài phía giao diện | Ràng buộc độ dài | `maxLength === -1` (không đặt) cho `company`, `vat`, `phonenumber`, `website`, `city`, `state`, `zip`, `billing_*`, `shipping_*`. Giới hạn thật phía server/CSDL chưa rõ (AMB-CUST-02) | 🟢 | — | UI thực tế (DOM) |
| REQ-CUST-33 | Rời ô Company với tên đã tồn tại → hiện cảnh báo trùng tên | Gợi ý tránh tạo trùng | Gõ Company trùng tên một KH đã có (dùng KH test vừa tạo) → rời ô → request `POST /admin/clients/check_duplicate_customer_name` trả `exists: true` → ngay dưới ô hiện khối thông tin nguyên văn **"It looks that a customer with name `<tên>` already exists, if you still want to create the customer you can ignore this message."** (tên in đậm) | 🟢 | — | Kiểm chứng thực tế · API · POST /admin/clients/check_duplicate_customer_name · 200 · `cust_new_form_duplicate_name_warning_viewport.png` |
| REQ-CUST-34 | Cảnh báo trùng tên không chặn việc lưu | Theo nội dung cảnh báo "you can ignore this message" | Sau REQ-CUST-33 bấm `Save` → tạo được KH thứ hai cùng tên. **Chưa kiểm chứng** — không tạo bản ghi trùng trong lượt recon | ⚪ | — | Suy từ nội dung cảnh báo — chưa kiểm chứng |
| REQ-CUST-35 | Currency mặc định System Default, có tooltip cảnh báo | Tiền tệ riêng của khách hàng | `#default_currency` có 3 option: rỗng (hiển thị `System Default`, chọn sẵn) · `USD` · `EUR`. Biểu tượng `?` cạnh nhãn có tooltip nguyên văn **"If the customer use other currency then the base currency make sure you select the appropriate currency for this customer. Changing the currency is not possible after transactions are recorded."** | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-36 | Default Language mặc định System Default, 26 ngôn ngữ | Ngôn ngữ của khách hàng | `#default_language` có 27 option: rỗng (`System Default`, chọn sẵn) + 26 giá trị (`english`, `chinese`, `vietnamese`, …, `romanian`) | 🟢 | — | UI thực tế (DOM) |
| REQ-CUST-37 | Groups chọn nhiều và có nút thêm group nhanh | Phân nhóm khách hàng | `select[name="groups_in[]"]` là `select-multiple`, mặc định không chọn (`Nothing selected`); bên phải có nút `+` (`data-target="#customer_group_modal"`). Số group biến động theo dữ liệu — không assert | 🟢 | — | UI thực tế (DOM) · `cust_new_form_default_viewport.png` |
| REQ-CUST-38 | Country mặc định không chọn, 250 quốc gia | Quốc gia của khách hàng | `#country` có 251 option: rỗng (chọn sẵn) + 250 quốc gia, option đầu `Afghanistan` (`value=1`); `Vietnam` có `value=243`. Billing/Shipping Country cùng danh sách | 🟢 | — | UI thực tế (DOM) |
| REQ-CUST-39 | Lưu khách hàng mới → chuyển sang hồ sơ, báo thành công | Kết quả tạo mới | Company `auto_cust_<timestamp>` + các trường khác → `Save` → URL `/admin/clients/client/<id mới>`, thông báo **"Customer added successfully."**, tiêu đề trang `#<id> <Company>`, `document.title` = Company | 🟢 | — | Kiểm chứng thực tế · `cust_detail_tabs_menu_viewport.png` |
| REQ-CUST-40 | Giá trị đã nhập được lưu nguyên văn | Không tự sửa dữ liệu người dùng | Sau REQ-CUST-39, mở lại tab Profile → mọi ô giữ đúng giá trị đã nhập; `website` nhập `auto-cust-141157.example.com` (không có `http://`) được lưu y nguyên, không tự thêm tiền tố | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-41 | "Same as Customer Info" chép địa chỉ sang Billing | Điền nhanh địa chỉ thanh toán | Điền Address/City/State/Zip/Country ở tab Customer Details → tab `Billing & Shipping` → bấm `Same as Customer Info` → `billing_street/city/state/zip/country` bằng đúng 5 giá trị tương ứng | 🟢 | — | Kiểm chứng thực tế (DOM) · `cust_new_billing_shipping_copied_viewport.png` |
| REQ-CUST-42 | "Copy Billing Address" chép Billing sang Shipping | Điền nhanh địa chỉ giao hàng | Sau REQ-CUST-41 bấm `Copy Billing Address` → 5 ô `shipping_*` bằng 5 ô `billing_*` | 🟢 | — | Kiểm chứng thực tế (DOM) · `cust_new_billing_shipping_copied_viewport.png` |
| REQ-CUST-43 | Shipping Address có tooltip hướng dẫn | Gợi ý khi không dùng địa chỉ giao hàng | Biểu tượng `?` cạnh `Shipping Address` có tooltip nguyên văn **"Do not fill shipping address information if you won't use shipping address on customer invoices"** | 🟢 | — | UI thực tế (DOM) |
| REQ-CUST-44 | "Save and create contact" lưu KH rồi mở form tạo liên hệ | Lối tắt tạo KH kèm contact | Form tạo có hai nút submit: `Save and create contact` và `Save`. Bấm `Save and create contact` → KH được tạo và mở modal `Add new contact` của KH đó. **Chưa kiểm chứng** — mới thấy nút (AMB-CUST-12) | ⚪ | — | UI thực tế — chưa bấm |
| REQ-CUST-45 | Màn chi tiết có menu 19 tab theo thứ tự cố định | Điều hướng hồ sơ khách hàng | `/admin/clients/client/<id>` → menu tab: `Profile · Contacts · Notes · Statement · Invoices · Payments · Proposals · Credit Notes · Estimates · Subscriptions · Expenses · Contracts · Projects · Tasks · Tickets · Files · Vault · Reminders · Map`; mỗi tab mở bằng `?group=<khoá>` (VD `contacts`, `notes`, `attachments` cho Files, `vault`, `reminders`, `map`). Ở viewport 973×853 menu xếp dọc (AMB-CUST-16) | 🟢 | — | Kiểm chứng thực tế · `cust_detail_tabs_menu_viewport.png` |
| REQ-CUST-46 | Tab có dữ liệu hiển thị số đếm cạnh tên | Biết nhanh tab nào có dữ liệu | KH test có 1 contact, 1 file, 1 reminder → mục `Contacts`, `Files`, `Reminders` của menu có huy hiệu số `1`; tab không có dữ liệu không có huy hiệu | 🟢 | — | Kiểm chứng thực tế · `cust_files_after_upload_viewport.png` |
| REQ-CUST-47 | Tiêu đề hồ sơ có menu thả xuống chứa Delete | Lối xoá từ màn chi tiết | Mũi tên cạnh tiêu đề `#<id> <Company>` mở menu có đúng 1 mục `Delete` (→ `/admin/clients/delete/<id>`, lớp `_delete`) | 🟢 | — | UI thực tế (DOM) |
| REQ-CUST-48 | Sửa: xoá trắng Company → thông báo bắt buộc | Validation áp cả khi sửa | Tab Profile → xoá trắng Company → `Save` → `#company-error` **"This field is required."**, không rời trang | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-49 | Sửa và lưu → báo cập nhật thành công | Kết quả sửa hồ sơ | Đổi Phone KH test → `Save` → ở lại `/admin/clients/client/<id>`, thông báo **"Customer updated successfully."**, ô Phone hiển thị giá trị mới | 🟢 | — | Kiểm chứng thực tế |
| REQ-CUST-50 | Customer Admins gán nhân viên phụ trách | Phân công người quản lý KH | Tab con `Customer Admins` → `Assign Admin` → modal `Assign Admin` với multi-select `customer_admins[]` liệt kê nhân viên (đo được 3) → chọn tài khoản đang đăng nhập → `Save` → URL `?tab=customer_admins`, thông báo **"Customer updated successfully."**, bảng (cột `Staff Member · Date Assigned · Options`) có dòng nhân viên đó, `Date Assigned` dạng `DD-MM-YYYY HH:mm:ss` | 🟢 | — | Kiểm chứng thực tế |
| REQ-CUST-51 | Tuỳ chọn "Show primary contact full name…" chỉ hiện khi KH đã có liên hệ | Hiển thị tên liên hệ trên chứng từ | Checkbox `#show_primary_contact` (nhãn "Show primary contact full name on Invoices, Estimates, Payments, Credit Notes"): KH chưa có contact → tổ tiên lớp `hide` (`offsetParent === null`); sau khi thêm contact → hiển thị, mặc định **không** tick | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-52 | Xoá khách hàng sau khi xác nhận | Xoá KH và dữ liệu đi kèm | Bấm `Delete` (bảng hoặc menu tiêu đề) → hộp xác nhận → đồng ý → KH biến mất khỏi danh sách, contact của KH bị xoá theo. **Chưa kiểm chứng** — thao tác xoá KH bị chặn trong phiên recon; hành vi khi KH có giao dịch chưa rõ (AMB-CUST-09) | ⚪ | — | Chưa kiểm chứng |

## 2. Đặc tả trường dữ liệu — form khách hàng

| Field (Label) | Tên field (payload) | Loại UI | Required | Ràng buộc quan sát được | Mặc định | REQ liên quan |
|---|---|---|---|---|---|---|
| `* Company` | `company` | text | ✅ (jQuery Validate) | Không `maxlength`; khoảng trắng thuần vẫn hợp lệ phía client | rỗng · autofocus | REQ-CUST-29 → 33, 48 |
| `VAT Number` | `vat` | text | — | Không `maxlength` | rỗng | REQ-CUST-12, 32 |
| `Phone` | `phonenumber` | text | — | Không `maxlength`, không kiểm định dạng | rỗng | REQ-CUST-11, 32 |
| `Website` | `website` | text | — | Lưu nguyên văn, không tự thêm `http://` | rỗng | REQ-CUST-40 |
| `Groups` | `groups_in[]` | multi-select + nút `+` | — | — | không chọn | REQ-CUST-37 |
| `Currency` | `default_currency` | select | — | `''`(System Default) · `1` USD · `2` EUR | System Default | REQ-CUST-35 |
| `Default Language` | `default_language` | select | — | 27 option | System Default | REQ-CUST-36 |
| `Address` | `address` | textarea | — | — | rỗng | REQ-CUST-41 |
| `City` · `State` · `Zip Code` | `city` · `state` · `zip` | text | — | Không `maxlength` | rỗng | REQ-CUST-41 |
| `Country` | `country` | select | — | 251 option | không chọn | REQ-CUST-38 |
| Billing: `Street` · `City` · `State` · `Zip Code` · `Country` | `billing_street` · `billing_city` · `billing_state` · `billing_zip` · `billing_country` | textarea/text/select | — | — | rỗng | REQ-CUST-41 |
| Shipping: như Billing | `shipping_*` | textarea/text/select | — | — | rỗng | REQ-CUST-42, 43 |
| `Show primary contact full name on …` | `show_primary_contact` | checkbox | — | Chỉ hiện khi có contact | không tick | REQ-CUST-51 |
| *(ẩn)* | `csrf_token_name` | hidden | — | Giá trị dạng `<32 ký tự hex>` — không chép | — | — |

## 3. Business Rules & Validation Messages

| REQ ID | Rule / Trigger | Thông báo (nguyên văn) |
|---|---|---|
| REQ-CUST-30, 48 | Company trống | "This field is required." |
| REQ-CUST-33 | Company trùng tên KH đã có (rời ô) | "It looks that a customer with name **`<tên>`** already exists, if you still want to create the customer you can ignore this message." |
| REQ-CUST-35 | Tooltip Currency | "If the customer use other currency then the base currency make sure you select the appropriate currency for this customer. Changing the currency is not possible after transactions are recorded." |
| REQ-CUST-39 | Tạo thành công | "Customer added successfully." |
| REQ-CUST-49, 50 | Sửa / gán admin thành công | "Customer updated successfully." |
| REQ-CUST-43 | Tooltip Shipping Address | "Do not fill shipping address information if you won't use shipping address on customer invoices" |

## 4. User Flow — tạo khách hàng kèm địa chỉ

1. `/admin/clients` → `New Customer`
2. Nhập Company (rời ô → cảnh báo nếu trùng — REQ-CUST-33) và thông tin liên quan
3. Tab `Billing & Shipping` → `Same as Customer Info` → `Copy Billing Address` (REQ-CUST-41, 42)
4. `Save` → hồ sơ `/admin/clients/client/<id>` (REQ-CUST-39)
5. Tab con `Customer Admins` → `Assign Admin` (REQ-CUST-50)
