# Kế hoạch cập nhật TC — LOGIN-LOCKOUT-11112026 · module `login`

> **Mode PLAN — chưa sửa TC nào.** Kế hoạch này chờ user duyệt rồi mới chạy APPLY.
> ← [Index TC `TEST_CASES_LOGIN_SUMMARY.md`](../TEST_CASES_LOGIN_SUMMARY.md)

| Mục | Giá trị |
|---|---|
| Ticket | Khoá tài khoản khi đăng nhập sai nhiều lần — mã nội bộ `LOGIN-LOCKOUT-11112026` (ticket không mang mã) |
| Impact Report nguồn | [`impact_LOGIN-LOCKOUT-11112026.md`](../../../requirements/login/impact/impact_LOGIN-LOCKOUT-11112026.md) · [`impact_LOGIN-ASSUMPTIONS-11112026.md`](../../../requirements/login/impact/impact_LOGIN-ASSUMPTIONS-11112026.md) — report thứ hai là phần chốt Assumption tạm cho AMB của **chính ticket này**, nên gộp chung một kế hoạch. APPLY sẽ ghi `delta_tc_LOGIN-LOCKOUT-11112026.md` |
| Requirements đã đọc | Index `REQUIREMENTS_LOGIN_SUMMARY.md` + `web/requirements_login_web.md` — REQ-LOGIN-35 → 47 (STORY-LOGIN-06), REQ-LOGIN-30, Nhật ký 11-11-2026 |
| Bộ TC hiện hành | 59 TC · 129 biến thể · độ hạt **GỘP** · 1 nền tảng (web) · `part_01_web_chuc_nang.md` (46 TC) · `part_02_web_ky_thuat_phi_chuc_nang.md` (13 TC) |
| Nguồn map REQ ↔ TC | Cột `REQ ID` của 2 part + Bảng Đối Soát Coverage của index. **Chưa có RTM** (`docs/traceability/` chưa tồn tại) |
| ⚠️ Mốc git | `docs/testcases/` **chưa được git theo dõi** (`git status`: `?? docs/testcases/`) → APPLY sẽ **không có mốc git** để đối chiếu bản cũ. Đề nghị user commit `docs/testcases/` trước khi duyệt APPLY — agent không tự commit |

## 1. Bảng ánh xạ REQ → TC

### ✅ Chắc chắn (theo cột `REQ ID`)

| REQ | Đổi gì | TC map được |
|---|---|---|
| REQ-LOGIN-30 (✏️ biên tập, giữ ⚪) | AC thêm phạm vi: áp khi tài khoản chưa bị khoá; không gửi quá 4 lần sai liên tiếp | CRM_LOGIN_TC_018 |
| REQ-LOGIN-07 (không đổi) | Không đổi nội dung — nhưng mỗi lần gửi sai giờ có thể được **đếm** vào bộ đếm khoá (AMB-LOGIN-23 vẫn chưa biết email không tồn tại có bị đếm không) | CRM_LOGIN_TC_013, 017, 039, 047, 056 dùng lặp `recon.khongtontai@example.invalid` |

### ⚠️ Suy luận — cần user xác nhận

| REQ / AMB | TC | Căn cứ suy luận |
|---|---|---|
| AMB-LOGIN-24 (Assumption: có role Project Manager) + ticket gạch đầu dòng 6 (*"TC phải dùng tài khoản Project Manager"*) | CRM_LOGIN_TC_018 | TC_018 gửi mật khẩu sai cho tài khoản có thật (`TK-TEST-01`). Ticket nói về TC khoá tài khoản; TC_018 không phải TC khoá nhưng cũng đẩy bộ đếm lên 4. **Đề xuất giữ `TK-TEST-01`** — đây là tài khoản test riêng, không phải Admin dùng chung, và tách khỏi tài khoản PM của Story 06 thì hai bên không khoá lẫn nhau (RISK-LOGIN-07). Cần user xác nhận |

