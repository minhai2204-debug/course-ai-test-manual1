---
name: kiem-thu-csdl
description: Bối cảnh quyết định kiểm thử CSDL (chỉ SELECT) — vì sao skill được sửa, phần nào còn treo
type: project
cập nhật: 17-11-2026
---

# Kiểm thử CSDL

Luật đầy đủ nằm ở [`.claude/rules/database_rules.md`](../../.claude/rules/database_rules.md) — **đọc file đó** khi làm TC `@DBCheck`. Ở đây chỉ giữ dòng thời gian và phần còn treo.

| Ngày | Sự kiện |
|---|---|
| 14-11-2026 | User: dự án cho truy cập DB, cần TC kiểm dữ liệu trong DB, **chỉ được viết SELECT**. Agent đề xuất 9 thay đổi skill → user *"Duyệt cả 9"*. Không tạo command/tầng `db/` riêng: TC DB nằm cùng file nền tảng, gắn tag `@DBCheck` |
| 15-11-2026 | User muốn kiểm DB cho thêm · sửa · xoá · tìm kiếm · báo cáo · dashboard → thêm 3 loại truy vấn A/B/C. Trả lời 2 câu: (1) **cho phép** truy vấn tổng hợp trên dữ liệu nghiệp vụ thật; (2) công thức báo cáo **lấy từ tài liệu phân tích yêu cầu** (`MET-…`), không từ mã nguồn app |

## Còn treo

- **AMB-SYS-05:** chưa biết engine DB, tài khoản có read-only phía DB không, cách kết nối. `.env` chưa có `DB_*` → agent không tự chạy truy vấn; khối 🗄️ chấm `BLOCKED` khi thực thi.
- Tên bảng/cột trong TC `@DBCheck` đang là **placeholder** `<bảng>.<cột>` + `@NeedsVerify` (user chọn 14-11-2026) — có schema thì thay.
- Máy chưa có Python → `db_check.py` chưa chạy được ([[may-local-cong-cu]]).
- Mặc định an toàn đang áp: coi tài khoản DB **có thể có quyền ghi** → chốt chặn luôn bật; luôn che cột nhạy cảm.

Liên quan: [[quy-uoc-test-case]] · [[moi-truong-crm-dung-chung]]
