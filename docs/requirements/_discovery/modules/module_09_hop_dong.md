# Module 09 — Hợp đồng (`CTR`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md) · Khảo sát: 02-11-2026, mode UI, chỉ đọc

## `CTR` — Contracts

| Mục | Giá trị |
|---|---|
| Route | `/admin/contracts` · Tạo mới `/admin/contracts/contract` · Sửa/xem `/admin/contracts/contract/{id}` |
| Loại màn hình | Danh sách + 2 biểu đồ + form |
| Khối tổng hợp | Contract Summary · Contracts by Type · Contracts Value by Type (USD) |
| Thanh công cụ | New Contract · Export |
| Cột bảng `#contracts` | # · Subject · Customer · Contract Type · Contract Value · Start Date · End Date · Project · Signature |
| Status flow | "Contract Summary": **Active · Expired · About to Expire · Recently Added · Trash**; cột `Signature`: **Not Signed · Marked as signed**; dòng hết hạn tô đỏ; Dashboard có widget "Contracts Expiring Soon" |
| Ước lượng | 20–30 REQ |
| Risk | 🟡 — có giá trị tiền và chữ ký, nhưng không sinh công nợ trực tiếp |

### Vùng chưa xác minh
- Luồng ký hợp đồng (Signature) — chưa quan sát
- Contract Type lấy từ Setup (BLOCKED)

### Evidence

| Tệp | Màn hình · trạng thái |
|---|---|
| [ctr_overview_fullpage.png](../evidence/ctr_overview_fullpage.png) | Danh sách Contracts + Contract Summary + 2 biểu đồ |
