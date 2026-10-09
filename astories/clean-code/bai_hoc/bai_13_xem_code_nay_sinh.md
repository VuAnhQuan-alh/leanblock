# Bài 13 — Xem code sạch nảy sinh: mổ bộ parse Args

> [!info] Về bài này
> Dựng từ **Chương 14 — "Successive Refinement" (Case Study of a Command-Line Argument Parser)** của *Clean Code* (Robert C. Martin, 2008 — `tai_lieu/`, `tr. 193–250`). Đây là **chương công phu nhất** của sách — và bài công phu nhất của khoá.
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 31`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Vì chương là một màn refactor dài bằng code Java, bài này **port bộ parse `Args` sang TypeScript chạy được**, cho thấy code sạch *nảy sinh dần* qua refactor mà hành vi không đổi.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: một module khởi đầu ổn nhưng không nhân rộng nổi](#1-mở-đầu-một-module-khởi-đầu-ổn-nhưng-không-nhân-rộng-nổi)
2. [Bài toán Args](#2-bài-toán-args)
3. [Code minh hoạ: từ bản nháp tới ArgumentMarshaler đa hình](#3-code-minh-hoạ-từ-bản-nháp-tới-argumentmarshaler-đa-hình)
4. [Vì sao refactor theo bước nhỏ, test luôn xanh](#4-vì-sao-refactor-theo-bước-nhỏ-test-luôn-xanh)
5. [Thông điệp lớn: chỉ chạy được là chưa đủ](#5-thông-điệp-lớn-chỉ-chạy-được-là-chưa-đủ)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào codebase của bạn](#7-áp-dụng-vào-codebase-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mở đầu: một module khởi đầu ổn nhưng không nhân rộng nổi

Mọi bài trước dạy các *nguyên tắc* của code sạch. Bài này cho xem chúng vận hành *trong thực tế*, trên một ca duy nhất kéo dài cả chương.

> [!quote] Ch. 14 — Successive Refinement (tr. 193)
> "This chapter is a case study in successive refinement. You will see a module that started well but did not scale. Then you will see how the module was refactored and cleaned."
>
> *Chương này là một ca nghiên cứu về **gọt giũa liên tiếp**. Bạn sẽ thấy một module khởi đầu ổn nhưng không nhân rộng nổi. Rồi bạn sẽ thấy nó được refactor và làm sạch ra sao.*

Đây là điểm mạnh *nhất* của *Clean Code*: không giảng lý thuyết, mà cho bạn **đứng sau lưng** tác giả xem một mớ hỗn độn được gột sạch từng bước.

## 2. Bài toán Args

`Args` là tiện ích parse tham số dòng lệnh. Bạn dựng nó với một *schema* và mảng `args`, rồi hỏi giá trị:

```
const arg = new Args("l,p#,d*", argv);
const logging = arg.getBoolean('l');   // -l : boolean
const port = arg.getInt('p');          // -p : integer (#)
const directory = arg.getString('d');  // -d : string (*)
```

Schema `"l,p#,d*"` khai ba tham số: `-l` boolean, `-p` số nguyên, `-d` chuỗi. Nghe đơn giản, nhưng bản cài đặt đầu tiên của Uncle Bob phình ra rất nhanh khi thêm kiểu — mỗi kiểu mới lại chèn thêm `if/else` và thêm một map, một cơn ác mộng nhân rộng. Lời giải nảy sinh là **ArgumentMarshaler**: mỗi kiểu tự biết cách parse chính nó, đa hình sau một giao diện chung.

## 3. Code minh hoạ: từ bản nháp tới ArgumentMarshaler đa hình

Dưới đây là hai bản — bản **nháp** (mỗi kiểu một map, `if/else` kiểm hậu tố) và bản **sạch** (đa hình qua `ArgumentMarshaler`) — port sang TS, cùng parse một schema+args và cho **cùng kết quả**:

```typescript
import { strict as assert } from "node:assert";

