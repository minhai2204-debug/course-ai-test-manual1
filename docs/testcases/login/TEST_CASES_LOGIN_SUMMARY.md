# Test Cases — Đăng nhập (`LOGIN`) (tổng 84 TC · 1 nền tảng)

> **INDEX module — tên file bất biến, không chứa dòng TC.** TC chi tiết nằm ở file nền tảng — mỗi nền tảng **một file duy nhất** (xem **Bản đồ tài liệu**).
> ← [Danh mục test cases](../README.md) · Requirements: [`REQUIREMENTS_LOGIN_SUMMARY.md`](../../requirements/login/REQUIREMENTS_LOGIN_SUMMARY.md)

| Thông tin | Nội dung |
|---|---|
| **Nguồn requirement** | [`REQUIREMENTS_LOGIN_SUMMARY.md`](../../requirements/login/REQUIREMENTS_LOGIN_SUMMARY.md) · [`web/requirements_login_web.md`](../../requirements/login/web/requirements_login_web.md) — `REQ-LOGIN-01` → `REQ-LOGIN-47` (bản 11-11-2026 — ticket `LOGIN-LOCKOUT-11112026` + Assumption tạm, chưa commit; bản trước: 05-11-2026, git `cb8ea3a`) |
| **Hệ thống · prefix** | `CRM` — Perfex CRM 3.1.6, khu admin · TC ID `CRM_LOGIN_TC_NNN` |
| **Dải TC ID đã dùng** | `CRM_LOGIN_TC_001` → `CRM_LOGIN_TC_084` — chung mọi nền tảng. TC kế tiếp: `CRM_LOGIN_TC_085` |
| **Nền tảng** | Web ✅ 84 TC · Android — chưa có requirements · iOS — chưa có · API — chưa có |
| **Mode · độ hạt** | QUICK (`/generate-testcases-from-requirements`) · **GỘP** — **84 TC · 156 biến thể** (91 biến thể ở 28 TC có Bảng biến thể + 54 TC đơn + 11 mục Bảng kiểm Kiểu B ở TC_001, TC_002). TC_060 → 071 sinh ở chế độ **BỔ SUNG** 11-11-2026 · TC_072 → 084 (kiểm CSDL) sinh ở chế độ **BỔ SUNG** 14-11-2026 |
| **Mức rủi ro · độ sâu** | `Cao` → **Đầy đủ** — V1 đủ 6 nhánh, V2 mọi nhánh có điều kiện kích hoạt, V3/V4 đủ nhánh trong giới hạn năng lực QA.<br>Căn cứ chấm Cao: đụng **xác thực** · là **cổng vào** mọi module (hỏng là chặn cả đợt kiểm thử) · có cookie ghi nhớ và luồng đặt lại mật khẩu.<br>**Rà lại độ sâu khi:** có thêm role nhân viên (AMB-LOGIN-01/02 mở lại) → mở rộng Permission theo role · khoá tài khoản đã chốt theo ticket `LOGIN-LOCKOUT-11112026` (REQ-LOGIN-35 → 47) → sinh TC ở lượt BỔ SUNG, dùng tài khoản Project Manager · QA được cấp hộp thư test / quyền API / CSDL → mở nhánh Integration · API · Database |
| **Phạm vi REQ** | **47/47 REQ có TC.** STORY-LOGIN-06 (REQ-LOGIN-35 → 47 — khoá tài khoản, ⚪ chưa kiểm chứng) phủ bởi TC_060 → 071 (mục Vòng 2c + 3b của file web, sinh bổ sung 11-11-2026) — chạy được khi có tài khoản Project Manager. Không REQ nào bị loại khỏi phạm vi. REQ ⚪ (16, 23, 24, 29 → 34) viết theo **Assumption tạm** (AMB ⏭️ 05-11-2026) — TC gắn tag `@assumption-based`. Ngoài phạm vi theo requirements: cổng khách hàng `/clients/*` · validation chi tiết màn đặt mật khẩu mới · cấu hình 2FA (module `PROF`) · cấu hình chính sách đăng nhập (module `SETTING`) · **Kiểm CSDL (14-11-2026):** TC_072 → 084 (`@DBCheck`, mục Vòng 3c) bổ sung kiểm dữ liệu cho 13 REQ đã có TC (09, 15, 23, 24, 28, 33, 35, 39, 43, 44, 45, 46, 47) — tên bảng/cột giữ chỗ, chạy được khi có kết nối CSDL (AMB-SYS-05) |
| **Ngày sinh** | 09-11-2026 |

## Bản đồ tài liệu

| Nền tảng | File | Nhóm chức năng | Số TC | TC ID | REQ bao phủ |
|---|---|---|---|---|---|
| Web | [web/test_cases_login_web.md](web/test_cases_login_web.md) | V1 Smoke · V2a form Login · V2b Forgot Password, phiên & điều hướng, ghi nhớ, đoán lỗi, kịch bản · V2c khoá tài khoản (ngưỡng, thông báo, thời hạn, bộ đếm) · V3a phân quyền & bảo mật · V3b khoá tài khoản (CSRF, khoá theo email, khoá ở mọi IP) · V3c kiểm CSDL (`@DBCheck` — mật khẩu băm, ghi nhớ đăng nhập, bộ đếm khoá, mã đặt lại) · V4 bàn phím, responsive, đa trình duyệt | 84 | 001–084 | REQ-LOGIN-01 → 47 |
| Web — dữ liệu | [web/data/email_dai_254_255_320.txt](web/data/email_dai_254_255_320.txt) | Chuỗi email 254 / 255 / 320 ký tự, mỗi dòng một chuỗi | — | 014, 024 | — |

> Web: **một file duy nhất** cho toàn bộ TC (quy ước từ 14-11-2026 — không tách part). 3 part cũ (`part_01_web_chuc_nang` · `part_02_web_ky_thuat_phi_chuc_nang` · `part_03_web_khoa_tai_khoan`) đã gộp nguyên văn ngày 14-11-2026: Part 01 → Vòng 1 · 2a · 2b · Part 03 → Vòng 2c · 3b · Part 02 → Vòng 3a · 4. Nhóm khoá tài khoản giữ quy ước riêng (tài khoản Project Manager, chạy tuần tự) ở bảng đầu mục Vòng 2c.

## Assumptions

Không có xung đột giữa tài liệu requirements và ảnh evidence — 10/10 ảnh khớp mô tả chữ (nhãn, thứ tự, thông báo, trạng thái focus). Mọi giả định dưới đây là điểm requirements **chưa nói tới**, không phải điểm mâu thuẫn.

