# Requirements — Khách hàng (`CUST`)

> **INDEX module — tên file bất biến.** Phần dùng chung · phân quyền · trạng thái · ánh xạ CSDL · AMB/RISK · phân rã Story · Nhật ký. REQ chi tiết nằm ở file nền tảng và file story (xem **Bản đồ tài liệu**).
> ← [Danh mục hệ thống](../README.md) · [Bản đồ khám phá — module 02](../_discovery/modules/module_02_khach_hang.md)

## 1. Metadata & Tổng quan

| Thuộc tính | Giá trị |
|---|---|
| **Module** | Khách hàng khu admin — Customers (gồm Contacts) |
| **Prefix** | `CUST` (cấp bởi `/discover-system` 02-11-2026) |
| **Hệ thống** | `CRM` — Perfex CRM 3.1.6, khu admin `/admin/*` |
| **Nền tảng** | Web ✅ · Android — chưa có · iOS — chưa có · API — chưa có |
| **Dải mã đã dùng** | `REQ-CUST-01` → `REQ-CUST-115` · `AMB-CUST-01` → `AMB-CUST-23` · `RISK-CUST-01` → `RISK-CUST-09` (đợt 1: UI recon 16-11-2026 — REQ 01 → 115, AMB 01 → 20, RISK 01 → 09 · đợt 2: câu hỏi Q3, Q4, Q8 khi sinh TC Story 02, 16-11-2026 — AMB 21 → 23) |
| **Mã kế tiếp** | Đợt phân tích sau bắt đầu từ `REQ-CUST-116` · `AMB-CUST-24` · `RISK-CUST-10` — **KHÔNG đánh lại từ 01** |
| **Nguồn** | Khảo sát UI thực tế (mode UI — user xác nhận không có tài liệu, 16-11-2026) |
| **Môi trường** | 🔒 Dùng chung (~2.956 KH, phần lớn do người khác tạo). User cho phép 16-11-2026: **tạo + sửa + xoá bản ghi do chính lượt test tạo** (`auto_cust_<timestamp>`); không đụng bản ghi có sẵn |
| **Ngày khảo sát** | 16-11-2026 |

**Mục đích:** quản lý khách hàng (công ty) — thực thể trung tâm mà ≥ 12 module khác tham chiếu — cùng liên hệ (contact), ghi chú, nhắc việc, tệp, vault, sao kê công nợ và địa chỉ.

**Trong phạm vi** (user chốt 16-11-2026 — "Lõi + tab riêng"): danh sách `/admin/clients` (Summary, tìm kiếm, lọc, Export, Bulk Actions, Active) · form tạo/sửa (3 tab con) · Customer Admins · Contacts (tab + trang tổng `/admin/clients/all_contacts`) · Import CSV · Notes · Statement · Files · Vault · Reminders · Map · 11 tab liên kết module khác ở mức "danh sách lọc theo KH + nút tạo mới".

**Ngoài phạm vi:** nghiệp vụ chứng từ của 11 module liên kết (thuộc `INV`, `PAY`, `PROP`, `CRN`, `EST`, `SUBS`, `EXP`, `CTR`, `PRJ`, `TASK`, `TICK`) · đăng nhập và quyền của contact ở cổng khách hàng (`/clients/*`) · cấu hình mặc định quyền contact, nhóm KH, Google API key ở Setup (`SETTING`, BLOCKED).

### Bản đồ phủ tài liệu

Không có tài liệu — toàn bộ REQ sinh từ khảo sát UI thực tế.

## Bản đồ tài liệu

