# STORY-CUST-01 — Danh sách khách hàng & tóm tắt

> ← [Index module `REQUIREMENTS_CUSTOMERS_SUMMARY.md`](../../REQUIREMENTS_CUSTOMERS_SUMMARY.md) · [File web](../requirements_customers_web.md) — phân quyền · trạng thái · AMB/RISK · Nhật ký nằm ở index.
>
> **Phạm vi:** trang `/admin/clients` — thanh công cụ, khối *Customers Summary*, bảng `#clients` (DataTables server-side `POST /admin/clients/table`), tìm kiếm, sắp xếp, phân trang, Export, Bulk Actions, bộ lọc, công tắc Active.
> **REQ:** `REQ-CUST-01` → `REQ-CUST-27` (27 REQ) · **AMB:** AMB-CUST-04, 05, 06, 07, 10, 11 · **RISK:** RISK-CUST-02, 03

## 1. Yêu cầu chức năng

| REQ ID | Tên yêu cầu | Mô tả | Acceptance Criteria | Trạng thái | Cập nhật lần cuối | Nguồn |
|---|---|---|---|---|---|---|
| REQ-CUST-01 | Trang danh sách hiển thị thanh công cụ khách hàng | Lối vào các chức năng chính của module | Mở `/admin/clients` → `document.title` **chứa** `Customers`; thấy nút `New Customer` (→ `/admin/clients/client`), `Import Customers` (→ `/admin/clients/import`), `Contacts` (→ `/admin/clients/all_contacts`) và nút lọc biểu tượng phễu (`button.dropdown-toggle` chứa `i.fa-filter`, tooltip `Filter by`); cả 4 có `offsetParent !== null` ở viewport 973×853 | 🟢 | — | Kiểm chứng thực tế · `cust_list_export_menu_open_viewport.png` |
| REQ-CUST-02 | Khối Customers Summary hiển thị 6 bộ đếm | Tổng quan nhanh số khách hàng và liên hệ | Khối tiêu đề `Customers Summary` có đúng 6 nhãn theo thứ tự: `Total Customers` · `Active Customers` · `Inactive Customers` · `Active Contacts` · `Inactive Contacts` · `Contacts Logged In Today`, mỗi nhãn kèm một số nguyên. Giá trị biến động theo dữ liệu — **không** assert số cụ thể | 🟢 | — | Kiểm chứng thực tế · `cust_list_export_menu_open_viewport.png` |
| REQ-CUST-03 | Total Customers = Active Customers + Inactive Customers | Bộ đếm tổng nhất quán với hai bộ đếm con | Đọc 3 số cùng một lần tải trang → `Total = Active + Inactive`. Đo 2 lần: `2954 = 2945 + 9` và (sau khi tạo 2 KH test, tắt Active 1 KH) `2956 = 2946 + 10`. Số của tổng cũng bằng `N` trong dòng `Showing … of N entries` khi không lọc (REQ-CUST-08) | 🟢 | — | Kiểm chứng thực tế (DOM, 2 lần đo) |
| REQ-CUST-04 | Summary chỉ cập nhật sau khi tải lại trang | Đổi trạng thái Active trên bảng không làm đổi số ngay | (1) Ghi 6 số Summary, (2) tắt công tắc Active của một KH test trên bảng, (3) chờ request `change_client_status` xong → 6 số **không đổi**, (4) tải lại trang → `Active Customers` giảm 1, `Inactive Customers` tăng 1. Cố ý hay không: AMB-CUST-04 | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-05 | Bảng danh sách có 9 cột theo thứ tự cố định | Cấu trúc bảng `#clients` | `thead th` của `#clients` theo thứ tự: ô chọn tất cả (không sắp xếp được, lớp `sorting_disabled not-export`) · `#` · `Company` · `Primary Contact` · `Primary Email` · `Phone` · `Active` · `Groups` · `Date Created`. Mỗi dòng có checkbox `value = <id khách hàng>` | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-06 | Sắp xếp mặc định theo Company tăng dần | Thứ tự khi mở trang | Mở `/admin/clients` → cột `Company` mang lớp `sorting_asc`, các cột khác không. Kiểm bằng dữ liệu test: lọc `auto_cust_` → `auto_cust_20261116…` đứng trước `auto_cust_import_…` đứng trước `auto_cust_tc035_…` | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-07 | Số dòng mỗi trang mặc định 25, chọn được 10/25/50/100/All | Điều khiển phân trang | `select[name=clients_length]` có đúng 5 option, `value` lần lượt `10, 25, 50, 100, -1` (nhãn `-1` là `All`); giá trị chọn sẵn `25`; bảng hiện 25 dòng khi tổng > 25 | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-08 | Dòng thông tin phân trang báo tổng số bản ghi | Người dùng biết đang xem phần nào | Không lọc → `#clients_info` có dạng `Showing 1 to 25 of <N> entries`, `<N>` có dấu phẩy ngăn nghìn (VD `2,954`) và bằng `Total Customers` (REQ-CUST-03) | 🟢 | — | Kiểm chứng thực tế · API · POST /admin/clients/table · 200 (`iTotalRecords`) |
| REQ-CUST-09 | Ô Search tìm theo Company, khớp một phần, không phân biệt hoa thường | Tìm nhanh khách hàng | Nhập `AUTO_CUST_20261116141157` (chữ hoa) vào ô `Search...` của bảng → còn đúng dòng KH test có Company `auto_cust_20261116141157`. Nhập `auto_cust_` → mọi dòng có Company **chứa** chuỗi này (đo được 15 dòng) | 🟢 | — | Kiểm chứng thực tế · `cust_list_export_menu_open_viewport.png` |
| REQ-CUST-10 | Ô Search khớp email của Primary Contact | Tìm KH qua email liên hệ | Nhập email contact chính của KH test (`auto_cust_contact_<timestamp>@auto.test`) → còn đúng dòng KH đó | 🟢 | — | Kiểm chứng thực tế |
| REQ-CUST-11 | Ô Search khớp số điện thoại của khách hàng | Tìm theo cột Phone | Nhập Phone của KH test (VD `0901141157`) → còn đúng dòng KH đó | 🟢 | — | Kiểm chứng thực tế |
| REQ-CUST-12 | Ô Search khớp VAT Number dù cột này không hiển thị | Tìm theo mã số thuế | Nhập VAT Number của KH test (VD `VAT141157`) → còn đúng dòng KH đó, dù bảng không có cột VAT | 🟢 | — | Kiểm chứng thực tế |
| REQ-CUST-13 | Ô Search không tìm theo City | Phạm vi cột tìm kiếm | Nhập City của KH test (`auto_city_141157`, chuỗi duy nhất) → `Showing 0 to 0 of 0 entries`. Cố ý hay không: AMB-CUST-05 | 🟢 | — | Kiểm chứng thực tế |
| REQ-CUST-14 | Khi đang tìm, dòng thông tin ghi rõ tổng trước khi lọc | Người dùng biết kết quả đã bị lọc | Có từ khoá → `#clients_info` có dạng `Showing 1 to <k> of <k> entries (filtered from <N> total entries)` | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-15 | Nút Export mở menu 4 định dạng | Xuất danh sách | Bấm `Export` → menu hiện đúng 4 mục theo thứ tự `Excel` · `CSV` · `PDF` · `Print` | 🟢 | — | Kiểm chứng thực tế · `cust_list_export_menu_open_viewport.png` |
| REQ-CUST-16 | Tệp Export chứa đúng các dòng đang hiển thị theo bộ lọc | Tác tạo của Export — **dùng được** (skill 4.3.8) | Lọc `auto_cust_<timestamp>` → Export `CSV` → tệp có dòng tiêu đề theo cột của bảng (trừ cột chọn `not-export`) và đúng các dòng đang lọc. **Chưa kiểm chứng** — không tải tệp trong lượt recon (AMB-CUST-11) | ⚪ | — | Chưa kiểm chứng |
| REQ-CUST-17 | Hộp thoại Bulk Actions có Mass Delete và Groups | Thao tác hàng loạt | Bấm `Bulk Actions` → modal `#customers_bulk_action` tiêu đề `Bulk Actions`: checkbox `Mass Delete` (bỏ tick sẵn), multi-select `Groups` (`Nothing selected`), dòng cảnh báo đỏ nguyên văn **"If you do not select any group all groups assigned to the selected customers will be removed."**, nút `Close` và `Confirm` | 🟢 | — | Kiểm chứng thực tế · `cust_list_bulk_actions_modal_viewport.png` |
| REQ-CUST-18 | Tick Mass Delete ẩn ô Groups | Hai thao tác loại trừ nhau | Trong modal Bulk Actions tick `Mass Delete` → khối Groups bị tổ tiên lớp `hide` ẩn (`offsetParent === null`); bỏ tick → hiện lại | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-19 | Bulk Confirm thay toàn bộ group của các KH đã chọn | Gán group hàng loạt | Chọn 1 KH test có group A → Bulk Actions → chọn group B → Confirm → KH chỉ còn group B. Không chọn group → mọi group của KH bị gỡ (theo cảnh báo REQ-CUST-17). **Chưa kiểm chứng** (AMB-CUST-10, RISK-CUST-02) | ⚪ | — | UI thực tế — chỉ đọc cảnh báo |
| REQ-CUST-20 | Bulk Mass Delete xoá các KH đã chọn | Xoá hàng loạt | Chỉ chọn KH test → tick Mass Delete → Confirm → các KH đó biến mất khỏi danh sách. **Chưa kiểm chứng** — thao tác xoá KH bị chặn trong phiên recon (AMB-CUST-09) | ⚪ | — | Chưa kiểm chứng |
| REQ-CUST-21 | Menu lọc có New Filter và danh sách bộ lọc đã lưu | Lối vào bộ lọc nâng cao | Bấm nút phễu → menu có liên kết `New Filter`, sau đó là danh sách tên bộ lọc đã lưu. Khi **chưa** áp bộ lọc: `Clear Filter` và `Edit` có `style.display = 'none'`. Sau khi áp một bộ lọc chưa lưu (REQ-CUST-23): `Edit` hiện, `Clear Filter` vẫn ẩn. Tên bộ lọc đã lưu do người dùng đặt — không assert danh sách cụ thể (AMB-CUST-06) | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-22 | Create Filter có 15 loại điều kiện, Apply chỉ bật khi điều kiện có giá trị | Trình tạo bộ lọc | `New Filter` → modal `Create Filter`: dropdown `Add Rule` gồm đúng 15 mục: `Phone · Active · Invoices · Estimates · Proposals · Projects · Contracts Types · City · Zip Code · State · Country · Responsible admin · Groups · Customers assigned to me · Requires Registration Confirmation`; công tắc `Save Filter` (tắt sẵn); nút `Apply`. Thêm rule `Active` → hiện radio `Yes` / `No`, `Apply.disabled === true` cho tới khi chọn một giá trị | 🟢 | — | Kiểm chứng thực tế · `cust_list_create_filter_modal_viewport.png` |
| REQ-CUST-23 | Bộ lọc Active = No chỉ còn khách hàng không hoạt động | Lọc theo cờ Active | Rule `Active` = `No` → `Apply` (không bật Save Filter) → mọi dòng có công tắc Active **tắt**, số dòng bằng `Inactive Customers` của Summary cùng thời điểm (đo: 9 = 9) | 🟢 | — | Kiểm chứng thực tế (DOM) |
| REQ-CUST-24 | Bật Save Filter lưu bộ lọc vào menu | Tác tạo của bộ lọc — **dùng được** | Tạo rule + bật `Save Filter` + đặt tên `auto_filter_<timestamp>` → Apply → tên xuất hiện trong menu phễu; chọn lại → áp đúng điều kiện. **Chưa kiểm chứng** — phạm vi chia sẻ bộ lọc chưa rõ (AMB-CUST-06) | ⚪ | — | Chưa kiểm chứng |
| REQ-CUST-25 | Công tắc Active trên dòng đổi trạng thái khách hàng ngay, lưu bền | Bật/tắt KH không cần mở form | Trên dòng KH test bấm công tắc Active → request `GET /admin/clients/change_client_status/<id>/0` (tắt) hoặc `/1` (bật) trả 200; tải lại trang → công tắc giữ trạng thái mới. Tooltip của công tắc nguyên văn **"Won't be shown in dropdowns when creating new records"** | 🟢 | — | Kiểm chứng thực tế · API · GET /admin/clients/change_client_status/{id}/{0\|1} · 200 |
| REQ-CUST-26 | Khách hàng Inactive không xuất hiện trong dropdown chọn KH khi tạo bản ghi mới | Hệ quả nghiệp vụ của cờ Active — **dùng được** (skill 4.3.8) | Tắt Active KH test → mở form tạo Invoice → dropdown Customer **không** có KH đó; bật lại → có. **Chưa kiểm chứng** — chỉ có tooltip REQ-CUST-25 làm căn cứ | ⚪ | — | Suy từ tooltip — chưa kiểm chứng |
| REQ-CUST-27 | Dòng KH có liên kết vào hồ sơ và tuỳ chọn khi rê chuột | Điều hướng từ bảng | Ô Company là liên kết tới `/admin/clients/client/<id>`; khối `.row-options` của dòng KH test có `View` (→ `/admin/clients/client/<id>`) · `Contacts` (→ `?group=contacts`) · `Delete` (→ `/admin/clients/delete/<id>`, lớp `_delete`). Ô `Date Created` định dạng `DD-MM-YYYY HH:mm:ss`. Một số dòng dữ liệu cũ hiện nhãn `Person - View Profile` và chỉ có `View \| Delete` — chưa rõ nguồn gốc (AMB-CUST-07) | 🟢 | — | Kiểm chứng thực tế (DOM) · API · POST /admin/clients/table · 200 |