### ❓ Chưa có TC → ngoài phạm vi DELTA

| REQ | Số REQ | Lý do |
|---|:-:|---|
| REQ-LOGIN-35 → 47 | 13 | REQ 🟢 mới (trạng thái ⚪) của STORY-LOGIN-06 — chưa có TC nào |

## 2. Kế hoạch sửa từng TC

| # | TC ID | File · dòng | Vòng · Nhánh | Sửa ô nào | Sửa thế nào | Mở evidence? |
|:-:|---|---|---|---|---|:-:|
| 1 | CRM_LOGIN_TC_018 | `web/parts/part_01_web_chuc_nang.md:41` | V2 · Validation (Password) · Business Rule | `Pre-Condition` · `Test Steps` (bước 6) · `Expected Result` (bước 6) | **Pre-Condition:** thêm *"bộ đếm sai của `TK-TEST-01` đang ở 0 — đăng nhập đúng `TK-TEST-01` rồi Logout trước bước 1"*. Nếu thiếu bước này, một lần chạy hỏng giữa chừng để lại 1–4 lần sai, và lần chạy lại sẽ khoá `TK-TEST-01` ở biến thể đầu (REQ-LOGIN-35). Thêm câu *"**không** thêm biến thể thứ 5 — 5 lần sai liên tiếp khoá tài khoản 15 phút"*. **Bước 6** vẫn là dọn dẹp, không chấm; bỏ câu *"chính sách khoá thuộc AMB-LOGIN-10 (ngoài phạm vi TC)"*. Thay bằng: *đăng nhập đúng để đưa bộ đếm về 0 (REQ-LOGIN-39); sau 4 lần sai tài khoản chưa bị khoá (REQ-LOGIN-35). Bị khoá → ghi nhận lệch so với REQ-LOGIN-35, chờ 15 phút rồi đăng nhập lại để dọn* | ❌ (không thuộc 4 nhóm V1) |
| 2 | CRM_LOGIN_TC_017 | `part_01:40` | V2 · EP / BVA (Password) | `Test Steps` (bước 2) · `Test Data` | 6 biến thể `a`–`f` hiện gửi sai **liên tiếp** cho cùng một email. Sửa thành mỗi biến thể một email riêng: `recon.khongtontai.tc017a@example.invalid` … `…tc017f@…`. Expected không đổi | ❌ |
| 3 | CRM_LOGIN_TC_047 | `part_02:21` | V3 · Security (SQLi/XSS Password) | `Test Steps` (bước 2) · `Test Data` | 5 biến thể cùng email — đúng ngưỡng 5. Sửa thành mỗi biến thể một email riêng: `recon.khongtontai.tc047a@example.invalid` … `…tc047e@…`. Expected không đổi | ❌ |
| 4 | CRM_LOGIN_TC_013 | `part_01:36` | V2 · Validation · EP (Email) | `Test Data` (biến thể `a`, `c`, `e`) | Đổi `recon.khongtontai@example.invalid` → `recon.khongtontai.tc013@example.invalid`. Biến thể `c` viết hoa và `e` thêm khoảng trắng **của cùng email đó**, vì chúng kiểm hoa/thường và khoảng trắng — 3 lần/lượt chạy, dưới ngưỡng. `b`, `f` đã có email riêng | ❌ |
| 5 | CRM_LOGIN_TC_039 | `part_01:70` | V2 · Use Case | `Test Steps` (bước 2, 6) · `Test Data` | Đổi sang `recon.khongtontai.tc039@example.invalid` — 1 lần sai Login + 1 lần Forgot. Forgot không phải lần đăng nhập sai | ❌ |
| 6 | CRM_LOGIN_TC_056 | `part_01:74` | V2 · Error Guessing | `Test Steps` (bước 2) · `Test Data` | Đổi sang `recon.khongtontai.tc056@example.invalid` — 2 lần/lượt (gửi + F5 gửi lại) | ❌ |
| 7 | Quy ước chung của Part 01 | `part_01:10` | — | Ô `Quy ước chung` | Thêm: *"Case sai dùng email đuôi `@example.invalid`, **mỗi TC (TC nhiều lần gửi: mỗi biến thể) một email riêng** — lần sai có thể bị đếm vào bộ đếm khoá 5 lần (REQ-LOGIN-35, AMB-LOGIN-23). **Không bao giờ** gửi mật khẩu sai cho email admin"* | ❌ |

