## Impact Report — AMB-LOGIN-01 · 05-11-2026

> Không có ticket. Nguồn là câu trả lời trực tiếp của user: *"Tạm thời hệ thống chỉ có role admin"*.
> ← [Index module `LOGIN`](../REQUIREMENTS_LOGIN_SUMMARY.md)

### Tóm tắt

| Nhóm | Số lượng | REQ |
|---|---|---|
| 🟢 Thêm mới | 0 | — |
| 🟡 Sửa | 0 | — |
| 🔴 Bỏ | 0 | — |
| ⚪ Chưa build | 0 | — |
| ⏸️ Trùng, không tác động | 28 | REQ-LOGIN-01 → 28 — không REQ nào mô tả hành vi theo role |

Mã kế tiếp giữ nguyên: `REQ-LOGIN-29` · `AMB-LOGIN-19` · `RISK-LOGIN-07`.

### Test case cần xử lý

Không tác động: chưa có `docs/testcases/` và chưa có RTM, nên chưa có TC nào map vào module này.

Khi viết TC cho `LOGIN`: **không** viết case phân quyền cho Super Admin và nhân viên role khác. Ma trận phân quyền hiện còn 2 ô đã kiểm chứng và 4 ô `❔`.

### Ambiguity

| Mã | Chuyển trạng thái | Ghi chú |
|---|---|---|
| AMB-LOGIN-01 | ❓ → ✅ | Không có role Super Admin riêng. Khớp Assumption tạm "Giống Admin" |
| AMB-LOGIN-02 | ❓ → ✅ | Cùng câu trả lời: chưa có role nhân viên nào khác. Assumption tạm không còn áp dụng; chưa có TC nào dựa trên nó |
| AMB-SYS-02 | ❓ → ✅ | Danh sách role: tạm thời chỉ có admin. Chưa kiểm chứng trên UI vì `/admin/roles` bị chặn |
| AMB-SYS-01 | ❓ giữ nguyên, viết lại | Bỏ giả định "thiếu quyền Super Admin". Xem Cảnh báo |
| AMB-LOGIN-03 | ❓ giữ nguyên | Contact là tài khoản khách hàng, không phải role nhân viên, nên câu trả lời này không giải quyết |

### Thay đổi trong tài liệu

| Nơi | Thay đổi |
|---|---|
| `login/REQUIREMENTS_LOGIN_SUMMARY.md` | Ma trận phân quyền: 6 ô chuyển sang không áp dụng (đã kiểm chứng 2 · chưa rõ 4 · không áp dụng 6). AMB-LOGIN-01, 02 ✅. Thêm dòng Nhật ký |
| `README.md` | Dòng `LOGIN`: AMB treo 16 (🔴 5). Gỡ AMB-LOGIN-01, 02, AMB-SYS-02 khỏi mục 3. Viết lại AMB-SYS-01 và lý do BLOCKED của `SETTING`, `STAFF` |
| `_discovery/system_map.md` | Ma trận sơ bộ, AMB-SYS-01, AMB-SYS-02, thứ tự khảo sát, Nhật ký khám phá |
| `_discovery/modules/module_18_*.md`, `module_19_*.md` | Bỏ lý do "không phải Super Admin" |

### Cảnh báo

- ⚠️ **Câu trả lời mâu thuẫn với điều đã đo.** Tài khoản admin trong `.env` bị `Access denied` ở Settings, Staff, Roles, Activity Log và menu Setup rỗng (đo lại 02-11-2026). Nếu chỉ có role admin thì chưa giải thích được vì sao. `SETTING` và `STAFF` vẫn BLOCKED, chờ AMB-SYS-01.
- ⚠️ **Kết luận mang tính tạm thời.** Có thêm role thì phải mở lại AMB-LOGIN-01, 02 và hai cột trong ma trận phân quyền.
- ⚠️ **Chưa kiểm chứng trên UI.** Nguồn là lời user; `/admin/roles` bị chặn nên agent không tự xác nhận được.
