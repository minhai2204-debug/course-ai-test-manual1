---
name: skills-test-data-generator
description: Skill sinh test data có cấu trúc, unique, traceable cho automation tests, bao gồm positive, negative, boundary và edge cases.
---

# Test Data Generator

Purpose: Generate reliable test data for automation tests.

---

## When to Use

Use this skill when:

- Creating test data for new test cases
- Generating boundary and edge case data
- Setting up data-driven tests
- Creating API request payloads

---

## Responsibilities

Generate test data for:

- Registration forms
- Login credentials
- Form submissions
- API payloads
- Search queries
- File uploads

---

## Data Rules

All generated data must be:

- **Unique** — No duplication within test suite
- **Deterministic** — Same seed produces same data (when needed)
- **Traceable** — Can identify which test generated it

---

## Unique Data Pattern

Recommended format:

```
<prefix>_<testName>_<timestamp>
```

Examples:

```
auto_register_20260402133000
test_login_1712024100
```

---

## Common Data Types

### Email
```
auto_<testName>_<timestamp>@test.com
```
Example: `auto_register_20260402@test.com`

### Username
```
user_<testName>_<timestamp>
```
Example: `user_login_20260402133000`

### Phone
```
Random 10-digit number starting with valid prefix
```
Example: `0912345678`

### Password
```
Mix of uppercase, lowercase, digits, special chars
```
Example: `Test@12345`

---

## Data Categories

### Positive Data (Happy Path)
- Valid format, within constraints
- All required fields filled
- Standard business values

### Negative Data
- Missing required fields
- Invalid format (wrong email, short password)
- Invalid characters
- Already existing values (duplicate check)

### Boundary Values
- Minimum length (e.g., 1 character)
- Maximum length (e.g., 255 characters)
- Min + 1, Max - 1
- Empty string vs null
- Zero, negative numbers

### Edge Cases
- Unicode / special characters
- Very long strings
- SQL injection patterns (for security testing)
- HTML tags in text fields
- Leading/trailing whitespace

---

## Constraints

Test data must:

- Respect field validation rules (from DOM inspection)
- Match input format (date format, phone format)
- Avoid duplication across test runs
- Not contain real PII (personal data)

---

## Output Format

Provide data in structured format:

```json
{
  "positive": [
    { "email": "auto_tc01_20260402@test.com", "password": "Test@12345" }
  ],
  "negative": [
    { "email": "", "password": "Test@12345", "expectedError": "Email is required" },
    { "email": "invalid-email", "password": "Test@12345", "expectedError": "Invalid email format" }
  ],
  "boundary": [
    { "email": "a@b.co", "password": "12345678", "note": "Min length" }
  ]
}
```

---

## Multi-Step Data Pipeline (Cross-Module)

> Mở rộng cho bài toán: test data cần đi qua **nhiều modules nối tiếp** mới tạo ra được data hoàn chỉnh cho module cuối.

### Khi nào dùng

- Tính năng đi qua chuỗi N modules (VD: Đối tác → Thanh toán → Thuế → Biên bản)
- Data module sau **phụ thuộc** output module trước (Reference fields)
- Cần tạo data thật trên hệ thống qua browser

### Data Chain Pattern

```
Module 1 → Output: {id_1, code_1}
    ↓ (Reference)
Module 2 → Input: {id_1} → Output: {id_2}
    ↓ (Reference)
Module 3 → Input: {id_1, id_2} → Output: {id_3}
    ↓ (Reference)
Module N → Input: {id_1..id_N-1} → Output: Final Result
```

### Field Classification

| Loại field | Mô tả | Cách sinh data |
|-----------|-------|----------------|
| **Dimension field** | Giá trị thuộc chiều kết hợp trong ma trận | Lấy chính xác từ bộ combo — KHÔNG random |
| **Supporting field** | Bắt buộc nhưng không phải dimension | Random + unique + traceable |
| **Reference field** | ID/code từ output module trước | Copy từ output module trước trong chuỗi |
| **Computed field** | Tự tính từ formula/business rules | Tính theo formula — phải verify |

### Data Chain Tracing Format

```
auto_combo{XX}_{module_short}_{timestamp}
```

Ví dụ cho combo 01:
```
Module 1: partner_name  = "auto_combo01_partner_1712049200"
Module 2: payment_desc  = "auto_combo01_payment_1712049200"
Module 3: tax_note      = "auto_combo01_tax_1712049200"
→ Có thể trace: combo 01 tạo ra những data nào ở mỗi module
```

---

## Combinatorial Data Generation

> Sinh bộ data cho **ma trận kết hợp đa chiều** — mỗi bộ kết hợp = 1 bộ data hoàn chỉnh.

### Khi nào dùng

- Đã có ma trận kết hợp (từ `/generate-cross-module-test-plan`)
- Cần sinh N bộ data tương ứng N bộ kết hợp
- Mỗi bộ data phải có expected output (template, formula, computed values)

### Combinatorial Data Structure

```json
{
  "combination_id": "COMBO_01",
  "dimensions": {
    "D1": "value_from_matrix",
    "D2": "value_from_matrix"
  },
  "module_data": {
    "module_1": { "field1": "...", "field2": "..." },
    "module_2": { "ref_from_module1": "...", "field3": "..." }
  },
  "expected_output": {
    "template": "EXPECTED_TEMPLATE_CODE",
    "formula": "Amount × Rate",
    "computed_values": { "total": 110000000 }
  }
}
```

### Rules cho Combinatorial Data

