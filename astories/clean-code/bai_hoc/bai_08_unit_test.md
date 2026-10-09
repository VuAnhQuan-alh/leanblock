# Bài 8 — Unit test: giữ test sạch như giữ code

> [!info] Về bài này
> Dựng từ **Chương 9 — "Unit Tests"** của *Clean Code* (Robert C. Martin, 2008 — `tai_lieu/`, `tr. 121–133`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 31`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Mạch bài: *test bẩn → gọi tên vấn đề → bản sạch (TypeScript, chạy được) → nguyên tắc → đối chiếu 2026 → áp dụng*.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: từ test vứt đi tới test tự động](#1-mở-đầu-từ-test-vứt-đi-tới-test-tự-động)
2. [Ba luật của TDD](#2-ba-luật-của-tdd)
3. [Giữ test sạch, nếu không sẽ mất chúng](#3-giữ-test-sạch-nếu-không-sẽ-mất-chúng)
4. [Code minh hoạ: một khái niệm mỗi test](#4-code-minh-hoạ-một-khái-niệm-mỗi-test)
5. [F.I.R.S.T — năm chữ của test sạch](#5-first--năm-chữ-của-test-sạch)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào codebase của bạn](#7-áp-dụng-vào-codebase-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mở đầu: từ test vứt đi tới test tự động

Uncle Bob mở chương bằng một kỷ niệm giữa thập niên 90: để test một `Timer` trên hệ nhúng, ông viết một chương trình nghe bàn phím, gõ một giai điệu rồi chờ nó phát lại trên màn hình năm giây sau. Ông *hát* theo khi gõ, rồi hát lại khi các dấu chấm hiện ra. "Đó là test của tôi!" — xem nó chạy xong, ông **vứt code test đi**. Ngày nay ông sẽ viết test phủ mọi ngóc ngách, mock hàm thời gian để kiểm soát tuyệt đối, và *check-in test cùng code trong một gói*. Nghề đã đi rất xa — nhưng nhiều người, trong cơn vội thêm test, đã bỏ lỡ những điểm tinh tế của việc viết test *tốt*.

## 2. Ba luật của TDD

> [!quote] Ch. 9 — The Three Laws of TDD (tr. 122)
> "First Law You may not write production code until you have written a failing unit test. Second Law You may not write more of a unit test than is sufficient to fail, and not compiling is failing. Third Law You may not write more production code than is sufficient to pass the currently failing test."
>
> *Luật 1: Không được viết code sản xuất khi chưa có một unit test đang **fail**. Luật 2: Không được viết test nhiều hơn mức đủ để fail — và không biên dịch được cũng là fail. Luật 3: Không được viết code sản xuất nhiều hơn mức đủ để làm test đang fail **pass**.*

Ba luật này khoá bạn vào một vòng lặp chừng **ba mươi giây**: test và code sản xuất ra đời cùng nhau, test chỉ đi trước vài giây. Làm theo cách này, mỗi ngày bạn viết hàng chục test, mỗi năm hàng nghìn — phủ gần như toàn bộ code. Nhưng khối test khổng lồ đó cũng đặt ra một bài toán quản lý: nếu để nó bẩn, nó thành gánh nặng.

## 3. Giữ test sạch, nếu không sẽ mất chúng

Uncle Bob kể một đội từng quyết định test *không cần* sạch như code sản xuất — "quick and dirty". Hệ quả dây chuyền: code sản xuất tiến hoá → test bẩn khó sửa theo → sửa test tốn hơn viết code mới → test thành gánh nặng → vứt bỏ cả bộ test → mất khả năng đổi code an toàn → code sản xuất mục ruỗng theo. Bài học:

> [!quote] Ch. 9 — Keeping Tests Clean (tr. 124)
> "Test code is just as important as production code. It is not a second-class citizen. It requires thought, design, and care."
>
> *Code test quan trọng ngang code sản xuất. Nó không phải công dân hạng hai. Nó đòi hỏi suy nghĩ, thiết kế và chăm chút.*

Vì sao đáng đến thế? Vì chính test là thứ giữ code *đổi được*:

> [!quote] Ch. 9 — Tests Enable the -ilities (tr. 124)
> "It is unit tests that keep our code flexible, maintainable, and reusable. […] If you have tests, you do not fear making changes to the code!"
>
> *Chính unit test giữ cho code **linh hoạt, dễ bảo trì, tái dùng được**. […] Có test rồi, bạn không còn sợ thay đổi code!*

## 4. Code minh hoạ: một khái niệm mỗi test

Điều làm nên test sạch, theo Uncle Bob, là: "tính đọc được, tính đọc được, và tính đọc được". Và một quy tắc cốt lõi:

> [!quote] Ch. 9 — Single Concept per Test (tr. 131)
> "we want to test a single concept in each test function."
>
> *ta muốn mỗi hàm test kiểm đúng **một khái niệm**.*

Một hàm test gộp nhiều khái niệm buộc người đọc phải tự đoán mỗi đoạn đang kiểm gì. Tách ra, mỗi hàm một khái niệm, tên tự kể:

```typescript
import { strict as assert } from "node:assert";

// ===== SUT: hàm thuần, dễ test (Fast, Repeatable, không phụ thuộc môi trường) =====
function priceAfterDiscount(price: number, percentOff: number): number {
  return Math.round(price * (100 - percentOff)) / 100;
}

// ===== Test BẨN: một hàm gộp nhiều KHÁI NIỆM, khó đọc =====
function dirtyTest(): void {
  assert.equal(priceAfterDiscount(100, 0), 100);
  assert.equal(priceAfterDiscount(100, 10), 90);
  assert.equal(priceAfterDiscount(100, 100), 0);
  assert.equal(priceAfterDiscount(250, 20), 200);
  // trộn: không giảm, giảm thường, giảm hết, số lẻ — bốn khái niệm một chỗ
}

// ===== Test SẠCH: mỗi hàm một KHÁI NIỆM, tên tự kể (build-operate-check) =====
function noDiscountKeepsPrice(): void {
  assert.equal(priceAfterDiscount(100, 0), 100);
}
function tenPercentOff(): void {
  assert.equal(priceAfterDiscount(100, 10), 90);
}
function fullDiscountIsFree(): void {
  assert.equal(priceAfterDiscount(100, 100), 0);
}

// chạy (self-validating: kết quả là boolean pass/fail, không phải đọc log)
const tests = { dirtyTest, noDiscountKeepsPrice, tenPercentOff, fullDiscountIsFree };
for (const [name, fn] of Object.entries(tests)) {
  fn();
  console.log(`PASS  ${name}`);
}
console.log("tất cả test xanh — test sạch: mỗi hàm một khái niệm, tên tự kể.");
```

Kết quả chạy thật:

```
PASS  dirtyTest
PASS  noDiscountKeepsPrice
PASS  tenPercentOff
PASS  fullDiscountIsFree
tất cả test xanh — test sạch: mỗi hàm một khái niệm, tên tự kể.
```

`dirtyTest` *vẫn pass* — nó không sai. Nhưng khi nó fail, bạn phải đọc từng dòng để biết khái niệm nào hỏng. Còn khi `fullDiscountIsFree` fail, cái tên đã nói hết. Mỗi test sạch theo lối **build–operate–check**: dựng dữ liệu, gọi thao tác, kiểm kết quả — ít assert, một khái niệm.

> [!note] Tự thử
> 1. Phá `priceAfterDiscount` (đổi `100 - percentOff` thành `100 + percentOff`). Chạy lại: test nào đỏ? Cái tên test có cho bạn biết ngay *khái niệm* nào hỏng không — so với `dirtyTest`?
> 2. Thêm test `oddDiscountRoundsCorrectly` cho `priceAfterDiscount(250, 20)`. Giờ `dirtyTest` có còn lý do tồn tại không?
> 3. Làm một test *phụ thuộc* test khác (dùng biến toàn cục mà test trước gán). Chạy đảo thứ tự xem có gãy không — đó là vì sao F.I.R.S.T đòi **Independent**.

## 5. F.I.R.S.T — năm chữ của test sạch

Test sạch tuân theo năm quy tắc ghép thành chữ **FIRST**:

- **Fast** — nhanh. Test chậm thì bạn ngại chạy; ngại chạy thì phát hiện lỗi muộn.
- **Independent** — độc lập. Test này không được dựng điều kiện cho test kia; chạy được theo thứ tự bất kỳ. Phụ thuộc nhau thì một cái fail kéo theo cả loạt fail giả.
- **Repeatable** — lặp lại được ở mọi môi trường (máy bạn, QA, production, cả khi không mạng trên tàu). Không thì bạn luôn có cớ "tại môi trường".
- **Self-Validating** — tự kiểm chứng:

> [!quote] Ch. 9 — F.I.R.S.T. (tr. 131)
> "The tests should have a boolean output. Either they pass or fail. You should not have to read through a log file to tell whether the tests pass."
>
> *Test phải cho ra kết quả boolean. Hoặc pass hoặc fail. Bạn không phải đọc log để biết test có qua hay không.*

- **Timely** — kịp lúc. Viết test *ngay trước* code sản xuất làm nó pass; viết test sau thì dễ phát hiện code khó test.

Và lời kết của chương, một vòng khép lại với [Bài 0](bai_00_clean_code_la_gi.md):

> [!quote] Ch. 9 — Conclusion (tr. 133)
> "If you let the tests rot, then your code will rot too. Keep your tests clean."
>
> *Nếu bạn để test mục ruỗng, thì code của bạn cũng sẽ mục ruỗng theo. Hãy giữ test luôn sạch.*

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Chương này **già đi tốt về kỷ luật test**, nhưng tỉ lệ và thứ bậc test là chỗ 2026 bàn lại nhiều.
> - **TDD "ba luật" — còn giá trị, nhưng không còn là giáo điều.** Cuộc tranh luận **"Is TDD Dead?"** (2014, DHH – Kent Beck – Martin Fowler) đặt lại vấn đề: test-first là *một* kỷ luật tốt, không phải *luật* duy nhất. DHH nêu "test-induced design damage" — ép code méo mó chỉ để test-first được. Năm 2026: viết test là bắt buộc với người chuyên nghiệp; viết *trước* hay *ngay sau* thì tuỳ ngữ cảnh. (Nối với [Bài 5 khoá Clean Coder](../../clean-coder/bai_hoc/bai_05_tdd.md) nếu bạn học cả hai khoá.)
> - **Kim tự tháp test → Testing Trophy.** Uncle Bob nghiêng hẳn về unit test. Năm 2026, **Kent C. Dodds** đề xuất *Testing Trophy* (nặng integration test), còn *testing honeycomb* (cho microservice) cũng tương tự: nhiều unit test cô lập bằng mock có thể *pass trong khi hệ thống vẫn hỏng*. Cân bằng mới: ít unit test hơn, nhiều integration test "test như người dùng dùng" hơn.
> - **F.I.R.S.T — vẫn vàng nguyên.** Năm chữ này gần như không ai cãi, và là tiêu chí tốt để review test đến tận 2026.
> - **"Test code quan trọng ngang production" — vẫn vàng, và mạnh hơn.** CI bắt buộc test xanh mới merge; coverage gate; test là tài liệu sống. Nhưng cảnh báo 2026: đừng thờ *con số coverage* (Goodhart's law) — 100% coverage vẫn có thể test rỗng. Chất lượng assertion > % dòng chạy qua.
> - **Mới sau 2008**: property-based testing (fast-check), snapshot test, và AI sinh test — nhưng AI sinh test dễ ra test "xác nhận code hiện tại" chứ không kiểm *ý định*; vẫn cần người xem lại.

## 7. Áp dụng vào codebase của bạn

> [!question] Áp dụng vào codebase của bạn
> 1. **Chấm test của bạn theo F.I.R.S.T.** Mở bộ test dự án, chọn 5 test, chấm từng chữ F-I-R-S-T. Chữ nào rớt nhiều nhất? (Thường là *Fast* hoặc *Independent*.)
> 2. **Săn test nhiều khái niệm.** Tìm một hàm test dài assert đủ thứ. Tách thành vài test tên tự kể. Khi nó fail, giờ bạn biết ngay khái niệm nào hỏng chưa?
> 3. **Đối chiếu hình tháp.** Dự án bạn nghiêng unit hay integration? Có unit test nào mock nhiều tới mức *pass mà hệ thống vẫn hỏng* không? Cân nhắc một integration test thay thế.
> 4. **Đừng thờ coverage.** Nếu có coverage gate, chọn một file coverage cao và đọc test: chúng kiểm *hành vi* hay chỉ *chạy qua dòng*? (Goodhart: khi con số thành mục tiêu, nó thôi là thước đo tốt.)

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Three Laws of TDD** | Test fail trước → chỉ đủ để fail → code chỉ đủ để pass; vòng lặp ~30 giây (tr. 122). |
| **Tests enable the -ilities** | Test là thứ giữ code flexible/maintainable/reusable vì nó xoá nỗi sợ đổi (tr. 124). |
| **Single concept per test** | Mỗi hàm test kiểm một khái niệm; tối thiểu assert mỗi khái niệm (tr. 131). |
| **Build-Operate-Check** | Cấu trúc một test: dựng dữ liệu → gọi thao tác → kiểm kết quả. |
| **F.I.R.S.T** | Fast, Independent, Repeatable, Self-Validating, Timely (tr. 131–133). |
| **Testing Trophy / honeycomb** | (2026) Nghiêng về integration test hơn kim tự tháp unit-nặng. |

## 9. Câu hỏi tự kiểm tra

1. Phát biểu ba luật của TDD. Vòng lặp chúng tạo ra dài bao lâu? *(tr. 122)*
2. Chuyện gì xảy ra với đội để test "quick and dirty"? Vì sao "test bẩn tệ ngang không có test"? *(tr. 124)*
3. Vì sao "test enable the -ilities"? *(tr. 124)*
4. Giải thích năm chữ F.I.R.S.T. *(tr. 131–133)*
5. "Is TDD Dead?" và Testing Trophy đặt lại điều gì về lời khuyên của chương này? *(Đối chiếu 2026)*

## Tóm tắt một trang

```
BÀI 8 — UNIT TEST: GIỮ TEST SẠCH NHƯ GIỮ CODE
─────────────────────────────────────────────────────────
BA LUẬT TDD (tr.122): test-fail trước → chỉ đủ để fail →
         code chỉ đủ để pass. Vòng lặp ~30 giây.

GIỮ SẠCH  "test quan trọng NGANG production" (tr.124).
         Để bẩn → khó sửa → vứt bộ test → code mục ruỗng.
         "test enable the -ilities": xoá nỗi sợ đổi (tr.124).

MỘT KHÁI NIỆM MỖI TEST (tr.131). build-operate-check, ít assert.
         fullDiscountIsFree() fail → biết ngay khái niệm nào hỏng.

F.I.R.S.T (tr.131-133)
   Fast · Independent · Repeatable · Self-Validating · Timely
   "để test mục → code mục. Giữ test sạch" (tr.133).

2026   "Is TDD Dead?" (2014): test-first là MỘT kỷ luật, không
       phải luật duy nhất; coi chừng test-induced design damage.
       Testing Trophy (Dodds): nghiêng integration hơn unit-nặng.
       Đừng thờ % coverage (Goodhart). F.I.R.S.T vẫn vàng.
```

## Nguồn

- **Robert C. Martin**, *Clean Code* (Prentice Hall, 2008) — **Chương 9, "Unit Tests"** (`tr. 121–133`): test `Timer` vứt-đi thời 90s (tr. 121–122); ba luật TDD, vòng lặp 30 giây (tr. 122–123); giữ test sạch, câu chuyện đội "quick and dirty" (tr. 123–124); tests enable the -ilities (tr. 124); clean tests = readability, Listing 9-1 (tr. 124–127); domain-specific testing language, one assert per test (tr. 127–131); single concept per test, `addMonths` (tr. 131–132); F.I.R.S.T (tr. 131–133); kết luận (tr. 133). `tai_lieu/Clean.Code.2008.8.pdf`
- Phản biện 2026 dẫn từ ngoài sách: *"Is TDD Dead?"* (2014, DHH/Beck/Fowler); Kent C. Dodds, *Testing Trophy*; định luật Goodhart về coverage; property-based testing (fast-check).
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 31`.

---

**Bản đồ khoá học:** [Bài 0 — Clean Code là gì](bai_00_clean_code_la_gi.md) · [Bài 1 — Đặt tên](bai_01_dat_ten.md) · [Bài 2 — Hàm](bai_02_ham.md) · [Bài 3 — Comment](bai_03_comment.md) · [Bài 4 — Định dạng](bai_04_dinh_dang.md) · [Bài 5 — Object & dữ liệu](bai_05_object_va_du_lieu.md) · [Bài 6 — Xử lý lỗi](bai_06_xu_ly_loi.md) · [Bài 7 — Ranh giới](bai_07_ranh_gioi.md) · [Bài 8 ← bạn đang ở đây] · [Bài 9 — Class](bai_09_class.md) · [Bài 10 — Hệ thống](bai_10_he_thong.md) · [Bài 11 — Thiết kế nổi lên](bai_11_thiet_ke_noi_len.md) · [Bài 12 — Concurrency](bai_12_concurrency.md) · [Bài 13 — Xem code sạch nảy sinh](bai_13_xem_code_nay_sinh.md) · [Bài 14 — Refactor ngoài đời](bai_14_refactor_ngoai_doi.md) · [Bài 15 — Danh mục mùi code](bai_15_danh_muc_mui_code.md)

Xem thêm [README khoá học](../README.md).