// =====================================================================
// BẢN NHÁP ĐẦU ("khởi đầu ổn nhưng không nhân rộng nổi"): mọi thứ nhét
// trong Args, mỗi kiểu một map riêng, parse bằng if/else kiểm hậu tố.
// =====================================================================
class ArgsMessy {
  private booleans: Map<string, boolean> = new Map();
  private ints: Map<string, number> = new Map();
  private strings: Map<string, string> = new Map();
  constructor(schema: string, args: string[]) {
    for (const el of schema.split(",")) {
      const id = el.charAt(0);
      const tail = el.substring(1);
      if (tail === "") this.booleans.set(id, false);
      else if (tail === "#") this.ints.set(id, 0);
      else if (tail === "*") this.strings.set(id, "");
    }
    let i = 0;
    while (i < args.length) {
      const a = args[i];
      if (a.startsWith("-")) {
        const id = a.charAt(1);
        if (this.booleans.has(id)) this.booleans.set(id, true);
        else if (this.ints.has(id)) { this.ints.set(id, parseInt(args[i + 1], 10)); i++; }
        else if (this.strings.has(id)) { this.strings.set(id, args[i + 1]); i++; }
      }
      i++;
    }
  }
  getBoolean(id: string): boolean { return this.booleans.get(id) ?? false; }
  getInt(id: string): number { return this.ints.get(id) ?? 0; }
  getString(id: string): string { return this.strings.get(id) ?? ""; }
}

// =====================================================================
// BẢN SẠCH NẢY SINH: ArgumentMarshaler đa hình, MỘT map duy nhất.
// Thêm kiểu mới = thêm một marshaler, KHÔNG đụng vòng parse.
// =====================================================================
interface ArgumentMarshaler {
  set(value: string | null): void;
  get(): boolean | number | string;
  wantsValue(): boolean; // boolean không nuốt tham số kế tiếp
}
class BooleanMarshaler implements ArgumentMarshaler {
  private value = false;
  set(_value: string | null): void { this.value = true; }
  get(): boolean { return this.value; }
  wantsValue(): boolean { return false; }
}
class IntegerMarshaler implements ArgumentMarshaler {
  private value = 0;
  set(value: string | null): void { this.value = parseInt(value ?? "0", 10); }
  get(): number { return this.value; }
  wantsValue(): boolean { return true; }
}
class StringMarshaler implements ArgumentMarshaler {
  private value = "";
  set(value: string | null): void { this.value = value ?? ""; }
  get(): string { return this.value; }
  wantsValue(): boolean { return true; }
}
class Args {
  private marshalers: Map<string, ArgumentMarshaler> = new Map();
  constructor(schema: string, args: string[]) {
    for (const el of schema.split(",")) {
      const id = el.charAt(0);
      const tail = el.substring(1);
      if (tail === "") this.marshalers.set(id, new BooleanMarshaler());
      else if (tail === "#") this.marshalers.set(id, new IntegerMarshaler());
      else if (tail === "*") this.marshalers.set(id, new StringMarshaler());
    }
    let i = 0;
    while (i < args.length) {
      const a = args[i];
      if (a.startsWith("-")) {
        const id = a.charAt(1);
        const m = this.marshalers.get(id);
        if (m) {
          if (m.wantsValue()) { m.set(args[i + 1]); i++; }
          else m.set(null);
        }
      }
      i++;
    }
  }
  getBoolean(id: string): boolean { const m = this.marshalers.get(id); return m ? (m.get() as boolean) : false; }
  getInt(id: string): number { const m = this.marshalers.get(id); return m ? (m.get() as number) : 0; }
  getString(id: string): string { const m = this.marshalers.get(id); return m ? (m.get() as string) : ""; }
}

const schema = "l,p#,d*";
const argv = ["-l", "-p", "8080", "-d", "/tmp/log"];
const messy = new ArgsMessy(schema, argv);
const clean = new Args(schema, argv);

assert.equal(messy.getBoolean("l"), clean.getBoolean("l"));
assert.equal(messy.getInt("p"), clean.getInt("p"));
assert.equal(messy.getString("d"), clean.getString("d"));