| Nền tảng | File | Story | REQ bao phủ |
|---|---|---|---|
| Chung ≥ 2 nền tảng | chính file này | — | Không có — module mới có một nền tảng |
| Web | [web/requirements_customers_web.md](web/requirements_customers_web.md) | metadata khảo sát · NFR · Danh mục Evidence | — (mục lục story) |
| Web | [web/stories/story_01_danh_sach.md](web/stories/story_01_danh_sach.md) | STORY-CUST-01 | `REQ-CUST-01` → `REQ-CUST-27` |
| Web | [web/stories/story_02_tao_sua_khach_hang.md](web/stories/story_02_tao_sua_khach_hang.md) | STORY-CUST-02 | `REQ-CUST-28` → `REQ-CUST-52` |
| Web | [web/stories/story_03_lien_he.md](web/stories/story_03_lien_he.md) | STORY-CUST-03 | `REQ-CUST-53` → `REQ-CUST-72` |
| Web | [web/stories/story_04_import.md](web/stories/story_04_import.md) | STORY-CUST-04 | `REQ-CUST-73` → `REQ-CUST-80` |
| Web | [web/stories/story_05_ghi_chu_nhac_viec_tep.md](web/stories/story_05_ghi_chu_nhac_viec_tep.md) | STORY-CUST-05 | `REQ-CUST-81` → `REQ-CUST-95` |
| Web | [web/stories/story_06_vault_statement_map.md](web/stories/story_06_vault_statement_map.md) | STORY-CUST-06 | `REQ-CUST-96` → `REQ-CUST-104` |
| Web | [web/stories/story_07_tab_lien_ket.md](web/stories/story_07_tab_lien_ket.md) | STORY-CUST-07 | `REQ-CUST-105` → `REQ-CUST-115` |

**Tổng: 115 REQ** = 0 ở index + 115 ở `web/stories/` · trạng thái 🟢 99 · ⚪ 16 (REQ-CUST-16, 19, 20, 24, 26, 34, 44, 52, 71, 72, 79, 80, 90, 95, 99, 104).

## 2. Yêu cầu dùng chung nhiều nền tảng

Không áp dụng — module mới khảo sát trên Web. Khi khảo sát app/API, rule trùng sẽ được chuyển lên đây (giữ nguyên mã, mở rộng cột `Nền tảng`).

## 3. Ánh xạ dữ liệu (Field ↔ CSDL)

`Truy vấn CSDL: ✅ chỉ SELECT` nhưng **chưa có kết nối** (AMB-SYS-05, `.env` chưa có `DB_*`) → chưa khảo sát schema. Bảng dưới chỉ ghi **tên field trong payload** quan sát được; cột CSDL là placeholder — TC `@DBCheck` dùng placeholder kèm `@NeedsVerify` cho tới khi điền.

| Field (Label) / dữ liệu hệ thống sinh | Tên field (payload) | Bảng.cột | Nhạy cảm? | REQ liên quan | Cách đã xác minh |
|---|---|---|---|---|---|
| `Company` | `company` | `<bảng KH>.<cột company>` | — | REQ-CUST-30, 31, 39 | Chưa — placeholder |
| `VAT Number` · `Phone` · `Website` | `vat` · `phonenumber` · `website` | `<bảng KH>.<cột>` | — | REQ-CUST-40 | Chưa — placeholder |
| Cờ Active KH | (switch) `change_client_status/{id}/{0\|1}` | `<bảng KH>.<cột active>` | — | REQ-CUST-25 | Chưa — placeholder |
| *(hệ thống sinh)* Date Created | — | `<bảng KH>.<cột ngày tạo>` | — | REQ-CUST-27 | Chưa — múi giờ chưa chốt |
| Contact: `firstname` · `lastname` · `email` · `title` · `phonenumber` | như tên field | `<bảng contact>.<cột>` | email người khác → che | REQ-CUST-64 | Chưa — placeholder |
| Contact: mật khẩu | `password` | `<bảng contact>.<cột mật khẩu>` | 🔒 chỉ kiểm hình thái | REQ-CUST-60 | Chưa — placeholder |
| Contact: `is_primary` · cờ Active | `is_primary` · switch `change_contact_status` | `<bảng contact>.<cột>` | — | REQ-CUST-61, 69 | Chưa — placeholder |
| Vault: `server_address` · `username` · `password` | như tên field | `<bảng vault>.<cột>` | 🔒 password | REQ-CUST-99 | Chưa — placeholder |

Kiểu xoá (mềm / cứng) của KH và contact: **chưa rõ** (REQ-CUST-52, 72 ⚪).

### 3.1. Ánh xạ tìm kiếm & lọc