> Độ hạt GỘP giữ nguyên: không tách biến thể nào thành TC mới, không TC nào vượt 6 biến thể. **Không đổi TC ID**, không thêm TC trong lượt DELTA này.

### TC đã rà — không sửa

| TC | Lý do không sửa |
|---|---|
| CRM_LOGIN_TC_009 | Mọi biến thể gửi Password **trống / toàn khoảng trắng** → máy chủ coi là trống (ASM-04) → theo REQ-LOGIN-44 không tính là lần sai. *Impact Report `LOGIN-ASSUMPTIONS-11112026` vẫn xếp TC này vào nhóm ⚠️ review vì AMB-LOGIN-23 — đó là nhầm; REQ-LOGIN-44 đã loại TC này khỏi rủi ro* |
| CRM_LOGIN_TC_021 | Chỉ còn biến thể `a` (Password trống) → như TC_009. *Impact Report `LOGIN-LOCKOUT-11112026` xếp vào ⚠️ review — sau REQ-LOGIN-44 thì không cần* |
| CRM_LOGIN_TC_010 | Email trống → không có email nào để đếm |
| CRM_LOGIN_TC_014, 046, 059 | Mỗi biến thể đã dùng một email khác nhau |
| CRM_LOGIN_TC_042 | 1 lần gửi/lượt với email Contact. Chỉ chạm ngưỡng khi chạy lại ≥ 5 lần trong 15 phút — không sửa, ghi vào *Bộ chạy đề xuất* |
| CRM_LOGIN_TC_027 | Bước 13–14 sai 1 lần với `TK-TEST-03`, bước 15 đăng nhập đúng đưa bộ đếm về 0 (REQ-LOGIN-39) |
| CRM_LOGIN_TC_043, 058 | Bị từ chối do mã chống giả mạo → theo REQ-LOGIN-45 không tính là lần sai; mỗi lượt chạy chỉ một lần trên tài khoản admin |
| TC đăng nhập đúng bằng admin (005, 006, 019, 029, 036, 038, 051…) | Không gửi mật khẩu sai cho email admin |

## 3. Cập nhật ở index `TEST_CASES_LOGIN_SUMMARY.md` (APPLY)

