---
name: may-local-cong-cu
description: Máy Windows của user thiếu Python (Node có từ 20-11-2026) — script nào không chạy được và cách đã dùng thay thế
type: project
cập nhật: 20-11-2026
---

# Máy local và công cụ

- Windows 10, có **Git Bash** + **PowerShell 5.1**.
- **Không có Python** (`python3` chỉ là stub của Microsoft Store). **Node v26.13.1 LTS** đã cài 20-11-2026 (bộ cài MSI chính thức nodejs.org, `C:\Program Files\nodejs`) — trước đó máy không có Node.
  → Không chạy được: `scripts/db-check/db_check.py` (kể cả `python -m unittest scripts/db-check/test_db_check.py`), `scripts/user-guide/md2html.py`, `scripts/quality-insights/qi.py`, `scripts/design-compare/dc.py`. (Allure qua `npx` giờ chạy được vì đã có Node.)
  → Workflow cần các script này phải báo user cài Python 3.9+ trước, **không** tự viết lại logic script bằng tay rồi coi như đã chạy.
- Có **Excel 2007**. Xuất Excel (16-11-2026, `test_cases_customers_web.xlsx`) đã làm bằng cách **dựng `.xlsx` trực tiếp bằng PowerShell** rồi mở Excel để căn dòng.
- Đọc transcript `.jsonl` / JSON lớn: dùng PowerShell `ConvertFrom-Json` theo từng dòng.
- Git trên Windows in cảnh báo LF → CRLF khi commit: bình thường, không đổi nội dung.

Liên quan: [[trinh-duyet-va-dang-nhap]] · [[kiem-thu-csdl]]