| Mã | Điểm chưa rõ | Giả định đã áp dụng | TC bị ảnh hưởng |
|---|---|---|---|
| ASM-01 | Địa chỉ hệ thống và tài khoản admin | Lấy từ `.env` (`URL`, `EMAIL_ADMIN`, `PASSWORD_ADMIN`) — 🔒 không chép giá trị vào tài liệu (theo `docs/requirements/README.md`) | Mọi TC |
| ASM-02 | Tài khoản test riêng cho case cần email **tồn tại** (sai mật khẩu, 2FA). Tài khoản `.env` không vào được module Staff (AMB-SYS-01) nên QA không tự tạo được | Người quản trị hệ thống cấp: `TK-TEST-01` = `qa.login.rieng01@example.test` / `QaLogin@2026` (không 2FA) · `TK-TEST-02a` = `qa.login.2fa.email@example.test` / `Qa2fa@2026` (2FA qua Email) · `TK-TEST-02b` = `qa.login.2fa.ga@example.test` / `Qa2fa@2026` (Google Authenticator). Giá trị là **dự kiến** — chưa cấp thì TC BLOCKED | TC_015, 018, 035 · TC_034 (ưu tiên — chưa có thì chạy bằng admin, xếp cuối bộ) |
| ASM-03 | Requirements chỉ kiểm chứng biến thể `abc` của định dạng email | Các biến thể còn lại theo luật kiểm `type=email` chuẩn HTML của Chrome: chặn khi thiếu `@`/tên miền/phần trước `@`, nhiều `@`, có dấu cách, ký tự lạ trong tên miền, chữ có dấu trước `@`, ký tự ngoài tập cho phép trước `@` (`(` `)` `,` `<` `>` `\`); **cho qua** `a@localhost`, dấu `+` `'` `=` `#`, chữ hoa, tên miền tiếng Việt (chỉ khi **gõ tay** — Chrome đổi sang punycode). **Máy chủ kiểm định dạng riêng, chặt hơn trình duyệt** (quan sát `run_1794303621`, 10-11-2026): tên miền không có dấu chấm (`qa.login@localhost`) và chuỗi không phải email (`<script>…`) bị trả `The Email Address field must contain a valid email address.` — ở cả form Login và Forgot Password | TC_011–013, 023, 024, 048, 054, 059 |
| ASM-04 | Ô chỉ toàn khoảng trắng | Trình duyệt tự bỏ khoảng trắng đầu/cuối của ô `type=email` → coi như trống. Máy chủ coi Password toàn khoảng trắng là trống → báo bắt buộc nhập | TC_009b-c, 010b, 022b |
| ASM-05 | Không có `maxlength` ở cả hai form | Email/Password rất dài vẫn gửi được, **không** lỗi hệ thống. Form Login: máy chủ giới hạn email **≤ 254 ký tự** — 254 trả thông báo chung, từ 255 trả `The Email Address field must contain a valid email address.` (quan sát `run_1794303621`). Form Forgot: 254 ký tự trả `Email not found`; 255 trở lên chưa quan sát. Password 1024 ký tự vẫn trả thông báo chung | TC_014, 017, 024d |
| ASM-06 | Email tài khoản tồn tại có phân biệt hoa/thường, có bỏ khoảng trắng không | Không phân biệt hoa/thường; khoảng trắng đầu/cuối bị trình duyệt bỏ → đăng nhập thành công | TC_015 |
| ASM-07 | Mật khẩu phân biệt hoa/thường? Ngưỡng khoá tài khoản | Mật khẩu phân biệt hoa/thường và tính cả dấu cách. Ngưỡng khoá đã chốt (ticket `LOGIN-LOCKOUT-11112026`, 11-11-2026): **5 lần** sai liên tiếp cùng email → khoá 15 phút (REQ-LOGIN-35, 36); đăng nhập đúng trước đó đưa bộ đếm về 0 (REQ-LOGIN-39). TC_018 bắt đầu bằng 1 lần đăng nhập đúng, gửi đúng 4 lần sai → **chưa** khoá. Bước 6 là bước **dọn dẹp, không chấm** — bị khoá thì ghi nhận lệch so với REQ-LOGIN-35, chờ 15 phút rồi dọn | TC_018 |
| ASM-08 | Dán vào ô nhập / sao chép từ ô mật khẩu | Cho dán vào cả hai ô; trình duyệt chặn sao chép từ ô mật khẩu | TC_016, 019 |
| ASM-09 | Bấm vào chữ `Remember me` có tích ô không | Có — nhãn gắn với ô tích | TC_020 |
| ASM-10 | Requirements chỉ kiểm `/admin/` và `/admin/clients` | Mọi route admin khác (`/admin/invoices`, `/admin/projects`) được bảo vệ giống hệt | TC_028c-d |
| ASM-11 | Hộp thư test cho luồng đặt lại mật khẩu (AMB-LOGIN-13) — README ghi QA chưa có hộp thư test | DevOps cấp hộp thư đọc được (VD Mailpit) và người quản trị cấp `TK-TEST-03` = `qa.reset.01@mailpit.local` / `QaReset@2026`. Chưa có → TC BLOCKED | TC_026, 027 |
| ASM-12 | Danh sách kích thước màn hình (requirements chỉ khảo sát 1598×790) | Chốt 1920×1080 · 1366×768 · 768×1024 · 375×812 · 1366×768 phóng to 200% | TC_053 |
| ASM-13 | Cam kết trình duyệt (requirements chỉ khảo sát Chrome 146) | Chrome (mọi TC) + Edge và Firefox bản ổn định mới nhất (luồng chính). **Không** kiểm Safari, trình duyệt di động | TC_054 |
| ASM-14 | Thứ tự Tab trang Forgot Password chưa ghi trong requirements | Logo → Email Address → Confirm | TC_052 |
| ASM-15 | Cách làm phiên chính hết hạn | Cookie phiên `sp_session` hạn 8 giờ trượt (requirements mục 7) → đóng mọi tab của hệ thống, chờ 8 giờ 10 phút, hoặc xoá riêng cookie này trong DevTools. Chạy trên profile Chrome riêng (ẩn danh đóng là mất cookie); **xoá toàn bộ cookie của tên miền hệ thống trước mỗi TC** — cookie `autologin` còn hạn của TC trước làm TC sau tự đăng nhập | TC_040, 041, 045 |
| ASM-16 | Bấm gửi hai lần liên tiếp | Chỉ một lần xử lý có hiệu lực; không hiện trang từ chối yêu cầu | TC_036, 037 |
| ASM-17 | Đăng xuất ở một tab có huỷ phiên ở tab khác | Có — phiên bị huỷ phía máy chủ (hệ quả của REQ-LOGIN-27) | TC_033 |
| ASM-18 | Sửa mã chống giả mạo trước khi gửi form | Máy chủ từ chối yêu cầu, không đăng nhập. Nội dung trang từ chối chưa quan sát | TC_043 |
| ASM-19 | Email bị hiện lại ở trang Forgot Password (REQ-LOGIN-22) có được mã hoá ký tự đặc biệt không | Có — chuỗi hiện lại dưới dạng chữ, không chạy được script (xác nhận ở biến thể `a`, `run_1794303621`). Chuỗi không phải email bị máy chủ báo lỗi định dạng (ASM-03) **trước** khi tra email, nên khung đỏ là thông báo định dạng chứ không phải `Email not found`. Chuỗi chứa `<img … onerror=` bị máy chủ web trả trang `403 Forbidden` — chờ DevOps/PO xác nhận | TC_048 |
| ASM-20 | Nút Back sau khi đăng xuất | Trình duyệt có thể hiện lại ảnh cũ của trang; mọi thao tác tiếp theo đều bị đưa về trang Login | TC_049 |
| ASM-21 | REQ ⚪ chưa ai quan sát (16, 23, 24, 29 → 34) | Dùng nguyên **Assumption tạm** của AMB-LOGIN-03, 11 → 15, 17, 18 (user chốt 05-11-2026). Câu trả lời thật khác đi → sửa TC qua `/update-testcases-from-impact` | TC_010, 018, 026, 027, 034, 035, 040, 041, 042 |
| ASM-22 | Cách đóng menu ảnh đại diện | Đóng được bằng bấm ra ngoài, bấm lại ảnh đại diện, phím Esc | TC_055 |
| ASM-23 | Forgot Password với email **tồn tại** viết khác hoa/thường | Không phân biệt hoa/thường (như ASM-06 ở trang Login) — vẫn báo thành công và gửi thư tới hộp thư của tài khoản | TC_026b |
| ASM-24 | Nạp lại trang (F5) sau khi đăng nhập sai, đồng ý gửi lại biểu mẫu | Xử lý như một lần đăng nhập sai bình thường: vẫn một khung `Invalid email or password`, không trang từ chối mã chống giả mạo | TC_056 |
| ASM-25 | Bấm Back ngay sau khi đăng nhập thành công | Trình duyệt tải lại trang Login từ máy chủ, REQ-LOGIN-12 đưa về Dashboard — không hiện lại ảnh cũ của form | TC_057 |
| ASM-26 | Trang Login để quá hạn cookie chống giả mạo (≈ 1 giờ trượt — requirements mục 7) | Máy chủ từ chối như TC_043; mở lại trang Login thì đăng nhập bình thường | TC_058 |
| ASM-28 | Email **không tồn tại** gửi sai nhiều lần có bị đếm vào bộ đếm khoá không (AMB-LOGIN-23 — user chốt ⏭️ 11-11-2026, không có hành vi giả định) | Chưa biết → mỗi TC một email không tồn tại riêng (`recon.khongtontai.tc<NNN>[biến thể]@example.invalid`); TC gửi sai từ 4 lần/lượt dùng email riêng cho **từng biến thể**. Gửi Password trống không tính là lần sai (REQ-LOGIN-44) nên TC_009, 021 giữ email chung | TC_013, 017, 039, 047, 056 |
| ASM-29 | Tài khoản và đồng hồ cho TC khoá tài khoản (TC_060 → 071) | Người quản trị cấp `TK-PM-1`, `TK-PM-2` (role Project Manager — Assumption tạm AMB-LOGIN-24), chỉ dành cho kiểm thử, lưu ở `.env` (`EMAIL_PM_1` / `PASSWORD_PM_1` · `EMAIL_PM_2` / `PASSWORD_PM_2`). Mốc T đo bằng đồng hồ máy của tester lúc bấm `Login` lần sai thứ 5; chờ thêm **1 phút biên an toàn** (T + 16) vì đồng hồ máy và máy chủ có thể lệch nhau. Chưa cấp tài khoản → TC BLOCKED | TC_060 → 071 |
| ASM-27 | Trả mật khẩu `TK-TEST-03` về giá trị cũ sau TC_027 | Đổi được ở `Edit Profile` (module `PROF`), hệ thống không cấm dùng lại mật khẩu cũ. Bị cấm → người quản trị đặt lại | TC_027 |
| ASM-30 | Tên bảng / cột CSDL và múi giờ lưu thời gian — chưa có kết nối CSDL, chưa khảo sát schema (AMB-SYS-05) | Khối 🗄️ dùng tên giữ chỗ (bảng quy ước đầu mục Vòng 3c); TC mang `@NeedsVerify`. Khảo sát xong → điền tên thật, ghi mục *Ánh xạ dữ liệu* của requirements LOGIN, gỡ tag | TC_072 → 084 |
| ASM-31 | Requirements không nói cách lưu mật khẩu và việc ghi thời điểm đăng nhập gần nhất | Mật khẩu lưu dạng băm có tiền tố thuật toán (thông lệ bảo mật); đăng nhập đúng cập nhật thời điểm đăng nhập gần nhất. Neo tạm REQ-LOGIN-09 / 24 — **đề xuất bổ sung REQ** qua `/update-requirements-from-ticket` | TC_072, 073, 084 |

## Kỹ thuật thiết kế đã áp dụng

### Danh sách field & đối soát bảng Field-Level (15 loại)

| Field | Màn | Loại | Mục của bảng — đối soát | TC |
|---|---|---|---|---|
| Email Address | Login | Email | **9/9** · format hợp lệ ✅ 013a · thiếu `@` ✅ 011a · thiếu tên miền ✅ 011b · tên miền không hợp lệ ✅ 012c-d (trình duyệt chặn) · 059 (máy chủ chặn) · nhiều `@` ✅ 012a · ký tự đặc biệt trước `@` ✅ 013b, 046 (được phép) · 012f (bị chặn) · max length ✅ 014 (biên 254/255 của máy chủ) · hoa/thường ✅ 013c, 015a-c · email tồn tại — form đăng nhập không có ràng buộc "duy nhất"; đối soát thay bằng **tồn tại / không tồn tại** ✅ 013 ↔ 015, 018 · *bổ sung:* bắt buộc 008, 010 · khoảng trắng 010b, 013e · SQLi 046 | 008, 010–015, 046, 059 |
| Password | Login | Password | **7/7** · min/max length ✅ 017a-c · yêu cầu ký tự đặc biệt ➖ · yêu cầu hoa/thường ➖ · yêu cầu số ➖ — *form đăng nhập không áp chính sách độ mạnh; chính sách nằm ở màn đặt mật khẩu mới (ngoài phạm vi)*. Thay vào đó kiểm **phân biệt hoa/thường** ✅ 018b · copy-paste ✅ 016, 019 · hiện/ẩn ✅ 001 mục `6` (xác nhận **không có** nút) · confirm password ➖ — form không có ô xác nhận · *bổ sung:* bắt buộc 009 · khoảng trắng 009b-c, 017f · Unicode/emoji 017d-e · SQLi/XSS 047 | 009, 016–019, 047 |
| Remember me | Login | Checkbox | **4/4** · mặc định ✅ 001 (mục 3) · tích/bỏ tích ✅ 020, 051 · required ➖ — không bắt buộc, đăng nhập không tích vẫn được (005) · nhóm radio ➖ — chỉ một ô tích độc lập | 001, 005, 020, 051 |
| Email Address | Forgot Password | Email | **9/9** · format hợp lệ ✅ 024a · thiếu `@` ✅ 023a · thiếu tên miền ✅ 023b · tên miền không hợp lệ ✅ 023f · nhiều `@` ✅ 023d · ký tự đặc biệt trước `@` ✅ 024b · max length ✅ 024d · hoa/thường ✅ 026b (email **tồn tại** viết hoa) · 024c · email tồn tại ✅ 024 ↔ 026 · *bổ sung:* trống/khoảng trắng 022 · giữ giá trị 025 · XSS/SQLi 048 | 022–026, 048 |
| Ô nhập mã 2FA | Bước nhập mã | OTP / MFA Code | ⚠️ **chờ recon** — field có thật theo REQ-LOGIN-32 nhưng màn chưa quan sát; mã đúng · mã sai · bỏ ngang chưa có TC (cần `TK-TEST-02a/b` + bổ sung REQ) | 035 (chỉ tới bước hiện màn nhập mã) |

Thành phần khác (Component-Level): **Giao diện tĩnh** ✅ 001, 002 · **Menu thả xuống** (Modal/Dialog) ✅ 003, 055 · **Thông báo** ✅ 008–010, 013, 022, 024 (khung đỏ đúng nội dung, không cộng dồn 025) · **Data Table/List** ➖ module không có bảng dữ liệu · **CRUD** ➖ module không tạo/sửa/xoá bản ghi · **Permission/Role** ✅ 042 · **Status Flow** ✅ bảng S1–S10 dưới đây.

### Bảng quyết định — kết quả khi bấm `Login` (≥ 3 điều kiện kết hợp)

| Rule | Ô Email | Định dạng Email | Tài khoản | Ô Password | → Kết quả | TC phủ |
|---|---|---|---|---|---|---|
| R1 | Trống | — | — | Trống | 2 khung: Password + Email bắt buộc | TC_008 |
| R2 | Có | Đúng | Bất kỳ | Trống / toàn khoảng trắng | 1 khung `The Password field is required.` | TC_009 |
| R3 | Trống / toàn khoảng trắng | — | — | Có | 1 khung `The Email Address field is required.` | TC_010 |
| R4 | Có | Sai (trình duyệt bắt được) | — | Bất kỳ (kể cả trống) | Trình duyệt chặn, không gửi | TC_011, 012 |
| R4b | Có | Trình duyệt cho qua, máy chủ coi là sai (tên miền không có dấu chấm · > 254 ký tự) | — | Có | `The Email Address field must contain a valid email address.` | TC_014b-c, 059 |
| R5 | Có | Đúng | Không tồn tại | Có | `Invalid email or password` | TC_013, 014a, 017, 046, 047 |
| R6 | Có | Đúng | Nhân viên tồn tại, chưa khoá — lần sai thứ 1 → 5 | Sai | `Invalid email or password` (giống R5) — lần thứ 5 cũng vậy (REQ-LOGIN-42, Assumption tạm) nhưng khoá tài khoản | TC_018 (4 lần sai) · TC_060 bước 7 (lần thứ 5) · TC_066, 067, 068, 069 (bộ đếm) |
| R7 | Có | Đúng | Nhân viên tồn tại, không 2FA | Đúng | Vào Dashboard | TC_005, 006, 015 |
| R8 | Có | Đúng | Nhân viên bật 2FA | Đúng | Bước nhập mã, chưa vào Dashboard | TC_035 |
| R9 | Có | Đúng | Contact khách hàng | Đúng mật khẩu Contact | `Invalid email or password` | TC_042 |
| R10 | Có | Đúng | Nhân viên tồn tại, **đang bị khoá** | Đúng hoặc sai | `Your account is locked. Please try again in 15 minutes.`, không vào Dashboard (REQ-LOGIN-37, 38) | TC_060 bước 9, 061 (mật khẩu sai), 062 (mật khẩu đúng), 069, 071 (IP khác) |

### Bảng chuyển trạng thái phiên

| # | Trạng thái hiện tại | Hành động | Trạng thái kế tiếp | Hợp lệ? | TC phủ |
|---|---|---|---|---|---|
| S1 | Chưa đăng nhập | Mở route admin | Chưa đăng nhập — đứng ở trang Login | ❌ bị chặn | TC_028 |
| S2 | Chưa đăng nhập | Đăng nhập đúng (kể cả sau khi bị chặn) | Đã đăng nhập — Dashboard | ✅ | TC_005, 029 |
| S3 | Chưa đăng nhập | Đăng nhập đúng, tài khoản 2FA | Chờ nhập mã | ✅ | TC_035 |
| S4 | Đã đăng nhập | Mở trang Login (gõ địa chỉ · Back ngay sau khi đăng nhập) | Đã đăng nhập — Dashboard | ❌ bị chặn | TC_030, 057 |
| S5 | Đã đăng nhập | Mở trang Forgot Password | Đã đăng nhập — Dashboard | ❌ bị chặn | TC_031 |
| S6 | Đã đăng nhập | Logout | Chưa đăng nhập — trang Login | ✅ | TC_007 |
| S7 | Vừa đăng xuất | Mở route admin / thao tác ở tab khác / Back | Chưa đăng nhập — trang Login | ❌ bị chặn | TC_032, 033, 049 |
| S8 | Đã đăng nhập có ghi nhớ | Logout rồi mở route admin | Chưa đăng nhập — cookie ghi nhớ còn sót nhưng không khôi phục | ❌ bị chặn | TC_045 |
| S9 | Đã đăng nhập, timer đang chạy | Logout | Đã đăng nhập — cảnh báo | ❌ bị chặn | TC_034 |
| S10 | Đã đăng nhập (có / không ghi nhớ) | Phiên chính hết hạn | Có ghi nhớ: vẫn đăng nhập · không ghi nhớ: trang Login | ✅ / ❌ | TC_040, 041 |
| S11 | Chưa đăng nhập · đã sai 4 lần liên tiếp | Sai mật khẩu lần thứ 5 | Tài khoản bị khoá 15 phút | ✅ | TC_060, 069 |
| S12 | Tài khoản bị khoá | Đăng nhập (đúng / sai, mọi IP) | Vẫn khoá, không gia hạn | ❌ bị chặn | TC_061, 062, 064, 071 |
| S13 | Tài khoản bị khoá | Hết 15 phút | Đăng nhập được, bộ đếm về 0 | ✅ | TC_063, 064, 065 |
| S14 | Chưa đăng nhập · đã sai 1 → 4 lần | Đăng nhập đúng | Đã đăng nhập — bộ đếm về 0 | ✅ | TC_066 · TC_018 bước 6 (dọn dẹp, không chấm) |

## Bảng Đối Soát Coverage (toàn module)

| REQ ID | Mô tả ngắn | Web — số TC | TC IDs | Positive / Negative / Boundary | Ghi chú |
|---|---|---|---|---|---|
| REQ-LOGIN-01 | Form Login hiển thị khi chưa đăng nhập | 4 | 001, 020, 050, 053 | ✅ P (REQ hiển thị) | |
| REQ-LOGIN-02 | Ô Email được focus sẵn | 2 | 001, 050 | ✅ P | |
| REQ-LOGIN-03 | Email sai định dạng — trình duyệt chặn (Login) | 4 | 011, 012, 054, 059 | ✅ N · B (011d) | 11 biến thể · 059 kiểm phần **máy chủ** chặn định dạng — chưa có REQ riêng, nên bổ sung |
| REQ-LOGIN-04 | Ô Password che ký tự | 1 | 016 | ✅ P · N (không sao chép được) | |
| REQ-LOGIN-05 | Bỏ trống cả hai → thông báo bắt buộc | 1 | 008 | ✅ N | |
| REQ-LOGIN-06 | Password trống → thông báo Password | 1 | 009 | ✅ N · B (009b-c) | |
| REQ-LOGIN-07 | Email không tồn tại → thông báo chung | 7 | 013, 014, 017, 039, 046, 047, 056 | ✅ N · B (014, 017) | |
| REQ-LOGIN-08 | Login xoá Email sau lỗi | 1 | 021 | ✅ N | |
| REQ-LOGIN-09 | Đăng nhập đúng → Dashboard | 11 | 005, 006, 015, 019, 036, 038, 039, 051, 054, 072, 073 | ✅ P · N (038) | kiểm CSDL 072, 073 (ASM-31) |
| REQ-LOGIN-10 | Sau đăng nhập luôn vào Dashboard | 1 | 029 | ✅ P | |
| REQ-LOGIN-11 | Chưa đăng nhập mở route admin → Login | 1 | 028 | ✅ N | 4 biến thể |
| REQ-LOGIN-12 | Đã đăng nhập mở Login → Dashboard | 2 | 030, 057 | ✅ N | 057 `@NeedsVerify` (Back sau đăng nhập) |
| REQ-LOGIN-13 | Đã đăng nhập mở Forgot → Dashboard | 1 | 031 | ✅ N | |
| REQ-LOGIN-14 | Form gửi kèm CSRF token | 2 | 043, 058 | ✅ P · N (token giả · token quá hạn) | 043 `@TechCheck` · 058 không cần DevTools |
| REQ-LOGIN-15 | Tích Remember me tạo cookie `autologin` | 2 | 044, 074 | ✅ P | `@TechCheck` |
| REQ-LOGIN-16 | Cookie ghi nhớ khôi phục phiên | 1 | 040 | ✅ P | ⚪ assumption-based |
| REQ-LOGIN-17 | Link Forgot Password mở trang quên mật khẩu | 2 | 004, 039 | ✅ P | |
| REQ-LOGIN-18 | Trang Forgot Password hiển thị form | 2 | 002, 052 | ✅ P | |
| REQ-LOGIN-19 | Email sai định dạng — trình duyệt chặn (Forgot) | 1 | 023 | ✅ N | 6 biến thể |
| REQ-LOGIN-20 | Forgot trống → "Email not found" | 1 | 022 | ✅ N · B (022b) | ⚠️ nghi lỗi — AMB-LOGIN-05 |
| REQ-LOGIN-21 | Forgot email không tồn tại → "Email not found" | 4 | 024, 025, 037, 039 | ✅ N · B (024d) | ⚠️ RISK-LOGIN-02 |
| REQ-LOGIN-22 | Forgot giữ lại Email sau lỗi | 2 | 025, 048 | ✅ P · N (048) | |
| REQ-LOGIN-23 | Forgot email tồn tại → gửi thư | 2 | 026, 083 | ✅ P | ⚪ assumption-based · cần hộp thư test · 2 biến thể (chữ thường · viết hoa) |
| REQ-LOGIN-24 | Link trong thư mở màn đặt mật khẩu mới | 2 | 027, 084 | ✅ P · N (mật khẩu cũ hết hiệu lực) | ⚪ assumption-based · cần hộp thư test |
| REQ-LOGIN-25 | Menu avatar có mục Logout | 2 | 003, 055 | ✅ P | |
| REQ-LOGIN-26 | Logout → về trang Login | 3 | 007, 039, 054 | ✅ P | |
| REQ-LOGIN-27 | Sau Logout route admin bị khoá | 4 | 032, 033, 039, 049 | ✅ N | |
| REQ-LOGIN-28 | Sau Logout cookie ghi nhớ còn sót không khôi phục phiên | 2 | 045, 076 | ✅ N | `@TechCheck` · RISK-LOGIN-03 |
| REQ-LOGIN-29 | Contact không đăng nhập được khu admin | 1 | 042 | ✅ N | ⚪ assumption-based |
| REQ-LOGIN-30 | Email tồn tại + sai mật khẩu → thông báo chung | 1 | 018 | ✅ N · B (018c-d) | ⚪ assumption-based · cần `TK-TEST-01` · bắt đầu bằng 1 lần đăng nhập đúng, tối đa 4 lần sai/lượt (✏️ 11-11-2026) |
| REQ-LOGIN-31 | Email trống, có Password → chỉ thông báo Email | 1 | 010 | ✅ N · B (010b) | ⚪ assumption-based |
| REQ-LOGIN-32 | Tài khoản 2FA phải nhập mã | 1 | 035 | ✅ P | ⚪ assumption-based · cần `TK-TEST-02a/b` |
| REQ-LOGIN-33 | Không tích Remember me thì không ghi nhớ | 2 | 041, 075 | ✅ N | ⚪ assumption-based |
| REQ-LOGIN-34 | Logout khi timer chạy → cảnh báo, không đăng xuất | 1 | 034 | ✅ N | ⚪ assumption-based |
| REQ-LOGIN-35 | Sai 5 lần liên tiếp cùng email → khoá | 3 | 060, 066, 080 | ✅ N · B (060: lần 5 khoá · 066: 4 lần chưa khoá) | ticket `LOGIN-LOCKOUT-11112026` · cần `TK-PM-1` |
| REQ-LOGIN-36 | Khoá tự hết sau 15 phút | 1 | 063 | ✅ P · B (T + 16 phút) | chờ 16 phút thời gian thật |
| REQ-LOGIN-37 | Thông báo khoá trên trang Login | 1 | 061 | ✅ N | ⚪ assumption-based (AMB-LOGIN-21) · `@NeedsVerify` — chưa có ảnh thông báo khoá |
| REQ-LOGIN-38 | Đang khoá, mật khẩu đúng vẫn bị chặn | 1 | 062 | ✅ N | `@NeedsVerify` |
| REQ-LOGIN-39 | Đăng nhập đúng đặt bộ đếm về 0 | 2 | 066, 077 | ✅ P · B (2 × 4 lần sai) | TC_018 bước 6 dùng hành vi này để dọn, không chấm |
| REQ-LOGIN-40 | Email khác cùng IP không bị khoá | 1 | 070 | ✅ P | cần `TK-PM-2` |
| REQ-LOGIN-41 | Đang khoá thì khoá ở mọi IP | 1 | 071 | ✅ N | cần mạng thứ hai · `@NeedsVerify` |
| REQ-LOGIN-42 | Lần sai thứ 5 vẫn báo thông báo chung | 1 | 060 | ✅ N · B | ⚪ assumption-based (AMB-LOGIN-19) |
| REQ-LOGIN-43 | Thử trong lúc khoá không gia hạn khoá | 2 | 064, 081 | ✅ N | ⚪ assumption-based (AMB-LOGIN-20) |
| REQ-LOGIN-44 | Password trống không tính là lần sai | 2 | 067, 078 | ✅ N · B (067b toàn khoảng trắng) | ⚪ assumption-based (AMB-LOGIN-22) |
| REQ-LOGIN-45 | Bị từ chối do mã chống giả mạo không tính là lần sai | 2 | 068, 078 | ✅ N | ⚪ assumption-based (AMB-LOGIN-22) · `@TechCheck` |
| REQ-LOGIN-46 | Bộ đếm riêng từng email | 2 | 069, 079 | ✅ N | ⚪ assumption-based (AMB-LOGIN-22) · `@NeedsVerify` |
| REQ-LOGIN-47 | Hết khoá thì bộ đếm về 0 | 2 | 065, 082 | ✅ P | ⚪ assumption-based (AMB-LOGIN-25) |

**Tổng: 47/47 REQ có TC** — không dòng 🔴, không dòng ⚪ ngoài phạm vi.
**Phép thử chiều ngược (6b):** 6 TC gánh ≥ 2 REQ (TC_025, 039, 050, 054, 060, 066). TC_060 (35, 42) và TC_066 (39, 35) mỗi TC có đúng **1** REQ chỉ dựa vào nó (42 · 39), REQ-LOGIN-35 có cả hai chống lưng; các TC còn lại mọi REQ đều có TC khác → ✅ không vi phạm. **Bổ sung 14-11-2026:** TC_078 gánh 2 REQ (44, 45) — cả hai có TC khác chống lưng (TC_067, TC_068) → ✅.

## Bảng Đối Soát Evidence

Đã mở **10/10** ảnh trong `docs/requirements/login/web/evidence/` (Chrome 146, 1598×790) trước khi ghi dòng TC đầu tiên.

| Ảnh evidence | Màn hình / trạng thái | TC dựa vào | Đầy đủ? |
|---|---|---|---|
| `login_default_viewport.png` | Login — mặc định | TC_001, 020 (bước 1), 050 (bước 1) | ✅ form nằm trọn trong ảnh |
| `login_empty_submit_viewport.png` | Login — gửi trống, 2 khung đỏ | TC_008 | ✅ |
| `login_password_empty_viewport.png` | Login — Password trống, Email bị xoá, focus ô Email | TC_009a, 021a | ✅ |
| `login_invalid_credentials_viewport.png` | Login — `Invalid email or password` | TC_013a, 017, 021b, 046, 047 | ✅ |
| `login_success_landing_viewport.png` | Dashboard ngay sau đăng nhập | TC_005, 006, 029 | ✅ |
| `forgot_password_default_viewport.png` | Forgot — mặc định, không focus | TC_002, 004, 052 (bước 1) | ✅ |
| `forgot_password_empty_submit_viewport.png` | Forgot — gửi trống, `Email not found` | TC_022a | ✅ |
| `forgot_password_unknown_email_viewport.png` | Forgot — email không tồn tại, email được giữ | TC_024a, 025, 037 | ✅ |
| `logout_menu_open_viewport.png` | Dashboard — menu avatar đang mở | TC_003, 007 (bước 1), 055 (bước 1) | ✅ |
| `logout_redirect_login_viewport.png` | Login ngay sau Logout | TC_007 (bước 3), 032 | ✅ |
| Đọc DOM lúc recon (requirements mục 3) | Thứ tự Tab Login · autofocus · ô che mật khẩu · ô ẩn token | TC_001 (mục 4), 016, 043, 050 | ✅ truy về số liệu DOM trong requirements |
| (không có) | Màn nhập mã 2FA | TC_035 | 🔴 THIẾU — `@NeedsVerify` |
| (không có) | Thông báo gửi yêu cầu đặt lại thành công | TC_026 | 🔴 THIẾU — `@NeedsVerify` |
| (không có) | Màn đặt mật khẩu mới | TC_027 | 🔴 THIẾU — `@NeedsVerify` |
| (không có) | Cảnh báo Logout khi timer đang chạy | TC_034 | 🔴 THIẾU — `@NeedsVerify` |
| (không có) | Trang từ chối khi token chống giả mạo sai | TC_043 | 🔴 THIẾU — `@NeedsVerify` |
| (không có) | Bấm nhãn `Remember me` | TC_020 (bước 4–5) | 🔴 THIẾU — `@NeedsVerify` |
| (không có) | Thứ tự Tab trang Forgot Password | TC_052 | 🔴 THIẾU — `@NeedsVerify` |
| (không có) | Trang Login ở kích thước khác 1598×790 | TC_053 | 🔴 THIẾU — `@NeedsVerify` |
| (không có) | Đóng menu avatar | TC_055 | 🔴 THIẾU — `@NeedsVerify` |
| (không có) | F5 gửi lại biểu mẫu sau đăng nhập sai | TC_056 | 🔴 THIẾU — `@NeedsVerify` |
| (không có) | Back ngay sau khi đăng nhập | TC_057 | 🔴 THIẾU — `@NeedsVerify` |
| (không có) | Trang Login quá hạn cookie chống giả mạo | TC_058 | 🔴 THIẾU — `@NeedsVerify` |
| (không có) | Văn bản thay thế của logo (`alt`) | TC_050, 052 (🔧) | 🔴 THIẾU — ⚠️ ở dòng 🔧 |
| [`run_1794303621/evidence/CRM_LOGIN_TC_013_d_step5_email_khong_hop_le.jpg`](../../executions/login/web/run_1794303621/evidence/CRM_LOGIN_TC_013_d_step5_email_khong_hop_le.jpg) | Login — `qa.login@localhost`, máy chủ báo sai định dạng | TC_059 | ✅ |
| [`run_1794303621/evidence/CRM_LOGIN_TC_014_c_step5_email_khong_hop_le.jpg`](../../executions/login/web/run_1794303621/evidence/CRM_LOGIN_TC_014_c_step5_email_khong_hop_le.jpg) | Login — email 320 ký tự, máy chủ báo sai định dạng | TC_014b-c | ✅ |
| [`run_1794303621/evidence/CRM_LOGIN_TC_048_a_step5_email_khong_hop_le.jpg`](../../executions/login/web/run_1794303621/evidence/CRM_LOGIN_TC_048_a_step5_email_khong_hop_le.jpg) | Forgot — `<script>…` hiện lại dạng chữ, máy chủ báo sai định dạng | TC_048a | ✅ |
| (không có) | Forgot — chuỗi `<img … onerror=` sau khi qua WAF | TC_048b | 🔴 THIẾU — `@NeedsVerify` (run_1794303621 nhận 403) |
| (không có) | Login — tài khoản đang khoá, thông báo khoá (chữ lấy từ ticket) | TC_060, 061, 062, 069, 071 | 🔴 THIẾU — `@NeedsVerify`. 11-11-2026 đã mở lại 10/10 ảnh trước khi sinh Part 03 — không ảnh nào ở trạng thái khoá |
| (không có) | Trang từ chối khi mã chống giả mạo sai (với tài khoản PM) | TC_068 | 🔴 THIẾU — `@NeedsVerify` (như TC_043) |
| `login_invalid_credentials_viewport.png` | Login — `Invalid email or password` | TC_060 (lần 1–5), 065, 066, 067, 068, 069 | ✅ thông báo chung — dùng lại cho lần sai trước ngưỡng khoá |

### Vùng chưa có evidence — đề xuất recon bổ sung

| Vùng | Cần gì để recon | TC chờ |
|---|---|---|
| Bước nhập mã 2FA | Tài khoản test bật 2FA (`TK-TEST-02a/b`) | TC_035 |
| Luồng đặt lại mật khẩu | Hộp thư test + `TK-TEST-03` | TC_026, 027 |
| Popup Logout khi timer chạy | Tạo task test, bật timer, chụp popup | TC_034 |
| Trang từ chối token | DevTools sửa token, chụp trang trả về | TC_043 |
| Nhãn Remember me · đóng menu avatar · Tab trang Forgot | Thao tác trực tiếp, đọc DOM (`label for`, thứ tự focus) | TC_020, 052, 055 |
| Responsive | Chụp 4 kích thước + phóng to 200% | TC_053 |
| F5 sau lỗi · Back sau đăng nhập | Thao tác trực tiếp, chụp trang | TC_056, 057 |
| Trang Login quá hạn token | DevTools xoá cookie `csrf_cookie_name`, chụp trang trả về | TC_058 |
| `alt` của logo | Đọc DOM ở trang Login và Forgot Password | TC_050, 052 |
| Thông báo khoá tài khoản | Tài khoản `TK-PM-1` (chưa cấp) — khoá bằng 5 lần sai, chụp viewport trang Login ở lần gửi thứ 5 và thứ 6 · ghi nguyên văn, vị trí, màu khung | TC_060, 061, 062, 069, 071 |
| Trang từ chối mã chống giả mạo | Chung với dòng *Trang từ chối token* phía trên | TC_068 |
| Tên bảng / cột · múi giờ CSDL · cách lưu bộ đếm khoá và bản ghi ghi nhớ | Kết nối CSDL chỉ đọc (`DB_*` — AMB-SYS-05) → `SELECT` trên `information_schema` + tạo dữ liệu qua UI rồi `SELECT` đối chiếu (skill `skills-requirements-analyzer` mục 6.3.1) | TC_072 → 084 |

## Đối soát loại kiểm thử (4 vòng)

| Vòng | Nhánh | Trạng thái | TC ID / Lý do |
|---|---|---|---|
| 1 | UI cơ bản | ✅ | TC_001–003 (3 TC · 12 mục kiểm) — Login, Forgot Password, menu avatar |
| 1 | Open form | ✅ | TC_004 (1 TC · 2 biến thể: liên kết · URL trực tiếp) · mở menu ở TC_003 |
| 1 | Display | ✅ | TC_005 (Dashboard sau đăng nhập) · TC_008 (khung thông báo) |
| 1 | Input valid data | ✅ | TC_005 (tối thiểu) · TC_006 (đầy đủ, có Remember me) |
| 1 | Save | ✅ | TC_005, 006 (gửi form đăng nhập) · TC_007 (đăng xuất) |
| 1 | Verify data | ✅ | TC_005 bước 7 (phiên dùng được ở trang khác) |
| 2 | UI Behavior | ✅ | TC_016, 019, 020, 055 (4 TC · 6 biến thể) |
| 2 | Required | ✅ | TC_008, 009, 010, 022 (4 TC · 8 biến thể) |
| 2 | Validation | ✅ | TC_011–015, 017, 018, 021, 023–025, 059 (12 TC · 45 biến thể — trình duyệt chặn ở 011, 012, 023; máy chủ chặn ở 014b-c, 059 · Email Login 9/9 · Password 7/7 · Remember me 4/4 · Email Forgot 9/9 mục bảng) |
| 2 | Equivalence Partitioning | ✅ | TC_013, 015, 017, 024 (trùng TC Validation) |
| 2 | Boundary Value Analysis | ✅ | TC_009b-c, 014a-c, 017a-c, 024d — ô không có giới hạn độ dài nên biên lấy theo chuẩn email 254/255/320 ký tự (ASM-05) · ngưỡng khoá: TC_066 (4 lần sai — chưa khoá), TC_060 (5 lần — khoá), TC_063 (T + 16 phút) |
| 2 | Business Rule | ✅ | TC_018, 021, 025, 040, 041 · khoá tài khoản: TC_061, 062, 066, 067, 069 (5 TC · 6 biến thể) |
| 2 | Decision Table | ✅ | R1–R10 + R4b → TC_005, 008–014, 018, 035, 042, 059 · R6 lần thứ 5: TC_060 · R10 (tài khoản đang khoá): TC_061, 062 |
| 2 | State Transition | 🟡 Nông | S11–S14 (khoá tài khoản) → TC_060, 062–066, 069, 071. S1–S10 → TC_005, 007, 028–035, 040, 041, 045, 049, 057. Trạng thái S3 *"Chờ nhập mã"* (TC_035) **chưa có chuyển tiếp ra** (mã đúng · mã sai · bỏ ngang mở route admin) — chờ recon màn 2FA bằng `TK-TEST-02a/b` và bổ sung REQ (review 10-11-2026, Gap #8) |
| 2 | Dependency | ✅ | TC_040, 041, 045 (Remember me ↔ khôi phục phiên ↔ đăng xuất) |
| 2 | Use Case / Scenario | ✅ | TC_039 (trọn vòng) · TC_026, 027 (đặt lại mật khẩu — TC_027 tự gửi yêu cầu, không phụ thuộc TC_026) |
| 2 | Save / Edit / Delete | ➖ | Module không có CRUD — không tạo/sửa/xoá bản ghi nào |
| 2 | Error Guessing | ✅ | TC_033, 036, 037, 038, 056, 057, 058 (2 tab, bấm đúp, mất mạng, F5 gửi lại biểu mẫu, Back sau đăng nhập, trang Login quá hạn mã chống giả mạo) |
| 3 | Permission | 🟡 Nông | TC_042 (Contact × đăng nhập admin) · Admin × đăng nhập/đăng xuất ở TC_005, 007. Theo Assumption tạm AMB-LOGIN-24 (11-11-2026) có thêm role **Project Manager** — ma trận phân quyền của requirements mở lại cột này thành ❔, nhưng **chưa có REQ** cho *PM × đăng nhập / đăng xuất* → bổ sung REQ qua `/update-requirements-from-ticket` rồi mới viết TC. Cần tài khoản PM thật |
| 3 | Security | 🟡 Nông | TC_016, 018, 028, 032, 033, 042–049, 058 (truy cập khi chưa đăng nhập, sau đăng xuất, Back, CSRF, cookie, SQLi/XSS, không lộ email ở Login). Còn thiếu: mã phiên đổi sau đăng nhập · `http://` tự chuyển `https://` — chưa có REQ, bổ sung REQ qua `/update-requirements-from-ticket` rồi mới viết TC (review 10-11-2026, Gap #4, #5) |
| 3 | Security · khoá tài khoản / brute-force | ✅ | TC_060 → 071 (12 TC · 13 biến thể — mục Vòng 2c + 3b, sinh bổ sung 11-11-2026). Riêng V3: TC_068 (mã chống giả mạo), 070 (khoá theo email, không theo máy/mạng), 071 (khoá ở mọi IP). Tài khoản Project Manager, chạy tuần tự (RISK-LOGIN-07). Thông báo khoá có lộ email tồn tại không (AMB-LOGIN-23 ⏭️) — **không** có TC vì chưa có hành vi giả định. *Lịch sử: ⏭️ Cố ý bỏ (user, 05-11-2026) → 🔴 Thiếu (DELTA 11-11-2026) → ✅.* Password spraying (khoá theo email, không theo IP — RISK-LOGIN-04) ngoài khả năng kiểm của QA — đội Security |
| 3 | API | ➖ | QA không có quyền gọi API trực tiếp, chưa có đặc tả API (`docs/requirements/README.md`, chốt 05-11-2026) — đội Dev xác minh |
| 3 | Database · D1 Lưu đúng | ➖ | Module không có form lưu dữ liệu người dùng nhập — form Login / Forgot Password chỉ dùng để xác thực |
| 3 | Database · D2 Giá trị hệ thống sinh | ✅ | TC_073 (thời điểm đăng nhập gần nhất — ASM-31). Nhánh Database cả thảy: TC_072 → 084 · 13 TC · 14 biến thể · tên bảng/cột giữ chỗ, chờ kết nối CSDL (AMB-SYS-05) |
| 3 | Database · D3 Toàn vẹn | ⏭️ Cố ý bỏ | Có thứ để kiểm (bấm đúp `Login` có tích Remember me sinh mấy bản ghi ghi nhớ) nhưng requirements chưa có kỳ vọng — không có cơ sở chấm. **Quyết định: người viết TC, 14-11-2026 — chờ PO.** Rà lại khi có REQ về số phiên ghi nhớ của một tài khoản |
| 3 | Database · D4 Xoá | ✅ | TC_076 (đăng xuất xoá bản ghi ghi nhớ của phiên) |
| 3 | Database · D5 Bảo mật dữ liệu | ✅ | TC_072 (mật khẩu admin lưu dạng băm) · TC_084 (mật khẩu mới sau đặt lại lưu dạng băm) — ASM-31 |
| 3 | Database · D6 Trạng thái ẩn | ✅ | TC_074, 075 (bản ghi ghi nhớ đăng nhập) · TC_077 → 082 (6 TC · 7 biến thể — bộ đếm lần sai, thời điểm khoá) · TC_083 (mã đặt lại mật khẩu) |
| 3 | Database · D7 Nhật ký | ➖ | Requirements không có yêu cầu nhật ký đăng nhập (như nhánh Logging / Audit) |
| 3 | Integration | ➖ | QA không có quyền kiểm tầng tích hợp — chưa có hộp thư test cho SMTP (README, chốt 05-11-2026). Lỗi / quá hạn của máy chủ thư do đội Dev/DevOps kiểm. Luồng gửi thư thành công vẫn có TC_026 (`Partial`) |
| 3 | Logging / Audit | ➖ | Requirements không có yêu cầu nhật ký đăng nhập; trang nhật ký hoạt động bị chặn với tài khoản `.env` (đo 02-11-2026) |
| 4 | Compatibility | ✅ | TC_054 (1 TC · 2 biến thể: Edge, Firefox) + mọi TC chạy trên Chrome |
| 4 | Compatibility · Safari, trình duyệt di động | ⏭️ Cố ý bỏ | ASM-13 — requirements chỉ khảo sát Chrome 146, chưa có cam kết trình duyệt. **Quyết định: người viết TC, 09-11-2026 — chờ PO xác nhận.** Rà lại khi có người dùng macOS/iOS hoặc PO công bố danh sách trình duyệt hỗ trợ |
| 4 | Responsive / UI Stability | ✅ | TC_053 (1 TC · 5 biến thể: 1920 · 1366 · 768 · 375 · phóng to 200%) |
| 4 | Accessibility | ✅ | TC_050–052 (Tab, focus, Enter/Space · văn bản thay thế của logo ở 🔧 TC_050, 052) — kiểm WCAG đầy đủ / trình đọc màn hình ➖ cần công cụ riêng, chưa có người phụ trách |
| 4 | Performance | ➖ | Không có ngưỡng thời gian cam kết. Đo tải thuộc đội Hạ tầng/hiệu năng — chưa chỉ định, PM chốt ở Master Test Plan mục 2.2 |
| 4 | Regression | ➖ | Module mới, chưa có bug nào được đóng (`docs/bugs/login/` chưa tồn tại) |
| 4 | E2E | ➖ | Chưa có module thứ hai được đặc tả (README requirements: 23 module ⬜/⏸️). Rà lại khi module `CUST` có requirements |

## Rà soát đặc tính chất lượng (ISO/IEC 25010:2023)

| Đặc tính | Trạng thái | TC ID / Lý do |
|---|---|---|
| Functional Suitability | ✅ Có TC | TC_001–041, 055–058 |
| Performance Efficiency | ➖ Ngoài phạm vi | Không có ngưỡng cam kết, không có công cụ tải — đội Hạ tầng/hiệu năng (chưa chỉ định, PM chốt) |
| Compatibility | ✅ Có TC | TC_054 (Edge, Firefox) + Chrome. Safari, trình duyệt di động không kiểm — PO xác nhận nếu cần |
| Interaction Capability | ✅ Có TC | TC_001, 002, 008–010, 016, 020, 050–052, 055 (nhãn, thông báo lỗi, điều hướng bàn phím). WCAG đầy đủ — cần công cụ riêng, chưa có người phụ trách |
| Reliability | ✅ Có TC | TC_036–038, 040, 041, 056–058 (bấm đúp, mất mạng, phiên hết hạn, gửi lại biểu mẫu, Back, mã chống giả mạo quá hạn) |
| Security | ✅ Có TC | TC_016, 018, 028, 032, 033, 042–049, 058. Pentest / quét lỗ hổng — đội Security (chưa chỉ định, PM chốt). Khoá tài khoản — TC_060 → 071 (11-11-2026) · Kiểm CSDL — TC_072 → 084 (mật khẩu lưu dạng băm, bộ đếm khoá, ghi nhớ đăng nhập, mã đặt lại — 14-11-2026) |
| Maintainability | ➖ Không áp dụng | Đặc tính của mã nguồn, không kiểm bằng manual TC — code review / phân tích tĩnh của đội Dev |
| Flexibility | ✅ Có TC | TC_053 (responsive). Đổi ngôn ngữ trang Login — trang chỉ có tiếng Anh, không có bộ chọn ngôn ngữ; PO xác nhận nếu cần |
| Safety | ➖ Không áp dụng | App nghiệp vụ, lỗi đăng nhập không gây thiệt hại vật lý — PO xác nhận |

## Đối soát cột Automation

Chấm theo `.claude/skills/skills-rbt-manual-testing/references/automation_criteria.md` — 3 trục kỹ thuật · sẵn sàng · đáng làm, lấy mức thấp nhất.

| Nền tảng | Yes | Partial | No | ⏸️ Hoãn |
|---|---|---|---|---|
| Web | 53 | 31 | 0 | 20 (9 Yes · 11 Partial) |

### Điều kiện cần chuẩn bị

| # | Điều kiện | Ai cấp | Trạng thái | TC phụ thuộc |
|---|---|---|---|---|
| 1 | Tài khoản nhân viên test riêng `TK-TEST-01` (không 2FA) | Người quản trị hệ thống | ⏳ Chưa có | TC_015, 018 · TC_034 (ưu tiên — không chặn, chạy được bằng admin) |
| 2 | Tài khoản test bật 2FA `TK-TEST-02a` (Email) · `TK-TEST-02b` (Google Authenticator, cấp kèm secret TOTP) | Người quản trị hệ thống | ⏳ Chưa có | TC_035 |
| 3 | Hộp thư test đọc được qua API + `TK-TEST-03` | DevOps + người quản trị | ⏳ Chưa có | TC_026, 027 |
| 4 | Xoá riêng cookie bằng script thay cho chờ (phiên 8 giờ · mã chống giả mạo 1 giờ) | — (Playwright làm được) | ✅ Đã có | TC_040, 041, 058 |
| 5 | Tạo Contact / task / khách hàng test trên môi trường dùng chung | — (AMB-SYS-03 cho phép tạo dữ liệu thử) | ✅ Đã có | TC_034, 042, 049 |
| 6 | 2 tài khoản **Project Manager** chỉ dành cho kiểm thử, lưu ở `.env` (AMB-LOGIN-24 — ticket cấm dùng Admin cho TC khoá tài khoản) | Người quản trị hệ thống | ⏳ Chưa có | TC_060 → 071 (TC_070 cần cả `TK-PM-2`) |
| 7 | Mạng thứ hai có IP công cộng khác (Wi-Fi 4G, hoặc proxy cho script) | QA tự chuẩn bị / DevOps cấp proxy | ⏳ Chưa có | TC_071 |
| 8 | Chờ thời gian khoá thật 16 phút — máy chủ không có cách rút ngắn (`page.clock` không tác động khoá phía máy chủ). Thời hạn khoá ngắn hơn trên môi trường test → rút thời gian chạy | Dev backend (nếu muốn rút ngắn) | ✅ Chấp nhận chờ | TC_063, 064, 065 · gián tiếp mọi TC khoá (phải chờ trước khi dùng lại tài khoản) |
| 9 | Kết nối CSDL **chỉ đọc**: biến `DB_*` trong `.env` (nên là tài khoản DB read-only) + khảo sát schema để thay tên giữ chỗ trong khối 🗄️ (AMB-SYS-05, ASM-30). Automation dùng `DbClient` chỉ-đọc (`CODE_TEMPLATES.md` § 10) | User / DBA | ⏳ Chưa có | TC_072 → 084 |

### TC Partial · Hoãn

| TC ID | Nền tảng | Automation | Trục chặn | Điều kiện · phần kiểm tay · lý do |
|---|---|---|---|---|
| CRM_LOGIN_TC_015 | Web | Partial | 2 · môi trường dùng chung | Điều kiện #1 |
| CRM_LOGIN_TC_018 | Web | Partial | 2 · môi trường dùng chung | Điều kiện #1 — không được nhập sai trên tài khoản admin dùng chung |
| CRM_LOGIN_TC_026 | Web | Partial · ⏸️ Hoãn | 1 · Email | Điều kiện #3 · hoãn tới khi recon màn thông báo thành công |
| CRM_LOGIN_TC_027 | Web | Partial · ⏸️ Hoãn | 1 · Email | Điều kiện #3 · hoãn tới khi recon màn đặt mật khẩu mới |
| CRM_LOGIN_TC_035 | Web | Partial · ⏸️ Hoãn | 1 · SMS/OTP | Điều kiện #2 — biến thể `b` lên `Yes` khi có secret TOTP · hoãn tới khi recon màn nhập mã |
| CRM_LOGIN_TC_053 | Web | Partial · ⏸️ Hoãn | 2 · Expected cần mắt người | Hiện đủ phần tử + không cuộn ngang: máy chấm. "Không đè, không cắt chữ": kiểm tay hoặc visual regression · hoãn tới khi có ảnh chuẩn |
| CRM_LOGIN_TC_060 | Web | Partial · ⏸️ Hoãn | 2 · tiền đề cần tài khoản PM | Điều kiện #6 · hoãn tới khi recon thông báo khoá |
| CRM_LOGIN_TC_061 | Web | Partial · ⏸️ Hoãn | 2 · tiền đề cần tài khoản PM | Điều kiện #6 · hoãn tới khi recon thông báo khoá |
| CRM_LOGIN_TC_062 | Web | Partial · ⏸️ Hoãn | 2 · tiền đề cần tài khoản PM | Điều kiện #6 · hoãn tới khi recon thông báo khoá |
| CRM_LOGIN_TC_063 | Web | Partial | 1 · thời gian thật phía máy chủ · 2 · tài khoản PM | Điều kiện #6, #8 |
| CRM_LOGIN_TC_064 | Web | Partial | 1 · thời gian thật phía máy chủ · 2 · tài khoản PM | Điều kiện #6, #8 |
| CRM_LOGIN_TC_065 | Web | Partial | 1 · thời gian thật phía máy chủ · 2 · tài khoản PM | Điều kiện #6, #8 |
| CRM_LOGIN_TC_066 | Web | Partial | 2 · tiền đề cần tài khoản PM | Điều kiện #6 — không khoá tài khoản nếu PASS |
| CRM_LOGIN_TC_067 | Web | Partial | 2 · tiền đề cần tài khoản PM | Điều kiện #6 — không khoá tài khoản nếu PASS |
| CRM_LOGIN_TC_068 | Web | Partial · ⏸️ Hoãn | 2 · tiền đề cần tài khoản PM | Điều kiện #6 · script sửa ô ẩn thay cho DevTools · hoãn tới khi recon trang từ chối (như TC_043) |
| CRM_LOGIN_TC_069 | Web | Partial · ⏸️ Hoãn | 2 · tiền đề cần tài khoản PM | Điều kiện #6 · hoãn tới khi recon thông báo khoá |
| CRM_LOGIN_TC_070 | Web | Partial | 2 · tiền đề cần 2 tài khoản PM | Điều kiện #6 (`TK-PM-1` + `TK-PM-2`) |
| CRM_LOGIN_TC_071 | Web | Partial · ⏸️ Hoãn | 2 · cần mạng thứ hai | Điều kiện #6, #7 · hoãn tới khi recon thông báo khoá |
| CRM_LOGIN_TC_072 | Web | Partial | 2 · kết nối CSDL | Điều kiện #9 |
| CRM_LOGIN_TC_073 | Web | Partial | 2 · kết nối CSDL | Điều kiện #9 |
| CRM_LOGIN_TC_074 | Web | Partial | 2 · kết nối CSDL · tài khoản admin dùng chung | Điều kiện #9 — không chạy song song với TC đăng nhập admin có Remember me |
| CRM_LOGIN_TC_075 | Web | Partial | 2 · kết nối CSDL · tài khoản admin dùng chung | Điều kiện #9 — như TC_074 |
| CRM_LOGIN_TC_076 | Web | Partial | 2 · kết nối CSDL · tài khoản admin dùng chung | Điều kiện #9 — như TC_074 |
| CRM_LOGIN_TC_077 | Web | Partial | 2 · tài khoản PM · kết nối CSDL | Điều kiện #6, #9 |
| CRM_LOGIN_TC_078 | Web | Partial | 2 · tài khoản PM · kết nối CSDL | Điều kiện #6, #9 · biến thể `b` script sửa ô ẩn thay cho DevTools |
| CRM_LOGIN_TC_079 | Web | Partial | 2 · tài khoản PM · kết nối CSDL | Điều kiện #6, #9 |
| CRM_LOGIN_TC_080 | Web | Partial | 1 · thời gian thật phía máy chủ · 2 · tài khoản PM · kết nối CSDL | Điều kiện #6, #8, #9 |
| CRM_LOGIN_TC_081 | Web | Partial | 1 · thời gian thật phía máy chủ · 2 · tài khoản PM · kết nối CSDL | Điều kiện #6, #8, #9 |
| CRM_LOGIN_TC_082 | Web | Partial | 1 · thời gian thật phía máy chủ · 2 · tài khoản PM · kết nối CSDL | Điều kiện #6, #8, #9 |
| CRM_LOGIN_TC_083 | Web | Partial | 2 · tài khoản test · kết nối CSDL | Điều kiện #3 (chỉ `TK-TEST-03`, không cần hộp thư), #9 |
| CRM_LOGIN_TC_084 | Web | Partial · ⏸️ Hoãn | 1 · Email · 2 · kết nối CSDL | Điều kiện #3, #9 · hoãn như TC_027 tới khi recon màn đặt mật khẩu mới |
| CRM_LOGIN_TC_020 | Web | Yes · ⏸️ Hoãn | — | `@NeedsVerify` bước 4–5 (bấm nhãn) |
| CRM_LOGIN_TC_034 | Web | Yes · ⏸️ Hoãn | — | `@NeedsVerify` — chưa thấy popup cảnh báo |
| CRM_LOGIN_TC_043 | Web | Yes · ⏸️ Hoãn | — | `@NeedsVerify` — chưa thấy trang từ chối token |
| CRM_LOGIN_TC_048 | Web | Yes · ⏸️ Hoãn | — | `@NeedsVerify` biến thể `b` — máy chủ web trả 403, chờ DevOps/PO |
| CRM_LOGIN_TC_052 | Web | Yes · ⏸️ Hoãn | — | `@NeedsVerify` — thứ tự Tab trang Forgot (ASM-14) |
| CRM_LOGIN_TC_055 | Web | Yes · ⏸️ Hoãn | — | `@NeedsVerify` — cách đóng menu (ASM-22) |
| CRM_LOGIN_TC_056 | Web | Yes · ⏸️ Hoãn | — | `@NeedsVerify` — F5 gửi lại biểu mẫu (ASM-24) |
| CRM_LOGIN_TC_057 | Web | Yes · ⏸️ Hoãn | — | `@NeedsVerify` — Back sau đăng nhập (ASM-25) |
| CRM_LOGIN_TC_058 | Web | Yes · ⏸️ Hoãn | — | `@NeedsVerify` — trang từ chối khi mã chống giả mạo quá hạn (ASM-26); script xoá cookie thay cho chờ 1 giờ (điều kiện #4) |

**Thứ tự ưu tiên automate:** (1) `@Smoke` · `@CriticalPath`: TC_001–007, 039 → (2) Validation nhiều biến thể: TC_011–013, 017, 023, 024, 046, 047 → (3) phiên & điều hướng: TC_028–033 → (4) đa trình duyệt TC_054 → (5) kiểm CSDL TC_072 → 077 khi có điều kiện #9 → phần còn lại.

## Bộ chạy đề xuất

> Ba ổ trạng thái dùng chung làm TC FAIL oan khi chạy lại / chạy song song (review 10-11-2026): bộ đếm giờ trên tài khoản admin (TC_034) · cookie ghi nhớ trong profile Chrome riêng (TC_040, 041, 045) · mật khẩu `TK-TEST-03` bị đổi (TC_027). Thứ tự dưới đây khử cả ba.

| Thứ tự | Nhóm | TC | Lưu ý |
|---|---|---|---|
| 1 | Smoke | TC_001–007 | Chạy trước tiên. FAIL ở TC_005 hoặc 007 → dừng đợt, báo lỗi chặn |
| 2 | Độc lập | TC_008–014, 016, 017, 019–025, 028–033, 036–039, 042, 043, 046–052, 055–057, 059 | Mỗi TC tự dựng tiền đề (cửa sổ ẩn danh mới hoặc phiên admin riêng) — chạy song song được. TC_042 trước TC_049 (TC_049 dùng lại khách hàng `QA Login KH042`). Các TC gửi sai mỗi TC một email riêng (ASM-28) nên chạy song song không dồn quá ngưỡng khoá; **không** chạy lại TC_042 quá 4 lần trong 15 phút (cùng một email Contact) |
| 3 | Cần tài khoản / hộp thư riêng | TC_015, 018 (`TK-TEST-01`) · TC_035 (`TK-TEST-02a/b`) · TC_026, 027 (`TK-TEST-03`) | Chưa cấp → BLOCKED. TC_027 tự dọn: trả mật khẩu `TK-TEST-03` về `QaReset@2026` ở bước 15. **TC_018 không chạy song song với TC_015** (cùng `TK-TEST-01`) và luôn bắt đầu bằng 1 lần đăng nhập đúng — bộ đếm khoá 5 lần (REQ-LOGIN-35) |
| 3b | Khoá tài khoản — **tuần tự**, tài khoản Project Manager | TC_066 → 067 → 068 (không khoá nếu PASS) → **lượt khoá 1:** TC_060 (tạo khoá lúc T₁) → 070 → 061 → 062 (cùng cửa sổ khoá, trong 10 phút sau T₁) → chờ 16 phút kể từ lần thử cuối → **lượt khoá 2:** khoá (K) → 063 → **lượt khoá 3:** khoá (K) → 065 → **lượt khoá 4:** khoá (K) → 064 → **lượt khoá 5:** TC_069 → **lượt khoá 6:** khoá (K) từ mạng 1 → TC_071 trên mạng 2 | Không chạy song song, không chạy hai lượt khoá chồng lên nhau trên cùng tài khoản; mỗi TC bắt đầu từ TĐ-K (đăng nhập đúng → bộ đếm = 0). Dùng lại một lần khoá cho nhiều TC chỉ khi các TC đó **không** đòi "không gửi thêm lần nào sau T". ⚠️ **TC_063 và TC_065 không được dùng chung một lần khoá** — TC_063 đăng nhập đúng làm bộ đếm về 0, TC_065 chạy sau sẽ PASS mà không kiểm được REQ-LOGIN-47. Có `TK-PM-2` thì xen kẽ hai tài khoản để rút thời gian chờ. Ước lượng ≈ 1 giờ 45 phút (6 lượt khoá × ~17 phút). Chưa có tài khoản PM → BLOCKED |
| 3c | Kiểm CSDL — cần kết nối CSDL (điều kiện #9) | TC_072, 073 · **tuần tự** TC_074 → 075 → 076 · TC_077 → 082 chạy **trong lượt 3b** (tài khoản PM): 077 → 078 → 079 không khoá, chạy cùng TC_066 → 068; TC_080, 081, 082 mỗi TC một lượt khoá 16 phút · TC_083, 084 cùng nhóm 3 (`TK-TEST-03`) | TC_074 → 076 đếm bản ghi ghi nhớ của tài khoản admin dùng chung — **không** chạy cùng lúc với TC đăng nhập admin có Remember me (TC_006, 040, 041, 044, 045). TC_084 không chạy song song với TC_027 (cùng đổi mật khẩu `TK-TEST-03`). Chưa có kết nối CSDL → cả nhóm BLOCKED |
| 4 | Profile Chrome riêng — **tuần tự** | TC_044 → 045 → 040 → 041 | Xoá toàn bộ cookie của tên miền hệ thống **trước mỗi TC**. TC_040, 041 chờ 8 giờ 10 phút (chạy qua đêm) hoặc dùng cách 🔧 |
| 5 | Chờ lâu | TC_058 | Chờ 1 giờ 10 phút, không mở tab hệ thống khác trong lúc chờ — hoặc dùng cách 🔧 |
| 6 | Cuối bộ | TC_034 · TC_053, 054 | TC_034 chạy bằng `TK-TEST-01`; chưa có thì chạy bằng admin và **phải** để cuối cùng (bộ đếm giờ trên admin chặn mọi `Logout` khác). TC_053, 054 đổi kích thước / trình duyệt |

## Điểm cần user review

1. **13 TC `@NeedsVerify`** (TC_020, 026, 027, 034, 035, 043, 048, 052, 053, 055, 056, 057, 058) — TC_020, 055 đã xác nhận trên UI ở `run_1794303621`, chờ gỡ tag — Expected chưa có ảnh chống lưng; nên recon bổ sung theo bảng *Vùng chưa có evidence*.
2. **Tài khoản / hộp thư test chưa có** — TC_015, 018, 026, 027, 035 sẽ BLOCKED cho tới khi cấp `TK-TEST-01/02a/02b/03` (ASM-02, ASM-11).
3. **TC PASS không có nghĩa hành vi đúng** ở TC_022 (Forgot trống báo "Email not found" — AMB-LOGIN-05) và TC_024 (lộ email tồn tại — RISK-LOGIN-02). Nên báo dev riêng.
4. **TC_044, TC_045** ghi nhận cookie `autologin` thiếu HttpOnly/SameSite và còn sót sau Logout (RISK-LOGIN-03) — là hiện trạng, không phải tiêu chí FAIL.
5. **TC_043, TC_044, TC_048** cần tester biết DevTools (`@TechCheck`) — cách thao tác DevTools đã dời xuống `🔧 Ghi chú kỹ thuật` (review 10-11-2026). Tester không có DevTools: chạy TC_058 thay cho TC_043, TC_006 thay cho TC_044.
6. **Còn mở sau review 10-11-2026** — cần bổ sung REQ / recon trước khi viết TC: mã phiên đổi sau đăng nhập · `http://` tự chuyển `https://` (V3 Security) · chuyển tiếp ra khỏi bước nhập mã 2FA (V2 State Transition). Mật khẩu tài khoản test (ASM-02, ASM-11) nên chuyển sang biến `.env` khi được cấp thật.
7. **Máy chủ kiểm định dạng / độ dài email** (phát hiện ở `run_1794303621`) chưa có REQ — TC_014, 048, 059 đang dựa vào quan sát. Nên bổ sung REQ qua `/update-requirements-from-ticket`. Chưa biết giới hạn 254 ký tự có áp cho form Forgot không (mới quan sát 254 ký tự).
8. **TC_047-e, TC_048-b** — chuỗi chứa `<img … onerror=` bị máy chủ web (LiteSpeed) trả `403 Forbidden`. Chờ DevOps/PO xác nhận đây là hành vi chấp nhận được rồi mới sửa Expected.
9. **Khoá tài khoản (11-11-2026)** — TC_060 → 071 (mục Vòng 2c + 3b) phủ 13 REQ mới nhưng **toàn bộ BLOCKED** cho tới khi có 2 tài khoản Project Manager (điều kiện #6). 6 TC `@NeedsVerify` (060, 061, 062, 068, 069, 071) — chưa ai thấy thông báo khoá, chữ lấy từ ticket; lượt chạy đầu nên chụp ảnh làm evidence. 7/12 TC dựa trên Assumption tạm (`@assumption-based`). AMB-LOGIN-23 (thông báo khoá có lộ email tồn tại không) chưa có câu trả lời thật và **không có TC** — rủi ro bảo mật chưa kiểm.
10. **Kiểm CSDL (14-11-2026)** — TC_072 → 084 (`@DBCheck`, mục Vòng 3c) **BLOCKED** cho tới khi có kết nối CSDL chỉ đọc và khảo sát schema (AMB-SYS-05, điều kiện #9): mọi tên bảng/cột trong khối 🗄️ đang là tên giữ chỗ. TC_072, 073, 084 dựa trên kỳ vọng requirements **chưa nói** (cách lưu mật khẩu, thời điểm đăng nhập gần nhất — ASM-31) → nên bổ sung REQ. Chỉ được chạy `SELECT` (`.claude/rules/database_rules.md`), không dùng CSDL để mở khoá hay dọn dữ liệu.

## Nhật ký thay đổi

| Ngày | Nguồn | Thay đổi | Mốc git trước khi ghi |
|---|---|---|---|
| 09-11-2026 | `/generate-testcases-from-requirements` (QUICK · GỘP) | Sinh mới 55 TC (`CRM_LOGIN_TC_001` → `055`) · 125 biến thể · 2 part web | `cb8ea3a` (chưa có `docs/testcases/`) |
| 10-11-2026 | `/review-testcases` **mode FIX** — [báo cáo](review/testcase_review_report_web_20261110.md) | **Viết lại** TC_027 (tự dựng tiền đề, tách bước, bước dọn trả mật khẩu) · Priority TC_026, 027 → High. **Khử trạng thái dùng chung:** TC_034 (chạy bằng `TK-TEST-01`, bước dừng timer), TC_040, 041, 045 (xoá cookie, đóng tab khi chờ, tách bước) + mục *Bộ chạy đề xuất*. **Sửa cách viết:** TC_001, 002 (tên tab), 014 (file dữ liệu `web/data/`), 016 (bỏ bước trùng TC_001), 018 (bước 6 thành dọn dẹp), 021 (bỏ biến thể `b` trùng TC_013-a), 039, 051, 054 (tách bước), 042, 049 (Pre-Condition), 043, 048 (DevTools xuống 🔧), 044 (Test Scenario). **Thêm:** TC_056–058 (Error Guessing), TC_012-f, TC_026-b, `alt` logo ở 🔧 TC_050, 052 · ASM-23 → 27. Index: S1–S10, dòng ⏭️ Compatibility, field OTP/MFA, State Transition + Security → 🟡. **55 → 58 TC · 125 → 129 biến thể** | `752c90a` (cả 2 part + index) — xem bản cũ: `git show 752c90a:docs/testcases/login/web/parts/part_01_web_chuc_nang.md` |
| 10-11-2026 | Sửa Expected theo kết quả chạy — [`run_1794303621`](../../executions/login/web/run_1794303621/execution_report.md) FAIL #1, #2, #4 (TC giả định sai, không phải lỗi hệ thống) | **TC_013:** bỏ biến thể `d` (`qa.login@localhost`), lý do ghi trong Expected; biến thể `f` ghi rõ phải gõ tay. **TC_014:** Test Scenario + Expected `5` theo biên máy chủ — `a` (254) `Invalid email or password`, `b`/`c` (255/320) `The Email Address field must contain a valid email address.`. **TC_048:** Expected `5` — `a`, `b` thông báo định dạng, `c` `Email not found`; `b` thêm `@NeedsVerify` (403 WAF). **Thêm TC_059** (tách từ TC_013-d — máy chủ chặn định dạng). ASM-03, 05, 19 · bảng quyết định thêm R4b · coverage REQ-LOGIN-03 · evidence · Automation (53 Yes). **58 → 59 TC · 129 biến thể.** Chưa sửa TC_047-e (chờ DevOps/PO) | **Không có mốc git** — user chọn sửa không commit trước (`docs/testcases/` chưa được git theo dõi ở repo chính; worktree còn thay đổi chưa commit). Bản trước khi sửa chỉ còn ở scratchpad phiên làm việc |
| 11-11-2026 | `/update-testcases-from-impact` **APPLY** — ticket `LOGIN-LOCKOUT-11112026` (khoá tài khoản) · [kế hoạch đã duyệt](impact/impact_plan_LOGIN-LOCKOUT-11112026.md) · [Delta TC List](impact/delta_tc_LOGIN-LOCKOUT-11112026.md) | **V2 · Validation / Business Rule — TC_018:** Pre-Condition bắt đầu bằng 1 lần đăng nhập đúng (đưa bộ đếm về 0), cấm thêm biến thể thứ 5; bước 6 bỏ câu "ngoài phạm vi AMB-LOGIN-10", dẫn REQ-LOGIN-35, 39. **V2 · EP/BVA — TC_017**, **V3 · Security — TC_047:** mỗi biến thể một email không tồn tại riêng. **V2 · Validation — TC_013**, **V2 · Use Case — TC_039**, **V2 · Error Guessing — TC_056:** email riêng của từng TC. Quy ước chung Part 01. Index: ASM-07 · thêm ASM-28 · bảng quyết định R6, R10 · trạng thái S11–S14 · Coverage 34/47 (13 REQ mới ⚪ ngoài phạm vi DELTA) · 4 vòng: Decision Table, Permission → 🟡, khoá tài khoản ⏭️ → 🔴 · ISO Security · điều kiện Automation #6 · Bộ chạy 3b. **59 TC · 129 biến thể — không đổi** | **Không có mốc git** — `docs/testcases/` chưa được git theo dõi (`git status`: `??`, 11-11-2026). Bản trước khi sửa lưu ở scratchpad phiên làm việc |
| 11-11-2026 | `/generate-testcases-from-requirements` — chế độ **BỔ SUNG** (QUICK · GỘP) cho REQ-LOGIN-35 → 47 | **Thêm Part 03** `part_03_web_khoa_tai_khoan.md` *(đã gộp vào `web/test_cases_login_web.md` ngày 14-11-2026)*: TC_060 → 071 (V2: 060–067, 069 · V3: 068, 070, 071), tài khoản Project Manager, tiền đề TĐ-K và khoá (K) dùng chung. Mở lại 10/10 ảnh evidence — không ảnh nào ở trạng thái khoá → 6 TC `@NeedsVerify`. Index: Bản đồ tài liệu · ASM-29 · bảng quyết định R6, R10 · S11–S14 · Coverage **47/47** · 4 vòng: BVA, Business Rule, Decision Table ✅, khoá tài khoản 🔴 → ✅ · ISO Security · Automation (+12 Partial, +6 Hoãn, điều kiện #7, #8) · Bộ chạy 3b. Part 02 thêm link sang Part 03. **59 → 71 TC · 129 → 142 biến thể** | **Không có mốc git** — `docs/testcases/` chưa được git theo dõi. Part 01, 02 không bị sửa dòng TC nào |
| 14-11-2026 | Gộp file theo quy ước mới *mỗi nền tảng một file TC, không tách part* (skill rbt — Quy Tắc Xuất File mục 2) | Gộp nguyên văn 3 part web → [`web/test_cases_login_web.md`](web/test_cases_login_web.md); xoá `web/parts/`. Thứ tự mục: Vòng 1 · 2a · 2b (Part 01) → 2c (Part 03 · V2) → 3a (Part 02 · V3) → 3b (Part 03 · V3) → 4 (Part 02 · V4). Bảng thông tin của Part 02 (năng lực QA) chuyển lên đầu file, của Part 03 chuyển xuống đầu mục Vòng 2c. **Không đổi** dòng TC, TC ID, biến thể nào — đã đối chiếu 71/71 dòng TC trùng khớp nguyên văn. **71 TC · 142 biến thể** | **Không có mốc git** — `docs/testcases/` chưa được git theo dõi |
| 14-11-2026 | `/generate-testcases-from-requirements` — chế độ **BỔ SUNG** (QUICK · GỘP) cho nhánh V3 `Database` sau khi QA được cấp quyền truy vấn CSDL **chỉ SELECT** | **Thêm mục Vòng 3c** vào [`web/test_cases_login_web.md`](web/test_cases_login_web.md): TC_072 → 084 (13 TC · 14 biến thể, `@DBCheck`, `Auto Type` = `UI+DB`) — D2 TC_073 · D4 TC_076 · D5 TC_072, 084 · D6 TC_074, 075, 077 → 083 · D1, D7 ➖ · D3 ⏭️. Tên bảng/cột giữ chỗ (AMB-SYS-05) → mọi TC mới mang `@NeedsVerify`. Index: dải TC · Bản đồ tài liệu · ASM-30, 31 · Coverage (13 REQ thêm TC, vẫn **47/47**) · 4 vòng nhánh Database ➖ → 7 dòng D1–D7 · ISO Security · Automation (+13 Partial, +1 Hoãn, điều kiện #9) · Bộ chạy 3c · Điểm review #10. **71 TC cũ không đổi dòng nào** · **71 → 84 TC · 142 → 156 biến thể** | **Không có mốc git** — `docs/testcases/` chưa được git theo dõi |
