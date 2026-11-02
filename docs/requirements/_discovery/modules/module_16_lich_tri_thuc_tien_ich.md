# Module 16 — Lịch · Cơ sở tri thức · Tiện ích (`CAL` · `KBASE` · `UTIL`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc
>
> Gộp chung file vì là 3 module nhỏ, risk thấp, mỗi cái 1–2 màn hình. **Vẫn là 3 prefix, 3 tài liệu requirements riêng.**

## `CAL` — Calendar

| Mục | Giá trị |
|---|---|
| Route | `/admin/utilities/calendar` · Tạo sự kiện `/admin/utilities/calendar?new_event=true&date=<ngày>` (Quick create "Event") |
| Loại màn hình | Lịch |
| Điều khiển | Today · Month · Week · Day · Filter By |
| Bộ lọc (15) | Events · Tasks · Projects · Invoices · Estimates · Proposals · Contracts · Customer / Expense / Lead / Estimate / Invoice / Credit Note / Proposal / Ticket Reminders |
| Ước lượng | 10–15 REQ |
| Risk | 🟢 |

## `KBASE` — Knowledge Base

| Mục | Giá trị |
|---|---|
| Route | `/admin/knowledge_base` · Tạo bài `/admin/knowledge_base/article` |
| Loại màn hình | Danh sách + Groups |
| Thanh công cụ | New Article · Groups · Export |
| Cột bảng | Article Name · Group · Date Published |
| Dữ liệu | **0 bài viết** ("No entries found") |
| Ước lượng | 10–15 REQ |
| Risk | 🟢 — nội dung có thể hiển thị công khai ở cổng khách hàng (ngoài phạm vi) |

## `UTIL` — Media · Bulk PDF Export

| Mục | Giá trị |
|---|---|
| Route | Media `/admin/utilities/media` (tiêu đề "Files") · Bulk PDF Export `/admin/utilities/bulk_pdf_exporter` |
| Media | Trình quản lý file kiểu elFinder (URL chuyển sang `#elf_l1_Lw`); thư mục `admin-example` (thư mục riêng của tài khoản) · `public` |
| Bulk PDF Export — trường | `* Select Type` (Invoices · Estimates · Payments · Credit Notes · Proposals · Expenses) · From Date · To Date · Include Tag · nút Export |
| Ước lượng | 10 REQ |
| Risk | 🟢 — Media cho upload / xoá file trên máy chủ dùng chung: chỉ xem khi recon |

### Vùng chưa xác minh
- Media: thao tác upload / xoá / đổi tên — không thử (môi trường dùng chung)
- Calendar: hộp thoại tạo sự kiện — chưa mở

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [cal_overview_fullpage.png](../evidence/cal_overview_fullpage.png) | Calendar — tháng 11-2026 |
| [kbase_overview_fullpage.png](../evidence/kbase_overview_fullpage.png) | Danh sách Knowledge Base — rỗng |
| [util_overview_fullpage.png](../evidence/util_overview_fullpage.png) | Media — trình quản lý file |
| [util_bulk_pdf_export_fullpage.png](../evidence/util_bulk_pdf_export_fullpage.png) | Bulk PDF Export — form mặc định |
