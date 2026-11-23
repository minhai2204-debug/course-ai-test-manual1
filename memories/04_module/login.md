---
name: login
description: Lịch sử và trạng thái module LOGIN — các lượt chạy workflow, ticket khoá tài khoản, bug, việc còn dở
type: project
cập nhật: 18-11-2026
---

# Module LOGIN

**Tài liệu:** [requirements](../../docs/requirements/login/REQUIREMENTS_LOGIN_SUMMARY.md) · [test cases](../../docs/testcases/login/TEST_CASES_LOGIN_SUMMARY.md) · [lần chạy run_1794303621](../../docs/executions/login/web/run_1794303621/execution_report.md) · [bug](../../docs/bugs/login/web/BUG_login_1794305372_TC050.md) · [checklist regression mới nhất 18-11](../../docs/checklists/login/web/checklist_regression_20261118.md) (bản 09-11 giữ làm lịch sử)

Số liệu hiện tại (REQ, TC, AMB) đọc ở danh mục `docs/*/README.md` — không chép sang đây.

## Dòng thời gian

| Ngày | Việc | Ghi chú cần nhớ |
|---|---|---|
| 02-11 | `/generate-requirements-from-website login` mode UI | User tự gõ mật khẩu theo Bước 1/2. Phát hiện: Forgot Password trả *"Email not found"* cả khi bỏ trống → lộ email tồn tại (AMB-LOGIN-05/06) — TC PASS theo hành vi hiện tại **không** có nghĩa là đúng |
| 05-11 | Đóng AMB-LOGIN-01 (chỉ có role admin) · Assumption tạm cho AMB còn treo | Impact `impact_AMB-LOGIN-01.md`, `impact_LOGIN-ASSUMPTIONS-05112026.md` |
| 09-11 | `/generate-testcases-from-requirements` GỘP → 55 TC · test data JSON · checklist regression | |
| 10-11 | `/review-testcases` REVIEW → FIX (áp nhóm A–D) · `/execute-test-cases` 34 TC (user tự đăng nhập 3 lần) · sửa Expected 4 TC giả định sai · bug viền focus | Bug: `a { outline: none }` trong `tailwind.css`, 🟡 Minor · P3, không đẩy Jira. TC_047-e chờ DevOps/PO xác nhận trang 403 |
| 11-11 | Ticket **khoá tài khoản** (5 lần sai/15 phút, khoá theo email, không theo IP; TC dùng tài khoản **Project Manager**, không dùng Admin) → REQ-LOGIN-35 → 47 · Assumption tạm cho AMB mới · `/update-testcases-from-impact` PLAN → APPLY · sinh TC bổ sung 060+ | Không có mã ticket → impact đặt tên `LOGIN-LOCKOUT-11112026`. 6 TC `@NeedsVerify` (thông báo khoá lấy từ ticket). Chạy hết nhóm khoá ~1 giờ 45 phút, tuần tự |
| 14-11 | Gộp 3 part → `web/test_cases_login_web.md` · bổ sung TC `@DBCheck` (mật khẩu băm D5, bộ đếm khoá D6) | Bản 3 part gốc chỉ còn ở scratchpad phiên cũ — coi như đã mất |
| 18-11 | `/generate-checklist-test` LOGIN → **Regression** (agent tự chọn loại, TC-based) · 39 mục · 41/47 REQ | Trạng thái mượn từ `run_1794303621`: 15 PASS · 2 FAIL (TC_013/014 — FAIL theo Expected cũ, đã sửa sau lần chạy) · 2 BLOCKED. Nhóm khoá tài khoản gom vào **một lượt khoá**, chạy các nhóm khác trong 16 phút chờ để vừa ~45 phút. Cắt REQ-14, 15, 41, 44, 45, 46 |
| 18-11 | `/generate-traceability-matrix login` (mục đích: báo cáo coverage trước release) → tạo mới `docs/traceability/` | RTM 2 tầng (chưa có script). 47/47 REQ có TC nhưng chỉ 34/84 TC từng chạy, 26/47 REQ chưa có TC nào chạy (STORY-03, 06 = 0). 22 REQ ⚪ = *chưa kiểm chứng*, **không** phải *chưa implement* → không xếp ⏭️. FAIL TC_013/014/048 xếp "chạy lại", không mở bug |
| 18-11 | `/execute-test-cases` 23 TC (20 chưa từng chạy + 3 BLOCKED cũ) → [`run_1794989188`](../../docs/executions/login/web/run_1794989188/execution_report.md): **12 PASS · 0 FAIL · 11 BLOCKED**, không video | Pane trình duyệt tích hợp, user gõ mật khẩu 10 lần. User chọn *"Chỉ chạy phần agent tự làm được"* → 019, 038, 042, 054 BLOCKED. TC_001/016/056 BLOCKED **lần 2** cùng nguyên nhân pane → giao chạy tay hoặc Playwright MCP. TC_043: trang từ chối là `419 Page Expired!` (không phải chữ ứng viên). TC_045 dùng chung lượt đăng nhập với TC_006 |
| 18-11 | `/generate-checklist-test LOGIN` lần 2 cùng ngày → **ghi đè** `checklist_regression_20261118.md` (cùng ngày, chưa ai tick) | Giữ nguyên 39 mục và thứ tự; trạng thái mượn từ 2 lần chạy: 29/39 (22 PASS · 2 FAIL · 5 BLOCKED). Thêm chú thích nhãn tiếng Việt (`Bảng tin` = Dashboard), mục 31 điền câu cảnh báo timer |

## Việc còn dở

- Chưa từng chạy (18-11-2026): 30 TC — khoá tài khoản 060 → 071 (thiếu 2 tài khoản PM; TC_071 cần thêm mạng IP khác), `@DBCheck` 072 → 084, tài khoản test 015, 018, 026, 027, 035. BLOCKED cần người/Playwright: 001, 016, 019, 038, 040, 041, 042, 053, 054, 056, 058.
- 7 TC dùng chung email sai (009, 013, 017, 021, 039, 047, 056) cần email riêng từng TC (AMB-LOGIN-23 chưa rõ email không tồn tại có bị khoá không).
- Chờ `/review-testcases` FIX: gỡ `@NeedsVerify` TC_020, 055, 034, 043, 057, 053; TC_034 điền câu cảnh báo + nút đóng `×`; TC_043 (và 036, 058) đổi chữ trang từ chối sang `419 Page Expired!`; Expected kiểm chữ `Dashboard` phụ thuộc ngôn ngữ tài khoản.
- `test_data_login_web.json` đã không còn trong `docs/` → sinh lại khi cần.
- REQ-LOGIN-23/24 (email đặt lại mật khẩu) không có đường kiểm chứng — chờ hộp thư test.
- Chưa có automation. RTM sinh lại 18-11-2026 15:43 sau `run_1794989188` (54/84 TC có kết quả, 17/47 REQ chưa có TC nào chạy) — sinh lại sau mỗi lần chạy TC mới.

Liên quan: [[quy-uoc-test-case]] · [[moi-truong-crm-dung-chung]] · [[backlog]]
