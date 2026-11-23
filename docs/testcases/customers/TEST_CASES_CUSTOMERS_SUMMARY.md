# Test Cases — Khách hàng `CUST` (tổng 66 TC · 1 nền tảng)

> **INDEX — tên file bất biến, không chứa dòng TC.** TC chi tiết ở file nền tảng (xem **Bản đồ tài liệu**).
> ← [Danh mục test case](../README.md) · Requirements: [`REQUIREMENTS_CUSTOMERS_SUMMARY.md`](../../requirements/customers/REQUIREMENTS_CUSTOMERS_SUMMARY.md)

| Thông tin | Nội dung |
|---|---|
| **Nguồn requirement** | [REQUIREMENTS_CUSTOMERS_SUMMARY.md](../../requirements/customers/REQUIREMENTS_CUSTOMERS_SUMMARY.md) · [story_02_tao_sua_khach_hang.md](../../requirements/customers/web/stories/story_02_tao_sua_khach_hang.md) |
| **Phạm vi REQ** | **STORY-CUST-02** — `REQ-CUST-28` → `REQ-CUST-52` (25 REQ, 25/25 có TC). Story 01, 03 → 07 (`REQ-CUST-01` → 27, 53 → 115) **chưa sinh TC** — lượt sau chạy `/generate-testcases-manual-rbt` ở chế độ BỔ SUNG, TC ID nối tiếp từ `CRM_CUST_TC_067` |
| **Dải TC ID đã dùng** | `CRM_CUST_TC_001` → `CRM_CUST_TC_066` — chung mọi nền tảng · TC kế tiếp `CRM_CUST_TC_067` |
| **Mode · độ hạt** | FULL RBT (6 bước, checkpoint Bước 2 + Bước 4 đã duyệt 16-11-2026) · **GỘP** — 66 TC · **81 biến thể dữ liệu** + **16 mục bảng kiểm** |
| **Mức rủi ro · độ sâu** | `Cao` → **Đầy đủ** — V1 đủ 6 nhánh, V2 mọi nhánh có điều kiện kích hoạt, V3 Permission + Security + Database (D1 · D2 · D3 · D4 · D5 · D8), V4 Responsive + Accessibility.<br>Căn cứ chấm Cao: dữ liệu cá nhân khách hàng · KH là cổng vào của ≥ 12 module khác · có xoá không hoàn tác · có phân công người phụ trách (phân quyền).<br>**Hạ xuống Tiêu chuẩn khi:** module chỉ còn một vai trò vĩnh viễn **và** KH không còn là khoá của module khác — thực tế coi như không xảy ra |
| **Môi trường** | 🔒 Dùng chung — TC chỉ tạo / sửa / xoá KH test `auto_cust_…` (user cho phép 16-11-2026). KH 16007, 16008 giữ lại từ lượt recon, TC **không** phụ thuộc vào chúng |
| **Ngày sinh** | 16-11-2026 |

## Bản đồ tài liệu

| Nền tảng | File | Nhóm chức năng | Số TC | TC ID | REQ bao phủ |
|---|---|---|---|---|---|
| Web | [web/test_cases_customers_web.md](web/test_cases_customers_web.md) | Vòng 1 Smoke · Vòng 2a Required/Validation ô chữ · Vòng 2b Dropdown/địa chỉ/hành vi/menu · Vòng 2c Customer Admins/xoá/đoán lỗi · Vòng 3a Permission/Security · Vòng 3b Database · Vòng 4 Responsive/Accessibility | 66 | 001–066 | REQ-CUST-28 → 52 |

## Assumptions

User chấp nhận toàn bộ giả định Q1 → Q10 ở Bước 2 (16-11-2026). TC dựa vào giả định ghi `assumption-based` trong Expected.

