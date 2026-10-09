# Bài 15 — Danh mục mùi code: bảng tra của cả khoá

> [!info] Về bài này
> Dựng từ **Chương 17 — "Smells and Heuristics"** của *Clean Code* (Robert C. Martin, 2008 — `tai_lieu/`, `tr. 285–314`).
> Đây là **chương bảng tra**: ~66 "mùi code" (code smell) và heuristic, đánh mã theo nhóm (C/E/F/G/J/N/T). Bài này dùng nó làm **mục lục ngược của cả khoá** — mỗi mùi trỏ về bài đã mổ nó.
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 31`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: một danh sách, một hệ giá trị](#1-mở-đầu-một-danh-sách-một-hệ-giá-trị)
2. [Code minh hoạ: gột ba mùi cùng lúc](#2-code-minh-hoạ-gột-ba-mùi-cùng-lúc)
3. [Bảng tra mùi code theo nhóm](#3-bảng-tra-mùi-code-theo-nhóm)
4. [Vài heuristic General đáng nhớ nhất](#4-vài-heuristic-general-đáng-nhớ-nhất)
5. [Câu chốt: không phải luật, mà là hệ giá trị](#5-câu-chốt-không-phải-luật-mà-là-hệ-giá-trị)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào codebase của bạn](#7-áp-dụng-vào-codebase-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mở đầu: một danh sách, một hệ giá trị

> [!quote] Ch. 17 — Smells and Heuristics (tr. 285)
> "In his wonderful book Refactoring […] Martin Fowler identified many different 'Code Smells.' The list that follows includes many of Martin's smells and adds many more of my own."
>
> *Trong cuốn **Refactoring** tuyệt vời của mình, Martin Fowler đã nêu ra nhiều "mùi code" khác nhau. Danh sách dưới đây gồm nhiều mùi của Martin và thêm nhiều mùi của riêng tôi.*

Uncle Bob lập danh sách này bằng cách refactor nhiều chương trình, mỗi lần đổi một chỗ thì tự hỏi "vì sao mình đổi" rồi ghi lại. Kết quả là một danh mục vừa để *đọc từ đầu đến cuối*, vừa để *tra cứu*:

> [!quote] Ch. 17 — Smells and Heuristics (tr. 286)
> "This list is meant to be read from top to bottom and also to be used as a reference."
>
> *Danh sách này vừa để đọc từ trên xuống, vừa để dùng làm tài liệu tra cứu.*

Bài này đúng là một **tra cứu**: dùng nó như tấm bản đồ ngược — thấy một mùi, biết ngay bài nào của khoá đã mổ nó.

## 2. Code minh hoạ: gột ba mùi cùng lúc

Một đoạn code thật thường bốc *nhiều* mùi một lúc. Ví dụ hàm `canCheckout` dưới đây mắc ba mùi: **G25** (số ma thuật `18`, `0`), **G29** (điều kiện phủ định `!(...)`), và ý định bị che (thiếu **G19** biến giải thích):

```typescript
import { strict as assert } from "node:assert";

// TRƯỚC: nhiều "mùi" cùng lúc —
// G25 số ma thuật (18, 0), G29 điều kiện phủ định (!(... )), G19 ý định bị che
function canCheckoutDirty(age: number, balance: number): boolean {
  return !(age < 18) && !(balance <= 0);
}

// SAU: G25 đặt tên hằng, G19 biến giải thích, G29 điều kiện khẳng định
const MIN_AGE = 18;
function canCheckoutClean(age: number, balance: number): boolean {
  const isAdult = age >= MIN_AGE;
  const hasFunds = balance > 0;
  return isAdult && hasFunds;
}

