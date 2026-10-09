# Bài 3 — SOLID (2): LSP, ISP, DIP

> [!info] Về bài này
> Dựng từ **Phần III — Design Principles**: **Ch.9 LSP**, **Ch.10 ISP**, **Ch.11 DIP** của *Clean Architecture* (Robert C. Martin, 2017 — `tai_lieu/`, `tr. 77–92`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 27`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Nối [Bài 2](bai_02_solid_srp_ocp.md) (SRP, OCP). DIP là bản lề mở sang Phần IV–V. Mức *kiến trúc*, không lặp mức class ([`clean-code` Bài 9](../../clean-code/bai_hoc/bai_09_class.md)).
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [LSP: thay thế được](#1-lsp-thay-thế-được)
2. [Code minh hoạ: bài toán Square/Rectangle](#2-code-minh-hoạ-bài-toán-squarerectangle)
3. [LSP ở tầm kiến trúc](#3-lsp-ở-tầm-kiến-trúc)
4. [ISP: đừng phụ thuộc thứ bạn không dùng](#4-isp-đừng-phụ-thuộc-thứ-bạn-không-dùng)
5. [DIP: phụ thuộc trừu tượng, tránh concrete khả biến](#5-dip-phụ-thuộc-trừu-tượng-tránh-concrete-khả-biến)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào dự án của bạn](#7-áp-dụng-vào-dự-án-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. LSP: thay thế được

Barbara Liskov (1988) định nghĩa *subtype* qua một tính chất thay thế: nếu mọi chương trình `P` viết theo kiểu `T` vẫn hành xử y hệt khi ta thay một object kiểu `T` bằng object kiểu `S`, thì `S` là subtype của `T`. Nói gọn: **lớp con phải thay được lớp cha mà chương trình không đổi hành vi**. Ví dụ "đúng" của sách: `License` với hai subtype `PersonalLicense` và `BusinessLicense` — ứng dụng không hề quan tâm đang dùng cái nào; cả hai thay thế được cho `License`. Ví dụ "sai" là bài toán kinh điển dưới đây.

## 2. Code minh hoạ: bài toán Square/Rectangle

> [!quote] Ch. 9 — The Square/Rectangle Problem (tr. 78)
> "Square is not a proper subtype of Rectangle because the height and width of the Rectangle are independently mutable; in contrast, the height and width of the Square must change together."
>
> *`Square` **không** phải subtype hợp lệ của `Rectangle`, vì chiều cao và chiều rộng của `Rectangle` đổi **độc lập**; trong khi của `Square` thì **phải đổi cùng nhau**.*

```typescript
import { strict as assert } from "node:assert";

// ===== VI PHẠM LSP: Square "là" Rectangle nhưng phá bất biến =====
class Rectangle {
  protected w = 0;
  protected h = 0;
  setW(w: number): void { this.w = w; }
  setH(h: number): void { this.h = h; }
  area(): number { return this.w * this.h; }
}
class Square extends Rectangle {
  setW(w: number): void { this.w = w; this.h = w; } // w,h phải đổi cùng nhau
  setH(h: number): void { this.w = h; this.h = h; }
}

// chương trình P mong đợi hành vi của Rectangle
function resizeAndCheck(r: Rectangle): number {
  r.setW(5);
  r.setH(2);
  return r.area(); // kỳ vọng 5*2 = 10
}

console.log("Rectangle:", resizeAndCheck(new Rectangle()), "(kỳ vọng 10)");
console.log("Square   :", resizeAndCheck(new Square()), "(ra 4 — setH ghi đè cả w!)");
assert.equal(resizeAndCheck(new Rectangle()), 10);
assert.notEqual(resizeAndCheck(new Square()), 10); // Square KHÔNG thay được Rectangle

// ===== TÔN TRỌNG LSP: không ép "là-một"; mỗi hình tự tính, bất biến =====
interface Shape { area(): number; }
class Rect implements Shape {
  private w: number; private h: number;
  constructor(w: number, h: number) { this.w = w; this.h = h; }
  area(): number { return this.w * this.h; }
}
class Sq implements Shape {
  private side: number;
  constructor(side: number) { this.side = side; }
  area(): number { return this.side * this.side; }
}
const shapes: Shape[] = [new Rect(5, 2), new Sq(4)];
console.log("LSP-OK areas:", shapes.map((s) => s.area()), "— ai cũng thay được qua Shape");
```

Kết quả chạy thật:

```
Rectangle: 10 (kỳ vọng 10)
Square   : 4 (ra 4 — setH ghi đè cả w!)
LSP-OK areas: [ 10, 16 ] — ai cũng thay được qua Shape
```

`resizeAndCheck` tin nó đang nói chuyện với `Rectangle` (đặt rộng 5, cao 2 → diện tích 10). Nhưng `Square` ghi đè khiến `setH(2)` kéo cả `w=2` → ra 4. Cách "chữa" duy nhất là nhét `if (r instanceof Square)` vào chương trình — tức là *chương trình phải biết kiểu cụ thể*, và thế thì các kiểu đó **không còn thay thế được**. Bản tôn trọng LSP bỏ quan hệ "là-một" gượng ép: `Rect` và `Sq` cùng `implements Shape`, mỗi lớp tự tính, ai cũng thay được qua `Shape`.

> [!note] Tự thử
> 1. Thêm `if (r instanceof Square)` vào `resizeAndCheck` để "chữa". Code có còn sạch không? Bạn vừa làm chương trình *phụ thuộc kiểu cụ thể* — đó là dấu hiệu gì?
> 2. Thêm `Circle` vào bản LSP-OK. `shapes.map(s => s.area())` có cần đổi không?
> 3. Vì sao "Square is-a Rectangle" đúng trong *toán học* mà sai trong *code*? (Gợi ý: bất biến về *tính khả biến* của w/h.)

## 3. LSP ở tầm kiến trúc

Thuở đầu OO, LSP được coi là cách "hướng dẫn dùng kế thừa". Nhưng Uncle Bob mở rộng: LSP áp cho *mọi* quan hệ interface/implementation — kể cả giữa các component và dịch vụ qua REST. Sách kể ca một hệ gọi taxi: nếu một nhà cung cấp taxi hiện thực REST API *lệch chuẩn* (ví dụ hoán field), hệ thống buộc phải cài thêm các `if` đặc biệt để xử lý ngoại lệ đó — và những `if` ấy chính là *vết LSP rò rỉ vào kiến trúc*, làm hệ thống phức tạp dần. Nói cách khác: LSP không chỉ là chuyện kế thừa — nó là nguyên tắc về *tính thay thế được của mọi ranh giới*.

## 4. ISP: đừng phụ thuộc thứ bạn không dùng

ISP mức class nói "đừng ép một lớp hiện thực interface có method nó không cần". Nhưng gốc rễ sâu hơn, ở tầm kiến trúc:

> [!quote] Ch. 10 — ISP and Architecture (tr. 85)
> "In general, it is harmful to depend on modules that contain more than you need."
>
> *Nhìn chung, **phụ thuộc vào module chứa nhiều hơn mức bạn cần** là có hại.*

Ví dụ: hệ `S` dùng framework `F`, mà `F` lại buộc vào database `D`. Dù `S` chẳng đụng tính năng nào của `D`, một thay đổi (hay một *lỗi*) trong `D` vẫn có thể buộc `F` và `S` phải build/deploy lại, thậm chí hỏng theo. Bài học: *phụ thuộc vào thứ mang theo "hành lý" bạn không cần* là nguồn rắc rối — nối thẳng sang [Bài 7 (Ranh giới)](bai_06_ranh_gioi_dependency_rule.md) và "database là chi tiết" ([Bài 9](bai_09_chi_tiet.md)).

## 5. DIP: phụ thuộc trừu tượng, tránh concrete khả biến

Đây là nguyên tắc *bản lề* của cả cuốn sách — hiện thân trực tiếp của sức mạnh OO ở [Bài 1](bai_01_he_hinh_lap_trinh.md):

> [!quote] Ch. 11 — DIP (tr. 87)
> "the most flexible systems are those in which source code dependencies refer only to abstractions, not to concretions."
>
> *những hệ thống **linh hoạt nhất** là những hệ mà phụ thuộc mã nguồn chỉ trỏ tới **trừu tượng**, không trỏ tới **cụ thể**.*

Nhưng Uncle Bob rất thực tế: ta *không* đảo mọi phụ thuộc concrete. `String` của Java là concrete nhưng cực **ổn định** (stable) — hiếm đổi, nên cứ phụ thuộc thoải mái. Thứ cần tránh là **concrete khả biến (volatile)** — module ta đang tích cực phát triển, hay đổi:

> [!quote] Ch. 11 — DIP (tr. 87)
> "It is the volatile concrete elements of our system that we want to avoid depending on."
>
> *Chính những phần tử **concrete khả biến** của hệ thống mới là thứ ta muốn tránh phụ thuộc.*

Vì "mọi thay đổi interface đều kéo theo thay đổi ở implementation, nhưng ngược lại thì không" → **interface ổn định hơn implementation** (Stable Abstractions). Từ đó rút ra các luật code rất cụ thể:

| Luật DIP | Ý |
| :--- | :--- |
| Đừng trỏ tới concrete **khả biến** | trỏ tới interface trừu tượng; buộc dùng **Abstract Factory** để tạo object (Bài 10 `clean-code`) |
| Đừng kế thừa từ concrete khả biến | kế thừa là quan hệ cứng nhất; dùng rất dè |
| Đừng override hàm concrete | override thường kéo theo phụ thuộc mã nguồn vào concrete |

> [!quote] Ch. 11 — Stable Abstractions (tr. 88)
> "Don't refer to volatile concrete classes. Refer to abstract interfaces instead."
>
> *Đừng trỏ tới lớp concrete khả biến. Hãy trỏ tới interface trừu tượng.*

Demo của DIP đã làm ở [Bài 1 (`copy`)](bai_01_he_hinh_lap_trinh.md) và [`clean-code` Bài 9 (`Portfolio`)](../../clean-code/bai_hoc/bai_09_class.md) — nên ở đây tập trung vào LSP; DIP sẽ trở lại thành *Dependency Rule* ở [Bài 6](bai_06_ranh_gioi_dependency_rule.md).

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Ba nguyên tắc này bền, nhưng mỗi cái có một sắc thái 2026:
> - **LSP vượt khỏi kế thừa — đúng và càng quan trọng.** Năm 2026 kế thừa ít dùng (ưu tiên hợp thành), nhưng LSP sống khoẻ ở **ranh giới API/dịch vụ**: mọi implementation của một interface, mọi phiên bản của một REST/gRPC contract, phải *thay thế được*. Đây là nền của **contract testing** (Pact) và **versioning**. Bài học taxi của sách chính là chuyện API lệch chuẩn thời microservice.
> - **ISP ↔ "phụ thuộc tối thiểu" thời package.** Năm 2026, "đừng phụ thuộc thứ bạn không dùng" là lý lẽ chống **dependency bloat** (một `npm install` kéo hàng trăm gói transitive), và cổ vũ tree-shaking, interface hẹp, và cảnh giác với framework "nuốt trọn" (nối [Bài 9](bai_09_chi_tiet.md)).
> - **DIP = trái tim, nhưng đừng cực đoan (ponytail).** "Phụ thuộc trừu tượng" bị lạm thành "tạo interface cho MỌI lớp" — thứ mà chính Uncle Bob *không* bảo (ông nói chỉ tránh concrete **khả biến**, cứ phụ thuộc cái **ổn định** như `String`). Tạo `IUserServiceInterface` cho một lớp duy nhất không bao giờ có implementation thứ hai là over-engineering. Phân biệt *volatile* vs *stable* là chìa khoá thực dụng.
> - **Phê bình SOLID (tiếp Bài 2):** phe data-oriented vẫn cho rằng DIP/đa hình bừa bãi hại hiệu năng; đúng với code nóng, ít liên quan code nghiệp vụ.

## 7. Áp dụng vào dự án của bạn

> [!question] Áp dụng vào dự án của bạn
> 1. **Săn vết LSP.** Tìm một chỗ có `instanceof` / `if (type === ...)` để xử lý riêng một subtype. Đó là dấu hiệu subtype *không* thay thế được — vi phạm LSP rò rỉ.
> 2. **Soi "hành lý thừa" (ISP).** Dependency nào bạn kéo vào chỉ để dùng *một* tính năng nhỏ nhưng phải gánh cả khối? Có interface/gói hẹp hơn không?
> 3. **Phân loại volatile vs stable (DIP).** Liệt kê các concrete mà core logic phụ thuộc. Cái nào *khả biến* (bạn đang phát triển, hay đổi) → nên chèn abstraction; cái nào *ổn định* (stdlib) → cứ để. Đừng abstract hoá cái ổn định.

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| :--- | :--- |
| **LSP** | Lớp con/implementation phải thay được lớp cha mà chương trình không đổi hành vi (tr. 77). |
| **Square/Rectangle problem** | Ví dụ kinh điển vi phạm LSP vì bất biến w/h khác nhau (tr. 78). |
| **ISP** | Đừng phụ thuộc module chứa nhiều hơn mức bạn cần (tr. 85). |
| **DIP** | Hệ linh hoạt nhất: phụ thuộc trừu tượng, không concrete (tr. 87). |
| **Volatile vs stable** | Tránh phụ thuộc concrete *khả biến*; cứ phụ thuộc concrete *ổn định* như `String` (tr. 87). |
| **Stable Abstractions** | Interface ổn định hơn implementation → ưu tiên phụ thuộc interface (tr. 88). |

## 9. Câu hỏi tự kiểm tra

1. Phát biểu LSP bằng lời thường. Ví dụ `License` "đúng", Square/Rectangle "sai" khác nhau ở đâu? *(tr. 77–78)*
2. Trong demo, vì sao `Square` làm `resizeAndCheck` ra 4 thay vì 10? Cách "chữa" bằng `instanceof` sai ở đâu? *(mục 2)*
3. ISP ở tầm kiến trúc cảnh báo điều gì? Ví dụ S→F→D minh hoạ ra sao? *(tr. 85)*
4. DIP: vì sao ta *không* đảo phụ thuộc vào `String` nhưng *nên* đảo với module đang phát triển? *(tr. 87)*
5. Ba luật code cụ thể của DIP là gì? *(tr. 88)*

## Tóm tắt một trang

```
BÀI 3 — SOLID (2): LSP, ISP, DIP
─────────────────────────────────────────────────────────
LSP (tr.77)  lớp con THAY ĐƯỢC lớp cha, chương trình không đổi.
   Square/Rectangle (tr.78): w,h của Square phải đổi cùng nhau →
   resizeAndCheck ra 4 thay vì 10. "Chữa" bằng instanceof = thua.
   Tầm kiến trúc: vết LSP (if đặc biệt) rò rỉ vào hệ (ca taxi REST).

ISP (tr.85)  "phụ thuộc module chứa NHIỀU HƠN mức cần là CÓ HẠI".
   S→F→D: đổi/lỗi trong D kéo F, S deploy lại dù S không đụng D.

DIP (tr.87)  "hệ linh hoạt nhất: phụ thuộc TRỪU TƯỢNG, không concrete".
   Tránh concrete KHẢ BIẾN (volatile); cứ phụ thuộc cái ỔN ĐỊNH (String).
   Luật: đừng trỏ/kế thừa/override concrete khả biến (tr.88) → Abstract Factory.

2026  LSP ↔ contract testing / API versioning. ISP ↔ chống dependency
   bloat. DIP = trái tim NHƯNG đừng tạo interface cho MỌI lớp
   (chỉ tránh volatile). → Dependency Rule, Bài 6.
```

## Nguồn

- **Robert C. Martin**, *Clean Architecture* (Prentice Hall, 2017) — **Ch.9 "LSP"** (`tr. 77–82`): định nghĩa Liskov 1988, ví dụ License (tr. 77); Square/Rectangle (tr. 78); LSP và kiến trúc, ca taxi REST (tr. 79–82). **Ch.10 "ISP"** (`tr. 83–86`): ISP và ngôn ngữ (tr. 83–84); "harmful to depend on modules that contain more than you need", S→F→D (tr. 85); kết luận (tr. 86). **Ch.11 "DIP"** (`tr. 87–92`): "most flexible… abstractions not concretions", volatile vs stable, String (tr. 87); Stable Abstractions, ba luật code, Abstract Factory (tr. 88–90); component ổn định (tr. 91–92). `tai_lieu/Clean.Architecture.2017.9.pdf`
- Bối cảnh 2026 dẫn từ ngoài sách: contract testing (Pact), API versioning; dependency bloat / tree-shaking; phê bình over-abstraction.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 27`.

---

**Bản đồ khoá học:** [Bài 0 — Hai giá trị](bai_00_hai_gia_tri.md) · [Bài 1 — Ba hệ hình lập trình](bai_01_he_hinh_lap_trinh.md) · [Bài 2 — SOLID (1): SRP, OCP](bai_02_solid_srp_ocp.md) · [Bài 3 ← bạn đang ở đây] · [Bài 4 — Nguyên tắc Component](bai_04_nguyen_tac_component.md) · [Bài 5 — Kiến trúc là gì & Độc lập](bai_05_kien_truc_va_doc_lap.md) · [Bài 6 — Ranh giới & Dependency Rule](bai_06_ranh_gioi_dependency_rule.md) · [Bài 7 — Business Rules & The Clean Architecture](bai_07_clean_architecture.md) · [Bài 8 — Humble Object, Main, Services](bai_08_humble_main_services.md) · [Bài 9 — Chi tiết: DB, Web, Framework](bai_09_chi_tiet.md) · [Bài 10 — The Missing Chapter: đóng gói](bai_10_dong_goi.md) · [Bài 11 — Case study & tổng kết](bai_11_case_study.md)

Xem thêm [README khoá học](../README.md).
