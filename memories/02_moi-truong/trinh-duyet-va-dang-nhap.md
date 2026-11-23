---
name: trinh-duyet-va-dang-nhap
description: Trình duyệt nào đã dùng được để recon/chạy TC, cách xử lý bước cần mật khẩu, giới hạn khi chụp evidence
type: project
cập nhật: 20-11-2026
---

# Trình duyệt và đăng nhập

## Trình duyệt đã dùng

- **`.mcp.json` đã tạo 20-11-2026** ở gốc project: server `playwright` (`--browser=chrome --viewport-size=1600,750 --config=.claude/playwright-mcp-config.json`) và `playwright-mobile` (`--device=Pixel 7 --isolated`), chạy qua `cmd /c npx` (Windows bắt buộc). Đã cài Node 20-11-2026, chạy thử qua stdio: `playwright` lên 38 tool (có `browser_start_video`), `playwright-mobile` lên 25 tool. `initPage` trong config được tính **tương đối theo thư mục file config** (`.claude/`) nên trỏ đúng `playwright-mcp-init.cjs`. Sau khi khởi động lại Claude Code (20-11-2026) tool `mcp__playwright__*` và `mcp__playwright-mobile__*` đều có; mở thật Chrome 146 headed đo được `inner 1600×750` · `outer 1616×884` (không bị cắt), snapshot rơi đúng `.playwright-mcp/` của project. → Từ nay recon / chạy TC dùng **Playwright MCP** theo rule, không cần Chrome cổng debug hay pane tích hợp nữa.
- Cách đã chạy được (02-11-2026, theo yêu cầu user *"khởi chạy bằng Google Chrome của local"*): mở **Chrome local** với **profile tạm riêng**, cửa sổ ~1614×885 (vùng nhìn ~1600×750), điều khiển/chụp ảnh qua **cổng debug của Chrome**.
- Browser pane của app (Claude Browser) cũng đã dùng: pane hẹp (từng chỉ 545px, lần recon CUST 973×853) → bố cục desktop có thể chưa thấy; ghi rõ viewport đã dùng vào tài liệu. Pane không lưu ảnh thẳng vào repo, nhưng mỗi ảnh chụp có file nguồn ở `~/.claude/projects/…/tool-results/mcp-Claude_Browser-blob-*.jpg` → **chép file đó** vào `evidence/` (cách dùng từ 18-11-2026).

## Bước cần mật khẩu

- Agent **không tự gõ mật khẩu** trên site này. Chia luồng thành *Bước 1 / Bước 2…*: agent viết hướng dẫn, user tự thao tác rồi trả lời `Xong bước N` / `Đã đăng nhập xong`.
- Khi user đăng nhập cho lượt chạy TC: dặn **không tick Remember me**, không bấm gì thêm sau khi vào Dashboard.
- Đăng xuất / thử phiên chỉ làm trong **cửa sổ tách biệt** đó, không ảnh hưởng phiên khác của user.
- Cookie: chỉ ghi **tên, cờ, hạn dùng** — không đọc giá trị.

## Giới hạn khi chạy TC trên khung trình duyệt điều khiển từ xa

Lượt `/execute-test-cases` LOGIN (10-11-2026) cho 3 kết quả giả do khung không giữ focus hệ điều hành: viền focus không hiện (TC_001), Ctrl+C/V không chạm clipboard (TC_016), F5 không reload (TC_056). Các TC bàn phím / clipboard / focus cần chạy lại trên trình duyệt thật có người thao tác trước khi kết luận FAIL.

Liên quan: [[moi-truong-crm-dung-chung]] · [[may-local-cong-cu]]

## Pane trình duyệt tích hợp — giới hạn đo được 18-11-2026 (`run_1794989188`)

| Việc | Kết quả |
|---|---|
| Pane ẩn / cửa sổ Claude thu nhỏ | Click, phím, ảnh chụp **timeout** ("tab not on screen"). Agent tự mở lại được: `preview_start` + `mcp__ccd_view__show_pane` (pane `preview`) — user không cần bấm Ctrl+Shift+B |
| Focus cửa sổ | `document.hasFocus()` về `false` sau mỗi lệnh → không quan sát được viền focus (TC_001 mục 4) |
| Ctrl+C / Ctrl+V | Không chạm bộ nhớ tạm (TC_016, 019) |
| F5 | Không nạp lại trang (TC_056) |
| Hộp `confirm()` gốc | Không hiện, coi như Huỷ → nút Xoá của Perfex không chạy (task 2193 còn sót) |
| `resize_window` giả lập | Bị xoá khi hết lượt của agent; ảnh chụp ở khổ > pane bị lệch — kiểm bằng DOM, không tin ảnh |
| Phím Tab / Space / Shift+Tab / Enter, double-click | Chạy đúng (TC_051, 036) |
| Cookie | `sp_session`, `csrf_cookie_name` là HttpOnly — không xoá được bằng script. `autologin` đọc / xoá được qua `cookieStore` (cả hạn, path, Secure) |
| Nút "Phân công mới" ở `/admin/tasks` | Click thật không mở modal — dựng Pre-Condition bằng `element.click()` qua script |

→ TC cần focus thật, clipboard, F5, hộp thoại gốc, xoá cookie HttpOnly: **không** chạy bằng pane nữa — giao tester chạy tay hoặc Playwright MCP.
