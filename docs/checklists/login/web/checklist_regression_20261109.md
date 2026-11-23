## Đăng nhập (`LOGIN`) — Checklist Regression (39 mục · ~45 phút)

**Nguồn:** TC-based — [`TEST_CASES_LOGIN_SUMMARY.md`](../../../testcases/login/TEST_CASES_LOGIN_SUMMARY.md) → [`part_01_web_chuc_nang.md`](../../../testcases/login/web/test_cases_login_web.md) · [`part_02_web_ky_thuat_phi_chuc_nang.md`](../../../testcases/login/web/test_cases_login_web.md)
**Loại:** Regression (module) — agent suy ra (user không chỉ định): module vừa có bộ TC đầy đủ, chưa có hotfix hay mốc release. Lấy mục từ V1 + V2 + V3 `Permission`; bỏ V4 và V3 ngoài `Permission`
**Scope:** Module `LOGIN` · nền tảng Web · trang Login, Forgot Password, menu ảnh đại diện, điều hướng phiên · role Admin (role nhân viên duy nhất hiện có) + Contact khách hàng
**Mã checklist:** `CL-regression_20261109` — mã mục khi chạy = `CL-regression_20261109-<nn>`
**Trạng thái lấy từ:** Chưa có lần chạy nào — chưa có `docs/executions/login/web/`

**Quy ước:** đường dẫn tính từ địa chỉ gốc ở biến `URL` trong `.env` · **tài khoản admin** = `EMAIL_ADMIN` / `PASSWORD_ADMIN` trong `.env` (🔒 không ghi giá trị vào checklist) · mỗi mục chạy trong **cửa sổ ẩn danh mới** trừ khi ghi khác · email sai luôn đuôi `@example.invalid` để không khoá tài khoản dùng chung · chuỗi dài lấy từ [`test_data_login_web.json`](../../../testcases/login/web/test_data_login_web.json).
**Cần chuẩn bị:** `TK-TEST-01` (`qa.login.rieng01@example.test` / `QaLogin@2026`) · `TK-TEST-02a` (`qa.login.2fa.email@example.test` / `Qa2fa@2026`) · `TK-TEST-03` (`qa.reset.01@mailpit.local` + hộp thư test) · Contact `auto_tc042_20261109160000_D9E3@example.test` / `Contact@2026` tạo trong module Customers. Chưa có thì mục tương ứng đánh `⚠️ BLOCKED`.

### Nhóm: Giao diện & mở trang

| # | Trạng thái | Hạng mục kiểm tra | Kết quả kỳ vọng | Priority | REQ ID | TC ID liên quan | Execution ID |
|---|---|---|---|---|---|---|---|
| 1 | ☐ | Mở `/admin/authentication`, không chạm chuột hay bàn phím | Thấy logo, tiêu đề `Login`, ô `Email Address`, ô `Password`, ô tích `Remember me` (chưa tích), nút `Login`, liên kết `Forgot Password?`; con trỏ nhấp nháy sẵn trong ô Email | P1 | REQ-LOGIN-01, REQ-LOGIN-02 | CRM_LOGIN_TC_001 | — |
| 2 | ☐ | Mở `/admin/authentication/forgot_password` | Tiêu đề `Forgot Password`, ô `Email Address` trống không có con trỏ, nút `Confirm`; không có liên kết quay lại Login | P2 | REQ-LOGIN-18 | CRM_LOGIN_TC_002 | — |
| 3 | ☐ | Bấm liên kết `Forgot Password?` trên trang Login | Thanh địa chỉ kết thúc bằng `/admin/authentication/forgot_password`, tiêu đề `Forgot Password` | P2 | REQ-LOGIN-17 | CRM_LOGIN_TC_004 | — |
| 4 | ☐ | Đăng nhập admin, bấm ảnh đại diện góc trên bên phải | Menu đúng 5 mục theo thứ tự: `My Profile` · `My Timesheets` · `Edit Profile` · `Language` · `Logout` | P2 | REQ-LOGIN-25 | CRM_LOGIN_TC_003 | — |

### Nhóm: Đăng nhập & đăng xuất

