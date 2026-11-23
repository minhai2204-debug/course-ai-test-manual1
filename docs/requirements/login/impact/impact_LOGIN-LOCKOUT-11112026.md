## Impact Report — LOGIN-LOCKOUT-11112026 · 11-11-2026

> Ticket **"Khoá tài khoản khi đăng nhập sai nhiều lần"** do PO chốt. Ticket không mang mã và không ghi ngày chốt, nên dùng mã nội bộ `LOGIN-LOCKOUT-11112026` (cùng cách đặt tên với `LOGIN-ASSUMPTIONS-05112026`) và ghi nhận ngày 11-11-2026. Có mã Jira thật thì giữ nguyên mã nội bộ này trong Nhật ký và ghi thêm mã thật bên cạnh.
> ← [Index module `LOGIN`](../REQUIREMENTS_LOGIN_SUMMARY.md) · REQ chi tiết: [web/requirements_login_web.md — STORY-LOGIN-06](../web/requirements_login_web.md)

### Nội dung ticket → phân loại

| # | Gạch đầu dòng của ticket (nguyên văn) | Nhóm | REQ |
|---|---|---|---|
| AC#1 | Đăng nhập sai mật khẩu 5 lần liên tiếp với cùng một email thì tài khoản bị khoá 15 phút. | 🟢 Thêm — tách 2 rule: ngưỡng và thời hạn (skill 4.3.4) | REQ-LOGIN-35, 36 |
| AC#2 | Khi bị khoá, trang đăng nhập hiển thị: "Your account is locked. Please try again in 15 minutes." | 🟢 Thêm | REQ-LOGIN-37 |
| AC#3 | Trong thời gian bị khoá, nhập đúng mật khẩu cũng không đăng nhập được. | 🟢 Thêm | REQ-LOGIN-38 |
| AC#4 | Đăng nhập thành công trước khi đủ 5 lần thì bộ đếm lần sai được đặt lại về 0. | 🟢 Thêm | REQ-LOGIN-39 |
| AC#5 | Chỉ khoá theo email, không khoá theo IP. | 🟢 Thêm — tách 2 rule: email khác cùng IP không bị khoá · email bị khoá thì khoá ở mọi IP | REQ-LOGIN-40, 41 |
| AC#6 | Môi trường dùng chung: TC phải dùng tài khoản Project Manager, KHÔNG dùng tài khoản Admin. | Không cấp REQ — **ràng buộc kiểm thử**, không phải hành vi hệ thống | Ghi vào kết luận AMB-LOGIN-10, metadata Môi trường, RISK-LOGIN-01 · mở AMB-LOGIN-24 |

Trước khi xếp vào nhóm THÊM đã rà cả 34 REQ cũ: không REQ nào mô tả khoá tài khoản. Chính sách này trước đó chỉ là câu hỏi AMB-LOGIN-10. REQ gần nhất là REQ-LOGIN-30 (email tồn tại + sai mật khẩu); hành vi của nó không đổi, chỉ ghi rõ thêm phạm vi (xem ✏️ bên dưới).

### Tóm tắt

| Nhóm | Số lượng | REQ |
|---|---|---|
| 🟢 Thêm mới (trạng thái ⚪ — chưa kiểm chứng, chưa biết hệ thống đã build chưa) | 7 | REQ-LOGIN-35 → 41 |
| 🟡 Sửa | 0 | — |
| 🔴 Bỏ | 0 | — |
| ✏️ Biên tập (hành vi không đổi) | 1 | REQ-LOGIN-30 — thêm phạm vi "áp khi tài khoản chưa bị khoá, không gửi quá 4 lần sai liên tiếp" |
| ⏸️ Trùng, không tác động | 33 | REQ-LOGIN-01 → 29, 31 → 34 |

Sau cập nhật: 41 REQ = 🟢 25 · ⚪ 16. Thêm STORY-LOGIN-06. Mã kế tiếp: `REQ-LOGIN-42` · `AMB-LOGIN-27` · `RISK-LOGIN-09`.

### Test case cần xử lý

Đã rà theo cột `REQ ID` và dữ liệu test của [`part_01_web_chuc_nang.md`](../../../testcases/login/web/test_cases_login_web.md), [`part_02_web_ky_thuat_phi_chuc_nang.md`](../../../testcases/login/web/test_cases_login_web.md) và index [`TEST_CASES_LOGIN_SUMMARY.md`](../../../testcases/login/TEST_CASES_LOGIN_SUMMARY.md). Chưa có RTM.