console.log("logging (-l):", clean.getBoolean("l"));
console.log("port (-p)   :", clean.getInt("p"));
console.log("dir (-d)    :", clean.getString("d"));
console.log("nháp và sạch CÙNG kết quả — code sạch nảy sinh mà hành vi không đổi.");
```

Kết quả chạy thật:

```
logging (-l): true
port (-p)   : 8080
dir (-d)    : /tmp/log
nháp và sạch CÙNG kết quả — code sạch nảy sinh mà hành vi không đổi.
```

Khác biệt lộ ra khi **thêm một kiểu** `double` (hậu tố `##`): bản `ArgsMessy` buộc thêm một `Map<string, number>` *nữa*, thêm một nhánh `else if` ở *cả* vòng parse-schema *và* vòng parse-args, thêm một getter. Bản `Args` chỉ cần **thêm một lớp** `DoubleMarshaler` và một dòng trong parse-schema — vòng parse-args **không đụng tới**, vì nó chỉ nói chuyện với giao diện `ArgumentMarshaler`. Đó chính là OCP ([Bài 9](bai_09_class.md)) và đa hình thay switch ([Bài 2](bai_02_ham.md)) hiện ra trong một ca thật.

> [!note] Tự thử
> 1. Thêm `DoubleMarshaler` (hậu tố `##`) vào **cả hai** bản. Đếm số chỗ bạn phải sửa ở `ArgsMessy` so với `Args`. Đây là toàn bộ luận điểm của chương.
> 2. Thêm tham số `-p` *thiếu* giá trị (bỏ `"8080"` khỏi `argv`). Hai bản xử lý ra sao? Chương thật dành nhiều công cho chính việc *xử lý lỗi* này ([Bài 6](bai_06_xu_ly_loi.md)).
> 3. Viết một hàm test `assertParsesPort` chỉ kiểm `-p`. Giờ sửa logic boolean, test port có gãy oan không? (Nối [Bài 8](bai_08_unit_test.md): một khái niệm mỗi test.)

## 4. Vì sao refactor theo bước nhỏ, test luôn xanh

Uncle Bob không viết thẳng ra bản sạch. Ông đi qua *hàng chục* bước nhỏ (Listing 14-2 đến 14-16), mỗi bước một phép biến đổi giữ nguyên hành vi, chạy test sau mỗi bước. Đây là hiện thân của "cách thật sự viết hàm" ở [Bài 2](bai_02_ham.md) và "refactor là quy tắc 2–4" ở [Bài 11](bai_11_thiet_ke_noi_len.md). Và kết quả thường là **xoá nhiều hơn thêm**:

> [!quote] Ch. 14 — (incremental refactoring) (tr. 250)
> "Much of good software design is simply about partitioning—creating appropriate places to put different kinds of code."
>
> *Phần lớn thiết kế phần mềm tốt chỉ đơn giản là **phân vùng** — tạo ra những chỗ thích hợp để đặt từng loại code khác nhau.*

Phần lớn thay đổi với lớp `Args` là *xoá*: code bị dời sang `ArgsException`, các marshaler tách ra file riêng. Mỗi phép tách làm lộ ra một vi phạm SRP tiếp theo, cho tới khi mỗi mảnh "nhỏ đến mức khó mà sai".

## 5. Thông điệp lớn: chỉ chạy được là chưa đủ

Lời kết của chương là một trong những đoạn mạnh nhất cả cuốn:

> [!quote] Ch. 14 — Conclusion (tr. 250)
> "It is not enough for code to work. Code that works is often badly broken. Programmers who satisfy themselves with merely working code are behaving unprofessionally."
>
> *Code chạy được thôi thì chưa đủ. Code chạy được thường vẫn hỏng nặng. Lập trình viên tự mãn với code "chỉ cần chạy" là đang cư xử thiếu chuyên nghiệp.*

Vì không gì bào mòn một dự án lâu dài bằng code tồi: lịch tồi làm lại được, yêu cầu tồi định nghĩa lại được, nhưng code tồi thì mục ruỗng và lên men, thành sức nặng kéo cả đội xuống. Nên:

