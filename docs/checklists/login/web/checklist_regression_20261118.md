## Đăng nhập (`LOGIN`) — Checklist Regression (39 mục · ~45 phút)

**Nguồn:** TC-based — [`TEST_CASES_LOGIN_SUMMARY.md`](../../../testcases/login/TEST_CASES_LOGIN_SUMMARY.md) → [`web/test_cases_login_web.md`](../../../testcases/login/web/test_cases_login_web.md) (84 TC, `CRM_LOGIN_TC_001` → `084`, không có TC `@Deprecated`)
**Loại:** Regression (module) — agent suy ra (user không chỉ định): checklist regression trước ([`checklist_regression_20261109.md`](checklist_regression_20261109.md), giữ nguyên) chỉ phủ 34 REQ, nay module có 47 REQ sau ticket khoá tài khoản `LOGIN-LOCKOUT-11112026`. Lấy mục từ V1 + V2 + V3 `Permission`; thêm TC_070 (V3b — khoá theo email, không khoá người khác) vì ảnh hưởng quyền truy cập của người dùng khác. Bỏ V4, V3 ngoài `Permission` và V3c `Database`
**Scope:** Module `LOGIN` · nền tảng Web · trang Login, Forgot Password, menu ảnh đại diện, điều hướng phiên, khoá tài khoản · tài khoản admin + Project Manager + Contact khách hàng
**Mã checklist:** `CL-regression_20261118` — mã mục khi chạy = `CL-regression_20261118-<nn>`
**Trạng thái lấy từ:** 29/39 mục đã có kết quả (22 PASS · 2 FAIL · 5 BLOCKED) — lần chạy bộ TC [`run_1794303621`](../../../executions/login/web/run_1794303621/execution_report.md) (10-11-2026) và [`run_1794989188`](../../../executions/login/web/run_1794989188/execution_report.md) (18-11-2026), lấy kết quả mới nhất của từng TC. Chưa có lần chạy nào của chính checklist này
**Lưu ý trạng thái:** mục 15, 16 `❌ FAIL` là kết quả theo Expected **cũ** của TC_013-d, TC_014-b/c (10-11-2026) — Expected đã sửa ngay sau lần chạy đó (máy chủ tự kiểm định dạng email); cột *Kết quả kỳ vọng* dưới đây đã theo Expected mới. Mục 1, 14, 29, 30, 39 `⚠️ BLOCKED` do giới hạn của trình duyệt tích hợp hoặc bước tay chưa làm (focus, bộ nhớ tạm, xoá cookie HttpOnly, tạo Contact) — không phải lỗi hệ thống; tester chạy tay trên Chrome thật là kiểm được. Chạy lại checklist này sẽ thay các trạng thái mượn.
**Cập nhật 18-11-2026 15:50:** ghi đè bản sinh lúc sáng cùng ngày (chưa ai tick) — làm mới trạng thái theo `run_1794989188`; kỳ vọng mục 31 điền nội dung cảnh báo đã quan sát; thêm chú thích nhãn tiếng Việt. Số mục và thứ tự mục không đổi.

**Quy ước:** đường dẫn tính từ địa chỉ gốc ở biến `URL` trong `.env` · **tài khoản admin** = `EMAIL_ADMIN` / `PASSWORD_ADMIN` trong `.env` · 🔒 không ghi mật khẩu vào checklist, ảnh hay bug · mỗi mục chạy trong **cửa sổ ẩn danh mới** trừ khi ghi khác · email sai luôn đuôi `@example.invalid`, mỗi mục một email riêng · **không bao giờ** gửi mật khẩu sai cho email admin.
**Ngôn ngữ giao diện:** trang Login / Forgot Password tiếng Anh. Khu admin của tài khoản `.env` hiện để **Tiếng Việt** — `Dashboard` hiện là **`Bảng tin`**, `Customers` là **`Khách hàng`**, `Logout` là **`Đăng xuất`**; tick đạt khi nhãn tiếng Việt tương ứng (user chốt 18-11-2026).