| # | Rule |
|---|------|
| 1 | Dimension values PHẢI đúng 100% so với ma trận — KHÔNG random |
| 2 | Mỗi combo dùng data riêng (unique per combo) |
| 3 | Computed values phải đúng theo formula |
| 4 | Mỗi combo PHẢI có expected output |
| 5 | Traceable: format `auto_combo{XX}_{module_short}_{timestamp}` (xem *Data Chain Tracing Format* ở trên) |

### Workflow tham chiếu

- `/generate-cross-module-test-plan` → Sinh ma trận kết hợp (input cho skill này)
- `/generate-combinatorial-test-data` → Workflow chính dùng skill này cho combinatorial data

---

## Bộ Dữ Liệu Đối Soát CSDL (tìm kiếm · báo cáo · dashboard)

Dùng cho nhóm **D9** (tìm kiếm) và **D10** (báo cáo / dashboard) của Bảng kiểm CSDL (`skills-rbt-manual-testing`). Mục tiêu: một tập bản ghi **nhỏ, có chủ đích**, mà kết quả đúng tính được **trước** khi chạy — không phụ thuộc dữ liệu thật đang có trên môi trường dùng chung.

**Quy tắc:**

| Quy tắc | Lý do |
|---|---|
| Mọi bản ghi mang **mã lượt chạy chung** `auto_<module>_<run>` ở trường tìm được (tên, mã, ghi chú) — VD `auto_cust_1731650000_hn_dau` | Câu SQL loại B thu hẹp bằng `LIKE 'auto_<module>_<run>%'` (khớp đầu chuỗi, dùng chỉ mục) — chỉ đúng bộ của lượt này, không lẫn lượt khác |
| Tạo **qua UI / API**, không bao giờ `INSERT` vào CSDL | `database_rules.md` — CSDL chỉ để đọc; tạo qua UI cũng là kiểm luôn đường tạo |
| Mỗi bản ghi đi kèm **lý do có mặt** (nó thử điều gì) | Bộ dữ liệu không có lý do sẽ phình ra mà không phủ thêm trường hợp nào |
| Có **bảng giá trị kỳ vọng** tính từ Định nghĩa chỉ số `MET-…` / Ánh xạ tìm kiếm — trước khi chạy | Kỳ vọng tính sau khi thấy kết quả là chép kết quả, không phải kiểm |
| Có **kế hoạch dọn qua UI** (xoá theo mã lượt chạy) và ghi vào mục *Dữ liệu đã tạo & dọn dẹp* của report | Môi trường dùng chung — bản ghi test còn sót làm lệch báo cáo của người khác |

**Bộ tối thiểu cho tìm kiếm (D9)** — mỗi dòng một bản ghi, thêm bớt theo Ánh xạ tìm kiếm của module:

| # | Bản ghi (trường tìm) | Thử điều gì | Kỳ vọng khi tìm `Hà Nội` |
|---|---|---|---|
| S1 | `auto_cust_<run>_s1 Hà Nội` | Khớp có dấu | Có |
| S2 | `auto_cust_<run>_s2 HÀ NỘI` | Hoa thường | Có (nếu không phân biệt) |
| S3 | `auto_cust_<run>_s3 Ha Noi` | Không dấu | Theo Ánh xạ: có / không |
| S4 | `auto_cust_<run>_s4 Hà Nam` | Gần giống, không khớp | Không |
| S5 | `auto_cust_<run>_s5 100%_off` | Ký tự đại diện `%` `_` được tìm như chữ | Tìm `100%` chỉ ra S5 |
| S6 | `auto_cust_<run>_s6 Hà Nội` rồi **xoá** qua UI | Xoá mềm không hiện | Không |
| S7 | ≥ (kích thước trang + 1) bản ghi `auto_cust_<run>_p<nn>` | Phân trang: trùng / sót giữa hai trang | Cộng các trang = `COUNT` |

**Bộ tối thiểu cho báo cáo (D10)** — giá trị chọn để **mỗi** điều kiện của định nghĩa làm số thay đổi một lượng khác nhau, nhìn chênh lệch là biết điều kiện nào sai:

| # | Bản ghi | Giá trị | Thử điều gì | Có được tính? (theo `MET-…`) |
|---|---|---|---|---|
| R1 | Hoá đơn `auto_inv_<run>_r1`, **Đã thanh toán**, ngày thanh toán giữa kỳ | `1.000.000` | Trường hợp chuẩn | Có |
| R2 | Như R1, ngày thanh toán **00:00:00** ngày đầu kỳ | `20.000` | Biên dưới của kỳ | Có |
| R3 | Như R1, ngày thanh toán **23:59:59** ngày cuối kỳ | `300` | Biên trên của kỳ | Có |
| R4 | Như R1, ngày thanh toán **00:00:00** ngày đầu kỳ **sau** | `4` | Ngoài biên trên | Không |
| R5 | Hoá đơn **Nháp** / **Huỷ** | `50.000` | Trạng thái bị loại | Không |
| R6 | Như R1 rồi **xoá** qua UI | `600.000` | Xoá mềm bị loại | Không |
| | | | **Kỳ vọng chênh lệch** | **+1.020.304** — mỗi chữ số ứng với một bản ghi, lệch chữ số nào là biết bản ghi nào bị tính sai |

> Giá trị **khác bậc** nhau (1.000.000 · 20.000 · 300 · 4) là cố ý — tổng sai một lượng là đọc ra ngay bản ghi gây lệch. Múi giờ của biên kỳ lấy theo định nghĩa chỉ số; định nghĩa chưa nói múi giờ → AMB, không tự chọn.

## Rules References

- `.claude/rules/automation_rules.md` — Test data generation rules (Section 2)
- `.claude/rules/database_rules.md` — CSDL chỉ đọc · 3 loại truy vấn · trước–sau · nguồn công thức (mục 2–2c)