# Danh mục Requirements — Hệ thống CRM (Perfex CRM · khu admin)

> **Điểm vào cấp hệ thống.** Đọc file này trước khi recon bất kỳ module nào: biết module nào đã có, **prefix nào đã bị chiếm**, mã REQ kế tiếp.
> Bản đồ khám phá: [`_discovery/system_map.md`](_discovery/system_map.md)

## Thuộc tính hệ thống

| Thuộc tính | Giá trị |
|---|---|
| **Tên hệ thống** | Perfex CRM 3.1.6 (bản demo dùng cho khoá học) — khu quản trị `/admin/*` |
| **Mã hệ thống** | `CRM` — tiền tố TC ID (`CRM_…`) |
| **URL · tài khoản** | Lưu ở `.env` (biến `URL`, `EMAIL_ADMIN`, `PASSWORD_ADMIN`) — **không** ghi vào `docs/` |
| **Môi trường** | 🔒 **Dùng chung** — chỉ đọc khi khám phá. Có dữ liệu do người khác tạo (VD bộ lọc `auto_filter_tc029_*`, ~2.800 khách hàng) |
| **Phạm vi đợt này** | Chỉ khu admin. **Cổng khách hàng** (`/clients/*`, dùng URL/tài khoản khác) — user sẽ cung cấp sau → chạy `/discover-system` mode ADD |
| **Năng lực kiểm thử của QA** | Chốt 02-11-2026 — dùng cho nhánh Vòng 3 của **mọi** bộ TC:<br>• Gọi API: ❔ chưa xác nhận — hệ thống không có REST API công khai, dữ liệu bảng tải qua `POST /admin/<module>/table` (DataTables)<br>• Truy vấn CSDL: ❔ chưa xác nhận<br>• Kiểm tầng tích hợp (email, cron, Stripe): ❔ chưa xác nhận<br>• Xem nhật ký hoạt động: ❌ tài khoản bị chặn (`/admin/utilities/activity_log` → Access denied, đo 02-11-2026) — chưa rõ tài khoản nào mở được (AMB-SYS-01)<br>• DevTools trình duyệt: ❔ chưa xác nhận |

## 1. Bảng danh mục module