**Cần chuẩn bị** (chưa có thì mục tương ứng đánh `⚠️ BLOCKED`, **không** chạy thay bằng tài khoản admin):

| Cần | Dùng cho mục | Tình trạng 18-11-2026 |
|---|---|---|
| `TK-PM-1`, `TK-PM-2` — tài khoản Project Manager, biến `EMAIL_PM_1` / `PASSWORD_PM_1` · `EMAIL_PM_2` / `PASSWORD_PM_2` trong `.env` | 33–38 | ⏳ `.env` chưa có biến |
| `TK-TEST-01` (không 2FA) · `TK-TEST-02a` (bật 2FA) · `TK-TEST-03` + hộp thư test — giá trị dự kiến ở ASM-02, ASM-11 của index TC | 17, 32, 21, 22 | ⏳ chưa cấp |
| Contact `qa.contact.login042@example.test` (mật khẩu theo Test Data TC_042) | 39 | ⏳ chưa tạo — cần người tạo Contact theo Pre-Condition TC_042 |
| Profile Chrome riêng (không ẩn danh), đã xoá cookie của tên miền hệ thống · DevTools | 28–30 | — |

**Thứ tự chạy đề xuất (để vừa ~45 phút):** đầu tiên tiền đề TĐ-K (đăng nhập đúng `TK-PM-1` → `Đăng xuất`) rồi mục **33 → 36** (~5 phút, ghi giờ **T**) · trong 16 phút chờ hết khoá, chạy nhóm 1–6 và 8 ở cửa sổ khác · từ **T + 16 phút** chạy mục **37 → 38** · mục 31 (bộ đếm giờ) chạy **cuối cùng** nếu phải dùng tài khoản admin.

### Nhóm: Giao diện & mở trang

| # | Trạng thái | Hạng mục kiểm tra | Kết quả kỳ vọng | Priority | REQ ID | TC ID liên quan | Execution ID |
|---|---|---|---|---|---|---|---|
| 1 | ⚠️ BLOCKED | Mở `/admin/authentication`, không chạm chuột hay bàn phím | Thấy logo, tiêu đề `Login`, ô `Email Address`, ô `Password`, ô `Remember me` chưa tích, nút `Login`, liên kết `Forgot Password?`; con trỏ nhấp nháy sẵn trong ô Email | P1 | REQ-LOGIN-01, REQ-LOGIN-02 | CRM_LOGIN_TC_001 | [run_1794989188](../../../executions/login/web/run_1794989188/execution_report.md)<br><sub>18-11-2026</sub> |
| 2 | ✅ PASS | Mở `/admin/authentication/forgot_password` | Tiêu đề `Forgot Password`, ô `Email Address` trống, nút `Confirm`; không có liên kết quay lại Login | P2 | REQ-LOGIN-18 | CRM_LOGIN_TC_002 | [run_1794303621](../../../executions/login/web/run_1794303621/execution_report.md)<br><sub>10-11-2026</sub> |
| 3 | ✅ PASS | Bấm liên kết `Forgot Password?` trên trang Login | Thanh địa chỉ kết thúc bằng `/admin/authentication/forgot_password`, tiêu đề `Forgot Password` | P2 | REQ-LOGIN-17 | CRM_LOGIN_TC_004 | [run_1794303621](../../../executions/login/web/run_1794303621/execution_report.md)<br><sub>10-11-2026</sub> |
| 4 | ✅ PASS | Đăng nhập admin, bấm ảnh đại diện góc phải, rồi bấm `Esc` | Menu đúng 5 mục (tiếng Anh: `My Profile` · `My Timesheets` · `Edit Profile` · `Language` · `Logout`); bấm `Esc` menu đóng | P2 | REQ-LOGIN-25 | CRM_LOGIN_TC_003, CRM_LOGIN_TC_055 | [run_1794303621](../../../executions/login/web/run_1794303621/execution_report.md)<br><sub>10-11-2026</sub> |

