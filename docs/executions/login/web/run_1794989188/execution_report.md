# Execution Report — Đăng nhập (`LOGIN`) · Web · Chạy theo phạm vi chọn (23 TC)

| Thông tin | Nội dung |
|---|---|
| Run ID | run_1794989188 |
| Nền tảng | `web` |
| Loại nguồn | `Bộ TC` |
| Nguồn TC | [`web/test_cases_login_web.md`](../../../../testcases/login/web/test_cases_login_web.md) (84 TC, 0 `@Deprecated`) |
| Phạm vi | 23/84 TC · loại 0 TC `@Deprecated`. **20 TC chưa từng chạy, chạy được với tài khoản admin `.env`:** 005, 006, 019, 029, 034, 036, 038, 039, 040, 041, 042, 043, 044, 045, 051, 053, 054, 057, 058, 059 · **3 TC BLOCKED ở `run_1794303621`:** 001, 016, 056 — chọn theo mục *Việc cần làm* của [RTM LOGIN](../../../../traceability/login/traceability_matrix_login.md) |
| Môi trường | `https://crm.anhtester.com` (biến `URL` trong `.env`) — môi trường demo dùng chung |
| Build / Version | Perfex CRM 3.1.6 (theo requirements) |
| Tài khoản | Tài khoản admin `.env` — **user tự gõ mật khẩu** ở mọi bước đăng nhập; agent không gõ mật khẩu |
| Trình duyệt | Trình duyệt tích hợp của Claude desktop app (Chromium) — Playwright MCP chưa được đăng ký (repo chưa có `.mcp.json`) |
| Người thực hiện | minhai2204-debug (agent hỗ trợ) |
| Bắt đầu → Kết thúc | 18-11-2026 15:06 → 15:39 (≈ 33 phút, gồm thời gian chờ user gõ mật khẩu 10 lần) |
| Môi trường dùng chung? | Có — auto-skip TC phá huỷ đang BẬT |
| Video | Không — chưa nạp tool quay (Playwright MCP chưa đăng ký); user chọn chạy không video |
| Cách xử lý bước agent không tự làm được | User chọn **"Chỉ chạy phần agent tự làm được"**: TC cần ngắt mạng máy, trình duyệt khác Chrome, tạo Contact có mật khẩu, dán từ trình soạn thảo → `⚠️ BLOCKED`, không chạy |

## 1. Tổng kết

| Trạng thái | Số lượng | Tỷ lệ |
|---|---|---|
| ✅ PASS | 12 | 52.2% |
| ❌ FAIL | 0 | 0% |
| ⚠️ BLOCKED | 11 | 47.8% |
| ⏭️ SKIPPED | 0 | 0% |
| **Tổng** | **23** | 100% |

> **Pass rate (không tính SKIPPED):** 12/23 = 52.2% · trên TC chấm được (PASS + FAIL): 12/12. Không TC nào FAIL — 11 TC BLOCKED đều do giới hạn công cụ / điều kiện chạy, không phải lỗi hệ thống.
>
> **Ngôn ngữ môi trường:** tài khoản admin dùng chung đang để **Tiếng Việt** (khác lúc recon 02-11 và lần chạy 10-11). Bước kiểm chữ `Dashboard` / `Customers` được chấm theo nghĩa tương đương (`Bảng tin` / `Khách hàng`) — **user chốt 18-11-2026**. Trang Login và Forgot Password vẫn tiếng Anh.

## 2. Kết quả từng TC

