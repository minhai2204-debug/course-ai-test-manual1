# Ma Trận Truy Vết (RTM) — Đăng nhập (`LOGIN`)

> **Tóm tắt:** 47/47 REQ đã có TC (100%) · **0/84 TC có script automation** · **54/84 TC đã có kết quả** (37 PASS · 6 FAIL · 11 BLOCKED) · **17/47 REQ chưa có TC nào được chạy** — toàn bộ STORY-LOGIN-06 (khoá tài khoản, 13 REQ) chưa từng được kiểm trên hệ thống · chỉ 25/47 REQ có ít nhất 1 TC PASS · 22 REQ ⚪ mô tả theo Assumption tạm, chưa kiểm chứng

| Thông tin | Nội dung |
|---|---|
| Ngày sinh | 18-11-2026 15:43 — sinh lại sau lần chạy `run_1794989188` (lần sinh trước: 18-11-2026 14:56) |
| Mục đích | Báo cáo độ phủ trước release |
| Phạm vi | Module `LOGIN` · web (nền tảng duy nhất của module) |
| Mốc git | `cb8ea3a` — ⚠️ `docs/testcases/`, `docs/checklists/`, `docs/executions/`, `docs/bugs/`, `docs/traceability/` **chưa commit** ở mốc này: RTM đọc từ bản đang có trên máy |
| Nguồn đã quét | REQ: `requirements/login/` (index + `web/requirements_login_web.md` — 47 REQ, 6 Story) · TC: `testcases/login/web/test_cases_login_web.md` (84 TC, 0 `@Deprecated`) · Automation: **không tìm thấy script** (`.spec.ts`, `*Test.java`, `.py`) — RTM 2 tầng REQ ↔ TC, ẩn cột `Automation` · Checklist: [`checklist_regression_20261118.md`](../../checklists/login/web/checklist_regression_20261118.md) (bản mới nhất) · Kết quả chạy (kết quả mới nhất của **từng** TC): [`run_1794303621`](../../executions/login/web/run_1794303621/execution_report.md) (10-11-2026, 34 TC) + [`run_1794989188`](../../executions/login/web/run_1794989188/execution_report.md) (18-11-2026, 23 TC — 3 TC chạy lại: 001, 016, 056) · chưa có `retest_*` · Bug: `bugs/README.md` (1 bug đang mở) |
| Tổng hợp | [../traceability_matrix.md](../traceability_matrix.md) — ⬛ module ngoài tầm nhìn của RTM nằm ở đó |

## 1. Tổng quan

| Chỉ số | Tiến độ | Giá trị |
|---|---|---|
| Requirement Coverage | `▰▰▰▰▰▰▰▰▰▰` | **47/47** (100%) REQ trong phạm vi — 0 REQ loại trừ |
| Platform Coverage · web | `▰▰▰▰▰▰▰▰▰▰` | 47/47 cặp REQ × nền tảng |
| Automation Coverage | `▱▱▱▱▱▱▱▱▱▱` | **0/84** TC (0%) — chưa có script nào |
| REQ có ≥1 TC đã chạy | `▰▰▰▰▰▰▱▱▱▱` | 30/47 (64%) — 17 REQ chưa có TC nào chạy (trước: 21/47) |
| REQ có ≥1 TC PASS | `▰▰▰▰▰▱▱▱▱▱` | 25/47 (53%) — 5 REQ đã chạy nhưng chỉ có FAIL / BLOCKED: REQ-LOGIN-02, 04, 16, 29, 33 |
| TC đã có kết quả | `▰▰▰▰▰▰▱▱▱▱` | 54/84 (64%) — 30 TC chưa từng chạy (trước: 34/84) |
| Pass rate (kết quả mới nhất từng TC) | `▰▰▰▰▰▰▰▱▱▱` | 37/54 (69%) · ❌ 6 FAIL · 🚫 11 BLOCKED · 30 TC chưa chạy |
| REQ có mục trong checklist regression | `▰▰▰▰▰▰▰▰▰▱` | 41/47 — nguồn phụ, không thay TC |

