# Bản đồ hệ thống — CRM (Perfex CRM · khu admin)

> **INDEX tầng khám phá — tên file bất biến.** Không chứa mã REQ. Chi tiết từng module ở thư mục [`modules/`](modules/) (xem **Bản đồ tài liệu**).
> Danh mục + trạng thái recon: [`../README.md`](../README.md) — nơi **duy nhất** theo dõi tiến độ recon.

## 1. Bối cảnh khảo sát

| Mục | Giá trị |
|---|---|
| Ngày | 02-11-2026 |
| Mode · Mặt | **UI** (user chỉ định) · **Web** — 1 mặt |
| Hệ thống | Perfex CRM **3.1.6** (đọc từ tham số `?v=3.1.6` của tài nguyên tĩnh) — bản demo dùng cho khoá học |
| URL · tài khoản | Lưu ở `.env` — không ghi vào tài liệu |
| Role đã dùng | 1 tài khoản admin (`user-id-2` trong `body.className`) — menu Setup rỗng, khu cấu hình trả `Access denied`. User xác nhận 05-11-2026: tạm thời hệ thống chỉ có role admin |
| Đăng nhập | User tự đăng nhập trong cửa sổ Chrome (agent không nhập mật khẩu trên host không phải local/staging). Trang đăng nhập chụp trong browser context không cookie — không đăng xuất phiên đang dùng |
| Môi trường | 🔒 **Dùng chung**. Đợt khảo sát 02-11-2026 **chỉ đọc**: không tạo / sửa / xoá, không bấm Save. Từ 05-11-2026 user cho phép **tạo dữ liệu thử** ngay trên môi trường này (AMB-SYS-03): chỉ tạo mới, đặt tên nhận diện được; không sửa / xoá bản ghi có sẵn. Có dữ liệu của người khác (bộ lọc `auto_filter_tc029_*`, ~2.800 khách hàng) |
| Phạm vi crawl | Khu admin `/admin/*`: 14 mục sidebar cấp 1 + 15 mục cấp 2 · menu header (Quick create, Profile, Language, Todo, Notifications) · `a[href]` trên Dashboard · 2 màn chi tiết (Customer, Project) · 11 route khu Setup thử bằng điều hướng trực tiếp (chỉ đọc) |
| Ngoài phạm vi | **Cổng khách hàng** — URL/tài khoản khác, user cung cấp sau → mode ADD |
| Tài liệu QA | Không nạp (mode UI). Repo có `SRS_Login_Module.md` / `docs/SRS_Login_Module.txt` — dùng được khi recon `LOGIN` |
| Công cụ | **Google Chrome 146 trên máy local** (headed, profile tạm riêng, cửa sổ `1614×885`), điều khiển qua Chrome DevTools Protocol: đọc DOM bằng `Runtime.evaluate`, chụp bằng `Page.captureScreenshot`. Playwright MCP không có trong phiên |
| Viewport đo được | `innerWidth × innerHeight` = **1598 × 790** (outer `1614×885`) — bố cục desktop, `body` **không** có class `page-small` |
| Cách chụp full-page | Giả lập viewport `1598 × <chiều cao trang>` rồi chụp, sau đó trả lại kích thước cũ. **Không** dùng `captureBeyondViewport`: cách đó làm Perfex chuyển bố cục `page-small` và giấu sidebar (gặp ở lần chụp thử, đã chụp lại toàn bộ) |
| Tầng network | Quan sát thụ động: trang render phía server (CodeIgniter), bảng danh sách tải qua `POST /admin/clients/table` (DataTables server-side). Không thấy REST API JSON |
| Evidence | **25 ảnh** trong [`evidence/`](evidence/) — mỗi module ≥ 1 ảnh, liệt kê ở mục **Danh mục evidence** cuối file. Đã mở lại từng ảnh xác nhận đúng màn hình trước khi ghi danh mục |
| Dữ liệu trong ảnh | Ảnh chứa dữ liệu demo do người dùng khác của môi trường tạo (tên, email, số điện thoại); `prof_overview_fullpage.png` hiện email + số điện thoại của tài khoản đang dùng. User xem và **chấp nhận giữ nguyên** ngày 02-11-2026 |

