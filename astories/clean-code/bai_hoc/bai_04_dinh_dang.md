# Bài 4 — Định dạng: code là để nói với con người

> [!info] Về bài này
> Dựng từ **Chương 5 — "Formatting"** của *Clean Code* (Robert C. Martin, 2008 — `tai_lieu/`, `tr. 75–92`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 31`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Mạch bài: *code lộn xộn → gọi tên vấn đề → bản sạch (TypeScript, chạy được) → nguyên tắc → đối chiếu 2026 → áp dụng*.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: định dạng là giao tiếp](#1-mở-đầu-định-dạng-là-giao-tiếp)
2. [Định dạng dọc: ẩn dụ tờ báo](#2-định-dạng-dọc-ẩn-dụ-tờ-báo)
3. [Code minh hoạ: máy không quan tâm định dạng](#3-code-minh-hoạ-máy-không-quan-tâm-định-dạng)
4. [Khoảng cách dọc: khai báo gần nơi dùng, hàm gọi gần hàm bị gọi](#4-khoảng-cách-dọc-khai-báo-gần-nơi-dùng-hàm-gọi-gần-hàm-bị-gọi)
5. [Định dạng ngang và thụt lề](#5-định-dạng-ngang-và-thụt-lề)
6. [Luật của đội](#6-luật-của-đội)
7. [Đối chiếu 2026](#7-đối-chiếu-2026)
8. [Áp dụng vào codebase của bạn](#8-áp-dụng-vào-codebase-của-bạn)
9. [Từ điển thuật ngữ](#9-từ-điển-thuật-ngữ)
10. [Câu hỏi tự kiểm tra](#10-câu-hỏi-tự-kiểm-tra)
11. [Tóm tắt một trang](#tóm-tắt-một-trang)
12. [Nguồn](#nguồn)

---

## 1. Mở đầu: định dạng là giao tiếp

Khi ai đó mở "nắp ca-pô" code của bạn, ta muốn họ trầm trồ về sự ngăn nắp, nhất quán, chú ý đến từng chi tiết — muốn họ thấy *có người chuyên nghiệp đã làm việc ở đây*. Nếu thay vào đó họ thấy một mớ như "do một đám thuỷ thủ say viết", họ sẽ kết luận cái sự cẩu thả ấy thấm vào mọi ngóc ngách khác của dự án.

> [!quote] Ch. 5 — The Purpose of Formatting (tr. 76)
> "Code formatting is about communication, and communication is the professional developer's first order of business."
>
> *Định dạng code là chuyện **giao tiếp**, và giao tiếp là việc hệ trọng hàng đầu của một lập trình viên chuyên nghiệp.*

Bạn có thể tưởng "chạy được" mới là việc hàng đầu. Uncle Bob bác lại: tính năng hôm nay nhiều khả năng đổi ở bản sau, nhưng *tính đọc được* thì ảnh hưởng tới mọi thay đổi về sau. Thậm chí:

> [!quote] Ch. 5 — The Purpose of Formatting (tr. 76)
> "Your style and discipline survives, even though your code does not."
>
> *Phong cách và kỷ luật của bạn sống sót, ngay cả khi code của bạn thì không.*

## 2. Định dạng dọc: ẩn dụ tờ báo

Một file nguồn nên đọc như một bài báo viết khéo: tên (tiêu đề) đơn giản mà đủ nói ta có đang ở đúng chỗ không; phần trên cùng là khái niệm và thuật toán mức cao; càng xuống dưới chi tiết càng tăng, tới cuối là những hàm cấp thấp nhất. Giữa các khái niệm nên có **dòng trống** như khoảng ngắt giữa các ý; các dòng liên quan mật thiết thì nên **đặc** (gần nhau, không chen comment vô bổ vào giữa). Uncle Bob đo thực tế: FitNesse ~50.000 dòng vẫn dựng từ các file điển hình ~200 dòng, hiếm khi quá 500 — "file nhỏ thường dễ hiểu hơn file to".

## 3. Code minh hoạ: máy không quan tâm định dạng

Điểm cốt lõi của chương: định dạng **không** đổi hành vi — nó nói với *con người*. Cùng một hàm, dồn một dòng và trình bày sạch, máy chạy y hệt:

```typescript
import { strict as assert } from "node:assert";

// cùng một hàm, hai cách trình bày — máy chạy y hệt, người đọc thì không

// bản dồn một dòng (máy không phàn nàn)
function sumEvenSquaresDense(xs:number[]){let s=0;for(const x of xs){if(x%2===0){s+=x*x;}}return s;}

// bản thoáng: thụt lề theo cấp, giãn dòng theo khái niệm
function sumEvenSquaresClean(numbers: number[]): number {
  let sum = 0;
  for (const n of numbers) {
    if (n % 2 === 0) {
      sum += n * n;
    }
  }
  return sum;
}

const data = [1, 2, 3, 4, 5, 6];
assert.equal(sumEvenSquaresDense(data), sumEvenSquaresClean(data));
console.log("bản dồn một dòng :", sumEvenSquaresDense(data));
console.log("bản trình bày sạch:", sumEvenSquaresClean(data));
console.log("máy cho cùng kết quả — định dạng là nói với CON NGƯỜI, không phải máy.");
```

Kết quả chạy thật:

```
bản dồn một dòng : 56
bản trình bày sạch: 56
máy cho cùng kết quả — định dạng là nói với CON NGƯỜI, không phải máy.
```

Hai hàm cho cùng `56`. Trình biên dịch/Node không phân biệt. Khác biệt duy nhất là *con người đọc*: bản `Dense` buộc bạn giải mã một dòng đặc nghẹt, còn bản `Clean` để mắt lướt qua từng cấp. Vì định dạng chỉ phục vụ người đọc, nó là thứ nên **giao hẳn cho công cụ** (xem Đối chiếu 2026).

> [!note] Tự thử
> 1. Thêm một điều kiện nữa vào cả hai hàm (ví dụ bỏ qua số chia hết cho 3). Bản nào bạn sửa mà không sợ sai dấu ngoặc?
> 2. Dán bản `Dense` vào trình format của editor (hoặc Prettier). Nó có biến thành đúng bản `Clean` không? Đó là lý do 2026 không còn tranh cãi chuyện này.
> 3. Thêm `sumEvenSquaresDense` một lỗi nhỏ (đổi `x*x` thành `x+x`). `assert` có bắt ngay không? So với việc dò lỗi trong một dòng đặc nghẹt.

## 4. Khoảng cách dọc: khai báo gần nơi dùng, hàm gọi gần hàm bị gọi

> [!quote] Ch. 5 — Vertical Distance (tr. 80)
> "Concepts that are closely related should be kept vertically close to each other."
>
> *Những khái niệm liên quan mật thiết nên được giữ gần nhau theo chiều dọc.*

Hệ quả cụ thể:

- **Biến khai báo gần nơi dùng.** Vì hàm nên ngắn, biến cục bộ thường nằm đầu hàm; biến điều khiển vòng lặp khai báo ngay trong câu lệnh lặp; biến thực thể (instance) khai báo ở đầu lớp — một chỗ ai cũng biết để tìm.
- **Hàm phụ thuộc đặt gần nhau.** Nếu hàm A gọi hàm B, hãy để chúng gần nhau theo chiều dọc, và nếu được, **hàm gọi nằm trên hàm bị gọi** — cho dòng chảy tự nhiên.

> [!quote] Ch. 5 — Vertical Distance (tr. 82)
> "If one function calls another, they should be vertically close, and the caller should be above the callee, if at all possible."
>
> *Nếu một hàm gọi một hàm khác, chúng nên gần nhau theo chiều dọc, và nếu có thể, hàm gọi nằm **bên trên** hàm bị gọi.*

Đây chính là hiện thân của *Stepdown Rule* ở [Bài 2 (Hàm)](bai_02_ham.md): đọc từ trên xuống, mỗi hàm giới thiệu hàm kế dưới.

## 5. Định dạng ngang và thụt lề

Về chiều ngang, Uncle Bob *từ bỏ* thói **căn lề thẳng cột** (xếp thẳng hàng tên biến/toán tử gán): nó kéo mắt đi sai chỗ (đọc tụt xuống cột tên mà quên nhìn kiểu), và công cụ format tự động thường xoá nó đi. Nếu một danh sách dài đến mức *thèm* căn cột, thì vấn đề là **danh sách quá dài** (lớp nên tách), chứ không phải thiếu căn.

Về thụt lề thì tuyệt đối không nhân nhượng:

> [!quote] Ch. 5 — Indentation (tr. 88)
> "Without indentation, programs would be virtually unreadable by humans."
>
> *Không có thụt lề, chương trình gần như không thể đọc nổi đối với con người.*

Và đừng phá thụt lề để nhét một `if`/`while`/hàm ngắn vào một dòng — hãy giãn ra. Với thân vòng lặp rỗng (*dummy scope*), hãy để dấu `;` xuống dòng riêng, có ngoặc, kẻo nó lẩn mất.

## 6. Luật của đội

> [!quote] Ch. 5 — Team Rules (tr. 90)
> "Every programmer has his own favorite formatting rules, but if he works in a team, then the team rules."
>
> *Lập trình viên nào cũng có bộ quy tắc định dạng ưa thích của riêng mình; nhưng khi làm trong một đội, thì **đội** định đoạt.*

(Chơi chữ: "the team rules" vừa là "luật của đội" vừa là "đội cai trị".) Cả đội thống nhất *một* phong cách và mọi người tuân theo — để phần mềm trông như do một trí tuệ nhất quán viết ra, không phải một đám cãi nhau. Tốt nhất là có công cụ tự áp dụng quy tắc đó.

## 7. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Đây là chương mà **năm 2026 gần như đã "giải quyết xong" bằng công cụ** — và đó đúng là điều Uncle Bob mong ("có công cụ tự động thì tốt").
> - **Tranh cãi định dạng gần như biến mất.** Các formatter quyết đoán — **Prettier** (JS/TS), **gofmt** (Go), **Black** (Python), **rustfmt** — áp một phong cách *duy nhất*, chạy tự động khi lưu file hoặc trong pre-commit hook/CI. "Luật của đội" (tr. 90) giờ là một file cấu hình được commit vào repo, không phải một cuộc họp. Tranh cãi tab-vs-space phần lớn đã chết.
> - **Căn lề thẳng cột**: Uncle Bob đã đúng trước thời đại — formatter hiện đại xoá nó đi, nên đừng phí công căn tay.
> - **Số liệu file ~200 dòng (tr. 77)** chỉ là "cảm giác", không phải luật. 2026 không nên bám con số; nhưng tinh thần "file nhỏ dễ hiểu hơn" vẫn đúng. Nhiều ngôn ngữ nay một file nhiều lớp/hàm nhỏ là chuyện thường.
> - **Ẩn dụ tờ báo & khoảng cách dọc**: còn nguyên giá trị, vì chúng nói về *thứ tự ý tưởng*, thứ mà formatter **không** làm thay được. Formatter sắp dấu cách; bạn vẫn phải tự quyết hàm nào đặt trên hàm nào.
> - **Hệ quả thực tế**: năm 2026, đừng tốn một giây review để bàn dấu cách — hãy cài formatter + linter, và dồn công sức review vào *cấu trúc* (thứ tự, khoảng cách dọc, kích thước file).

## 8. Áp dụng vào codebase của bạn

> [!question] Áp dụng vào codebase của bạn
> 1. **Kiểm tra tự động hoá.** Dự án bạn đã có formatter (Prettier/gofmt/Black…) chạy trong pre-commit hook hoặc CI chưa? Nếu chưa, cài nó — đây là "Boy Scout" mức đội, xoá sổ một loại tranh cãi vĩnh viễn.
> 2. **Đọc một file như đọc báo.** Mở một file lớn trong dự án. Phần mức-cao có nằm trên không? Chi tiết có tăng dần khi cuộn xuống không? Nếu không, thử sắp lại.
> 3. **Săn khoảng cách dọc tồi.** Tìm một hàm gọi một hàm khác ở *tận cuối* file. Kéo nó lại gần. Dễ theo dòng chảy hơn chứ?
> 4. **Đo một file.** File lớn nhất trong module bạn dài bao nhiêu dòng? Nó có đang làm quá nhiều việc để cần tách không? (Nối sang [Bài 9 (Class)](bai_09_class.md).)

## 9. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Newspaper metaphor** | File nên như bài báo: tên-tiêu-đề, mức cao ở trên, chi tiết tăng dần xuống dưới (tr. 77). |
| **Vertical openness** | Dòng trống ngăn giữa các khái niệm — tín hiệu thị giác cho "ý mới" (tr. 78). |
| **Vertical density** | Dòng liên quan mật thiết đặt sát nhau, không chen comment vô bổ (tr. 79). |
| **Vertical distance** | Khái niệm liên quan giữ gần nhau; biến gần nơi dùng; caller trên callee (tr. 80–83). |
| **Horizontal alignment** | Căn thẳng cột tên/toán tử — Uncle Bob *bỏ*, vì kéo mắt sai và bị formatter xoá (tr. 87–88). |
| **Team rules** | Cả đội thống nhất một phong cách; 2026 = file cấu hình formatter commit vào repo (tr. 90). |

## 10. Câu hỏi tự kiểm tra

1. Vì sao định dạng "quá quan trọng để bỏ qua, cũng quá quan trọng để sùng bái"? Việc hàng đầu của dev chuyên nghiệp là gì? *(tr. 76)*
2. Ẩn dụ tờ báo nói gì về cách sắp một file nguồn? *(tr. 77)*
3. Ba quy tắc "khoảng cách dọc" là gì? *(tr. 80–83)*
4. Vì sao Uncle Bob bỏ căn lề thẳng cột? *(tr. 87–88)*
5. "Team rules" nghĩa gì, và năm 2026 nó được hiện thực hoá bằng cái gì?

## Tóm tắt một trang

```
BÀI 4 — ĐỊNH DẠNG: CODE LÀ ĐỂ NÓI VỚI CON NGƯỜI
─────────────────────────────────────────────────────────
LÕI      Định dạng = GIAO TIẾP, việc hàng đầu của dev (tr.76).
         "Phong cách sống sót dù code thì không" (tr.76).

DỌC      Ẩn dụ tờ báo: tên-tiêu-đề, mức cao trên, chi tiết tăng
         dần xuống (tr.77). Dòng trống ngăn khái niệm; dòng
         liên quan đặt sát. File điển hình ~200 dòng.

KHOẢNG CÁCH  khái niệm liên quan → gần nhau (tr.80).
         biến gần nơi dùng; CALLER trên CALLEE (tr.82).

NGANG    bỏ căn lề thẳng cột (tr.87). Thụt lề là bắt buộc —
         "không thụt lề → không đọc nổi" (tr.88).

ĐỘI      "the team rules" (tr.90) — cả đội một phong cách.

MÁY KHÔNG QUAN TÂM: Dense vs Clean đều ra 56. Định dạng phục
         vụ NGƯỜI → giao cho công cụ.

2026     Prettier/gofmt/Black/rustfmt + pre-commit/CI đã GIẢI
         QUYẾT tranh cãi dấu cách. "Luật đội" = file cấu hình.
         Nhưng THỨ TỰ ý tưởng (ẩn dụ tờ báo) vẫn phải tự làm.
```

## Nguồn

- **Robert C. Martin**, *Clean Code* (Prentice Hall, 2008) — **Chương 5, "Formatting"** (`tr. 75–92`): ấn tượng về sự ngăn nắp (tr. 75–76); mục đích của định dạng = giao tiếp, "phong cách sống sót" (tr. 76); kích thước file, ẩn dụ tờ báo (tr. 76–78); khoảng trống dọc, mật độ dọc (tr. 78–80); khoảng cách dọc — biến gần nơi dùng, hàm phụ thuộc (tr. 80–84); định dạng ngang, bỏ căn cột, thụt lề, dummy scope (tr. 87–90); luật của đội (tr. 90–92). `tai_lieu/Clean.Code.2008.8.pdf`
- Bối cảnh 2026 dẫn từ ngoài sách: Prettier, gofmt, Black, rustfmt; pre-commit hook; EditorConfig.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 31`.

---

**Bản đồ khoá học:** [Bài 0 — Clean Code là gì](bai_00_clean_code_la_gi.md) · [Bài 1 — Đặt tên](bai_01_dat_ten.md) · [Bài 2 — Hàm](bai_02_ham.md) · [Bài 3 — Comment](bai_03_comment.md) · [Bài 4 ← bạn đang ở đây] · [Bài 5 — Object & dữ liệu](bai_05_object_va_du_lieu.md) · [Bài 6 — Xử lý lỗi](bai_06_xu_ly_loi.md) · [Bài 7 — Ranh giới](bai_07_ranh_gioi.md) · [Bài 8 — Unit test](bai_08_unit_test.md) · [Bài 9 — Class](bai_09_class.md) · [Bài 10 — Hệ thống](bai_10_he_thong.md) · [Bài 11 — Thiết kế nổi lên](bai_11_thiet_ke_noi_len.md) · [Bài 12 — Concurrency](bai_12_concurrency.md) · [Bài 13 — Xem code sạch nảy sinh](bai_13_xem_code_nay_sinh.md) · [Bài 14 — Refactor ngoài đời](bai_14_refactor_ngoai_doi.md) · [Bài 15 — Danh mục mùi code](bai_15_danh_muc_mui_code.md)

Xem thêm [README khoá học](../README.md).
