# Báo Cáo Review Test Cases — Đăng nhập (`LOGIN`) · Web

> ← [Index module `TEST_CASES_LOGIN_SUMMARY.md`](../TEST_CASES_LOGIN_SUMMARY.md) · Workflow `/review-testcases` · **Mode REVIEW**, sau đó **Mode FIX** cùng ngày — điểm và gap bên dưới chấm trên bản `752c90a` (trước khi sửa); việc đã áp dụng xem mục cuối [*Kết quả Mode FIX*](#kết-quả-mode-fix-10-11-2026)

## Tổng quan

- **Nguồn:** [`web/parts/part_01_web_chuc_nang.md`](../web/test_cases_login_web.md) (42 TC) · [`web/parts/part_02_web_ky_thuat_phi_chuc_nang.md`](../web/test_cases_login_web.md) (13 TC) · index [`TEST_CASES_LOGIN_SUMMARY.md`](../TEST_CASES_LOGIN_SUMMARY.md) — mốc git `752c90a`
- **Requirements đối chiếu:** [`REQUIREMENTS_LOGIN_SUMMARY.md`](../../../requirements/login/REQUIREMENTS_LOGIN_SUMMARY.md) · [`requirements_login_web.md`](../../../requirements/login/web/requirements_login_web.md) — `REQ-LOGIN-01` → `34` (git `cb8ea3a`)
- **Số TC review:** 55 · `@Deprecated`: 0 · **125 biến thể** (đếm lại độc lập: 86 biến thể ở 25 TC có Bảng biến thể + 28 TC đơn + 11 mục Bảng kiểm Kiểu B ở TC_001, TC_002 — **khớp** con số index công bố)
- **Kết quả:** 🟢 54 tốt | 🟡 1 cần sửa | 🔴 0 nên viết lại
- **Điểm trung bình:** 11,5/12 (37 TC đạt 12/12)
- **Loại trừ theo requirements:** cổng khách hàng `/clients/*` · màn đặt mật khẩu mới ngoài phần `REQ-LOGIN-24` · cấu hình 2FA (module `PROF`) · cấu hình chính sách đăng nhập (module `SETTING`) · khoá tài khoản / brute-force (`AMB-LOGIN-10`, `RISK-LOGIN-04`) · thứ tự hai thông báo bắt buộc (`AMB-LOGIN-04`) · mã chuyển hướng HTTP (`AMB-LOGIN-09`)
- **Kết quả chạy:** chưa có `docs/executions/login/` → không có ghi chú `⚠️ chưa có evidence` / `@NeedsVerify` nào đã được giải quyết để dọn

**Nhận định chung:** cách viết từng TC rất tốt — Steps đánh số, Expected khớp số bước, nhãn nguyên văn, dữ liệu cụ thể, ngôn ngữ DOM đã được dồn xuống `🔧 Ghi chú kỹ thuật` gần như toàn bộ. Điểm yếu thật **không nằm ở rubric** mà ở 3 chỗ: (1) TC_027 và nhóm TC có trạng thái dùng chung (timer trên tài khoản admin, profile Chrome dùng chung cookie ghi nhớ, mật khẩu `TK-TEST-03` bị đổi) — chạy lại hoặc chạy song song sẽ FAIL oan; (2) bốn nhánh 4 vòng còn nông: Error Guessing, Security, State Transition, Accessibility; (3) hai mục field-level chỉ phủ hình thức.

## Chi tiết từng TC

> Cột *Trừ điểm* ghi tiêu chí bị trừ: C1 Rõ ràng · C2 Expected đo được · C3 Độc lập · C4 Test data · C5 Truy vết · C6 Đúng trọng tâm. Đề xuất sửa chi tiết (trích nguyên văn + bản viết lại) cho TC bị trừ điểm nằm ở mục kế tiếp.

| TC ID | Điểm | Xếp loại | Trừ điểm | Vấn đề chính | Đề xuất sửa |
|---|---|---|---|---|---|
| CRM_LOGIN_TC_001 | 12/12 | 🟢 | — | Mục `5` *"Tên tab trình duyệt kết thúc bằng `- Login`"* chặt hơn REQ-LOGIN-01 (*"chứa `- Login`"*) — không trừ điểm | Đổi thành *"Tên tab trình duyệt có chữ `- Login`"* |
| CRM_LOGIN_TC_002 | 12/12 | 🟢 | — | Mục `5` cùng vấn đề như TC_001 | Như TC_001 |
| CRM_LOGIN_TC_003 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_004 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_005 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_006 | 12/12 | 🟢 | — | Phần chính trùng TC_044 (xem *TC trùng lặp*) | — |
| CRM_LOGIN_TC_007 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_008 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_009 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_010 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_011 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_012 | 12/12 | 🟢 | — | Mới 5 biến thể — còn chỗ cho ký tự đặc biệt **bị chặn** trước `@` (Gap #7) | Thêm biến thể `f` |
| CRM_LOGIN_TC_013 | 12/12 | 🟢 | — | Biến thể `a` trùng TC_021-b | Xem *TC trùng lặp* |
| CRM_LOGIN_TC_014 | 11/12 | 🟢 | C4 −1 | Chuỗi 254/255/320 ký tự chỉ cho dưới dạng công thức, tester phải tự dựng và tự đếm | Lưu sẵn chuỗi nguyên văn trong file dữ liệu |
| CRM_LOGIN_TC_015 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_016 | 11/12 | 🟢 | C6 −1 | Gộp 3 hành vi: che ký tự · không có nút hiện/ẩn · chặn sao chép; mục "không có nút hiện/ẩn" đã có ở TC_001 mục `6` | Bỏ bước/Expected `4` |
| CRM_LOGIN_TC_017 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_018 | 10/12 | 🟢 | C2 −1 · C6 −1 | Expected `6` chấm PASS/FAIL theo chính sách khoá tài khoản — vùng `AMB-LOGIN-10` đã quyết không viết TC | Đổi bước 6 thành bước dọn dẹp, không chấm |
| CRM_LOGIN_TC_019 | 12/12 | 🟢 | — | Pre-Condition bảo chép mật khẩu admin ra trình soạn thảo — không trừ điểm | Thêm *"không lưu file, đóng không lưu sau khi chạy"* |
| CRM_LOGIN_TC_020 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_021 | 12/12 | 🟢 | — | Biến thể `b` trùng TC_013-a | Xem *TC trùng lặp* |
| CRM_LOGIN_TC_022 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_023 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_024 | 12/12 | 🟢 | — | Biến thể `c` (viết hoa email **không tồn tại**) không chứng minh được gì về hoa/thường | Bổ sung TC_026-b (Gap #6) |
| CRM_LOGIN_TC_025 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_026 | 11/12 | 🟢 | C2 −1 | Expected `4` chưa có nội dung chữ (`@NeedsVerify`); Priority `Medium` thấp so với luồng đặt lại mật khẩu | Điền chữ sau recon · Priority → `High` |
| CRM_LOGIN_TC_027 | 8/12 | 🟡 | C1 −1 · C2 −1 · C3 −1 · C4 −1 | Phụ thuộc TC_026 chạy trước · đổi mật khẩu `TK-TEST-03` không trả lại → chạy lần 2 hỏng · bước 4 và 6 mơ hồ / gộp nhiều thao tác | Viết lại — xem chi tiết |
| CRM_LOGIN_TC_028 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_029 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_030 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_031 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_032 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_033 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_034 | 10/12 | 🟢 | C1 −1 · C2 −1 | Bước 4 *"Đóng hộp cảnh báo"* không nói đóng bằng gì; Expected `2` chưa quan sát; timer bật trên tài khoản admin **dùng chung** làm Logout của TC khác bị chặn | Chạy bằng `TK-TEST-01` hoặc xếp cuối bộ, đưa bước dừng timer vào Steps |
| CRM_LOGIN_TC_035 | 11/12 | 🟢 | C2 −1 | Expected `5` chưa quan sát (`@NeedsVerify`) | Điền nhãn màn nhập mã sau recon |
| CRM_LOGIN_TC_036 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_037 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_038 | 12/12 | 🟢 | — | — | Có thể thêm cách ngắt mạng thay thế: DevTools → Network → `Offline` |
| CRM_LOGIN_TC_039 | 11/12 | 🟢 | C1 −1 | Bước 1, 3, 5 mỗi bước gộp 3–4 thao tác | Tách mỗi bước một thao tác |
| CRM_LOGIN_TC_040 | 10/12 | 🟢 | C1 −1 · C3 −1 | Bước 5 không bảo đóng tab hệ thống → request nền (nếu có) gia hạn phiên trượt 8 giờ; *"chưa đăng nhập"* không nói cách đạt khi profile còn cookie ghi nhớ | Bổ sung cách dọn cookie + đóng tab trong lúc chờ |
| CRM_LOGIN_TC_041 | 10/12 | 🟢 | C1 −1 · C3 −1 | Như TC_040 — chạy ngay sau TC_040 cùng profile thì cookie `autologin` còn hạn tự đăng nhập, TC FAIL oan | Như TC_040 |
| CRM_LOGIN_TC_055 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_042 | 11/12 | 🟢 | C4 −1 | Email Contact là duy nhất — chạy lần 2 tạo trùng sẽ lỗi ở Pre-Condition | Ghi *"có rồi thì dùng lại"* |
| CRM_LOGIN_TC_043 | 11/12 | 🟢 | C2 −1 | Bước 2 dùng ngôn ngữ DevTools ở phần TC chính (*"sửa giá trị ô ẩn `csrf_token_name`"*); Expected `4` chưa quan sát | Dời cách làm xuống `🔧` · ghi ứng viên Expected `4` |
| CRM_LOGIN_TC_044 | 11/12 | 🟢 | C2 −1 | Che dòng `🔧` đi thì TC chỉ còn *"Vào Dashboard"* — trùng TC_006, không còn kiểm REQ-LOGIN-15 | Ghi rõ ở Test Scenario là TC kiểm bằng DevTools |
| CRM_LOGIN_TC_045 | 10/12 | 🟢 | C1 −1 · C3 −1 | Bước 1 gộp 4 thao tác; tiền đề *"chưa đăng nhập"* như TC_040 | Tách bước 1 · bổ sung cách dọn cookie |
| CRM_LOGIN_TC_046 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_047 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_048 | 11/12 | 🟢 | C2 −1 | Bước 2 *"trong DevTools đổi kiểu ô Email từ `email` sang `text`"* nằm ở phần TC chính | Dời cách làm xuống `🔧` |
| CRM_LOGIN_TC_049 | 11/12 | 🟢 | C3 −1 | Bước 4 cần *"tên khách hàng đầu tiên trong danh sách"* — Pre-Condition không bảo đảm danh sách Customers có dữ liệu | Thêm vào Pre-Condition |
| CRM_LOGIN_TC_050 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_051 | 11/12 | 🟢 | C1 −1 | Bước 7 *"Bấm Shift+Tab, rồi bấm Enter"* — 2 thao tác, Expected `7` không nói focus sau Shift+Tab | Tách thành bước 7 và 8 |
| CRM_LOGIN_TC_052 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_053 | 12/12 | 🟢 | — | — | — |
| CRM_LOGIN_TC_054 | 11/12 | 🟢 | C1 −1 | Bước 2, 3 gộp 3–5 thao tác; *"nhập lại Password admin"* không nói phải xoá chữ cũ trong ô | Tách bước, ghi rõ xoá ô Password |

### Đề xuất sửa chi tiết

#### 🟡 CRM_LOGIN_TC_027 — 8/12 (viết lại)

| Chỗ chưa đạt (trích nguyên văn) | Vì sao | Đề xuất |
|---|---|---|
| Pre-Condition *"Đã chạy TC_026, thư đặt lại còn trong hộp thư và chưa dùng"* | C3 — TC không tự dựng tiền đề, chạy riêng (hoặc TC_026 FAIL) là BLOCKED | *"Đã có `TK-TEST-03` + hộp thư test (ASM-11). Tự gửi yêu cầu: mở `/admin/authentication/forgot_password`, nhập `qa.reset.01@mailpit.local`, bấm `Confirm`, chờ thư mới trong hộp thư test (≤ 5 phút)"* |
| Test Data *"mật khẩu mới `QaReset@2026New`"* + bước 7 *"đăng nhập lại bằng mật khẩu cũ `QaReset@2026`"*, không có bước trả lại mật khẩu | C4 — sau lần chạy đầu, mật khẩu của `TK-TEST-03` là `QaReset@2026New`; lần chạy sau bước 7 không còn "mật khẩu cũ" đúng nghĩa, và TC_026 · TC_027 lần sau làm việc trên tài khoản đã đổi | Thêm bước cuối: *"9. (Dọn dẹp — không chấm) Đăng nhập bằng mật khẩu mới → ảnh đại diện → `Edit Profile` → đổi mật khẩu về `QaReset@2026`"*. Edit Profile thuộc module `PROF`, ở đây chỉ dùng để dọn |
| Bước 4 *"Nhập mật khẩu mới vào ô mật khẩu mới (và ô xác nhận nếu có)"* | C1 — người chạy không biết ô nào, có mấy ô | Giữ `@NeedsVerify` tới khi recon, sau đó ghi đúng nhãn từng ô, mỗi ô một bước |
| Bước 6 *"Mở `/admin/authentication`, nhập Email `qa.reset.01@mailpit.local` + mật khẩu mới, bấm `Login`"* | C1 — 4 thao tác trong 1 bước | Tách: *"6. Mở `/admin/authentication` · 7. Nhập Email `qa.reset.01@mailpit.local` · 8. Nhập Password = mật khẩu mới · 9. Bấm `Login`"* (bước 7 cũ tách tương tự) |
| Expected `3` *"Mở màn đặt mật khẩu mới của hệ thống — ⚠️ chưa có evidence"* · `5` *"Có thông báo đặt mật khẩu thành công — ⚠️ chưa có evidence"* | C2 — tester không biết đối chiếu chữ gì | Sau recon: ghi tiêu đề màn và câu thông báo nguyên văn. Trước recon giữ nguyên ghi chú `⚠️` (đây là điểm trừ có lý do, không phải lỗi người viết) |

#### TC bị trừ điểm khác

| TC | Trích nguyên văn | Đề xuất sửa |
|---|---|---|
| TC_018 | Expected *"6. Vào Dashboard — tài khoản chưa bị khoá sau 4 lần sai"* nằm trong khối *"Biến thể `a`–`d` cho cùng kết quả"* | Tách khỏi khối biến thể và bỏ chấm: *"6. (Dọn dẹp — không chấm PASS/FAIL, chính sách khoá thuộc AMB-LOGIN-10) Đăng nhập bằng mật khẩu đúng. Ghi lại: vào Dashboard hay bị khoá. Bị khoá → báo người quản trị mở khoá `TK-TEST-01`"*. ASM-07 vẫn giữ để nói cách xử lý |
| TC_034 | Bước *"4. Đóng hộp cảnh báo"* · Pre-Condition *"Đăng nhập admin … bấm bắt đầu bộ đếm giờ"* · *"dọn dẹp: dừng bộ đếm giờ sau khi chạy"* (chỉ ở Pre-Condition) | (1) Bước 4 → *"Bấm nút đóng của hộp cảnh báo"* (ghi nhãn nút sau recon). (2) Thêm *"6. Mở task `QA-LOGIN-TC034-TIMER`, bấm dừng bộ đếm giờ — thanh đầu trang không còn bộ đếm nào"* vào Steps để dọn dẹp có Expected. (3) Chạy bằng `TK-TEST-01` thay vì tài khoản admin dùng chung — timer đang chạy trên admin làm mọi TC bấm `Logout` khác (TC_003, 007, 039, 045, 049, 054…) bị chặn nếu chạy cùng lúc hoặc TC_034 dừng giữa chừng. Chưa có `TK-TEST-01` thì xếp TC_034 **cuối** bộ chạy |
| TC_040 · TC_041 | Pre-Condition *"Profile Chrome riêng cho test … chưa đăng nhập"* · bước *"5. Không thao tác trên hệ thống trong 8 giờ 10 phút"* | Pre-Condition: *"Profile Chrome riêng cho test, đã xoá toàn bộ cookie của tên miền hệ thống (chrome://settings/content/all → tên miền → Xoá dữ liệu)"* — nếu không, cookie `autologin` của TC_040 làm TC_041 tự đăng nhập. Bước 5: *"Đóng mọi tab của hệ thống (giữ trình duyệt mở hoặc đóng đều được), không mở lại trong 8 giờ 10 phút"* — tab Dashboard để mở có thể gửi request nền và gia hạn phiên trượt |
| TC_045 | *"1. Mở `/admin/authentication`, nhập Email và Password admin, tích `Remember me`, bấm `Login`"* | Tách thành 4 bước, đánh lại số Expected. Pre-Condition thêm câu xoá cookie như TC_040 |
| TC_043 | *"2. Trong DevTools, sửa giá trị ô ẩn `csrf_token_name` của form thành 32 chữ số `0`"* · Expected *"4. … hiện trang/thông báo từ chối yêu cầu — ⚠️ chưa có evidence"* | Bước 2 → *"2. Thay mã chống giả mạo của form bằng mã giả (cách làm ở 🔧)"*, dời câu DevTools xuống `🔧 Ghi chú kỹ thuật`. Expected `4`: ghi ứng viên *"trang báo `The action you have requested is not allowed.`"* (cùng chữ TC_036 dùng) và xác nhận khi recon |
| TC_048 | *"2. Với biến thể `a`, `b`: trong DevTools đổi kiểu ô Email từ `email` sang `text`"* | *"2. Với biến thể `a`, `b`: tắt kiểm tra định dạng email của ô Email (cách làm ở 🔧)"* + dời câu DevTools xuống `🔧` |
| TC_044 | Expected chính *"4. Không có khung thông báo đỏ · 5. Vào Dashboard (`/admin/`)"* — toàn bộ nội dung REQ-LOGIN-15 nằm ở `🔧` | REQ-LOGIN-15 là cơ chế ẩn, hệ quả nghiệp vụ đã có ở TC_040. Giữ TC nhưng đổi Test Scenario thành *"[Security · Cookie · kiểm bằng DevTools] …"* để người lập bộ chạy biết TC này chỉ có giá trị khi giao cho tester có DevTools; ghi chú *"Hệ quả nghiệp vụ: TC_040"* |
| TC_049 | Bước *"4. Bấm vào tên khách hàng đầu tiên trong danh sách (nếu danh sách còn hiện)"* — Pre-Condition chỉ ghi *"đang ở `/admin/clients`"* | Pre-Condition thêm *"danh sách Customers có ít nhất 1 khách hàng (VD `QA Login KH042` của TC_042; chưa có thì tạo `QA Login KH049` — AMB-SYS-03)"* |
| TC_042 | Pre-Condition *"tạo khách hàng `QA Login KH042` và một Contact có email `qa.contact.login042@example.test`"* | Thêm *"Đã có Contact này từ lần chạy trước thì dùng lại, không tạo mới (email Contact không được trùng)"* |
| TC_039 | *"1. Mở `/admin/authentication`, nhập Email …, Password `Abc@12345`, bấm `Login`"* (bước 3, 5 tương tự) | Tách mỗi bước một thao tác; Expected chỉ đặt ở bước bấm `Login` / `Confirm` / gõ URL |
| TC_051 | *"7. Bấm Shift+Tab, rồi bấm Enter"* | *"7. Bấm Shift+Tab"* → Expected *"Focus về ô `Password`"* · *"8. Bấm Enter"* → *"Form được gửi, vào Dashboard (`/admin/`)"* |
| TC_054 | *"3. Xoá ô Email, nhập Email admin, nhập lại Password admin, bấm `Login`"* | *"3. Xoá chữ trong ô Email · 4. Nhập Email admin · 5. Xoá chữ trong ô Password · 6. Nhập Password admin · 7. Bấm `Login`"* |
| TC_016 | *"4. Quan sát ô Password và vùng xung quanh ô"* → *"Không có biểu tượng con mắt hay nút hiện/ẩn"* | Bỏ bước và Expected `4` — đã kiểm ở TC_001 mục `6`. TC còn lại một nhóm hành vi: ô Password che chữ và không cho lấy chữ ra |
| TC_014 | Test Data *"`a`×64 + `@` + `b`×63 + `.` + `c`×63 + `.` + `d`×53 + `.invalid`"* | Lưu 3 chuỗi nguyên văn vào `docs/testcases/login/web/data/email_dai_254_255_320.txt`, Test Data dẫn link file. Giữ công thức làm chú thích |
| TC_026 | Expected *"4. Hiện thông báo gửi yêu cầu thành công — ⚠️ chưa có evidence, nội dung chữ chưa từng quan sát"* · Priority `Medium` | Sau recon ghi câu thông báo nguyên văn. Priority → `High` (xem *Priority*). Thêm biến thể `b` viết hoa (Gap #6) |
| TC_035 | Expected *"5. Hiện bước yêu cầu nhập mã xác thực — ⚠️ chưa có evidence"* | Sau recon ghi tiêu đề, nhãn ô nhập mã, nút gửi nguyên văn |

## Đối soát loại kiểm thử (4 vòng)

> Chấm độc lập rồi so với Bảng 4 vòng của index. Dòng **in đậm** là chỗ review chấm khác index.

| Vòng | Nhánh | Index ghi | Review chấm | Ghi chú |
|---|---|---|---|---|
| 1 | UI cơ bản | ✅ | ✅ | TC_001–003 (3 TC · 11 mục Kiểu B + menu 5 mục) — đủ nhãn nguyên văn, thứ tự, trạng thái mặc định, con trỏ, không có placeholder ở cả 2 màn |
| 1 | Open form | ✅ | ✅ | TC_004 (2 biến thể) · TC_003 mở menu · TC_055 đóng menu (3 biến thể) |
| 1 | Display | ✅ | ✅ | TC_005 · TC_008 |
| 1 | Input valid data | ✅ | ✅ | TC_005 (tối thiểu) · TC_006 (đầy đủ) |
| 1 | Save | ✅ | ✅ | TC_005, 006 · TC_007 |
| 1 | Verify data | ✅ | ✅ | TC_005 bước 7 |
| 2 | UI Behavior | ✅ | ✅ | TC_016, 019, 020, 055 (4 TC · 6 biến thể) |
| 2 | Required | ✅ | ✅ | TC_008, 009, 010, 022 (4 TC · 8 biến thể) — bỏ trống từng ô + bỏ trống tất cả, ở cả 2 form |
| **2** | **Validation** | ✅ | **🟡 Nông** | TC_011–015, 017, 018, 021, 023–025 (11 TC · 45 biến thể). Hai mục field-level chỉ phủ hình thức — xem bảng 15 loại |
| 2 | Equivalence Partitioning | ✅ | ✅ | TC_013, 015, 017, 024 |
| 2 | Boundary Value Analysis | ✅ | ✅ | TC_009b-c, 014, 017a-c, 024d. Hai ô không có min/max (ASM-05) nên nhánh thực chất là kiểm độ bền với chuỗi dài — chấp nhận |
| 2 | Business Rule | ✅ | ✅ | TC_018, 021, 025, 040, 041 — mỗi rule có cả phía tuân thủ và phía ngược lại |
| 2 | Decision Table | ✅ | ✅ | R1–R9 đều có TC |
| **2** | **State Transition** | ✅ | **🟡 Nông** | S1–S10 có TC. Trạng thái S3 *"Chờ nhập mã"* (TC_035) **không có chuyển tiếp ra nào**: mã đúng → Dashboard · mã sai · bỏ ngang mở route admin (Gap #8) |
| 2 | Dependency | ✅ | ✅ | TC_040, 041, 045 |
| 2 | Use Case / Scenario | ✅ | ✅ | TC_039 · TC_026 → 027 (TC_027 🟡 về cách viết, không phải về độ phủ) |
| 2 | Save / Edit / Delete | ➖ | ➖ | Đồng ý — module không có CRUD |
| **2** | **Error Guessing** | ✅ | **🟡 Nông** | Có 2 tab · bấm đúp · mất mạng. Thiếu 3 tình huống quen thuộc của form đăng nhập máy chủ trả trang trực tiếp (requirements mục 6: POST trả 200): nạp lại trang sau lỗi · Back sau khi đăng nhập · để trang Login quá hạn mã chống giả mạo (Gap #1–3) |
| 3 | Permission | ✅ | ✅ | Hệ thống chỉ có 1 role nhân viên (AMB-LOGIN-01/02 ✅) — Admin ở TC_005, 007 · Contact × khu admin ở TC_042 |
| **3** | **Security** | ✅ | **🟡 Nông** | TC_016, 018, 028, 032, 033, 042–049 phủ tốt truy cập khi chưa đăng nhập, sau đăng xuất, Back, CSRF, cookie, SQLi/XSS. Thiếu: mã phiên đổi sau đăng nhập · `http://` tự chuyển `https://` (Gap #4, #5) |
| 3 | Security · khoá tài khoản / brute-force | ⏭️ | ⏭️ AMB-LOGIN-10 | Loại trừ theo requirements |
| 3 | API | ➖ | ➖ | Đồng ý — QA không có quyền gọi API (README, 05-11-2026) |
| 3 | Database | ➖ | ➖ | Đồng ý — README |
| 3 | Integration | ➖ | ➖ | Đồng ý — README; TC_026/027 phụ thuộc hộp thư test đã ghi ở ASM-11 |
| 3 | Logging / Audit | ➖ | ➖ | Đồng ý — không có yêu cầu nhật ký, trang nhật ký bị chặn |
| 4 | Compatibility | ✅ | ✅ · **lỗi ghi nhãn** | TC_054 (Edge, Firefox) đủ. Phần *"Không kiểm Safari, trình duyệt di động (ASM-13)"* là `⏭️` (có thứ đó, quyết định không kiểm) nhưng đang nằm trong ô ✅ và thiếu **ai quyết + điều kiện rà lại** → tách thành dòng `⏭️` riêng, VD *"Quyết định: PO, <ngày>. Rà lại khi có người dùng macOS/iOS"* |
| 4 | Responsive / UI Stability | ✅ | ✅ | TC_053 (5 biến thể) |
| **4** | **Accessibility** | ✅ | **🟡 Nông** | TC_050–052: Tab · Enter/Space · viền focus ✅. Thiếu mục *"ảnh có văn bản thay thế"* của checklist — logo `ANHTESTER` là ảnh bấm được ở cả 2 màn (Gap #9) |
| 4 | Performance | ➖ | ➖ | Đồng ý — không có ngưỡng cam kết |
| 4 | Regression | ➖ | ➖ | Đồng ý — chưa có `docs/bugs/login/` |
| 4 | E2E | ➖ | ➖ | Đồng ý — chưa có module thứ hai được đặc tả |

## Đối soát bảng 15 loại field

| Field | Màn | Loại | Index ghi | Review chấm | Mục thiếu / nông |
|---|---|---|---|---|---|
| Email Address | Login | Email | 9/9 | **8/9 · 🟡** | **Ký tự đặc biệt trước `@`**: mới có ký tự **được phép** (`+` ở 013b; `'` `=` `#` ở 046) — chưa có ký tự **bị chặn** (`(` `)` `,` `<` `>` `\`) để biết trình duyệt chặn đúng → Gap #7. Các mục còn lại đạt |
| Password | Login | Password | 7/7 | 7/7 ✅ | — (3 mục chính sách độ mạnh `➖` có lý do đúng: form đăng nhập không áp chính sách) |
| Remember me | Login | Checkbox | 4/4 | 4/4 ✅ | — |
| Email Address | Forgot Password | Email | 9/9 | **8/9 · 🟡** | **Hoa/thường**: TC_024-c viết hoa một email **không tồn tại** — kết quả `Email not found` xảy ra dù hệ thống có phân biệt hoa/thường hay không, nên biến thể không trả lời được câu hỏi. Cần email **tồn tại** viết hoa → Gap #6 |
| Ô nhập mã 2FA | Bước nhập mã | OTP / MFA Code | không liệt kê | ⚠️ chưa liệt kê | Field có thật theo REQ-LOGIN-32 nhưng màn chưa recon — liệt kê vào bảng field của index với trạng thái *"chờ recon"* (Gap #8) |

## Coverage Gaps (TC còn thiếu)

| # | Kịch bản thiếu | Vòng / Nhánh | Priority đề xuất |
|---|---|---|---|
| 1 | Đăng nhập lỗi (VD `recon.khongtontai@example.invalid` / `Abc@12345`) rồi bấm F5 → trình duyệt hỏi gửi lại biểu mẫu; chọn gửi lại → vẫn ở trang Login, đúng **một** khung `Invalid email or password`, không vào Dashboard. Áp tương tự cho Forgot Password. Hành vi chưa quan sát → `@NeedsVerify` | V2 · Error Guessing | Medium |
| 2 | Đăng nhập đúng, tới Dashboard rồi bấm Back của trình duyệt → không hiện lại form Login còn chữ đã gõ; bị đưa về Dashboard (hệ quả REQ-LOGIN-12) | V2 · Error Guessing | Medium |
| 3 | Mở trang Login, để yên quá hạn cookie chống giả mạo (≈ 1 giờ trượt — requirements mục 7), rồi nhập đúng tài khoản và bấm `Login` → ghi nhận người dùng thấy gì (trang từ chối hay đăng nhập được). Đây là phiên bản **không cần DevTools** của TC_043 và là tình huống người dùng gặp thật | V2 · Error Guessing | Medium |
| 4 | Mã phiên đổi sau khi đăng nhập: 🔧 so cookie `sp_session` trước và sau bấm `Login` — **khác nhau** (chỉ so, không chép giá trị). `@TechCheck`. Chưa có REQ — bổ sung REQ khi recon | V3 · Security | Medium |
| 5 | Gõ địa chỉ trang Login bằng `http://` → trình duyệt tự chuyển sang `https://`, thanh địa chỉ có biểu tượng ổ khoá, form hiện bình thường. Requirements mục 7 đã quan sát *"Toàn bộ qua HTTPS"* nhưng chưa thành REQ | V3 · Security | Medium |
| 6 | Forgot Password với email **tồn tại** viết hoa `QA.RESET.01@MAILPIT.LOCAL` → cùng kết quả như chữ thường (thông báo thành công, có thư). Thêm làm biến thể `b` của TC_026 (cần `TK-TEST-03` + hộp thư test) | V2 · Validation (Email Forgot · hoa/thường) | Medium |
| 7 | Email Login chứa ký tự không hợp lệ trước `@`: `qa(login)@example.invalid` → trình duyệt chặn, trang không nạp lại. Thêm làm biến thể `f` của TC_012 (5 → 6 biến thể, đúng trần) | V2 · Validation (Email Login · ký tự đặc biệt) | Low |
| 8 | Bước nhập mã 2FA (sau TC_035): mã đúng → vào Dashboard · mã sai → báo lỗi, chưa vào Dashboard · đang chờ mã mà mở thẳng `/admin/` → về trang Login. Cần recon bằng `TK-TEST-02a/b` và bổ sung REQ — REQ-LOGIN-32 hiện dừng ở *"hiện bước nhập mã"* | V2 · State Transition (S3) + Field OTP/MFA | Medium |
| 9 | Logo `ANHTESTER` ở trang Login và Forgot Password có văn bản thay thế mô tả được (🔧 đọc thuộc tính `alt`). `@TechCheck`. Gộp được vào TC_050 dưới `🔧` | V4 · Accessibility | Low |

## TC trùng lặp — đề xuất xử lý

| TC | Trùng với | Đề xuất |
|---|---|---|
| CRM_LOGIN_TC_021-b | CRM_LOGIN_TC_013-a | Cùng dữ liệu (`recon.khongtontai@example.invalid` / `Abc@12345`), cùng bước, cùng Expected — TC_013 Expected `5` đã khẳng định *"ô Email và ô Password đều trống"*. **Không** `@Deprecated` TC nào (TC_021 là TC duy nhất của REQ-LOGIN-08). Bỏ biến thể `b` của TC_021, ghi trong Expected: *"Biến thể sai thông tin đã kiểm ở TC_013-a (Expected 5) — bỏ 10-11-2026 do trùng"* |
| CRM_LOGIN_TC_016 bước 4 | CRM_LOGIN_TC_001 mục `6` | Cùng kiểm *"không có nút hiện/ẩn mật khẩu"* → bỏ khỏi TC_016 (đã nêu ở bảng trên) |
| CRM_LOGIN_TC_044 (phần chính) | CRM_LOGIN_TC_006 | Steps 1–5 và Expected chính giống nhau, chỉ khác `🔧`. Trùng có chủ đích (khác REQ, TC_044 là TC 🟢 duy nhất của REQ-LOGIN-15) → giữ cả hai. Trong *Bộ chạy đề xuất*, tester có DevTools chạy TC_044 là đủ phủ TC_006 |

## Priority

| TC | Hiện tại | Đề xuất | Lý do |
|---|---|---|---|
| CRM_LOGIN_TC_026 | Medium | **High** | Luồng đặt lại mật khẩu là đường lấy lại quyền truy cập, `Risk Level` cột đã `High`, module chấm rủi ro `Cao`. BLOCKED vì thiếu hộp thư không phải lý do hạ Priority |
| CRM_LOGIN_TC_027 | Medium | **High** | Như trên — mật khẩu cũ còn dùng được sau khi đặt lại là lỗi bảo mật |

Các Priority còn lại hợp lý với rủi ro: luồng sống còn `Critical` (TC_005, 007), validation/bảo mật `High`, Responsive `Low`.

## Vấn đề mức bộ TC (rubric không bắt được)

1. **Trạng thái dùng chung làm TC FAIL oan khi chạy lại / chạy song song** — ba ổ:
   - Timer của TC_034 bật trên tài khoản admin dùng chung → mọi TC bấm `Logout` bị chặn (xem TC_034)
   - Profile Chrome riêng dùng chung cho TC_040 → 041 → 045: cookie ghi nhớ của TC_040 phá tiền đề *"chưa đăng nhập"* của TC_041 (xem TC_040/041)
   - Mật khẩu `TK-TEST-03` bị TC_027 đổi mà không trả lại (xem TC_027)

   → Index thêm mục **Bộ chạy đề xuất** ghi thứ tự: TC_034 cuối bộ, TC_040/041/045 mỗi TC dọn cookie trước khi chạy.
2. **Mật khẩu tài khoản test ghi thẳng trong tài liệu** (ASM-02, ASM-11 và TC_015, 018, 026, 027, 035) trong khi tài khoản admin dùng biến `.env`. Hiện là giá trị *dự kiến*; khi được cấp thật nên chuyển sang biến `.env` (VD `TK_TEST_01_PASSWORD`) và TC ghi tên biến — cùng quy ước 🔒 với admin.
3. **Lệch số liệu nhỏ:** Part 01 dòng tiêu đề Vòng 2b ghi *"Bảng chuyển trạng thái phiên (S1–S9)"* trong khi index có S1–**S10** → sửa thành `S1–S10`.
4. **Bước gộp 2 thao tác** (*"Nhập Email và Password admin"* ở TC_029, 036, 038, 040, 041, 043, 044) — chấp nhận, không trừ điểm; chỉ trừ ở bước gộp từ 3 thao tác trở lên.

## Kết luận & Khuyến nghị

1. **Viết lại TC_027** theo bảng đề xuất: tự gửi yêu cầu đặt lại trong Pre-Condition, tách bước, thêm bước trả mật khẩu về `QaReset@2026`. Nâng TC_026, TC_027 lên Priority `High`.
2. **Khử trạng thái dùng chung** ở TC_034, TC_040, TC_041, TC_045 (đổi tài khoản / dọn cookie / đóng tab trong lúc chờ) và ghi thứ tự chạy vào index — đây là nguồn FAIL oan lớn nhất khi bộ TC bắt đầu được chạy.
3. **Bổ sung 3 TC Error Guessing** (Gap #1–3) và **2 TC Security** (Gap #4–5) — nối tiếp từ `CRM_LOGIN_TC_056`; Gap #4, #5 cần bổ sung REQ trước qua `/update-requirements-from-ticket`.
4. **Thêm biến thể** TC_012-f (Gap #7) và TC_026-b (Gap #6); bỏ TC_021-b và bước 4 của TC_016 (trùng).
5. **Dọn ngôn ngữ DevTools ở phần TC chính** của TC_043, TC_048 xuống `🔧`; tách dòng `⏭️` Safari/di động ở nhánh Compatibility kèm người quyết và điều kiện rà lại. Recon màn 2FA để mở Gap #8.

## Kết quả Mode FIX (10-11-2026)

- **Lệnh:** `/review-testcases FIX docs\testcases\login\web` — bộ TC không đổi kể từ lần review (`git diff 752c90a HEAD` rỗng) nên dùng lại báo cáo này làm checkpoint
- **Duyệt ở checkpoint:** user chọn cả 4 nhóm A · B · C · D
- **Mốc git trước khi sửa:** `752c90a` (part 01, part 02, index) — xem bản cũ bằng `git show 752c90a:<đường dẫn file>`
- **Sửa tại chỗ**, cùng tên file, không sinh bản sao. Không TC nào `@Deprecated`, không đánh lại số

| Nhóm | TC | Đã làm |
|---|---|---|
| A · Viết lại 🟡 | TC_027 | Pre-Condition tự gửi yêu cầu đặt lại (bỏ phụ thuộc TC_026) · tách bước 6–7 cũ thành 7–14 · thêm bước 15 dọn dẹp trả mật khẩu `TK-TEST-03` về `QaReset@2026` (ASM-27) · Priority → High |
| A | TC_026 | Priority → High · thêm biến thể `b` viết hoa (Gap #6, ASM-23) |
| B · Trạng thái dùng chung | TC_034 | Chạy bằng `TK-TEST-01` (chưa có thì xếp cuối bộ) · bước 4 *"Bấm nút đóng của hộp cảnh báo"* · bước 6 dừng timer có Expected |
| B | TC_040, 041 | Pre-Condition xoá cookie tên miền hệ thống · bước 5 đóng mọi tab trong lúc chờ |
| B | TC_045 | Tách bước 1 thành 4 bước, đánh lại số Expected/🔧 · Pre-Condition xoá cookie |
| B | Index | Thêm mục **Bộ chạy đề xuất** (6 nhóm, TC_034 cuối bộ, profile riêng chạy tuần tự) |
| C · Cách viết | TC_001, 002 | *"kết thúc bằng"* → *"có chữ"* `- Login` |
| C | TC_014, 024-d | Chuỗi dài lưu nguyên văn ở [`web/data/email_dai_254_255_320.txt`](../web/data/email_dai_254_255_320.txt) (254 / 255 / 320 ký tự — đã đếm lại) |
| C | TC_016 | Bỏ bước/Expected kiểm nút hiện/ẩn (trùng TC_001 mục `6`) |
| C | TC_018 | Bước 6 thành bước dọn dẹp không chấm, tách khỏi khối biến thể |
| C | TC_021 | Bỏ biến thể `b` (trùng TC_013-a), lý do ghi trong Expected |
| C | TC_039, 051, 054 | Tách bước mỗi bước một thao tác, Expected theo số bước mới |
| C | TC_042, 049 | Pre-Condition: dùng lại Contact có sẵn · danh sách Customers có ≥ 1 khách hàng |
| C | TC_043, 048 | Câu thao tác DevTools dời xuống `🔧` · TC_043 Expected `4` ghi ứng viên chữ trang từ chối |
| C | TC_044 | Test Scenario ghi rõ *"kiểm bằng DevTools"*, hệ quả nghiệp vụ ở TC_040 |
| C | Part 01 · index | `S1–S9` → `S1–S10` · tách dòng `⏭️` Compatibility (Safari, di động) kèm người quyết + điều kiện rà lại · liệt kê field OTP/MFA *chờ recon* |
| D · Gap | TC_056 · 057 · 058 | **TC mới** Error Guessing — Gap #1 (F5 gửi lại biểu mẫu, phần trang Login), #2 (Back sau đăng nhập), #3 (trang Login quá hạn mã chống giả mạo). Cả 3 `@NeedsVerify` (ASM-24 → 26) |
| D | TC_012-f | Gap #7 — `qa(login)@example.invalid` (6 biến thể, đúng trần) |
| D | TC_050, 052 | Gap #9 — `alt` logo ở `🔧`, tag `@TechCheck` |

**Sau khi sửa:** 58 TC · 129 biến thể (88 ở 26 TC có Bảng biến thể + 30 TC đơn + 11 mục Kiểu B). Field Email Login, Email Forgot đạt 9/9 thật. Đối soát 4 vòng ở index: Validation · Error Guessing · Accessibility → ✅; **State Transition và Security ghi 🟡** vì phần còn thiếu chưa có REQ.

**Chưa làm — cần bổ sung REQ / recon trước:**

| Gap | Lý do chưa viết TC | Đường xử lý |
|---|---|---|
| #4 Mã phiên đổi sau đăng nhập | Chưa có REQ | `/update-requirements-from-ticket` → `/update-testcases-from-impact` |
| #5 `http://` tự chuyển `https://` | Requirements mục 7 có quan sát nhưng chưa thành REQ | Như trên |
| #8 Chuyển tiếp ra khỏi bước nhập mã 2FA | Màn chưa recon, REQ-LOGIN-32 dừng ở *"hiện bước nhập mã"* | Recon bằng `TK-TEST-02a/b`, bổ sung REQ |
| #1 phần Forgot Password | F5 sau lỗi ở trang Forgot — khác form, khác thông báo nên không gộp vào TC_056 (bảng CẤM gộp); giá trị thấp | Thêm TC riêng nếu PO cần |
| Vấn đề mức bộ #2 — mật khẩu test ghi thẳng trong tài liệu | Giá trị còn là *dự kiến* | Chuyển sang biến `.env` khi được cấp thật |