## 2. Sơ đồ điều hướng (cây menu nguyên trạng)

```
Sidebar (#side-menu)
├── Dashboard ............................ /admin/
├── Customers ............................ /admin/clients
├── Projects ............................. /admin/projects
├── Tasks ................................ /admin/tasks
├── Contracts ............................ /admin/contracts
├── Sales
│   ├── Proposals ........................ /admin/proposals
│   ├── Estimates ........................ /admin/estimates
│   ├── Invoices ......................... /admin/invoices
│   ├── Payments ......................... /admin/payments
│   ├── Credit Notes ..................... /admin/credit_notes
│   └── Items ............................ /admin/invoice_items
├── Subscriptions ........................ /admin/subscriptions
├── Expenses ............................. /admin/expenses
├── Support .............................. /admin/tickets
├── Leads ................................ /admin/leads
├── Estimate Request ..................... /admin/estimate_request
├── Knowledge Base ....................... /admin/knowledge_base
├── Utilities
│   ├── Media ............................ /admin/utilities/media
│   ├── Bulk PDF Export .................. /admin/utilities/bulk_pdf_exporter
│   └── Calendar ......................... /admin/utilities/calendar
└── Reports
    ├── Sales ............................ /admin/reports/sales
    ├── Expenses ......................... /admin/reports/expenses
    ├── Expenses vs Income ............... /admin/reports/expenses_vs_income
    ├── Leads ............................ /admin/reports/leads
    ├── Timesheets overview .............. /admin/staff/timesheets?view=all
    └── KB Articles ...................... /admin/reports/knowledge_base_articles

Setup (#setup-menu) ...................... RỖNG với tài khoản hiện tại

Header
├── Quick create (+): Invoice · Estimate · Proposal · Credit Note · Customer · Subscription
│                     Project · Task · Expense · Contract · Article · Ticket · Event
├── Newsfeed ("Share documents, ideas..")
├── To Do (badge số) ..................... /admin/todo
├── Notifications
└── Profile menu: My Profile (/admin/profile) · My Timesheets (/admin/staff/timesheets)
                  Edit Profile (/admin/staff/edit_profile) · Language (26 ngôn ngữ) · Logout

Route ngoài menu (thấy qua a[href])
├── /admin/misc/reminders · /admin/staff/reset_dashboard
├── /admin/clients/client/{id}?group=… (19 tab) · /admin/projects/view/{id}?group=… (18 tab)
└── /admin/<entity>/<entity> (form tạo mới) · /admin/<entity>/list_<entity>/{id} (xem)

Đăng nhập: /admin/authentication — Email · Password · Remember me · Forgot Password?
```

**Route khu Setup thử bằng điều hướng (02-11-2026):**

| Route | Kết quả |
|---|---|
| `/admin/settings` · `/admin/staff` · `/admin/roles` · `/admin/utilities/activity_log` · `/admin/emails` · `/admin/custom_fields` · `/admin/departments` · `/admin/currencies` · `/admin/taxes` · `/admin/paymentmodes` | → `/admin/access_denied` ("Access denied") |
| `/admin/modules` | → chuyển về `/admin/` (Dashboard) |

> Route trả `access_denied` (không phải 404) → route **có tồn tại**, bị chặn bởi kiểm tra quyền. Nội dung bên trong **chưa nhìn thấy**.

## 3. Bảng module tổng