> [!quote] Ch. 14 — Conclusion (tr. 250)
> "So the solution is to continuously keep your code as clean and simple as it can be. Never let the rot get started."
>
> *Vậy lời giải là liên tục giữ code sạch và đơn giản hết mức có thể. Đừng bao giờ để sự mục ruỗng bắt đầu.*

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Bài học **phương pháp** của chương này là phần *bất tử nhất* của cả cuốn sách — và năm 2026 có công cụ mạnh hơn hẳn để thực thi nó.
> - **"Refactor theo bước nhỏ, test luôn xanh" — chuẩn vàng 2026**, và giờ được công cụ hoá: IDE refactor tự động (Rename, Extract Method/Class an toàn), và nhất là **AI pair programmer** (Copilot/Cursor) có thể thực hiện biến đổi — nhưng *chỉ an toàn khi có test bọc*. Chương này là lời nhắc: test (xem [Bài 8](bai_08_unit_test.md)) là thứ cho phép refactor không sợ hãi, dù người hay máy làm.
> - **Ví dụ `ArgumentMarshaler` qua kế thừa/đa hình** là lời giải 2008. Năm 2026, với TS, cùng bài toán có thể giải bằng *discriminated union + switch* (xem [Bài 5](bai_05_object_va_du_lieu.md)) — compiler lo exhaustiveness, đôi khi gọn hơn cây lớp. Cả hai đều đúng; đây là chỗ "trường phái" mà Uncle Bob tự nhận ([Bài 0](bai_00_clean_code_la_gi.md)).
> - **AI làm "code chạy được" rẻ đi — khiến thông điệp của chương *càng* quan trọng.** Năm 2026, sinh code "chỉ cần chạy" dễ chưa từng thấy (một prompt là xong). Đúng vì vậy mà "chạy được thôi chưa đủ" (tr. 250) càng đắt giá: giá trị của lập trình viên dịch từ *viết code* sang *đánh giá, cấu trúc, và giữ sạch* code — thứ AI chưa làm tin cậy được.
> - **"Đừng bao giờ để mục ruỗng bắt đầu" = Boy Scout Rule** ([Bài 0](bai_00_clean_code_la_gi.md)) ở mức vi mô, và là lý lẽ chống *nợ kỹ thuật* tích tụ — vẫn là chân lý quản trị kỹ thuật 2026.
> - **Vẫn vàng toàn bộ**: gọt giũa liên tiếp, xoá-nhiều-hơn-thêm, phân vùng, và "chạy được chưa đủ".

## 7. Áp dụng vào codebase của bạn

> [!question] Áp dụng vào codebase của bạn
> 1. **Tìm một `ArgsMessy` của bạn.** Tìm một hàm/lớp "khởi đầu ổn nhưng không nhân rộng nổi" — mỗi lần thêm trường hợp lại phải sửa nhiều chỗ. Đó là ứng viên cho đa hình/union.
> 2. **Refactor một bước, chạy test.** Chọn một phép biến đổi nhỏ (Extract Method). *Trước* khi làm, đảm bảo có test bọc. Làm xong, chạy test. Lặp lại. Cảm giác "an toàn để đổi" có khác với sửa mò không?
> 3. **Đếm xoá vs thêm.** Lần refactor tới, xem diff: bạn xoá nhiều hơn hay thêm nhiều hơn? Refactor tốt thường *xoá* nhiều.
> 4. **Soi "chạy được là xong".** Tìm một chỗ bạn (hoặc AI) vừa làm cho *chạy được* rồi bỏ đó. Dành 5 phút gột nó ngay bây giờ — "đừng để mục ruỗng bắt đầu".

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Successive refinement** | Gọt giũa liên tiếp: nhiều bước nhỏ giữ-hành-vi, test xanh sau mỗi bước (tr. 193). |
| **Args / schema** | Bộ parse tham số dòng lệnh; schema `"l,p#,d*"` khai kiểu từng tham số (tr. 193–194). |
| **ArgumentMarshaler** | Giao diện để mỗi kiểu tham số tự parse mình; đa hình thay switch (tr. 200+). |
| **Partitioning** | Phân vùng: tạo chỗ thích hợp cho từng loại code — phần lớn thiết kế tốt (tr. 250). |
| **"Working code is not enough"** | Chạy được thôi chưa đủ; tự mãn với nó là thiếu chuyên nghiệp (tr. 250). |
| **Never let the rot get started** | Liên tục giữ sạch; đừng để mục ruỗng khởi phát (tr. 250). |

## 9. Câu hỏi tự kiểm tra

