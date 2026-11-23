---
name: ghi-output-vao-repo-chinh
description: Deliverable (TC, báo cáo, requirements) phải ghi vào docs/ của checkout chính, không phải docs/ của worktree
type: feedback
cập nhật: 17-11-2026 (chuyển từ bộ nhớ máy local, gốc 10-11-2026)
---

# Ghi kết quả vào `docs/` của repo chính

Kết quả đầu ra (test cases, báo cáo review, requirements, execution report, bug…) phải ghi vào
`C:\Users\h\Desktop\Ai_Testing_Manual\course-ai-test-manual1\docs`,
**không** phải `docs/` trong worktree `.claude\worktrees\<tên>`.

**Why:** 10-11-2026, sau `/review-testcases` (REVIEW rồi FIX) user báo hai lần *"bạn đang làm sai ý tôi, kết quả đầu ra nằm ở …\docs"* vì kết quả chỉ nằm trong worktree. Repo chính có file mà worktree không có, và `docs/testcases/` ở repo chính chưa được git theo dõi → worktree không thấy.

**How to apply:**
- Phiên chạy trong worktree → đọc **và** ghi file deliverable ở `docs/` của repo chính.
- Trước khi ghi đè, so file ở repo chính với bản mình lấy làm gốc (repo chính có thể mới hơn).
- Không tự commit trên nhánh của repo chính — xem [[nhanh-commit-va-don-worktree]].
- Phiên worktree cũ từng bị **hook chặn Edit** ghi vào checkout chính → soạn file ở scratchpad rồi chép sang.
