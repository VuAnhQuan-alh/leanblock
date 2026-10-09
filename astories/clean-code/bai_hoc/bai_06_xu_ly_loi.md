# Bài 6 — Xử lý lỗi: tách lỗi khỏi logic, và đừng trả null

> [!info] Về bài này
> Dựng từ **Chương 7 — "Error Handling"** (tác giả Michael Feathers) của *Clean Code* (Robert C. Martin, 2008 — `tai_lieu/`, `tr. 103–112`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 31`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Mạch bài: *lỗi che khuất logic → gọi tên vấn đề → bản sạch (TypeScript, chạy được) → nguyên tắc → đối chiếu 2026 → áp dụng*.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: khi xử lý lỗi nuốt chửng logic](#1-mở-đầu-khi-xử-lý-lỗi-nuốt-chửng-logic)
2. [Dùng exception thay vì mã lỗi](#2-dùng-exception-thay-vì-mã-lỗi)
3. [Viết try-catch-finally trước, cung cấp bối cảnh](#3-viết-try-catch-finally-trước-cung-cấp-bối-cảnh)
4. [Bọc API bên thứ ba, định nghĩa luồng bình thường](#4-bọc-api-bên-thứ-ba-định-nghĩa-luồng-bình-thường)
5. [Code minh hoạ: đừng trả null](#5-code-minh-hoạ-đừng-trả-null)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào codebase của bạn](#7-áp-dụng-vào-codebase-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mở đầu: khi xử lý lỗi nuốt chửng logic

Việc xử lý lỗi nghe có vẻ lạc đề trong một cuốn về code sạch, nhưng mối liên hệ rất rõ: nhiều codebase bị xử-lý-lỗi **thống trị** tới mức không còn nhìn ra code *thật sự làm gì* giữa rừng `if`-kiểm-lỗi rải khắp nơi.

> [!quote] Ch. 7 — Error Handling (tr. 103)
> "Error handling is important, but if it obscures logic, it's wrong."
>
> *Xử lý lỗi là quan trọng, nhưng nếu nó che khuất logic, thì nó sai.*

Cả chương là các kỹ thuật để viết code **vừa sạch vừa bền** — xử lý lỗi một cách duyên dáng mà không bôi bẩn luồng chính.

## 2. Dùng exception thay vì mã lỗi

Ví dụ `DeviceController` dùng mã lỗi: mỗi lời gọi kéo theo một `if` kiểm lỗi ngay sau, lồng nhau nhiều tầng, logic tắt nghẽn. Dễ quên kiểm, và caller bị bôi bẩn.

> [!quote] Ch. 7 — Use Exceptions Rather Than Return Codes (tr. 104)
> "it is better to throw an exception when you encounter an error. The calling code is cleaner. Its logic is not obscured by error handling."
>
> *tốt hơn là ném exception khi gặp lỗi. Code gọi sẽ sạch hơn. Logic của nó không bị xử-lý-lỗi che khuất.*

Tách `sendShutDown()` thành `try { tryToShutDown() } catch {...}` — hai mối bận tâm (thuật toán tắt máy và xử lý lỗi) vốn quấn vào nhau, giờ **tách ra**, hiểu độc lập từng cái.

## 3. Viết try-catch-finally trước, cung cấp bối cảnh

Exception định nghĩa một **phạm vi** trong chương trình: khối `try` giống một *transaction* — `catch` phải để chương trình ở trạng thái nhất quán bất kể trong `try` có gì hỏng. Vì vậy, khi viết code có thể ném exception, hãy **bắt đầu bằng khung try-catch-finally**, dùng TDD: viết test ép ra exception trước, rồi mới xây hành vi của handler để thoả test — cách này dựng phạm vi transaction của `try` trước (nối sang [Bài 8 (Unit test)](bai_08_unit_test.md)).

Mỗi exception ném ra cũng phải **cung cấp đủ bối cảnh** để truy ra nguồn và vị trí lỗi: stack trace cho biết *ở đâu* nhưng không cho biết *ý định* của thao tác đã hỏng — nên hãy kèm thông điệp nói rõ thao tác nào thất bại và kiểu thất bại gì.

## 4. Bọc API bên thứ ba, định nghĩa luồng bình thường

Khi một API bên thứ ba ném cả tá kiểu exception, đừng bắt từng kiểu (sinh trùng lặp). Hãy **bọc** nó trong một lớp của bạn, dịch mọi exception về *một* kiểu chung:

> [!quote] Ch. 7 — Define Exception Classes in Terms of a Caller's Needs (tr. 109)
> "wrapping third-party APIs is a best practice. When you wrap a third-party API, you minimize your dependencies upon it."
>
> *bọc các API bên thứ ba là một thực hành tốt. Khi bọc, bạn giảm thiểu phụ thuộc vào nó.*

(Chủ đề này nối thẳng sang [Bài 7 (Ranh giới)](bai_07_ranh_gioi.md).) Và khi một "ngoại lệ" thực ra là chuyện *bình thường*, đừng dùng exception — hãy dùng **Special Case Pattern**: tạo một object xử lý sẵn ca đặc biệt, để code gọi không phải bận tâm. Ví dụ: thay vì `catch(MealExpensesNotFound)` rồi cộng per-diem, hãy để DAO luôn trả về một `MealExpenses` mà khi không có hoá đơn thì `getTotal()` trả thẳng per-diem.

## 5. Code minh hoạ: đừng trả null

Thứ "mời gọi lỗi" đứng đầu danh sách là **trả về null**.

> [!quote] Ch. 7 — Don't Return Null (tr. 110)
> "When we return null, we are essentially creating work for ourselves and foisting problems upon our callers. All it takes is one missing null check to send an application spinning out of control."
>
> *Khi trả về null, ta đang tự tạo việc cho mình và trút rắc rối lên đầu caller. Chỉ cần sót một lần kiểm null là cả ứng dụng mất kiểm soát.*

Nghịch lý Feathers chỉ ra: vấn đề của code đầy `if (x != null)` không phải *thiếu* một lần kiểm null, mà là *có quá nhiều*. Lời giải thường chỉ là trả về một **Special Case** — như danh sách rỗng:

```typescript
import { strict as assert } from "node:assert";

type Employee = { name: string; pay: number };

// ===== Bản bẩn: getEmployees có thể trả null → caller phải canh null =====
function getEmployeesNullable(hasData: boolean): Employee[] | null {
  if (!hasData) return null;
  return [{ name: "An", pay: 100 }, { name: "Binh", pay: 200 }];
}
function totalPayDirty(hasData: boolean): number {
  let total = 0;
  const employees = getEmployeesNullable(hasData);
  if (employees !== null) {
    // null-check lẫn vào giữa logic
    for (const e of employees) total += e.pay;
  }
  return total;
}

// ===== Bản sạch: luôn trả về danh sách (rỗng khi không có dữ liệu) =====
function getEmployees(hasData: boolean): Employee[] {
  if (!hasData) return []; // special case: danh sách rỗng
  return [{ name: "An", pay: 100 }, { name: "Binh", pay: 200 }];
}
function totalPayClean(hasData: boolean): number {
  let total = 0;
  for (const e of getEmployees(hasData)) total += e.pay; // không còn null-check
  return total;
}

for (const hasData of [true, false]) {
  assert.equal(totalPayDirty(hasData), totalPayClean(hasData));
  console.log(`hasData=${hasData}: bẩn=${totalPayDirty(hasData)}  sạch=${totalPayClean(hasData)}`);
}
console.log("trả danh sách rỗng thay vì null → caller sạch, hết canh null.");
```

Kết quả chạy thật:

```
hasData=true: bẩn=300  sạch=300
hasData=false: bẩn=0  sạch=0
trả danh sách rỗng thay vì null → caller sạch, hết canh null.
```

Và nếu trả null đã tệ, thì **truyền null vào** còn tệ hơn:

> [!quote] Ch. 7 — Don't Pass Null (tr. 111)
> "Returning null from methods is bad, but passing null into methods is worse."
>
> *Trả null từ method thì tệ, nhưng truyền null **vào** method còn tệ hơn.*

Vì gần như không ngôn ngữ nào xử lý đẹp được một `null` bị truyền nhầm; cách hợp lý là **cấm truyền null theo mặc định** — khi đó một `null` trong danh sách tham số nghiễm nhiên là dấu hiệu của lỗi.

> [!note] Tự thử
> 1. Bỏ dòng `if (employees !== null)` ở bản bẩn (giữ `getEmployeesNullable`) rồi chạy với `hasData=false`. Lỗi gì xảy ra? Đó chính là `NullPointerException` mà sách cảnh báo.
> 2. Đổi kiểu trả về bản bẩn thành `Employee[]` (bỏ `| null`) nhưng vẫn `return null`. TypeScript (với `strictNullChecks`) báo gì *trước khi* chạy?
> 3. Viết thêm một hàm trả về `Map` rỗng thay vì null cho một tra cứu. Caller gọn hơn bao nhiêu?

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Chương này **già đi rất tốt về nguyên tắc**, nhưng công cụ 2026 đã cho những lời giải mạnh hơn hẳn 2008.
> - **"Don't return null" → hệ kiểu lo giúp.** Năm 2008, trả null là lỗi *lúc chạy*. Năm 2026, TypeScript với `strictNullChecks` biến `null`/`undefined` thành thứ **compiler bắt được lúc biên dịch**: `Employee[] | null` buộc caller xử lý, còn `Employee[]` thì cấm null ngay từ kiểu. Kotlin (`?`), Swift (`Optional`), Rust (`Option`) đều đi theo hướng này. Lời khuyên của Feathers giờ được *ngôn ngữ* cưỡng chế.
> - **Exception vs mã lỗi — có lựa chọn thứ ba.** Năm 2026 nhiều nơi quay lại "lỗi là giá trị": kiểu `Result<T, E>` / `Either` (Rust, Go trả `(value, err)`, thư viện TS `neverthrow`). Ưu điểm: lỗi hiện **tường minh trong chữ ký hàm** (không "ném xuyên" vô hình), buộc caller xử lý. Đây là sự tổng hợp: giữ cái "tách lỗi khỏi logic" của exception, cộng cái "lỗi là một phần của kiểu" của mã lỗi. Nối với kiểu `Result` ở [Bài 2 (Hàm)](bai_02_ham.md).
> - **Checked exceptions** (tr. 107): Feathers tuyên bố "cuộc tranh luận đã khép" — và 2026 đồng ý, checked exception của Java bị xem là sai lầm thiết kế (phá OCP, phá đóng gói). Gần như không ngôn ngữ mới nào copy nó.
> - **Special Case Pattern & bọc API** (tr. 109): còn nguyên giá trị, là nền cho [Bài 7](bai_07_ranh_gioi.md).
> - **Vẫn vàng**: tách xử-lý-lỗi khỏi luồng chính, cung cấp bối cảnh cho lỗi, và "xử lý lỗi che khuất logic là sai".

## 7. Áp dụng vào codebase của bạn

> [!question] Áp dụng vào codebase của bạn
> 1. **Bật `strictNullChecks`** (hoặc tương đương trong ngôn ngữ của bạn) nếu chưa. Đếm số lỗi nó phát hiện — mỗi lỗi là một `NullPointerException` tiềm tàng mà sách 2008 phải bắt bằng tay.
> 2. **Săn hàm trả null.** Tìm một hàm trả `T | null`/`T | undefined`. Nó có thể trả Special Case (danh sách rỗng, object mặc định) thay thế không?
> 3. **Đếm null-check.** Tìm khối code nhiều `if (x != null)` lồng nhau. Theo Feathers, vấn đề là *quá nhiều* null, không phải *thiếu một*. Refactor nguồn trả null.
> 4. **Cân nhắc Result.** Với một luồng mà lỗi là chuyện *bình thường* (parse input, gọi mạng), thử một kiểu `Result<T, E>` thay vì ném exception. Chữ ký hàm có trung thực hơn không?

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Exception vs error code** | Ném exception tách xử-lý-lỗi khỏi luồng chính, không bắt caller kiểm ngay (tr. 104). |
| **Try-as-transaction** | Khối `try` như một transaction; `catch` phải để trạng thái nhất quán (tr. 105). |
| **Checked exception** | Exception khai trong chữ ký; phá OCP + đóng gói — "cuộc tranh luận đã khép" (tr. 107). |
| **Wrapping third-party API** | Bọc API ngoài để giảm phụ thuộc, dịch về một kiểu exception chung (tr. 108–109). |
| **Special Case Pattern** | Object xử lý sẵn ca đặc biệt, để code gọi khỏi phải rẽ nhánh (tr. 109). |
| **Don't return/pass null** | Trả null tệ, truyền null tệ hơn; cấm null theo mặc định (tr. 110–112). |
| **Result / Option** | (2026) Lỗi là giá trị tường minh trong kiểu; thay cho exception/mã lỗi. |

## 9. Câu hỏi tự kiểm tra

1. Vì sao exception sạch hơn mã lỗi? Hai mối bận tâm nào được tách ra? *(tr. 104)*
2. Vì sao nên viết khung try-catch-finally *trước*? Khối try giống cái gì? *(tr. 105)*
3. "Vấn đề không phải thiếu một null-check, mà là có quá nhiều" nghĩa là gì? *(tr. 110)*
4. Special Case Pattern giải quyết tình huống nào mà exception làm rối? *(tr. 109)*
5. Năm 2026, công cụ/kiểu nào đã cưỡng chế "đừng trả null" và cho lựa chọn thứ ba ngoài exception/mã lỗi?

## Tóm tắt một trang

```
BÀI 6 — XỬ LÝ LỖI: TÁCH LỖI KHỎI LOGIC, ĐỪNG TRẢ NULL
─────────────────────────────────────────────────────────
LÕI      "xử lý lỗi che khuất logic = sai" (tr.103).
         Tách xử-lý-lỗi thành MỐI BẬN TÂM RIÊNG.

EXCEPTION > mã lỗi: caller sạch, logic không bị che (tr.104).
         Viết try-catch-finally TRƯỚC (try = transaction, tr.105).
         Exception phải mang BỐI CẢNH (thao tác + kiểu lỗi).

BỌC API ngoài về một kiểu exception chung (tr.109) → Bài 7.
SPECIAL CASE: object xử lý sẵn ca đặc biệt, caller khỏi rẽ nhánh.

ĐỪNG TRẢ NULL  trút rắc rối lên caller (tr.110). Trả [] / object
         mặc định. getEmployees(): [] thay vì null → hết null-check.
ĐỪNG TRUYỀN NULL  còn tệ hơn (tr.111). Cấm null theo mặc định.

2026   strictNullChecks (TS), Optional (Kotlin/Swift/Rust) →
       null là lỗi LÚC BIÊN DỊCH. Lựa chọn thứ ba: Result<T,E>
       (lỗi là giá trị). Checked exception = sai lầm, đã khép.
```

## Nguồn

- **Robert C. Martin**, *Clean Code* (Prentice Hall, 2008) — **Chương 7, "Error Handling"** (Michael Feathers) (`tr. 103–112`): xử lý lỗi không được che logic (tr. 103); exception thay mã lỗi, `DeviceController` (tr. 104–105); viết try-catch-finally trước với TDD (tr. 105–106); unchecked exception, "cuộc tranh luận đã khép", giá của checked exception (tr. 106–107); cung cấp bối cảnh (tr. 107); định nghĩa exception theo nhu cầu caller, bọc API bên thứ ba (tr. 107–109); định nghĩa luồng bình thường, Special Case Pattern (tr. 109–110); đừng trả null (tr. 110–111); đừng truyền null (tr. 111–112); kết luận (tr. 112). `tai_lieu/Clean.Code.2008.8.pdf`
- Phản biện/bổ sung 2026 dẫn từ ngoài sách: TypeScript `strictNullChecks`; `Option`/`Optional` (Rust/Kotlin/Swift); `Result`/`Either` (`neverthrow`); Go `(value, err)`.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 31`.

---

**Bản đồ khoá học:** [Bài 0 — Clean Code là gì](bai_00_clean_code_la_gi.md) · [Bài 1 — Đặt tên](bai_01_dat_ten.md) · [Bài 2 — Hàm](bai_02_ham.md) · [Bài 3 — Comment](bai_03_comment.md) · [Bài 4 — Định dạng](bai_04_dinh_dang.md) · [Bài 5 — Object & dữ liệu](bai_05_object_va_du_lieu.md) · [Bài 6 ← bạn đang ở đây] · [Bài 7 — Ranh giới](bai_07_ranh_gioi.md) · [Bài 8 — Unit test](bai_08_unit_test.md) · [Bài 9 — Class](bai_09_class.md) · [Bài 10 — Hệ thống](bai_10_he_thong.md) · [Bài 11 — Thiết kế nổi lên](bai_11_thiet_ke_noi_len.md) · [Bài 12 — Concurrency](bai_12_concurrency.md) · [Bài 13 — Xem code sạch nảy sinh](bai_13_xem_code_nay_sinh.md) · [Bài 14 — Refactor ngoài đời](bai_14_refactor_ngoai_doi.md) · [Bài 15 — Danh mục mùi code](bai_15_danh_muc_mui_code.md)

Xem thêm [README khoá học](../README.md).
