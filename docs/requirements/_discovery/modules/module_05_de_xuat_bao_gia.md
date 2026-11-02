# Module 05 — Đề xuất · Báo giá (`PROP` · `EST`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc
>
> Gộp chung file vì cùng là chứng từ trước bán hàng, dùng chung Items, luôn khảo sát liền nhau. **Vẫn là 2 prefix, 2 tài liệu requirements riêng.**

## `PROP` — Proposals

| Mục | Giá trị |
|---|---|
| Route | `/admin/proposals` · `/admin/proposals/list_proposals` · Tạo mới `/admin/proposals/proposal` |
| Loại màn hình | Danh sách (+ chế độ xem list_proposals) + form |
| Thanh công cụ | New Proposal · Export |
| Cột bảng `#proposals` | Proposal # · Subject · To · Total · Date · Open Till · Project · Tags · Date Created · Status |
| Status flow | 6 trạng thái (widget "Proposal overview" của Dashboard): **Draft · Sent · Open · Revised · Declined · Accepted** |
| Ước lượng | 25–30 REQ |
| Risk | 🟡 — chứng từ có tiền nhưng chưa phát sinh công nợ |

## `EST` — Estimates

| Mục | Giá trị |
|---|---|
| Route | `/admin/estimates` · `/admin/estimates/list_estimates` · Tạo mới `/admin/estimates/estimate` |
| Loại màn hình | Danh sách + form |
| Thanh công cụ | Create New Estimate · Export |
| Cột bảng `#estimates` | Estimate # · Amount · Total Tax · Customer · Project · Tags · Date · Expiry Date · Reference # · Status |
| Status flow | 6 trạng thái (widget "Estimate overview" của Dashboard): **Draft · Not Sent · Sent · Expired · Declined · Accepted** |
| Ước lượng | 25–35 REQ |
| Risk | 🔴 — tính tiền + thuế; **chuyển sang Invoice đã quan sát được** — estimate Accepted mang nhãn "Invoiced" dưới cột Amount |

### Vùng chưa xác minh
- Cột "To" của Proposal: gửi tới Customer hay cả Lead — chưa rõ
- Thao tác chuyển Estimate → Invoice (nút, điều kiện) — mới thấy kết quả (nhãn "Invoiced"), chưa mở luồng; Proposal → Estimate/Invoice — ❔
- Form tạo mới (dòng hàng, thuế, giảm giá) — chưa mở

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [prop_overview_fullpage.png](../evidence/prop_overview_fullpage.png) | Danh sách Proposals |
| [est_overview_fullpage.png](../evidence/est_overview_fullpage.png) | Danh sách Estimates — có nhãn "Invoiced" dưới Amount |