| Mã | Giả định | Nguồn | TC dựa vào |
|---|---|---|---|
| ASM-01 | Company chỉ gồm khoảng trắng **phải** bị chặn như ô trống — TC viết theo hành vi đúng, hiện đang FAIL | Q1 · AMB-CUST-01 | TC_011 |
| ASM-02 | Kiểm biên độ dài 1 / 191 / 255 (lưu đủ) và > 255 (xử lý êm, không cắt âm thầm) | Q2 · AMB-CUST-02 | TC_012, 013 |
| ASM-03 | VAT, Phone, Website, Zip Code **không** kiểm định dạng — mọi chuỗi lưu nguyên văn | Q3 · AMB-CUST-21 (mới) | TC_021, 022, 023, 027 |
| ASM-04 | VAT không bắt buộc duy nhất | Q4 · AMB-CUST-22 (mới) | TC_021-d |
| ASM-05 | Xoá KH không giao dịch: xoá được, KH + contact không còn, mở lại địa chỉ cũ không thấy dữ liệu | Q5 · AMB-CUST-09 | TC_047, 050, 064 |
| ASM-06 | Xoá KH đang có hoá đơn / dự án — **⏭️ cố ý bỏ** ở Story 02, chuyển sang bộ TC `INV` | Q6 | — |
| ASM-07 | Nhân viên role khác (`Project Manager`) chỉ **xem** KH mình được gán làm Customer Admin; **không** tạo / sửa / xoá KH. Tài khoản dự kiến `EMAIL_PM_1` / `PASSWORD_PM_1` trong `.env` — chưa có → BLOCKED | Q7 · AMB-CUST-08 · AMB-LOGIN-24 | TC_055 → 059 |
| ASM-08 | Hai tab cùng sửa: bản lưu sau ghi đè, không báo xung đột | Q8 · AMB-CUST-23 (mới) | TC_049 |
| ASM-09 | Đổi Currency sau khi có giao dịch — **⏭️ cố ý bỏ**, chuyển E2E với `INV` | Q9 | — |
| ASM-10 | Chạy ở `1600×750`; TC không kiểm bố cục theo vị trí, riêng TC_065 kiểm 2 mốc kích thước | Q10 · AMB-CUST-16 | TC_065 |
| ASM-11 | Company có khoảng trắng đầu/cuối được cắt bỏ khi lưu | Suy luận khi sinh — chưa quan sát | TC_016 |
| ASM-12 | Cảnh báo trùng tên bắt được cả khác hoa thường / thừa khoảng trắng | Suy luận khi sinh — chưa quan sát | TC_019 |
| ASM-13 | "Save and create contact" mở ngay hộp thoại tạo contact của KH vừa lưu | AMB-CUST-12 | TC_045 |

## Kỹ thuật thiết kế đã áp dụng

| Kỹ thuật | Áp dụng | TC |
|---|---|---|
| Phân lớp tương đương (EP) | Mỗi ô chữ: lớp hợp lệ thường · ký tự đặc biệt · script/SQL · Unicode/emoji · định dạng lạ | TC_014, 015, 021 → 027 |
| Giá trị biên (BVA) | Company: 0 (trống) · 1 · 191 · 255 · 256 · 1000 ký tự (không có mốc thật — ASM-02) | TC_009, 012, 013 |
| Bảng quyết định | ➖ Không có chỗ nào ≥ 3 điều kiện cùng quyết định một kết quả | — |
| Chuyển trạng thái | ➖ Story 02 không có luồng trạng thái (cờ Active thuộc Story 01) | — |
| Đoán lỗi | Bấm Save 2 lần · F5 / Back sau lưu · 2 tab cùng sửa · rời form giữa chừng · phiên đổi ở tab khác | TC_048, 049, 054, 061, 062 |

### Đối soát Field-Level (bảng 15 loại)