| TC ID | Test Scenario | Kết quả | Bước fail | Ghi chú |
|---|---|---|---|---|
| CRM_LOGIN_TC_059 | Email trình duyệt cho qua nhưng máy chủ coi là sai định dạng → thông báo định dạng của máy chủ | ✅ PASS | — | `qa.login@localhost` / `Abc@12345`: trình duyệt không chặn, trang nạp lại ở `/admin/authentication`, đúng một khung đỏ `The Email Address field must contain a valid email address.`; hai ô trống; không vào Dashboard |
| CRM_LOGIN_TC_056 | F5 sau khi đăng nhập sai, đồng ý gửi lại biểu mẫu → vẫn ở trang Login | ⚠️ BLOCKED | — | Bước 4 đạt (`Invalid email or password`). Bước 5–7 không kiểm được: phím F5 do công cụ gửi **không** nạp lại trang (biến đánh dấu đặt trên trang trước khi bấm vẫn còn, kiểu điều hướng vẫn `navigate`), không thấy hộp thoại gửi lại biểu mẫu — hộp thoại gốc của trình duyệt nằm ngoài tầm công cụ. Lần thứ 2 BLOCKED cùng nguyên nhân → cần tester chạy tay |
| CRM_LOGIN_TC_001 | Trang Login hiển thị đủ thành phần, đúng nhãn, thứ tự, trạng thái mặc định | ⚠️ BLOCKED | — | Viewport 1600×800 (giả lập của pane). Mục `1` (logo `ANHTESTER` căn giữa, phía trên tiêu đề `Login`), `2` (thứ tự Email → Password → `Remember me` → nút `Login` rộng bằng ô nhập 336px → `Forgot Password?`), `3` (hai ô trống, không chữ gợi ý, `Remember me` chưa tích), `5` (tên tab `Perfex CRM \| Anh Tester Demo - Login`), `6` (không captcha, không liên kết đăng ký, không nút hiện mật khẩu) **đạt**. Mục `4`: con trỏ có nằm sẵn trong ô Email (phần tử đang focus = `email`) nhưng **viền xanh** không quan sát được — pane mất focus cửa sổ ngay sau mỗi lệnh công cụ (`document.hasFocus() = false`), trình duyệt chỉ vẽ viền focus khi cửa sổ có focus. Lần thứ 2 BLOCKED cùng nguyên nhân |
| CRM_LOGIN_TC_016 | Ô Password che ký tự, không sao chép được ra ngoài | ⚠️ BLOCKED | — | Không dựng được Pre-Condition: bộ nhớ tạm của pane không hoạt động — gõ `ClipboardCu`, Ctrl+A, Ctrl+C, xoá, Ctrl+V → ô vẫn trống, nên bước 5 không phân biệt được "trình duyệt chặn sao chép" với "bộ nhớ tạm không chạy". Bước 3 (ô `type=password`, che ký tự) đã đạt ở `run_1794303621`. Lần thứ 2 BLOCKED |
| CRM_LOGIN_TC_019 | Dán Email và Password từ bộ nhớ tạm → đăng nhập thành công | ⚠️ BLOCKED | — | Không chạy: cần sao chép mật khẩu admin từ trình soạn thảo vào bộ nhớ tạm (agent không xử lý mật khẩu) và bộ nhớ tạm của pane không hoạt động (xem TC_016). User chọn chỉ chạy phần agent tự làm được |
| CRM_LOGIN_TC_038 | Mất mạng khi bấm Login → không vào được; có mạng lại thì đăng nhập bình thường | ⚠️ BLOCKED | — | Không chạy: bước 3 phải ngắt mạng của máy — agent không có công cụ ngắt mạng (ngắt mạng cũng cắt luôn phiên làm việc của agent) |
| CRM_LOGIN_TC_042 | Contact của khách hàng không đăng nhập được vào khu admin | ⚠️ BLOCKED | — | Không chạy: Pre-Condition phải tạo Contact `qa.contact.login042@example.test` **có mật khẩu** — tạo tài khoản kèm mật khẩu là bước agent không tự làm; user chọn chỉ chạy phần agent tự làm được |
| CRM_LOGIN_TC_005 | Đăng nhập thành công (không tích Remember me) → vào Dashboard | ✅ PASS | — | User tự gõ email + mật khẩu admin, agent bấm `Login`. Bước 2–4: ô Email có chữ, ô Password `type=password`, `Remember me` trống. Bước 5: không khung đỏ. Bước 6: địa chỉ `/admin/`, có ảnh đại diện, thanh bên trái hiện — **nhãn tiếng Việt**: tên tab `Bảng tin`, menu `Bảng tin` · `Khách hàng` · `Các dự án` (tài khoản admin dùng chung đang để ngôn ngữ Tiếng Việt, `<html lang="vi">`). Chấm theo nghĩa tương đương — **user chốt 18-11-2026**. Bước 7: mở được `/admin/clients` (tab `Khách hàng`), không bị đưa về Login |
| CRM_LOGIN_TC_029 | Bị chặn ở trang khác rồi đăng nhập → luôn vào Dashboard, không quay lại trang cũ | ✅ PASS | — | Bước 2: chưa đăng nhập mở `/admin/clients` → về `/admin/authentication`, không khung thông báo. User gõ thông tin admin, agent bấm `Login`. Bước 4: không khung đỏ. Bước 5: địa chỉ `/admin/` (tab `Bảng tin`), **không** phải `/admin/clients` |
| CRM_LOGIN_TC_036 | Bấm đúp nút Login thật nhanh → chỉ đăng nhập một lần, không trang lỗi | ✅ PASS | — | User gõ thông tin admin, agent bấm đúp nút `Login` (một thao tác double-click). Bước 3: không trang lỗi, không khung đỏ. Bước 4: vào `/admin/` (tab `Bảng tin`), vẫn 1 tab; không có chữ `The action you have requested is not allowed.` |
| CRM_LOGIN_TC_039 | Kịch bản trọn vòng: đăng nhập sai → quên mật khẩu → đăng nhập đúng → đăng xuất → bị chặn | ✅ PASS | — | `recon.khongtontai.tc039@example.invalid` / `Abc@12345`. Bước 4: khung `Invalid email or password`. Bước 5: trang `Forgot Password`. Bước 7: khung `Email not found`. Bước 8: trang Login không còn khung đỏ. Bước 9–10: user gõ thông tin admin, agent bấm `Login` → `/admin/`. Bước 11: ảnh đại diện → `Đăng xuất` → về `/admin/authentication`. Bước 12: gõ `/admin/` → vẫn dừng ở trang Login |
| CRM_LOGIN_TC_043 | Form gửi kèm mã chống giả mạo; mã bị sửa thì không đăng nhập được | ✅ PASS | — | Bước 2 (🔧): form có đúng 1 ô ẩn `csrf_token_name` dài 32 ký tự → agent sửa thành 32 chữ số `0` bằng script (tương đương DevTools → Elements). Bước 4: **không** vào Dashboard — máy chủ trả trang **`419 Page Expired!`** · *"Sorry, the page has expired, return to previous page and refresh to continue."* (tên tab `Error`) — Expected chỉ nêu `The action you have requested is not allowed.` là **ứng viên** `@NeedsVerify`; ý chính "trang từ chối yêu cầu" đạt → đề nghị cập nhật chữ trong Expected và gỡ `@NeedsVerify` qua `/review-testcases`. [Ảnh](evidence/CRM_LOGIN_TC_043_step4_419_page_expired.jpg). Bước 5: `/admin/` → trang Login. Bước 6: mở lại trang (mã thật 32 ký tự), user gõ thông tin admin → vào Dashboard (`/admin`, tab `Bảng tin`); 🔧 form gửi đúng 3 khoá `csrf_token_name`, `email`, `password` |
| CRM_LOGIN_TC_044 | Tích Remember me khi đăng nhập tạo cookie ghi nhớ đúng hình thái | ✅ PASS | — | Bước 4: user gõ thông tin admin, agent tích `Remember me` rồi bấm `Login` — không khung đỏ. Bước 5: vào `/admin/` (tab `Bảng tin`). 🔧 (đọc bằng `document.cookie` + `cookieStore`, không có DevTools): trước bước 4 **không** có `autologin`; sau bước 4 có `autologin` — host-only (domain của hệ thống), path `/`, Secure = có, hạn **62 ngày**, giá trị dài **110 ký tự** (không chép giá trị). Cookie đọc được bằng script → **không** có HttpOnly (RISK-LOGIN-03, không phải tiêu chí PASS/FAIL). `csrf_cookie_name`, `sp_session` không đọc được bằng script (HttpOnly) nên không xác nhận được bằng cách này |
| CRM_LOGIN_TC_006 | Đăng nhập thành công (có tích Remember me) → vào Dashboard | ✅ PASS | — | Trước khi chạy: đã đăng xuất + xoá cookie `autologin` còn sót của TC_044. Bước 2–3: user gõ email + mật khẩu admin (ô Email có chữ, ô Password `type=password`). Bước 4: agent bấm ô `Remember me` → hiện dấu tích. Bước 5: không khung đỏ. Bước 6: `/admin/`, tên tab `Bảng tin` (= Dashboard — ngôn ngữ môi trường, user chốt chấm tương đương), thanh bên trái hiện |
| CRM_LOGIN_TC_045 | Đăng xuất vô hiệu ghi nhớ đăng nhập dù cookie ghi nhớ còn sót | ✅ PASS | — | **Bước 1–4 dùng chung lượt đăng nhập với TC_006** (cùng thao tác: trình duyệt không còn `autologin`, tích `Remember me`, đăng nhập admin) → vào Dashboard. Pre-Condition "profile riêng" thay bằng profile của pane đã đăng xuất + xoá `autologin`. Bước 5: ảnh đại diện → `Đăng xuất`. Bước 6: về `/admin/authentication`. Bước 7–8: gõ `/admin/` → dừng ở trang Login, **không** tự đăng nhập lại. 🔧: sau bước 4 có `autologin`; sau bước 5 `autologin` **vẫn còn** trong trình duyệt (RISK-LOGIN-03) nhưng không khôi phục được phiên |
| CRM_LOGIN_TC_051 | Đăng nhập hoàn toàn bằng bàn phím: Space tích Remember me, Enter gửi form | ✅ PASS | — | Bước 2–3 do user gõ (email → Tab → mật khẩu); user bấm chuột **một lần** vào ô Email để đưa bàn phím vào pane — ô đó vốn đang giữ focus nên không đổi thứ tự focus. Sau bước 3 focus ở ô Password, ô có dấu chấm. Agent bấm phím: bước 4 Tab → focus `remember` · bước 5 Space → tích · bước 6 Space → bỏ tích · bước 7 Shift+Tab → focus `password` · bước 8 Enter → form gửi, vào Dashboard (`/admin`, tab `Bảng tin`). Không có cookie `autologin` (ô đã bỏ tích) |
| CRM_LOGIN_TC_053 | Trang Login hiển thị đủ, không tràn ngang ở các kích thước màn hình đã chốt | ⚠️ BLOCKED | — | Kích thước đặt bằng giả lập viewport của pane, nạp lại trang sau mỗi lần đổi. Bước 3–4 **đạt** ở `a` 1920×1080 · `b` 1366×768 · `c` 768×1024 · `d` 375×812: đủ logo, tiêu đề `Login`, `Email Address`, `Password`, `Remember me`, nút `Login`, `Forgot Password?` — mọi phần tử nằm trong bề ngang khung, không chữ bị cắt; độ rộng nội dung = bề ngang khung, thử cuộn ngang 200px trang không xê dịch. Ảnh: [c](evidence/CRM_LOGIN_TC_053_c_step3_768x1024.jpg) · [d](evidence/CRM_LOGIN_TC_053_d_step3_375x812.jpg). **Không kiểm được:** biến thể `e` (phóng to trình duyệt 200% — pane không có lệnh phóng to trang); bước 5 (đăng nhập ở từng kích thước) — giả lập viewport bị pane xoá khi chuyển lượt cho user gõ mật khẩu. `@NeedsVerify` của bước 3 đã có bằng chứng ở `a`–`d` |
| CRM_LOGIN_TC_057 | Bấm Back ngay sau khi đăng nhập thành công → không quay lại form Login, vẫn ở Dashboard | ✅ PASS | — | User gõ thông tin admin, agent bấm `Login` → bước 3: `/admin/` (tab `Bảng tin`). Bước 4: nút Back của trình duyệt. Bước 5: điểm dừng `/admin/`, tab `Bảng tin`, **không** có form Login hay email đã gõ, vẫn đang đăng nhập — trang Login chỉ nạp thoáng qua rồi tự chuyển về Dashboard (khớp REQ-LOGIN-12). Đã xác nhận trên UI — đề nghị gỡ `@NeedsVerify` |
| CRM_LOGIN_TC_034 | Logout khi có bộ đếm giờ đang chạy → hiện cảnh báo, không đăng xuất | ✅ PASS | — | Chạy **cuối** buổi bằng tài khoản admin (chưa có `TK-TEST-01`, đúng Pre-Condition). Pre-Condition: tạo task `QA-LOGIN-TC034-TIMER` (id 2193) ở `/admin/tasks`, bấm `Bắt đầu tính giờ` — góc trên hiện huy hiệu bộ đếm. Bước 1–2: ảnh đại diện → `Đăng xuất`. Bước 2–3: hiện hộp cảnh báo toàn màn hình *"Phát hiện mục tính thời gian đang chạy! Bạn có chắc chắn muốn đăng xuất mà không dừng chức năng lại??"* + nút đỏ `Đăng xuất` + dấu `×` ([ảnh](evidence/CRM_LOGIN_TC_034_step2_canh_bao_timer.jpg)); thanh địa chỉ vẫn `/admin/`. Bước 4: nút đóng là dấu **`×`** góc trên bên phải → hộp đóng. Bước 5: mở được `/admin/clients`, vẫn đăng nhập. Bước 6: mở task 2193 → `Dừng tính giờ` → `Lưu` → nút trở lại `Bắt đầu tính giờ`, không còn huy hiệu bộ đếm. Đã xác nhận trên UI (nội dung cảnh báo, nhãn nút đóng) — đề nghị gỡ `@NeedsVerify` và điền nhãn nút vào bước 4 |
| CRM_LOGIN_TC_040 | Có tích Remember me → khi phiên chính hết hạn vẫn vào thẳng Dashboard | ⚠️ BLOCKED | — | Không chạy: bước 5 phải chờ 8 giờ 10 phút; cách thay trong 🔧 là xoá riêng cookie `sp_session` — cookie này là HttpOnly (`document.cookie` trống cả khi đang đăng nhập), pane không có DevTools nên agent không xoá được |
| CRM_LOGIN_TC_041 | Không tích Remember me → khi phiên chính hết hạn phải đăng nhập lại | ⚠️ BLOCKED | — | Không chạy: cùng lý do TC_040 (chờ 8 giờ 10 phút hoặc xoá cookie HttpOnly `sp_session` bằng DevTools) |
| CRM_LOGIN_TC_058 | Để trang Login quá hạn mã chống giả mạo rồi mới đăng nhập → bị từ chối, mở lại trang thì đăng nhập được | ⚠️ BLOCKED | — | Không chạy: bước 2 phải để yên 1 giờ 10 phút, không mở tab nào khác của hệ thống (xung đột với các TC còn lại trong buổi); cách thay trong 🔧 là xoá cookie `csrf_cookie_name` — cookie HttpOnly, agent không xoá được |
| CRM_LOGIN_TC_054 | Luồng chính chạy đúng trên các trình duyệt đã chốt ngoài Chrome | ⚠️ BLOCKED | — | Không chạy: biến thể `a` Edge, `b` Firefox — pane chỉ là Chromium, agent không điều khiển trình duyệt khác |