| # | Module (tên UI) | Bí danh | Prefix | Nền tảng | File khám phá | Loại màn hình | Risk | Ước REQ |
|---|---|---|---|---|---|---|---|---|
| 1 | Login / Forgot Password | Authentication | `LOGIN` | Web | [module_01](modules/module_01_dang_nhap.md) | Form | 🔴 | 15–20 |
| 2 | Customers | Clients · Contacts | `CUST` | Web | [module_02](modules/module_02_khach_hang.md) | Danh sách + chi tiết 19 tab | 🔴 | 60–80 |
| 3 | Items | Invoice Items | `ITEM` | Web | [module_03](modules/module_03_hang_hoa.md) | Danh sách + Import + Groups | 🟡 | 15–20 |
| 4 | Projects | — | `PRJ` | Web | [module_04](modules/module_04_du_an_cong_viec.md) | Danh sách + chi tiết 18 tab | 🔴 | 60–80 |
| 5 | Tasks | Timesheets | `TASK` | Web | [module_04](modules/module_04_du_an_cong_viec.md) | Danh sách + Overview | 🟡 | 30–40 |
| 6 | Proposals | — | `PROP` | Web | [module_05](modules/module_05_de_xuat_bao_gia.md) | Danh sách + form | 🟡 | 25–30 |
| 7 | Estimates | — | `EST` | Web | [module_05](modules/module_05_de_xuat_bao_gia.md) | Danh sách + form | 🔴 | 25–35 |
| 8 | Invoices | Recurring Invoices · Batch Payments | `INV` | Web | [module_06](modules/module_06_hoa_don.md) | Danh sách + form | 🔴 | 35–45 |
| 9 | Payments | — | `PAY` | Web | [module_07](modules/module_07_thanh_toan.md) | Danh sách | 🔴 | 10–15 |
| 10 | Credit Notes | — | `CRN` | Web | [module_08](modules/module_08_giay_bao_co.md) | Danh sách + form | 🔴 | 20–25 |
| 11 | Contracts | — | `CTR` | Web | [module_09](modules/module_09_hop_dong.md) | Danh sách + biểu đồ | 🟡 | 20–30 |
| 12 | Leads | — | `LEAD` | Web | [module_10](modules/module_10_khach_tiem_nang.md) | Danh sách | 🟡 | 30–40 |
| 13 | Expenses | — | `EXP` | Web | [module_11](modules/module_11_chi_phi.md) | Danh sách + Import | 🟡 | 20–25 |
| 14 | Subscriptions | — | `SUBS` | Web | [module_12](modules/module_12_goi_dinh_ky.md) | Danh sách | 🟡 | 15–20 |
| 15 | Support | Support Tickets | `TICK` | Web | [module_13](modules/module_13_ho_tro_ticket.md) | Danh sách | 🟡 | 25–35 |
| 16 | Estimate Request | — | `EREQ` | Web | [module_14](modules/module_14_yeu_cau_bao_gia.md) | Danh sách + Forms | 🟢 | 10–15 |
| 17 | Dashboard | — | `DASH` | Web | [module_15](modules/module_15_dashboard_bao_cao.md) | Dashboard 13 widget | 🟡 | 15–20 |
| 18 | Reports | — | `RPT` | Web | [module_15](modules/module_15_dashboard_bao_cao.md) | Báo cáo | 🟡 | 25–30 |
| 19 | Calendar | — | `CAL` | Web | [module_16](modules/module_16_lich_tri_thuc_tien_ich.md) | Lịch | 🟢 | 10–15 |
| 20 | Knowledge Base | KB | `KBASE` | Web | [module_16](modules/module_16_lich_tri_thuc_tien_ich.md) | Danh sách + Groups | 🟢 | 10–15 |
| 21 | Media · Bulk PDF Export | Utilities | `UTIL` | Web | [module_16](modules/module_16_lich_tri_thuc_tien_ich.md) | Trình quản lý file · công cụ xuất | 🟢 | 10 |
| 22 | My Profile · To Do · Reminders · Notifications · Newsfeed | — | `PROF` | Web | [module_17](modules/module_17_ca_nhan.md) | Trang cá nhân | 🟢 | 15–20 |
| 23 | Setup | Settings | `SETTING` | Web | [module_18](modules/module_18_cau_hinh_he_thong.md) | ❔ chưa thấy UI | 🔴 | ❔ |
| 24 | Staff · Roles | — | `STAFF` | Web | [module_19](modules/module_19_nhan_vien_vai_tro.md) | ❔ chưa thấy UI | 🔴 | ❔ |

**Tổng: 24 module trong 19 file** — kiểm chứng: 01–03 (3) + 04 (2) + 05 (2) + 06–14 (9) + 15 (2) + 16 (3) + 17–19 (3) = 24.