| TC ID | REQ liên quan | Hành động | Lý do |
|---|---|---|---|
| CRM_LOGIN_TC_018 | REQ-LOGIN-30 | ⚠️ Review & sửa | Dựa trên Assumption tạm cũ của AMB-LOGIN-10: bước 6 ghi *"chính sách khoá thuộc AMB-LOGIN-10 (ngoài phạm vi TC)"*, ASM-07 ghi *"Ngưỡng khoá tài khoản (AMB-LOGIN-10 chưa rõ)"*. Nay đã chốt: 4 lần sai (biến thể `a`–`d`) **chưa** khoá, và lần đăng nhập đúng ở bước 6 đặt bộ đếm về 0 (REQ-LOGIN-39). Cần: (1) bỏ câu "ngoài phạm vi", sửa ASM-07 theo REQ-LOGIN-35, 39; (2) **cấm thêm biến thể thứ 5** — thêm là khoá `TK-TEST-01` 15 phút; (3) ticket yêu cầu TC đăng nhập sai bằng tài khoản thật phải dùng tài khoản Project Manager → xác định `TK-TEST-01` có phải tài khoản PM không (AMB-LOGIN-24) |
| CRM_LOGIN_TC_017 | REQ-LOGIN-07 | ⚠️ Review dữ liệu test | 6 biến thể `a`–`f` gửi mật khẩu sai **liên tiếp** cho cùng email `recon.khongtontai@example.invalid`. Nếu email không tồn tại cũng bị đếm (AMB-LOGIN-23), biến thể `f` (lần thứ 6) sẽ hiện thông báo khoá thay vì `Invalid email or password` → FAIL oan. Nên dùng email riêng cho từng biến thể (VD `recon.khongtontai+tc017f@example.invalid`) |
| CRM_LOGIN_TC_047 | REQ-LOGIN-07 | ⚠️ Review dữ liệu test | 5 biến thể `a`–`e` cùng email `recon.khongtontai@example.invalid` — chạm đúng ngưỡng 5; lý do như TC_017 |
| CRM_LOGIN_TC_009 · TC_013 · TC_021 · TC_039 · TC_056 | REQ-LOGIN-06, 07, 08 | ⚠️ Review dữ liệu test | Cùng dùng `recon.khongtontai@example.invalid` (TC_013 biến thể `c`, `e` chỉ khác hoa/thường và khoảng trắng; TC_056 gửi 2 lần nhờ F5). Từng TC chưa tới 5 lần, nhưng **Bộ chạy đề xuất số 2 chạy song song** → cộng dồn quá 5 lần trong 15 phút nếu email không tồn tại cũng bị đếm (AMB-LOGIN-23). TC_009 gửi Password trống — có được tính là lần sai không: AMB-LOGIN-22. Đổi sang email riêng từng TC thì không phụ thuộc câu trả lời |
| Index `TEST_CASES_LOGIN_SUMMARY.md` | REQ-LOGIN-35 → 41 | ⚠️ Sửa index TC | *Đối soát loại kiểm thử* ghi `Security · khoá tài khoản / brute-force — ⏭️ Cố ý bỏ (AMB-LOGIN-10, quyết định user 05-11-2026)`; *ISO 25010 · Security* ghi `Khoá tài khoản — AMB-LOGIN-10 ⏭️` → đổi thành có TC. Bảng quyết định R1–R9 thiếu điều kiện "tài khoản đang khoá". *Bộ chạy đề xuất* cần một bộ **tuần tự** riêng cho Story 06 (RISK-LOGIN-07) |
| — | REQ-LOGIN-35 → 41 | ➕ Viết mới | Yêu cầu mới, chưa có TC. Dùng tài khoản Project Manager, **không** dùng Admin. TC theo Assumption tạm của AMB-LOGIN-19 → 26 gắn nhãn `assumption-based`. Chạy tuần tự, mỗi TC bắt đầu bằng 1 lần đăng nhập đúng + Logout. BLOCKED khi chưa có tài khoản PM (AMB-LOGIN-24) |

