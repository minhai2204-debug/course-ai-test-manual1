---
name: quy-uoc-test-case
description: Quy ước sinh / sửa test case user đã chốt — 1 file mỗi nền tảng, độ hạt GỘP, Assumption tạm, bổ sung thay vì sinh lại
type: feedback
cập nhật: 18-11-2026
---

# Quy ước test case

## 1 file TC mỗi nền tảng — không chia `parts/`

User 14-11-2026: *"mục sinh test case tôi không muốn chia thành nhiều parts … toàn bộ testcases sinh ra chỉ lưu vào 1 file duy nhất, định dạng file vẫn như cũ"*. Skill/command đã sửa theo; bộ LOGIN đã gộp từ 3 part thành `web/test_cases_login_web.md`.

**How to apply:** mọi bộ TC mới / bổ sung ghi vào **đúng một** `test_cases_<module>_<nền-tảng>.md`, kể cả khi vượt 50 TC. `stories/` của requirements và `parts/` của User Guide **không** bị ảnh hưởng. Link cũ trong tài liệu lịch sử (execution report, review, impact) đã được trỏ sang file mới, chữ hiển thị giữ tên part cũ.

## Độ hạt GỘP

Cả LOGIN (09-11) và CUST (16-11) đều chọn **GỘP** (một TC nhiều biến thể `-a`, `-b`…). Hỏi lại chỉ khi user tự nêu khác.

## Đóng AMB bằng Assumption tạm

User nhiều lần (05-11, 11-11, 16-11) chọn *"dùng Assumption tạm"* / *"Theo giả định"* thay vì chờ PO. Khi làm: ghi ⏭️ theo Assumption, TC dựa trên giả định gắn `@NeedsVerify`, nói rõ trong báo cáo đây **không** phải đáp án thật (VD AMB-LOGIN-10 chính sách khoá vẫn chưa biết). Ô phân quyền chưa kiểm chứng giữ ❔, không đổi thành ❌.

## Bộ TC đã có lần chạy → bổ sung, không sinh lại

14-11-2026 user muốn "generate lại" LOGIN để thêm kiểm DB; vì đã có `run_1794303621` trỏ vào TC ID, user chọn **"Bổ sung TC DB"** thay vì sinh lại cả module. TC ID luôn nối tiếp (LOGIN tới `084`, CUST tiếp theo từ `CRM_CUST_TC_067`).

## Các quyết định nhỏ khác

- `/review-testcases FIX` LOGIN (10-11-2026): áp cả 4 nhóm A–D; sửa Expected **không** tạo mốc git (user chọn *"Sửa luôn, không mốc git"*).
- `/generate-test-data` LOGIN: xuất **JSON**, mật khẩu ghi `[FROM_ENV]`, mỗi bộ data map về TC ID. ⚠️ File `docs/testcases/login/web/test_data_login_web.json` **không còn** trong `docs/` (kiểm 17-11-2026) — cần sinh lại nếu làm automation data-driven.
- `/create-bug-report`: **không cần Jira**.
- Xuất Excel: lưu cùng thư mục, giữ nguyên `.md` gốc.
- Checklist regression LOGIN: bản 09-11-2026 (32/34 REQ) đã thay bằng `checklist_regression_20261118.md` (39 mục, 41/47 REQ). Checklist là ảnh chụp — lần rà sau sinh file mới, không sửa đè.

Liên quan: [[kiem-thu-csdl]] · [[login]] · [[customers]]