### Nhóm: Đăng nhập & đăng xuất

| # | Trạng thái | Hạng mục kiểm tra | Kết quả kỳ vọng | Priority | REQ ID | TC ID liên quan | Execution ID |
|---|---|---|---|---|---|---|---|
| 5 | ✅ PASS | Đăng nhập tài khoản admin, không tích `Remember me` | Vào Dashboard: địa chỉ kết thúc `/admin/`, tên tab `Dashboard` / `Bảng tin`, thanh menu bên trái hiện | P1 | REQ-LOGIN-09 | CRM_LOGIN_TC_005 | [run_1794989188](../../../executions/login/web/run_1794989188/execution_report.md)<br><sub>18-11-2026</sub> |
| 6 | ✅ PASS | Đăng nhập tài khoản admin, có tích `Remember me` | Vào Dashboard `/admin/`, không có khung thông báo đỏ | P1 | REQ-LOGIN-09 | CRM_LOGIN_TC_006 | [run_1794989188](../../../executions/login/web/run_1794989188/execution_report.md)<br><sub>18-11-2026</sub> |
| 7 | ✅ PASS | Đang ở Dashboard, bấm ảnh đại diện → `Logout` / `Đăng xuất` | Về ngay `/admin/authentication`, không hộp xác nhận; ô Email trống | P1 | REQ-LOGIN-26 | CRM_LOGIN_TC_007 | [run_1794303621](../../../executions/login/web/run_1794303621/execution_report.md)<br><sub>10-11-2026</sub> |
| 8 | ✅ PASS | Bấm đúp thật nhanh nút `Login` với tài khoản admin | Vào Dashboard `/admin/`, chỉ một tab; không hiện trang lỗi hay trang từ chối yêu cầu | P2 | REQ-LOGIN-09 | CRM_LOGIN_TC_036 | [run_1794989188](../../../executions/login/web/run_1794989188/execution_report.md)<br><sub>18-11-2026</sub> |

### Nhóm: Bắt buộc nhập & định dạng (form Login)

| # | Trạng thái | Hạng mục kiểm tra | Kết quả kỳ vọng | Priority | REQ ID | TC ID liên quan | Execution ID |
|---|---|---|---|---|---|---|---|
| 9 | ✅ PASS | Để trống cả Email và Password, bấm `Login` | Đủ 2 khung đỏ `The Password field is required.` và `The Email Address field is required.` (không xét thứ tự) | P1 | REQ-LOGIN-05 | CRM_LOGIN_TC_008 | [run_1794303621](../../../executions/login/web/run_1794303621/execution_report.md)<br><sub>10-11-2026</sub> |
| 10 | ✅ PASS | Nhập Email `auto_cl10_20261118@example.invalid`, Password 3 dấu cách, bấm `Login` | Đúng 1 khung đỏ `The Password field is required.`; ô Email bị xoá trống | P1 | REQ-LOGIN-06, REQ-LOGIN-08 | CRM_LOGIN_TC_009, CRM_LOGIN_TC_021 | [run_1794303621](../../../executions/login/web/run_1794303621/execution_report.md)<br><sub>10-11-2026</sub> |
| 11 | ✅ PASS | Để trống Email, nhập Password `Abc@12345`, bấm `Login` | Đúng 1 khung đỏ `The Email Address field is required.` | P2 | REQ-LOGIN-31 | CRM_LOGIN_TC_010 | [run_1794303621](../../../executions/login/web/run_1794303621/execution_report.md)<br><sub>10-11-2026</sub> |
| 12 | ✅ PASS | Nhập Email `abc`, Password `Abc@12345`, bấm `Login` | Trình duyệt hiện cảnh báo cạnh ô Email; trang không nạp lại, chữ đã nhập còn nguyên | P1 | REQ-LOGIN-03 | CRM_LOGIN_TC_011, CRM_LOGIN_TC_012 | [run_1794303621](../../../executions/login/web/run_1794303621/execution_report.md)<br><sub>10-11-2026</sub> |
| 13 | ✅ PASS | Nhập Email `qa.login@localhost`, Password `Abc@12345`, bấm `Login` | Trình duyệt không chặn; đúng 1 khung đỏ `The Email Address field must contain a valid email address.` | P2 | REQ-LOGIN-03 | CRM_LOGIN_TC_059 | [run_1794989188](../../../executions/login/web/run_1794989188/execution_report.md)<br><sub>18-11-2026</sub> |
| 14 | ⚠️ BLOCKED | Gõ `Abc@12345` vào ô Password | Chỉ hiện 9 dấu chấm; không có nút hiện/ẩn mật khẩu | P2 | REQ-LOGIN-04 | CRM_LOGIN_TC_016 | [run_1794989188](../../../executions/login/web/run_1794989188/execution_report.md)<br><sub>18-11-2026</sub> |