## 4. Bản đồ entity & phụ thuộc

Quan hệ dưới đây đọc từ **cột bảng danh sách** và **tab màn chi tiết** — đã quan sát. Quan hệ chuyển đổi: **Estimate → Invoice đã quan sát** (estimate Accepted mang nhãn "Invoiced"); Lead → Customer mới thấy trạng thái lead `Customer`, luồng chuyển `❔` — kiểm ở recon module.

```
                       ┌──────────── Item (ITEM) ── dùng trong ──┐
                       ▼                                         ▼
Lead (LEAD) ─❔→ Customer (CUST) ◄── Contact (gộp trong CUST)    Proposal · Estimate · Invoice · Credit Note
                  │                                               (PROP)    (EST)     (INV)     (CRN)
                  ├─► Project (PRJ) ─► Task (TASK) ─► Timesheet
                  ├─► Invoice (INV) ◄── Payment (PAY: cột "Invoice #")
                  │        ▲  ▲─────── Credit Note (CRN: cột "Remaining Amount")
                  │        └────────── Expense (EXP: cột "Invoice")
                  ├─► Contract (CTR) · Subscription (SUBS) · Ticket (TICK: cột "Contact")
                  └─► Reminders · Files · Vault · Notes · Statement (tab của Customer)
```

| Entity | Cột / tab chứng minh liên kết | Thuộc module |
|---|---|---|
| Customer ↔ Project · Invoice · Estimate · Proposal · Credit Note · Subscription · Expense · Contract · Task · Ticket · Payment | 19 tab `?group=…` của `/admin/clients/client/{id}` | `CUST` (trung tâm) |
| Project ↔ Task · Timesheet · Milestone · File · Discussion · Gantt · Ticket · Contract · Proposal · Estimate · Invoice · Subscription · Expense · Credit Note · Note · Activity | 18 tab `?group=project_…` của `/admin/projects/view/{id}` | `PRJ` |
| Estimate → Invoice | Nhãn "Invoiced" dưới Amount của estimate Accepted ở `/admin/estimates` | `EST` · `INV` |
| Payment → Invoice | Cột `Invoice #` ở `/admin/payments` | `PAY` |
| Expense → Project · Customer · Invoice | Cột ở `/admin/expenses` | `EXP` |
| Ticket → Contact · Department · Service | Cột ở `/admin/tickets` | `TICK` |
| Subscription ↔ Stripe | Logo **stripe** ở khối Subscriptions Summary | `SUBS` |
| Calendar ← Event · Task · Project · Invoice · Estimate · Proposal · Contract + 8 loại Reminder | 15 bộ lọc ở `/admin/utilities/calendar` | `CAL` |
| Reports ← Invoice · Item · Payment · Credit Note · Proposal · Estimate · Customer · Expense · Lead · Timesheet · KB Article | Sales: 7 báo cáo bảng + 3 báo cáo biểu đồ; + 5 mục Reports khác | `RPT` |
| Department · Service · Payment Mode · Tax · Currency · Contract Type · Customer Group · Lead Source/Status | Xuất hiện làm cột/bộ lọc ở nhiều module — **dữ liệu master quản lý ở Setup** (không mở được) | `SETTING` (BLOCKED) |

**Ranh giới entity — quyết định đã chốt với user 02-11-2026:**
- Contacts **gộp** vào `CUST` (contact luôn thuộc 1 customer ở khu admin; vòng đời đăng nhập của contact nằm ở cổng khách hàng — ngoài phạm vi)
- Payments **tách** `PAY` khỏi `INV` (menu, danh sách, báo cáo riêng; dính tiền)
- Timesheets gộp vào `TASK`; báo cáo "Timesheets overview" thuộc `RPT`
- Milestones · Discussions · Files · Gantt là tab con không có menu riêng → nằm trong `PRJ`

**Phát hiện network cấp hệ thống:**
- Tài nguyên tĩnh mang `?v=3.1.6` → phiên bản ứng dụng
- Bảng danh sách: DataTables server-side `POST /admin/<module>/table` (quan sát ở `clients`; các module khác kiểm khi recon)
- Không có REST API JSON quan sát được → QA không gọi API trực tiếp, nhánh API của TC ghi là không kiểm được (AMB-SYS-04 ✅)

