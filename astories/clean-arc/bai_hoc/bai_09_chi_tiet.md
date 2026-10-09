# Bài 9 — Chi tiết: Database, Web, Framework đều là *chi tiết*

> [!info] Về bài này
> Dựng từ **Phần VI — Details**: **Ch.30 "The Database Is a Detail"**, **Ch.31 "The Web Is a Detail"**, **Ch.32 "Frameworks Are Details"** của *Clean Architecture* (Robert C. Martin, 2017 — `tai_lieu/`, `tr. 277–296`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 27`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Phần VI trả lời: những thứ ta hay coi là "nền tảng" của dự án — DB, web, framework — thực ra là *chi tiết* bị đẩy ra rìa vòng tròn ([Bài 7](bai_07_clean_architecture.md)).
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: thứ ta tưởng là nền tảng, hoá ra là chi tiết](#1-mở-đầu-thứ-ta-tưởng-là-nền-tảng-hoá-ra-là-chi-tiết)
2. [Database là chi tiết — data model mới là kiến trúc](#2-database-là-chi-tiết--data-model-mới-là-kiến-trúc)
3. [Web là chi tiết — chỉ là một dao động](#3-web-là-chi-tiết--chỉ-là-một-dao-động)
4. [Framework là chi tiết — đừng cưới nó](#4-framework-là-chi-tiết--đừng-cưới-nó)
5. [Code minh hoạ: giữ framework ở arm's length](#5-code-minh-hoạ-giữ-framework-ở-arms-length)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào dự án của bạn](#7-áp-dụng-vào-dự-án-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mở đầu: thứ ta tưởng là nền tảng, hoá ra là chi tiết

Nhiều dự án bắt đầu bằng câu hỏi "dùng database nào? framework nào?" — như thể đó là *nền móng*. Phần VI lật ngược: trong vòng tròn Clean Architecture ([Bài 7](bai_07_clean_architecture.md)), tất cả chúng nằm ở **vòng ngoài cùng** — là *chi tiết*, là *cơ chế*, bị đẩy xa khỏi business rules. Bảng tổng:

| Thứ | Thường bị coi là | Thật ra là | Vòng |
| :--- | :--- | :--- | :---: |
| Database | nền tảng dữ liệu | **chi tiết** (data *model* mới là kiến trúc) | ngoài cùng |
| Web / GUI | kiến trúc ứng dụng | **chi tiết** (delivery mechanism) | ngoài cùng |
| Framework | bộ khung dự án | **chi tiết** (công cụ để dùng) | ngoài cùng |

## 2. Database là chi tiết — data model mới là kiến trúc

Uncle Bob tách rạch ròi *data model* (quan trọng) khỏi *database* (chi tiết):

> [!quote] Ch. 30 — The Database Is a Detail (tr. 277)
> "the database is not the data model. The database is piece of software. The database is a utility that provides access to the data."
>
> *database **không phải** là data model. Database là một **phần mềm**, một tiện ích cung cấp quyền truy cập dữ liệu.* (Nguyên văn sách in "is piece", thiếu "a".)

*Cấu trúc* bạn trao cho dữ liệu (data model) thì cực kỳ hệ trọng với kiến trúc. Nhưng *công cụ* lưu nó — Oracle, Postgres, Mongo, hay file phẳng — là cơ chế mức thấp, và "kiến trúc sư giỏi không để cơ chế mức thấp làm ô nhiễm kiến trúc hệ thống". Kết luận chương gói trong hai câu:

> [!quote] Ch. 30 — Conclusion (tr. 283)
> "The data is significant. The database is a detail."
>
> *Dữ liệu thì **hệ trọng**. Database thì là **chi tiết**.*

## 3. Web là chi tiết — chỉ là một dao động

Web nghe như một cuộc cách mạng kiến trúc, nhưng Uncle Bob đặt nó vào lịch sử dài:

> [!quote] Ch. 31 — The Web Is a Detail (tr. 285)
> "the web is just the latest in a series of oscillations that our industry has gone through since the 1960s."
>
> *web chỉ là **dao động** mới nhất trong một chuỗi mà ngành ta đã trải qua từ thập niên 1960.*

Con lắc liên tục đung đưa giữa "tập trung sức tính toán ở máy chủ" và "đẩy ra client": mainframe + terminal → PC độc lập → client/server → web (server-side) → rich client (JS) → đám mây… Mỗi lần người ta lại tưởng "đây là hồi kết". Với kiến trúc sư nhìn dài hạn, **GUI/web chỉ là một IO device, một delivery mechanism** — một chi tiết. Nghiệp vụ cốt lõi không nên biết nó đang được giao qua web, desktop, hay CLI (đúng "keeping options open" ở [Bài 5](bai_05_kien_truc_va_doc_lap.md)).

## 4. Framework là chi tiết — đừng cưới nó

Chương gai góc nhất Phần VI. Tác giả framework mời bạn vào một *cuộc hôn nhân một chiều*:

> [!quote] Ch. 32 — The Risks (tr. 292)
> "the author is asking you to marry the framework—to make a huge, long-term commitment to that framework. […] It's a one-directional marriage. You take on all the risk and burden; the framework author takes on nothing at all."
>
> *tác giả đang mời bạn **cưới framework** — một cam kết khổng lồ, sâu rộng. […] Đó là **hôn nhân một chiều**. Bạn gánh toàn bộ rủi ro và gánh nặng; tác giả framework chẳng gánh gì.*

Framework tiến hoá theo nhu cầu *của tác giả*, không của bạn; có thể bỏ tính năng bạn cần, đổi API, hoặc chết. Vậy nên:

> [!quote] Ch. 32 — The Solution (tr. 293)
> "Don't marry the framework! […] Keep it at arm's length. Treat the framework as a detail that belongs in one of the outer circles of the architecture."
>
> *Đừng cưới framework! […] Giữ nó ở **khoảng cách một cánh tay**. Coi framework là một chi tiết thuộc về một trong các vòng ngoài của kiến trúc.*

Cụ thể: nếu framework đòi bạn kế thừa business object từ base class của nó — **nói không**; hãy tạo *proxy* và giữ proxy trong các component là plugin của business rules.

## 5. Code minh hoạ: giữ framework ở arm's length

```typescript
import { strict as assert } from "node:assert";

// ===== Business object THUẦN: không biết framework nào =====
class Order {
  private total: number;
  constructor(total: number) { this.total = total; }
  payable(): number { return this.total > 100 ? this.total - 10 : this.total; } // business rule
}

// ===== Framework (vòng ngoài) đòi một "persistable" có serialize() =====
interface FrameworkPersistable { serialize(): string; }
function frameworkSave(p: FrameworkPersistable): string {
  return `[framework] saved: ${p.serialize()}`;
}

// ===== CÁCH ĐÚNG: PROXY bọc Order cho framework, giữ Order ở arm's length =====
class OrderFrameworkProxy implements FrameworkPersistable {
  private order: Order;
  constructor(order: Order) { this.order = order; }
  serialize(): string { return `order:${this.order.payable()}`; }
}

const order = new Order(150);
assert.equal(order.payable(), 140); // business rule test được, KHÔNG cần framework
console.log("payable (thuần):", order.payable());
console.log(frameworkSave(new OrderFrameworkProxy(order))); // framework chỉ chạm proxy
console.log("Order không kế thừa/không import framework — framework ở 'arm's length'.");
```

Kết quả chạy thật:

```
payable (thuần): 140
[framework] saved: order:140
Order không kế thừa/không import framework — framework ở 'arm's length'.
```

`Order` thuần nghiệp vụ: không `extends` base class nào của framework, không `import` framework. Nó test được bằng một dòng `assert` mà chẳng cần dựng framework. Khi framework cần một "persistable", ta đưa `OrderFrameworkProxy` — proxy sống ở vòng ngoài, hiện thực interface của framework và *gọi vào* `Order`. Nếu mai đổi framework, chỉ proxy phải viết lại; `Order` bất động. Đây đúng "derive proxies instead" của Uncle Bob, và là DIP ([Bài 3](bai_03_solid_lsp_isp_dip.md)) áp vào ranh giới framework.

> [!note] Tự thử
> 1. Cho `Order` `extends FrameworkEntity` (kế thừa base class framework). Giờ test `payable()` có cần dựng framework không? Đổi framework thì `Order` sao?
> 2. Thêm framework thứ hai (`OtherFrameworkPersistable` với `toJSON()`). Viết proxy thứ hai. `Order` có đổi dòng nào không?
> 3. Nếu proxy *cũng* lọt vào vòng trong (business rule import proxy), điều gì hỏng? (Gợi ý: proxy phải ở vòng *ngoài*.)

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Ba "chi tiết" này là nơi Clean Architecture **đúng về nguyên tắc nhưng gây tranh cãi về mức độ** năm 2026:
> - **"Database là chi tiết" — đúng, nhưng ORM/repository đã làm chuyện này gần như miễn phí.** Prisma, TypeORM, Drizzle, EF Core cho đổi backend qua config; repository pattern cô lập truy vấn. Nhưng (ponytail) cảnh báo ngược: *lạm dụng* abstraction DB (generic repository trên generic repository) để "database là chi tiết" thường là over-engineering — nhiều app CRUD gọi thẳng query builder là *đủ*. Và phe "database-first" (schema là trung tâm, như sự kiện/CQRS) lập luận data model *quan trọng tới mức* đáng để kiến trúc xoay quanh nó.
> - **"Web là chi tiết / dao động" — tiên tri chính xác.** Từ 2017: SSR (Next.js) ↔ SPA ↔ server components ↔ edge ↔ islands — con lắc Uncle Bob mô tả vẫn đung đưa đúng y. Bài học giữ nguyên: đừng khoá nghiệp vụ vào một vị trí render.
> - **"Đừng cưới framework" — lý tưởng đẹp, thực tế phải cân.** Đây là chỗ va chạm mạnh nhất với thực tế 2026: Rails, Spring Boot, Next.js, NestJS *cố ý* yêu cầu bạn "cưới" để đổi lấy tốc độ khổng lồ. Với **startup/sản phẩm đời ngắn**, ôm framework là lựa chọn đúng (xem Bài 0, 5, 7). "Arm's length" trả giá bằng indirection + boilerplate; đáng trả khi *nghiệp vụ sống lâu hơn framework*. Biết đặt cược bên nào, theo vòng đời dự kiến của sản phẩm, mới là nghề.
> - **AI 2026:** LLM sinh code gắn chặt framework rất nhanh (scaffold cả app Next.js một prompt). Càng khiến "đừng cưới framework" khó giữ — nhưng cũng khiến *business rule thuần, test được* thành phần đáng giữ sạch bằng tay.
> - **Vẫn vàng:** business rule không nên `import` DB/web/framework; đổi được chi tiết mà không đụng nghiệp vụ là thước đo kiến trúc.

## 7. Áp dụng vào dự án của bạn

> [!question] Áp dụng vào dự án của bạn
> 1. **Grep framework trong core.** Tìm trong business logic các `import` tên ORM/web framework/UI lib. Mỗi cái là một "mối hôn nhân" — core đã cưới chi tiết. Đánh giá: đáng không, hay nên dựng proxy?
> 2. **Thử phép "đổi DB tưởng tượng".** Nếu phải đổi Postgres→Mongo, bao nhiêu file *business* phải đổi? Lý tưởng là 0 (chỉ tầng gateway). Con số thật nói lên DB đang là "chi tiết" hay "nền tảng" trong dự án bạn.
> 3. **Định vị cược framework.** Sản phẩm bạn dự kiến sống bao lâu? Ngắn → ôm framework có thể đúng. Dài/nghiệp vụ phức tạp → giữ core ở arm's length. Quyết có ý thức, đừng mặc định.

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| :--- | :--- |
| **Detail (chi tiết)** | Thứ ở vòng ngoài cùng: DB, web, framework — cơ chế, không phải chính sách (Ch.30–32). |
| **Data model vs database** | Data model (cấu trúc dữ liệu) = kiến trúc; database (công cụ lưu) = chi tiết (tr. 277, 283). |
| **Delivery mechanism** | Web/GUI chỉ là cách *giao* phần mềm, một IO device — chi tiết (tr. 285). |
| **Oscillation** | Con lắc tập trung↔phân tán sức tính toán qua các thập niên; web chỉ là một nhịp (tr. 285). |
| **One-directional marriage** | Cưới framework: bạn gánh hết rủi ro, tác giả framework gánh 0 (tr. 292). |
| **Arm's length / proxy** | Giữ framework ở vòng ngoài; derive proxy thay vì kế thừa base class của nó (tr. 293). |

## 9. Câu hỏi tự kiểm tra

1. Phân biệt "data model" và "database". Cái nào là kiến trúc, cái nào là chi tiết? *(tr. 277, 283)*
2. Vì sao Uncle Bob gọi web là "một dao động"? Điều đó khuyên kiến trúc sư gì? *(tr. 285)*
3. "Hôn nhân một chiều" với framework nghĩa là gì? Ai gánh rủi ro? *(tr. 292)*
4. Trong demo, vì sao `Order` test được mà không cần framework? Proxy làm gì? *(mục 5)*
5. Năm 2026, khi nào "ôm framework" (ngược lời khuyên) lại là lựa chọn đúng? *(Đối chiếu 2026)*

## Tóm tắt một trang

```
BÀI 9 — CHI TIẾT: DB, WEB, FRAMEWORK ĐỀU LÀ CHI TIẾT
─────────────────────────────────────────────────────────
Thứ ta tưởng là NỀN TẢNG → thật ra là CHI TIẾT ở vòng ngoài cùng.

DATABASE  "database KHÔNG phải data model... là một tiện ích" (tr.277).
   "Dữ liệu hệ trọng. Database là chi tiết" (tr.283). Data MODEL = kiến trúc.

WEB  "web chỉ là dao động mới nhất từ thập niên 1960" (tr.285).
   Con lắc tập trung↔phân tán. GUI/web = delivery mechanism, IO device.

FRAMEWORK  "cưới framework = HÔN NHÂN MỘT CHIỀU, bạn gánh hết rủi ro" (tr.292).
   "ĐỪNG cưới framework! Giữ ở arm's length... chi tiết ở vòng ngoài" (tr.293).
   DEMO: Order thuần + OrderFrameworkProxy. Order test được, không import framework.

2026  ORM/repository làm "DB là chi tiết" gần như free (đừng lạm abstraction).
   "web là dao động" tiên tri đúng (SSR↔SPA↔edge↔islands). "đừng cưới
   framework" va thực tế: startup/đời-ngắn ôm framework là ĐÚNG. Cược
   theo vòng đời sản phẩm.
```

## Nguồn

- **Robert C. Martin**, *Clean Architecture* (Prentice Hall, 2017) — **Ch.30 "The Database Is a Detail"** (`tr. 277–284`): data model ≠ database, "database is a utility", quan hệ/Codd 1970, kết luận "the data is significant, the database is a detail" (tr. 277–283). **Ch.31 "The Web Is a Detail"** (`tr. 285–290`): "web is just the latest in a series of oscillations", GUI là delivery mechanism, ca company Q (tr. 285–289). **Ch.32 "Frameworks Are Details"** (`tr. 291–296`): framework marriage bất đối xứng, "one-directional marriage", các rủi ro, "don't marry the framework", "arm's length", derive proxies (tr. 291–295). `tai_lieu/Clean.Architecture.2017.9.pdf`
- Bối cảnh 2026 dẫn từ ngoài sách: Prisma/Drizzle/EF Core; con lắc SSR/SPA/server components/edge; framework-first (Rails/Next.js/NestJS); AI scaffolding.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 27`.

---

**Bản đồ khoá học:** [Bài 0 — Hai giá trị](bai_00_hai_gia_tri.md) · [Bài 1 — Ba hệ hình lập trình](bai_01_he_hinh_lap_trinh.md) · [Bài 2 — SOLID (1): SRP, OCP](bai_02_solid_srp_ocp.md) · [Bài 3 — SOLID (2): LSP, ISP, DIP](bai_03_solid_lsp_isp_dip.md) · [Bài 4 — Nguyên tắc Component](bai_04_nguyen_tac_component.md) · [Bài 5 — Kiến trúc là gì & Độc lập](bai_05_kien_truc_va_doc_lap.md) · [Bài 6 — Ranh giới & Dependency Rule](bai_06_ranh_gioi_dependency_rule.md) · [Bài 7 — Business Rules & The Clean Architecture](bai_07_clean_architecture.md) · [Bài 8 — Humble Object, Main, Services](bai_08_humble_main_services.md) · [Bài 9 ← bạn đang ở đây] · [Bài 10 — The Missing Chapter: đóng gói](bai_10_dong_goi.md) · [Bài 11 — Case study & tổng kết](bai_11_case_study.md)

Xem thêm [README khoá học](../README.md).