### Nhóm: Sai thông tin đăng nhập

| # | Trạng thái | Hạng mục kiểm tra | Kết quả kỳ vọng | Priority | REQ ID | TC ID liên quan | Execution ID |
|---|---|---|---|---|---|---|---|
| 15 | ❌ FAIL | Đăng nhập Email `auto_cl15_20261118@example.invalid`, Password `Abc@12345` | Đúng 1 khung đỏ `Invalid email or password`; ô Email và Password đều trống | P1 | REQ-LOGIN-07, REQ-LOGIN-08 | CRM_LOGIN_TC_013, CRM_LOGIN_TC_021 | [run_1794303621](../../../executions/login/web/run_1794303621/execution_report.md)<br><sub>10-11-2026</sub> |
| 16 | ❌ FAIL | Dán Email 255 ký tự (dòng 2 file [`email_dai_254_255_320.txt`](../../../testcases/login/web/data/email_dai_254_255_320.txt)), Password `Abc@12345`, bấm `Login` | Khung đỏ `The Email Address field must contain a valid email address.`; không có trang lỗi hay chữ `Database Error` | P3 | REQ-LOGIN-07 | CRM_LOGIN_TC_014 | [run_1794303621](../../../executions/login/web/run_1794303621/execution_report.md)<br><sub>10-11-2026</sub> |
| 17 | ☐ | Đăng nhập đúng `TK-TEST-01` rồi đăng xuất; đăng nhập lại với mật khẩu `SaiMatKhau@999` | Khung đỏ `Invalid email or password` — chữ giống hệt mục 15, không lộ email có tồn tại | P1 | REQ-LOGIN-30 | CRM_LOGIN_TC_018 | — |

### Nhóm: Quên mật khẩu

| # | Trạng thái | Hạng mục kiểm tra | Kết quả kỳ vọng | Priority | REQ ID | TC ID liên quan | Execution ID |
|---|---|---|---|---|---|---|---|
| 18 | ✅ PASS | Để trống Email trang Forgot Password, bấm `Confirm` | Đúng 1 khung đỏ `Email not found` (hành vi hiện tại, nghi lỗi — AMB-LOGIN-05) | P2 | REQ-LOGIN-20 | CRM_LOGIN_TC_022 | [run_1794303621](../../../executions/login/web/run_1794303621/execution_report.md)<br><sub>10-11-2026</sub> |
| 19 | ✅ PASS | Nhập Email `abc` trang Forgot Password, bấm `Confirm` | Trình duyệt hiện cảnh báo cạnh ô Email; trang không nạp lại | P2 | REQ-LOGIN-19 | CRM_LOGIN_TC_023 | [run_1794303621](../../../executions/login/web/run_1794303621/execution_report.md)<br><sub>10-11-2026</sub> |
| 20 | ✅ PASS | Nhập `auto_cl20_20261118@example.invalid` trang Forgot Password, bấm `Confirm` | Khung đỏ `Email not found`; ô Email vẫn giữ nguyên chuỗi vừa nhập | P1 | REQ-LOGIN-21, REQ-LOGIN-22 | CRM_LOGIN_TC_024, CRM_LOGIN_TC_025 | [run_1794303621](../../../executions/login/web/run_1794303621/execution_report.md)<br><sub>10-11-2026</sub> |
| 21 | ☐ | Nhập email `TK-TEST-03` trang Forgot Password, bấm `Confirm` | Không có khung `Email not found`; hộp thư test nhận thư đặt lại mật khẩu trong 5 phút | P2 | REQ-LOGIN-23 | CRM_LOGIN_TC_026 | — |
| 22 | ☐ | Mở liên kết trong thư mục 21, đặt mật khẩu mới, đăng nhập bằng mật khẩu mới | Vào Dashboard; mật khẩu cũ báo `Invalid email or password` (rà xong trả lại mật khẩu cũ — ASM-27) | P2 | REQ-LOGIN-24 | CRM_LOGIN_TC_027 | — |