| # | Trạng thái | Hạng mục kiểm tra | Kết quả kỳ vọng | Priority | REQ ID | TC ID liên quan | Execution ID |
|---|---|---|---|---|---|---|---|
| 5 | ☐ | Đăng nhập tài khoản admin, không tích `Remember me` | Vào Dashboard: địa chỉ kết thúc `/admin/`, tên tab có chữ `Dashboard`, thanh bên trái hiển thị | P1 | REQ-LOGIN-09 | CRM_LOGIN_TC_005 | — |
| 6 | ☐ | Đăng nhập tài khoản admin, có tích `Remember me` | Vào Dashboard `/admin/`, không có khung thông báo đỏ | P1 | REQ-LOGIN-09 | CRM_LOGIN_TC_006 | — |
| 7 | ☐ | Đang ở Dashboard, bấm ảnh đại diện rồi bấm `Logout` | Về ngay `/admin/authentication`, không hộp xác nhận; ô Email trống, con trỏ trong ô Email | P1 | REQ-LOGIN-26 | CRM_LOGIN_TC_007 | — |
| 8 | ☐ | Bấm đúp thật nhanh nút `Login` với tài khoản admin | Vào Dashboard `/admin/`, chỉ một tab; không hiện trang `The action you have requested is not allowed.` | P2 | REQ-LOGIN-09 | CRM_LOGIN_TC_036 | — |
| 9 | ☐ | Ngắt mạng rồi bấm `Login`; bật mạng, nạp lại trang, đăng nhập lại | Lần đầu trình duyệt báo mất kết nối; lần sau vào Dashboard | P3 | REQ-LOGIN-09 | CRM_LOGIN_TC_038 | — |

### Nhóm: Bắt buộc nhập & định dạng (form Login)

| # | Trạng thái | Hạng mục kiểm tra | Kết quả kỳ vọng | Priority | REQ ID | TC ID liên quan | Execution ID |
|---|---|---|---|---|---|---|---|
| 10 | ☐ | Để trống cả Email và Password, bấm `Login` | Hiện đủ 2 khung đỏ `The Password field is required.` và `The Email Address field is required.` (không xét thứ tự) | P1 | REQ-LOGIN-05 | CRM_LOGIN_TC_008 | — |
| 11 | ☐ | Nhập Email `auto_cl11_20261109@example.invalid`, để trống Password, bấm `Login` | Đúng 1 khung đỏ `The Password field is required.`; ô Email bị xoá trống | P1 | REQ-LOGIN-06, REQ-LOGIN-08 | CRM_LOGIN_TC_009, CRM_LOGIN_TC_021 | — |
| 12 | ☐ | Nhập Password 3 dấu cách, Email `auto_cl12_20261109@example.invalid`, bấm `Login` | Đúng 1 khung đỏ `The Password field is required.` | P3 | REQ-LOGIN-06 | CRM_LOGIN_TC_009 | — |
| 13 | ☐ | Để trống Email, nhập Password `Abc@12345`, bấm `Login` | Đúng 1 khung đỏ `The Email Address field is required.` | P2 | REQ-LOGIN-31 | CRM_LOGIN_TC_010 | — |
| 14 | ☐ | Nhập Email `abc`, Password `Abc@12345`, bấm `Login` | Trình duyệt hiện cảnh báo cạnh ô Email; trang không nạp lại, chữ đã nhập còn nguyên | P1 | REQ-LOGIN-03 | CRM_LOGIN_TC_011, CRM_LOGIN_TC_012 | — |
| 15 | ☐ | Gõ `Abc@12345` vào ô Password | Chỉ hiện 9 dấu chấm; không có nút hiện/ẩn mật khẩu | P2 | REQ-LOGIN-04 | CRM_LOGIN_TC_016 | — |
| 16 | ☐ | Bấm ô `Remember me` hai lần liên tiếp | Lần 1 hiện dấu tích, lần 2 dấu tích mất | P3 | REQ-LOGIN-01 | CRM_LOGIN_TC_020 | — |

### Nhóm: Sai thông tin đăng nhập

