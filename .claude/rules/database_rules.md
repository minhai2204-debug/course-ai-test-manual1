# Quy Tắc Kiểm Chứng Dữ Liệu Trong CSDL (Database — CHỈ ĐỌC)

> Áp dụng cho **mọi** tác vụ đụng tới cơ sở dữ liệu — khảo sát schema, viết manual TC `@DBCheck`, chạy TC, sinh automation, review.
>
> Công cụ chạy truy vấn: [`scripts/db-check/`](../../scripts/db-check/README.md) · cách viết TC: skill [`skills-rbt-manual-testing`](../skills/skills-rbt-manual-testing/SKILL.md) mục *Quy Tắc Ngôn Ngữ Kiểm Chứng* mục 3b (khối `🗄️` + tag `@DBCheck`, `Auto Type` = `UI+DB` / `API+DB`) và Bảng kiểm CSDL của nhánh V3 `Database` · ánh xạ field ↔ cột: skill [`skills-requirements-analyzer`](../skills/skills-requirements-analyzer/SKILL.md) mục 6.3.1.

---

## 1. Nguyên tắc gốc — CSDL chỉ để ĐỌC

QA được phép truy cập CSDL **chỉ để kiểm chứng** dữ liệu mà thao tác trên UI / API sinh ra. Mọi thay đổi dữ liệu đi qua **ứng dụng**, không bao giờ đi thẳng vào CSDL.

| ✅ Được phép | ❌ NGHIÊM CẤM |
|---|---|
| `SELECT …` (theo đúng 1 trong 3 loại ở mục 2) | `INSERT` · `UPDATE` · `DELETE` · `MERGE` · `REPLACE` · `UPSERT` |
| `WITH … SELECT …` (CTE chỉ đọc) | DDL: `CREATE` · `ALTER` · `DROP` · `TRUNCATE` · `RENAME` · `COMMENT` |
| `SELECT` trên `information_schema` / catalog để khảo sát schema | `GRANT` · `REVOKE` · `SET` · `USE` · `LOCK` · `UNLOCK` · `KILL` · `LOAD` · `COPY` |
| | Gọi thủ tục / hàm: `CALL` · `EXEC` · `EXECUTE` · `DO` — kể cả khi tên nghe như chỉ đọc |
| | Câu **trông như đọc mà ghi hoặc khoá**: `SELECT … INTO` · `SELECT … FOR UPDATE` / `FOR SHARE` · `LOCK IN SHARE MODE` · `INTO OUTFILE` / `DUMPFILE` · hàm có tác dụng phụ (`sleep`, `pg_sleep`, `nextval`, `setval`, `pg_terminate_backend`, `lo_import`…) |
| | Nhiều câu lệnh trong một lần chạy (`SELECT …; DELETE …`) |

> 🔒 **Phòng hai lớp.** Luật này và chốt chặn của `scripts/db-check/` là lớp **thứ hai**. Lớp thứ nhất phải là **tài khoản CSDL chỉ có quyền đọc** do DBA cấp. Tài khoản đang dùng có quyền ghi → ghi rõ ở dòng *Năng lực kiểm thử của QA* trong `docs/requirements/README.md` và đề nghị DBA cấp tài khoản read-only — luật trong skill không chặn được người gõ tay ngoài công cụ.

---

## 2. Ba loại truy vấn kiểm chứng — ghi loại ở đầu khối `🗄️`

Mỗi câu `SELECT` thuộc **đúng một** loại. Loại quyết định phạm vi được đọc và cách so kết quả:

| Loại | Dùng cho | Phạm vi được đọc | Cách so | Cờ `db_check.py` |
|---|---|---|---|---|
| **A · Bản ghi** | Thêm · sửa · xoá · trạng thái ẩn | **Chỉ** bản ghi do test tạo (`auto_<test>_<timestamp>…`) hoặc mã bản ghi đọc trên UI | Từng cột với giá trị kỳ vọng · trước/sau (`--snapshot` / `--diff`) | `--mode record` (mặc định) |
| **B · Tập kết quả** | Tìm kiếm · lọc · sắp xếp · phân trang · danh sách | Cùng điều kiện với UI, **thu hẹp trong bộ dữ liệu test** của lượt chạy (`LIKE 'auto_<run>%'` — khớp đầu chuỗi, dùng được chỉ mục) | **Tập mã bản ghi** UI = tập mã CSDL · nhãn tổng số = `COUNT` · thứ tự = `ORDER BY` | `--mode set` |
| **C · Tổng hợp** | Báo cáo · dashboard · ô tổng số · biểu đồ | **Được** đọc dữ liệu nghiệp vụ thật (user cho phép 15-11-2026) — nhưng **chỉ trả về số tổng hợp** | **Nhất quán**: số UI = số SQL đọc cùng thời điểm · **Chênh lệch**: sau − trước = giá trị của bản ghi test | `--mode aggregate` |

**Luật riêng của loại C** — nới phạm vi đọc thì phải siết thứ được trả về:

| Quy tắc | Lý do |
|---|---|
| Mọi cột trong `SELECT` là **hàm tổng hợp** (`COUNT` · `SUM` · `AVG` · `MIN` · `MAX`) hoặc **cột của `GROUP BY`** — không có dòng thô | Đọc toàn bảng mà trả về dòng thô là kéo dữ liệu khách hàng ra report |
| Cột `GROUP BY` **không** là cột cá nhân (tên, email, điện thoại, địa chỉ) — chỉ là trạng thái, loại, kỳ, mã danh mục | Nhóm theo email = liệt kê email |
| Tối đa **50 nhóm** | Báo cáo hơn 50 dòng → thu hẹp kỳ hoặc bộ lọc, không kéo nguyên bảng |
| Bắt buộc lọc **kỳ thời gian** và/hoặc **trạng thái** đúng như bộ lọc trên UI | Không lọc kỳ là quét toàn bảng lịch sử — chậm, và không so được với màn hình |
| Câu SQL dựng từ **Định nghĩa chỉ số** (mục 2c), ghi mã định nghĩa ở dòng đầu khối `🗄️` | Xem mục 2c |

### 2b. Kiểm trên môi trường dùng chung — số tổng nhảy liên tục

Người khác thao tác cùng lúc làm số tổng thay đổi giữa hai lần đọc. Báo cáo / dashboard kiểm bằng **cả hai** cách:

| Cách | Làm gì | Chứng minh |
|---|---|---|
| **Nhất quán** | Đọc số trên UI rồi chạy SQL loại C **ngay sau đó** (≤ 1 phút), cùng bộ lọc kỳ / trạng thái | Màn hình tính đúng trên dữ liệu đang có |
| **Chênh lệch** | Đo UI + SQL (trước) → tạo / sửa / xoá bản ghi `auto_…` có giá trị **đã biết** qua UI → đo lại (sau). Kỳ vọng: `sau − trước = giá trị đã biết` ở **cả** UI lẫn SQL | Báo cáo **có tính** (hoặc **đã loại**) đúng bản ghi — điều mà "khớp số" không chứng minh được |

- Lệch mà SQL đọc liền sau cũng lệch theo cùng mức → người khác chen vào giữa: **chạy lại tối đa 2 lần**, ghi số lần chạy lại vào report. Lệch cả 3 lần → FAIL
- Dashboard cập nhật **định kỳ** (job nền, bộ nhớ đệm) → đọc độ trễ ở Định nghĩa chỉ số, chờ bằng **hỏi lại có giới hạn** (mỗi 5–10 giây, tối đa = độ trễ + 1 phút), **không** sleep cứng

### 2c. Nguồn công thức — tài liệu phân tích yêu cầu, KHÔNG phải mã nguồn app

Câu SQL kiểm báo cáo là một **cách tính thứ hai, độc lập** để đối chiếu với app. Chép lại logic của app (đọc mã nguồn, đọc câu SQL app chạy qua network/log) thì SQL sai y như app và TC vẫn PASS.