## 5. Ma trận phân quyền sơ bộ (cấp module)

Chỉ có **1 tài khoản**. User xác nhận 05-11-2026: tạm thời hệ thống chỉ có role admin (`/admin/roles` vẫn Access denied nên chưa tự kiểm chứng được trên UI).

| Module | Admin (tài khoản `.env`) | Super Admin | Role khác |
|---|---|---|---|
| 22 module từ `LOGIN` → `PROF` | ✅ Xem được trang danh sách (chưa thử tạo/sửa/xoá) | — | — |
| `SETTING` | ❌ Access denied (đã kiểm chứng 10 route) | — | — |
| `STAFF` | ❌ Access denied (`/admin/staff`, `/admin/roles`) | — | — |
| Activity Log (thuộc `SETTING`) | ❌ Access denied | — | — |

**Đã kiểm chứng: 24 ô · Suy diễn: 0 ô · Không áp dụng: toàn bộ cột Super Admin + role khác** (user xác nhận 05-11-2026 — AMB-SYS-02; có thêm role thì mở lại).
> ✅ ở đây chỉ nghĩa là **mở được trang**. Quyền tạo/sửa/xoá chưa kiểm — không được làm tròn thành "có toàn quyền".

## 6. Thứ tự khảo sát đã chốt (02-11-2026)

Xếp theo *module được phụ thuộc trước, risk sau*:

| Thứ tự | Prefix | Lý do | Lệnh |
|---|---|---|---|
| 1 | `LOGIN` | Cửa vào mọi module | `/generate-requirements-from-website login` |
| 2 | `CUST` | Entity trung tâm, 19 tab, hầu hết module tham chiếu | `/generate-requirements-from-website customers` |
| 3 | `ITEM` | Danh mục dùng trong mọi chứng từ bán hàng | `/generate-requirements-from-website items` |
| 4 | `PRJ` | Entity trung tâm thứ hai, 18 tab | `/generate-requirements-from-website projects` |
| 5 | `TASK` | Phụ thuộc Project | `/generate-requirements-from-website tasks` |
| 6 | `PROP` | Chứng từ bán hàng đầu chuỗi | `/generate-requirements-from-website proposals` |
| 7 | `EST` | | `/generate-requirements-from-website estimates` |
| 8 | `INV` | Tiền — risk cao | `/generate-requirements-from-website invoices` |
| 9 | `PAY` | Phụ thuộc Invoice | `/generate-requirements-from-website payments` |
| 10 | `CRN` | Phụ thuộc Invoice · 0 bản ghi — tạo dữ liệu thử khi recon | `/generate-requirements-from-website credit_notes` |
| 11 | `CTR` | | `/generate-requirements-from-website contracts` |
| 12 | `LEAD` | | `/generate-requirements-from-website leads` |
| 13 | `EXP` | | `/generate-requirements-from-website expenses` |
| 14 | `SUBS` | 0 bản ghi — tạo dữ liệu thử khi recon | `/generate-requirements-from-website subscriptions` |
| 15 | `TICK` | 0 bản ghi — tạo dữ liệu thử khi recon | `/generate-requirements-from-website tickets` |
| 16 | `EREQ` | 0 bản ghi — tạo dữ liệu thử khi recon | `/generate-requirements-from-website estimate_request` |
| 17 | `DASH` | Tổng hợp từ module khác → khảo sát sau | `/generate-requirements-from-website dashboard` |
| 18 | `RPT` | Tổng hợp từ module khác | `/generate-requirements-from-website reports` |
| 19 | `CAL` | | `/generate-requirements-from-website calendar` |
| 20 | `KBASE` | 0 bài viết — tạo dữ liệu thử khi recon | `/generate-requirements-from-website knowledge_base` |
| 21 | `UTIL` | | `/generate-requirements-from-website utilities` |
| 22 | `PROF` | | `/generate-requirements-from-website profile` |
| — | `SETTING` · `STAFF` | **BLOCKED** — tài khoản `.env` không được phép vào (AMB-SYS-01 ✅) | — |