const cases: Array<[number, number]> = [
  [17, 100],
  [18, 100],
  [25, 0],
  [30, 50],
];
for (const [age, bal] of cases) {
  assert.equal(canCheckoutDirty(age, bal), canCheckoutClean(age, bal));
  console.log(`age=${age} balance=${bal} -> ${canCheckoutClean(age, bal)}`);
}
console.log("cùng kết quả; bản sạch gột 3 mùi: G25 số ma thuật, G29 phủ định, G19 biến giải thích.");
```

Kết quả chạy thật:

```
age=17 balance=100 -> false
age=18 balance=100 -> true
age=25 balance=0 -> false
age=30 balance=50 -> true
cùng kết quả; bản sạch gột 3 mùi: G25 số ma thuật, G29 phủ định, G19 biến giải thích.
```

`!(age < 18) && !(balance <= 0)` cho đúng kết quả nhưng bắt não bạn *đảo ngược* hai lần. `isAdult && hasFunds` đọc thẳng. Đây là cách danh mục mùi hoạt động trong thực tế: bạn không học thuộc 66 mã, bạn tập *ngửi* thấy "có gì đó không ổn" rồi tra xem nó là mùi gì và cách gột.

> [!note] Tự thử
> 1. Thêm điều kiện thứ ba "tài khoản không bị khoá" theo kiểu phủ định (`!isLocked`) vào bản bẩn, rồi gột nó theo G29. Bản nào bạn đọc nhanh hơn?
> 2. Đổi `MIN_AGE` thành `21`. Bạn sửa mấy chỗ ở bản sạch? Ở bản bẩn (nếu `18` xuất hiện nhiều nơi)?
> 3. Đặt tên hàm `canCheckoutDirty` thành `check`. Giờ nó mắc thêm mùi nào? (Gợi ý: **G20** / **N1** — xem bảng dưới.)

## 3. Bảng tra mùi code theo nhóm

Toàn bộ ~66 mùi, nhóm theo mã, kèm bài của khoá đã mổ:

| Nhóm | Mã | Mùi | Mổ ở bài |
| --- | --- | --- | --- |
| **Comments** | C1–C5 | thông tin lạc chỗ, comment lỗi thời, thừa, viết dở, **code bị comment lại** | [Bài 3](bai_03_comment.md) |
| **Environment** | E1–E2 | build / test cần hơn một bước | [Bài 8](bai_08_unit_test.md), [Bài 10](bai_10_he_thong.md) |
| **Functions** | F1–F4 | quá nhiều tham số, tham số đầu ra, cờ boolean, **hàm chết** | [Bài 2](bai_02_ham.md) |
| **General** | G1–G36 | (36 mùi tổng quát — xem mục 4) | rải khắp khoá |
| **Java** | J1–J3 | import dài, kế thừa hằng, hằng vs enum | (đặc thù Java — lược) |
| **Names** | N1–N7 | tên mô tả, đúng mức trừu tượng, chuẩn hoá, rõ nghĩa, dài theo phạm vi, tránh mã hoá, **tên tả side-effect** | [Bài 1](bai_01_dat_ten.md) |
| **Tests** | T1–T9 | thiếu test, dùng coverage tool, đừng bỏ test vặt, test boundary, test dồn quanh bug, **test phải nhanh** | [Bài 8](bai_08_unit_test.md) |

## 4. Vài heuristic General đáng nhớ nhất

36 mục nhóm **G** là phần ruột; những mục đắt nhất và nơi khoá đã mổ:

| Mã | Heuristic | Mổ ở bài |
| --- | --- | --- |
| **G5** | Duplication (trùng lặp) — "gốc rễ mọi điều xấu" | [Bài 2](bai_02_ham.md), [Bài 11](bai_11_thiet_ke_noi_len.md) |
| **G6** | Code at Wrong Level of Abstraction | [Bài 2](bai_02_ham.md) |
| **G14** | Feature Envy | [Bài 5](bai_05_object_va_du_lieu.md) |
| **G15** | Selector Arguments (cờ boolean) | [Bài 2](bai_02_ham.md) |
| **G19** | Use Explanatory Variables (biến giải thích) | mục 2 trên |
| **G20** | Function Names Should Say What They Do | [Bài 1](bai_01_dat_ten.md), [Bài 2](bai_02_ham.md) |
| **G23** | Prefer Polymorphism to If/Else or Switch/Case | [Bài 2](bai_02_ham.md), [Bài 5](bai_05_object_va_du_lieu.md) |
| **G25** | Replace Magic Numbers with Named Constants | [Bài 1](bai_01_dat_ten.md), mục 2 |
| **G28** | Encapsulate Conditionals | mục 2 |
| **G29** | Avoid Negative Conditionals | mục 2 |
| **G30** | Functions Should Do One Thing | [Bài 2](bai_02_ham.md) |
| **G31** | Hidden Temporal Couplings | [Bài 2](bai_02_ham.md), [Bài 12](bai_12_concurrency.md) |
| **G34** | Functions Should Descend Only One Level of Abstraction | [Bài 2](bai_02_ham.md) |
| **G36** | Avoid Transitive Navigation (Luật Demeter) | [Bài 5](bai_05_object_va_du_lieu.md) |

Thấy danh sách này gần như *phủ lại toàn bộ khoá* không? Đó là chủ ý: Chương 17 là bản cô đọng của cả cuốn, viết dưới dạng "mùi để ngửi" thay vì "nguyên tắc để nhớ".

## 5. Câu chốt: không phải luật, mà là hệ giá trị

Lời kết của chương — cũng là lời kết của cả phần "code sạch" — làm rõ: danh sách này không phải một bộ luật để tuân theo máy móc.

> [!quote] Ch. 17 — Conclusion (tr. 314)
> "Clean code is not written by following a set of rules. You don't become a software craftsman by learning a list of heuristics. Professionalism and craftsmanship come from values that drive disciplines."
>
> *Code sạch không phải được viết ra bằng cách tuân theo một bộ luật. Bạn không trở thành thợ thủ công phần mềm bằng cách học thuộc một danh sách heuristic. Tính chuyên nghiệp và tay nghề đến từ những **giá trị** dẫn dắt kỷ luật.*

Danh sách chỉ *ngụ ý* một hệ giá trị — và hệ giá trị ấy mới là đích thực sự của cả cuốn sách. Đây đúng tinh thần [Bài 0](bai_00_clean_code_la_gi.md): các bậc thầy định nghĩa "sạch" mỗi người một kiểu, vì sạch là *khẩu vị được rèn*, không phải checklist.

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Danh mục mùi này **già đi tốt về nội dung**, và điều lớn nhất năm 2026 là: phần lớn nó đã được **tự động hoá**.
> - **Linter/analyzer bắt mùi thay bạn.** Nhiều mục trong danh sách giờ là *rule* bật sẵn: ESLint/Biome (JS/TS), SonarQube/SonarLint (đa ngôn ngữ), golangci-lint, Ruff (Python). G5 (trùng lặp), G25 (magic number), G29 (negative conditional), C5 (commented-out code), F4 (dead function) — máy flag ngay khi bạn gõ. Năm 2026, một phần "ngửi mùi" là việc của CI, không phải của mắt người.
> - **Nhưng máy chỉ bắt mùi *cú pháp*, không bắt mùi *ngữ nghĩa*.** G6 (sai mức trừu tượng), G14 (feature envy), G17 (trách nhiệm đặt sai chỗ), G22 (phụ thuộc logic nên thành vật lý) đòi *hiểu ý định* — vẫn cần người (và một phần, review có AI hỗ trợ). Đây là nơi tay nghề 2026 còn giá trị.
> - **Coi chừng biến mùi thành giáo điều (Goodhart).** Khi "0 cảnh báo linter" thành mục tiêu, người ta tắt rule hoặc viết lách để qua — đúng cái bẫy mà quy tắc 4 ([Bài 11](bai_11_thiet_ke_noi_len.md)) và lời kết chương này cảnh báo: danh sách chỉ *ngụ ý* giá trị, đừng thờ danh sách.
> - **"Giá trị dẫn dắt kỷ luật, không phải luật" — càng đúng trong kỷ nguyên AI.** AI có thể đọc thuộc cả 66 mùi và sửa cú pháp, nhưng *khẩu vị* về khi nào một trừu tượng là đúng, khi nào tách là quá đà — vẫn là thứ con người rèn. Chính vì vậy, câu kết tr. 314 là câu bản lề giữa *Clean Code* và cuốn chị em *The Clean Coder* (xem khoá [`clean-coder`](../../clean-coder/README.md)): từ **code sạch** sang **nghề sạch**.
> - **Vẫn vàng**: toàn bộ các mùi ngữ nghĩa, và thông điệp "sạch là hệ giá trị, không phải checklist".

## 7. Áp dụng vào codebase của bạn

> [!question] Áp dụng vào codebase của bạn
> 1. **Bật một analyzer.** Nếu dự án chưa có, cài ESLint/SonarLint (hoặc tương đương). Chạy một lần — bao nhiêu mùi trong danh sách này được máy flag tự động?
> 2. **Tìm một mùi ngữ nghĩa máy bỏ sót.** Tự đọc một module và tìm G6 (sai mức trừu tượng) hoặc G14 (feature envy) — những mùi linter *không* bắt. Đây là bài tập rèn khẩu vị.
> 3. **Dùng bảng mục 3–4 làm checklist review.** Lần review PR tới, lướt qua nhóm G và hỏi "đoạn này có mùi nào không?". Nhưng nhớ mục 6: đừng biến nó thành giáo điều.
> 4. **Nối sang nghề.** Đọc câu kết tr. 314. Với bạn, "giá trị dẫn dắt kỷ luật" nghĩa là gì — và đó là cây cầu sang khoá [`clean-coder`](../../clean-coder/README.md) về *cách hành xử* chuyên nghiệp.

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Code smell** | "Mùi code" — dấu hiệu bề mặt gợi ý một vấn đề thiết kế sâu hơn (Fowler) (tr. 285). |
| **Heuristic** | Quy tắc kinh nghiệm để nhận và gột mùi; không phải luật tuyệt đối (tr. 285). |
| **Mã mùi (C/E/F/G/J/N/T)** | Comments/Environment/Functions/General/Java/Names/Tests — nhóm trong danh mục. |
| **G5 Duplication** | Trùng lặp — mùi quan trọng nhất; "gốc rễ mọi điều xấu" (tr. ~289). |
| **G23 Prefer polymorphism** | Thay if/else/switch theo loại bằng đa hình (tr. ~301). |
| **"Values drive disciplines"** | Sạch đến từ *giá trị*, không từ việc học thuộc checklist (tr. 314). |

## 9. Câu hỏi tự kiểm tra

1. Danh mục mùi này đến từ đâu, và Uncle Bob lập nó bằng cách nào? *(tr. 285–286)*
2. Hàm `canCheckoutDirty` ở mục 2 mắc những mùi nào (kèm mã)? Gột ra sao?
3. Kể ba mùi nhóm **General** mà *linter* bắt được tự động, và hai mùi nó *không* bắt được. *(Đối chiếu 2026)*
4. Vì sao danh sách "ngụ ý một hệ giá trị" thay vì là một bộ luật? *(tr. 314)*
5. Câu kết tr. 314 bắc cầu sang chủ đề nào của cuốn *The Clean Coder*?

## Tóm tắt một trang

```
BÀI 15 — DANH MỤC MÙI CODE: BẢNG TRA CỦA CẢ KHOÁ
─────────────────────────────────────────────────────────
NGUỒN  Fowler "code smells" + Uncle Bob thêm (tr.285). ~66 mùi,
       mã C/E/F/G/J/N/T. "vừa đọc trên-xuống, vừa tra cứu" (tr.286).