**Phân bổ REQ theo trạng thái:**

| ✅ Đã automate | 🟣 Automate một phần | 🟡 Thủ công | 🟠 Chỉ checklist | 🔴 Chưa có TC | ⏭️ Loại trừ |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 47 | 0 | 0 | 0 |

> **⚪ chưa kiểm chứng** (hậu tố ở cột Trạng thái) = REQ ghi theo ticket hoặc Assumption tạm, chưa quan sát được trên hệ thống (`REQ-LOGIN-16, 23, 24, 29 → 47` — 22 REQ). Có TC không có nghĩa hành vi đã đúng: TC của các REQ này mang `@assumption-based` / `@NeedsVerify`, kết quả chạy đầu tiên cũng là lần kiểm chứng đầu tiên. Lần chạy 18-11 đã có kết quả PASS cho REQ-LOGIN-34 (cảnh báo bộ đếm giờ khi đăng xuất).
>
> **Ngôn ngữ môi trường:** từ sau 10-11-2026, giao diện admin của tài khoản dùng chung là Tiếng Việt — kết quả 18-11 chấm nhãn `Bảng tin` / `Khách hàng` tương đương `Dashboard` / `Customers` (user chốt).

## 2. Việc cần làm

1. ❌ **6 TC FAIL** (kết quả mới nhất đều từ `run_1794303621`, 10-11-2026 — lần chạy 18-11 không có FAIL):
   - **2 TC có bug đang mở** — `CRM_LOGIN_TC_050`, `CRM_LOGIN_TC_052` ([`BUG_login_1794305372_TC050`](../../bugs/login/web/BUG_login_1794305372_TC050.md), Minor · P3, viền focus) → `/retest-fixed-bugs` khi Dev báo fix
   - **3 TC FAIL theo Expected cũ, chưa có bug** — `CRM_LOGIN_TC_013`, `CRM_LOGIN_TC_014`, `CRM_LOGIN_TC_048` (biến thể `a`): Expected đã sửa 10-11-2026 sau lần chạy (máy chủ tự kiểm định dạng email) → chạy lại bằng `/execute-test-cases`, **không** mở bug
   - **1 TC chờ quyết định, chưa có bug** — `CRM_LOGIN_TC_047`-e (và `CRM_LOGIN_TC_048`-b): chuỗi `"><img … onerror=` bị máy chủ web trả trang 403 trần. Hỏi DevOps / PO trước — chấp nhận → sửa Expected qua `/review-testcases`; không → `/create-bug-report`
2. ▶️ **30 TC chưa từng chạy** → `/execute-test-cases` khi có điều kiện:
   - **12 TC chờ tài khoản Project Manager** `TK-PM-1/2` (`.env` chưa có `EMAIL_PM_1/2`): 060 → 071 — cả STORY-LOGIN-06, gồm 2 TC Critical 060, 062
   - **13 TC `@DBCheck` chờ kết nối CSDL** (`.env` chưa có `DB_*` — AMB-SYS-05): 072 → 084
   - **5 TC chờ tài khoản test / hộp thư**: 015, 018 (`TK-TEST-01`) · 035 (`TK-TEST-02a`) · 026, 027 (`TK-TEST-03` + hộp thư)
3. 🚫 **11 TC BLOCKED** — pane trình duyệt tích hợp không làm được (focus, bộ nhớ tạm, F5, xoá cookie HttpOnly, phóng to trang, Edge/Firefox) hoặc cần bước tay: 001, 016, 019, 038, 040, 041, 042, 053, 054, 056, 058. **001, 016, 056 đã BLOCKED 2 lần cùng nguyên nhân** → giao tester chạy tay, hoặc cấu hình Playwright MCP (`.mcp.json`) rồi `/execute-test-cases`
4. 📝 **Cập nhật TC theo kết quả 18-11** → `/review-testcases` mode FIX: TC_043 (và 036, 058) đổi chữ trang từ chối sang `419 Page Expired!` · TC_034 điền nội dung cảnh báo + nút đóng `×` · gỡ `@NeedsVerify` TC_034, 043, 053 (bước 3), 057 · Expected kiểm chữ `Dashboard` không phụ thuộc ngôn ngữ tài khoản
5. 🟡 **Bắt đầu automate:** 35 TC Critical/High đã chấm `Automation = Yes` → `/generate-automation-from-testcases`

