# Bài 0 — Clean Code là gì? "There will be code"

> [!info] Về bài này
> Dựng từ **Chương 1 — "Clean Code"** của *Clean Code: A Handbook of Agile Software Craftsmanship* (Robert C. Martin — "Uncle Bob", Prentice Hall, 2008 — `tai_lieu/`, `tr. 1–15`).
> Trích nguồn theo `Ch. N` (chương) và `tr. X` (số trang **in trong sách**; muốn tra tệp PDF thì cộng 31 → PDF = `tr. + 31`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn ngay dưới — vì nguồn là tiếng Anh.
> Đây là khoá **code-first**: từ Bài 1 trở đi mỗi bài đi theo mạch *code bẩn → gọi tên "mùi" → bản sạch (TypeScript, chạy được) → nguyên tắc → đối chiếu 2026 → áp dụng vào codebase của bạn*. Bài 0 này đặt nền: *thế nào là code sạch, và vì sao đáng để bận tâm*.
>
> **Chạy code:** cần **Node 22.6+** (Node chạy thẳng `.ts`, tự bỏ phần kiểu). Lưu file rồi gõ `node <tên-file>.ts`. Không cần cài gói, không `tsc`, không `tsconfig.json`.

## Mục lục

1. [Mở đầu: killer app chết vì code bẩn](#1-mở-đầu-killer-app-chết-vì-code-bẩn)
2. [Cái giá thật của việc sống chung với mớ hỗn độn](#2-cái-giá-thật-của-việc-sống-chung-với-mớ-hỗn-độn)
3. [Code minh hoạ: cùng một phép tính, hai cách viết](#3-code-minh-hoạ-cùng-một-phép-tính-hai-cách-viết)
4. [Clean code là gì? — hỏi chính những bậc thầy](#4-clean-code-là-gì--hỏi-chính-những-bậc-thầy)
5. [Quy tắc Hướng đạo sinh và tỉ lệ đọc:viết 10:1](#5-quy-tắc-hướng-đạo-sinh-và-tỉ-lệ-đọcviết-101)
6. [Đối chiếu 2026: một cuốn sách gây tranh cãi](#6-đối-chiếu-2026-một-cuốn-sách-gây-tranh-cãi)
7. [Áp dụng vào codebase của bạn](#7-áp-dụng-vào-codebase-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mở đầu: killer app chết vì code bẩn

Uncle Bob mở sách không bằng một định nghĩa, mà bằng một đám tang. Cuối thập niên 80, một công ty viết ra một *killer app* — phần mềm ai cũng mua, ai cũng dùng. Rồi vòng release cứ dài dần ra. Bug từ bản này sót sang bản kia. Thời gian tải phình to, app crash nhiều thêm. Có một ngày, chính Uncle Bob tắt hẳn sản phẩm trong cơn bực, không bao giờ mở lại. Ít lâu sau công ty đóng cửa.

Hai thập niên sau ông gặp lại một nhân viên đời đầu của công ty đó và hỏi chuyện gì đã xảy ra:

> [!quote] Ch. 1 — Bad Code (tr. 4)
> "They had rushed the product to market and had made a huge mess in the code. As they added more and more features, the code got worse and worse until they simply could not manage it any longer. It was the bad code that brought the company down."
>
> *Họ ép sản phẩm ra thị trường quá gấp và để lại một mớ hỗn độn trong code. Càng thêm tính năng, code càng tệ, tới mức không còn quản nổi nữa. Chính code bẩn đã quật ngã công ty.*

Ai làm nghề này cũng từng bị code bẩn cản bước. Uncle Bob đặt cho nó một cái tên: **wading** — lội. Ta lội qua một đầm lầy gai góc chằng chịt, dò dẫm tìm đường, mong vớ được một manh mối nào đó, nhưng chỉ thấy thêm code vô nghĩa. Và rồi ông hỏi ngược một câu khó chịu: *bạn từng bị code bẩn cản bước — vậy thì sao chính bạn vẫn viết ra nó?* Vì vội. Vì sếp sẽ cằn nhằn nếu bạn dừng lại dọn. Vì bạn chán cái module này rồi và chỉ muốn cho nó xong. Rồi tự nhủ sẽ quay lại dọn sau — mà quên mất **định luật LeBlanc**:

> [!quote] Ch. 1 — Bad Code (tr. 4)
> "Later equals never."
>
> *Để sau tức là không bao giờ.*

## 2. Cái giá thật của việc sống chung với mớ hỗn độn

Chuyện trên không phải xui rủi cá biệt. Nó là một **đường cong năng suất** mà Uncle Bob vẽ ra: nhóm khởi đầu phóng rất nhanh, nhưng qua một hai năm, mỗi thay đổi lại làm gãy hai ba chỗ khác; không sửa nào còn là nhỏ nữa; năng suất tụt dần về gần số 0. Quản lý thấy vậy làm điều duy nhất họ nghĩ ra: **thêm người**. Nhưng người mới không hiểu thiết kế, lại càng chất thêm hỗn độn, đẩy năng suất xuống sâu hơn.

Cái kết quen thuộc là **"cuộc đại tái thiết trên mây"** (*the grand redesign in the sky*): đội nổi loạn, đòi viết lại từ đầu. Một "tiger team" tinh nhuệ được lập ra để dựng hệ mới làm được mọi thứ hệ cũ làm — trong khi vẫn phải đuổi theo các thay đổi của hệ cũ. Cuộc đua đó có thể kéo *mười năm*. Tới lúc xong, thành viên tiger team ban đầu đã rời đi, còn người ở lại thì lại đòi viết lại cái hệ "mới" vì nó cũng đã thành một mớ hỗn độn.

Vậy nên giữ code sạch không phải chuyện làm đẹp — nó là chuyện sống còn. Và đây là nghịch lý mà Uncle Bob muốn đập tan:

> [!quote] Ch. 1 — The Primal Conundrum (tr. 6)
> "The only way to make the deadline—the only way to go fast—is to keep the code as clean as possible at all times."
>
> *Cách duy nhất để kịp deadline — cách duy nhất để đi nhanh — là giữ code sạch nhất có thể, mọi lúc.*

Lập trình viên nào có vài năm nghề cũng biết mớ hỗn độn trước đó làm mình chậm lại. Nhưng ai cũng chịu áp lực tạo ra mớ hỗn độn mới để kịp hạn. Người chuyên nghiệp hiểu rằng vế sau là sai: bạn **không** kịp deadline bằng cách bày bừa — mớ bừa bộn làm bạn chậm lại *ngay lập tức*, và khiến bạn trễ hạn.

## 3. Code minh hoạ: cùng một phép tính, hai cách viết

Trước khi nghe các bậc thầy định nghĩa "sạch", hãy thấy tận mắt cái khác biệt mà mọi chương sau sẽ mổ xẻ. Hai hàm dưới đây cho **cùng một con số**, nhưng chỉ một hàm đọc được mà không phải giải mã trong đầu:

```typescript
import { strict as assert } from "node:assert";

// --- Bản "bẩn": đọc được không? ---
function m(l: number[][]): number {
  let t = 0;
  for (let i = 0; i < l.length; i++)
    if (l[i][0] === 1) t += l[i][1] * l[i][2];
  return t;
}

// --- Bản "sạch": cùng phép tính, nhưng đọc như văn xuôi ---
const PAID = 1;
type OrderLine = { status: number; quantity: number; unitPrice: number };

function totalOfPaidOrders(lines: OrderLine[]): number {
  return lines
    .filter((line) => line.status === PAID)
    .reduce((sum, line) => sum + line.quantity * line.unitPrice, 0);
}

const rawLines = [
  [1, 2, 50],
  [0, 9, 10],
  [1, 1, 30],
];
const orderLines: OrderLine[] = rawLines.map(
  ([status, quantity, unitPrice]) => ({ status, quantity, unitPrice }),
);

const fromDirty = m(rawLines);
const fromClean = totalOfPaidOrders(orderLines);

assert.equal(fromDirty, fromClean); // cùng một kết quả
console.log("bản bẩn   m(l)              =", fromDirty);
console.log("bản sạch  totalOfPaidOrders =", fromClean);
console.log("hai hàm cho cùng một số:", fromDirty === fromClean);
console.log("nhưng chỉ một hàm đọc được mà không phải giải mã.");
```

Kết quả chạy thật:

```
bản bẩn   m(l)              = 130
bản sạch  totalOfPaidOrders = 130
hai hàm cho cùng một số: true
nhưng chỉ một hàm đọc được mà không phải giải mã.
```

Hàm `m` không sai — nó chạy đúng. Nhưng để hiểu nó làm gì, bạn phải tự giải mã: `l[i][0] === 1` nghĩa là gì? `1` là trạng thái nào? `l[i][1] * l[i][2]` là tích của hai thứ gì? Mọi tri thức ấy nằm trong đầu người viết, không nằm trong code. Bản `totalOfPaidOrders` nói thẳng ý định: *tổng của những đơn đã thanh toán*. Cả cuốn sách này, rút gọn lại, là tập hợp những kỹ thuật để biến `m` thành `totalOfPaidOrders`.

> [!note] Tự thử
> 1. Thêm một dòng đơn `PAID` nữa vào cả `rawLines` lẫn `orderLines`, chạy lại, xem hai hàm có còn khớp không.
> 2. Trong `m`, đổi `l[i][0] === 1` thành `=== 0`. Giờ `m` tính gì? Phải mất bao lâu bạn mới trả lời được — so với việc đọc tên hàm ở bản sạch?
> 3. Thử xoá dòng `assert.equal(...)` rồi cố tình làm hai hàm lệch nhau. Không có `assert`, bạn phát hiện ra bằng cách nào?

## 4. Clean code là gì? — hỏi chính những bậc thầy

Uncle Bob không tự tiện định nghĩa. Ông đi hỏi những lập trình viên lừng danh. Mỗi người soi "code sạch" từ một góc — gộp lại thành bộ tiêu chí mà cả khoá sẽ triển khai.

**Bjarne Stroustrup** (cha đẻ C++) nhấn vào *sự thanh thoát* và *làm một việc*:

> [!quote] Ch. 1 — What Is Clean Code? (tr. 7)
> "I like my code to be elegant and efficient. The logic should be straightforward to make it hard for bugs to hide […] Clean code does one thing well."
>
> *Tôi thích code của mình thanh thoát và hiệu quả. Logic phải rành mạch để bug khó mà ẩn nấp […] Code sạch làm tốt một việc.*

**Grady Booch** (tác giả *Object Oriented Analysis and Design*) nhấn vào *tính đọc được*:

> [!quote] Ch. 1 — What Is Clean Code? (tr. 8)
> "Clean code is simple and direct. Clean code reads like well-written prose."
>
> *Code sạch thì giản dị và thẳng thắn. Code sạch đọc như một áng văn xuôi được viết khéo.*

**"Big" Dave Thomas** (sáng lập OTI) buộc code sạch vào *test* — một điều mười năm trước 2008 còn gây giật mình:

> [!quote] Ch. 1 — What Is Clean Code? (tr. 9)
> "Clean code can be read, and enhanced by a developer other than its original author. It has unit and acceptance tests. […] It provides one way rather than many ways for doing one thing."
>
> *Code sạch có thể được một lập trình viên khác — không phải tác giả gốc — đọc và mở rộng. Nó có unit test và acceptance test. […] Nó cho một cách làm một việc, thay vì nhiều cách.*

**Michael Feathers** (tác giả *Working Effectively with Legacy Code*) rút tất cả về một chữ:

> [!quote] Ch. 1 — What Is Clean Code? (tr. 10)
> "Clean code always looks like it was written by someone who cares."
>
> *Code sạch trông luôn như được viết bởi một người có để tâm.*

**Ron Jeffries** nhắc lại bốn *quy tắc code đơn giản* của Kent Beck — mà bạn sẽ gặp lại nguyên vẹn ở [Bài 11 (Thiết kế nổi lên)](bai_11_thiet_ke_noi_len.md):

> [!quote] Ch. 1 — What Is Clean Code? (tr. 10)
> "In priority order, simple code: • Runs all the tests; • Contains no duplication; • Expresses all the design ideas that are in the system; • Minimizes the number of entities such as classes, methods, functions, and the like."
>
> *Theo thứ tự ưu tiên, code đơn giản: chạy qua mọi test; không trùng lặp; diễn đạt hết mọi ý tưởng thiết kế trong hệ thống; tối thiểu số thực thể như class, method, function…*

**Ward Cunningham** (cha đẻ Wiki) cho một thước đo gần như thiền:

> [!quote] Ch. 1 — What Is Clean Code? (tr. 11)
> "You know you are working on clean code when each routine you read turns out to be pretty much what you expected."
>
> *Bạn biết mình đang làm việc với code sạch khi mỗi hàm bạn đọc hoá ra đúng gần như những gì bạn đã đoán.*

Gộp lại, "sạch" trong khoá này nghĩa là: **đọc như văn xuôi, làm một việc, không trùng lặp, nói rõ ý định, có test bọc, và được viết bởi một người có để tâm.** Đó là sợi chỉ xuyên suốt 15 bài tiếp theo.

## 5. Quy tắc Hướng đạo sinh và tỉ lệ đọc:viết 10:1

Vì sao đọc được lại quan trọng đến thế? Vì ta đọc code nhiều hơn viết — nhiều hơn rất nhiều:

> [!quote] Ch. 1 — We Are Authors (tr. 14)
> "the ratio of time spent reading vs. writing is well over 10:1. We are constantly reading old code as part of the effort to write new code."
>
> *tỉ lệ thời gian đọc so với viết là hơn 10:1. Ta liên tục đọc code cũ như một phần của việc viết code mới.*

Đã đọc nhiều hơn viết như vậy, thì làm code dễ đọc — dù phải viết cực hơn — rốt cuộc lại khiến việc viết dễ hơn. Và không chỉ viết sạch một lần là xong; code phải được giữ sạch theo thời gian. Uncle Bob mượn một quy tắc của Hướng đạo sinh Mỹ:

> [!quote] Ch. 1 — The Boy Scout Rule (tr. 14)
> "Leave the campground cleaner than you found it."
>
> *Hãy để lại khu cắm trại sạch hơn lúc bạn đến.*

Dọn không cần to tát: đổi một cái tên biến cho rõ hơn, tách một hàm hơi dài, xoá một mẩu trùng lặp, gột một câu `if` rối. Nếu mỗi lần check-in ta để code sạch hơn lúc check-out một chút, code đơn giản là **không thể mục ruỗng**.

## 6. Đối chiếu 2026: một cuốn sách gây tranh cãi

Đây là điểm khác lớn nhất giữa khoá này và một bản tóm tắt sách thông thường: *Clean Code* năm 2026 là cuốn **vừa kinh điển vừa bị cãi dữ dội**. Và điều đáng nói là chính Uncle Bob đã mời bạn cãi:

> [!quote] Ch. 1 — Schools of Thought (tr. 13)
> "Indeed, many of the recommendations in this book are controversial. You will probably not agree with all of them. You might violently disagree with some of them. That's fine. We can't claim final authority."
>
> *Thật vậy, nhiều khuyến nghị trong sách này gây tranh cãi. Hẳn bạn sẽ không đồng ý với tất cả. Có cái bạn có thể phản đối kịch liệt. Không sao. Chúng tôi không dám nhận mình là chân lý cuối cùng.*

Ông còn ví sách như **một "trường phái"** (Object Mentor School of Clean Code), giống các võ đường — đúng trong khuôn khổ của nó, nhưng không phủ định các trường phái khác. Khoá này giữ đúng tinh thần đó. Vì vậy từ Bài 1, mỗi nguyên tắc đều kèm một mục **`[!warning] Đối chiếu 2026`** tách phần *còn đúng* khỏi phần *đã lỗi hoặc đang bị phản biện*. Vài mặt trận nóng nhất bạn sẽ gặp:

> [!warning] Đối chiếu 2026 — những chỗ sẽ bị cãi
> - **"Hàm phải thật nhỏ" (Ch.3)** — lời khuyên hàm chỉ 3–4 dòng, tách hàm liên tục, bị phê là đẻ ra quá nhiều *gián tiếp*: để hiểu một việc phải nhảy qua chục hàm con. ([Bài 2](bai_02_ham.md) sẽ mổ.)
> - **"Clean Code, Horrible Performance" (Casey Muratori, 2023)** — phong trào *data-oriented design* chỉ ra rằng lời khuyên đa hình/đóng gói kiểu OOP ở [Bài 5 (Object & dữ liệu)](bai_05_object_va_du_lieu.md) và danh mục Ch.17 có thể khiến code chậm đi nhiều lần trên phần cứng hiện đại.
> - **"Comment là thất bại" (Ch.4)** — năm 2026 ta rộng lượng hơn với comment giải thích *vì sao*, với docstring, với ADR. ([Bài 3](bai_03_comment.md))
> - **Chính ví dụ của sách** — đoạn `SetupTeardownIncluder` ở Ch.15 thường bị lấy làm ví dụ ngược: tách nhỏ tới mức *khó đọc hơn*. ([Bài 14](bai_14_refactor_ngoai_doi.md))
> - **"Đừng trả null" (Ch.7)** vs kiểu `Result`/`Option` và `strictNullChecks` của TypeScript ngày nay. ([Bài 6](bai_06_xu_ly_loi.md))
>
> Mục tiêu không phải "bắt lỗi Uncle Bob", mà là học cách một thợ lành nghề đọc một tác phẩm kinh điển: **lấy nguyên tắc còn sống, hiểu bối cảnh của phần đã cũ, và biết khi nào thì bẻ luật.**

## 7. Áp dụng vào codebase của bạn

> [!question] Ba việc trước khi sang Bài 1
> 1. **Tìm một hàm `m` của chính bạn.** Mở codebase bạn đang làm, tìm một hàm mà sáu tháng nữa *người khác* (hoặc chính bạn) sẽ phải giải mã. Dán nó vào một file nháp — cuối khoá bạn sẽ quay lại refactor nó.
> 2. **Đo "định luật LeBlanc" trong dự án của bạn.** Tìm một chỗ trong code có comment kiểu `// TODO`, `// fix later`, `// hack`. Nó ra đời bao lâu rồi? "Later" đã thành "never" chưa?
> 3. **Chọn thước đo "sạch" của riêng bạn.** Trong sáu tiêu chí ở mục 4 (đọc được, làm một việc, không trùng lặp, rõ ý định, có test, có để tâm), đâu là điểm yếu nhất của codebase hiện tại của bạn? Ghi lại — đó là bài học bạn nên đọc kỹ nhất.

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Clean code** | Code đọc như văn xuôi, làm một việc, không trùng lặp, rõ ý định, có test bọc — chủ đề trung tâm cả sách (tr. 7–11). |
| **Wading** ("lội") | Phải dò dẫm vật lộn qua code bẩn để hiểu nó làm gì (tr. 4). |
| **LeBlanc's law** | "Later equals never" — cái gì định dọn "sau" thì thường không bao giờ dọn (tr. 4). |
| **The grand redesign in the sky** | Ảo tưởng "viết lại từ đầu sẽ sạch" — thường lặp lại đúng mớ hỗn độn cũ (tr. 5). |
| **Boy Scout Rule** | Để lại code sạch hơn lúc bạn chạm vào, mỗi lần check-in (tr. 14). |
| **Code-sense** | "Giác quan code" — khả năng nhìn một mớ hỗn độn và thấy ngay chuỗi phép biến đổi để gột sạch nó (tr. 7). |
| **Đối chiếu 2026** | Mục cố định của khoá: tách *nguyên tắc còn đúng* khỏi *phần đã lỗi/đang bị phản biện* trong lời Uncle Bob. |

## 9. Câu hỏi tự kiểm tra

1. Uncle Bob mở sách bằng câu chuyện công ty nào, và nó minh hoạ điều gì về code bẩn?
2. Phát biểu "định luật LeBlanc" và cho một ví dụ trong codebase của bạn. *(gợi ý: tr. 4)*
3. Vì sao Uncle Bob nói "cách duy nhất để đi nhanh là giữ code sạch"? Nghịch lý ông đập tan là gì? *(tr. 6)*
4. Nêu ba trong sáu tiêu chí "code sạch" mà các bậc thầy đưa ra, kèm tên người nói. *(tr. 7–11)*
5. Tỉ lệ đọc:viết code là bao nhiêu, và nó dẫn tới kết luận gì về cách viết? *(tr. 14)*
6. Kể một khuyến nghị của sách mà năm 2026 đang bị phản biện — và lập luận phản biện đó là gì?

## Tóm tắt một trang

```
BÀI 0 — CLEAN CODE LÀ GÌ? "THERE WILL BE CODE"
─────────────────────────────────────────────────────────
LUẬN ĐỀ   Code sẽ không bao giờ biến mất (tr. 2). Đã có code
          thì có code sạch và code bẩn — và khác biệt đó
          quyết định sống còn của cả sản phẩm.

CÁI GIÁ   Code bẩn → năng suất tụt dần về 0 → "đại tái thiết
          trên mây" → 10 năm sau lại một mớ hỗn độn mới.
          Định luật LeBlanc: "Later equals never" (tr. 4).

NGHỊCH LÝ Cách DUY NHẤT để đi nhanh = giữ code sạch mọi lúc
          (tr. 6). Bày bừa KHÔNG giúp kịp deadline.

SẠCH LÀ GÌ (tr. 7–11)
   Bjarne   : làm tốt một việc, logic rành mạch
   Booch    : đọc như văn xuôi
   Big Dave : có unit + acceptance test; một cách làm một việc
   Feathers : trông như người có để tâm viết ra
   Beck/Ron : chạy test · không trùng lặp · rõ ý · ít thực thể
   Ward     : mỗi hàm đúng như bạn đoán

GIỮ SẠCH  Đọc:viết > 10:1 (tr. 14) → viết cho dễ đọc.
          Quy tắc Hướng đạo: để lại sạch hơn lúc đến (tr. 14).

2026      Sách VỪA kinh điển VỪA bị cãi — và chính Uncle Bob
          mời bạn cãi (tr. 13). Mặt trận nóng: hàm-quá-nhỏ,
          "Clean Code Horrible Performance", comment, null.
          Mỗi bài sau có mục ĐỐI CHIẾU 2026.
```

## Nguồn

- **Robert C. Martin**, *Clean Code: A Handbook of Agile Software Craftsmanship* (Prentice Hall, 2008) — **Chương 1, "Clean Code"** (`tr. 1–15`): sẽ-luôn-có-code (tr. 1–3); killer app chết vì code bẩn và định luật LeBlanc (tr. 3–4); cái giá của mớ hỗn độn, đại tái thiết trên mây (tr. 4–6); nghịch lý "đi nhanh = giữ sạch" (tr. 6); định nghĩa code sạch của sáu bậc thầy (tr. 7–12); trường phái và lời mời tranh luận (tr. 13); tỉ lệ đọc:viết và Quy tắc Hướng đạo sinh (tr. 13–15). `tai_lieu/Clean.Code.2008.8.pdf`
- Phản biện 2026 dẫn từ ngoài sách: Casey Muratori, *"Clean Code, Horrible Performance"* (2023); phong trào data-oriented design; các bài *"A Case Against Clean Code"*.
- Quy ước trích: `tr. X` = số trang in trong sách; trang tệp PDF = `X + 31`.

---

**Bản đồ khoá học:** [Bài 0 ← bạn đang ở đây] · [Bài 1 — Đặt tên](bai_01_dat_ten.md) · [Bài 2 — Hàm](bai_02_ham.md) · [Bài 3 — Comment](bai_03_comment.md) · [Bài 4 — Định dạng](bai_04_dinh_dang.md) · [Bài 5 — Object & dữ liệu](bai_05_object_va_du_lieu.md) · [Bài 6 — Xử lý lỗi](bai_06_xu_ly_loi.md) · [Bài 7 — Ranh giới](bai_07_ranh_gioi.md) · [Bài 8 — Unit test](bai_08_unit_test.md) · [Bài 9 — Class](bai_09_class.md) · [Bài 10 — Hệ thống](bai_10_he_thong.md) · [Bài 11 — Thiết kế nổi lên](bai_11_thiet_ke_noi_len.md) · [Bài 12 — Concurrency](bai_12_concurrency.md) · [Bài 13 — Xem code sạch nảy sinh](bai_13_xem_code_nay_sinh.md) · [Bài 14 — Refactor ngoài đời](bai_14_refactor_ngoai_doi.md) · [Bài 15 — Danh mục mùi code](bai_15_danh_muc_mui_code.md)

Xem thêm [README khoá học](../README.md).