| Ô tìm / bộ lọc / sắp xếp | Cột CSDL | Kiểu khớp | Hoa thường | Có dấu – không dấu | Ký tự đặc biệt | Mặc định | REQ | Cách đã xác minh |
|---|---|---|---|---|---|---|---|---|
| Ô `Search...` danh sách KH | `<company>` · `<email contact chính>` · `<phonenumber>` · `<vat>` | chứa | không phân biệt | ❔ chưa thử | ❔ chưa thử | — | REQ-CUST-09 → 12 | Tạo KH test qua UI, tìm từng biến thể |
| Ô `Search...` — City | — | không tìm | — | — | — | — | REQ-CUST-13 | Thử chuỗi City duy nhất → 0 dòng |
| Sắp xếp mặc định | `<company>` tăng dần | — | — | — | — | ✅ | REQ-CUST-06 | Quan sát UI (`sorting_asc`) |
| Rule `Active` | `<active>` | chính xác | — | — | — | — | REQ-CUST-23 | Số dòng = Inactive Customers |
| Sắp xếp Contacts tổng | `<firstname>` tăng dần | — | — | — | — | ✅ | REQ-CUST-70 | Quan sát UI |

## 4. Ma trận Phân quyền

| Hành động | Admin (tài khoản `.env`) | Nhân viên role khác (VD "Project Manager") | Contact khách hàng |
|---|---|---|---|
| Xem danh sách KH | ✅ | ❔ | — |
| Tạo KH | ✅ | ❔ | — |
| Sửa KH | ✅ | ❔ | — |
| Xoá KH | ❔ | ❔ | — |
| Import KH | ✅ | ❔ | — |
| Thêm / sửa contact | ✅ | ❔ | — |
| Tạo vault entry | ❔ | ❔ | — |

Tổng 21 ô = Đã kiểm chứng 5 · Suy diễn 0 · Chưa rõ 9 · Không áp dụng 7.
Ô "không áp dụng" là toàn bộ cột *Contact khách hàng* (7 ô) — contact không vào được khu admin (Assumption tạm AMB-LOGIN-03 / REQ-LOGIN-29); quyền của contact ở cổng KH (6 quyền REQ-CUST-62) thuộc phạm vi cổng khách hàng.
[Xoá KH × Admin] là ❔ vì thao tác xoá KH bị chặn trong phiên recon (AMB-CUST-09); [Tạo vault entry × Admin] là ❔ vì agent không nhập mật khẩu (AMB-CUST-13). Cột *Nhân viên role khác*: danh sách nhân viên ở `Assign Admin` có một nhân viên tên **"Project Manager"** — chưa có tài khoản để kiểm (AMB-CUST-08, gắn AMB-LOGIN-24).

## 5. Ma trận Trạng thái

Không có chuỗi trạng thái (status flow). Ba cờ trạng thái quan sát được:

| Entity | Trạng thái hiện tại | Hành động | Trạng thái kế tiếp | Ai thực hiện | REQ |
|---|---|---|---|---|---|
| Khách hàng | Active | Tắt công tắc Active trên danh sách | Inactive — không hiện ở dropdown khi tạo bản ghi mới (⚪) | Admin | REQ-CUST-25, 26 |
| Khách hàng | Inactive | Bật công tắc Active | Active | Admin | REQ-CUST-25 |
| Khách hàng | Bất kỳ | Delete + xác nhận | Đã xoá (⚪ — kiểu xoá chưa rõ) | ❔ | REQ-CUST-52 |
| Contact | Active (mặc định khi tạo / import) | Tắt công tắc Active | Inactive | Admin | REQ-CUST-64, 69, 76 |
| Contact | Inactive | Bật công tắc Active | Active | Admin | REQ-CUST-69 |
| Reminder | Is notified = No | Tới giờ nhắc (job nền) | Is notified = Yes (⚪) | Hệ thống | REQ-CUST-89, 90 |

## 6. Điểm Mơ Hồ & Rủi Ro

### Ambiguities

