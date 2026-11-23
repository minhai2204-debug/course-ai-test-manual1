# STORY-CUST-05 — Ghi chú · Nhắc việc · Tệp đính kèm

> ← [Index module `REQUIREMENTS_CUSTOMERS_SUMMARY.md`](../../REQUIREMENTS_CUSTOMERS_SUMMARY.md) · [File web](../requirements_customers_web.md)
>
> **Phạm vi:** tab `Notes` (`?group=notes`) · `Reminders` (`?group=reminders`) · `Files` (`?group=attachments`) của hồ sơ KH.
> **REQ:** `REQ-CUST-81` → `REQ-CUST-95` (15 REQ) · **AMB:** AMB-CUST-03, 14, 15 · **RISK:** RISK-CUST-04

## 1. Yêu cầu chức năng

| REQ ID | Tên yêu cầu | Mô tả | Acceptance Criteria | Trạng thái | Cập nhật lần cuối | Nguồn |
|---|---|---|---|---|---|---|
| REQ-CUST-81 | Tab Notes có nút New Note và bảng 4 cột | Ghi chú nội bộ về KH | `?group=notes` → nút `New Note` (mở ô `description` ẩn sẵn, form `POST /admin/misc/add_note/<id>/customer`), bảng cột `Description · Added From · Date Added · Options`, sắp xếp mặc định `Date Added` giảm dần | 🟢 | — | Kiểm chứng thực tế · `cust_notes_empty_note_saved_viewport.png` |
| REQ-CUST-82 | Lưu ghi chú với mô tả trống vẫn thành công | Hành vi hiện tại — nghi lỗi | `New Note` → để trống Description → bấm lưu → trang tải lại, thông báo **"Note added successfully."**, bảng có dòng Description **rỗng**, `Added From` = nhân viên đang đăng nhập, `Date Added` dạng `DD-MM-YYYY HH:mm:ss`. AMB-CUST-03 🔴 | 🟢 | — | Kiểm chứng thực tế · `cust_notes_empty_note_saved_viewport.png` |
| REQ-CUST-83 | Sửa ghi chú tại chỗ | Cập nhật nội dung không rời trang | Biểu tượng bút ở cột Options → hiện ô sửa với nút `Cancel` và `Update note` → nhập `auto_note_<timestamp> cập nhật` → `Update note` → `POST /admin/misc/edit_note/<note_id>` 200, thông báo **"Note updated successfully"** (không có dấu chấm cuối), ô Description hiển thị nội dung mới giữ nguyên dấu tiếng Việt | 🟢 | — | Kiểm chứng thực tế |
| REQ-CUST-84 | Xoá ghi chú phải xác nhận; huỷ thì giữ nguyên | Chống xoá nhầm | Biểu tượng thùng rác (`/admin/misc/delete_note/<note_id>`, lớp `_delete`) → hộp xác nhận nguyên văn **"Are you sure you want to perform this action?"** → chọn huỷ → ghi chú còn nguyên, URL không đổi. Hộp xác nhận là `window.confirm` gốc — khung hộp do trình duyệt vẽ, chỉ assert nội dung chuỗi | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-85 | Xác nhận xoá ghi chú → báo đã xoá | Kết quả xoá | Đồng ý ở REQ-CUST-84 → trang tải lại, thông báo **"Note deleted"**, bảng `No entries found` (KH test chỉ có 1 note) | 🟢 | — | Kiểm chứng thực tế |
| REQ-CUST-86 | Modal Set Reminder có 4 trường, người nhận mặc định là mình | Đặt nhắc việc cho KH | `?group=reminders` → `Set Reminder` → modal tiêu đề `Set Reminder` (form `POST /admin/misc/add_reminder/<id>/customer`): `* Date to be notified` (datetimepicker) · `* Set reminder to` (select nhân viên, chọn sẵn tài khoản đang đăng nhập) · `* Description` · `Send also an email for this reminder` (không tick) | 🟢 | — | Kiểm chứng thực tế · `cust_reminder_modal_datepicker_viewport.png` |
| REQ-CUST-87 | Bỏ trống ngày và mô tả → 2 thông báo bắt buộc | Validation nhắc việc | Modal trống → `Save` → `#date-error` và `#description-error` đều **"This field is required."** | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-88 | Bộ chọn ngày khoá các ngày đã qua, ghi giá trị dạng DD-MM-YYYY HH:mm | Không đặt nhắc việc trong quá khứ qua bộ chọn | Mở bộ chọn ngày → mọi ngày **trước hôm nay** của tháng hiện tại mang lớp `xdsoft_disabled` (đo ngày 16-11-2026: ngày 1 → 15); chọn một ngày tương lai, giờ `09:00` → ô có giá trị dạng `DD-MM-YYYY 09:00` (đo: `20-11-2026 09:00`). Nhập tay ngày quá khứ chưa thử | 🟢 | — | Kiểm chứng thực tế (DOM) · `cust_reminder_modal_datepicker_viewport.png` |
| REQ-CUST-89 | Lưu nhắc việc → báo thành công, dòng mới chưa thông báo | Kết quả đặt nhắc việc | Ngày tương lai + Description `auto_reminder_<timestamp>` → `Save` → thông báo **"Reminder added successfully. You will be notified in time."**; bảng (cột `Description · Date · Remind · Is notified?`) có dòng: description · `20-11-2026 09:00:00` · tên người nhận · `No` | 🟢 | — | Kiểm chứng thực tế |
| REQ-CUST-90 | Tới giờ nhắc, người nhận được thông báo và cột Is notified đổi Yes | Tác tạo của nhắc việc — **dùng được** | Tới mốc giờ đã đặt → người nhận có thông báo trong hệ thống (và email nếu tick) → `Is notified?` = `Yes`. **Chưa kiểm chứng** — cần chờ tới giờ, chạy bằng job nền (AMB-CUST-14) | ⚪ | — | Chưa kiểm chứng |
| REQ-CUST-91 | Tab Files có vùng kéo thả và ghi chú phạm vi | Đính kèm tệp cho KH | `?group=attachments` → ghi chú nguyên văn **"Files from projects and tasks linked to the customer are not shown on this table."**, vùng `Drop files here to upload` (Dropzone, `POST /admin/clients/upload_attachment/<id>`), bảng cột `File · Show to customers area · Date Uploaded · Options` | 🟢 | — | Kiểm chứng thực tế · `cust_files_after_upload_viewport.png` |
| REQ-CUST-92 | Tệp không thuộc danh sách cho phép bị từ chối | Chặn loại tệp nguy hiểm | Thả tệp `.exe` → thông báo **"You can't upload files of this type."**, không có dòng mới. Cấu hình Dropzone đọc từ DOM: `acceptedFiles = .png,.jpg,.pdf,.doc,.docx,.xls,.xlsx,.ppt,.pptx,.zip`, `maxFilesize = 128` (MB, chưa thử giới hạn). `.jpeg`, `.gif`, `.txt`, `.csv` không có trong danh sách (AMB-CUST-15) | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-93 | Tải lên tệp hợp lệ → dòng mới, mặc định ẩn với khách hàng | Kết quả upload | Thả tệp `auto_cust_file_<timestamp>.pdf` → trang tải lại; bảng có dòng: liên kết tải (`/download/file/client/<32 ký tự hex>`) · công tắc `Show to customers area` **tắt** · `Date Uploaded` dạng `DD-MM-YYYY HH:mm:ss` · Options (gửi email, xoá). Tab `Files` có huy hiệu `1` | 🟢 | — | Kiểm chứng thực tế · `cust_files_after_upload_viewport.png` |
| REQ-CUST-94 | Xoá tệp sau khi xác nhận | Gỡ tệp đính kèm | Biểu tượng thùng rác (`/admin/clients/delete_attachment/<id>/<file_id>`, lớp `_delete`) → đồng ý → dòng biến mất, bảng `No entries found` (không có thông báo nổi) | 🟢 | — | Kiểm chứng thực tế |
| REQ-CUST-95 | Bật "Show to customers area" thì khách hàng thấy tệp ở cổng | Tác tạo của công tắc — **dùng được** | Bật công tắc (`data-switch-url` = `/admin/misc/toggle_file_visibility`, chưa bấm) → contact của KH thấy tệp ở cổng khách hàng. **Chưa kiểm chứng** — cổng KH ngoài phạm vi | ⚪ | — | Chưa kiểm chứng |