## 3. Chi tiết TC FAIL

Không có TC FAIL.

## 4. TC BLOCKED

| TC ID | Nguyên nhân chặn | Cần gì để chạy được |
|---|---|---|
| CRM_LOGIN_TC_001 | Mục `4` (viền xanh ô Email khi vừa mở trang) — pane mất focus cửa sổ sau mỗi lệnh công cụ. Mọi mục khác đạt. **BLOCKED lần 2** | Tester chạy tay trên Chrome thật, chỉ cần nhìn mục `4` |
| CRM_LOGIN_TC_016 | Bộ nhớ tạm của pane không hoạt động — không dựng được Pre-Condition `ClipboardCu`. **BLOCKED lần 2** | Tester chạy tay bước 4–5 trên Chrome thật |
| CRM_LOGIN_TC_056 | Phím F5 của công cụ không nạp lại trang; hộp thoại gửi lại biểu mẫu ngoài tầm công cụ. **BLOCKED lần 2** | Tester chạy tay bước 5–7 |
| CRM_LOGIN_TC_019 | Phải dán mật khẩu admin từ trình soạn thảo — agent không xử lý mật khẩu, bộ nhớ tạm pane không chạy | Tester chạy tay |
| CRM_LOGIN_TC_038 | Phải ngắt mạng của máy | Tester chạy tay (tắt Wi-Fi / rút cáp) |
| CRM_LOGIN_TC_040 · 041 | Phải chờ 8 giờ 10 phút, hoặc xoá cookie HttpOnly `sp_session` bằng DevTools | Tester có DevTools, hoặc Playwright MCP (`context.clearCookies` theo tên) |
| CRM_LOGIN_TC_042 | Phải tạo Contact có mật khẩu (`qa.contact.login042@example.test`) | Tester tạo Contact theo Pre-Condition rồi chạy lại — hoặc user cho phép agent tạo Contact và tự đặt mật khẩu |
| CRM_LOGIN_TC_053 | Biến thể `e` (phóng to 200%) không giả lập được; bước 5 không giữ được kích thước khi user gõ mật khẩu. Bước 3–4 của `a`–`d` **đạt** | Tester chạy tay `e` + bước 5, hoặc Playwright MCP headless với `viewport` + `deviceScaleFactor` |
| CRM_LOGIN_TC_054 | Edge / Firefox — pane chỉ là Chromium | Tester chạy tay trên Edge, Firefox |
| CRM_LOGIN_TC_058 | Phải để yên trang 1 giờ 10 phút, hoặc xoá cookie HttpOnly `csrf_cookie_name` | Tester có DevTools, hoặc Playwright MCP |

