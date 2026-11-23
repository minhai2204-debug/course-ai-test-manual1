---
name: he-thong-va-pham-vi
description: Các quyết định cấp hệ thống user đã chốt — mã hệ thống, danh sách & thứ tự module, phạm vi, nguồn tài liệu
type: project
cập nhật: 17-11-2026
---

# Hệ thống và phạm vi

Nguồn chính thức: [`docs/requirements/README.md`](../../docs/requirements/README.md) (tầng 1) và [`_discovery/system_map.md`](../../docs/requirements/_discovery/system_map.md) (tầng 2). Ở đây chỉ ghi **lý do / lời user** đứng sau các quyết định.

| Quyết định | Ngày | Lời user / căn cứ |
|---|---|---|
| Hệ thống: Perfex CRM 3.1.6 demo của khoá học, **chỉ khu admin** `/admin/*` | 02-11-2026 | *"Trang này chỉ dành cho admin. Trang user/customer dùng URL khác, sau này tôi cập nhật chạy lại sau"* → cổng khách hàng chạy `/discover-system` mode ADD khi có URL |
| Mã hệ thống `CRM` → TC ID `CRM_<PREFIX>_TC_<nnn>` | 02-11-2026 | Đề xuất của agent, user không phản đối |
| 24 module · cách tách/gộp · thứ tự khảo sát `LOGIN → CUST → ITEM → PRJ → TASK → …` | 02-11-2026 | User: *"1. đã đủ 2. đúng 3. đúng"* |
| Evidence discovery chụp full-page bằng Chrome local, giữ nguyên dữ liệu demo người khác trong ảnh | 02-11-2026 | *"Chốt, giữ nguyên ảnh"* (site demo công khai) |
| `LOGIN` recon **mode UI**, **không** dùng `SRS_Login_Module.md` | 02-11-2026 | Chọn *"Bỏ — chỉ UI"* |
| `CUST` không có tài liệu → mode UI · phạm vi *Lõi + tab riêng* (không đi sâu cả 19 tab) | 16-11-2026 | Chọn qua câu hỏi đầu `/generate-requirements-from-website CUST` |
| `SETTING`, `STAFF` hoãn — tài khoản `.env` không được vào | 05-11-2026 | AMB-SYS-01 |

## Master Test Plan

- `/generate-master-test-plan` chạy 05-11-2026 → `test_plan_release_1.0.md` chỉ nằm trên nhánh `claude/generate-master-test-plan-180f8e` (xem [[nhanh-commit-va-don-worktree]]), **chưa có** `docs/test-plans/` ở thư mục chính.
- Quyết định khi đó: giữ 3 module trong phạm vi theo số liệu repo · dùng đúng 21 prefix của repo (phiếu ghi sai `CN`, `SUB`, `KB`…) · mốc đã qua giữ ngày + đánh dấu trễ · CI chọn **GitHub Actions** (phiếu ghi nhầm "GitLab Actions").
- Phiếu `plans/master-test-plan/test_plan.config.yaml` ở thư mục chính đã chép bản đã sửa.

Liên quan: [[quy-uoc-test-case]] · [[moi-truong-crm-dung-chung]]