DEMO   canCheckout: !(age<18) && !(balance<=0) mắc 3 mùi:
       G25 số ma thuật · G29 phủ định · G19 thiếu biến giải thích
       → isAdult && hasFunds (cùng kết quả, đọc thẳng).

BẢNG TRA NGƯỢC  mỗi nhóm trỏ về bài đã mổ:
   Comments→B3 · Functions→B2 · Names→B1 · Tests→B8 ·
   G5/G11 trùng lặp→B2,11 · G14/G36 Demeter→B5 · G23 đa hình→B2,5

CÂU CHỐT  "clean code KHÔNG viết bằng cách theo bộ luật...
       tay nghề đến từ GIÁ TRỊ dẫn dắt kỷ luật" (tr.314).

2026  phần lớn mùi cú pháp đã TỰ ĐỘNG HOÁ (ESLint/Sonar/Ruff).
      Mùi ngữ nghĩa (G6/G14/G17) vẫn cần người. Đừng thờ "0 cảnh
      báo" (Goodhart). Cầu nối sang khoá clean-coder: nghề sạch.
```

## Nguồn

- **Robert C. Martin**, *Clean Code* (Prentice Hall, 2008) — **Chương 17, "Smells and Heuristics"** (`tr. 285–314`): nguồn gốc từ Fowler, cách lập danh sách (tr. 285–286); Comments C1–C5 (tr. 286–287); Environment E1–E2, Functions F1–F4 (tr. 287–288); General G1–G36 (tr. 288–308); Java J1–J3 (tr. 308–309); Names N1–N7 (tr. 309–311); Tests T1–T9 (tr. 313–314); kết luận "values drive disciplines" (tr. 314). `tai_lieu/Clean.Code.2008.8.pdf`
- Bổ sung 2026 dẫn từ ngoài sách: ESLint/Biome, SonarQube/SonarLint, Ruff, golangci-lint; định luật Goodhart; cầu nối sang *The Clean Coder* (khoá `clean-coder`).
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 31`.