| Mã | Câu hỏi | Nguy cơ | Mức độ | Assumption tạm | Trạng thái | Kết luận |
|---|---|---|---|---|---|---|
| AMB-CUST-01 | Company chỉ gồm khoảng trắng vượt qua validation phía trình duyệt, và môi trường đã có bản ghi Company toàn khoảng trắng (id 9330). Server có chặn không? Có phải lỗi? | KH không có tên hiển thị → chọn nhầm KH ở hoá đơn, báo cáo | 🔴 | Hành vi hiện tại là thật (REQ-CUST-31), nghi lỗi | ❓ Chờ trả lời | — |
| AMB-CUST-02 | Độ dài tối đa của Company, VAT, Phone, Website, địa chỉ là bao nhiêu? Giao diện không đặt `maxlength` | TC biên không có mốc; nhập quá dài có thể lỗi CSDL | 🟡 | Không kiểm biên độ dài cho tới khi có câu trả lời hoặc schema CSDL | ❓ Chờ trả lời | — |
| AMB-CUST-03 | Ghi chú với mô tả **trống** vẫn được lưu ("Note added successfully."). Cố ý? | Bản ghi rác, nhật ký KH vô nghĩa | 🔴 | Hành vi hiện tại là thật (REQ-CUST-82), nghi lỗi | ❓ Chờ trả lời | — |
| AMB-CUST-04 | Customers Summary không cập nhật ngay khi đổi Active trên bảng, chỉ đổi sau khi tải lại trang. Cố ý? | Người dùng thấy số lệch thực tế | 🟢 | Hành vi hiện tại là đúng (REQ-CUST-04) | ❓ Chờ trả lời | — |
| AMB-CUST-05 | Ô Search danh sách KH không tìm theo City (và địa chỉ). Phạm vi cột tìm kiếm mong muốn là gì? | Người dùng không tìm được KH theo thành phố | 🟢 | Hành vi hiện tại là đúng (REQ-CUST-13) | ❓ Chờ trả lời | — |
| AMB-CUST-06 | Bộ lọc đã lưu là của riêng từng nhân viên hay dùng chung toàn hệ thống? Menu lọc đang có các bộ lọc do người khác tạo — nhưng môi trường dùng chung **một** tài khoản admin nên không phân biệt được | TC REQ-CUST-24 kỳ vọng sai phạm vi | 🟡 | Theo từng nhân viên — chưa kiểm được với một tài khoản | ❓ Chờ trả lời | — |
| AMB-CUST-07 | Nhiều dòng hiện Company là `Person - View Profile` nhưng kiểm trùng tên với chuỗi này trả `exists: false`. Nhãn này là dữ liệu thật hay nhãn hệ thống sinh khi KH là cá nhân? | TC tìm/sắp xếp theo Company sai với các dòng này | 🟡 | Dữ liệu cũ do người khác tạo — không dùng làm dữ liệu test | ❓ Chờ trả lời | — |
| AMB-CUST-08 | Xin tài khoản nhân viên role khác (VD nhân viên "Project Manager" thấy trong danh sách Assign Admin) để kiểm chứng 7 ô phân quyền đang ❔. Gắn AMB-LOGIN-24 | Không biết nhân viên thường xem/sửa/xoá KH được tới đâu (thường chỉ KH mình phụ trách) | 🔴 | Không suy quyền từ Admin — ô giữ ❔ | ❓ Chờ trả lời | — |
| AMB-CUST-09 | Xoá KH: xoá cứng hay mềm? KH đang có hoá đơn/giao dịch có xoá được không, thông báo là gì? Contact, note, file, vault đi theo thế nào? Thao tác xoá KH bị chặn trong phiên recon | REQ-CUST-20, 52 không có Expected cụ thể | 🟡 | Xoá được KH không có giao dịch, contact bị xoá theo | ❓ Chờ trả lời | — |
| AMB-CUST-10 | Bulk Actions Confirm khi **không** chọn group sẽ gỡ toàn bộ group của các KH đã chọn (theo cảnh báo trên UI). Cố ý thiết kế như vậy? | Mất phân nhóm hàng loạt do bấm nhầm (RISK-CUST-02) | 🟡 | Đúng như cảnh báo | ❓ Chờ trả lời | — |
| AMB-CUST-11 | Tệp Export (Excel/CSV/PDF/Print) có xuất đúng cột, đúng bộ lọc đang áp, và với lựa chọn `All` có giới hạn số dòng không? Chưa tải tệp trong lượt recon | REQ-CUST-16 chưa có căn cứ | 🟡 | Xuất đúng các dòng đang lọc, bỏ cột chọn | ❓ Chờ trả lời | — |
| AMB-CUST-12 | "Save and create contact" sau khi lưu có mở ngay modal tạo contact của KH mới không? | REQ-CUST-44 chưa có căn cứ | 🟢 | Có | ❓ Chờ trả lời | — |
| AMB-CUST-13 | Vault: tester tự tạo mục vault bằng mật khẩu giả để kiểm che/hiện mật khẩu và 3 mức `visibility` — agent không nhập mật khẩu vào ô | REQ-CUST-99 chưa kiểm chứng | 🟡 | Mật khẩu che mặc định, chỉ người thuộc mức visibility xem được | ❓ Chờ trả lời | — |
| AMB-CUST-14 | Reminder chạy bằng job nền (cron) — tần suất bao lâu, thông báo hiện ở đâu, email có gửi khi tick? | REQ-CUST-90 chờ sai mốc | 🟡 | Thông báo trong hệ thống ≤ 15 phút sau mốc | ❓ Chờ trả lời | — |
| AMB-CUST-15 | Danh sách đuôi tệp cho phép thiếu `.jpeg`, `.gif`, `.txt`, `.csv`. Cố ý? (cấu hình ở Setup — BLOCKED) | Người dùng không tải được ảnh `.jpeg` phổ biến | 🟢 | Danh sách hiện tại là đúng (REQ-CUST-92) | ❓ Chờ trả lời | — |
| AMB-CUST-16 | Recon chạy ở viewport 973×853 (khung Browser của app); viewport chuẩn dự án `1600×750` chưa khảo sát. Ở 973 menu tab xếp dọc, bảng Contacts/Files cuộn ngang | Locator / ảnh automation chạy ở 1600 có bố cục khác | 🟡 | AC chỉ assert nội dung và thuộc tính, không assert bố cục; recon bổ sung ở 1600×750 khi có Playwright MCP | ❓ Chờ trả lời | — |
| AMB-CUST-17 | Contact Inactive có bị chặn đăng nhập cổng KH không? Welcome email / Set password email có gửi đúng không? Cần cổng KH + hộp thư test | REQ-CUST-71 chưa kiểm chứng | 🟡 | Có hiệu lực như tên gọi | ❓ Chờ trả lời | — |
| AMB-CUST-18 | Ô Phone của contact điền sẵn `+84` theo Country `Vietnam` của KH. KH không có Country thì điền gì? | TC REQ-CUST-58 thiếu nhánh | 🟢 | Để trống | ❓ Chờ trả lời | — |
| AMB-CUST-19 | Tên nhóm KH (Groups) trùng nhau rất nhiều (317 option, 72 tên khác nhau). Hệ thống có ràng buộc tên nhóm duy nhất không? Nhóm quản lý ở Setup (BLOCKED) | Chọn nhầm nhóm cùng tên; dữ liệu test của người khác làm nhiễu | 🟢 | Không ràng buộc duy nhất | ❓ Chờ trả lời | — |
| AMB-CUST-20 | Simulate Import hiển thị `0` ở cột Country / Billing country / Shipping country khi tệp để trống. Import thật lưu `0` hay rỗng? | KH nhập vào có Country sai | 🟢 | Lưu rỗng | ❓ Chờ trả lời | — |
| AMB-CUST-21 | VAT Number, Phone, Website, Zip Code **không** kiểm định dạng (Phone nhận chữ, Website nhận chuỗi không phải URL, Zip nhận chữ). Cố ý? | Dữ liệu liên hệ sai lan sang hoá đơn, email | 🟡 | Cố ý — mọi chuỗi lưu nguyên văn (Q3 khi sinh TC Story 02) | ❓ Chờ trả lời | — |
| AMB-CUST-22 | VAT Number có phải duy nhất giữa các KH không? | Hai KH trùng mã số thuế | 🟢 | Không bắt buộc duy nhất (Q4) | ❓ Chờ trả lời | — |
| AMB-CUST-23 | Hai người cùng sửa một KH: bản lưu sau ghi đè hay hệ thống báo xung đột? | Mất thay đổi của người lưu trước | 🟢 | Bản lưu sau ghi đè, không báo (Q8) | ❓ Chờ trả lời | — |

