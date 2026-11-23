---
name: cach-lam-viec-voi-user
description: Cách user giao việc, ý nghĩa các câu trả lời ngắn, những gì user muốn được hỏi trước
type: user
cập nhật: 17-11-2026
---

# Cách làm việc với user

## Giao tiếp

- Luôn trả lời **Tiếng Việt**, ngắn gọn, có căn cứ (CLAUDE.md mục 1).
- User là QA/tester học khoá *AI Testing Manual*, dùng bộ command `/…` trong `.claude/commands/` làm quy trình chính. Hiểu rõ thuật ngữ REQ / TC / AMB / RTM — không cần giải thích lại.

## Ý nghĩa các câu trả lời ngắn (đã gặp nhiều lần)

| User gõ | Nghĩa | Làm gì |
|---|---|---|
| `Commit` | Commit **ngay** phần vừa làm | Chỉ commit đúng thư mục của tác vụ (VD chỉ `docs/requirements/`), không kéo theo file khác đang thay đổi |
| `Chưa commit` | Để user xem lại trước | Không commit, không hỏi lại trong lượt đó |
| `Chưa push` | **Không bao giờ** tự push | Tới 17-11-2026 user chưa từng yêu cầu push |
| `Để sau` | Hoãn bước kế tiếp agent vừa đề xuất | Dừng, ghi việc đó vào [[backlog]] |
| `Cứ để lại` | Giữ nguyên hiện trạng (VD bản ghi test còn sót trên môi trường) | Không dọn, không hỏi lại |
| `Dùng gợi ý` · `Theo giả định` · `Duyệt cả N` | Chấp nhận toàn bộ đề xuất agent vừa đưa | Làm đúng đề xuất, không thêm bớt |
| `dùng Assumption tạm …` | Đóng AMB đang treo bằng giả định tạm thay vì chờ PO | Ghi ⏭️ theo Assumption, nêu rõ là tạm — xem [[quy-uoc-test-case]] |

## Những việc phải hỏi / chờ duyệt trước

- **Sửa bộ skill / command / rule:** user thường nói *"đưa ra gợi ý, đừng chỉnh sửa gì đến khi tôi duyệt"* → liệt kê đề xuất đánh số, **chờ** `Duyệt …` rồi mới sửa (14-11 và 15-11-2026).
- **Chỉ làm đúng phạm vi được yêu cầu.** VD 14-11-2026: user bảo sửa skill để TC không chia part → chỉ sửa skill; bộ TC `LOGIN` chỉ gộp khi user nói tiếp *"Gộp LOGIN ngay"*.
- **Lệnh git đổi trạng thái nhánh** (`checkout`, `branch -f`, `merge`…): hỏi trước — xem [[nhanh-commit-va-don-worktree]].
- **Xuất file định dạng khác** (Excel, HTML): lưu **cùng thư mục**, **không xoá bản gốc** `.md`.
- Câu cần mật khẩu: agent **không tự gõ mật khẩu** trên site — user tự thao tác (xem [[trinh-duyet-va-dang-nhap]]).

## Thói quen khi kết thúc việc

- Báo rõ: file nào đã ghi, đã commit hay chưa, đã push hay chưa, việc gì còn lại.
- Đề xuất **lệnh `/…` kế tiếp** theo chuỗi workflow — user hay chọn tiếp từ gợi ý đó.