## 7. Nhật ký khám phá

| Ngày | Mode · Mặt | Phạm vi | Kết quả | Nguồn |
|---|---|---|---|---|
| 02-11-2026 | UI · Web — Chrome local | Khu admin, 1 tài khoản admin (không phải Super Admin), viewport 1598×790 | 24 module · 24 prefix · 2 module BLOCKED · 25 ảnh evidence. Thay cho bản nháp cùng ngày khảo sát bằng Browser pane (không có ảnh, viewport hẹp) — bản nháp đã bỏ, không phát hành | UI thực tế — chỉ đọc |
| 02-11-2026 | Recon module `LOGIN` | `/generate-requirements-from-website login` | Lệch so với bản đồ: ước 15–20 REQ, thực tế **28 REQ** (gồm Forgot Password, đăng xuất, cookie ghi nhớ, bảo vệ route). Route và ranh giới module không đổi | UI thực tế |
| 05-11-2026 | Cập nhật theo trả lời của user | `/update-requirements-from-ticket` | User xác nhận 05-11-2026: tạm thời hệ thống chỉ có role admin: AMB-SYS-02 ✅, cột Super Admin + role khác thành không áp dụng, AMB-SYS-01 viết lại. Danh sách module không đổi | User cung cấp — chưa xác minh UI |
| 05-11-2026 | Cập nhật theo trả lời của user | Trả lời trực tiếp | AMB-SYS-01 ✅ tài khoản `.env` không được phép vào khu Setup. AMB-SYS-03 ✅ được tạo dữ liệu thử. Danh sách module không đổi | User cung cấp |
| 05-11-2026 | Cập nhật theo trả lời của user | Trả lời trực tiếp | AMB-SYS-04 ✅ chốt năng lực QA. Danh sách module không đổi | User cung cấp |
| 16-11-2026 | Recon module `CUST` | `/generate-requirements-from-website CUST` | Lệch so với bản đồ: ước 60–80 REQ, thực tế **115 REQ / 7 Story** (phạm vi "lõi + tab riêng"; 11 tab chứng từ chỉ ở mức hiển thị). Tab con thứ 3 `Customer Admins` chỉ có ở form **sửa**, form tạo có 2 tab. Thêm route `/admin/clients/all_contacts` (trang Contacts tổng) và `/admin/clients/import` đã mở. Danh sách nhân viên (Assign Admin) có nhân viên tên "Project Manager" — liên quan AMB-LOGIN-24. Ranh giới module, prefix không đổi. Bảng *Bản đồ tài liệu*: `CUST` ⬜ → ✅, đồng thời sửa `LOGIN` ⬜ → ✅ (bị sót từ 02-11-2026, danh mục đã ghi ✅) | UI thực tế |

## Ambiguity & Risk cấp hệ thống

| Mã | Loại | Nội dung | Mức |
|---|---|---|---|
| AMB-SYS-01 | Ambiguity | Tài khoản admin trong `.env` bị chặn ở khu Setup / Staff / Roles / Activity Log → ✅ Đã trả lời 05-11-2026: tài khoản này không được phép vào khu Setup. `SETTING`, `STAFF` giữ ⏸️ Hoãn | 🔴 |
| AMB-SYS-02 | Ambiguity | Danh sách role của hệ thống chưa biết → ✅ Đã trả lời 05-11-2026: tạm thời chỉ có role admin (chưa kiểm chứng trên UI vì `/admin/roles` bị chặn) | 🔴 |
| AMB-SYS-03 | Ambiguity | 5 module đang **0 bản ghi**: Tickets · Subscriptions · Credit Notes · Estimate Request · Knowledge Base → ✅ Đã trả lời 05-11-2026: được tạo dữ liệu thử trên môi trường hiện tại khi recon | 🔴 |
| AMB-SYS-04 | Ambiguity | Năng lực QA (API · CSDL · tích hợp · DevTools) chưa xác nhận → ✅ Đã trả lời 05-11-2026: có DevTools + quan sát network; không có quyền gọi API trực tiếp, CSDL, tầng tích hợp. Chi tiết ở `../README.md` | 🔴 |
| RISK-SYS-01 | Risk | Môi trường dùng chung, dữ liệu do nhiều người tạo/sửa liên tục → số liệu Dashboard / Reports / bộ đếm summary biến động giữa các lần chạy; AC không được assert giá trị tuyệt đối | 🟡 |
| RISK-SYS-02 | Risk | Dữ liệu master (tax, currency, payment mode, department…) chỉ sửa được ở Setup đang BLOCKED → không chủ động tạo được tiền điều kiện cho TC | 🟡 |
| RISK-SYS-03 | Risk | Trạng thái hoá đơn có thể lệch giữa hai màn tổng hợp: báo cáo Sales ghi "Cancelled invoices are excluded" nhưng widget "Invoice overview" ở Dashboard không có Cancelled → tổng số Dashboard và Reports có thể không khớp | 🟡 |