## 3. Ma trận chi tiết

> Cột `Checklist` = mã mục của checklist regression 18-11-2026 (nguồn phụ, không tính vào độ phủ). Cột `Kết quả gần nhất` lấy kết quả mới nhất của **từng** TC trong ô `TC IDs` (BLOCKED tính là đã chạy) — `—` khi chưa TC nào chạy.

### 3.1. Màn hình & validation đăng nhập (STORY-LOGIN-01)

`▰▰▰▰▰` 13/13 REQ có TC · 11/13 REQ có ít nhất 1 TC đã chạy

| REQ ID | Yêu cầu | TC IDs | Checklist | Kết quả gần nhất | Trạng thái |
|---|---|---|---|:-:|---|
| REQ-LOGIN-01 | Trang Login hiển thị form đăng nhập khi chưa đăng nhập | CRM_LOGIN_TC_001, CRM_LOGIN_TC_020, CRM_LOGIN_TC_050, CRM_LOGIN_TC_053 | CL-regression_20261118-01 | ✅ 1 · ❌ 1 🐞 · 🚫 2 | 🟡 Thủ công |
| REQ-LOGIN-02 | Ô Email Address được focus sẵn khi tải trang | CRM_LOGIN_TC_001, CRM_LOGIN_TC_050 | CL-regression_20261118-01 | ❌ 1 🐞 · 🚫 1 | 🟡 Thủ công |
| REQ-LOGIN-03 | Email sai định dạng bị trình duyệt chặn, không gửi form Login | CRM_LOGIN_TC_011, CRM_LOGIN_TC_012, CRM_LOGIN_TC_054, CRM_LOGIN_TC_059 | CL-regression_20261118-12, CL-regression_20261118-13 | ✅ 3 · 🚫 1 | 🟡 Thủ công |
| REQ-LOGIN-04 | Ô Password che ký tự nhập | CRM_LOGIN_TC_016 | CL-regression_20261118-14 | 🚫 1 | 🟡 Thủ công |
| REQ-LOGIN-05 | Bỏ trống Email → thông báo bắt buộc nhập Email | CRM_LOGIN_TC_008 | CL-regression_20261118-09 | ✅ 1 | 🟡 Thủ công |
| REQ-LOGIN-06 | Bỏ trống Password → thông báo bắt buộc nhập Password | CRM_LOGIN_TC_009 | CL-regression_20261118-10 | ✅ 1 | 🟡 Thủ công |
| REQ-LOGIN-07 | Email không tồn tại → thông báo chung "Invalid email or password" | CRM_LOGIN_TC_013, CRM_LOGIN_TC_014, CRM_LOGIN_TC_017, CRM_LOGIN_TC_039, CRM_LOGIN_TC_046, CRM_LOGIN_TC_047, CRM_LOGIN_TC_056 | CL-regression_20261118-15, CL-regression_20261118-16 | ✅ 3 · ❌ 3 · 🚫 1 | 🟡 Thủ công |
| REQ-LOGIN-08 | Máy chủ không giữ lại giá trị Email sau khi đăng nhập lỗi | CRM_LOGIN_TC_021 | CL-regression_20261118-10, CL-regression_20261118-15 | ✅ 1 | 🟡 Thủ công |
| REQ-LOGIN-14 | Form Login gửi kèm CSRF token | CRM_LOGIN_TC_043, CRM_LOGIN_TC_058 | — | ✅ 1 · 🚫 1 | 🟡 Thủ công |
| REQ-LOGIN-29 | Contact khách hàng không đăng nhập được vào khu admin | CRM_LOGIN_TC_042 | CL-regression_20261118-39 | 🚫 1 | 🟡 Thủ công · ⚪ chưa kiểm chứng |
| REQ-LOGIN-30 | Email tồn tại + sai mật khẩu → thông báo chung "Invalid email or password" | CRM_LOGIN_TC_018 | CL-regression_20261118-17 | — | 🟡 Thủ công · ⚪ chưa kiểm chứng |
| REQ-LOGIN-31 | Bỏ trống Email, có Password → chỉ hiện thông báo Email | CRM_LOGIN_TC_010 | CL-regression_20261118-11 | ✅ 1 | 🟡 Thủ công · ⚪ chưa kiểm chứng |
| REQ-LOGIN-32 | Tài khoản bật 2FA phải nhập mã sau mật khẩu | CRM_LOGIN_TC_035 | CL-regression_20261118-32 | — | 🟡 Thủ công · ⚪ chưa kiểm chứng |