- Công thức lấy từ **tài liệu phân tích yêu cầu** (SRS → `/analyze-requirement-document` → mục *Định nghĩa chỉ số*; tài liệu requirements module mục 6.3.3 — skill `skills-requirements-analyzer`). Mỗi chỉ số có mã `MET-<MODULE>-<nn>`
- Tài liệu chưa định nghĩa đủ (thiếu trạng thái được tính, kỳ, làm tròn…) → mở `AMB-<MODULE>-<nn>` và gắn `@NeedsVerify` cho TC. **Không** tự suy công thức từ UI, từ mã nguồn, hay từ chính câu SQL app chạy
- Số UI ≠ số SQL dựng theo định nghĩa → **FAIL có căn cứ**, ghi cả hai số + mã `MET-…`. Không sửa SQL cho khớp app

### 2d. Luật phạm vi chung — mọi loại

| Quy tắc | Lý do |
|---|---|
| **Bắt buộc có `WHERE`** — loại A, B lọc theo **dữ liệu do chính test tạo ra** (`auto_<test>_<timestamp>…`) hoặc mã bản ghi đọc trên UI; loại C lọc theo kỳ / trạng thái (mục 2) | Môi trường dùng chung chứa dữ liệu thật của người khác. Không lọc là kéo cả bảng về, vừa chậm vừa lộ dữ liệu |
| **Bắt buộc giới hạn số dòng** — `LIMIT n` (MySQL/PostgreSQL) · `TOP n` / `FETCH FIRST n ROWS ONLY` (SQL Server/Oracle). Mặc định `n ≤ 50` | Câu lọc sai điều kiện vẫn không kéo cả bảng. `db-check` tự chặn ở `--max-rows` dù câu quên giới hạn |
| **KHÔNG `SELECT *`** — liệt kê đúng cột cần kiểm | `*` kéo theo cột mật khẩu băm, token, dữ liệu cá nhân không liên quan tới Expected |
| **KHÔNG** quét bảng lớn không có chỉ mục (`LIKE '%…'` trên bảng triệu dòng, `JOIN` không điều kiện) | Truy vấn nặng trên CSDL dùng chung làm chậm cả hệ thống — đó cũng là sự cố |
| Timeout mỗi câu **≤ 30 giây** | Câu chạy lâu hơn là câu sai phạm vi |
| Tên bảng / cột **lấy từ schema thật** (`information_schema`), ghi ở mục *Ánh xạ dữ liệu* của tài liệu requirements module — **không đoán** | Cùng tinh thần *"không đoán locator"*: tên cột đoán sai là TC FAIL giả |

---

## 3. Kết nối & bí mật

- Thông tin kết nối sống ở **`.env`** (đã `.gitignore`): `DB_ENGINE` (`mysql` · `postgres` · `mssql`) · `DB_HOST` · `DB_PORT` · `DB_NAME` · `DB_USER` · `DB_PASSWORD`
- **KHÔNG** ghi host, tài khoản, mật khẩu, chuỗi kết nối vào `docs/`, vào TC, vào report, vào log
- `.env` chưa có biến `DB_*` → agent **không** tự chạy truy vấn: TC `@DBCheck` vẫn sinh được (khối 🗄️ là câu SELECT để tester tự chạy bằng công cụ của họ); khi thực thi, TC chấm `BLOCKED` theo dòng `@DBCheck` ở bảng *TC đặc biệt* của `skills-manual-test-executor`

---

## 4. Dữ liệu cá nhân & bí mật trong kết quả

| Loại cột | Ghi vào evidence / report / Allure |
|---|---|
| Mật khẩu băm, token, khoá API, session, OTP | **Chỉ hình thái**: `<bcrypt $2y$, 60 ký tự>`, `<32 ký tự hex>` — **không** chép giá trị |
| Email, số điện thoại, tên, địa chỉ **của người khác** | Che (`db-check --mask` mặc định bật cho cột khớp mẫu `password|pass|hash|token|secret|key|email|phone|mobile|address`) |
| Dữ liệu do test tự sinh (`auto_…@auto.test`) | Không cần che |

