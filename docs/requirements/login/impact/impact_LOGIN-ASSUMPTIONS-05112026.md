## Impact Report — LOGIN-ASSUMPTIONS-05112026 · 05-11-2026

> Không có ticket. Nguồn là chỉ đạo của user: *"dùng Assumption tạm làm cho AMB còn treo"*.
> ← [Index module `LOGIN`](../REQUIREMENTS_LOGIN_SUMMARY.md)

### Tóm tắt

| Nhóm | Số lượng | REQ |
|---|---|---|
| 🟢 Thêm mới (trạng thái ⚪ — chưa kiểm chứng) | 6 | REQ-LOGIN-29 → 34 |
| 🟡 Sửa | 0 | — |
| 🔴 Bỏ | 0 | — |
| ⏸️ Trùng, không tác động | 28 | REQ-LOGIN-01 → 28 |

Sau cập nhật: 34 REQ = 🟢 25 · ⚪ 9. Mã kế tiếp: `REQ-LOGIN-35` · `AMB-LOGIN-19` · `RISK-LOGIN-07`.

### Test case cần xử lý

Chưa có `docs/testcases/` và chưa có RTM, nên không có TC nào cần sửa hay deprecated.

| TC ID | REQ liên quan | Hành động | Lý do |
|---|---|---|---|
| — | REQ-LOGIN-29 → 34 | ➕ Viết mới, nhãn `assumption-based` | Hành vi giả định, chưa từng quan sát trên hệ thống |
| — | REQ-LOGIN-16, 23, 24 | ➕ Viết mới, nhãn `assumption-based` | ⚪ từ đợt trước, nay theo Assumption tạm |

### Ambiguity

Mọi dòng dưới đây chuyển từ ❓ sang ⏭️: **test theo Assumption tạm và chấp nhận rủi ro. Không phải câu trả lời thật.**

| Mã | Mức | Assumption được dùng | Hệ quả |
|---|---|---|---|
| AMB-LOGIN-03 | 🔴 | Contact không đăng nhập được vào `/admin` | → REQ-LOGIN-29 ⚪. Ô phân quyền giữ ❔ |
| AMB-LOGIN-04 | 🟡 | Không assert thứ tự thông báo | Không REQ mới |
| AMB-LOGIN-05 | 🔴 | Giữ hành vi hiện tại, nghi là lỗi | REQ-LOGIN-20 giữ nguyên |
| AMB-LOGIN-06 | 🔴 | Hành vi hiện tại là thật, đánh dấu rủi ro | REQ-LOGIN-21 giữ nguyên |
| AMB-LOGIN-07 | 🟡 | Test đúng hành vi hiện tại từng màn | REQ-LOGIN-08, 22 giữ nguyên |
| AMB-LOGIN-08 | 🟡 | Hành vi hiện tại là đúng | REQ-LOGIN-10 giữ nguyên |
| AMB-LOGIN-09 | 🟡 | AC chỉ assert điểm dừng | Không REQ mới |
| AMB-LOGIN-10 | 🔴 | Không viết TC khoá tài khoản cho tới khi có môi trường riêng | Không REQ mới |
| AMB-LOGIN-11 | 🟡 | Cùng thông báo với REQ-LOGIN-07 | → REQ-LOGIN-30 ⚪ |
| AMB-LOGIN-12 | 🔴 | Cookie khôi phục phiên trong 62 ngày | REQ-LOGIN-16 giữ ⚪ |
| AMB-LOGIN-13 | 🟡 | Gửi email kèm link đặt lại | REQ-LOGIN-23, 24 giữ ⚪ |
| AMB-LOGIN-14 | 🟡 | Có popup cảnh báo, không đăng xuất | → REQ-LOGIN-34 ⚪ |
| AMB-LOGIN-15 | 🟡 | Có bước nhập mã sau mật khẩu | → REQ-LOGIN-32 ⚪ |
| AMB-LOGIN-16 | 🟢 | Hành vi hiện tại | REQ-LOGIN-18 giữ nguyên |
| AMB-LOGIN-17 | 🟢 | Chỉ hiện thông báo Email | → REQ-LOGIN-31 ⚪ |
| AMB-LOGIN-18 | 🟡 | Không tạo cookie | → REQ-LOGIN-33 ⚪ |

Không đổi: `AMB-SYS-01, 03, 04` — cấp hệ thống, không có Assumption tạm để dùng.

### Cảnh báo

- ⚠️ **TC PASS trên AMB-LOGIN-05, 06 không có nghĩa hành vi đúng.** Hai chỗ này vẫn nghi là lỗi và rủi ro bảo mật: Forgot Password trả "Email not found" khi bỏ trống, và để lộ email nào có trong hệ thống. Nên báo dev riêng thay vì chỉ ghi vào bộ TC.
- ⚠️ **AMB-LOGIN-10 không có đáp án.** Chính sách khoá tài khoản vẫn chưa biết; Assumption chỉ quyết định tạm không viết TC. RISK-LOGIN-01, 04 giữ nguyên.
- ⚠️ **Nếu sau này có câu trả lời khác Assumption tạm**, mọi TC `assumption-based` liên quan phải sửa. AMB ⏭️ được giữ lại trong bảng để truy được quyết định này.
- ⚠️ **REQ-LOGIN-29 → 34 chưa ai quan sát trên hệ thống.** Chạy được cần: account Contact (29) · tài khoản test riêng (30) · người gõ mật khẩu (31) · tài khoản bật 2FA (32) · đăng nhập không tick Remember me (33) · timer đang chạy (34).
