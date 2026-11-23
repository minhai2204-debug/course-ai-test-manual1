# Requirements Web — Khách hàng (`CUST`)

> ← [Index module `REQUIREMENTS_CUSTOMERS_SUMMARY.md`](../REQUIREMENTS_CUSTOMERS_SUMMARY.md) — phân quyền · trạng thái · ánh xạ CSDL · AMB/RISK · Story · Nhật ký nằm ở index.
>
> File nền tảng web vượt ngưỡng 80 REQ và module có 2 entity (Customer · Contact) → REQ chi tiết nằm ở **7 file story** (skill mục 5.1, 5.2). File này giữ metadata khảo sát, mục lục story, yêu cầu phi chức năng và Danh mục Evidence.

## 1. Metadata khảo sát

| Thuộc tính | Giá trị |
|---|---|
| **Nền tảng** | Web — khu admin |
| **REQ trong file nền tảng** | `REQ-CUST-01` → `REQ-CUST-115` (115 REQ, chia ở 7 file story) |
| **Trình duyệt khảo sát** | Trình duyệt tích hợp của Claude desktop app (Chromium 152, headed), viewport **973×853** (khung Browser của app — không đạt được viewport chuẩn `1600×750` của dự án: giả lập kích thước lớn hơn khung bị co ảnh và vỡ bố cục). Ở viewport này menu tab hồ sơ KH xếp dọc và một số bảng cuộn ngang (AMB-CUST-16). Mọi AC dựa trên thông báo mặc định của trình duyệt **chỉ đúng với trình duyệt này** |
| **Phiên khảo sát** | Tài khoản admin trong `.env` (hiển thị tên `Admin Example`). Bước đăng nhập do **user tự thao tác**; agent đọc DOM, thao tác và chụp ảnh |
| **Tầng network** | Quan sát thụ động request do UI phát sinh (`read_network_requests`). Không gọi API trực tiếp |
| **Dữ liệu test do lượt này tạo** | KH `auto_cust_20261116141157` (id 16007) + contact `auto_cust_contact_20261116141157@auto.test` + 1 reminder · KH `auto_cust_import_20261116141157` (id 16008, tạo bằng Import) + 1 contact. Đã dọn: 1 note, 1 tệp PDF. **Giữ lại 2 KH** theo quyết định của user 16-11-2026 (thao tác xoá KH cũng bị chặn trong phiên) — RISK-CUST-09 |
| **Ngày** | 16-11-2026 |

**Quy ước cột `Nguồn`:** `Kiểm chứng thực tế` = đã thao tác và xác nhận · `UI thực tế (DOM)` = chỉ đọc thuộc tính, chưa thao tác · `API · <method> <route> · <status>` = từ tầng network.
**Trạng thái ⚪** = chưa kiểm chứng được trong lượt recon (tác tạo cần tải tệp / chờ job nền / cổng KH / thao tác xoá KH bị chặn) — luôn ghi lý do ngay trong AC.

## 2. Bản đồ phủ tài liệu

Không có tài liệu — toàn bộ REQ sinh từ khảo sát UI thực tế (user xác nhận 16-11-2026: module `CUST` không có spec, ticket, file field hay mockup).

## 3. Mục lục Story (REQ chi tiết)

| Story | File | REQ | Số REQ |
|---|---|---|---|
| STORY-CUST-01 — Danh sách & tóm tắt | [stories/story_01_danh_sach.md](stories/story_01_danh_sach.md) | REQ-CUST-01 → 27 | 27 |
| STORY-CUST-02 — Tạo, sửa & hồ sơ KH | [stories/story_02_tao_sua_khach_hang.md](stories/story_02_tao_sua_khach_hang.md) | REQ-CUST-28 → 52 | 25 |
| STORY-CUST-03 — Liên hệ (Contacts) | [stories/story_03_lien_he.md](stories/story_03_lien_he.md) | REQ-CUST-53 → 72 | 20 |
| STORY-CUST-04 — Import CSV | [stories/story_04_import.md](stories/story_04_import.md) | REQ-CUST-73 → 80 | 8 |
| STORY-CUST-05 — Ghi chú · Nhắc việc · Tệp | [stories/story_05_ghi_chu_nhac_viec_tep.md](stories/story_05_ghi_chu_nhac_viec_tep.md) | REQ-CUST-81 → 95 | 15 |
| STORY-CUST-06 — Vault · Statement · Map | [stories/story_06_vault_statement_map.md](stories/story_06_vault_statement_map.md) | REQ-CUST-96 → 104 | 9 |
| STORY-CUST-07 — Tab liên kết module khác | [stories/story_07_tab_lien_ket.md](stories/story_07_tab_lien_ket.md) | REQ-CUST-105 → 115 | 11 |

`27 + 25 + 20 + 8 + 15 + 9 + 11 = 115 ✔`

## 4. Yêu cầu phi chức năng (quan sát được trên web)