### Risks

| Mã | Rủi ro | Mô tả | Mitigation |
|---|---|---|---|
| RISK-CUST-01 | Dữ liệu dùng chung | ~2.956 KH phần lớn do người khác tạo, một tài khoản admin dùng chung | TC chỉ dùng bản ghi `auto_cust_<timestamp>` tự tạo; không assert số đếm tuyệt đối (dùng quan hệ / chênh lệch); không sửa, xoá bản ghi có sẵn |
| RISK-CUST-02 | Bulk Actions làm mất dữ liệu hàng loạt | Mass Delete và "Confirm không chọn group" tác động mọi KH đang tick | TC chỉ tick KH test, lọc theo `auto_cust_<timestamp>` trước khi tick; không dùng "chọn tất cả" |
| RISK-CUST-03 | Đổi trạng thái bằng GET | `change_client_status` / `change_contact_status` là GET kèm `csrf_token_name` trên URL — token có thể lọt vào log, lịch sử, header Referer | Báo dev/Security; TC bảo mật riêng; không chép token vào tài liệu |
| RISK-CUST-04 | Lộ đường dẫn máy chủ | Dòng tệp đính kèm có `data-path` chứa đường dẫn tuyệt đối trên máy chủ | Báo dev; không chép đường dẫn vào `docs/` |
| RISK-CUST-05 | Mật khẩu mặc định hiển thị rõ | `Default password for all contacts` ở Import là ô `text` | Báo dev; TC không dùng mật khẩu thật |
| RISK-CUST-06 | Vault chứa thông tin truy cập nhạy cảm | Mục vault lưu server / username / password của khách hàng | Chỉ dùng giá trị giả; không chụp ảnh mục vault có dữ liệu; kiểm 3 mức visibility bằng tài khoản riêng |
| RISK-CUST-07 | KH không có tên | Company toàn khoảng trắng được chấp nhận (AMB-CUST-01) | TC REQ-CUST-31 ghi rõ là hành vi nghi lỗi; báo PO |
| RISK-CUST-08 | Bố cục phụ thuộc viewport | Recon ở 973×853 (AMB-CUST-16) | Automation dùng locator ngữ nghĩa, không dựa vị trí; recon lại ở 1600×750 trước khi sinh script |
| RISK-CUST-09 | Dữ liệu test của lượt recon được giữ lại | KH id 16007 (kèm contact, reminder) và id 16008 (kèm contact) còn trên môi trường — user chốt 16-11-2026 **giữ lại** để dùng cho lượt sinh test case | TC có thể dùng 2 KH này làm dữ liệu có sẵn nhưng **không** phụ thuộc giá trị cụ thể (id, số đếm); TC cần trạng thái sạch vẫn tự tạo `auto_cust_<timestamp>` riêng; cộng 2 KH này khi đối chiếu số đếm |