| Ô | Loại | Mục của bảng đã phủ | Mục không áp dụng / lý do |
|---|---|---|---|
| Company | Text | Required (009, 010) · Min/Max (012, 013) · Whitespace-only (011) · Ký tự đặc biệt (014-a) · XSS (014-b, d · 052) · SQLi (014-c) · Unicode/Emoji (015) · Leading/trailing spaces (016) — **8/8** | — |
| VAT Number | Text | Ký tự đặc biệt + HTML (021-b) · Max (021-c) · trùng giá trị (021-d) · hợp lệ (021-a) — 4/8 | Required ➖ không bắt buộc · Whitespace-only, XSS, SQLi, Unicode ⏭️ — cùng cơ chế lưu với Company đã kiểm đủ; rà lại khi VAT có ràng buộc riêng (AMB-CUST-21). Quyết định: QA, 16-11-2026 |
| Phone | Phone | Chỉ số (022-a) · Prefix `+84` (022-b) · Dấu `-` `.` khoảng trắng (022-b, c) · Chữ xen lẫn (022-d) · Max length (022-e) — **5/6** | Mã vùng không hợp lệ ➖ — hệ thống không kiểm định dạng Phone (ASM-03), không có khái niệm mã vùng |
| Website | Text (URL) | Có / không giao thức (023-a, b) · chuỗi không phải URL (023-c) · `javascript:` (023-d) | Required ➖ · Max length ⏭️ cùng cơ chế với Company. Quyết định: QA, 16-11-2026 |
| Address | Textarea | Max length (024-c) · Line breaks (024-a) · HTML tags (024-b) — **3/5** | Resize ➖ — hành vi chuẩn của trình duyệt · Character counter ➖ — form không có bộ đếm |
| City · State | Text | Unicode (025-a · 026-a) · Ký tự đặc biệt (025-b · 026-b) · Max (025-c · 026-c) | Required ➖ · XSS/SQLi ⏭️ — kiểm ở Billing (035) và Company. Quyết định: QA, 16-11-2026 |
| Zip Code | Text | Số (027-a) · Chữ (027-b) · Dài (027-c) | Required ➖ |
| Country | Dropdown | Mặc định (001-`6`, 028) · danh sách + tìm (028) · đổi lựa chọn + lưu (028) — **4/5** | Option disabled ➖ — không có option bị khoá · Required ➖ — không bắt buộc |
| Currency | Dropdown | Mặc định (001-`5`, 029) · options (029) · đổi + lưu (029) | Option disabled ➖ · Required ➖ |
| Default Language | Dropdown | Mặc định (030) · tất cả options — đếm 26 (030) · đổi + lưu (030) | Option disabled ➖ · Required ➖ |
| Groups | Multi-Select | Chọn nhiều · bỏ chọn (031) · thêm mục mới qua nút `+` (032) — **3/4** | Giới hạn số lượng ➖ — không có giới hạn · Tag trùng ⏭️ — tên nhóm trùng là dữ liệu master ở Setup (AMB-CUST-19, BLOCKED) |
| Show primary contact… | Checkbox | Mặc định (036) · hiện/ẩn theo điều kiện (036) · tích + lưu (036) | Required ➖ · nhóm radio ➖ |
| Billing / Shipping (10 ô) | Text · Textarea · Dropdown | Độ bền gộp 6 ô (035) · chép tự động (033, 034) | Từng mục riêng ⏭️ — cùng loại và cùng cơ chế lưu với ô Customer Details đã kiểm đủ. Quyết định: QA, 16-11-2026. Rà lại khi Billing/Shipping có validation riêng |
| Customer Admins | Multi-Select (hộp thoại) | Chọn 1 / nhiều (042) · gỡ (043) · đóng không lưu (044) | Giới hạn số lượng ➖ |

### Đối soát Component-Level

| Component | Trạng thái | TC |
|---|---|---|
| Giao diện tĩnh của màn hình | ✅ | TC_001, 002, 003 |
| Data Table / List | ➖ ở Story 02 — chỉ dùng danh sách để đối chiếu (TC_007). Bảng KH đầy đủ thuộc Story 01 | — |
| CRUD Lifecycle | ✅ | Tạo 005/006 · xem 006/007 · sửa 008/063 · xoá 046/047/064 · trùng tên 020 · 2 tab 049 |
| Permission / Role | ✅ (BLOCKED khi chạy) | TC_055 → 059 |
| Modal / Dialog | ✅ | Assign Admin 042, 044 · tạo nhóm 032 · hộp xác nhận xoá 046 |
| Notification / Toast | ✅ | "Customer added successfully." (005) · "Customer updated successfully." (008, 042) · thông báo xoá (047) · "Page expired…" (054) |
| Status Flow | ➖ Story 02 không có luồng trạng thái | — |
| Báo cáo / Dashboard | ➖ Không có | — |

## Bảng Đối Soát Coverage (toàn module)

Chỉ tính REQ trong phạm vi (Story 02). Mọi TC ở nền tảng Web.

