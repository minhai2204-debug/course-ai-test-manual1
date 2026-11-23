# STORY-CUST-04 — Import khách hàng từ CSV

> ← [Index module `REQUIREMENTS_CUSTOMERS_SUMMARY.md`](../../REQUIREMENTS_CUSTOMERS_SUMMARY.md) · [File web](../requirements_customers_web.md)
>
> **Phạm vi:** trang `/admin/clients/import` — hướng dẫn, bảng mẫu, Simulate Import, Import.
> **REQ:** `REQ-CUST-73` → `REQ-CUST-80` (8 REQ) · **AMB:** AMB-CUST-20 · **RISK:** RISK-CUST-05

## 1. Yêu cầu chức năng

| REQ ID | Tên yêu cầu | Mô tả | Acceptance Criteria | Trạng thái | Cập nhật lần cuối | Nguồn |
|---|---|---|---|---|---|---|
| REQ-CUST-73 | Trang Import hiển thị hướng dẫn và bảng mẫu 27 cột | Người dùng biết định dạng tệp | `Import Customers` → `/admin/clients/import`, `document.title` **chứa** `Import`; khối hướng dẫn gồm 4 điểm (UTF-8 · ngày dạng `Y-m-d` · cấu hình quyền contact mặc định ở Setup · **"Duplicate email rows won't be imported."**); bảng mẫu 27 cột: `Firstname · Lastname · Email · Contact phonenumber · Position` (nhãn phụ `Contact field`) · `Company · Vat · Phonenumber · Country · City · Zip · State · Address · Website · Billing street · Billing city · Billing state · Billing zip · Billing country · Shipping street · Shipping city · Shipping state · Shipping zip · Shipping country · Longitude · Latitude · Stripe id`; 4 cột có dấu `*`: `Firstname`, `Lastname`, `Email`, `Company` | 🟢 | — | Kiểm chứng thực tế · `cust_import_no_file_submit_viewport.png` |
| REQ-CUST-74 | Không chọn tệp → thông báo bắt buộc, không gửi | Validation form import | Không chọn tệp → `Simulate Import` (hoặc `Import`) → `#file_csv-error` **"This field is required."**, URL không đổi | 🟢 | — | Kiểm chứng thực tế (DOM) · `cust_import_no_file_submit_viewport.png` |
| REQ-CUST-75 | Simulate Import xem trước dữ liệu, không ghi vào hệ thống | Kiểm tệp trước khi nhập thật | Chọn CSV 1 dòng (`auto_cust_import_<timestamp>`) → `Simulate Import` → khối `Simulation Data` kèm ghi chú **"Max 100 rows are shown"** và **"If you are satisfied with the results upload the file again and click import."**, bảng hiện đúng dòng trong tệp. Không ghi dữ liệu: Import thật cùng email ngay sau đó vẫn báo `Total Imported: 1` (nếu mô phỏng đã ghi, dòng sẽ bị bỏ vì trùng email — REQ-CUST-77) | 🟢 | — | Kiểm chứng thực tế · `cust_import_simulation_result_viewport.png` |
| REQ-CUST-76 | Import tạo khách hàng kèm contact chính | Nhập dữ liệu hàng loạt | CSV có dòng hợp lệ (đủ 4 cột bắt buộc) → `Import` → thông báo **"Total Imported: <n>"**; mỗi dòng tạo 1 KH (Company) + 1 contact chính (Firstname/Lastname/Email) đang Active; KH xuất hiện ở danh sách với Primary Contact/Email | 🟢 | — | Kiểm chứng thực tế (KH test id 16008) |
| REQ-CUST-77 | Dòng trùng email bị bỏ qua khi import | Email contact là duy nhất | CSV 2 dòng cùng email, khác Company → `Import` → **"Total Imported: 1"**; chỉ dòng đầu được tạo | 🟢 | — | Kiểm chứng thực tế |
| REQ-CUST-78 | Ô "Default password for all contacts" hiển thị rõ ký tự | Mật khẩu mặc định cho contact nhập vào | Ô `default_pass_all` có `type === 'text'` (không che ký tự). RISK-CUST-05 | 🟢 | — | UI thực tế (DOM) |
| REQ-CUST-79 | Download Sample tải tệp CSV mẫu đúng 27 cột | Tác tạo của trang — **dùng được** | Bấm `Download Sample` → tải tệp CSV có dòng tiêu đề trùng 27 cột REQ-CUST-73. **Chưa kiểm chứng** — không tải tệp trong lượt recon | ⚪ | — | Chưa kiểm chứng |
| REQ-CUST-80 | Groups chọn khi import được gán cho mọi KH nhập vào | Gán nhóm hàng loạt | Chọn group ở ô `Groups` → Import → mọi KH mới thuộc group đó. **Chưa kiểm chứng** | ⚪ | — | UI thực tế — chưa thử |

## 2. Đặc tả trường dữ liệu — form import

| Field (Label) | Tên field | Loại UI | Required | Ràng buộc quan sát được | REQ liên quan |
|---|---|---|---|---|---|
| `* Choose CSV File` | `file_csv` | file | ✅ | Không đặt `accept` — trình duyệt không lọc loại tệp | REQ-CUST-74 |
| `Groups` | `groups_in[]` | multi-select + nút `+` | — | — | REQ-CUST-80 |
| `Default password for all contacts` | `default_pass_all` | **text** | — | Hiển thị rõ ký tự | REQ-CUST-78 |
| Nút `Import` / `Simulate Import` | — | button | — | — | REQ-CUST-75 → 77 |

## 3. Business Rules & Validation Messages

| REQ ID | Rule / Trigger | Thông báo (nguyên văn) |
|---|---|---|
| REQ-CUST-74 | Không chọn tệp | "This field is required." |
| REQ-CUST-75 | Simulate Import | "Max 100 rows are shown" · "If you are satisfied with the results upload the file again and click import." |
| REQ-CUST-76, 77 | Import xong | "Total Imported: `<n>`" |
| REQ-CUST-73 | Hướng dẫn #4 | "Duplicate email rows won't be imported." |

**Quan sát phụ (AMB-CUST-20):** bảng Simulation hiển thị `0` ở các cột Country / Billing country / Shipping country khi tệp để trống — chưa rõ import thật lưu `0` hay rỗng.
