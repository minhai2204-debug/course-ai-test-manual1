# Danh mục Requirements — Hệ thống CRM (Perfex CRM · khu admin)

> **Điểm vào cấp hệ thống.** Đọc file này trước khi recon bất kỳ module nào: biết module nào đã có, **prefix nào đã bị chiếm**, mã REQ kế tiếp.
> Bản đồ khám phá: [`_discovery/system_map.md`](_discovery/system_map.md)

## Thuộc tính hệ thống

| Thuộc tính | Giá trị |
|---|---|
| **Tên hệ thống** | Perfex CRM 3.1.6 (bản demo dùng cho khoá học) — khu quản trị `/admin/*` |
| **Mã hệ thống** | `CRM` — tiền tố TC ID (`CRM_…`) |
| **URL · tài khoản** | Lưu ở `.env` (biến `URL`, `EMAIL_ADMIN`, `PASSWORD_ADMIN`) — **không** ghi vào `docs/` |
| **Môi trường** | 🔒 **Dùng chung**. Từ 05-11-2026 user cho phép **tạo dữ liệu thử** ngay trên môi trường này (AMB-SYS-03): chỉ tạo mới, đặt tên nhận diện được; không sửa / xoá bản ghi có sẵn. Có dữ liệu do người khác tạo (VD bộ lọc `auto_filter_tc029_*`, ~2.800 khách hàng) |
| **Phạm vi đợt này** | Chỉ khu admin. **Cổng khách hàng** (`/clients/*`, dùng URL/tài khoản khác) — user sẽ cung cấp sau → chạy `/discover-system` mode ADD |
| **Năng lực kiểm thử của QA** | Chốt 05-11-2026 (AMB-SYS-04 ✅), cập nhật CSDL 14-11-2026 — dùng cho nhánh Vòng 3 của **mọi** bộ TC. Phần không có quyền ghi là **không kiểm được**, không viết thành case chạy được:<br>• DevTools trình duyệt: ✅ có — đã dùng thật trên Chrome local (DOM, network, cookie)<br>• Quan sát network: ✅ có — chỉ thụ động, request do UI tự gửi (VD `POST /admin/<module>/table`)<br>• Gọi API trực tiếp: ❌ không có quyền — chưa có đặc tả API<br>• Truy vấn CSDL: ✅ **chỉ `SELECT`** — user xác nhận 14-11-2026. Truy vấn **tổng hợp** (loại C — `COUNT`/`SUM`… chỉ trả số, không trả dòng thô) trên dữ liệu nghiệp vụ thật: ✅ cho phép (user, 15-11-2026). Công thức báo cáo / dashboard lấy từ **tài liệu phân tích yêu cầu** (Định nghĩa chỉ số `MET-…`), không từ mã nguồn app. Luật: `.claude/rules/database_rules.md`, chạy qua `scripts/db-check/`. Engine · tài khoản có read-only phía DB không · cách kết nối: **chưa chốt** (AMB-SYS-05). `.env` chưa có biến `DB_*` → agent chưa tự chạy truy vấn được; TC `@DBCheck` vẫn sinh, phần 🗄️ chấm `BLOCKED` khi thực thi cho tới khi có kết nối<br>• Kiểm tầng tích hợp (email, cron, Stripe): ❌ không có quyền — chưa có hộp thư test, chưa có tài khoản Stripe test<br>• Xem nhật ký hoạt động: ❌ tài khoản bị chặn (`/admin/utilities/activity_log` → Access denied, đo 02-11-2026) — tài khoản `.env` không được phép vào (AMB-SYS-01 ✅) |

## 1. Bảng danh mục module