## 7. Phân rã Epic / Story

**Epic:** Quản lý khách hàng khu admin (`CUST`).

| Story ID | Tên Story | REQ bao phủ | Số REQ | AMB / RISK liên quan | Ghi chú phạm vi |
|---|---|---|---|---|---|
| STORY-CUST-01 | Danh sách & tóm tắt | REQ-CUST-01 → 27 | 27 | AMB-CUST-04, 05, 06, 07, 10, 11 · RISK-CUST-02, 03 | Summary, tìm kiếm, sắp xếp, phân trang, Export, Bulk, bộ lọc, Active |
| STORY-CUST-02 | Tạo, sửa & hồ sơ KH | REQ-CUST-28 → 52 | 25 | AMB-CUST-01, 02, 09, 12, 21, 22, 23 · RISK-CUST-07 | Form 3 tab con, trùng tên, địa chỉ, Customer Admins, menu 19 tab, xoá |
| STORY-CUST-03 | Liên hệ (Contacts) | REQ-CUST-53 → 72 | 20 | AMB-CUST-17, 18 | Modal contact, email duy nhất, mật khẩu, quyền, Active, trang tổng |
| STORY-CUST-04 | Import CSV | REQ-CUST-73 → 80 | 8 | AMB-CUST-20 · RISK-CUST-05 | Mô phỏng, nhập thật, trùng email |
| STORY-CUST-05 | Ghi chú · Nhắc việc · Tệp | REQ-CUST-81 → 95 | 15 | AMB-CUST-03, 14, 15 · RISK-CUST-04 | Notes, Reminders, Files |
| STORY-CUST-06 | Vault · Statement · Map | REQ-CUST-96 → 104 | 9 | AMB-CUST-13 · RISK-CUST-06 | Vault, sao kê, toạ độ |
| STORY-CUST-07 | Tab liên kết module khác | REQ-CUST-105 → 115 | 11 | — | 11 tab chứng từ, mức hiển thị + nút tạo mới |