> Kiểm "mật khẩu được băm, không lưu bản rõ" → Expected kiểm **hình thái** (`bắt đầu bằng $2y$`, `dài 60`, `khác chuỗi mật khẩu đã nhập`). **Không** bao giờ in giá trị băm ra report.

---

## 5. Kiểm chứng — viết Expected cho DB

- Kiểm **từng cột** với giá trị kỳ vọng cụ thể — không viết *"dữ liệu lưu đúng"*
- **Sửa** → chụp bản ghi **trước và sau** (`db_check.py --snapshot` rồi `--diff`): kỳ vọng ghi rõ cột **phải đổi** và khẳng định **mọi cột khác giữ nguyên**. Chỉ kiểm cột được sửa là bỏ lọt lỗi ghi đè nhầm cột khác
- **Xoá** → ngoài bản ghi chính, kiểm bản ghi con / liên kết, và bản ghi đã xoá **không còn** trong kết quả tìm kiếm (loại B) lẫn số báo cáo (loại C, cách chênh lệch)
- **Tìm kiếm** → so **tập mã bản ghi**, không so chuỗi hiển thị; tổng số trên nhãn = `COUNT`; cộng mọi trang = `COUNT`, không trùng, không sót
- Giá trị **sinh theo phiên** (`id` tự tăng, `created_at`) → kiểm **khuôn / khoảng**: `created_at` nằm trong ±2 phút quanh thời điểm bấm Lưu, theo **múi giờ của CSDL** (ghi rõ múi giờ đã chốt khi khảo sát)
- Kiểm **phủ định** bằng đếm: *"không có bản ghi rác"* → `SELECT COUNT(*) … WHERE <khoá test>` = `0`
- Ghi xuống CSDL có độ trễ (hàng đợi, job nền) → **chờ bằng polling có giới hạn** (`expect.poll`, Awaitility, lặp truy vấn mỗi 1 s tối đa N lần) — **không** sleep cứng
- Kết quả DB lệch với UI → ghi **cả hai** vào report; không tự kết luận bên nào đúng khi requirements chưa nói

---

## 6. NGHIÊM CẤM

- ❌ Chạy bất kỳ câu nào ngoài `SELECT` / `WITH … SELECT` — kể cả để "dọn dữ liệu test", "đặt lại trạng thái khoá tài khoản", "tạo dữ liệu nhanh". Cần đổi trạng thái → làm qua UI / API, hoặc nhờ Dev/DBA
- ❌ Dùng CSDL để **tạo điều kiện tiên quyết** cho TC (chèn bản ghi, sửa cờ) — TC phải đi qua đúng luồng người dùng
- ❌ `SELECT *` · câu không có `WHERE` · câu không giới hạn số dòng trên bảng nghiệp vụ
- ❌ Chạy truy vấn bằng client tự viết / gõ thẳng vào driver mà bỏ qua chốt chặn của `scripts/db-check/` (automation dùng `DbClient` có cùng chốt chặn — `CODE_TEMPLATES.md` § 10)
- ❌ Chép chuỗi kết nối, mật khẩu CSDL, giá trị cột bí mật vào `docs/`, TC, report, Allure
- ❌ Đoán tên bảng / cột — chưa khảo sát schema thì TC dùng placeholder `<bảng>.<cột>` và gắn `@NeedsVerify`
- ❌ Hạ assertion DB cho khớp hành vi thật khi thấy lệch — lệch là kết quả kiểm thử, ghi lại
- ❌ Truy vấn loại C trả về dòng thô, nhóm theo cột cá nhân, hoặc không lọc kỳ / trạng thái
- ❌ Dựng công thức báo cáo từ mã nguồn app, từ câu SQL app chạy, hay sửa SQL cho khớp số app — công thức chỉ lấy từ Định nghĩa chỉ số (`MET-…`) của tài liệu phân tích yêu cầu (mục 2c)
- ❌ Kết luận FAIL báo cáo khi chỉ đo một lần trên môi trường dùng chung — chạy lại theo mục 2b trước