### Nhóm: Phiên & điều hướng

| # | Trạng thái | Hạng mục kiểm tra | Kết quả kỳ vọng | Priority | REQ ID | TC ID liên quan | Execution ID |
|---|---|---|---|---|---|---|---|
| 23 | ✅ PASS | Chưa đăng nhập, gõ thẳng `/admin/clients` vào thanh địa chỉ | Dừng ở `/admin/authentication`, form Login hiện, không có khung thông báo | P1 | REQ-LOGIN-11 | CRM_LOGIN_TC_028 | [run_1794303621](../../../executions/login/web/run_1794303621/execution_report.md)<br><sub>10-11-2026</sub> |
| 24 | ✅ PASS | Bị đưa về Login từ `/admin/clients`, đăng nhập tài khoản admin | Vào `/admin/` (Dashboard), **không** quay lại `/admin/clients` | P2 | REQ-LOGIN-10 | CRM_LOGIN_TC_029 | [run_1794989188](../../../executions/login/web/run_1794989188/execution_report.md)<br><sub>18-11-2026</sub> |
| 25 | ✅ PASS | Đang đăng nhập, gõ lần lượt `/admin/authentication` và `/admin/authentication/forgot_password` | Cả hai lần tự về `/admin/`, không thấy form Login hay Forgot Password | P2 | REQ-LOGIN-12, REQ-LOGIN-13 | CRM_LOGIN_TC_030, CRM_LOGIN_TC_031 | [run_1794303621](../../../executions/login/web/run_1794303621/execution_report.md)<br><sub>10-11-2026</sub> |
| 26 | ✅ PASS | Sau khi đăng xuất, gõ `/admin/` vào thanh địa chỉ | Dừng ở `/admin/authentication`, phải nhập lại email và mật khẩu | P1 | REQ-LOGIN-27 | CRM_LOGIN_TC_032 | [run_1794303621](../../../executions/login/web/run_1794303621/execution_report.md)<br><sub>10-11-2026</sub> |
| 27 | ✅ PASS | Mở 2 tab đã đăng nhập; đăng xuất ở tab A, bấm `Projects` / `Các dự án` ở tab B | Tab B về trang Login, không mở được trang dự án | P2 | REQ-LOGIN-27 | CRM_LOGIN_TC_033 | [run_1794303621](../../../executions/login/web/run_1794303621/execution_report.md)<br><sub>10-11-2026</sub> |
| 28 | ✅ PASS | Profile Chrome riêng: đăng nhập có tích `Remember me`, đăng xuất, gõ `/admin/` | Vẫn ở trang Login — không tự đăng nhập lại | P1 | REQ-LOGIN-28 | CRM_LOGIN_TC_045 | [run_1794989188](../../../executions/login/web/run_1794989188/execution_report.md)<br><sub>18-11-2026</sub> |
| 29 | ⚠️ BLOCKED | Profile riêng: đăng nhập có tích `Remember me`, xoá cookie `sp_session` trong DevTools, mở `/admin/` | Vào thẳng Dashboard, không phải nhập lại mật khẩu | P2 | REQ-LOGIN-16 | CRM_LOGIN_TC_040 | [run_1794989188](../../../executions/login/web/run_1794989188/execution_report.md)<br><sub>18-11-2026</sub> |
| 30 | ⚠️ BLOCKED | Profile riêng: đăng nhập **không** tích `Remember me`, xoá cookie `sp_session`, mở `/admin/` | Dừng ở trang Login, phải nhập lại | P2 | REQ-LOGIN-33 | CRM_LOGIN_TC_041 | [run_1794989188](../../../executions/login/web/run_1794989188/execution_report.md)<br><sub>18-11-2026</sub> |
| 31 | ✅ PASS | Bật bộ đếm giờ ở task `QA-LOGIN-TC034-TIMER`, bấm ảnh đại diện → `Đăng xuất` | Hộp cảnh báo *"Phát hiện mục tính thời gian đang chạy!…"* (EN: `Started tasks timers found!…`), nút đóng `×`; vẫn ở Dashboard. Dừng timer sau khi rà | P3 | REQ-LOGIN-34 | CRM_LOGIN_TC_034 | [run_1794989188](../../../executions/login/web/run_1794989188/execution_report.md)<br><sub>18-11-2026</sub> |
| 32 | ☐ | Đăng nhập đúng mật khẩu `TK-TEST-02a` (tài khoản bật 2FA) | Hiện bước nhập mã xác thực; chưa vào Dashboard (không thấy menu bên trái) | P2 | REQ-LOGIN-32 | CRM_LOGIN_TC_035 | — |