## 5. Dữ liệu đã tạo & dọn dẹp

| Dữ liệu | ID | Nơi tạo | Đã xoá? |
|---|---|---|---|
| Task `QA-LOGIN-TC034-TIMER` (Pre-Condition TC_034) | 2193 | `/admin/tasks` · tài khoản admin | ❌ **Chưa xoá** — bấm `Xóa` trong menu `○○○` của task không có tác dụng (nhiều khả năng hộp xác nhận gốc của trình duyệt bị pane tự huỷ). Không thử cách khác |
| 1 bản ghi thời gian (≈ 2 phút) của task trên | timesheet 81 | Do bật / dừng bộ đếm giờ | ❌ Đi cùng task 2193 — xoá task sẽ xoá theo |
| Lần đăng nhập sai bằng email `@example.invalid` (TC_039, 056, 059) | — | Trang Login | — Không tạo bản ghi; email không tồn tại, không khoá tài khoản thật |

> Bộ đếm giờ **đã dừng** (bước 6 TC_034) — không còn chặn `Đăng xuất` của người khác trên tài khoản admin dùng chung. Cuối buổi pane đã đăng xuất, cookie `autologin` đã xoá. Không đối chiếu số liệu hệ thống (lần chạy không thay đổi số liệu nghiệp vụ nào ngoài task 2193).