1. "Successive refinement" nghĩa là gì? Vì sao Uncle Bob *không* viết thẳng bản sạch? *(tr. 193)*
2. Vì sao bản `ArgsMessy` "không nhân rộng nổi" khi thêm kiểu, còn bản `ArgumentMarshaler` thì có? *(mục 3)*
3. "Phần lớn thiết kế tốt là phân vùng" nghĩa là gì trong ca `Args`? *(tr. 250)*
4. Giải thích "code chạy được thường vẫn hỏng nặng". *(tr. 250)*
5. Năm 2026, vì sao AI làm cho thông điệp "chạy được chưa đủ" *càng* quan trọng? *(Đối chiếu 2026)*

## Tóm tắt một trang

```
BÀI 13 — XEM CODE SẠCH NẢY SINH: MỔ BỘ PARSE ARGS
─────────────────────────────────────────────────────────
CA     Args: parse "l,p#,d*". Bản đầu "khởi đầu ổn nhưng không
       nhân rộng nổi" (tr.193) → mỗi kiểu một map + if/else.

NẢY SINH  ArgumentMarshaler đa hình, MỘT map. Thêm kiểu `##`:
       ArgsMessy sửa nhiều chỗ; Args chỉ THÊM MỘT LỚP.
       (= OCP bài 9 + đa hình thay switch bài 2, trong ca thật.)

CÁCH LÀM  hàng chục bước nhỏ giữ-hành-vi, TEST XANH mỗi bước.
       Phần lớn thay đổi là XOÁ. "thiết kế tốt = phân vùng" (tr.250).

THÔNG ĐIỆP  "code chạy được thôi CHƯA ĐỦ... tự mãn với nó là
       thiếu chuyên nghiệp" (tr.250). "đừng để mục ruỗng bắt
       đầu" (tr.250) = Boy Scout Rule ở mức vi mô.

2026   refactor-bước-nhỏ-test-xanh = chuẩn vàng, giờ có IDE + AI
       làm thay — nhưng chỉ AN TOÀN khi có test. AI làm "chạy
       được" rẻ đi → "chạy được chưa đủ" CÀNG quan trọng.
```

## Nguồn

- **Robert C. Martin**, *Clean Code* (Prentice Hall, 2008) — **Chương 14, "Successive Refinement"** (`tr. 193–250`): giới thiệu ca gọt giũa liên tiếp (tr. 193); bài toán `Args`, cách dùng (tr. 193–194); bản cài đặt đầu và chuỗi refactor dài qua `ArgumentMarshaler` (tr. 194–249); phân vùng, "working code is not enough", "never let the rot get started" (tr. 250). `tai_lieu/Clean.Code.2008.8.pdf`
- Bổ sung 2026 dẫn từ ngoài sách: IDE refactoring tự động; AI pair programming (Copilot/Cursor) và vai trò của test; discriminated union trong TypeScript; nợ kỹ thuật.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 31`.

---

**Bản đồ khoá học:** [Bài 0 — Clean Code là gì](bai_00_clean_code_la_gi.md) · [Bài 1 — Đặt tên](bai_01_dat_ten.md) · [Bài 2 — Hàm](bai_02_ham.md) · [Bài 3 — Comment](bai_03_comment.md) · [Bài 4 — Định dạng](bai_04_dinh_dang.md) · [Bài 5 — Object & dữ liệu](bai_05_object_va_du_lieu.md) · [Bài 6 — Xử lý lỗi](bai_06_xu_ly_loi.md) · [Bài 7 — Ranh giới](bai_07_ranh_gioi.md) · [Bài 8 — Unit test](bai_08_unit_test.md) · [Bài 9 — Class](bai_09_class.md) · [Bài 10 — Hệ thống](bai_10_he_thong.md) · [Bài 11 — Thiết kế nổi lên](bai_11_thiet_ke_noi_len.md) · [Bài 12 — Concurrency](bai_12_concurrency.md) · [Bài 13 ← bạn đang ở đây] · [Bài 14 — Refactor ngoài đời](bai_14_refactor_ngoai_doi.md) · [Bài 15 — Danh mục mùi code](bai_15_danh_muc_mui_code.md)

Xem thêm [README khoá học](../README.md).
