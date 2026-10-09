# Bài 2 — Hàm: nhỏ, làm một việc, kể một câu chuyện

> [!info] Về bài này
> Dựng từ **Chương 3 — "Functions"** của *Clean Code* (Robert C. Martin, 2008 — `tai_lieu/`, `tr. 31–52`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 31`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Mạch bài: *hàm bẩn → gọi tên vấn đề → bản sạch (TypeScript, chạy được) → nguyên tắc → đối chiếu 2026 → áp dụng*.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: ba phút không hiểu nổi một hàm](#1-mở-đầu-ba-phút-không-hiểu-nổi-một-hàm)
2. [Nhỏ, và làm một việc](#2-nhỏ-và-làm-một-việc)
3. [Code minh hoạ: chôn switch vào factory](#3-code-minh-hoạ-chôn-switch-vào-factory)
4. [Tham số: ít nhất có thể, và cờ boolean là mùi](#4-tham-số-ít-nhất-có-thể-và-cờ-boolean-là-mùi)
5. [Side effect là lời nói dối](#5-side-effect-là-lời-nói-dối)
6. [Tách lệnh khỏi truy vấn, ưu tiên exception](#6-tách-lệnh-khỏi-truy-vấn-ưu-tiên-exception)
7. [Đừng lặp lại, và cách thật sự viết ra hàm như thế](#7-đừng-lặp-lại-và-cách-thật-sự-viết-ra-hàm-như-thế)
8. [Đối chiếu 2026](#8-đối-chiếu-2026)
9. [Áp dụng vào codebase của bạn](#9-áp-dụng-vào-codebase-của-bạn)
10. [Từ điển thuật ngữ](#10-từ-điển-thuật-ngữ)
11. [Câu hỏi tự kiểm tra](#11-câu-hỏi-tự-kiểm-tra)
12. [Tóm tắt một trang](#tóm-tắt-một-trang)
13. [Nguồn](#nguồn)

---

## 1. Mở đầu: ba phút không hiểu nổi một hàm

Uncle Bob mở chương bằng một hàm thật lấy từ FitNesse — `testableHtml` — dài ngoằng, lồng `if` hai ba tầng điều khiển bằng cờ, trộn chuỗi lạ với lời gọi khó hiểu. Ông thách người đọc: *hiểu nó trong ba phút xem*. Gần như không ai làm được. Rồi ông cho xem bản sau khi tách vài hàm, đổi vài tên, sắp xếp lại — chỉ còn chín dòng mà ý định hiện rõ: *hàm này chèn các trang setup/teardown vào một trang test rồi render ra HTML*. Chương này là câu trả lời cho câu hỏi: điều gì khiến bản thứ hai đọc được còn bản thứ nhất thì không?

## 2. Nhỏ, và làm một việc

Quy tắc số một, và cũng gần như là tất cả:

> [!quote] Ch. 3 — Small! (tr. 34)
> "The first rule of functions is that they should be small. The second rule of functions is that they should be smaller than that."
>
> *Quy tắc đầu tiên của hàm: phải nhỏ. Quy tắc thứ hai: phải nhỏ hơn thế nữa.*

Uncle Bob thẳng thắn thừa nhận đây là khẳng định *không* chứng minh được bằng nghiên cứu — chỉ là điều bốn thập niên thử-và-sai dạy ông. Từ "nhỏ" kéo theo một hệ quả: thân mỗi khối `if`/`else`/`while` nên chỉ **một dòng**, mà dòng đó thường là một lời gọi hàm có tên mô tả rõ. Nghĩa là độ thụt lề của hàm không nên quá một hai cấp. Nhỏ để làm gì? Để **làm một việc**:

> [!quote] Ch. 3 — Do One Thing (tr. 35)
> "FUNCTIONS SHOULD DO ONE THING. THEY SHOULD DO IT WELL. THEY SHOULD DO IT ONLY."
>
> *HÀM NÊN LÀM MỘT VIỆC. LÀM TỐT. VÀ CHỈ LÀM MỘT VIỆC ĐÓ.*

Nhưng "một việc" là gì, khi một hàm ba dòng vẫn làm "ba bước"? Uncle Bob cho một thước đo rõ: nếu mọi bước trong hàm đều ở **đúng một mức trừu tượng ngay dưới tên hàm**, thì hàm làm một việc.

> [!quote] Ch. 3 — Do One Thing (tr. 36)
> "If a function does only those steps that are one level below the stated name of the function, then the function is doing one thing."
>
> *Nếu một hàm chỉ gồm những bước ở ngay một mức dưới cái tên đã đặt cho nó, thì hàm đó đang làm một việc.*

Một dấu hiệu khác: nếu bạn còn **tách ra được** một hàm con có tên *không* chỉ là lặp lại cài đặt, thì hàm gốc đang làm hơn một việc. Và code nên đọc từ trên xuống như một chuỗi đoạn văn — mỗi hàm dẫn tới hàm ở mức trừu tượng kế dưới (ông gọi là **Quy tắc Bước xuống**, *The Stepdown Rule*).

## 3. Code minh hoạ: chôn switch vào factory

Ví dụ kinh điển của chương: hàm `calculatePay` dùng `switch` theo loại nhân viên. Nó lớn, làm N việc, vi phạm **SRP** (nhiều lý do để thay đổi) và **OCP** (phải sửa mỗi khi thêm loại). Tệ nhất: sẽ có vô số hàm anh em (`isPayday`, `deliverPay`) lặp lại đúng cấu trúc `switch` đó. Lời giải: chôn `switch` vào tầng hầm của một **factory**, dùng đúng một lần để tạo đối tượng, còn mọi hành vi đi qua đa hình.

```typescript
import { strict as assert } from "node:assert";

type EmployeeType = "COMMISSIONED" | "HOURLY" | "SALARIED";
type EmployeeRecord = { type: EmployeeType; base: number };

// ===== Bản bẩn: một switch làm N việc. Thêm loại nhân viên =>
// phải sửa ở ĐÂY, và ở mọi hàm anh em (isPayday, deliverPay...). =====
function calculatePayDirty(e: EmployeeRecord): number {
  switch (e.type) {
    case "COMMISSIONED":
      return e.base + 500;
    case "HOURLY":
      return e.base * 40;
    case "SALARIED":
      return e.base;
    default:
      throw new Error("InvalidEmployeeType: " + e.type);
  }
}

// ===== Bản sạch: switch bị chôn trong factory, dùng ĐÚNG MỘT LẦN
// để tạo đối tượng; mọi hành vi đi qua đa hình. =====
interface Employee {
  calculatePay(): number;
}
class CommissionedEmployee implements Employee {
  private base: number;
  constructor(base: number) {
    this.base = base;
  }
  calculatePay(): number {
    return this.base + 500;
  }
}
class HourlyEmployee implements Employee {
  private base: number;
  constructor(base: number) {
    this.base = base;
  }
  calculatePay(): number {
    return this.base * 40;
  }
}
class SalariedEmployee implements Employee {
  private base: number;
  constructor(base: number) {
    this.base = base;
  }
  calculatePay(): number {
    return this.base;
  }
}
class EmployeeFactory {
  static make(r: EmployeeRecord): Employee {
    switch (r.type) {
      case "COMMISSIONED":
        return new CommissionedEmployee(r.base);
      case "HOURLY":
        return new HourlyEmployee(r.base);
      case "SALARIED":
        return new SalariedEmployee(r.base);
      default:
        throw new Error("InvalidEmployeeType: " + r.type);
    }
  }
}

const records: EmployeeRecord[] = [
  { type: "COMMISSIONED", base: 1000 },
  { type: "HOURLY", base: 25 },
  { type: "SALARIED", base: 5000 },
];

for (const r of records) {
  const dirty = calculatePayDirty(r);
  const clean = EmployeeFactory.make(r).calculatePay();
  assert.equal(dirty, clean);
  console.log(`${r.type.padEnd(12)} lương: bản bẩn=${dirty}  bản sạch=${clean}`);
}
console.log("hai bản cho cùng kết quả cho mọi loại nhân viên.");
```

Kết quả chạy thật:

```
COMMISSIONED lương: bản bẩn=1500  bản sạch=1500
HOURLY       lương: bản bẩn=1000  bản sạch=1000
SALARIED     lương: bản bẩn=5000  bản sạch=5000
hai bản cho cùng kết quả cho mọi loại nhân viên.
```

Hai bản cho **cùng con số**. Khác biệt nằm ở lúc *thay đổi*: muốn thêm loại `INTERN`, bản bẩn buộc bạn sửa cái `switch` trong `calculatePay` — và trong mọi hàm anh em. Bản sạch chỉ cần **thêm một lớp** `InternEmployee` và một dòng trong factory; `calculatePay`, `isPayday`, `deliverPay` không ai phải động vào. Luật của Uncle Bob: switch chấp nhận được nếu xuất hiện *một lần*, để tạo đối tượng đa hình, và giấu sau một quan hệ kế thừa.

> [!note] Tự thử
> 1. Thêm loại `"INTERN"` trả lương cố định `0`. Đếm xem bản bẩn và bản sạch mỗi bên buộc bạn sửa bao nhiêu chỗ.
> 2. Thêm một "hàm anh em" `isPayday(e)` cho cả hai cách. Bên nào lại phải viết thêm một `switch` nữa?
> 3. Bỏ nhánh `default` ở bản bẩn rồi truyền một `type` lạ. Chuyện gì xảy ra, và vì sao nhánh `default` quan trọng?

## 4. Tham số: ít nhất có thể, và cờ boolean là mùi

> [!quote] Ch. 3 — Function Arguments (tr. 40)
> "The ideal number of arguments for a function is zero (niladic). Next comes one (monadic), followed closely by two (dyadic). Three arguments (triadic) should be avoided where possible."
>
> *Số tham số lý tưởng của một hàm là **không**. Kế đến là **một**, rồi sát nút là **hai**. Ba tham số thì nên tránh nếu có thể.*

Tham số khó vì chúng ngốn năng lực khái niệm và làm việc viết test bùng nổ tổ hợp. Tham số *đầu ra* (output argument) còn khó hơn tham số *đầu vào*: ta quen thông tin đi *vào* qua tham số và đi *ra* qua giá trị trả về. Và có một loại tham số Uncle Bob ghét ra mặt:

> [!quote] Ch. 3 — Flag Arguments (tr. 41)
> "Flag arguments are ugly. Passing a boolean into a function is a truly terrible practice."
>
> *Tham số cờ thật xấu xí. Truyền một boolean vào hàm là một thói quen tệ hại.*

Vì một cờ boolean *tự thú* rằng hàm làm hai việc: một đằng khi cờ `true`, một nẻo khi `false`. Thay vì `render(isSuite: boolean)`, hãy tách thành `renderForSuite()` và `renderForSingleTest()`. Khi hàm có vẻ cần hơn hai ba tham số, thường là vài tham số trong đó đáng được gói thành một lớp riêng (`makeCircle(x, y, radius)` → `makeCircle(center: Point, radius)`).

## 5. Side effect là lời nói dối

> [!quote] Ch. 3 — Have No Side Effects (tr. 44)
> "Side effects are lies. Your function promises to do one thing, but it also does other hidden things."
>
> *Side effect là những lời nói dối. Hàm của bạn hứa làm một việc, nhưng lại lén làm thêm những việc khác.*

Ví dụ của sách: hàm `checkPassword(userName, password)` — theo tên thì chỉ kiểm mật khẩu — lại lén gọi `Session.initialize()`. Hệ quả là một **temporal coupling** (ràng buộc theo thời gian): `checkPassword` giờ chỉ gọi được vào "lúc an toàn để khởi tạo session"; gọi sai thứ tự thì mất dữ liệu session. Nếu buộc phải có ràng buộc thời gian ấy, ít nhất phải nói ra trong tên: `checkPasswordAndInitializeSession` — mà cái tên đó lại vi phạm "làm một việc". Nói cách khác: side effect ẩn là một cái bẫy, và cách duy nhất để trung thực là đừng giấu.

## 6. Tách lệnh khỏi truy vấn, ưu tiên exception

Hai nguyên tắc đi liền nhau. Thứ nhất, **Command Query Separation**:

> [!quote] Ch. 3 — Command Query Separation (tr. 45)
> "Functions should either do something or answer something, but not both."
>
> *Hàm nên hoặc **làm** một việc, hoặc **trả lời** một điều — chứ đừng cả hai.*

Hàm `public boolean set(attribute, value)` vừa gán vừa trả về thành/bại, đẻ ra câu `if (set("username", "unclebob"))` nhập nhằng: đang *hỏi* hay đang *gán*? Lời giải là tách: `if (attributeExists("username")) { setAttribute(...); }`.

Thứ hai, **ưu tiên exception hơn mã lỗi**. Trả về mã lỗi đẩy caller vào những `if` lồng sâu để xử lý lỗi ngay tại chỗ; dùng exception thì tách được phần xử lý lỗi khỏi luồng chính. Và vì "xử lý lỗi là một việc", một hàm có `try` thì `try` nên là từ **đầu tiên**, và sau khối `catch`/`finally` không còn gì nữa.

## 7. Đừng lặp lại, và cách thật sự viết ra hàm như thế

> [!quote] Ch. 3 — Don't Repeat Yourself (tr. 48)
> "Duplication may be the root of all evil in software."
>
> *Trùng lặp có lẽ là gốc rễ của mọi điều xấu xa trong phần mềm.*

Nhiều nguyên tắc lớn (chuẩn hoá CSDL của Codd, kế thừa OOP, lập trình cấu trúc…) rốt cuộc đều là chiến lược diệt trùng lặp. Nhưng đây là điều quan trọng nhất của chương, và là chỗ nhiều người hiểu lầm: **không ai viết ra những hàm sạch ngay từ đầu.**

> [!quote] Ch. 3 — How Do You Write Functions Like This? (tr. 49)
> "When I write functions, they come out long and complicated. […] So then I massage and refine that code, splitting out functions, changing names, eliminating duplication […] all the while keeping the tests passing."
>
> *Khi tôi viết hàm, chúng ra đời dài và rối. […] Rồi tôi nhào nặn và gọt giũa: tách hàm, đổi tên, diệt trùng lặp […] tất cả trong khi vẫn giữ cho test xanh.*

Nghĩa là code sạch là kết quả của **refactor có test bọc**, không phải của thiên tài gõ một phát ra ngay. Đó cũng là tinh thần của [Bài 13 (Xem code sạch nảy sinh)](bai_13_xem_code_nay_sinh.md). Và mục tiêu tối hậu không phải "hàm ngắn", mà là kể một câu chuyện:

> [!quote] Ch. 3 — Conclusion (tr. 49)
> "Master programmers think of systems as stories to be told rather than programs to be written."
>
> *Những lập trình viên bậc thầy nghĩ về hệ thống như những câu chuyện để kể, hơn là những chương trình để viết.*

## 8. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Đây là **chương bị cãi nhiều nhất** của cuốn sách. Tinh thần thì bền, nhưng vài con số và lời khuyên đã thành mặt trận.
> - **"Hàm phải cực nhỏ" (tr. 34)** — chính Uncle Bob thừa nhận không có nghiên cứu chống lưng. Phê bình phổ biến nhất (nổi nhất là của **John Ousterhout**, *A Philosophy of Software Design*, 2018): tách hàm quá đà đẻ ra một rừng hàm ba dòng, "shallow modules" — để hiểu một việc phải nhảy qua chục hàm, tổng độ phức tạp *tăng*. Ousterhout đề cao "deep module": giao diện nhỏ, ruột lớn. Cân nhắc: tách khi nó *giảm* tải nhận thức, đừng tách cho đủ chỉ tiêu dòng.
> - **"Clean Code, Horrible Performance" (Casey Muratori, 2023)** — chính ví dụ `switch → đa hình` ở mục 3 là mục tiêu chỉ trích. Trên phần cứng hiện đại, gọi ảo (virtual dispatch) qua nhiều lớp nhỏ có thể chậm hơn một `switch` phẳng nhiều lần. Với code nóng về hiệu năng (game, xử lý số lớn), *data-oriented design* thường ngược hẳn lời khuyên này. Với code nghiệp vụ thường ngày thì khác biệt ấy không đáng kể — biết *khi nào* mỗi bên thắng mới là nghề.
> - **Cờ boolean (tr. 41)** — lời khuyên còn đúng, và 2026 có cách diễn đạt tốt hơn: thay `render(true)` bằng tham số đối tượng `render({ suite: true })` hoặc union type `render("suite" | "single")` — tự mô tả ngay tại chỗ gọi.
> - **Exception vs mã lỗi (tr. 47)** — 2026 có lựa chọn thứ ba mà 2008 chưa phổ biến: kiểu `Result<T, E>` / `Either` (Rust, và các thư viện TS như `neverthrow`). Lỗi thành giá trị tường minh trong chữ ký hàm — xem thêm [Bài 6 (Xử lý lỗi)](bai_06_xu_ly_loi.md).
> - **Vẫn vàng nguyên**: làm một việc, side-effect-là-nói-dối, command-query separation, DRY, và "không ai viết sạch từ bản nháp đầu".

## 9. Áp dụng vào codebase của bạn

> [!question] Áp dụng vào codebase của bạn
> 1. **Tìm một `switch` lặp cấu trúc.** Trong code bạn có cái `switch`/`if-else` nào theo "loại" xuất hiện ở *nhiều* hàm không? Đó là ứng viên cho đa hình — nhưng trước khi refactor, hỏi: đây có phải code nóng về hiệu năng không? (xem Đối chiếu 2026)
> 2. **Săn một cờ boolean.** Tìm một hàm nhận `boolean` điều khiển luồng. Thử tách thành hai hàm tên rõ, hoặc đổi sang tham số đối tượng. Dễ đọc hơn ở chỗ gọi không?
> 3. **Soi side effect.** Chọn một hàm tên bắt đầu bằng `get`/`is`/`check`. Nó có lén thay đổi trạng thái gì không? Nếu có, đó là một "lời nói dối" — đặt lại tên hoặc tách ra.
> 4. **Thử quy trình "nháp rồi gọt".** Lần tới viết một hàm, cứ để nó ra đời dài và xấu *nhưng có test bọc*, rồi mới refactor nhỏ dần. Cảm giác có khác với việc cố viết hoàn hảo ngay không?

## 10. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Do One Thing** | Hàm chỉ gồm các bước ở đúng một mức trừu tượng dưới tên nó (tr. 35–36). |
| **Stepdown Rule** | Code đọc từ trên xuống, mỗi hàm dẫn tới hàm ở mức trừu tượng kế dưới (tr. 37). |
| **SRP / OCP** | Single Responsibility / Open-Closed — switch theo loại vi phạm cả hai (tr. 38). |
| **Niladic/monadic/dyadic/triadic** | Hàm 0/1/2/3 tham số; càng ít càng tốt (tr. 40). |
| **Flag argument** | Tham số boolean điều khiển luồng — mùi của "làm hai việc" (tr. 41). |
| **Side effect** | Việc ẩn hàm làm ngoài điều tên nó hứa; sinh *temporal coupling* (tr. 44). |
| **Command Query Separation** | Hàm hoặc *làm* hoặc *trả lời*, không cả hai (tr. 45). |
| **DRY** | Don't Repeat Yourself — diệt trùng lặp (tr. 48). |

## 11. Câu hỏi tự kiểm tra

1. Thước đo "làm một việc" của Uncle Bob là gì? Vì sao một hàm "ba bước" vẫn có thể là làm một việc? *(tr. 36)*
2. Vì sao `switch` theo loại vi phạm SRP và OCP? Khi nào thì `switch` chấp nhận được? *(tr. 38–39)*
3. Vì sao cờ boolean là "mùi"? Nêu hai cách thay nó. *(tr. 41)*
4. "Side effect là lời nói dối" nghĩa là gì? *temporal coupling* là gì? *(tr. 44)*
5. Theo Uncle Bob, hàm sạch được viết ra bằng cách nào? Vai trò của test ở đó? *(tr. 49)*
6. Casey Muratori và John Ousterhout phản biện điều gì về chương này? Khi nào lời phản biện đó đáng nghe nhất?

## Tóm tắt một trang

```
BÀI 2 — HÀM: NHỎ, LÀM MỘT VIỆC, KỂ MỘT CÂU CHUYỆN
─────────────────────────────────────────────────────────
NHỎ      "nhỏ, rồi nhỏ hơn thế" (tr.34). Thân if/while một dòng,
         thường là một lời gọi hàm. Thụt lề ≤ 1–2 cấp.

MỘT VIỆC Các bước ở ĐÚNG một mức dưới tên hàm (tr.36).
         Stepdown Rule: đọc trên-xuống như chuỗi đoạn văn.

SWITCH   switch theo loại vi phạm SRP+OCP, nhân bản ở mọi hàm
         anh em → chôn vào FACTORY, dùng 1 lần, còn lại đa hình.
         calculatePayDirty  ==  EmployeeFactory.make().calculatePay()

THAM SỐ  0 > 1 > 2 >> 3 (tr.40). Cờ boolean = mùi (tr.41):
         render(true) → renderForSuite()/renderForSingleTest().

TRUNG THỰC  side effect = nói dối (tr.44). Command-Query
         Separation (tr.45). Ưu tiên exception hơn mã lỗi (tr.47).

DRY      "trùng lặp là gốc rễ mọi điều xấu" (tr.48).

VIẾT SAO Không ai viết sạch từ nháp đầu: viết dài+xấu CÓ TEST,
         rồi gọt dần (tr.49). Hệ thống = câu chuyện để kể.

2026     Chương BỊ CÃI NHẤT. Ousterhout: đừng tách quá đà
         (shallow vs deep module). Muratori: switch→đa hình có
         thể chậm (data-oriented design). Thêm Result<T,E> cho lỗi.
```

## Nguồn

- **Robert C. Martin**, *Clean Code* (Prentice Hall, 2008) — **Chương 3, "Functions"** (`tr. 31–52`): hàm `testableHtml` ba-phút-không-hiểu và bản refactor (tr. 32–34); "small!", khối một dòng (tr. 34–35); do one thing, một mức trừu tượng, Stepdown Rule (tr. 35–37); switch, SRP/OCP, factory + đa hình (tr. 37–39); tên mô tả (tr. 39–40); số tham số lý tưởng, monad/dyad/triad, cờ boolean, argument object (tr. 40–44); side effect & temporal coupling, output argument (tr. 44–45); command query separation, ưu tiên exception, tách try/catch (tr. 45–48); DRY, lập trình cấu trúc, "cách thật sự viết hàm", hệ thống-là-câu-chuyện (tr. 48–50); liệt kê `SetupTeardownIncluder` (tr. 50–52). `tai_lieu/Clean.Code.2008.8.pdf`
- Phản biện 2026 dẫn từ ngoài sách: John Ousterhout, *A Philosophy of Software Design* (2018); Casey Muratori, *"Clean Code, Horrible Performance"* (2023); kiểu `Result`/`Either` (Rust, `neverthrow`).
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 31`.

---

**Bản đồ khoá học:** [Bài 0 — Clean Code là gì](bai_00_clean_code_la_gi.md) · [Bài 1 — Đặt tên](bai_01_dat_ten.md) · [Bài 2 ← bạn đang ở đây] · [Bài 3 — Comment](bai_03_comment.md) · [Bài 4 — Định dạng](bai_04_dinh_dang.md) · [Bài 5 — Object & dữ liệu](bai_05_object_va_du_lieu.md) · [Bài 6 — Xử lý lỗi](bai_06_xu_ly_loi.md) · [Bài 7 — Ranh giới](bai_07_ranh_gioi.md) · [Bài 8 — Unit test](bai_08_unit_test.md) · [Bài 9 — Class](bai_09_class.md) · [Bài 10 — Hệ thống](bai_10_he_thong.md) · [Bài 11 — Thiết kế nổi lên](bai_11_thiet_ke_noi_len.md) · [Bài 12 — Concurrency](bai_12_concurrency.md) · [Bài 13 — Xem code sạch nảy sinh](bai_13_xem_code_nay_sinh.md) · [Bài 14 — Refactor ngoài đời](bai_14_refactor_ngoai_doi.md) · [Bài 15 — Danh mục mùi code](bai_15_danh_muc_mui_code.md)

Xem thêm [README khoá học](../README.md).