| Module | Prefix | Nền tảng | Trạng thái recon | Mức phủ tài liệu | Tài liệu | REQ đã dùng | Mã kế tiếp | AMB treo | Story | Cập nhật |
|---|---|---|---|---|---|---|---|---|---|---|
| Đăng nhập (Login / Forgot Password) | `LOGIN` | Web ✅ | ✅ Đã có tài liệu | ⬜ Trắng ¹ | [`login/REQUIREMENTS_LOGIN_SUMMARY.md`](login/REQUIREMENTS_LOGIN_SUMMARY.md) | 01 → 28 | `REQ-LOGIN-29` | 16 (🔴 5) — xem mục 3 | 5 | 05-11-2026 |
| Khách hàng (Customers · Contacts) | `CUST` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-CUST-01` | — | — | 02-11-2026 |
| Hàng hoá (Items) | `ITEM` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-ITEM-01` | — | — | 02-11-2026 |
| Dự án (Projects) | `PRJ` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-PRJ-01` | — | — | 02-11-2026 |
| Công việc (Tasks · Timesheets) | `TASK` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-TASK-01` | — | — | 02-11-2026 |
| Đề xuất (Proposals) | `PROP` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-PROP-01` | — | — | 02-11-2026 |
| Báo giá (Estimates) | `EST` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-EST-01` | — | — | 02-11-2026 |
| Hoá đơn (Invoices) | `INV` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-INV-01` | — | — | 02-11-2026 |
| Thanh toán (Payments) | `PAY` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-PAY-01` | — | — | 02-11-2026 |
| Giấy báo có (Credit Notes) | `CRN` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-CRN-01` | AMB-SYS-03 | — | 02-11-2026 |
| Hợp đồng (Contracts) | `CTR` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-CTR-01` | — | — | 02-11-2026 |
| Khách tiềm năng (Leads) | `LEAD` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-LEAD-01` | — | — | 02-11-2026 |
| Chi phí (Expenses) | `EXP` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-EXP-01` | — | — | 02-11-2026 |
| Gói định kỳ (Subscriptions) | `SUBS` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-SUBS-01` | AMB-SYS-03 | — | 02-11-2026 |
| Hỗ trợ (Support Tickets) | `TICK` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-TICK-01` | AMB-SYS-03 | — | 02-11-2026 |
| Yêu cầu báo giá (Estimate Request) | `EREQ` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-EREQ-01` | AMB-SYS-03 | — | 02-11-2026 |
| Bảng điều khiển (Dashboard) | `DASH` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-DASH-01` | — | — | 02-11-2026 |
| Báo cáo (Reports) | `RPT` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-RPT-01` | — | — | 02-11-2026 |
| Lịch (Calendar) | `CAL` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-CAL-01` | — | — | 02-11-2026 |
| Cơ sở tri thức (Knowledge Base) | `KBASE` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-KBASE-01` | AMB-SYS-03 | — | 02-11-2026 |
| Tiện ích (Media · Bulk PDF Export) | `UTIL` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-UTIL-01` | — | — | 02-11-2026 |
| Cá nhân (Profile · To Do · Reminders · Notifications · Newsfeed) | `PROF` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-PROF-01` | — | — | 02-11-2026 |
| Cấu hình hệ thống (Setup) | `SETTING` | Web ⬜ | ⏸️ Hoãn — BLOCKED, tài khoản `.env` bị Access denied | ⬜ Trắng | — | — | `REQ-SETTING-01` | AMB-SYS-01 | — | 02-11-2026 |
| Nhân viên & Vai trò (Staff · Roles) | `STAFF` | Web ⬜ | ⏸️ Hoãn — BLOCKED, tài khoản `.env` bị Access denied | ⬜ Trắng | — | — | `REQ-STAFF-01` | AMB-SYS-01 | — | 02-11-2026 |

¹ Repo có `SRS_Login_Module.md` trong lịch sử git — user chọn **không dùng** khi recon `LOGIN` (mode UI, 02-11-2026).

**Tổng: 24 module** — 21 ⬜ · 2 ⏸️ · 1 ✅.

### Danh sách prefix đã chiếm

`LOGIN` · `CUST` · `ITEM` · `PRJ` · `TASK` · `PROP` · `EST` · `INV` · `PAY` · `CRN` · `CTR` · `LEAD` · `EXP` · `SUBS` · `TICK` · `EREQ` · `DASH` · `RPT` · `CAL` · `KBASE` · `UTIL` · `PROF` · `SETTING` · `STAFF`
Dành riêng: `SYS` (AMB/RISK cấp hệ thống — không cấp cho module).

> Module mới **phải** chọn prefix chưa có ở danh sách trên. Prefix đã cấp là vĩnh viễn, kể cả khi module đổi tên trên UI.

## 2. Trạng thái REQ toàn hệ thống

| Module | 🟢 | 🟡 | 🔴 | ⚪ | Tổng |
|---|---|---|---|---|---|
| `LOGIN` | 25 | 0 | 0 | 3 | 28 |
| **Toàn hệ thống** | **25** | **0** | **0** | **3** | **28** |

## 3. Ambiguity 🔴 High còn treo

| Mã | Nội dung | Ảnh hưởng | Người cần trả lời |
|---|---|---|---|
| AMB-SYS-01 | Tài khoản admin trong `.env` bị `Access denied` ở toàn bộ khu Setup, Staff, Roles, Activity Log, trong khi user xác nhận (05-11-2026) tạm thời hệ thống chỉ có role admin. Tài khoản nào mở được các khu này, hay quyền của tài khoản hiện tại đang thiếu? | `SETTING` · `STAFF` BLOCKED; nhánh Logging/Audit của TC không kiểm được | PO / chủ môi trường |
| AMB-SYS-03 | 5 module đang **0 bản ghi** (Tickets · Subscriptions · Credit Notes · Estimate Request · Knowledge Base) — chưa thấy màn chi tiết; môi trường dùng chung nên không tự tạo | `TICK` · `SUBS` · `CRN` · `EREQ` · `KBASE` recon thiếu màn chi tiết | PO / QA Lead |
| AMB-SYS-04 | Năng lực QA (gọi API · CSDL · tầng tích hợp · DevTools) chưa được xác nhận | Nhánh Vòng 3 của mọi bộ TC | QA Lead |
| AMB-LOGIN-03 | Contact khách hàng có đăng nhập được vào `/admin` không? | `LOGIN` — bảo mật phân tách 2 cổng | PO / Dev |
| AMB-LOGIN-05 | Forgot Password bỏ trống trả "Email not found" thay vì thông báo bắt buộc | `LOGIN` — nghi lỗi | PO / Dev |
| AMB-LOGIN-06 | Forgot Password tiết lộ email có tồn tại hay không | `LOGIN` — bảo mật | PO / Dev |
| AMB-LOGIN-10 | Chính sách khoá tài khoản / giới hạn đăng nhập sai | `LOGIN` — chống brute-force | PO / Dev |
| AMB-LOGIN-12 | Cookie `autologin` có khôi phục phiên không, hạn 62 ngày có đúng cấu hình? | `LOGIN` — REQ-LOGIN-16 ⚪ | Dev |

## 4. Cấu trúc thư mục chuẩn

```
docs/requirements/
├── README.md                              ← DANH MỤC (file này)
├── _discovery/                            ← tầng khám phá — do /discover-system ghi
│   ├── system_map.md                      ← INDEX bất biến
│   ├── modules/module_NN_<slug>.md        ← chi tiết module (bản đồ đã tách)
│   └── evidence/                          ← 1 ảnh tổng quan / module
└── <module>/
    ├── REQUIREMENTS_<TÊN_MODULE>_SUMMARY.md  ← INDEX module — tên bất biến
    ├── web/ · mobile/ · api/              ← tầng nền tảng (chỉ 3 tên này)
    │   ├── requirements_<module>_<nền-tảng>.md
    │   └── evidence/
    ├── analysis/                          ← phân tích ticket
    └── impact/                            ← Impact Report