| Mục | Sửa gì |
|---|---|
| Bảng đầu — `Nguồn requirement` | `REQ-LOGIN-01` → `REQ-LOGIN-47` (bản 11-11-2026) |
| Bảng đầu — `Mức rủi ro · độ sâu` | Bỏ điều kiện *"có môi trường riêng → mở nhánh khoá tài khoản (AMB-LOGIN-10)"*; thay bằng *"khoá tài khoản đã chốt theo ticket — TC sinh ở lượt BỔ SUNG"* |
| Bảng đầu — `Phạm vi REQ` | `34/34` → `34/47 REQ có TC` · 13 REQ (35 → 47) chưa có TC — ngoài phạm vi DELTA |
| ASM-07 | Ngưỡng khoá: **5 lần** sai liên tiếp (REQ-LOGIN-35), 4 lần chưa khoá, đăng nhập đúng đưa bộ đếm về 0 (REQ-LOGIN-39) · TC_018 bắt đầu bằng 1 lần đăng nhập đúng |
| ASM-28 (mới) | Email không tồn tại có bị đếm vào bộ đếm khoá không — chưa biết (AMB-LOGIN-23) → mỗi TC/biến thể dùng email riêng. Ảnh hưởng: TC_013, 017, 039, 047, 056 |
| Bảng quyết định | Thêm điều kiện **Tài khoản đang khoá**: R6 ghi rõ *"lần sai thứ 1–5"* (lần thứ 5 vẫn `Invalid email or password` — REQ-LOGIN-42) · **R10** tài khoản đang khoá + mật khẩu đúng/sai → thông báo khoá — TC phủ: *chưa có (➕)* |
| Bảng chuyển trạng thái phiên | Thêm **S11** đếm sai 4 → sai lần 5 → khoá · **S12** đang khoá → đăng nhập → vẫn khoá, không gia hạn · **S13** hết 15 phút → đăng nhập được, bộ đếm về 0 · **S14** đếm sai 1–4 → đăng nhập đúng → bộ đếm về 0 — TC phủ: *chưa có (➕)* |
| Bảng Đối Soát Coverage | REQ-LOGIN-30: thêm ghi chú *"bắt đầu bằng 1 lần đăng nhập đúng; tối đa 4 lần sai/lượt"* · thêm 13 dòng REQ-LOGIN-35 → 47: `0 TC — ⚪ ngoài phạm vi DELTA, sinh bổ sung` · dòng Tổng → `34/47` |
| Đối soát loại kiểm thử (4 vòng) | Xem mục 4 |
| ISO 25010 · Security | *"Khoá tài khoản — AMB-LOGIN-10 ⏭️"* → *"Khoá tài khoản — REQ-LOGIN-35 → 47, chưa có TC (sinh bổ sung)"* |
| Đối soát cột Automation | Điều kiện mới **#6** *2 tài khoản Project Manager chỉ dành cho kiểm thử (AMB-LOGIN-24)* — ⏳ chưa có. TC_018 vẫn `Partial` |
| Bộ chạy đề xuất | Nhóm 3: TC_018 bắt đầu bằng 1 lần đăng nhập đúng `TK-TEST-01` · lưu ý TC_042 không chạy lại quá 4 lần trong 15 phút · thêm dòng giữ chỗ **nhóm khoá tài khoản — tuần tự, tài khoản PM** cho TC sinh bổ sung (RISK-LOGIN-07) |
| Điểm cần user review | Thêm: tài khoản PM chưa có · AMB-LOGIN-23 (dò email qua thông báo khoá) chưa có câu trả lời thật |
| Nhật ký thay đổi | 1 dòng cho lượt APPLY |
| `docs/testcases/README.md` | Cập nhật REQ bao phủ `34/47`, ngày cập nhật. Số TC không đổi (59) |

## 4. Nhánh 4 vòng bị ticket chạm tới

```
Nhánh bị chạm: V2 · Validation (TC_013, 017, 018) · V2 · Business Rule (TC_018) · V2 · Decision Table (R6, R10)
               · V2 · State Transition (S11–S14) · V2 · Use Case (TC_039) · V2 · Error Guessing (TC_056)
               · V3 · Security (TC_047 · nhánh "khoá tài khoản / brute-force") · V3 · Permission (role Project Manager)
Nhánh KHÔNG đụng: toàn bộ V1 · V2 UI Behavior, Required, Dependency, Save/Edit/Delete · V3 API, Database, Integration, Logging · toàn bộ V4
```

**Vì sao V1 không bị chạm:** ticket không thêm, bớt hay đổi nhãn thành phần nào của form Login ở trạng thái mặc định (TC_001). Thông báo khoá chỉ hiện khi tài khoản đang bị khoá, tức thuộc trạng thái của V2 / V3, không thuộc bảng kiểm màn hình mặc định. Vì vậy không cần mở evidence. Hiện cũng **chưa có ảnh** thông báo khoá: TC sinh bổ sung cho REQ-LOGIN-37 sẽ phải gắn `@NeedsVerify`.