## 6. Đề xuất bước tiếp theo

- **Không có FAIL** → không cần `/create-bug-report` cho lần chạy này
- **`/review-testcases` mode FIX** — cập nhật Expected theo điều đã quan sát:
  - TC_043 bước 4: trang từ chối là `419 Page Expired!` · *"Sorry, the page has expired, return to previous page and refresh to continue."* — không phải `The action you have requested is not allowed.`; kiểm cả TC_036 (dùng cùng chữ ứng viên) và TC_058
  - TC_034 bước 2, 4: điền nội dung cảnh báo + nút đóng `×`; gỡ `@NeedsVerify`
  - Gỡ `@NeedsVerify`: TC_034, TC_043, TC_057, TC_053 (bước 3)
  - Expected kiểm chữ `Dashboard` / `Customers` (TC_005, 006, 036, 039, 044, 057…) phụ thuộc ngôn ngữ của tài khoản — đổi sang dấu hiệu không phụ thuộc ngôn ngữ (địa chỉ `/admin/`, có menu bên trái), hoặc thêm Pre-Condition "ngôn ngữ tài khoản = English"
- **TC_001, 016, 056 BLOCKED lần thứ 2** cùng nguyên nhân → không chạy lại bằng pane nữa: giao tester chạy tay, hoặc tạo `.mcp.json` cho Playwright MCP headed (có video) rồi chạy lại cùng TC_040, 041, 053, 058 — 7 TC
- **Dữ liệu còn sót:** task `QA-LOGIN-TC034-TIMER` (id 2193) — user xoá tay ở `/admin/tasks`, hoặc để lại
- Sinh lại RTM: `/generate-traceability-matrix login` — số TC từng chạy tăng từ 34 lên 54/84 (TC chưa từng chạy còn 30: nhóm khoá tài khoản 060 → 071, kiểm CSDL 072 → 084, tài khoản test 015, 018, 026, 027, 035)
- **Phát hiện ngoài TC:** tài khoản admin dùng chung đổi ngôn ngữ sang Tiếng Việt từ sau 10-11-2026 (ai đó trên môi trường dùng chung) — các lần chạy sau nên kiểm ngôn ngữ trước khi chấm