**Tổng: 7 Story / 115 REQ — mọi REQ thuộc đúng một Story, không mồ côi, không trùng.** `27 + 25 + 20 + 8 + 15 + 9 + 11 = 115 ✔`

| Nhóm | Mã | Nằm ở đâu |
|---|---|---|
| AMB thuộc Story | AMB-CUST-01 → 07, 09 → 15, 17, 18, 20 → 23 | phân bổ ở bảng Story |
| AMB cấp Epic | AMB-CUST-08, 16, 19 | Ma trận Phân quyền (08) · viewport cắt ngang mọi Story (16) · dữ liệu master nhóm KH ở Setup (19) |
| RISK thuộc Story | RISK-CUST-02 → 07 | phân bổ ở bảng Story |
| RISK cấp Epic | RISK-CUST-01, 08, 09 | dữ liệu dùng chung · viewport · dữ liệu test giữ lại — cắt ngang mọi Story |

Kiểm: AMB 20 (Story) + 3 (Epic) = 23 ✔ · RISK 6 + 3 = 9 ✔

**Hạng mục cấp Epic** (cố ý không gán vào Story): Ma trận Phân quyền (mục 4) · Ma trận Trạng thái (mục 5) · Ánh xạ dữ liệu (mục 3) · Yêu cầu phi chức năng (file `web/`, mục 4) · AMB-CUST-08, 16, 19 · RISK-CUST-01, 08, 09.

**Thứ tự triển khai đề xuất:** STORY-CUST-02 → 01 → 03 → 05 → 04 → 06 → 07.
- STORY-CUST-02 trước: mọi Story khác cần KH test tạo bằng form này
- 🔴 AMB-CUST-01 (REQ-CUST-31) và AMB-CUST-03 (REQ-CUST-82) đang **chờ PO** — TC vẫn viết theo hành vi hiện tại, gắn nhãn `assumption-based`; PO trả lời khác thì TC phải sửa
- REQ ⚪ **chưa chạy kiểm chứng được** nếu thiếu điều kiện: REQ-CUST-16, 79 (quyền tải tệp) · REQ-CUST-19, 20, 52, 72 (cho phép xoá bản ghi test — AMB-CUST-09) · REQ-CUST-24 (AMB-CUST-06) · REQ-CUST-26 (mở form chứng từ module khác) · REQ-CUST-34, 44, 80, 104 (chưa thao tác — làm được ngay) · REQ-CUST-71, 95 (cổng KH + hộp thư test) · REQ-CUST-90 (chờ job nền) · REQ-CUST-99 (tester tự nhập mật khẩu giả)
- Cột *Nhân viên role khác* của ma trận phân quyền BLOCKED cho tới khi có tài khoản (AMB-CUST-08)

## 8. Nhật ký thay đổi

| Ngày | Nguồn | REQ ảnh hưởng | Loại | Tóm tắt thay đổi | TC cần xử lý |
|---|---|---|---|---|---|
| 16-11-2026 | `/generate-testcases-manual-rbt` Story 02 — Bước 2 Q&A | AMB-CUST-21 → 23 (mới) · không REQ nào đổi | ✏️ Biên tập | Thêm 3 AMB từ câu hỏi Q3 (định dạng VAT/Phone/Website/Zip), Q4 (VAT duy nhất), Q8 (sửa đồng thời); user chấp nhận giả định Q1 → Q10 để viết TC — AMB vẫn ❓ chờ PO | Bộ TC Story 02 viết theo giả định: CRM_CUST_TC_021 → 023, 027, 049 nhãn `assumption-based` |
| 16-11-2026 | Trả lời trực tiếp của user | RISK-CUST-09 | ✏️ Biên tập | User chốt giữ lại 2 KH test (id 16007, 16008) cho lượt sinh test case — sửa mô tả và mitigation của RISK-CUST-09. Không REQ nào đổi | — |
| 16-11-2026 | UI recon | REQ-CUST-01 → 115 · AMB-CUST-01 → 20 · RISK-CUST-01 → 09 | 🟢 Thêm | Khởi tạo tài liệu từ khảo sát UI thực tế trên trình duyệt tích hợp của Claude desktop app (mode UI, viewport 973×853). 7 Story, 17 ảnh evidence. Tạo 2 KH test (id 16007, 16008) — chưa dọn (RISK-CUST-09) | — (viết mới) |