| REQ ID | Mô tả ngắn | Số TC | TC IDs | Đủ Positive/Negative/Boundary? | Ghi chú |
|---|---|---|---|---|---|
| REQ-CUST-28 | Form tạo 2 tab | 8 | 001, 002, 004, 038, 051, 056, 065, 066 | ✅ P + N (051, 056) | — |
| REQ-CUST-29 | Company focus sẵn | 2 | 001, 066 | ✅ P | Quan sát tĩnh — không có Negative |
| REQ-CUST-30 | Company trống khi tạo | 2 | 009, 037 | ✅ N | — |
| REQ-CUST-31 | Company toàn khoảng trắng | 1 | 011 | ✅ N | TC thiết kế để FAIL (ASM-01) |
| REQ-CUST-32 | Không giới hạn độ dài | 5 | 012, 013, 014, 021, 022 | ✅ P + N + B | — |
| REQ-CUST-33 | Cảnh báo trùng tên | 3 | 017, 018, 019 | ✅ P + N | — |
| REQ-CUST-34 | Trùng tên vẫn lưu | 1 | 020 | ✅ P | REQ ⚪ — `@NeedsVerify` |
| REQ-CUST-35 | Currency | 2 | 001, 029 | ✅ P | — |
| REQ-CUST-36 | Default Language | 2 | 001, 030 | ✅ P | — |
| REQ-CUST-37 | Groups + nút `+` | 3 | 001, 031, 032 | ✅ P | — |
| REQ-CUST-38 | Country | 2 | 001, 028 | ✅ P | — |
| REQ-CUST-39 | Lưu mới → hồ sơ + thông báo | 9 | 005, 006, 007, 048, 050, 054, 060, 061, 062 | ✅ P + N (054, 062) | — |
| REQ-CUST-40 | Lưu nguyên văn | 16 | 006, 007, 012, 014, 015, 016, 021–027, 035, 052, 060 | ✅ P + N + B | — |
| REQ-CUST-41 | Same as Customer Info | 2 | 033, 035 | ✅ P | — |
| REQ-CUST-42 | Copy Billing Address | 2 | 034, 035 | ✅ P | — |
| REQ-CUST-43 | Tooltip Shipping | 1 | 002 | ✅ P | Chỉ TC_002 kiểm riêng REQ này — TC_002 còn REQ-28 có TC khác chống lưng (6b đạt) |
| REQ-CUST-44 | Save and create contact | 1 | 045 | ✅ P | REQ ⚪ — `@NeedsVerify` |
| REQ-CUST-45 | Menu 19 tab | 6 | 003, 039, 040, 051, 053, 065 | ✅ P + N (051, 053) | — |
| REQ-CUST-46 | Huy hiệu số đếm | 1 | 041 | ✅ P + N (tab không dữ liệu) | — |
| REQ-CUST-47 | Menu Delete ở tiêu đề | 2 | 003, 046 | ✅ P | — |
| REQ-CUST-48 | Company trống khi sửa | 1 | 010 | ✅ N | — |
| REQ-CUST-49 | Sửa và lưu | 5 | 008, 049, 050, 057, 063 | ✅ P + N (057) | — |
| REQ-CUST-50 | Customer Admins | 7 | 003, 042, 043, 044, 050, 055, 059 | ✅ P + N (044, 055) | — |
| REQ-CUST-51 | Show primary contact | 1 | 036 | ✅ P + N (ẩn khi chưa có contact) | — |
| REQ-CUST-52 | Xoá KH | 5 | 046, 047, 050, 058, 064 | ✅ P + N (046, 058) | REQ ⚪ — xoá thật `@NeedsVerify` |

**25/25 REQ có TC · 0 🔴.** Phép thử chiều ngược (6b): TC gánh ≥ 2 REQ đều có TC khác chống lưng, trừ TC_002 có đúng 1 REQ riêng (REQ-CUST-43) — được giữ.

## Bảng Đối Soát Evidence

Đã mở **17/17** ảnh ở `docs/requirements/customers/web/evidence/` (16-11-2026).

