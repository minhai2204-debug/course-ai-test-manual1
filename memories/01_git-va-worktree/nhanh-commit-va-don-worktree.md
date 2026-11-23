---
name: nhanh-commit-va-don-worktree
description: Trạng thái các nhánh git, thư mục nào đã/chưa được git theo dõi, quy tắc commit và dọn worktree
type: project
cập nhật: 17-11-2026
---

# Nhánh, commit và dọn worktree

## Trạng thái nhánh (đo 17-11-2026 — kiểm lại bằng `git branch -a` / `git log` trước khi dựa vào)

| Nhánh | Đỉnh | Nội dung |
|---|---|---|
| `discovery/crm-admin` | `cb8ea3a` | **Đang checkout ở thư mục chính.** Chỉ có `docs/requirements/` (discovery + LOGIN) được commit |
| `main` (local) | `c940795` | Có thêm bộ TC LOGIN cũ (55 TC, 2 part) + báo cáo review — agent dời con trỏ `main` từ worktree. **Chưa push** |
| `origin/main` | `ca7cf5f` | Chưa có `docs/` |
| `claude/generate-master-test-plan-180f8e` | `76f287c` | **Duy nhất** nơi có Master Test Plan `release_1.0` — chưa merge; dựng trên trạng thái cũ (LOGIN 34 REQ, 0 TC) |
| `claude/discover-system-ui-17f1b6` | `4cce9bf` | Bản discovery đầu tiên đã bị thay thế — chưa merge, user chưa cho xoá |

## Thứ chưa được git theo dõi ở thư mục chính (17-11-2026)

`.claude/` · `CLAUDE.md` · `plans/` · `prompts/` · `scripts/` · `memories/` · `docs/testcases/` · `docs/executions/` · `docs/bugs/` · `docs/checklists/` · `docs/requirements/customers/` · 2 impact report LOGIN ngày 11-11.
Ngoài ra 2 file SRS (`SRS_Login_Module.md`, `docs/SRS_Login_Module.txt`) đang ở trạng thái **đã xoá, chưa commit** — user tự làm, **không đụng tới**.

→ Sửa lớn trên các thư mục chưa theo dõi thì **không có mốc git để quay lại**: chép bản gốc ra scratchpad trước, và nhắc user commit sớm (bản trong scratchpad mất khi hết phiên).

## Quy tắc

- **CẤM** `git pull/checkout/merge/rebase/reset` (CLAUDE.md). Chỉ đọc: `status`, `diff`, `log`.
- **Bài học 09-11-2026:** agent tự dời nhánh `main` mà không hỏi → sai. Mọi lệnh đổi con trỏ nhánh phải hỏi trước, hoặc gửi lệnh để user tự chạy.
- Commit chỉ khi user nói `Commit`, chỉ đúng thư mục của tác vụ. Không push.
- Nhắc lại phạm vi commit trong báo cáo: *"chỉ `docs/requirements/` được commit, các thư mục khác vẫn y nguyên"*.

## Dọn worktree

- User hay yêu cầu *"xoá worktree trong .claude"* sau khi xong việc. Xoá **thư mục** worktree được (khi đã sạch, commit đã nằm ở nhánh khác); **giữ nhánh** còn commit chưa merge.
- Nếu phiên đang chạy **bên trong** worktree sắp xoá → báo trước là phiên sẽ không làm tiếp được.
- Còn sót (17-11-2026): `.claude/worktrees/login-web-testcases-docs-31cd46` (vẫn đăng ký với git) và thư mục `review-login-web-testcases-546cb7`.

Liên quan: [[ghi-output-vao-repo-chinh]] · [[cach-lam-viec-voi-user]]