### 3.2. Phiên & điều hướng (STORY-LOGIN-02)

`▰▰▰▰▰` 5/5 REQ có TC · 5/5 REQ có ít nhất 1 TC đã chạy

| REQ ID | Yêu cầu | TC IDs | Checklist | Kết quả gần nhất | Trạng thái |
|---|---|---|---|:-:|---|
| REQ-LOGIN-09 | Đăng nhập đúng → vào Dashboard | CRM_LOGIN_TC_005, CRM_LOGIN_TC_006, CRM_LOGIN_TC_015, CRM_LOGIN_TC_019, CRM_LOGIN_TC_036, CRM_LOGIN_TC_038, CRM_LOGIN_TC_039, CRM_LOGIN_TC_051, CRM_LOGIN_TC_054, CRM_LOGIN_TC_072, CRM_LOGIN_TC_073 | CL-regression_20261118-05, CL-regression_20261118-06, CL-regression_20261118-08 | ✅ 5 · 🚫 3 | 🟡 Thủ công |
| REQ-LOGIN-10 | Sau đăng nhập luôn vào Dashboard, kể cả khi trước đó bị chặn ở trang khác | CRM_LOGIN_TC_029 | CL-regression_20261118-24 | ✅ 1 | 🟡 Thủ công |
| REQ-LOGIN-11 | Chưa đăng nhập mở route admin → về trang Login | CRM_LOGIN_TC_028 | CL-regression_20261118-23 | ✅ 1 | 🟡 Thủ công |
| REQ-LOGIN-12 | Đã đăng nhập mở trang Login → về Dashboard | CRM_LOGIN_TC_030, CRM_LOGIN_TC_057 | CL-regression_20261118-25 | ✅ 2 | 🟡 Thủ công |
| REQ-LOGIN-13 | Đã đăng nhập mở trang Forgot Password → về Dashboard | CRM_LOGIN_TC_031 | CL-regression_20261118-25 | ✅ 1 | 🟡 Thủ công |

### 3.3. Ghi nhớ đăng nhập (STORY-LOGIN-03)

`▰▰▰▰▰` 3/3 REQ có TC · 3/3 REQ có ít nhất 1 TC đã chạy

| REQ ID | Yêu cầu | TC IDs | Checklist | Kết quả gần nhất | Trạng thái |
|---|---|---|---|:-:|---|
| REQ-LOGIN-15 | Tick Remember me khi đăng nhập tạo cookie `autologin` | CRM_LOGIN_TC_044, CRM_LOGIN_TC_074 | — | ✅ 1 | 🟡 Thủ công |
| REQ-LOGIN-16 | Cookie `autologin` khôi phục phiên khi phiên chính hết hạn | CRM_LOGIN_TC_040 | CL-regression_20261118-29 | 🚫 1 | 🟡 Thủ công · ⚪ chưa kiểm chứng |
| REQ-LOGIN-33 | Không tick Remember me thì không tạo cookie `autologin` | CRM_LOGIN_TC_041, CRM_LOGIN_TC_075 | CL-regression_20261118-30 | 🚫 1 | 🟡 Thủ công · ⚪ chưa kiểm chứng |

### 3.4. Quên mật khẩu (STORY-LOGIN-04)

`▰▰▰▰▰` 8/8 REQ có TC · 6/8 REQ có ít nhất 1 TC đã chạy