| Ảnh evidence | Màn hình / trạng thái | TC dựa vào | Đầy đủ? |
|---|---|---|---|
| cust_new_form_default_viewport.png | Form tạo — mặc định | 001, 004, 028–031 | 🟨 Cắt tại ô `Address` — thiếu City/State/Zip/Country và 2 nút lưu; phần đó dựa vào DOM đã chép ở REQ-CUST-28, 38 |
| cust_new_form_empty_submit_viewport.png | Form tạo — lỗi Company trống | 009, 010 | ✅ |
| cust_new_form_duplicate_name_warning_viewport.png | Form tạo — cảnh báo trùng tên | 017, 020 | ✅ |
| cust_new_billing_shipping_copied_viewport.png | Billing & Shipping sau khi chép | 002, 033, 034 | 🟨 Cắt mất tiêu đề `Billing Address` + liên kết `Same as Customer Info`; dựa vào DOM ở REQ-CUST-41 |
| cust_detail_tabs_menu_viewport.png | Hồ sơ — menu tab | 003, 039, 040 | ✅ (18/19 mục trong ảnh, `Map` có trong DOM) |
| cust_files_after_upload_viewport.png | Tab Files — huy hiệu | 041 | ✅ |
| cust_contact_new_modal_empty_submit_viewport.png | Hộp thoại Add new contact | 036, 045 | ✅ |
| cust_contacts_tab_after_add_viewport.png | Tab Contacts | 036 | ✅ |
| cust_statement_this_month_viewport.png | Tab Statement | 052 | ✅ |
| cust_list_export_menu_open_viewport.png · cust_list_bulk_actions_modal_viewport.png · cust_list_create_filter_modal_viewport.png | Danh sách KH | 007, 046-b | ✅ (đã che dữ liệu người khác) |
| cust_notes_empty_note_saved_viewport.png · cust_reminder_modal_datepicker_viewport.png · cust_vault_new_entry_empty_submit_viewport.png · cust_import_no_file_submit_viewport.png · cust_import_simulation_result_viewport.png | Story 03 → 06 | 040-a, 041 (gián tiếp) | ✅ — chưa dùng trực tiếp ở Story 02 |
| (không có) | Hồ sơ — tab con Customer Admins + hộp thoại Assign Admin | 042, 043, 044 | 🔴 THIẾU ảnh — nhãn lấy từ DOM (REQ-CUST-50); cột `Options` chưa quan sát → TC_043 `@NeedsVerify` |
| (không có) | Menu nhỏ cạnh tiêu đề (`Delete`) · hộp xác nhận xoá KH | 003, 046, 047 | 🔴 THIẾU ảnh — dựa vào DOM (REQ-CUST-47); thông báo sau xoá chưa quan sát → `@NeedsVerify` |
| (không có) | Hộp thoại tạo nhóm (`+` cạnh Groups) | 032 | 🔴 THIẾU — `@NeedsVerify` |

### Vùng chưa có evidence — đề xuất recon bổ sung

1. Tab con `Customer Admins` + hộp thoại `Assign Admin` + cột `Options` (TC_042–044)
2. Hộp thoại tạo nhóm `#customer_group_modal` (TC_032)
3. Luồng xoá KH thật trên KH test + thông báo + địa chỉ cũ (TC_047, 050, 064) — cần cho phép thao tác xoá ở phiên recon
4. Phần dưới form tạo (City → nút lưu) chụp full-page (TC_001, 066)
5. Nhãn hiển thị của danh sách `Default Language` (TC_030)
6. Kích thước `1600×750` cho toàn bộ ảnh (AMB-CUST-16)

## Đối soát loại kiểm thử (4 vòng)