**Đã rà, không tác động:** TC_043, TC_058 (mã chống giả mạo sai/hết hạn + tài khoản admin) — lần gửi bị từ chối do mã CSRF được giả định không tính vào bộ đếm (AMB-LOGIN-22 (b)); nếu PO trả lời ngược lại thì 2 TC này **không** được chạy lặp trên tài khoản admin. Các TC đăng nhập đúng bằng tài khoản admin không gửi mật khẩu sai cho email admin → không bị ảnh hưởng. TC Forgot Password (TC_022 → 027, 037, 048, 052) không phải lần đăng nhập sai.

### Ambiguity

| Mã | Chuyển trạng thái | Ghi chú |
|---|---|---|
| AMB-LOGIN-10 | ⏭️ → ✅ | PO chốt chính sách: 5 lần sai liên tiếp → khoá 15 phút, theo email. **Khác Assumption tạm** ("không viết TC khoá cho tới khi có môi trường riêng") → sinh REQ-LOGIN-35 → 41; TC khoá được viết trên môi trường dùng chung bằng tài khoản PM. TC dựa trên assumption cũ: CRM_LOGIN_TC_018 + index TC |
| AMB-LOGIN-19 | (mới) ❓ 🔴 | Lần sai thứ 5 hiện thông báo gì — `Invalid email or password` hay thông báo khoá |
| AMB-LOGIN-20 | (mới) ❓ 🟡 | 15 phút tính từ lần sai thứ 5 hay khoá trượt theo mỗi lần thử |
| AMB-LOGIN-21 | (mới) ❓ 🟡 | "15 minutes" trong thông báo là chữ cố định hay thời gian còn lại |
| AMB-LOGIN-22 | (mới) ❓ 🟡 | Lần gửi nào được tính là sai: Password trống · bị từ chối do CSRF · sai ở email khác xen giữa |
| AMB-LOGIN-23 | (mới) ❓ 🔴 | Email không tồn tại có bị "khoá" không — nếu không thì thông báo khoá cho biết email nào tồn tại |
| AMB-LOGIN-24 | (mới) ❓ 🔴 | Có role/tài khoản Project Manager không (trái kết luận tạm "chỉ có role admin" của AMB-LOGIN-01, 02); cần 2 tài khoản PM chỉ dành cho kiểm thử, lưu ở `.env` |
| AMB-LOGIN-25 | (mới) ❓ 🟡 | Hết khoá thì bộ đếm về 0 hay vẫn giữ |
| AMB-LOGIN-26 | (mới) ❓ 🟢 | Có mở khoá sớm được không (Forgot Password / admin mở khoá) |

### Rủi ro

| Mã | Thay đổi | Ghi chú |
|---|---|---|
| RISK-LOGIN-01 | ✏️ sửa mô tả + mitigation | Khoá tài khoản giờ là chính sách thật: không bao giờ gửi mật khẩu sai cho email admin; TC khoá dùng tài khoản PM |
| RISK-LOGIN-04 | ✏️ sửa mô tả + mitigation | Có khoá theo email nhưng không theo IP → password spraying (thử ít mật khẩu trên nhiều email) không bị chặn |
| RISK-LOGIN-07 | (mới) | TC khoá tài khoản giẫm lên nhau / khoá tài khoản PM của người khác — chạy tuần tự, đặt bộ đếm về 0 trước mỗi TC |
| RISK-LOGIN-08 | (mới) | Ai biết email cũng có thể cố ý khoá tài khoản người khác 15 phút, lặp lại được (từ chối dịch vụ) |

### Cảnh báo

- 🚫 **STORY-LOGIN-06 BLOCKED** cho tới khi có tài khoản Project Manager (AMB-LOGIN-24). Ticket cấm dùng tài khoản Admin. Hiện `.env` chỉ có `EMAIL_ADMIN` / `PASSWORD_ADMIN`.
- ⚠️ Ticket mâu thuẫn với kết luận tạm của AMB-LOGIN-01, 02 (05-11-2026: "tạm thời chỉ có role admin"). Chưa mở lại cột *Nhân viên role khác* của ma trận phân quyền; chờ câu trả lời AMB-LOGIN-24.
- ⚠️ Toàn bộ REQ-LOGIN-35 → 41 là ⚪ — **chưa ai quan sát** việc khoá trên hệ thống. TC đầu tiên chạy được cũng là lần kiểm chứng đầu tiên rằng tính năng đã được build.
- ⚠️ REQ-LOGIN-41 cần máy/mạng có IP khác; REQ-LOGIN-40 cần tài khoản PM thứ hai. Mỗi lượt chạy Story 06 tốn ≥ 15 phút chờ hết khoá.
