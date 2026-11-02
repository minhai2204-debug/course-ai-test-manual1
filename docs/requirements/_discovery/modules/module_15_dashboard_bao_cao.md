# Module 15 — Dashboard · Báo cáo (`DASH` · `RPT`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc
>
> Gộp chung file vì cùng là màn hình tổng hợp chỉ đọc từ dữ liệu module khác, khảo sát sau cùng. **Vẫn là 2 prefix, 2 tài liệu requirements riêng.**

## `DASH` — Dashboard

| Mục | Giá trị |
|---|---|
| Route | `/admin/` · Đặt lại bố cục `/admin/staff/reset_dashboard` |
| Loại màn hình | Dashboard |
| Widget (13, theo `id`) | `finance_overview` · `top_stats` · `user_data` · `upcoming_events` · `calendar` · `payments_chart` · `contracts_expiring` · `tickets_report` · `todos` · `leads_chart` · `projects_chart` · `tickets_chart` · `projects_activity` |
| Tiêu đề quan sát | Payment Records · Contracts Expiring Soon · My To Do Items · Leads Overview · Statistics by Project Status · Latest Project Activity |
| Ước lượng | 15–20 REQ |
| Risk | 🟡 — số liệu tổng hợp, sai lệch khó phát hiện; dữ liệu môi trường dùng chung biến động (RISK-SYS-01) |

## `RPT` — Reports

| Mục | Giá trị |
|---|---|
| Route | `/admin/reports/sales` · `/admin/reports/expenses` · `/admin/reports/expenses_vs_income` · `/admin/reports/leads` · `/admin/staff/timesheets?view=all` · `/admin/reports/knowledge_base_articles` |
| Loại màn hình | Báo cáo |
| Sales | 7 báo cáo bảng: Invoices Report · Items Report · Payments Received · Credit Notes Report · Proposals Report · Estimates Report · Customers Report — 3 báo cáo biểu đồ: Total Income · Payment Modes (Transactions) · Total Value By Customer Groups — ghi chú đỏ: "Cancelled invoices are excluded from the report" |
| Leads report | "This Week Leads Conversions" · "Sources Conversion" · "Monthly" (chọn tháng) · nút "Switch to staff report" |
| Timesheets overview | Cột: Staff Member · Task · Timesheet Tags · Start Time · End Time · Note · Related · Time (h) · Time (decimal) |
| Ước lượng | 25–30 REQ |
| Risk | 🟡 — đối soát tiền giữa nhiều module |

### Vùng chưa xác minh
- Tiêu đề trang `/admin/reports/leads` là chuỗi mặc định "Perfex CRM \| Anh Tester Demo" (các báo cáo khác có tiêu đề riêng) — ghi nhận để kiểm ở recon
- Nội dung, bộ lọc thời gian, xuất file của từng báo cáo — chưa mở

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [dash_overview_fullpage.png](../evidence/dash_overview_fullpage.png) | Dashboard 13 widget |
| [rpt_overview_fullpage.png](../evidence/rpt_overview_fullpage.png) | Reports → Sales: 7 báo cáo bảng + 3 báo cáo biểu đồ |