---

**Bản đồ khoá học:** [Bài 0 — Clean Code là gì](bai_00_clean_code_la_gi.md) · [Bài 1 — Đặt tên](bai_01_dat_ten.md) · [Bài 2 — Hàm](bai_02_ham.md) · [Bài 3 — Comment](bai_03_comment.md) · [Bài 4 — Định dạng](bai_04_dinh_dang.md) · [Bài 5 — Object & dữ liệu](bai_05_object_va_du_lieu.md) · [Bài 6 — Xử lý lỗi](bai_06_xu_ly_loi.md) · [Bài 7 — Ranh giới](bai_07_ranh_gioi.md) · [Bài 8 — Unit test](bai_08_unit_test.md) · [Bài 9 — Class](bai_09_class.md) · [Bài 10 — Hệ thống](bai_10_he_thong.md) · [Bài 11 — Thiết kế nổi lên](bai_11_thiet_ke_noi_len.md) · [Bài 12 — Concurrency](bai_12_concurrency.md) · [Bài 13 — Xem code sạch nảy sinh](bai_13_xem_code_nay_sinh.md) · [Bài 14 — Refactor ngoài đời](bai_14_refactor_ngoai_doi.md) · [Bài 15 ← bạn đang ở đây]

Xem thêm [README khoá học](../README.md).