| Vòng | Nhánh | Trạng thái | TC ID / Lý do |
|---|---|---|---|
| 1 | UI cơ bản | ✅ | TC_001–003 (3 TC · 16 mục bảng kiểm) |
| 1 | Open form | ✅ | TC_004 (1 TC · 3 biến thể) |
| 1 | Display | ✅ | TC_006, 007 (định dạng `Date Created`, giữ nguyên văn) |
| 1 | Input valid data | ✅ | TC_005 (tối thiểu) · TC_006 (đầy đủ) |
| 1 | Save | ✅ | TC_005, 006, 008 |
| 1 | Verify data | ✅ | TC_006 (hồ sơ) · TC_007 (danh sách) |
| 2 | UI Behavior | ✅ | TC_033, 034, 036, 037, 038 |
| 2 | Required | ✅ | TC_009, 010 (2 TC · 3 biến thể) |
| 2 | Validation | ✅ | TC_011–016, 021–032, 035 (19 TC · 54 biến thể · Company đủ 8/8 mục bảng Text · Phone 5/6 · Address 3/5 · Dropdown 4/5 — chi tiết ở *Đối soát Field-Level*) |
| 2 | Equivalence Partitioning | ✅ | Nằm trong TC Validation (014, 015, 021–027) |
| 2 | Boundary Value Analysis | ✅ | TC_012, 013 (2 TC · 5 biến thể) |
| 2 | Business Rule | ✅ | Trùng tên: TC_017–020 (4 TC · 2 biến thể) |
| 2 | Decision Table | ➖ | Không có chỗ nào ≥ 3 điều kiện cùng quyết định một kết quả |
| 2 | State Transition | ➖ | Story 02 không có luồng trạng thái |
| 2 | Dependency | ✅ | TC_036 (ô tích phụ thuộc có contact) · TC_041 (huy hiệu theo dữ liệu tab) · TC_039, 040 (tab → nội dung, 2 TC · 12 biến thể) |
| 2 | Use Case / Scenario | ✅ | TC_050 (tạo → sửa → gán admin → xoá) |
| 2 | Save / Edit / Delete | ✅ | TC_042–047 (6 TC · 8 biến thể) |
| 2 | Error Guessing | ✅ | TC_048, 049 · TC_061 (Save 2 lần — gộp với kiểm CSDL), 062 |
| 3 | Permission | ✅ | TC_055–059 (5 TC — BLOCKED tới khi có tài khoản role khác, AMB-CUST-08) |
| 3 | Security | ✅ | TC_014, 023, 035, 051–054 (7 TC · 17 biến thể — XSS/SQLi lưu & hiển thị, chưa đăng nhập, mã số sai, phiên đổi). Quét lỗ hổng / pentest: ⏭️ ngoài khả năng QA chức năng — đội Security, quyết định QA 16-11-2026 |
| 3 | API | ➖ | QA không có quyền gọi API (`docs/requirements/README.md`) |
| 3 | Database · D1 Lưu đúng | ✅ | TC_060 (`@DBCheck`) |
| 3 | Database · D2 Giá trị hệ thống sinh | ✅ | TC_060 (`active`, `datecreated`, `addedfrom`) |
| 3 | Database · D3 Toàn vẹn | ✅ | TC_061 (Save 2 lần → 1 bản ghi) · TC_062 (rời form → 0 bản ghi) |
| 3 | Database · D4 Xoá | ✅ | TC_064 (`@NeedsVerify` — kiểu xoá chưa rõ) |
| 3 | Database · D5 Bảo mật dữ liệu | ✅ | TC_052 (chuỗi script lưu nguyên văn) |
| 3 | Database · D6 Trạng thái ẩn | ➖ | Story 02 không có trạng thái ẩn |
| 3 | Database · D7 Nhật ký | ➖ | Requirements không có yêu cầu audit; tài khoản bị chặn xem nhật ký hoạt động |
| 3 | Database · D8 Sửa trước/sau | ✅ | TC_063 |
| 3 | Database · D9 Tìm kiếm | ➖ | Tìm kiếm danh sách thuộc Story 01 |
| 3 | Database · D10 Báo cáo | ➖ | Story 02 không có báo cáo / dashboard |
| 3 | Integration | ➖ | Story 02 không có tích hợp bên thứ ba |
| 3 | Logging / Audit | ➖ | Requirements không có yêu cầu audit |
| 4 | Compatibility | ⏭️ Cố ý bỏ | Chỉ kiểm Chrome. **Quyết định: QA, 16-11-2026.** Rà lại khi dự án cam kết hỗ trợ trình duyệt khác |
| 4 | Responsive | ✅ | TC_065 (1 TC · 2 biến thể: 1600×750, 973×853) |
| 4 | Accessibility | ✅ | TC_066 (thứ tự Tab, viền focus, Enter). WCAG đầy đủ ➖ — cần công cụ riêng |
| 4 | Performance | ➖ | Không có công cụ đo tải — đội hạ tầng |
| 4 | Regression | ➖ | Module chưa có bug nào được đóng |
| 4 | E2E | ⏭️ Cố ý bỏ | Đổi Currency sau giao dịch (ASM-09) · xoá KH có hoá đơn (ASM-06) chuyển sang bộ TC `INV`. **Quyết định: QA (phạm vi user chốt 16-11-2026).** Rà lại khi sinh TC module `INV` |