```

## 5. Quy trình sử dụng

| Tình huống | Workflow | Ghi vào đâu |
|---|---|---|
| Recon một module trên web admin | `/generate-requirements-from-website <module>` | `<module>/web/` + cập nhật dòng ở bảng 1 |
| Thêm cổng khách hàng / module bị sót | `/discover-system` (mode ADD) | `_discovery/` + bảng 1 |
| Hệ thống vừa deploy tính năng mới | `/discover-system` (mode DELTA) | `_discovery/system_map.md` mục 7 |
| Phân tích tài liệu / ticket | `/analyze-requirement-document` | `<module>/analysis/` |
| Ticket thay đổi requirements đã có | `/update-requirements-from-ticket` | `<module>/` + `impact/` |
| Sinh test case từ requirements | `/generate-testcases-manual-rbt` | `docs/testcases/<module>/` |

> Mỗi lần recon xong một module: cập nhật cột `Nền tảng` · `Trạng thái recon` · `Tài liệu` · `REQ đã dùng` · `Mã kế tiếp` · `AMB treo` · `Cập nhật`.

## 6. Nhật ký danh mục

| Ngày | Thay đổi | Nguồn |
|---|---|---|
| 02-11-2026 | Khởi tạo danh mục — 24 module (22 ⬜ · 2 ⏸️), cấp 24 prefix. Bước 1 đối chiếu: chưa có `docs/requirements/` từ trước → không có lệch | `/discover-system` mode UI — khu admin, Chrome local, 25 ảnh evidence |
| 02-11-2026 | `LOGIN` → ✅: phát hành `login/REQUIREMENTS_LOGIN_SUMMARY.md` + `login/web/` — REQ-LOGIN-01 → 28 · 18 AMB · 6 RISK · 5 Story | `/generate-requirements-from-website login` |
| 05-11-2026 | User trả lời AMB-LOGIN-01: tạm thời hệ thống chỉ có role admin → AMB-LOGIN-01, AMB-LOGIN-02, AMB-SYS-02 ✅, gỡ khỏi mục 3. AMB-SYS-01 viết lại: bỏ giả định "thiếu quyền Super Admin" | `/update-requirements-from-ticket` |