## 2. Đặc tả trường dữ liệu

| Màn | Field (Label) | Tên field | Loại UI | Required | Ràng buộc / mặc định | REQ liên quan |
|---|---|---|---|---|---|---|
| Notes | Description | `description` | textarea | ❌ (hiện tại — AMB-CUST-03) | rỗng | REQ-CUST-82, 83 |
| Reminders | `* Date to be notified` | `date` | text + datetimepicker | ✅ | `DD-MM-YYYY HH:mm`; ngày đã qua bị khoá trong bộ chọn | REQ-CUST-87, 88 |
| Reminders | `* Set reminder to` | `staff` | select | ✅ | chọn sẵn nhân viên đang đăng nhập | REQ-CUST-86 |
| Reminders | `* Description` | `description` | textarea | ✅ | rỗng | REQ-CUST-87 |
| Reminders | `Send also an email for this reminder` | `notify_by_email` | checkbox | — | không tick | REQ-CUST-90 |
| Files | (vùng kéo thả) | `file` | Dropzone | — | 10 đuôi cho phép · tối đa 128 MB · 2 tệp song song | REQ-CUST-92, 93 |

## 3. Business Rules & Validation Messages

| REQ ID | Rule / Trigger | Thông báo (nguyên văn) |
|---|---|---|
| REQ-CUST-82 | Lưu note (kể cả trống) | "Note added successfully." |
| REQ-CUST-83 | Sửa note | "Note updated successfully" |
| REQ-CUST-84 | Bấm xoá (note / file / mọi liên kết `_delete`) | "Are you sure you want to perform this action?" |
| REQ-CUST-85 | Xoá note | "Note deleted" |
| REQ-CUST-87 | Ngày / mô tả nhắc việc trống | "This field is required." |
| REQ-CUST-89 | Lưu nhắc việc | "Reminder added successfully. You will be notified in time." |
| REQ-CUST-91 | Ghi chú tab Files | "Files from projects and tasks linked to the customer are not shown on this table." |
| REQ-CUST-92 | Tệp sai loại | "You can't upload files of this type." |