## 2. Ánh xạ tìm kiếm & lọc (bản web — phần CSDL ở index mục 6.3.2)

| Điều khiển | Cột / trường quan sát được | Kiểu khớp | Hoa thường | REQ |
|---|---|---|---|---|
| Ô `Search...` | Company · email Primary Contact · Phone · VAT Number | chứa | không phân biệt | REQ-CUST-09 → 12 |
| Ô `Search...` | City — **không** khớp | — | — | REQ-CUST-13 |
| Sắp xếp mặc định | Company | tăng dần | — | REQ-CUST-06 |
| Rule `Active` | cờ Active | chính xác (`1` / `0`) | — | REQ-CUST-23 |

## 3. Business Rules & Validation Messages

| REQ ID | Rule / Trigger | Thông báo (nguyên văn) |
|---|---|---|
| REQ-CUST-17 | Mở Bulk Actions | "If you do not select any group all groups assigned to the selected customers will be removed." |
| REQ-CUST-25 | Rê chuột lên công tắc Active | "Won't be shown in dropdowns when creating new records" |

## 4. User Flow — lọc danh sách theo Active

1. `/admin/clients` → bấm nút phễu → `New Filter`
2. `Add Rule` → chọn `Active` → chọn `No` → `Apply` (REQ-CUST-22, 23)
3. Bảng chỉ còn KH Inactive; tải lại trang để bỏ bộ lọc chưa lưu