## Rà soát đặc tính chất lượng (ISO/IEC 25010:2023)

| Đặc tính | Trạng thái | TC ID / Lý do |
|---|---|---|
| Functional Suitability | ✅ Có TC | TC_001–050, 060–064 |
| Performance Efficiency | ➖ Ngoài phạm vi | Không có công cụ đo tải — đội hạ tầng |
| Compatibility | ➖ Ngoài phạm vi | Chỉ Chrome (⏭️ Compatibility ở bảng 4 vòng) — QA lead quyết khi có cam kết đa trình duyệt |
| Interaction Capability | ✅ Có TC | TC_009, 017 (thông báo lỗi / cảnh báo dễ hiểu) · TC_046 (xác nhận trước khi xoá) · TC_066 (bàn phím) · TC_037 (lỗi ở tab ẩn) |
| Reliability | ✅ Có TC | TC_048 (F5 / Back) · TC_054 (phiên đổi giữa chừng) · TC_061 (Save 2 lần) · TC_062 (rời form) |
| Security | ✅ Có TC | TC_014, 051–059 (XSS/SQLi, chưa đăng nhập, mã số sai, CSRF, phân quyền). Pentest / quét lỗ hổng: đội Security |
| Maintainability | ➖ Không áp dụng | Đặc tính của mã nguồn — code review của đội Dev |
| Flexibility | ✅ Có TC | TC_065 (2 kích thước màn hình) · TC_015 (đa ngôn ngữ dữ liệu) · TC_030 (ngôn ngữ mặc định của KH) |
| Safety | ✅ Có TC | TC_046 (cảnh báo xác nhận trước thao tác xoá không hoàn tác) |

## Đối soát cột Automation

| Nền tảng | Yes | Partial | No | ⏸️ Hoãn |
|---|---|---|---|---|
| Web | 59 | 7 | 0 | 32 (mọi TC `@NeedsVerify` — trong đó 5 TC phân quyền chờ tài khoản role khác) |

### Điều kiện cần chuẩn bị

| # | Điều kiện | Ai cấp | Trạng thái | TC phụ thuộc |
|---|---|---|---|---|
| 1 | Kết nối CSDL chỉ-đọc (`DB_*` trong `.env`) + khảo sát schema | User / DBA (AMB-SYS-05) | ⏳ Chưa có | TC_052, 060, 061, 062, 063, 064 |
| 2 | Tài khoản nhân viên role khác `EMAIL_PM_1` / `PASSWORD_PM_1` | Quản trị hệ thống (AMB-CUST-08) | ⏳ Chưa có | TC_055–059 |
| 3 | Được phép xoá KH test trong phiên chạy | User — đã cho phép 16-11-2026 | ✅ Đã có | TC_046, 047, 050, 064 |

### TC Partial · No · Hoãn

| TC ID | Nền tảng | Automation | Trục chặn | Điều kiện · phần kiểm tay · lý do |
|---|---|---|---|---|
| CRM_CUST_TC_052 | Web | Partial | 3B · Database | Điều kiện #1 · phần UI chạy được ngay |
| CRM_CUST_TC_060 → 064 | Web | Partial | 3B · Database | Điều kiện #1 · phần UI chạy được ngay |
| CRM_CUST_TC_065 | Web | Partial | 3B · Responsive | Phần tử thấy/bấm được: máy chấm · "chữ không đè lên nhau": kiểm tay |
| CRM_CUST_TC_055 → 059 | Web | Yes · ⏸️ Hoãn | — | Chờ điều kiện #2 + chốt ASM-07 |
| CRM_CUST_TC_011 | Web | Yes · ⏸️ Hoãn | — | Chờ chốt AMB-CUST-01 (đang FAIL theo kỳ vọng đúng — vẫn nên automate khi chốt là lỗi) |
| CRM_CUST_TC_012, 013, 016, 019 → 023, 027, 030, 032, 037, 043, 045, 047, 049, 050, 053, 054, 066 | Web | Yes · ⏸️ Hoãn | — | `@NeedsVerify` — chờ recon bổ sung hoặc chốt AMB tương ứng |