| # | Trạng thái | Hạng mục kiểm tra | Kết quả kỳ vọng | Priority | REQ ID | TC ID liên quan | Execution ID |
|---|---|---|---|---|---|---|---|
| 17 | ☐ | Đăng nhập Email `auto_cl17_20261109@example.invalid`, Password `Abc@12345` | Đúng 1 khung đỏ `Invalid email or password`; ô Email và Password đều trống | P1 | REQ-LOGIN-07, REQ-LOGIN-08 | CRM_LOGIN_TC_013, CRM_LOGIN_TC_021 | — |
| 18 | ☐ | Dán Email 254 ký tự (bộ `BND_05` trong file test data), Password `Abc@12345`, bấm `Login` | Khung đỏ `Invalid email or password`; không có trang lỗi hay chữ `Database Error` | P3 | REQ-LOGIN-07 | CRM_LOGIN_TC_014 | — |
| 19 | ☐ | Đăng nhập `qa.login.rieng01@example.test` với mật khẩu sai `SaiMatKhau@999` | Khung đỏ `Invalid email or password` — chữ giống hệt mục 17 | P1 | REQ-LOGIN-30 | CRM_LOGIN_TC_018 | — |
| 20 | ☐ | Đăng nhập `qa.login.rieng01@example.test` với `qaLogin@2026` (sai chữ hoa đầu) | Khung đỏ `Invalid email or password`; sau đó mật khẩu đúng `QaLogin@2026` vẫn vào được | P2 | REQ-LOGIN-30 | CRM_LOGIN_TC_018 | — |
| 21 | ☐ | Đăng nhập Email viết hoa `QA.LOGIN.RIENG01@EXAMPLE.TEST`, Password `QaLogin@2026` | Vào Dashboard `/admin/` | P3 | REQ-LOGIN-09 | CRM_LOGIN_TC_015 | — |

### Nhóm: Quên mật khẩu

| # | Trạng thái | Hạng mục kiểm tra | Kết quả kỳ vọng | Priority | REQ ID | TC ID liên quan | Execution ID |
|---|---|---|---|---|---|---|---|
| 22 | ☐ | Để trống Email trang Forgot Password, bấm `Confirm` | Đúng 1 khung đỏ `Email not found` (hiện trạng, nghi lỗi — AMB-LOGIN-05) | P2 | REQ-LOGIN-20 | CRM_LOGIN_TC_022 | — |
| 23 | ☐ | Nhập Email `abc` trang Forgot Password, bấm `Confirm` | Trình duyệt hiện cảnh báo cạnh ô Email; trang không nạp lại | P2 | REQ-LOGIN-19 | CRM_LOGIN_TC_023 | — |
| 24 | ☐ | Nhập `auto_cl24_20261109@example.invalid` trang Forgot Password, bấm `Confirm` | Khung đỏ `Email not found`; ô Email vẫn giữ nguyên chuỗi vừa nhập | P1 | REQ-LOGIN-21, REQ-LOGIN-22 | CRM_LOGIN_TC_024, CRM_LOGIN_TC_025 | — |
| 25 | ☐ | Ngay sau mục 24, bấm `Confirm` thêm một lần không sửa gì | Vẫn đúng 1 khung đỏ `Email not found`, không cộng dồn; không trang lỗi | P3 | REQ-LOGIN-21 | CRM_LOGIN_TC_025, CRM_LOGIN_TC_037 | — |
| 26 | ☐ | Nhập `qa.reset.01@mailpit.local` trang Forgot Password, bấm `Confirm` | Không có khung `Email not found`; hộp thư test nhận thư đặt lại trong 5 phút | P2 | REQ-LOGIN-23 | CRM_LOGIN_TC_026 | — |
| 27 | ☐ | Mở liên kết trong thư, đặt mật khẩu `QaReset@2026New`, đăng nhập bằng mật khẩu mới | Vào Dashboard; mật khẩu cũ `QaReset@2026` báo `Invalid email or password` | P2 | REQ-LOGIN-24 | CRM_LOGIN_TC_027 | — |

### Nhóm: Phiên & điều hướng