### Nhóm: Khoá tài khoản (chạy tuần tự, một lượt khoá — xem *Thứ tự chạy đề xuất*)

| # | Trạng thái | Hạng mục kiểm tra | Kết quả kỳ vọng | Priority | REQ ID | TC ID liên quan | Execution ID |
|---|---|---|---|---|---|---|---|
| 33 | ☐ | Đăng nhập `TK-PM-1` sai 5 lần liên tiếp `SaiMatKhau@01` → `@05`; ghi giờ lần 5 = T | Cả 5 lần đúng 1 khung đỏ `Invalid email or password`; **không** có chữ `Your account is locked.` | P1 | REQ-LOGIN-35, REQ-LOGIN-42 | CRM_LOGIN_TC_060 | — |
| 34 | ☐ | Gửi lần thứ 6 với `TK-PM-1` / `SaiMatKhau@06` | Đúng 1 khung `Your account is locked. Please try again in 15 minutes.` (chữ theo ticket, chưa quan sát); không vào Dashboard | P1 | REQ-LOGIN-35, REQ-LOGIN-37 | CRM_LOGIN_TC_060, CRM_LOGIN_TC_061 | — |
| 35 | ☐ | Ngay sau mục 34, đăng nhập `TK-PM-1` bằng mật khẩu **đúng** | Vẫn khung có chữ `Your account is locked.`; không vào Dashboard | P1 | REQ-LOGIN-38 | CRM_LOGIN_TC_062 | — |
| 36 | ☐ | Cùng cửa sổ, cùng mạng, đăng nhập đúng `TK-PM-2` | Vào Dashboard `/admin/` — khoá chỉ áp cho email `TK-PM-1`. Rồi đăng xuất | P1 | REQ-LOGIN-40 | CRM_LOGIN_TC_070 | — |
| 37 | ☐ | Từ T + 16 phút (đã thử ở mục 34–35), đăng nhập đúng `TK-PM-1` | Không có chữ `Your account is locked.`; vào Dashboard — lần thử trong lúc khoá không gia hạn khoá. Rồi đăng xuất | P1 | REQ-LOGIN-36, REQ-LOGIN-43 | CRM_LOGIN_TC_063, CRM_LOGIN_TC_064 | — |
| 38 | ☐ | Ngay sau mục 37: `TK-PM-1` sai 4 lần (`SaiMatKhau@01` → `@04`), rồi đăng nhập đúng | 4 lần đều `Invalid email or password`, không khoá; lần đúng vào Dashboard — bộ đếm đã về 0. Rồi đăng xuất | P2 | REQ-LOGIN-39, REQ-LOGIN-47 | CRM_LOGIN_TC_066, CRM_LOGIN_TC_065 | — |

