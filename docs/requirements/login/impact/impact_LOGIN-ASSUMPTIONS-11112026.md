## Impact Report — LOGIN-ASSUMPTIONS-11112026 · 11-11-2026

> Không có ticket. Nguồn là chỉ đạo của user: *"dùng Assumption tạm để trả lời cho các AMB"* — áp cho 8 AMB còn ❓ sinh ra từ ticket khoá tài khoản ([impact_LOGIN-LOCKOUT-11112026.md](impact_LOGIN-LOCKOUT-11112026.md)).
> ← [Index module `LOGIN`](../REQUIREMENTS_LOGIN_SUMMARY.md) · REQ chi tiết: [web/requirements_login_web.md — STORY-LOGIN-06](../web/requirements_login_web.md)

### Tóm tắt

| Nhóm | Số lượng | REQ |
|---|---|---|
| 🟢 Thêm mới (trạng thái ⚪ — chưa kiểm chứng) | 6 | REQ-LOGIN-42 → 47 |
| 🟡 Sửa | 0 | — |
| 🔴 Bỏ | 0 | — |
| ✏️ Biên tập (giữ ⚪, chưa có TC) | 2 | REQ-LOGIN-35 (trỏ sang REQ-LOGIN-42, 44 → 46) · REQ-LOGIN-37 (assert nguyên văn thông báo khoá) |
| ⏸️ Trùng, không tác động | 39 | REQ-LOGIN-01 → 34, 36, 38 → 41 |

Sau cập nhật: 47 REQ = 🟢 25 · ⚪ 22. STORY-LOGIN-06 có 13 REQ. Mã kế tiếp: `REQ-LOGIN-48` · `AMB-LOGIN-27` · `RISK-LOGIN-09`.

### Test case cần xử lý

| TC ID | REQ liên quan | Hành động | Lý do |
|---|---|---|---|
| — | REQ-LOGIN-35 → 47 | ➕ Viết mới, nhãn `assumption-based` | Chưa có TC nào cho STORY-LOGIN-06. Dùng tài khoản Project Manager, không dùng Admin; chạy tuần tự (RISK-LOGIN-07) |
| CRM_LOGIN_TC_009 | REQ-LOGIN-06 | ⚠️ Review dữ liệu test (giữ nguyên từ impact trước, đổi lý do) | Theo Assumption tạm AMB-LOGIN-22, Password trống **không** tính là lần sai → hết rủi ro ở điểm này. Vẫn còn rủi ro theo AMB-LOGIN-23 (email không tồn tại có bị đếm không — vẫn chưa biết) |
| CRM_LOGIN_TC_013 · 017 · 021 · 039 · 047 · 056 | REQ-LOGIN-07, 08 | ⚠️ Review dữ liệu test (không đổi) | AMB-LOGIN-23 chốt ⏭️ mà **không** có hành vi giả định → vẫn phải đổi sang email không tồn tại riêng từng TC/biến thể |
| CRM_LOGIN_TC_018 | REQ-LOGIN-30 | ⚠️ Review & sửa (không đổi) | Như impact `LOGIN-LOCKOUT-11112026`. Thêm: theo Assumption tạm AMB-LOGIN-24, `TK-TEST-01` nên là tài khoản Project Manager hoặc được thay bằng tài khoản PM |
| CRM_LOGIN_TC_043 · 058 | REQ-LOGIN-14 | ⏸️ Không tác động | Theo Assumption tạm AMB-LOGIN-22 (b), lần bị từ chối do mã chống giả mạo không tính là lần sai (REQ-LOGIN-45) → chạy lặp trên tài khoản admin vẫn an toàn **nếu** giả định đúng |

### Ambiguity

Mọi dòng dưới đây chuyển từ ❓ sang ⏭️: **test theo Assumption tạm và chấp nhận rủi ro. Không phải câu trả lời thật.**

| Mã | Mức | Assumption được dùng | Hệ quả |
|---|---|---|---|
| AMB-LOGIN-19 | 🔴 | Lần sai thứ 5 vẫn "Invalid email or password"; thông báo khoá từ lần gửi thứ 6 | REQ-LOGIN-42 ⚪ |
| AMB-LOGIN-20 | 🟡 | 15 phút tính từ lần sai thứ 5, thử lại không gia hạn | REQ-LOGIN-43 ⚪. TC REQ-LOGIN-36, 38 vẫn chờ theo cách an toàn |
| AMB-LOGIN-21 | 🟡 | "15 minutes" là chữ cố định | REQ-LOGIN-37 assert nguyên văn |
| AMB-LOGIN-22 | 🟡 | Chỉ tính lần gửi có mật khẩu sai; Password trống và lần bị từ chối do mã chống giả mạo không tính; bộ đếm riêng từng email | REQ-LOGIN-44, 45, 46 ⚪ |
| AMB-LOGIN-23 | 🔴 | **Không có hành vi giả định** — né bằng dữ liệu test riêng từng TC | Không cấp REQ. Rủi ro dò tài khoản qua thông báo khoá **chưa xử lý** (RISK-LOGIN-02) |
| AMB-LOGIN-24 | 🔴 | Có role Project Manager; sẽ có 2 tài khoản PM chỉ dành cho kiểm thử ở `.env` | Ma trận phân quyền mở lại cột *Nhân viên role khác (Project Manager)* thành ❔ (3 ô). **Tài khoản chưa có thật** → TC Story 06 vẫn BLOCKED khi chạy |
| AMB-LOGIN-25 | 🟡 | Hết khoá thì bộ đếm về 0 | REQ-LOGIN-47 ⚪ |
| AMB-LOGIN-26 | 🟢 | Không có cách mở khoá sớm — chờ đủ 15 phút | Không cấp REQ (không kiểm chứng được bằng quyền hiện có). Bước dọn dẹp của TC Story 06 = chờ 15 phút |

### Cảnh báo

- 🚫 Chốt Assumption tạm cho AMB-LOGIN-24 **không tạo ra tài khoản**. Cần người quản trị cấp 2 tài khoản Project Manager và thêm vào `.env` (VD `EMAIL_PM_1`, `PASSWORD_PM_1`, `EMAIL_PM_2`, `PASSWORD_PM_2`) — agent không tự ghi giá trị.
- ⚠️ 22/47 REQ của module là ⚪. Riêng STORY-LOGIN-06 (13 REQ) **chưa ai quan sát** trên hệ thống — kể cả việc tính năng khoá đã được build.
- ⚠️ 3 AMB 🔴 (19, 23, 24) không còn ở mục *Ambiguity 🔴 High còn treo* của danh mục, nhưng **chưa có câu trả lời thật**. AMB-LOGIN-23 để lại một rủi ro bảo mật chưa được kiểm.