| REQ ID | Yêu cầu | TC IDs | Checklist | Kết quả gần nhất | Trạng thái |
|---|---|---|---|:-:|---|
| REQ-LOGIN-17 | Link "Forgot Password?" mở trang quên mật khẩu | CRM_LOGIN_TC_004, CRM_LOGIN_TC_039 | CL-regression_20261118-03 | ✅ 2 | 🟡 Thủ công |
| REQ-LOGIN-18 | Trang Forgot Password hiển thị form nhập email | CRM_LOGIN_TC_002, CRM_LOGIN_TC_052 | CL-regression_20261118-02 | ✅ 1 · ❌ 1 🐞 | 🟡 Thủ công |
| REQ-LOGIN-19 | Email sai định dạng bị trình duyệt chặn, không gửi form Forgot Password | CRM_LOGIN_TC_023 | CL-regression_20261118-19 | ✅ 1 | 🟡 Thủ công |
| REQ-LOGIN-20 | Forgot Password bỏ trống Email → thông báo "Email not found" | CRM_LOGIN_TC_022 | CL-regression_20261118-18 | ✅ 1 | 🟡 Thủ công |
| REQ-LOGIN-21 | Forgot Password với email không tồn tại → thông báo "Email not found" | CRM_LOGIN_TC_024, CRM_LOGIN_TC_025, CRM_LOGIN_TC_037, CRM_LOGIN_TC_039 | CL-regression_20261118-20 | ✅ 4 | 🟡 Thủ công |
| REQ-LOGIN-22 | Forgot Password giữ lại giá trị Email sau lỗi | CRM_LOGIN_TC_025, CRM_LOGIN_TC_048 | CL-regression_20261118-20 | ✅ 1 · ❌ 1 | 🟡 Thủ công |
| REQ-LOGIN-23 | Forgot Password với email tồn tại gửi email đặt lại mật khẩu | CRM_LOGIN_TC_026, CRM_LOGIN_TC_083 | CL-regression_20261118-21 | — | 🟡 Thủ công · ⚪ chưa kiểm chứng |
| REQ-LOGIN-24 | Link trong email đặt lại mở màn đặt mật khẩu mới | CRM_LOGIN_TC_027, CRM_LOGIN_TC_084 | CL-regression_20261118-22 | — | 🟡 Thủ công · ⚪ chưa kiểm chứng |

### 3.5. Đăng xuất (STORY-LOGIN-05)

`▰▰▰▰▰` 5/5 REQ có TC · 5/5 REQ có ít nhất 1 TC đã chạy

| REQ ID | Yêu cầu | TC IDs | Checklist | Kết quả gần nhất | Trạng thái |
|---|---|---|---|:-:|---|
| REQ-LOGIN-25 | Menu avatar có mục Logout | CRM_LOGIN_TC_003, CRM_LOGIN_TC_055 | CL-regression_20261118-04 | ✅ 2 | 🟡 Thủ công |
| REQ-LOGIN-26 | Bấm Logout → về trang Login | CRM_LOGIN_TC_007, CRM_LOGIN_TC_039, CRM_LOGIN_TC_054 | CL-regression_20261118-07 | ✅ 2 · 🚫 1 | 🟡 Thủ công |
| REQ-LOGIN-27 | Sau Logout, route admin yêu cầu đăng nhập lại | CRM_LOGIN_TC_032, CRM_LOGIN_TC_033, CRM_LOGIN_TC_039, CRM_LOGIN_TC_049 | CL-regression_20261118-26, CL-regression_20261118-27 | ✅ 4 | 🟡 Thủ công |
| REQ-LOGIN-28 | Sau Logout, cookie `autologin` còn sót không khôi phục phiên | CRM_LOGIN_TC_045, CRM_LOGIN_TC_076 | CL-regression_20261118-28 | ✅ 1 | 🟡 Thủ công |
| REQ-LOGIN-34 | Logout khi có timer đang chạy hiện popup cảnh báo, không đăng xuất | CRM_LOGIN_TC_034 | CL-regression_20261118-31 | ✅ 1 | 🟡 Thủ công · ⚪ chưa kiểm chứng |

