# Bộ nhớ dự án — Bản đồ (MEMORY.md)

> **Đọc file này ngay sau `CLAUDE.md`, trước khi làm bất kỳ việc gì.** Sau đó mở **chỉ** những file bộ nhớ khớp với việc đang làm theo bảng *"Làm việc gì → đọc file nào"* bên dưới.
>
> `memories/` giữ thứ **không** nằm sẵn trong `CLAUDE.md`, `.claude/rules/` hay `docs/`: lời user đã chốt, bài học khi làm sai, trạng thái môi trường / máy / git, việc còn dở. Số liệu REQ · TC · AMB **luôn** đọc ở danh mục `docs/*/README.md` — bộ nhớ chỉ trỏ tới, không chép lại.

## Thứ tự đọc khi mở phiên

```
CLAUDE.md  →  memories/MEMORY.md (file này)  →  00_nguoi-dung/  →  file bộ nhớ theo việc  →  docs/requirements/README.md (tầng 1)  →  …
```

1. **Luôn đọc:** [00_nguoi-dung/cach-lam-viec-voi-user.md](00_nguoi-dung/cach-lam-viec-voi-user.md) — ý nghĩa các câu trả lời ngắn của user, việc gì phải hỏi trước.
2. **Đọc theo việc:** bảng dưới.
3. **Gặp mâu thuẫn** giữa bộ nhớ và hiện trạng (file, nhánh, `.env`) → tin hiện trạng, sửa lại file bộ nhớ, ghi ngày.

## Làm việc gì → đọc file nào

| Việc sắp làm | Đọc |
|---|---|
| Mọi việc có commit / đụng nhánh / chạy trong worktree | [01_git-va-worktree/nhanh-commit-va-don-worktree.md](01_git-va-worktree/nhanh-commit-va-don-worktree.md) · [01_git-va-worktree/ghi-output-vao-repo-chinh.md](01_git-va-worktree/ghi-output-vao-repo-chinh.md) |
| Recon / chạy TC / chụp evidence trên CRM (`/discover-system`, `/generate-requirements-from-website`, `/execute-test-cases`, `/retest-fixed-bugs`, `/generate-user-guide` LIVE) | [02_moi-truong/moi-truong-crm-dung-chung.md](02_moi-truong/moi-truong-crm-dung-chung.md) · [02_moi-truong/trinh-duyet-va-dang-nhap.md](02_moi-truong/trinh-duyet-va-dang-nhap.md) |
| Chạy script Python / Node trong `scripts/`, xuất Excel / HTML | [02_moi-truong/may-local-cong-cu.md](02_moi-truong/may-local-cong-cu.md) |
| Module mới, phạm vi hệ thống, Master Test Plan | [03_quyet-dinh-chung/he-thong-va-pham-vi.md](03_quyet-dinh-chung/he-thong-va-pham-vi.md) |
| Sinh / sửa / review test case, test data, checklist, bug | [03_quyet-dinh-chung/quy-uoc-test-case.md](03_quyet-dinh-chung/quy-uoc-test-case.md) |
| TC `@DBCheck`, mọi việc đụng CSDL | [03_quyet-dinh-chung/kiem-thu-csdl.md](03_quyet-dinh-chung/kiem-thu-csdl.md) → rồi `.claude/rules/database_rules.md` |
| Làm module `LOGIN` | [04_module/login.md](04_module/login.md) |
| Làm module `CUST` (thư mục `customers/`) | [04_module/customers.md](04_module/customers.md) |
| User hỏi "làm gì tiếp", hoặc trước khi đề xuất bước kế tiếp | [05_viec-dang-treo/backlog.md](05_viec-dang-treo/backlog.md) |

## Cấu trúc thư mục

```
memories/
├── MEMORY.md                         ← BẢN ĐỒ (file này) — tên bất biến
├── 00_nguoi-dung/                    ← user là ai, cách giao việc, câu trả lời ngắn nghĩa là gì
├── 01_git-va-worktree/               ← nhánh, commit, worktree, nơi ghi output
├── 02_moi-truong/                    ← môi trường CRM dùng chung, trình duyệt, máy local
├── 03_quyet-dinh-chung/              ← quyết định cấp hệ thống, quy ước TC, CSDL
├── 04_module/<module>.md             ← mỗi module một file, tên = tên thư mục module trong docs/
└── 05_viec-dang-treo/backlog.md      ← việc "Để sau" + việc chờ người khác
```

## Quy tắc ghi bộ nhớ

| Quy tắc | Lý do |
|---|---|
| Mỗi file **một chủ đề**; file vượt ~80 dòng thì tách | Đọc theo việc, không đọc cả kho |
| Module mới → thêm `04_module/<tên-thư-mục-module>.md` + **một dòng** ở bảng *Làm việc gì → đọc file nào* | Bản đồ phải trỏ tới mọi file — file không có dòng ở đây coi như không tồn tại |
| Đầu file có frontmatter `name` · `description` · `type` (`user` / `feedback` / `project`) · `cập nhật: DD-MM-YYYY` | Biết file nói gì, cũ hay mới mà không phải đọc hết |
| `feedback` ghi kèm **Why** (lời user, ngày) và **How to apply** | Biết khi nào áp, khi nào là ngoại lệ |
| Liên kết chéo bằng `[[tên-file]]` | Lần theo bối cảnh liên quan |
| Ngày viết `DD-MM-YYYY` · chuyển "hôm qua", "tuần sau" thành ngày cụ thể | Theo CLAUDE.md, đọc lại sau vẫn đúng |
| 🔒 **KHÔNG** ghi mật khẩu, token, cookie, email đăng nhập, chuỗi kết nối — chỉ ghi **tên biến** `.env` | `memories/` được commit, lịch sử git không xoá được |
| **Không chép** số liệu / nội dung đã có ở `docs/`, `CLAUDE.md`, `.claude/rules/` — chỉ trỏ link | Hai nguồn sự thật sẽ lệch nhau |
| Sự thật hết đúng → **sửa hoặc xoá** dòng đó, không để song song bản cũ | Bộ nhớ sai nguy hiểm hơn không có |
| Sau mỗi tác vụ có quyết định mới của user / bài học / việc treo mới → cập nhật file tương ứng **trong lượt đó** | Phiên sau mới tiếp nối được |

## Nguồn gốc

Gom ngày 17-11-2026 từ: bộ nhớ local `~/.claude/projects/C--Users-h-Desktop-Ai-Testing-Manual-course-ai-test-manual1/memory/` (1 file) và lịch sử 9 phiên làm việc trước đó trên repo này (02-11 → 16-11-2026, gồm cả các phiên chạy trong worktree).