| Module | Prefix | Nền tảng | Trạng thái recon | Mức phủ tài liệu | Tài liệu | REQ đã dùng | Mã kế tiếp | AMB treo | Story | Cập nhật |
|---|---|---|---|---|---|---|---|---|---|---|
| Đăng nhập (Login / Forgot Password) | `LOGIN` | Web ✅ | ✅ Đã có tài liệu | ⬜ Trắng ¹ | [`login/REQUIREMENTS_LOGIN_SUMMARY.md`](login/REQUIREMENTS_LOGIN_SUMMARY.md) | 01 → 47 | `REQ-LOGIN-48` | 0 — 23 AMB ⏭️ theo Assumption tạm | 6 | 11-11-2026 |
| Khách hàng (Customers · Contacts) | `CUST` | Web ✅ | ✅ Đã có tài liệu | ⬜ Trắng ² | [`customers/REQUIREMENTS_CUSTOMERS_SUMMARY.md`](customers/REQUIREMENTS_CUSTOMERS_SUMMARY.md) | 01 → 115 | `REQ-CUST-116` | 23 (3 🔴) | 7 | 16-11-2026 |
| Hàng hoá (Items) | `ITEM` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-ITEM-01` | — | — | 02-11-2026 |
| Dự án (Projects) | `PRJ` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-PRJ-01` | — | — | 02-11-2026 |
| Công việc (Tasks · Timesheets) | `TASK` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-TASK-01` | — | — | 02-11-2026 |
| Đề xuất (Proposals) | `PROP` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-PROP-01` | — | — | 02-11-2026 |
| Báo giá (Estimates) | `EST` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-EST-01` | — | — | 02-11-2026 |
| Hoá đơn (Invoices) | `INV` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-INV-01` | — | — | 02-11-2026 |
| Thanh toán (Payments) | `PAY` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-PAY-01` | — | — | 02-11-2026 |
| Giấy báo có (Credit Notes) | `CRN` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-CRN-01` | — | — | 05-11-2026 |
| Hợp đồng (Contracts) | `CTR` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-CTR-01` | — | — | 02-11-2026 |
| Khách tiềm năng (Leads) | `LEAD` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-LEAD-01` | — | — | 02-11-2026 |
| Chi phí (Expenses) | `EXP` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-EXP-01` | — | — | 02-11-2026 |
| Gói định kỳ (Subscriptions) | `SUBS` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-SUBS-01` | — | — | 05-11-2026 |
| Hỗ trợ (Support Tickets) | `TICK` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-TICK-01` | — | — | 05-11-2026 |
| Yêu cầu báo giá (Estimate Request) | `EREQ` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-EREQ-01` | — | — | 05-11-2026 |
| Bảng điều khiển (Dashboard) | `DASH` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-DASH-01` | — | — | 02-11-2026 |
| Báo cáo (Reports) | `RPT` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-RPT-01` | — | — | 02-11-2026 |
| Lịch (Calendar) | `CAL` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-CAL-01` | — | — | 02-11-2026 |
| Cơ sở tri thức (Knowledge Base) | `KBASE` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-KBASE-01` | — | — | 05-11-2026 |
| Tiện ích (Media · Bulk PDF Export) | `UTIL` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-UTIL-01` | — | — | 02-11-2026 |
| Cá nhân (Profile · To Do · Reminders · Notifications · Newsfeed) | `PROF` | Web ⬜ | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-PROF-01` | — | — | 02-11-2026 |
| Cấu hình hệ thống (Setup) | `SETTING` | Web ⬜ | ⏸️ Hoãn — tài khoản `.env` không được phép vào | ⬜ Trắng | — | — | `REQ-SETTING-01` | — | — | 05-11-2026 |
| Nhân viên & Vai trò (Staff · Roles) | `STAFF` | Web ⬜ | ⏸️ Hoãn — tài khoản `.env` không được phép vào | ⬜ Trắng | — | — | `REQ-STAFF-01` | — | — | 05-11-2026 |

¹ Repo có `SRS_Login_Module.md` trong lịch sử git — user chọn **không dùng** khi recon `LOGIN` (mode UI, 02-11-2026).
² User xác nhận 16-11-2026: `CUST` không có tài liệu nào — mode UI.

**Tổng: 24 module** — 20 ⬜ · 2 ⏸️ · 2 ✅.

### Danh sách prefix đã chiếm

`LOGIN` · `CUST` · `ITEM` · `PRJ` · `TASK` · `PROP` · `EST` · `INV` · `PAY` · `CRN` · `CTR` · `LEAD` · `EXP` · `SUBS` · `TICK` · `EREQ` · `DASH` · `RPT` · `CAL` · `KBASE` · `UTIL` · `PROF` · `SETTING` · `STAFF`
Dành riêng: `SYS` (AMB/RISK cấp hệ thống — không cấp cho module).

> Module mới **phải** chọn prefix chưa có ở danh sách trên. Prefix đã cấp là vĩnh viễn, kể cả khi module đổi tên trên UI.

## 2. Trạng thái REQ toàn hệ thống

| Module | 🟢 | 🟡 | 🔴 | ⚪ | Tổng |
|---|---|---|---|---|---|
| `LOGIN` | 25 | 0 | 0 | 22 | 47 |
| `CUST` | 99 | 0 | 0 | 16 | 115 |
| **Toàn hệ thống** | **124** | **0** | **0** | **38** | **162** |

## 3. Ambiguity 🔴 High còn treo

| Mã | Nội dung | Ảnh hưởng | Người cần trả lời |
|---|---|---|---|
| AMB-CUST-01 | Company chỉ gồm khoảng trắng vượt qua validation phía trình duyệt; môi trường đã có KH Company toàn khoảng trắng. Server có chặn không — có phải lỗi? | REQ-CUST-31 ghi theo hành vi hiện tại, nghi lỗi; KH không tên gây chọn nhầm ở chứng từ | PO |
| AMB-CUST-03 | Ghi chú KH với mô tả trống vẫn lưu được ("Note added successfully."). Cố ý? | REQ-CUST-82 ghi theo hành vi hiện tại, nghi lỗi | PO |
| AMB-CUST-08 | Xin tài khoản nhân viên role khác (danh sách nhân viên có "Project Manager") để kiểm 7 ô phân quyền module `CUST` — cùng nhu cầu với AMB-LOGIN-24 | Cột role khác của ma trận phân quyền `CUST` toàn ❔ | User / quản trị |
| AMB-SYS-05 | CSDL: engine nào (MySQL/MariaDB · PostgreSQL · SQL Server…)? Tài khoản QA có bị giới hạn **chỉ đọc ở phía DB** hay chỉ là quy định? Máy QA kết nối thẳng được không (host/port, VPN)? | Chưa chạy được khối 🗄️ của TC `@DBCheck`, chưa khảo sát được `_discovery/db_map.md` và mục *Ánh xạ dữ liệu* — TC `@DBCheck` sinh trước phải dùng placeholder `<bảng>.<cột>` + `@NeedsVerify` | User / DBA |