### 3.6. Khoá tài khoản khi đăng nhập sai nhiều lần (STORY-LOGIN-06)

`▰▰▰▰▰` 13/13 REQ có TC · 0/13 REQ có ít nhất 1 TC đã chạy

| REQ ID | Yêu cầu | TC IDs | Checklist | Kết quả gần nhất | Trạng thái |
|---|---|---|---|:-:|---|
| REQ-LOGIN-35 | Sai mật khẩu 5 lần liên tiếp với cùng một email thì tài khoản bị khoá | CRM_LOGIN_TC_060, CRM_LOGIN_TC_066, CRM_LOGIN_TC_080 | CL-regression_20261118-33, CL-regression_20261118-34 | — | 🟡 Thủ công · ⚪ chưa kiểm chứng |
| REQ-LOGIN-36 | Khoá tự hết hiệu lực sau 15 phút | CRM_LOGIN_TC_063 | CL-regression_20261118-37 | — | 🟡 Thủ công · ⚪ chưa kiểm chứng |
| REQ-LOGIN-37 | Tài khoản đang khoá → trang Login hiển thị thông báo khoá | CRM_LOGIN_TC_061 | CL-regression_20261118-34 | — | 🟡 Thủ công · ⚪ chưa kiểm chứng |
| REQ-LOGIN-38 | Trong thời gian khoá, nhập đúng mật khẩu vẫn không đăng nhập được | CRM_LOGIN_TC_062 | CL-regression_20261118-35 | — | 🟡 Thủ công · ⚪ chưa kiểm chứng |
| REQ-LOGIN-39 | Đăng nhập thành công trước khi đủ 5 lần sai đặt bộ đếm lần sai về 0 | CRM_LOGIN_TC_066, CRM_LOGIN_TC_077 | CL-regression_20261118-38 | — | 🟡 Thủ công · ⚪ chưa kiểm chứng |
| REQ-LOGIN-40 | Khoá chỉ áp cho email bị sai — email khác đăng nhập được từ cùng máy | CRM_LOGIN_TC_070 | CL-regression_20261118-36 | — | 🟡 Thủ công · ⚪ chưa kiểm chứng |
| REQ-LOGIN-41 | Tài khoản đang khoá cũng không đăng nhập được từ IP khác | CRM_LOGIN_TC_071 | — | — | 🟡 Thủ công · ⚪ chưa kiểm chứng |
| REQ-LOGIN-42 | Lần sai thứ 5 vẫn hiện thông báo chung; thông báo khoá hiện từ lần gửi thứ 6 | CRM_LOGIN_TC_060 | CL-regression_20261118-33 | — | 🟡 Thủ công · ⚪ chưa kiểm chứng |
| REQ-LOGIN-43 | Thử đăng nhập trong lúc khoá không gia hạn thời gian khoá | CRM_LOGIN_TC_064, CRM_LOGIN_TC_081 | CL-regression_20261118-37 | — | 🟡 Thủ công · ⚪ chưa kiểm chứng |
| REQ-LOGIN-44 | Gửi form với Password trống không tính là một lần đăng nhập sai | CRM_LOGIN_TC_067, CRM_LOGIN_TC_078 | — | — | 🟡 Thủ công · ⚪ chưa kiểm chứng |
| REQ-LOGIN-45 | Lần gửi bị từ chối do mã chống giả mạo sai không tính là một lần đăng nhập sai | CRM_LOGIN_TC_068, CRM_LOGIN_TC_078 | — | — | 🟡 Thủ công · ⚪ chưa kiểm chứng |
| REQ-LOGIN-46 | Lần sai ở email khác xen giữa không làm đứt chuỗi sai liên tiếp của một email | CRM_LOGIN_TC_069, CRM_LOGIN_TC_079 | — | — | 🟡 Thủ công · ⚪ chưa kiểm chứng |
| REQ-LOGIN-47 | Hết khoá thì bộ đếm lần sai về 0 | CRM_LOGIN_TC_065, CRM_LOGIN_TC_082 | CL-regression_20261118-38 | — | 🟡 Thủ công · ⚪ chưa kiểm chứng |