| Hạng mục | Quan sát | Ghi chú |
|---|---|---|
| Hiệu năng danh sách | Bảng ~2.956 KH dùng DataTables **server-side** (`POST /admin/clients/table`), mỗi lần tải 25 dòng | Không đo thời gian phản hồi — không có công cụ đo trong lượt recon |
| Bảo mật — CSRF | Mọi form có `csrf_token_name` (`<32 ký tự hex>`); đổi trạng thái Active dùng **GET** kèm token trên URL (RISK-CUST-03) | — |
| Bảo mật — lộ thông tin | Dòng tệp đính kèm có thuộc tính `data-path` chứa đường dẫn tuyệt đối trên máy chủ (RISK-CUST-04) | Không chép đường dẫn vào tài liệu |
| Bảo mật — hiển thị mật khẩu | `Default password for all contacts` ở Import là ô `text` (RISK-CUST-05) | — |
| Đa ngôn ngữ dữ liệu | Lưu và hiển thị đúng tiếng Việt có dấu (`QA auto sửa`, `auto_note_… cập nhật`) | REQ-CUST-68, 83 |
| Responsive | Viewport 973×853: menu tab xếp dọc; bảng Contacts/Files cuộn ngang | AMB-CUST-16 |
| Định dạng ngày | Hiển thị `DD-MM-YYYY HH:mm:ss`; datetimepicker ghi `DD-MM-YYYY HH:mm`; Import yêu cầu `Y-m-d` | REQ-CUST-27, 73, 88 |

## 5. Danh mục Evidence

Ảnh chụp **viewport** 973×853 (thu về 800 px chiều ngang). Ảnh danh sách KH đã **che** cột Primary Contact / Primary Email của dữ liệu người khác (dải xám ghi "da che du lieu nguoi khac"). Mọi ảnh đã được mở lại xác nhận đúng trạng thái.

| Tệp | Màn hình | Trạng thái | REQ làm bằng chứng |
|---|---|---|---|
| [cust_list_export_menu_open_viewport.png](evidence/cust_list_export_menu_open_viewport.png) | Danh sách KH | Menu Export đang mở · thấy Summary + thanh công cụ | REQ-CUST-01, 02, 09, 15 |
| [cust_list_bulk_actions_modal_viewport.png](evidence/cust_list_bulk_actions_modal_viewport.png) | Danh sách KH | Modal Bulk Actions mở, chưa tick Mass Delete | REQ-CUST-17 |
| [cust_list_create_filter_modal_viewport.png](evidence/cust_list_create_filter_modal_viewport.png) | Danh sách KH | Modal Create Filter, chưa thêm rule | REQ-CUST-22 |
| [cust_new_form_default_viewport.png](evidence/cust_new_form_default_viewport.png) | Form tạo KH | Mặc định, tab Customer Details | REQ-CUST-28, 37 |
| [cust_new_form_empty_submit_viewport.png](evidence/cust_new_form_empty_submit_viewport.png) | Form tạo KH | Sau Save khi trống — lỗi Company | REQ-CUST-30 |
| [cust_new_form_duplicate_name_warning_viewport.png](evidence/cust_new_form_duplicate_name_warning_viewport.png) | Form tạo KH | Cảnh báo trùng tên dưới ô Company | REQ-CUST-33 |
| [cust_new_billing_shipping_copied_viewport.png](evidence/cust_new_billing_shipping_copied_viewport.png) | Form tạo KH — Billing & Shipping | Sau Same as Customer Info + Copy Billing Address | REQ-CUST-41, 42 |
| [cust_detail_tabs_menu_viewport.png](evidence/cust_detail_tabs_menu_viewport.png) | Hồ sơ KH test | Ngay sau khi tạo — menu tab | REQ-CUST-39, 45 |
| [cust_contact_new_modal_empty_submit_viewport.png](evidence/cust_contact_new_modal_empty_submit_viewport.png) | Modal Add new contact | Sau Save khi trống — lỗi bắt buộc, Phone `+84` | REQ-CUST-54, 55, 58 |
| [cust_contacts_tab_after_add_viewport.png](evidence/cust_contacts_tab_after_add_viewport.png) | Tab Contacts | Sau khi thêm contact test | REQ-CUST-53, 64 |
| [cust_notes_empty_note_saved_viewport.png](evidence/cust_notes_empty_note_saved_viewport.png) | Tab Notes | Có 1 note mô tả trống đã lưu | REQ-CUST-81, 82 |
| [cust_reminder_modal_datepicker_viewport.png](evidence/cust_reminder_modal_datepicker_viewport.png) | Modal Set Reminder | Lỗi bắt buộc + bộ chọn ngày mở (ngày 1 → 15 mờ) | REQ-CUST-86, 87, 88 |
| [cust_files_after_upload_viewport.png](evidence/cust_files_after_upload_viewport.png) | Tab Files | Sau khi tải lên PDF test · huy hiệu Files/Reminders | REQ-CUST-46, 91, 93 |
| [cust_vault_new_entry_empty_submit_viewport.png](evidence/cust_vault_new_entry_empty_submit_viewport.png) | Modal Vault Entry | Sau Save khi trống — 3 lỗi bắt buộc | REQ-CUST-97, 98 |
| [cust_statement_this_month_viewport.png](evidence/cust_statement_this_month_viewport.png) | Tab Statement | Kỳ This Month, KH chưa có giao dịch | REQ-CUST-100, 102 |
| [cust_import_no_file_submit_viewport.png](evidence/cust_import_no_file_submit_viewport.png) | Trang Import | Sau Simulate khi chưa chọn tệp | REQ-CUST-73, 74 |
| [cust_import_simulation_result_viewport.png](evidence/cust_import_simulation_result_viewport.png) | Trang Import | Kết quả Simulate Import | REQ-CUST-75 |

REQ không có ảnh nhưng `Nguồn` ghi `Kiểm chứng thực tế` đều có số liệu DOM / network chép trong AC (skill 7.2.1).