### Nhóm: Phân quyền

| # | Trạng thái | Hạng mục kiểm tra | Kết quả kỳ vọng | Priority | REQ ID | TC ID liên quan | Execution ID |
|---|---|---|---|---|---|---|---|
| 39 | ⚠️ BLOCKED | Đăng nhập khu admin bằng Contact `qa.contact.login042@example.test` | Khung đỏ `Invalid email or password`; không vào Dashboard | P1 | REQ-LOGIN-29 | CRM_LOGIN_TC_042 | [run_1794989188](../../../executions/login/web/run_1794989188/execution_report.md)<br><sub>18-11-2026</sub> |

### Không áp dụng cho module này

- **Data Table / List** — module không có bảng dữ liệu, lọc, tìm kiếm, phân trang
- **Báo cáo / Dashboard** — module không hiển thị số liệu; Dashboard chỉ là trang đích sau đăng nhập
- **CRUD Lifecycle** — module không tạo/sửa/xoá bản ghi nghiệp vụ (Contact mục 39 và task mục 31 là dữ liệu tiền đề của module khác)
- **Status Flow của entity** — không có entity mang trạng thái; luồng **phiên** nằm ở nhóm *Phiên & điều hướng*, luồng **khoá tài khoản** ở nhóm riêng
- **Notification / Toast** — module không dùng toast; thông báo là khung đỏ cố định trên form, đã có ở mục 9–20, 33–35
- **Modal / Dialog** — chỉ có hộp cảnh báo bộ đếm giờ khi đăng xuất (mục 31); không có modal nhập liệu
- **Ma trận quyền theo role nhân viên** — trang Login không đổi hành vi theo role; trục phân quyền duy nhất là nhân viên ↔ Contact khách hàng (mục 39)

### Đã cắt khỏi checklist (vẫn có trong bộ TC chi tiết)

- **REQ không có mục** (41/47 REQ có mục): REQ-LOGIN-14, 45 (CSRF — V3, cần DevTools sửa mã ẩn: TC_043, 058, 068) · REQ-LOGIN-15 (hình thái cookie ghi nhớ — V3: TC_044; phần dùng được đã có ở mục 29) · REQ-LOGIN-41 (khoá từ IP khác — V3, cần mạng thứ hai: TC_071) · REQ-LOGIN-44, 46 (Password trống / email khác xen giữa không tính lần sai — TC_067, 069: mỗi mục tốn thêm một lượt khoá 16 phút, vượt ngưỡng 45 phút)
- **V3 ngoài Permission** — SQLi/XSS TC_046–048, nút Back sau đăng xuất TC_049
- **V3c Database** — TC_072 → 084 (`@DBCheck`, cần `DB_*` trong `.env` — AMB-SYS-05)
- **V4** — bàn phím, responsive, đa trình duyệt: TC_050–054 (TC_050 đang có bug mở [`BUG_login_1794305372_TC050`](../../../bugs/login/web/BUG_login_1794305372_TC050.md))
- **Biến thể / mục trùng** — giữ 1–2 mục đại diện mỗi field: email viết hoa TC_015, password cực trị TC_017, dán từ bộ nhớ tạm TC_019, bấm `Remember me` TC_020, bấm đúp `Confirm` TC_037, mất mạng TC_038, kịch bản trọn vòng TC_039, F5 / Back sau đăng nhập TC_056–057

### Ký nhận

| Môi trường | Build / Version | Người thực hiện | Ngày | Kết quả (Pass/Fail/Blocked) |
|---|---|---|---|---|
|  |  |  |  |  |