| # | Trạng thái | Hạng mục kiểm tra | Kết quả kỳ vọng | Priority | REQ ID | TC ID liên quan | Execution ID |
|---|---|---|---|---|---|---|---|
| 28 | ☐ | Chưa đăng nhập, gõ thẳng `/admin/clients` vào thanh địa chỉ | Dừng ở `/admin/authentication`, form Login hiện, không có khung thông báo | P1 | REQ-LOGIN-11 | CRM_LOGIN_TC_028 | — |
| 29 | ☐ | Bị đưa về Login từ `/admin/clients`, đăng nhập tài khoản admin | Vào `/admin/` (Dashboard), **không** quay lại `/admin/clients` | P2 | REQ-LOGIN-10 | CRM_LOGIN_TC_029 | — |
| 30 | ☐ | Đang đăng nhập, gõ `/admin/authentication` vào thanh địa chỉ | Tự về `/admin/`, không thấy form Login | P2 | REQ-LOGIN-12 | CRM_LOGIN_TC_030 | — |
| 31 | ☐ | Đang đăng nhập, gõ `/admin/authentication/forgot_password` vào thanh địa chỉ | Tự về `/admin/`, không thấy form Forgot Password | P3 | REQ-LOGIN-13 | CRM_LOGIN_TC_031 | — |
| 32 | ☐ | Sau khi Logout, gõ `/admin/` vào thanh địa chỉ | Dừng ở `/admin/authentication`, phải nhập lại email và mật khẩu | P1 | REQ-LOGIN-27 | CRM_LOGIN_TC_032 | — |
| 33 | ☐ | Mở 2 tab đã đăng nhập; Logout ở tab A, bấm `Projects` ở tab B | Tab B về trang Login, không mở được Projects | P2 | REQ-LOGIN-27 | CRM_LOGIN_TC_033 | — |
| 34 | ☐ | Đăng nhập có tích `Remember me`, Logout, gõ `/admin/` (profile Chrome riêng, không ẩn danh) | Vẫn ở trang Login — không tự đăng nhập lại | P1 | REQ-LOGIN-28 | CRM_LOGIN_TC_045 | — |
| 35 | ☐ | Đăng nhập có tích `Remember me`, xoá cookie `sp_session` trong DevTools, mở `/admin/` | Vào thẳng Dashboard, không phải nhập lại mật khẩu | P2 | REQ-LOGIN-16 | CRM_LOGIN_TC_040 | — |
| 36 | ☐ | Đăng nhập **không** tích `Remember me`, xoá cookie `sp_session` trong DevTools, mở `/admin/` | Dừng ở trang Login, phải nhập lại | P2 | REQ-LOGIN-33 | CRM_LOGIN_TC_041 | — |
| 37 | ☐ | Bật bộ đếm giờ ở task `QA-LOGIN-TC034-TIMER`, bấm ảnh đại diện → `Logout` | Hiện cảnh báo bộ đếm giờ đang chạy; vẫn ở Dashboard (dừng timer sau khi rà) | P3 | REQ-LOGIN-34 | CRM_LOGIN_TC_034 | — |
| 38 | ☐ | Đăng nhập `qa.login.2fa.email@example.test` / `Qa2fa@2026` (tài khoản bật 2FA) | Hiện bước nhập mã xác thực; chưa vào Dashboard | P2 | REQ-LOGIN-32 | CRM_LOGIN_TC_035 | — |

### Nhóm: Phân quyền

| # | Trạng thái | Hạng mục kiểm tra | Kết quả kỳ vọng | Priority | REQ ID | TC ID liên quan | Execution ID |
|---|---|---|---|---|---|---|---|
| 39 | ☐ | Đăng nhập khu admin bằng Contact `auto_tc042_20261109160000_D9E3@example.test` / `Contact@2026` | Khung đỏ `Invalid email or password`; không vào Dashboard | P1 | REQ-LOGIN-29 | CRM_LOGIN_TC_042 | — |

### Không áp dụng cho module này

- **Data Table / List** — module không có bảng dữ liệu, lọc, tìm kiếm, phân trang
- **CRUD Lifecycle** — module không tạo/sửa/xoá bản ghi nghiệp vụ nào
- **Status Flow của entity** — không có entity mang trạng thái; luồng **phiên** đăng nhập đã nằm ở nhóm *Phiên & điều hướng*
- **Notification / Toast** — module không dùng toast; thông báo là khung đỏ cố định trên form, đã có ở mục 10–14, 17–25
- **Permission theo role nhân viên** — hệ thống hiện chỉ có 1 role nhân viên (AMB-LOGIN-01/02 ✅ 05-11-2026); phân quyền chỉ còn trục Admin ↔ Contact (mục 39)

### Đã cắt khỏi checklist (vẫn có trong bộ TC chi tiết)

- **V4** — bàn phím, responsive, đa trình duyệt: TC_050–054
- **V3 ngoài Permission** — CSRF, thuộc tính cookie, SQLi/XSS, nút Back sau đăng xuất: TC_043, 044, 046–049
- **Biến thể validation còn lại** — giữ 1–2 mục đại diện mỗi field: TC_011-b..d, 012, 013-b..f, 017, 023-b..f, 024-b..e
- **Mục trùng nội dung** — dán từ bộ nhớ tạm TC_019, kịch bản trọn vòng TC_039 (các bước đã có ở mục 5, 7, 17, 22–24, 32), đóng menu avatar TC_055

### Ký nhận

| Môi trường | Build / Version | Người thực hiện | Ngày | Kết quả (Pass/Fail/Blocked) |
|---|---|---|---|---|
|  |  |  |  |  |
