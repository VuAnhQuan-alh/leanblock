# Bài 5 — Object và cấu trúc dữ liệu: hai thứ đối xứng ngược

> [!info] Về bài này
> Dựng từ **Chương 6 — "Objects and Data Structures"** của *Clean Code* (Robert C. Martin, 2008 — `tai_lieu/`, `tr. 93–102`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 31`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Mạch bài: *bày hết dữ liệu → gọi tên vấn đề → hai cách tổ chức (TypeScript, chạy được) → nguyên tắc → đối chiếu 2026 → áp dụng*.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: vì sao để biến private?](#1-mở-đầu-vì-sao-để-biến-private)
2. [Trừu tượng hoá dữ liệu, không chỉ là getter/setter](#2-trừu-tượng-hoá-dữ-liệu-không-chỉ-là-gettersetter)
3. [Code minh hoạ: object và cấu trúc dữ liệu đối xứng ngược](#3-code-minh-hoạ-object-và-cấu-trúc-dữ-liệu-đối-xứng-ngược)
4. [Luật Demeter và "tàu hoả trật bánh"](#4-luật-demeter-và-tàu-hoả-trật-bánh)
5. [DTO, bean, Active Record và thể lai](#5-dto-bean-active-record-và-thể-lai)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào codebase của bạn](#7-áp-dụng-vào-codebase-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mở đầu: vì sao để biến private?

Chương mở bằng một câu hỏi xoáy thẳng vào thói quen "tự động sinh getter/setter":

Ta để biến `private` là vì không muốn ai phụ thuộc vào chúng — ta muốn giữ quyền đổi kiểu, đổi cài đặt bất cứ lúc nào. Vậy tại sao nhiều người lại tự động gắn getter/setter cho mọi biến, phơi bày biến private *y như thể chúng public*? Làm thế thì cái `private` chỉ còn là hình thức.

## 2. Trừu tượng hoá dữ liệu, không chỉ là getter/setter

So sánh một `Point` có `x`, `y` public với một `Point` chỉ lộ `getX()`, `getR()`, `setPolar()`… — bản thứ hai *không cho bạn biết* nó lưu toạ độ vuông góc hay toạ độ cực. Đó mới là che giấu cài đặt thật sự.

> [!quote] Ch. 6 — Data Abstraction (tr. 94)
> "Hiding implementation is not just a matter of putting a layer of functions between the variables. Hiding implementation is about abstractions!"
>
> *Che giấu cài đặt không chỉ là chèn một lớp hàm giữa các biến. Che giấu cài đặt là chuyện của **trừu tượng hoá**!*

Một lớp không nên chỉ đẩy biến ra ngoài qua getter/setter, mà nên phơi ra những **giao diện trừu tượng** cho phép người dùng thao tác với *bản chất* của dữ liệu mà không cần biết cách nó được lưu. `getPercentFuelRemaining()` tốt hơn cặp `getFuelTankCapacityInGallons()` + `getGallonsOfGasoline()`, vì nó giấu đi "hình dạng" của dữ liệu.

## 3. Code minh hoạ: object và cấu trúc dữ liệu đối xứng ngược

Đây là ý sâu nhất của chương — và cũng là chỗ gây tranh cãi nhất năm 2026.

> [!quote] Ch. 6 — Data/Object Anti-Symmetry (tr. 95)
> "Objects hide their data behind abstractions and expose functions that operate on that data. Data structure expose their data and have no meaningful functions."
>
> *Object giấu dữ liệu sau những trừu tượng và phơi ra các hàm thao tác trên dữ liệu đó. Cấu trúc dữ liệu thì phơi dữ liệu ra và không có hàm nào đáng kể.*

Hai định nghĩa đối lập nhau như gương. Ví dụ hình học dưới đây viết cả hai cách — cùng kết quả, nhưng *dễ* và *khó* ở hai chiều mở rộng ngược nhau:

```typescript
import { strict as assert } from "node:assert";

const PI = 3.141592653589793;

// ===== Cách THỦ TỤC: cấu trúc dữ liệu trần + một hàm area() tập trung =====
// Thêm HÌNH mới => sửa area(). Thêm HÀM mới (perimeter) => hình không đổi.
type SquareData = { kind: "square"; side: number };
type RectData = { kind: "rectangle"; height: number; width: number };
type CircleData = { kind: "circle"; radius: number };
type ShapeData = SquareData | RectData | CircleData;

function areaProcedural(shape: ShapeData): number {
  switch (shape.kind) {
    case "square":
      return shape.side * shape.side;
    case "rectangle":
      return shape.height * shape.width;
    case "circle":
      return PI * shape.radius * shape.radius;
  }
}

// ===== Cách HƯỚNG ĐỐI TƯỢNG: mỗi hình tự biết area() =====
// Thêm HÌNH mới => chỉ thêm lớp. Thêm HÀM mới => sửa mọi lớp.
interface Shape {
  area(): number;
}
class Square implements Shape {
  private side: number;
  constructor(side: number) {
    this.side = side;
  }
  area(): number {
    return this.side * this.side;
  }
}
class Rectangle implements Shape {
  private height: number;
  private width: number;
  constructor(height: number, width: number) {
    this.height = height;
    this.width = width;
  }
  area(): number {
    return this.height * this.width;
  }
}
class Circle implements Shape {
  private radius: number;
  constructor(radius: number) {
    this.radius = radius;
  }
  area(): number {
    return PI * this.radius * this.radius;
  }
}

const data: ShapeData[] = [
  { kind: "square", side: 3 },
  { kind: "rectangle", height: 2, width: 5 },
  { kind: "circle", radius: 1 },
];
const objects: Shape[] = [new Square(3), new Rectangle(2, 5), new Circle(1)];

for (let i = 0; i < data.length; i++) {
  const proc = areaProcedural(data[i]);
  const oo = objects[i].area();
  assert.equal(proc, oo);
  console.log(`${data[i].kind.padEnd(10)} area: thủ tục=${proc.toFixed(4)}  OO=${oo.toFixed(4)}`);
}
console.log("cùng kết quả — nhưng hai cách DỄ/KHÓ ở hai chiều mở rộng ngược nhau.");
```

Kết quả chạy thật:

```
square     area: thủ tục=9.0000  OO=9.0000
rectangle  area: thủ tục=10.0000  OO=10.0000
circle     area: thủ tục=3.1416  OO=3.1416
```
```
cùng kết quả — nhưng hai cách DỄ/KHÓ ở hai chiều mở rộng ngược nhau.
```

Đây là cái **đối xứng ngược** mà cả chương xoay quanh:

> [!quote] Ch. 6 — Data/Object Anti-Symmetry (tr. 97)
> "Procedural code (code using data structures) makes it easy to add new functions without changing the existing data structures. OO code, on the other hand, makes it easy to add new classes without changing existing functions."
>
> *Code thủ tục (dùng cấu trúc dữ liệu) khiến việc **thêm hàm mới** dễ, không phải đụng cấu trúc dữ liệu cũ. Code OO thì ngược lại: khiến việc **thêm lớp mới** dễ, không phải đụng hàm cũ.*

Thêm hình `Triangle`? Bản OO chỉ cần thêm một lớp; bản thủ tục phải sửa `areaProcedural` (và mọi hàm `perimeterProcedural`, `drawProcedural`…). Nhưng thêm *hàm* `perimeter`? Bản thủ tục chỉ viết một hàm mới; bản OO phải sửa **mọi** lớp hình. Nên Uncle Bob kết:

> [!quote] Ch. 6 — Data/Object Anti-Symmetry (tr. 97)
> "Mature programmers know that the idea that everything is an object is a myth. Sometimes you really do want simple data structures with procedures operating on them."
>
> *Lập trình viên chín chắn biết rằng "mọi thứ đều là object" là một chuyện hoang đường. Đôi khi bạn thực sự muốn cấu trúc dữ liệu đơn giản với các thủ tục thao tác trên chúng.*

> [!note] Tự thử
> 1. Thêm hình `Triangle` (đáy × cao / 2). Đếm số chỗ bạn phải sửa ở bản thủ tục so với bản OO.
> 2. Thêm *hàm* `perimeter` cho cả hai cách. Giờ bên nào phải sửa nhiều hơn? Thấy "đối xứng ngược" chưa?
> 3. Bỏ một nhánh `case` trong `areaProcedural`. TypeScript có cảnh báo không? (Gợi ý: union type + switch cho ta "exhaustiveness" — một lợi thế cấu trúc dữ liệu năm 2026.)

## 4. Luật Demeter và "tàu hoả trật bánh"

> [!quote] Ch. 6 — The Law of Demeter (tr. 97)
> "a module should not know about the innards of the objects it manipulates."
>
> *một module không nên biết về **ruột gan** của những object mà nó thao tác.*

Chính xác hơn: một method `f` của lớp `C` chỉ nên gọi method của `C`, của object do `f` tạo ra, của object truyền vào `f`, và của object giữ trong biến thực thể của `C` — chứ không gọi tiếp lên những gì các hàm đó *trả về*. Nói nôm na: **nói chuyện với bạn bè, đừng nói với người lạ** (*talk to friends, not to strangers*). Dòng `ctxt.getOptions().getScratchDir().getAbsolutePath()` là một **train wreck** (tàu hoả trật bánh) — một chuỗi toa móc vào nhau.

Nhưng Uncle Bob rất sòng phẳng: đây *có* vi phạm Demeter hay không **phụ thuộc** vào `ctxt`, `Options`, `ScratchDir` là **object** (có hành vi, phải giấu ruột) hay chỉ là **cấu trúc dữ liệu** (vốn dĩ phơi ruột, Demeter không áp). Nếu là object thật, đừng *hỏi* nó về nội tạng — hãy *bảo* nó làm việc:

> [!quote] Ch. 6 — Hiding Structure (tr. 99)
> "If ctxt is an object, we should be telling it to do something; we should not be asking it about its internals."
>
> *Nếu `ctxt` là một object, ta nên **bảo** nó làm một việc; ta không nên **hỏi** nó về nội tạng của nó.*

Thay vì lấy đường dẫn thư mục tạm rồi tự ghép file, hãy bảo `ctxt.createScratchFileStream(className)` — để `ctxt` tự giấu ruột.

## 5. DTO, bean, Active Record và thể lai

Dạng thuần tuý của cấu trúc dữ liệu là lớp chỉ có biến public, không hàm — gọi là **DTO** (Data Transfer Object), rất hữu ích khi nói chuyện với CSDL hay parse message từ socket. Dạng **bean** (biến private + getter/setter) chỉ là "đóng gói giả", làm vài người OO thuần tuý thấy dễ chịu chứ thường chẳng lợi gì thêm. **Active Record** là DTO đặc biệt có thêm `save`/`find`, dịch thẳng từ bảng CSDL.

Cái cần tránh là **thể lai** (*hybrid*): nửa object nửa cấu trúc dữ liệu — vừa có hàm làm việc quan trọng, vừa phơi biến public. Chúng khiến *vừa khó thêm hàm vừa khó thêm kiểu* — tệ cả đôi đường. Lời giải cho Active Record: coi nó là cấu trúc dữ liệu thuần, rồi tạo *object riêng* chứa nghiệp vụ và giấu dữ liệu bên trong.

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Chương này **tiên tri một cách bất ngờ**: chính Uncle Bob nói "mọi thứ là object là chuyện hoang đường" (tr. 97) — và năm 2026, phong trào **data-oriented** đã lớn mạnh đúng theo hướng đó.
> - **"Clean Code, Horrible Performance" (Casey Muratori, 2023)** nhắm thẳng vào ví dụ `Shape` ở mục 3. Luận điểm: bản OO đa hình (mỗi hình một lớp, gọi ảo `area()`) trên phần cứng hiện đại có thể **chậm hơn nhiều lần** bản thủ tục `switch` phẳng — vì gọi ảo phá cache, cản dự đoán nhánh, chặn vector hoá. Với code nóng (game, đồ hoạ, xử lý số lượng lớn), *data-oriented design* (Mike Acton) chọn hẳn phía cấu trúc dữ liệu. Trớ trêu: sách bị trích dẫn như "phản diện", nhưng chính chương này đã *thừa nhận* trade-off đó.
> - **Cân bằng đúng (2026)**: đây **không** phải "OO sai, thủ tục đúng". Đó là chọn theo *chiều mở rộng* (như sách nói) **cộng** thêm chiều *hiệu năng*. Code nghiệp vụ hay đổi kiểu → nghiêng object. Code nóng, cố định kiểu, đổi nhiều phép → nghiêng cấu trúc dữ liệu/thủ tục.
> - **TypeScript làm phía "cấu trúc dữ liệu" mạnh hơn 2008**: union type + `switch` cho *exhaustiveness checking* (quên một `case` là lỗi biên dịch), nên nhược điểm "thêm kiểu phải sửa mọi hàm" được compiler canh giúp — an toàn hơn hẳn `instanceof` của Java 2008.
> - **Luật Demeter** vẫn hữu ích như *heuristic*, nhưng đừng cứng nhắc: với fluent API/builder (`query.where().orderBy().limit()`) hay DTO thuần, chuỗi gọi dài là *cố ý* và hoàn toàn ổn — đúng như sách đã lưu ý là "còn tuỳ object hay data structure".

## 7. Áp dụng vào codebase của bạn

> [!question] Áp dụng vào codebase của bạn
> 1. **Đếm getter/setter vô nghĩa.** Tìm một lớp toàn `get`/`set` bọc biến private. Nó thực ra là *object* (nên có hành vi) hay chỉ là *DTO* (thì để biến public/readonly cho xong)? Đừng đóng gói giả.
> 2. **Xác định chiều mở rộng.** Chọn một phần hệ thống bạn hay sửa. Bạn thêm *kiểu* mới (nghiêng object) hay thêm *phép* mới (nghiêng cấu trúc dữ liệu + union/switch) nhiều hơn? Thiết kế theo chiều đó.
> 3. **Soi một code nóng.** Nếu dự án có vòng lặp xử lý hàng triệu phần tử qua đa hình, thử đo. Đây là chỗ lời phản biện của Muratori đáng nghe nhất.
> 4. **Săn một train wreck.** Tìm một chuỗi `a.getB().getC().getD()`. Hỏi: B, C, D là object hay data? Nếu là object, thử thay bằng một lời "bảo nó làm việc".

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Data abstraction** | Phơi *bản chất* dữ liệu qua giao diện trừu tượng, không phơi cách lưu (tr. 93–95). |
| **Data/Object anti-symmetry** | Object & cấu trúc dữ liệu đối xứng ngược về chiều dễ mở rộng (tr. 95–97). |
| **Law of Demeter** | "Nói với bạn bè, đừng nói với người lạ" — đừng gọi vào ruột object (tr. 97–98). |
| **Train wreck** | Chuỗi gọi `a.getB().getC()...` móc vào nhau như toa tàu (tr. 98). |
| **DTO** | Data Transfer Object — lớp chỉ có biến public, không hàm (tr. 100). |
| **Active Record** | DTO + `save`/`find`, dịch thẳng từ bảng CSDL (tr. 101). |
| **Hybrid** | Thể lai nửa object nửa data — tệ cả đôi đường, nên tránh (tr. 99). |
| **Data-oriented design** | (2026) Chọn cấu trúc dữ liệu/thủ tục vì hiệu năng cache; đối trọng với lời khuyên OO. |

## 9. Câu hỏi tự kiểm tra

1. Vì sao "che giấu cài đặt" *không* đồng nghĩa với "thêm getter/setter"? *(tr. 94)*
2. Phát biểu "đối xứng ngược" giữa object và cấu trúc dữ liệu. Thêm *kiểu* mới thì bên nào dễ; thêm *hàm* mới thì bên nào dễ? *(tr. 97)*
3. Luật Demeter nói gì? Khi nào một chuỗi gọi *không* vi phạm nó? *(tr. 97–99)*
4. "Mọi thứ đều là object là chuyện hoang đường" liên quan thế nào tới data-oriented design 2026? *(tr. 97, Đối chiếu 2026)*
5. Thể lai (hybrid) là gì và vì sao nên tránh? *(tr. 99)*

## Tóm tắt một trang

```
BÀI 5 — OBJECT & CẤU TRÚC DỮ LIỆU: HAI THỨ ĐỐI XỨNG NGƯỢC
─────────────────────────────────────────────────────────
TRỪU TƯỢNG  che giấu cài đặt = TRỪU TƯỢNG HOÁ, không phải
            bọc getter/setter (tr.94). getPercentFuelRemaining
            > getGallons + getCapacity.

ĐỐI XỨNG NGƯỢC (tr.97)
   OBJECT        : thêm KIỂU dễ, thêm HÀM khó
   DATA + THỦ TỤC: thêm HÀM dễ, thêm KIỂU khó
   areaProcedural(switch)  ==  shape.area()  (cùng kết quả)
   "mọi thứ là object = chuyện hoang đường" (tr.97)

DEMETER  "nói với bạn bè, đừng nói với người lạ" (tr.98).
         train wreck a.getB().getC(). BẢO object làm việc,
         đừng HỎI ruột nó (tr.99). Tuỳ object hay data.

DTO/bean/Active Record = cấu trúc dữ liệu. Tránh THỂ LAI.

2026  Muratori "Clean Code, Horrible Performance": OO đa hình
      có thể chậm hơn switch phẳng (data-oriented design).
      Chọn theo chiều-mở-rộng + hiệu-năng. TS union+switch cho
      exhaustiveness → phía data an toàn hơn Java 2008.
```

## Nguồn

- **Robert C. Martin**, *Clean Code* (Prentice Hall, 2008) — **Chương 6, "Objects and Data Structures"** (`tr. 93–102`): vì sao giữ biến private (tr. 93); trừu tượng hoá dữ liệu, Point/Vehicle (tr. 93–95); data/object anti-symmetry, ví dụ Shape thủ tục vs đa hình (tr. 95–97); Luật Demeter, train wreck, "nói với bạn bè" (tr. 97–98); hiding structure, "bảo object làm việc" (tr. 99); DTO, bean, Active Record, hybrid (tr. 99–101); kết luận (tr. 101). `tai_lieu/Clean.Code.2008.8.pdf`
- Phản biện 2026 dẫn từ ngoài sách: Casey Muratori, *"Clean Code, Horrible Performance"* (2023); Mike Acton, *data-oriented design*; TypeScript exhaustiveness checking.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 31`.

---

**Bản đồ khoá học:** [Bài 0 — Clean Code là gì](bai_00_clean_code_la_gi.md) · [Bài 1 — Đặt tên](bai_01_dat_ten.md) · [Bài 2 — Hàm](bai_02_ham.md) · [Bài 3 — Comment](bai_03_comment.md) · [Bài 4 — Định dạng](bai_04_dinh_dang.md) · [Bài 5 ← bạn đang ở đây] · [Bài 6 — Xử lý lỗi](bai_06_xu_ly_loi.md) · [Bài 7 — Ranh giới](bai_07_ranh_gioi.md) · [Bài 8 — Unit test](bai_08_unit_test.md) · [Bài 9 — Class](bai_09_class.md) · [Bài 10 — Hệ thống](bai_10_he_thong.md) · [Bài 11 — Thiết kế nổi lên](bai_11_thiet_ke_noi_len.md) · [Bài 12 — Concurrency](bai_12_concurrency.md) · [Bài 13 — Xem code sạch nảy sinh](bai_13_xem_code_nay_sinh.md) · [Bài 14 — Refactor ngoài đời](bai_14_refactor_ngoai_doi.md) · [Bài 15 — Danh mục mùi code](bai_15_danh_muc_mui_code.md)

Xem thêm [README khoá học](../README.md).