## Bản đồ tài liệu

| File | Module bao phủ | Prefix | Trạng thái recon |
|---|---|---|---|
| [modules/module_01_dang_nhap.md](modules/module_01_dang_nhap.md) | Đăng nhập | `LOGIN` | ✅ |
| [modules/module_02_khach_hang.md](modules/module_02_khach_hang.md) | Khách hàng | `CUST` | ✅ |
| [modules/module_03_hang_hoa.md](modules/module_03_hang_hoa.md) | Hàng hoá | `ITEM` | ⬜ |
| [modules/module_04_du_an_cong_viec.md](modules/module_04_du_an_cong_viec.md) | Dự án · Công việc | `PRJ` · `TASK` | ⬜ ⬜ |
| [modules/module_05_de_xuat_bao_gia.md](modules/module_05_de_xuat_bao_gia.md) | Đề xuất · Báo giá | `PROP` · `EST` | ⬜ ⬜ |
| [modules/module_06_hoa_don.md](modules/module_06_hoa_don.md) | Hoá đơn | `INV` | ⬜ |
| [modules/module_07_thanh_toan.md](modules/module_07_thanh_toan.md) | Thanh toán | `PAY` | ⬜ |
| [modules/module_08_giay_bao_co.md](modules/module_08_giay_bao_co.md) | Giấy báo có | `CRN` | ⬜ |
| [modules/module_09_hop_dong.md](modules/module_09_hop_dong.md) | Hợp đồng | `CTR` | ⬜ |
| [modules/module_10_khach_tiem_nang.md](modules/module_10_khach_tiem_nang.md) | Khách tiềm năng | `LEAD` | ⬜ |
| [modules/module_11_chi_phi.md](modules/module_11_chi_phi.md) | Chi phí | `EXP` | ⬜ |
| [modules/module_12_goi_dinh_ky.md](modules/module_12_goi_dinh_ky.md) | Gói định kỳ | `SUBS` | ⬜ |
| [modules/module_13_ho_tro_ticket.md](modules/module_13_ho_tro_ticket.md) | Hỗ trợ | `TICK` | ⬜ |
| [modules/module_14_yeu_cau_bao_gia.md](modules/module_14_yeu_cau_bao_gia.md) | Yêu cầu báo giá | `EREQ` | ⬜ |
| [modules/module_15_dashboard_bao_cao.md](modules/module_15_dashboard_bao_cao.md) | Dashboard · Báo cáo | `DASH` · `RPT` | ⬜ ⬜ |
| [modules/module_16_lich_tri_thuc_tien_ich.md](modules/module_16_lich_tri_thuc_tien_ich.md) | Lịch · Cơ sở tri thức · Tiện ích | `CAL` · `KBASE` · `UTIL` | ⬜ ⬜ ⬜ |
| [modules/module_17_ca_nhan.md](modules/module_17_ca_nhan.md) | Cá nhân | `PROF` | ⬜ |
| [modules/module_18_cau_hinh_he_thong.md](modules/module_18_cau_hinh_he_thong.md) | Cấu hình hệ thống | `SETTING` | ⏸️ |
| [modules/module_19_nhan_vien_vai_tro.md](modules/module_19_nhan_vien_vai_tro.md) | Nhân viên & Vai trò | `STAFF` | ⏸️ |

