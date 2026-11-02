# Module 04 — Dự án · Công việc (`PRJ` · `TASK`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc
>
> Gộp chung file vì quan hệ cha–con (task gắn với project, tab Tasks · Timesheets nằm trong Project). **Vẫn là 2 prefix, 2 tài liệu requirements riêng.**

## `PRJ` — Projects

| Mục | Giá trị |
|---|---|
| Route | Danh sách `/admin/projects` · Tạo mới `/admin/projects/project` · Chi tiết `/admin/projects/view/{id}?group=<tab>` |
| Loại màn hình | Danh sách + màn chi tiết nhiều tab |
| Thanh công cụ | New Project · Export |
| Cột bảng `#projects` | # · Project Name · Customer · Tags · Start Date · Deadline · Members · Status |
| Status flow | 5 trạng thái ở "Projects Summary": **Not Started · In Progress · On Hold · Cancelled · Finished** |
| Tab chi tiết (18) | Overview · Tasks · Timesheets · Milestones · Files · Discussions · Gantt · Tickets · Contracts · Sales (nhóm) · Proposals · Estimates · Invoices · Subscriptions · Expenses · Credit Notes · Notes · Activity |
| Ước lượng | 18 tab + status flow 5 trạng thái → 60–80 REQ |
| Risk | 🔴 — entity trung tâm thứ hai, status flow, liên kết chứng từ tiền |

## `TASK` — Tasks (gồm Timesheets)

| Mục | Giá trị |
|---|---|
| Route | `/admin/tasks` · `/admin/tasks/list_tasks` · Xem `/admin/tasks/view/{id}` · My Timesheets `/admin/staff/timesheets` |
| Loại màn hình | Danh sách + Tasks Overview |
| Thanh công cụ | New Task · Tasks Overview · Export · Bulk Actions |
| Cột bảng `#tasks` | # · Name · Status · Start Date · Due Date · Assigned to · Tags · Priority |
| Status flow | 5 trạng thái ở "Tasks Summary": **Not Started · In Progress · Testing · Awaiting Feedback · Complete** + cột Priority (Medium · High quan sát được); task định kỳ mang nhãn "Recurring Task" |
| Timesheets | Cột ở báo cáo tổng: Staff Member · Task · Timesheet Tags · Start Time · End Time · Note · Related · Time (h) · Time (decimal) |
| Ước lượng | 30–40 REQ |
| Risk | 🟡 — dùng hằng ngày, có status flow và tính giờ |

### Phát hiện tầng network
Chưa ghi riêng cho 2 module này — kiểm khi recon (dự kiến cùng mẫu `POST /admin/<module>/table`).

### Vùng chưa xác minh
- Thấy link `/admin/tasks/delete_task/{id}` trong DOM Dashboard — **không** mở (URL xoá)
- Quick create "Task" ở header là `#` (mở hộp thoại) — chưa mở
- Nội dung 18 tab project, Gantt, Milestones — chỉ đọc tên tab

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [prj_overview_fullpage.png](../evidence/prj_overview_fullpage.png) | Danh sách Projects + Projects Summary |
| [task_overview_fullpage.png](../evidence/task_overview_fullpage.png) | Danh sách Tasks + Tasks Summary (5 trạng thái) |
