# Bài 10 — Hệ thống: tách việc dựng khỏi việc dùng

> [!info] Về bài này
> Dựng từ **Chương 11 — "Systems"** (tác giả Kevin Dean Wampler) của *Clean Code* (Robert C. Martin, 2008 — `tai_lieu/`, `tr. 153–170`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 31`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Mạch bài: *dựng lẫn dùng → gọi tên vấn đề → bản sạch (TypeScript, chạy được) → nguyên tắc → đối chiếu 2026 → áp dụng*.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: xây một thành phố thế nào?](#1-mở-đầu-xây-một-thành-phố-thế-nào)
2. [Tách việc dựng hệ thống khỏi việc dùng nó](#2-tách-việc-dựng-hệ-thống-khỏi-việc-dùng-nó)
3. [Code minh hoạ: main và factory lắp ráp phụ thuộc](#3-code-minh-hoạ-main-và-factory-lắp-ráp-phụ-thuộc)
4. [Dependency Injection](#4-dependency-injection)
5. [Lớn dần lên: kiến trúc không cần đúng ngay từ đầu](#5-lớn-dần-lên-kiến-trúc-không-cần-đúng-ngay-từ-đầu)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào codebase của bạn](#7-áp-dụng-vào-codebase-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mở đầu: xây một thành phố thế nào?

> [!quote] Ch. 11 — Systems (tr. 153)
> "Complexity kills. It sucks the life out of developers, it makes products difficult to plan, build, and test."
>
> *Độ phức tạp giết người. Nó rút cạn sinh khí của lập trình viên, khiến sản phẩm khó lập kế hoạch, khó dựng, khó test. (Ray Ozzie)*

Một người không thể tự quản mọi chi tiết của một thành phố, vậy mà thành phố vẫn chạy — nhờ các *đội* quản từng phần (nước, điện, giao thông…) ở những *mức trừu tượng* phù hợp. Đội phần mềm cũng tổ chức như vậy, nhưng hệ thống họ làm lại thường thiếu đúng sự tách-mối-bận-tâm ấy. Bài này nâng "code sạch" lên **mức hệ thống**.

## 2. Tách việc dựng hệ thống khỏi việc dùng nó

Dựng (construction) là một quá trình *khác hẳn* dùng (use) — như toà nhà lúc đang xây (cần cẩu, thang ngoài) khác hẳn lúc hoàn thiện.

> [!quote] Ch. 11 — Separate Constructing a System from Using It (tr. 154)
> "Software systems should separate the startup process, when the application objects are constructed and the dependencies are 'wired' together, from the runtime logic that takes over after startup."
>
> *Hệ thống phần mềm nên **tách** quá trình khởi động — khi các object được dựng và phụ thuộc được "đấu nối" — khỏi logic lúc chạy tiếp quản sau đó.*

Phản ví dụ phổ biến: *lazy initialization* nhét thẳng vào getter (`if (service == null) service = new MyServiceImpl(...)`). Nó trộn logic-dựng vào logic-chạy, tạo phụ thuộc cứng vào `MyServiceImpl`, khó test, và vi phạm SRP một cách nhỏ. Một lần thì không sao, nhưng rải khắp ứng dụng thì chiến lược dựng bị phân mảnh, trùng lặp.

## 3. Code minh hoạ: main và factory lắp ráp phụ thuộc

Cách sạch: dồn mọi việc dựng về `main` (hoặc module do `main` gọi), rồi dùng **factory** để ứng dụng kiểm soát *khi nào* tạo mà không biết *chi tiết* tạo. Mũi tên phụ thuộc chỉ đi một chiều — rời khỏi `main`:

```typescript
import { strict as assert } from "node:assert";

type LineItem = { name: string; price: number };

// Factory: ứng dụng kiểm soát KHI NÀO tạo, nhưng không biết CHI TIẾT tạo thế nào
interface LineItemFactory {
  make(name: string, price: number): LineItem;
}
class StandardLineItemFactory implements LineItemFactory {
  make(name: string, price: number): LineItem {
    return { name, price };
  }
}
class TaxedLineItemFactory implements LineItemFactory {
  private rate: number;
  constructor(rate: number) {
    this.rate = rate;
  }
  make(name: string, price: number): LineItem {
    return { name, price: Math.round(price * (1 + this.rate)) };
  }
}

// Ứng dụng: chỉ DÙNG, được tiêm factory qua constructor — không new chi tiết nào
class OrderProcessor {
  private factory: LineItemFactory;
  private items: LineItem[] = [];
  constructor(factory: LineItemFactory) {
    this.factory = factory;
  }
  addItem(name: string, price: number): void {
    this.items.push(this.factory.make(name, price));
  }
  total(): number {
    return this.items.reduce((sum, item) => sum + item.price, 0);
  }
}

// main(): nơi DUY NHẤT lắp ráp phụ thuộc; ứng dụng không biết main tồn tại
function main(factory: LineItemFactory): number {
  const order = new OrderProcessor(factory);
  order.addItem("sách", 100);
  order.addItem("bút", 20);
  return order.total();
}

const plain = main(new StandardLineItemFactory());
const taxed = main(new TaxedLineItemFactory(0.1));
assert.equal(plain, 120);
assert.equal(taxed, 132);
console.log("không thuế :", plain);
console.log("có thuế 10%:", taxed);
console.log("đổi cách dựng LineItem mà KHÔNG sửa OrderProcessor — tách dựng khỏi dùng.");
```

Kết quả chạy thật:

```
không thuế : 120
có thuế 10%: 132
đổi cách dựng LineItem mà KHÔNG sửa OrderProcessor — tách dựng khỏi dùng.
```

`OrderProcessor` *chỉ dùng* factory, không `new` chi tiết nào. Đổi từ `StandardLineItemFactory` sang `TaxedLineItemFactory` — hành vi đổi (120 → 132) mà `OrderProcessor` không sửa một dòng. Chính `main` là nơi duy nhất biết *dựng cái gì bằng cái gì*; ứng dụng không hề biết `main` tồn tại.

> [!note] Tự thử
> 1. Viết `DiscountLineItemFactory` (giảm 10%) rồi tiêm vào `main`. `OrderProcessor` có đổi dòng nào không?
> 2. Di chuyển việc tạo `LineItem` vào thẳng `OrderProcessor.addItem` (bỏ factory). Giờ muốn test với giá có thuế, bạn phải làm gì? Thấy vì sao tách dựng-khỏi-dùng giúp test chưa?
> 3. Thêm một `addItem` thứ ba. Toàn bộ "dữ liệu dựng" nằm ở `main` — việc này có giống "đấu nối ở một chỗ" mà sách mô tả không?

## 4. Dependency Injection

Cơ chế mạnh để tách dựng khỏi dùng là **Dependency Injection (DI)** — áp dụng *Inversion of Control* vào quản lý phụ thuộc:

> [!quote] Ch. 11 — Dependency Injection (tr. 157)
> "an object should not take responsibility for instantiating dependencies itself. Instead, it should pass this responsibility to another 'authoritative' mechanism."
>
> *một object không nên tự gánh việc khởi tạo phụ thuộc của mình. Thay vào đó, nó nên trao việc đó cho một cơ chế "có thẩm quyền" khác.*

Object trở nên *hoàn toàn thụ động*: nó cung cấp constructor/setter để *được tiêm* phụ thuộc; chính `main` hoặc một *container* chuyên dụng (Spring ở Java) lo lắp ráp. Đây là `OrderProcessor(factory)` ở mục 3 — và cũng là `Portfolio(exchange)` ở [Bài 9](bai_09_class.md).

## 5. Lớn dần lên: kiến trúc không cần đúng ngay từ đầu

> [!quote] Ch. 11 — Scaling Up (tr. 158)
> "It is a myth that we can get systems 'right the first time.' Instead, we should implement only today's stories, then refactor and expand the system to implement new stories tomorrow."
>
> *Rằng ta có thể làm hệ thống "đúng ngay từ đầu" là một chuyện hoang đường. Thay vào đó, hãy hiện thực chỉ những story của hôm nay, rồi refactor và mở rộng để làm story của ngày mai.*

Khác hệ vật lý (toà nhà không thể đổi móng khi đã xây), kiến trúc phần mềm *có thể* lớn dần nếu giữ được sự tách-mối-bận-tâm. Sách phê phán **EJB2** như ví dụ kiến trúc trộn lẫn mối bận tâm, cản tăng trưởng hữu cơ. Lời kết của chương là một câu rất "ponytail":

> [!quote] Ch. 11 — Conclusion (tr. 169)
> "Whether you are designing systems or individual modules, never forget to use the simplest thing that can possibly work."
>
> *Dù đang thiết kế cả hệ thống hay từng module, đừng bao giờ quên dùng **thứ đơn giản nhất có thể chạy được**.*

Và một câu về ra quyết định: hãy **hoãn quyết định tới thời điểm muộn nhất có thể** — không phải vì lười, mà để quyết với nhiều thông tin nhất.

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Chương này **tiên tri đúng về hướng lớn**, nhưng chi tiết công nghệ (EJB, Spring XML, AspectJ) đã cũ hẳn.
> - **DI — vẫn chuẩn mực 2026**, nhưng cách làm đổi. Spring XML của 2008 nhường chỗ cho annotation/decorator (Spring Boot, **NestJS**, Angular). Và (ponytail) phong trào ngược: nhiều dự án TS/Go thấy **tiêm bằng tay qua constructor** là đủ, không cần container DI — đúng như ví dụ mục 3 làm. Đừng kéo cả framework DI vào chỉ để tiêm một interface.
> - **"Kiến trúc lớn dần, đừng BDUF"** → chính Uncle Bob mở rộng thành *Clean Architecture* (2017) và cộng đồng thành **evolutionary architecture** (Neal Ford, *Building Evolutionary Architectures*, 2017) với "fitness functions". Nối thẳng sang khoá *Clean Architecture* trong repo này.
> - **AOP / Aspect** (phần sách bàn nhiều, đã lược): năm 2026 ít dùng AspectJ; mối-bận-tâm-xuyên-suốt (logging, auth, transaction, metrics) nay thường do **middleware** (Express/Koa), **decorator**, **interceptor** (NestJS), hoặc **sidecar/service mesh** (Istio) lo — cùng ý tưởng "noninvasive", khác công cụ.
> - **"Tách dựng khỏi dùng"**: còn nguyên giá trị, là nền của **Hexagonal / Ports & Adapters** (xem [Bài 7](bai_07_ranh_gioi.md)) và **composition root** — nơi duy nhất lắp ráp đồ thị phụ thuộc, đúng như `main` ở mục 3.
> - **"Thứ đơn giản nhất có thể chạy" + "hoãn quyết định"**: là YAGNI và "last responsible moment" — vẫn là kim chỉ nam 2026 chống over-engineering.
> - **Vẫn vàng**: tách khởi-động khỏi runtime, một composition root, kiến trúc tiến hoá được.

## 7. Áp dụng vào codebase của bạn

> [!question] Áp dụng vào codebase của bạn
> 1. **Tìm composition root của bạn.** Dự án có *một* chỗ rõ ràng lắp ráp phụ thuộc (main, bootstrap, module gốc) không? Hay việc `new` các dịch vụ nặng rải khắp code?
> 2. **Săn lazy-init trộn lẫn.** Tìm một getter kiểu `if (x == null) x = new ...()`. Nó có trộn dựng vào dùng không? Thử đẩy việc dựng lên composition root.
> 3. **Cân nhắc DI thủ công vs framework.** Nếu dự án dùng container DI nặng, hỏi: có đáng không, hay constructor injection tay là đủ? Nếu chưa dùng gì mà `new` lung tung, thử tiêm qua constructor.
> 4. **Kiểm "right the first time".** Có phần kiến trúc nào bạn thiết kế quá sớm cho nhu cầu *tưởng tượng* (BDUF) không? Nó có cản bạn đổi hướng khi yêu cầu thay đổi không?

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Separate construction from use** | Tách quá trình khởi động (dựng + đấu nối) khỏi logic runtime (tr. 154). |
| **Composition root / Separation of main** | Dồn mọi việc dựng về `main`; phụ thuộc chỉ trỏ rời khỏi `main` (tr. 155–156). |
| **Factory** | Cho ứng dụng kiểm soát *khi nào* tạo mà giấu *chi tiết* tạo (tr. 156). |
| **Dependency Injection (DI) / IoC** | Object thụ động, được tiêm phụ thuộc qua constructor/setter (tr. 157). |
| **Scaling up / không BDUF** | Kiến trúc phần mềm lớn dần được; đừng thiết kế hết trước khi làm (tr. 158). |
| **Evolutionary architecture** | (2026) Kiến trúc tiến hoá có "fitness function"; hiện thân hiện đại của chương. |

## 9. Câu hỏi tự kiểm tra

1. Vì sao nên tách "khởi động" khỏi "runtime"? Lazy-init trong getter sai ở đâu? *(tr. 154)*
2. "Separation of main" nghĩa là gì? Mũi tên phụ thuộc trỏ theo chiều nào? *(tr. 155–156)*
3. DI khác lazy-init và JNDI lookup ra sao? *(tr. 157)*
4. Vì sao "làm đúng ngay từ đầu là chuyện hoang đường"? Phần mềm khác toà nhà chỗ nào? *(tr. 158)*
5. Năm 2026, AOP và Spring-XML của chương này được thay bằng những gì?

## Tóm tắt một trang

```
BÀI 10 — HỆ THỐNG: TÁCH VIỆC DỰNG KHỎI VIỆC DÙNG
─────────────────────────────────────────────────────────
"Complexity kills" (Ozzie, tr.153). Nâng code sạch lên MỨC HỆ THỐNG.

TÁCH DỰNG/DÙNG  tách khởi-động (dựng + đấu nối) khỏi runtime
         (tr.154). Lazy-init trong getter = trộn dựng vào dùng.

MAIN + FACTORY  dồn việc dựng về main; phụ thuộc chỉ TRỎ RỜI main.
         OrderProcessor(factory): đổi factory → 120↔132, app không đổi.

DI       object thụ động, được TIÊM phụ thuộc (tr.157). = IoC.
         Portfolio(exchange), OrderProcessor(factory).

LỚN DẦN  "đúng ngay từ đầu là chuyện hoang đường" (tr.158).
         Làm story hôm nay, refactor mở rộng mai. Đừng BDUF.
         "dùng thứ đơn giản nhất có thể chạy" (tr.169).

2026   DI qua annotation/decorator (NestJS) hoặc TAY qua constructor
       (đừng lạm framework). AOP → middleware/interceptor/service mesh.
       "lớn dần" → Clean Architecture + evolutionary architecture.
       = Hexagonal / composition root.
```

## Nguồn

- **Robert C. Martin**, *Clean Code* (Prentice Hall, 2008) — **Chương 11, "Systems"** (Kevin Dean Wampler) (`tr. 153–170`): "complexity kills", ẩn dụ thành phố (tr. 153–154); tách dựng khỏi dùng, lazy-init (tr. 154–155); separation of main, factory (tr. 155–156); Dependency Injection, IoC, Spring (tr. 157); scaling up, "myth of right the first time", EJB2 (tr. 157–159); cross-cutting concerns, AOP, proxy, AspectJ (tr. 160–167); optimize decision making, hoãn quyết định (tr. 167–168); dùng chuẩn khôn ngoan, DSL (tr. 168–169); kết luận, "simplest thing that can possibly work" (tr. 169). `tai_lieu/Clean.Code.2008.8.pdf`
- Bổ sung 2026 dẫn từ ngoài sách: Robert C. Martin, *Clean Architecture* (2017); Neal Ford, *Building Evolutionary Architectures* (2017); NestJS/Spring Boot DI; service mesh (Istio); Hexagonal / composition root.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 31`.

---

**Bản đồ khoá học:** [Bài 0 — Clean Code là gì](bai_00_clean_code_la_gi.md) · [Bài 1 — Đặt tên](bai_01_dat_ten.md) · [Bài 2 — Hàm](bai_02_ham.md) · [Bài 3 — Comment](bai_03_comment.md) · [Bài 4 — Định dạng](bai_04_dinh_dang.md) · [Bài 5 — Object & dữ liệu](bai_05_object_va_du_lieu.md) · [Bài 6 — Xử lý lỗi](bai_06_xu_ly_loi.md) · [Bài 7 — Ranh giới](bai_07_ranh_gioi.md) · [Bài 8 — Unit test](bai_08_unit_test.md) · [Bài 9 — Class](bai_09_class.md) · [Bài 10 ← bạn đang ở đây] · [Bài 11 — Thiết kế nổi lên](bai_11_thiet_ke_noi_len.md) · [Bài 12 — Concurrency](bai_12_concurrency.md) · [Bài 13 — Xem code sạch nảy sinh](bai_13_xem_code_nay_sinh.md) · [Bài 14 — Refactor ngoài đời](bai_14_refactor_ngoai_doi.md) · [Bài 15 — Danh mục mùi code](bai_15_danh_muc_mui_code.md)

Xem thêm [README khoá học](../README.md).