> Cột trạng thái ở bảng này là ảnh chụp lúc khám phá — **nguồn sự thật là [`../README.md`](../README.md)**.

## Danh mục evidence

Thư mục [`evidence/`](evidence/) — chụp 02-11-2026 trên Chrome local, viewport 1598×790. Hậu tố `_fullpage` = cả trang, `_viewport` = vùng đang hiển thị.

| Tệp | Màn hình · trạng thái | Module |
|---|---|---|
| [login_overview_viewport.png](evidence/login_overview_viewport.png) | Trang đăng nhập, form trống (browser context không cookie) | `LOGIN` |
| [cust_overview_fullpage.png](evidence/cust_overview_fullpage.png) | Danh sách Customers + Customers Summary | `CUST` |
| [item_overview_fullpage.png](evidence/item_overview_fullpage.png) | Danh sách Items | `ITEM` |
| [prj_overview_fullpage.png](evidence/prj_overview_fullpage.png) | Danh sách Projects + Projects Summary | `PRJ` |
| [task_overview_fullpage.png](evidence/task_overview_fullpage.png) | Danh sách Tasks + Tasks Summary | `TASK` |
| [prop_overview_fullpage.png](evidence/prop_overview_fullpage.png) | Danh sách Proposals | `PROP` |
| [est_overview_fullpage.png](evidence/est_overview_fullpage.png) | Danh sách Estimates (nhãn "Invoiced") | `EST` |
| [inv_overview_fullpage.png](evidence/inv_overview_fullpage.png) | Danh sách Invoices | `INV` |
| [pay_overview_fullpage.png](evidence/pay_overview_fullpage.png) | Danh sách Payments | `PAY` |
| [crn_overview_fullpage.png](evidence/crn_overview_fullpage.png) | Danh sách Credit Notes — rỗng | `CRN` |
| [ctr_overview_fullpage.png](evidence/ctr_overview_fullpage.png) | Contracts: Summary + 2 biểu đồ + danh sách | `CTR` |
| [lead_overview_fullpage.png](evidence/lead_overview_fullpage.png) | Danh sách Leads | `LEAD` |
| [exp_overview_fullpage.png](evidence/exp_overview_fullpage.png) | Danh sách Expenses | `EXP` |
| [subs_overview_fullpage.png](evidence/subs_overview_fullpage.png) | Subscriptions — rỗng, Summary có logo stripe | `SUBS` |
| [tick_overview_fullpage.png](evidence/tick_overview_fullpage.png) | Tickets — rỗng + Tickets Summary | `TICK` |
| [ereq_overview_fullpage.png](evidence/ereq_overview_fullpage.png) | Estimate Request — rỗng | `EREQ` |
| [dash_overview_fullpage.png](evidence/dash_overview_fullpage.png) | Dashboard 13 widget | `DASH` |
| [rpt_overview_fullpage.png](evidence/rpt_overview_fullpage.png) | Reports → Sales | `RPT` |
| [cal_overview_fullpage.png](evidence/cal_overview_fullpage.png) | Calendar — tháng 11-2026 | `CAL` |
| [kbase_overview_fullpage.png](evidence/kbase_overview_fullpage.png) | Knowledge Base — rỗng | `KBASE` |
| [util_overview_fullpage.png](evidence/util_overview_fullpage.png) | Media — trình quản lý file | `UTIL` |
| [util_bulk_pdf_export_fullpage.png](evidence/util_bulk_pdf_export_fullpage.png) | Bulk PDF Export — form mặc định | `UTIL` |
| [prof_overview_fullpage.png](evidence/prof_overview_fullpage.png) | My Profile (có email + số điện thoại tài khoản — user chấp nhận giữ) | `PROF` |
| [setting_access_denied_viewport.png](evidence/setting_access_denied_viewport.png) | `/admin/settings` → Access denied | `SETTING` |
| [staff_access_denied_viewport.png](evidence/staff_access_denied_viewport.png) | `/admin/staff` → Access denied | `STAFF` |

**25 ảnh · 24/24 module có ảnh.**