**Thứ tự ưu tiên automate:** `@Smoke` / `@CriticalPath` (TC_001–008, 050, 051) → Validation nhiều biến thể (TC_009, 014, 015, 024–026) → phần còn lại.

## Self-Quality Gate (11 tiêu chí)

| # | Tiêu chí | Kết quả |
|---|---|---|
| 0 | Độ hạt nhất quán | ✅ GỘP toàn bộ · mọi biến thể có mã · tối đa 6 biến thể/TC (TC_035, 039, 040) · gộp khác ô chỉ ở TC_035 theo ngoại lệ độ bền |
| 1 | Unique TC ID | ✅ 66 mã, không trùng, `CRM_CUST_TC_001` → `066` |
| 2 | 1-to-1 Step–Expected | ✅ Steps đánh số, Expected đánh số theo bước có kết quả quan sát được |
| 3 | Concrete Test Data | ✅ Mọi giá trị cụ thể; phần động duy nhất là `<ts>` theo quy ước truy vết (CLAUDE.md mục 7) |
| 4 | Field Validation Coverage | ✅ Đối soát theo bảng — mục bỏ qua có lý do (*Đối soát Field-Level*) |
| 5 | Automation Metadata Ready | ✅ 66/66 có `Automation` · `Auto Type` · `Tags`; ngoại lệ ở *Đối soát cột Automation* |
| 6 | Requirement Coverage | ✅ 25/25 REQ · 6b đạt |
| 7 | Evidence-verified | 🟨 17/17 ảnh đã mở · 3 vùng 🔴 thiếu ảnh → TC liên quan `@NeedsVerify` + đề xuất recon bổ sung |
| 8 | Ngôn ngữ kiểm chứng | ✅ Không còn thuật ngữ DOM ở phần TC chính; kỹ thuật duy nhất ở TC_054 dưới `🔧` (`@TechCheck`); SQL chỉ trong khối `🗄️` của 6 TC `@DBCheck`, đều `SELECT` loại A có `WHERE` theo dữ liệu test + `LIMIT`, không `SELECT *` |
| 9 | ISO/IEC 25010 | ✅ 9/9 đặc tính đã chấm, ô `➖` có người chịu trách nhiệm |
| 10 | Đối soát 4 vòng | ✅ Mọi nhánh đã chấm · `UI cơ bản`, `Validation`, `Permission` đều ✅ · GỘP có số biến thể |

## Điểm cần user review

1. **TC_011 sẽ FAIL** cho tới khi dev chặn Company toàn khoảng trắng (AMB-CUST-01) — cần PO xác nhận là lỗi để ghi bug
2. **5 TC phân quyền BLOCKED** — cần tài khoản nhân viên role khác (AMB-CUST-08, chung nhu cầu với AMB-LOGIN-24)
3. **6 TC `@DBCheck`** chỉ chạy được phần UI cho tới khi có kết nối CSDL (AMB-SYS-05)
4. 32 TC `@NeedsVerify` — 3 vùng thiếu evidence (Customer Admins, xoá KH, hộp thoại tạo nhóm) nên recon bổ sung trước lần chạy đầu

## Nhật ký thay đổi

| Ngày | Nguồn | TC ảnh hưởng | Loại | Tóm tắt | Mốc git |
|---|---|---|---|---|---|
| 16-11-2026 | `/generate-testcases-manual-rbt module CUST story_02` (FULL RBT) | CRM_CUST_TC_001 → 066 | 🟢 Thêm | Khởi tạo bộ TC module `CUST` cho STORY-CUST-02 (25 REQ) — độ hạt GỘP, rủi ro Cao → Đầy đủ. User chấp nhận giả định Q1 → Q10 | `cb8ea3a` (trước khi tạo — file mới) |
