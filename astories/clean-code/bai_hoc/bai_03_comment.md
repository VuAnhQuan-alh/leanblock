# Bài 3 — Comment: một "cái tốt cần thiết", không hơn

> [!info] Về bài này
> Dựng từ **Chương 4 — "Comments"** của *Clean Code* (Robert C. Martin, 2008 — `tai_lieu/`, `tr. 53–74`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 31`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Mạch bài: *comment thừa → gọi tên vấn đề → bản sạch (TypeScript, chạy được) → nguyên tắc → đối chiếu 2026 → áp dụng*.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: comment là thất bại của diễn đạt](#1-mở-đầu-comment-là-thất-bại-của-diễn-đạt)
2. [Comment không cứu được code tồi](#2-comment-không-cứu-được-code-tồi)
3. [Code minh hoạ: comment tan vào tên hàm](#3-code-minh-hoạ-comment-tan-vào-tên-hàm)
4. [Những comment tốt (hiếm)](#4-những-comment-tốt-hiếm)
5. [Những comment tồi (đa số)](#5-những-comment-tồi-đa-số)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào codebase của bạn](#7-áp-dụng-vào-codebase-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mở đầu: comment là thất bại của diễn đạt

Chương mở bằng câu đề từ của Kernighan & Plauger:

> [!quote] Ch. 4 — Comments (tr. 53)
> "Don't comment bad code—rewrite it."
>
> *Đừng comment cho code tồi — hãy viết lại nó.*

Uncle Bob đẩy xa hơn: comment, đẹp nhất, cũng chỉ là một "cái tốt cần thiết" (*necessary evil*). Nếu ngôn ngữ của ta đủ sức diễn đạt, hoặc nếu ta đủ khéo để diễn đạt bằng code, thì gần như không cần comment.

> [!quote] Ch. 4 — Comments (tr. 54)
> "The proper use of comments is to compensate for our failure to express ourself in code. […] Comments are always failures."
>
> *Công dụng đúng đắn của comment là bù đắp cho việc ta **thất bại** trong diễn đạt bằng code. […] Comment luôn là những thất bại.*

Vì sao ông gay gắt thế? Vì comment **nói dối** — không phải lúc nào, không phải cố ý, nhưng quá thường xuyên. Code thay đổi và tiến hoá; comment không phải lúc nào cũng đi theo được, và dần trở thành những mẩu lạc lõng ngày một sai. Nên:

> [!quote] Ch. 4 — Comments (tr. 54)
> "Truth can only be found in one place: the code."
>
> *Sự thật chỉ nằm ở một nơi duy nhất: chính code.*

## 2. Comment không cứu được code tồi

Động cơ phổ biến nhất để viết comment là… code tồi. Ta viết một module rối, biết nó rối, rồi tự nhủ "thôi comment lại cho dễ hiểu". **Không.** Hãy dọn nó.

> [!quote] Ch. 4 — Comments Do Not Make Up for Bad Code (tr. 55)
> "Rather than spend your time writing the comments that explain the mess you've made, spend it cleaning that mess."
>
> *Thay vì tốn thời gian viết comment giải thích mớ bừa bộn bạn vừa tạo ra, hãy tốn thời gian ấy để dọn nó.*

Và cách dọn thường chỉ là: tạo một hàm nói đúng điều mà cái comment định nói.

## 3. Code minh hoạ: comment tan vào tên hàm

Ví dụ kinh điển của chương. Bạn muốn thấy cái nào — một comment cộng một điều kiện khó hiểu, hay một hàm tự giải thích?

```typescript
import { strict as assert } from "node:assert";

const HOURLY_FLAG = 0x0001;
type EmployeeData = { flags: number; age: number };

// ===== Bản bẩn: điều kiện khó hiểu, phải dán comment để cứu =====
// Check to see if the employee is eligible for full benefits
function eligibleDirty(employee: EmployeeData): boolean {
  return (employee.flags & HOURLY_FLAG) !== 0 && employee.age > 65;
}

// ===== Bản sạch: comment biến thành một hàm có tên =====
class Employee {
  private flags: number;
  private age: number;
  constructor(flags: number, age: number) {
    this.flags = flags;
    this.age = age;
  }
  isEligibleForFullBenefits(): boolean {
    return (this.flags & HOURLY_FLAG) !== 0 && this.age > 65;
  }
}

const rows: EmployeeData[] = [
  { flags: HOURLY_FLAG, age: 70 },
  { flags: HOURLY_FLAG, age: 40 },
  { flags: 0, age: 70 },
];
for (const r of rows) {
  const dirty = eligibleDirty(r);
  const clean = new Employee(r.flags, r.age).isEligibleForFullBenefits();
  assert.equal(dirty, clean);
  console.log(`flags=${r.flags} age=${r.age} -> đủ điều kiện: ${clean}`);
}
console.log("comment đã tan vào tên hàm; điều kiện giờ tự giải thích.");
```

Kết quả chạy thật:

```
flags=1 age=70 -> đủ điều kiện: true
flags=1 age=40 -> đủ điều kiện: false
flags=0 age=70 -> đủ điều kiện: false
comment đã tan vào tên hàm; điều kiện giờ tự giải thích.
```

`if (employee.isEligibleForFullBenefits())` nói đúng điều mà comment `// Check to see if the employee is eligible...` định nói — nhưng nó *không thể* lạc hậu, vì nó **là** code. Khi điều kiện đổi, hàm đổi theo; comment thì có thể bị bỏ quên. Chỉ mất vài giây suy nghĩ để biến phần lớn ý định thành code như vậy.

> [!note] Tự thử
> 1. Đổi điều kiện tuổi từ `> 65` thành `>= 65` **chỉ ở bản sạch**, rồi chạy lại. Giờ hai bản lệch nhau — `assert` có bắt được không? Đó là lý do "sự thật nằm ở code".
> 2. Giả sử bạn chỉ sửa điều kiện mà *quên* sửa comment `// ... age > 65`. Comment trở thành cái gì? (Gợi ý: Uncle Bob gọi nó là lời nói dối.)
> 3. Thêm một flag `SALARIED_FLAG = 0x0002` và một điều kiện mới. Bạn thấy dễ hơn khi gói nó trong tên hàm, hay khi viết thêm comment?

## 4. Những comment tốt (hiếm)

Uncle Bob thừa nhận một số comment là cần hoặc có ích — nhưng nhắc: *comment tốt nhất là comment bạn tìm được cách để khỏi phải viết*.

> [!quote] Ch. 4 — Good Comments (tr. 55)
> "the only truly good comment is the comment you found a way not to write."
>
> *comment thật sự tốt duy nhất là comment mà bạn tìm ra cách để không phải viết.*

Các loại ông chấp nhận:

- **Pháp lý** — bản quyền, giấy phép ở đầu file (nên trỏ tới văn bản ngoài, đừng chép cả giấy phép vào).
- **Thông tin** — ví dụ giải thích một regex khớp định dạng ngày giờ (nhưng tốt hơn là tách thành lớp riêng).
- **Giải thích ý định** — *vì sao* chọn giải pháp này; bạn có thể không đồng ý, nhưng ít nhất hiểu người viết định làm gì.
- **Làm rõ** — dịch một tham số/giá trị trả về khó hiểu *của thư viện bạn không sửa được* ra tiếng người.
- **Cảnh báo hậu quả** — "đừng chạy test này trừ khi bạn rảnh cả buổi"; "`SimpleDateFormat` không thread-safe".
- **TODO** — ghi chú việc cần làm nhưng chưa làm được; nhưng *không* phải cái cớ để bỏ code tồi lại trong hệ thống.
- **Khuếch đại** — nhấn rằng một dòng trông vô hại kỳ thực rất quan trọng (`// cái trim này cực quan trọng…`).
- **Javadoc cho API công khai** — hữu ích, nhưng vẫn phải trung thực như mọi comment khác.

## 5. Những comment tồi (đa số)

> [!quote] Ch. 4 — Bad Comments (tr. 59)
> "Most comments fall into this category. Usually they are crutches or excuses for poor code […] amounting to little more than the programmer talking to himself."
>
> *Phần lớn comment rơi vào loại này. Thường chúng là cái nạng hoặc cái cớ cho code dở […] chẳng hơn gì tiếng lập trình viên tự lẩm bẩm với chính mình.*

Bộ sưu tập "mùi" của chương:

- **Lẩm bẩm** (*mumbling*) — nhét comment chỉ vì thấy "nên có" hoặc vì quy trình bắt; ví dụ một `catch` trống với dòng `// No properties files means all defaults are loaded` mà chẳng ai hiểu ai nạp mặc định, ở đâu.
- **Thừa** (*redundant*) — comment mất nhiều thời gian đọc hơn cả đoạn code nó mô tả, mà lại kém chính xác hơn.
- **Gây hiểu lầm** (*misleading*) — chính comment thừa ở trên còn tinh vi sai: nói hàm "trả về khi `closed` thành true", thật ra nó chờ hết timeout rồi ném exception.
- **Bị bắt buộc** (*mandated*) — luật "mọi hàm phải có javadoc" đẻ ra rác như Listing 4-3: `@param title The title of the CD`.
- **Nhật ký, nhiễu, vị trí** — comment ghi lịch sử sửa đổi (đã có Git), `// Private instance variable`, hay `////////// Actions //////////`.
- **Code bị comment lại** (*commented-out code*) — đừng để. Người sau không dám xoá vì tưởng nó quan trọng. Git nhớ hết rồi, cứ xoá.

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Đây là chương **lập trường gắt bị làm dịu đi nhiều nhất** theo thời gian. Năm 2026, cộng đồng phần lớn *không* còn coi "mọi comment là thất bại".
> - **"Comment luôn là thất bại" (tr. 54) — bị phản bác rộng rãi.** Phân biệt quan trọng mà sách nói lướt: comment giải thích *cái gì*/*thế nào* thường là mùi (nên thay bằng tên tốt), nhưng comment giải thích ***vì sao*** (một quyết định, một ràng buộc nghiệp vụ, một cái bẫy đã gặp) thì code **không** diễn đạt được. Jeff Atwood, và nhiều bài "In Defense of Comments", đứng về phía này. Chính Uncle Bob cũng để ngỏ ở loại "giải thích ý định" và "cảnh báo hậu quả" — đó mới là comment-vì-sao.
> - **Docstring/JSDoc/TSDoc cho API công khai**: năm 2026 là chuẩn mực, không phải rác — chúng nuôi IntelliSense, sinh tài liệu tự động, và được kiểm bằng công cụ. Lời cảnh báo của sách (javadoc cũng nói dối được) vẫn đúng, nhưng cán cân đã nghiêng về "có vẫn hơn".
> - **"Code bị comment lại thì xoá đi"**: còn đúng nguyên và nay *mạnh hơn* — Git phổ cập tuyệt đối, không còn lý do giữ code chết.
> - **Cái mới sau 2008**: comment giờ còn là *đầu vào cho AI*. Copilot/Cursor đọc comment-vì-sao và docstring để sinh code đúng ý hơn. Một comment "vì sao" tốt giờ phục vụ cả người lẫn máy.
> - **Vẫn vàng**: đừng comment để cứu code tồi (hãy dọn), comment thừa/gây hiểu lầm là nợ, và sự thật nằm ở code.

## 7. Áp dụng vào codebase của bạn

> [!question] Áp dụng vào codebase của bạn
> 1. **Phân loại comment-cái-gì vs comment-vì-sao.** Mở một file bạn đang làm, đọc từng comment và dán nhãn: cái này giải thích *cái gì* (ứng viên xoá, thay bằng tên tốt) hay *vì sao* (giữ lại)?
> 2. **Biến một comment thành hàm.** Tìm một comment đứng ngay trên một điều kiện hay một khối (`// nếu user đủ điều kiện...`). Rút khối đó thành hàm tên đúng như comment. Xoá comment.
> 3. **Săn code bị comment lại.** `grep` những dòng code bị `//` hoặc `/* */` bao quanh. Chúng ra đời bao lâu rồi? Xoá, tin vào Git.
> 4. **Tìm một comment nói dối.** Tìm một comment mà code bên dưới đã đổi khác. Đó là bằng chứng sống cho "comment nói dối" — sửa hoặc xoá.

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Necessary evil** | "Cái tốt cần thiết" — comment đẹp nhất cũng chỉ bù cho thất bại diễn đạt bằng code (tr. 54). |
| **Comment-vì-sao vs comment-cái-gì** | Phân biệt (của 2026): *vì sao* thường đáng giữ; *cái gì/thế nào* nên thay bằng tên tốt. |
| **Mumbling comment** | Comment nhét vào cho có, không truyền đạt được gì (tr. 59–60). |
| **Redundant comment** | Comment nói lại y code, dài hơn và kém chính xác hơn code (tr. 60–61). |
| **Misleading comment** | Comment sai tinh vi, khiến người đọc hiểu nhầm hành vi (tr. 63). |
| **Mandated comment** | Comment do quy tắc "mọi hàm phải có javadoc" bắt buộc → rác (tr. 63). |
| **Commented-out code** | Code bị tắt bằng comment; nên xoá, tin vào version control. |

## 9. Câu hỏi tự kiểm tra

1. Vì sao Uncle Bob gọi comment là "necessary evil" và nói chúng "luôn nói dối"? *(tr. 54)*
2. "Comment tốt nhất là comment bạn tìm cách để không viết" nghĩa là gì trong thực hành? *(tr. 55)*
3. Kể ba loại comment *tốt* và ba loại comment *tồi* mà chương nêu. *(tr. 55–63)*
4. Phân biệt comment-*cái gì* với comment-*vì sao*. Vì sao 2026 giữ loại sau? *(Đối chiếu 2026)*
5. Vì sao "code bị comment lại" nên xoá, và vì sao lời khuyên này *mạnh hơn* vào năm 2026?

## Tóm tắt một trang

```
BÀI 3 — COMMENT: "CÁI TỐT CẦN THIẾT", KHÔNG HƠN
─────────────────────────────────────────────────────────
LẬP TRƯỜNG  "đừng comment code tồi — viết lại nó" (Kernighan,
            tr.53). Comment = bù cho thất bại diễn đạt (tr.54).
            Sự thật chỉ nằm ở CODE (tr.54).

ĐỪNG        comment để cứu code rối → hãy DỌN (tr.55).
CÁCH DỌN    biến comment thành một hàm có tên:
            // check eligible...  →  isEligibleForFullBenefits()

COMMENT TỐT (hiếm): pháp lý · thông tin · GIẢI THÍCH Ý ĐỊNH ·
            làm rõ API ngoài · CẢNH BÁO HẬU QUẢ · TODO · javadoc API
COMMENT TỒI (đa số): lẩm bẩm · thừa · gây hiểu lầm · bị bắt buộc ·
            nhật ký/nhiễu · CODE BỊ COMMENT LẠI (xoá đi!)

2026   Lập trường "mọi comment là thất bại" ĐƯỢC LÀM DỊU.
       Tách: comment-CÁI-GÌ (mùi) vs comment-VÌ-SAO (giữ).
       JSDoc/TSDoc cho API = chuẩn, nuôi IntelliSense + AI.
       Vẫn vàng: dọn thay vì comment; xoá code chết.
```

## Nguồn

- **Robert C. Martin**, *Clean Code* (Prentice Hall, 2008) — **Chương 4, "Comments"** (`tr. 53–74`): đề từ Kernighan, comment là "necessary evil", "luôn là thất bại", nói dối, sự thật ở code (tr. 53–54); comment không cứu code tồi (tr. 55); giải thích bằng code, `isEligibleForFullBenefits` (tr. 55); comment tốt — pháp lý, thông tin, ý định, làm rõ, cảnh báo, TODO, khuếch đại, javadoc (tr. 55–59); comment tồi — lẩm bẩm, thừa, gây hiểu lầm, bắt buộc (tr. 59–63), và tiếp đó journal/noise/commented-out code (tr. 63–74). `tai_lieu/Clean.Code.2008.8.pdf`
- Phản biện 2026 dẫn từ ngoài sách: Jeff Atwood *"Coding Without Comments"* / *"When Good Comments Go Bad"*; loạt bài *"In Defense of Comments"*; chuẩn JSDoc/TSDoc.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 31`.

---

**Bản đồ khoá học:** [Bài 0 — Clean Code là gì](bai_00_clean_code_la_gi.md) · [Bài 1 — Đặt tên](bai_01_dat_ten.md) · [Bài 2 — Hàm](bai_02_ham.md) · [Bài 3 ← bạn đang ở đây] · [Bài 4 — Định dạng](bai_04_dinh_dang.md) · [Bài 5 — Object & dữ liệu](bai_05_object_va_du_lieu.md) · [Bài 6 — Xử lý lỗi](bai_06_xu_ly_loi.md) · [Bài 7 — Ranh giới](bai_07_ranh_gioi.md) · [Bài 8 — Unit test](bai_08_unit_test.md) · [Bài 9 — Class](bai_09_class.md) · [Bài 10 — Hệ thống](bai_10_he_thong.md) · [Bài 11 — Thiết kế nổi lên](bai_11_thiet_ke_noi_len.md) · [Bài 12 — Concurrency](bai_12_concurrency.md) · [Bài 13 — Xem code sạch nảy sinh](bai_13_xem_code_nay_sinh.md) · [Bài 14 — Refactor ngoài đời](bai_14_refactor_ngoai_doi.md) · [Bài 15 — Danh mục mùi code](bai_15_danh_muc_mui_code.md)

Xem thêm [README khoá học](../README.md).
