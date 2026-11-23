---
name: moi-truong-crm-dung-chung
description: Môi trường Perfex CRM demo dùng chung — được làm gì với dữ liệu, tài khoản nào có/chưa có, bản ghi test còn sót
type: project
cập nhật: 18-11-2026
---

# Môi trường CRM dùng chung

Nguồn chính thức: dòng *Môi trường* và *Năng lực kiểm thử của QA* trong [`docs/requirements/README.md`](../../docs/requirements/README.md). File này chỉ giữ phần **không** ghi ở đó hoặc dễ bị quên.

## Tài khoản

- `.env` có đúng 3 biến: `URL` · `EMAIL_ADMIN` · `PASSWORD_ADMIN`. Chỉ đọc để dùng — **không** chép giá trị vào `docs/`, `memories/`, log.
- Tài khoản admin `.env` **bị chặn** ở Setup, Staff/Roles, Activity log (AMB-SYS-01). Tạm thời hệ thống chỉ có role admin (AMB-LOGIN-01, 05-11-2026).
- **Chưa có** (chặn chạy TC): 2 tài khoản Project Manager cho TC khoá tài khoản (`EMAIL_PM_1/2` — đề xuất, chưa có trong `.env`) · tài khoản test `TK-TEST-01/02a/02b/03` · Contact test · hộp thư test · tài khoản role khác cho phân quyền CUST (AMB-CUST-08) · biến `DB_*`.
- Ảnh evidence từng lộ email đăng nhập admin (ảnh `prof_overview`) → mọi ảnh có khối thông tin tài khoản phải che/không chụp.

## Được làm gì với dữ liệu

| Ngày | User cho phép |
|---|---|
| 02-11-2026 | Khảo sát chỉ đọc |
| 05-11-2026 | Tạo dữ liệu thử ngay trên môi trường này (AMB-SYS-03), đặt tên nhận diện được |
| 16-11-2026 | Với bản ghi **do chính agent tạo** (`auto_cust_<timestamp>`): **tạo + sửa + xoá**. Bản ghi có sẵn của người khác: không sửa / xoá |

⚠️ README requirements vẫn ghi "không sửa / xoá" theo mốc 05-11 — câu trả lời 16-11 chỉ nới cho **bản ghi của mình**.

## Rủi ro đã biết

- **Khoá tài khoản dùng chung:** đăng nhập sai nhiều lần có thể khoá email. Email sai dùng đuôi `@example.invalid` dạng `auto_<test>_<timestamp>_<random>@example.invalid`, mỗi TC một email riêng; TC khoá tài khoản chạy **tuần tự**, không song song (RISK-LOGIN-01).
- Thao tác **xoá khách hàng bị bộ kiểm duyệt an toàn của phiên chặn** (16-11-2026) — không lách. Còn sót trên môi trường, user bảo *"Cứ để lại"*:
  - `auto_cust_20261116141157` (id 16007) + 1 contact + 1 reminder
  - `auto_cust_import_20261116141157` (id 16008) + 1 contact
- **18-11-2026** còn sót task `QA-LOGIN-TC034-TIMER` (id 2193) + 1 bản ghi thời gian ≈ 2 phút (timer **đã dừng**) — xoá qua pane không được (hộp xác nhận gốc). Chưa hỏi user xoá tay hay để lại.
- **Từ sau 10-11-2026 giao diện admin của tài khoản `.env` là Tiếng Việt** (`Bảng tin`, `Khách hàng`) — ai đó trên môi trường dùng chung đã đổi. User chốt 18-11: chấm nhãn tiếng Việt theo nghĩa tương đương; **không** tự đổi ngôn ngữ tài khoản. Trang Login / Forgot Password vẫn tiếng Anh.
- Có dữ liệu người khác tạo (~2.800 khách hàng, bộ lọc `auto_filter_tc029_*`) → số liệu Dashboard/Reports luôn trôi; không so giá trị tuyệt đối.
- Subscriptions tích hợp Stripe → dừng hỏi trước khi tạo gì có thể gọi sang Stripe.

Liên quan: [[trinh-duyet-va-dang-nhap]] · [[kiem-thu-csdl]]