## 4. 🟡 TC chưa automate

| Priority | Automation = Yes | Partial | No | Tổng |
|---|:-:|:-:|:-:|:-:|
| Critical | 2 | 2 | 0 | 4 |
| High | 33 | 14 | 0 | 47 |
| Medium | 18 | 14 | 0 | 32 |
| Low | 0 | 1 | 0 | 1 |
| **Tổng** | **53** | **31** | **0** | **84** |

<details><summary>Danh sách đầy đủ 84 TC (xếp theo Priority) — kèm kết quả mới nhất</summary>

| TC ID | Priority | Automation dự kiến | Ghi chú |
|---|---|---|---|
| CRM_LOGIN_TC_005 | Critical | Yes | đã chạy — PASS (run_1794989188) |
| CRM_LOGIN_TC_007 | Critical | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_060 | Critical | Partial | chưa chạy |
| CRM_LOGIN_TC_062 | Critical | Partial | chưa chạy |
| CRM_LOGIN_TC_001 | High | Yes | đã chạy — BLOCKED (run_1794989188) |
| CRM_LOGIN_TC_002 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_003 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_004 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_006 | High | Yes | đã chạy — PASS (run_1794989188) |
| CRM_LOGIN_TC_008 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_009 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_010 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_011 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_012 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_013 | High | Yes | đã chạy — FAIL (run_1794303621) |
| CRM_LOGIN_TC_016 | High | Yes | đã chạy — BLOCKED (run_1794989188) |
| CRM_LOGIN_TC_018 | High | Partial | chưa chạy |
| CRM_LOGIN_TC_021 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_022 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_023 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_024 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_025 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_026 | High | Partial | chưa chạy |
| CRM_LOGIN_TC_027 | High | Partial | chưa chạy |
| CRM_LOGIN_TC_028 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_030 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_032 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_033 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_035 | High | Partial | chưa chạy |
| CRM_LOGIN_TC_036 | High | Yes | đã chạy — PASS (run_1794989188) |
| CRM_LOGIN_TC_039 | High | Yes | đã chạy — PASS (run_1794989188) |
| CRM_LOGIN_TC_040 | High | Yes | đã chạy — BLOCKED (run_1794989188) |
| CRM_LOGIN_TC_041 | High | Yes | đã chạy — BLOCKED (run_1794989188) |
| CRM_LOGIN_TC_042 | High | Yes | đã chạy — BLOCKED (run_1794989188) |
| CRM_LOGIN_TC_043 | High | Yes | đã chạy — PASS (run_1794989188) |
| CRM_LOGIN_TC_044 | High | Yes | đã chạy — PASS (run_1794989188) |
| CRM_LOGIN_TC_045 | High | Yes | đã chạy — PASS (run_1794989188) |
| CRM_LOGIN_TC_046 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_047 | High | Yes | đã chạy — FAIL (run_1794303621) |
| CRM_LOGIN_TC_048 | High | Yes | đã chạy — FAIL (run_1794303621) |
| CRM_LOGIN_TC_049 | High | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_061 | High | Partial | chưa chạy |
| CRM_LOGIN_TC_063 | High | Partial | chưa chạy |
| CRM_LOGIN_TC_066 | High | Partial | chưa chạy |
| CRM_LOGIN_TC_070 | High | Partial | chưa chạy |
| CRM_LOGIN_TC_071 | High | Partial | chưa chạy |
| CRM_LOGIN_TC_072 | High | Partial | chưa chạy |
| CRM_LOGIN_TC_074 | High | Partial | chưa chạy |
| CRM_LOGIN_TC_076 | High | Partial | chưa chạy |
| CRM_LOGIN_TC_077 | High | Partial | chưa chạy |
| CRM_LOGIN_TC_080 | High | Partial | chưa chạy |
| CRM_LOGIN_TC_014 | Medium | Yes | đã chạy — FAIL (run_1794303621) |
| CRM_LOGIN_TC_015 | Medium | Partial | chưa chạy |
| CRM_LOGIN_TC_017 | Medium | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_019 | Medium | Yes | đã chạy — BLOCKED (run_1794989188) |
| CRM_LOGIN_TC_020 | Medium | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_029 | Medium | Yes | đã chạy — PASS (run_1794989188) |
| CRM_LOGIN_TC_031 | Medium | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_034 | Medium | Yes | đã chạy — PASS (run_1794989188) |
| CRM_LOGIN_TC_037 | Medium | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_038 | Medium | Yes | đã chạy — BLOCKED (run_1794989188) |
| CRM_LOGIN_TC_050 | Medium | Yes | đã chạy — FAIL (run_1794303621) |
| CRM_LOGIN_TC_051 | Medium | Yes | đã chạy — PASS (run_1794989188) |
| CRM_LOGIN_TC_052 | Medium | Yes | đã chạy — FAIL (run_1794303621) |
| CRM_LOGIN_TC_054 | Medium | Yes | đã chạy — BLOCKED (run_1794989188) |
| CRM_LOGIN_TC_055 | Medium | Yes | đã chạy — PASS (run_1794303621) |
| CRM_LOGIN_TC_056 | Medium | Yes | đã chạy — BLOCKED (run_1794989188) |
| CRM_LOGIN_TC_057 | Medium | Yes | đã chạy — PASS (run_1794989188) |
| CRM_LOGIN_TC_058 | Medium | Yes | đã chạy — BLOCKED (run_1794989188) |
| CRM_LOGIN_TC_059 | Medium | Yes | đã chạy — PASS (run_1794989188) |
| CRM_LOGIN_TC_064 | Medium | Partial | chưa chạy |
| CRM_LOGIN_TC_065 | Medium | Partial | chưa chạy |
| CRM_LOGIN_TC_067 | Medium | Partial | chưa chạy |
| CRM_LOGIN_TC_068 | Medium | Partial | chưa chạy |
| CRM_LOGIN_TC_069 | Medium | Partial | chưa chạy |
| CRM_LOGIN_TC_073 | Medium | Partial | chưa chạy |
| CRM_LOGIN_TC_075 | Medium | Partial | chưa chạy |
| CRM_LOGIN_TC_078 | Medium | Partial | chưa chạy |
| CRM_LOGIN_TC_079 | Medium | Partial | chưa chạy |
| CRM_LOGIN_TC_081 | Medium | Partial | chưa chạy |
| CRM_LOGIN_TC_082 | Medium | Partial | chưa chạy |
| CRM_LOGIN_TC_083 | Medium | Partial | chưa chạy |
| CRM_LOGIN_TC_084 | Medium | Partial | chưa chạy |
| CRM_LOGIN_TC_053 | Low | Partial | đã chạy — BLOCKED (run_1794989188) |

</details>

## 5. Kiểm tra khác

| Hạng mục | Số lượng | Kết quả |
|---|:-:|---|
| ⏭️ REQ loại trừ | 0 | ✅ Không có — index TC không có bảng *REQ cố ý KHÔNG có TC*; ⚪ của module nghĩa là *chưa kiểm chứng*, không phải *chưa implement* |
| 🔴 REQ chưa có TC | 0 | ✅ Không có |
| 🟠 REQ chỉ có checklist | 0 | ✅ Không có — 6 REQ không có mục checklist (REQ-LOGIN-14, 15, 41, 44, 45, 46) vẫn có TC |
| ⚪ Orphan test (không map về REQ) | 0 | ✅ Không có — chưa có script automation |
| 🧩 TC trỏ tới REQ không tồn tại | 0 | ✅ Không có — 84/84 TC trỏ về REQ-LOGIN-01 → 47 |
| 🗑️ Script trỏ vào TC Deprecated | 0 | ✅ Không có — không có TC `@Deprecated`, không có script |
| ⚠️ Mapping suy luận cần xác nhận | 0 | ✅ Không có — 100% mapping theo ID |