| Vòng · Nhánh | Hiện tại | Sau APPLY |
|---|---|---|
| 2 · Decision Table | ✅ R1–R9 + R4b | 🟡 Nông — R10 (tài khoản khoá) chưa có TC |
| 2 · State Transition | 🟡 Nông (S3) | 🟡 Nông — thêm S11–S14 chưa có TC |
| 3 · Security · khoá tài khoản / brute-force | ⏭️ Cố ý bỏ (AMB-LOGIN-10) | 🔴 Thiếu — chính sách đã chốt, REQ-LOGIN-35 → 47 chưa có TC. **Không** giữ ⏭️ vì căn cứ của quyết định (chưa biết chính sách, chờ môi trường riêng) không còn |
| 3 · Permission | ✅ (1 role nhân viên) | 🟡 Nông — Assumption tạm AMB-LOGIN-24 có role Project Manager, nhưng requirements chưa có REQ nào riêng cho *PM × đăng nhập / đăng xuất* (ma trận phân quyền ❔). Bổ sung REQ trước rồi mới viết TC |
| 2 · Validation · EP · Use Case · Error Guessing · 3 · Security | ✅ | ✅ — chỉ đổi dữ liệu test, dải TC và số biến thể không đổi |

> Hai dòng 🔴 / 🟡 mới là việc **ngoài phạm vi DELTA**: REQ 🟢 thì sinh TC ở lượt BỔ SUNG; Permission thì cần REQ trước. Gate #5 của DELTA chỉ yêu cầu chấm đúng nhánh bị chạm, không yêu cầu lấp ở lượt này.

## 5. Tác động lan toả

| Câu hỏi | Kết quả |
|---|---|
| Ticket có đụng thứ nhìn thấy trên màn hình mặc định không? | Không — xem mục 4 |
| TC nào dùng dữ liệu bị đổi nghĩa ở bước phụ? | Các TC gửi sai lặp cùng một email (TC_013, 017, 039, 047, 056 — sửa ở mục 2) · TC_018 chạy lại sau khi hỏng giữa chừng (sửa Pre-Condition) |
| Chạy song song (*Bộ chạy đề xuất* nhóm 2) có cộng dồn lần sai không? | Có, trước khi sửa: 5 TC trên cùng gửi tổng cộng **17 lần sai** cho `recon.khongtontai@example.invalid` trong một lượt. Sau khi đổi sang email riêng, mỗi email ≤ 3 lần/lượt |
| TC nào bị Deprecated / lấy TC Deprecated làm precondition? | Không có — ticket không gỡ chức năng nào |
| Số TC có vượt ngưỡng tách? | Không — lượt này không thêm TC (part_01 46 · part_02 13). Lượt BỔ SUNG cho 13 REQ dự kiến 6–8 TC (độ hạt GỘP) → part_01 lên 52–54, **vượt ngưỡng 50** → nên mở `part_03_web_khoa_tai_khoan.md` |

## 6. Ngoài phạm vi — việc tiếp theo

| Việc | Phạm vi | Command |
|---|---|---|
| Sinh TC cho STORY-LOGIN-06 (chế độ BỔ SUNG, TC ID nối từ `CRM_LOGIN_TC_060`, độ hạt GỘP, tài khoản PM, nhóm chạy tuần tự) | REQ-LOGIN-35 → 47 | `/generate-testcases-from-requirements` |
| Bổ sung REQ *Project Manager × đăng nhập / đăng xuất* rồi viết TC Permission | V3 · Permission | `/update-requirements-from-ticket` → sinh bổ sung |
| Recon thông báo khoá khi có tài khoản PM | Evidence cho REQ-LOGIN-37, 42 | `/generate-requirements-from-website login` (cập nhật evidence) |
| Đồng bộ automation (nếu đã có script cho TC_013, 017, 018, 039, 047, 056) | Sau APPLY | `/update-automation-from-impact` |
| Dựng RTM lần đầu | Module `login` | `/generate-traceability-matrix login` |