> `LOGIN`: 4 AMB 🔴 (AMB-LOGIN-03, 05, 06, 12) vẫn ⏭️ từ 05-11-2026 — user chốt test theo Assumption tạm. **Chưa có câu trả lời thật**, rủi ro được chấp nhận; xem [Impact Report](login/impact/impact_LOGIN-ASSUMPTIONS-05112026.md). AMB-LOGIN-10 đã ✅ ngày 11-11-2026 nhờ ticket khoá tài khoản ([Impact Report](login/impact/impact_LOGIN-LOCKOUT-11112026.md)). 3 AMB 🔴 của ticket đó (AMB-LOGIN-19, 23, 24) chuyển ⏭️ cùng ngày theo Assumption tạm ([Impact Report](login/impact/impact_LOGIN-ASSUMPTIONS-11112026.md)) — **vẫn chưa có tài khoản Project Manager** thật, STORY-LOGIN-06 chưa chạy được.

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
| 05-11-2026 | `LOGIN`: user chốt dùng Assumption tạm cho 16 AMB còn treo → ⏭️. Thêm REQ-LOGIN-29 → 34 ⚪. Mã kế tiếp `REQ-LOGIN-35` | `/update-requirements-from-ticket` |
| 05-11-2026 | User trả lời: AMB-SYS-01 ✅ tài khoản `.env` không được phép vào khu Setup → `SETTING`, `STAFF` giữ ⏸️ Hoãn. AMB-SYS-03 ✅ được tạo dữ liệu thử trên môi trường hiện tại. Gỡ cả hai khỏi mục 3 | Trả lời trực tiếp của user |
| 05-11-2026 | User chốt AMB-SYS-04 ✅: QA có DevTools + quan sát network; không có quyền gọi API trực tiếp, CSDL, tầng tích hợp, nhật ký hoạt động. Gỡ khỏi mục 3 | Trả lời trực tiếp của user |
| 11-11-2026 | `LOGIN`: ticket khoá tài khoản (mã nội bộ `LOGIN-LOCKOUT-11112026`) → thêm REQ-LOGIN-35 → 41 ⚪ + STORY-LOGIN-06; AMB-LOGIN-10 ✅; thêm AMB-LOGIN-19 → 26 (3 🔴 vào mục 3) và RISK-LOGIN-07, 08. Mã kế tiếp `REQ-LOGIN-42` | `/update-requirements-from-ticket` |
| 11-11-2026 | `LOGIN`: user chốt dùng Assumption tạm cho AMB-LOGIN-19 → 26 → ⏭️, gỡ 3 AMB 🔴 khỏi mục 3. Thêm REQ-LOGIN-42 → 47 ⚪. Mã kế tiếp `REQ-LOGIN-48` | `/update-requirements-from-ticket` |
| 14-11-2026 | User cho phép QA truy cập CSDL, **chỉ `SELECT`** → dòng `Năng lực kiểm thử của QA` đổi `Truy vấn CSDL` ❌ → ✅. Mở AMB-SYS-05 🔴 (engine · tài khoản read-only · cách kết nối). **Cần rà lại:** bộ TC `LOGIN` đang chấm V3 `Database` `➖` vì lý do cũ — chạy `/update-testcases-from-impact` để bổ sung TC `@DBCheck` (nhóm D5 mật khẩu băm, D6 bộ đếm khoá tài khoản) | Trả lời trực tiếp của user |
| 15-11-2026 | User chốt: cho phép truy vấn **tổng hợp** (loại C) trên dữ liệu nghiệp vụ thật để kiểm báo cáo / dashboard · công thức báo cáo lấy từ **tài liệu phân tích yêu cầu** (Định nghĩa chỉ số `MET-<MODULE>-<nn>`). Cập nhật dòng `Năng lực kiểm thử của QA` | Trả lời trực tiếp của user |
| 16-11-2026 | `CUST` → ✅: phát hành `customers/REQUIREMENTS_CUSTOMERS_SUMMARY.md` + `customers/web/` (7 file story) — REQ-CUST-01 → 115 · 20 AMB (3 🔴 vào mục 3) · 9 RISK · 7 Story. Tạo 2 KH test (id 16007, 16008) — user chốt giữ lại cho lượt sinh test case (RISK-CUST-09) | `/generate-requirements-from-website CUST` |
