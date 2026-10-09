# Bài 10 — The Missing Chapter: đóng gói code thế nào cho đúng

> [!info] Về bài này
> Dựng từ **Ch.34 "The Missing Chapter"** (tác giả **Simon Brown**) của *Clean Architecture* (Robert C. Martin, 2017 — `tai_lieu/`, `tr. 303–321`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 27`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Đây là chương *thực chiến nhất*: mọi nguyên tắc trước đó vô dụng nếu bạn tổ chức *thư mục/package* sai. Trả lời câu "vậy cuối cùng tôi xếp file vào đâu?".
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: ý định thiết kế đẹp có thể tan trong chớp mắt](#1-mở-đầu-ý-định-thiết-kế-đẹp-có-thể-tan-trong-chớp-mắt)
2. [Bốn lối tổ chức code](#2-bốn-lối-tổ-chức-code)
3. [Package by Component: lối Simon Brown chọn](#3-package-by-component-lối-simon-brown-chọn)
4. [Code minh hoạ: component giấu chi tiết bên trong](#4-code-minh-hoạ-component-giấu-chi-tiết-bên-trong)
5. [Devil in the details: dùng compiler để cưỡng chế kiến trúc](#5-devil-in-the-details-dùng-compiler-để-cưỡng-chế-kiến-trúc)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào dự án của bạn](#7-áp-dụng-vào-dự-án-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mở đầu: ý định thiết kế đẹp có thể tan trong chớp mắt

Uncle Bob mời Simon Brown viết chương cuối vì nhận ra sách thiếu một mảnh *rất* thực tế: *làm sao ánh xạ thiết kế đẹp lên cấu trúc thư mục code thật*. Thông điệp trung tâm:

> [!quote] Ch. 34 — Conclusion: The Missing Advice (tr. 320)
> "your best design intentions can be destroyed in a flash if you don't consider the intricacies of the implementation strategy."
>
> *những ý định thiết kế đẹp nhất của bạn có thể **tan trong chớp mắt** nếu bạn không cân nhắc tới các ngóc ngách của chiến lược hiện thực.*

Bạn có thể vẽ vòng tròn Clean Architecture ([Bài 7](bai_07_clean_architecture.md)) hoàn hảo trên giấy, nhưng nếu xếp file sai cách và dùng `public` bừa bãi, kiến trúc đó không tồn tại trong code thật.

## 2. Bốn lối tổ chức code

Simon Brown so sánh bốn cách, lấy ví dụ một use case "xem đơn hàng":

| Lối tổ chức | Gom theo | Ưu | Nhược |
| :--- | :--- | :--- | :--- |
| **Package by Layer** | *tầng kỹ thuật* (web / service / repository) | quen thuộc, hợp sách giáo khoa | một tính năng rải khắp các tầng; tầng là "lát ngang" |
| **Package by Feature** | *tính năng* (lát dọc: orders, customers) | tính năng tụ một chỗ, dễ thấy | vẫn để lộ chi tiết (repo) ra ngoài feature |
| **Ports and Adapters** | *inside* (domain) vs *outside* (infrastructure) | domain độc lập hạ tầng, đúng Dependency Rule | dễ dính "Périphérique anti-pattern" nếu lơi access modifier |
| **Package by Component** | *component* (OrdersComponent: cả nghiệp vụ + persistence, ẩn sau API) | một cửa vào cho "orders"; bước đệm lên micro-service | cần kỷ luật giấu nội bộ |

Hai lối đầu phổ biến nhưng Simon Brown xem là *dưới mức tối ưu*: Package by Layer làm một tính năng *rải* khắp các tầng; Package by Feature gom dọc tốt hơn nhưng vẫn phơi chi tiết (như `OrdersRepository` phải để `public`).

## 3. Package by Component: lối Simon Brown chọn

> [!quote] Ch. 34 — Package by Component (tr. 314)
> "A key benefit of the 'package by component' approach is that if you're writing code that needs to do something with orders, there's just one place to go—the OrdersComponent."
>
> *Lợi ích then chốt của lối "package by component" là: nếu bạn viết code cần làm gì đó với orders, chỉ có **một nơi để tới — OrdersComponent**.*

Bên trong component, vẫn giữ tách biệt (nghiệp vụ tách khỏi persistence), nhưng đó là *chi tiết nội bộ* mà consumer không cần biết. Điều này giống một `OrdersService` trong micro-service — khác biệt chỉ là *decoupling mode* ([Bài 5](bai_05_kien_truc_va_doc_lap.md)):

> [!quote] Ch. 34 — Package by Component (tr. 314)
> "You can think of well-defined components in a monolithic application as being a stepping stone to a micro-services architecture."
>
> *Bạn có thể coi những component được định nghĩa tốt trong một ứng dụng monolith như **bước đệm** lên kiến trúc micro-service.*

(Đây chính là luận điểm "modular monolith" ở [Bài 8](bai_08_humble_main_services.md): component rõ ràng *trước*, service *sau* nếu cần.)

## 4. Code minh hoạ: component giấu chi tiết bên trong

`OrdersComponent` là *cửa duy nhất* vào mọi thứ liên quan đơn hàng; kho dữ liệu (`#store`) là chi tiết nội bộ — thật sự riêng tư (JS `#private`, cưỡng chế ngay lúc chạy):

```typescript
import { strict as assert } from "node:assert";

type Order = { id: number; total: number };

// ===== PACKAGE BY COMPONENT: OrdersComponent là CỬA DUY NHẤT vào "orders" =====
class OrdersComponent {
  #store = new Map<number, Order>(); // persistence GIẤU bên trong (private thật)

  placeOrder(id: number, total: number): void {
    if (total <= 0) throw new Error("total phải dương"); // business rule
    this.#store.set(id, { id, total });
  }
  totalRevenue(): number {
    let sum = 0;
    for (const o of this.#store.values()) sum += o.total;
    return sum;
  }
}

const orders = new OrdersComponent();
orders.placeOrder(1, 100);
orders.placeOrder(2, 250);
assert.equal(orders.totalRevenue(), 350);
console.log("doanh thu:", orders.totalRevenue());
console.log("thuộc tính lộ ra ngoài:", JSON.stringify(Object.keys(orders)), "← #store bị giấu thật");
console.log("consumer chỉ đi qua API component; repository là chi tiết bên trong.");
```

Kết quả chạy thật:

```
doanh thu: 350
thuộc tính lộ ra ngoài: [] ← #store bị giấu thật
consumer chỉ đi qua API component; repository là chi tiết bên trong.
```

`Object.keys(orders)` trả về `[]` — `#store` *không* lộ ra ngoài. Consumer chỉ có thể gọi `placeOrder`/`totalRevenue`; không có đường nào chạm thẳng kho dữ liệu, nên business rule (`total phải dương`) không thể bị vòng qua. Đúng "một nơi để tới" của Simon Brown: muốn làm gì với orders → đi qua `OrdersComponent`.

> [!note] Tự thử
> 1. Đổi `#store` thành `store` công khai. Giờ `Object.keys(orders)` ra gì? Consumer có thể `orders.store.set(...)` vòng qua `placeOrder` (và business rule) không?
> 2. Thêm `OrdersRepository` tách khỏi `OrdersComponent` nhưng vẫn giấu sau API component. Consumer có cần biết nó tồn tại không?
> 3. Thử xếp cùng logic này theo "package by layer" (web/service/repo riêng): muốn hiểu "orders" bạn phải mở mấy file ở mấy tầng?

## 5. Devil in the details: dùng compiler để cưỡng chế kiến trúc

Bốn lối trông như bốn phong cách kiến trúc khác nhau — nhưng ảo tưởng đó *tan rã* nếu hiện thực sai. Thủ phạm số một:

> [!quote] Ch. 34 — The Devil Is in the Implementation Details (tr. 314)
> "Something I see on a regular basis is an overly liberal use of the public access modifier in languages such as Java. It's almost as if we, as developers, instinctively use the public keyword without thinking."
>
> *Thứ tôi thấy thường xuyên là việc **lạm dụng** access modifier `public`. Gần như thể chúng ta, lập trình viên, dùng từ khoá `public` theo bản năng mà không suy nghĩ.*

Nếu *mọi thứ* đều `public`, thì dù vẽ ranh giới đẹp thế nào, bất kỳ code nào cũng gọi thẳng được vào bất kỳ chỗ nào — kiến trúc chỉ còn trên giấy. Lời khuyên của Simon Brown rất thực dụng:

> [!quote] Ch. 34 — Package by Component (tr. 312)
> "I'd personally like to use the compiler to enforce my architecture if at all possible."
>
> *Cá nhân tôi muốn **dùng compiler để cưỡng chế kiến trúc** nếu có thể.*

Giấu nội bộ bằng access modifier (hoặc `#private`, hoặc ranh giới package/module) để *compiler* — không phải thiện chí con người — chặn các lời gọi vượt rào. Và lời kết gói cả chương:

> [!quote] Ch. 34 — Conclusion: The Missing Advice (tr. 320)
> "Leave options open where applicable, but be pragmatic […] The devil is in the implementation details."
>
> *Giữ ngỏ lựa chọn khi hợp lý, nhưng hãy **thực dụng** […] Ma quỷ nằm trong các chi tiết hiện thực.*

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Đây là chương **"thực dụng nhất" và hợp 2026 nhất** — vì nó nói về cưỡng chế, không chỉ lý tưởng.
> - **"Package by Component" ↔ modular monolith (2026).** "Component rõ ràng là bước đệm lên micro-service" đúng là triết lý modular monolith thắng thế hiện nay ([Bài 8](bai_08_humble_main_services.md)). Shopify, và nhiều template, tổ chức theo *module nghiệp vụ* có API rõ, giấu nội bộ — chính package-by-component.
> - **"Package by Feature / Vertical Slice" lên ngôi.** Năm 2026, **vertical slice architecture** (gom theo tính năng, xuyên tầng) là phản ứng phổ biến chống package-by-layer. Nó là bà con gần của package-by-feature/component mà Simon Brown đề cao.
> - **"Dùng compiler cưỡng chế" — 2026 có công cụ mạnh hơn hẳn.** TS `private`/`#private`, module `export` có kiểm soát; và cả tầng công cụ *kiểm ranh giới*: ESLint `no-restricted-imports`/`boundaries`, `dependency-cruiser`, **Nx module boundary tags**, ArchUnit, Java module system (JPMS). Lời khuyên của Simon Brown giờ là *rule trong CI*, không phải code review bằng mắt.
> - **"Lạm dụng public" vẫn là thói xấu phổ biến 2026** — và linter đã có thể cảnh báo. Mặc định nên là *đóng*, chỉ `export`/`public` khi thật cần (ngược bản năng).
> - **Vẫn vàng:** ánh xạ thiết kế → cấu trúc thư mục là bước quyết định; thiếu nó, Clean Architecture chỉ là sơ đồ đẹp. "The devil is in the implementation details."

## 7. Áp dụng vào dự án của bạn

> [!question] Áp dụng vào dự án của bạn
> 1. **Nhận diện lối đóng gói hiện tại.** Thư mục `src/` của bạn chia theo *tầng* (controllers/services/repositories) hay theo *tính năng/component* (orders/, customers/)? Theo tầng → cân nhắc chuyển sang component/feature.
> 2. **Đếm `public`/`export` thừa.** Có bao nhiêu thứ `export` mà chỉ dùng nội bộ một module? Mỗi cái là một lỗ rò ranh giới. Thu hẹp lại.
> 3. **Bật cưỡng chế compiler.** Cài `dependency-cruiser` / Nx tags / ESLint boundaries để *CI chặn* khi một module import vượt rào. Biến kiến trúc từ "thoả thuận" thành "luật".
> 4. **Thử "một nơi để tới".** Chọn một khái niệm nghiệp vụ (orders). Để làm gì đó với nó, bạn phải mở bao nhiêu thư mục? Nếu > 1, cân nhắc gom thành component.

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| :--- | :--- |
| **Package by Layer** | Gom theo tầng kỹ thuật (web/service/repo); một tính năng rải khắp (tr. 305). |
| **Package by Feature** | Gom theo tính năng (lát dọc); tốt hơn layer nhưng còn lộ chi tiết (tr. 307). |
| **Ports and Adapters** | Gom theo inside (domain) vs outside (infrastructure) (tr. 308). |
| **Package by Component** | Gom theo component có API rõ, giấu nội bộ; bước đệm micro-service (tr. 310+). |
| **Périphérique anti-pattern** | Hạ tầng một chỗ khiến code vòng qua domain gọi thẳng nhau (tr. 319). |
| **Enforce by compiler** | Dùng access modifier/module/linter để compiler chặn vượt ranh giới (tr. 312). |

## 9. Câu hỏi tự kiểm tra

1. Thông điệp trung tâm của chương (câu "best design intentions…") là gì? *(tr. 320)*
2. Bốn lối tổ chức code là gì? Mỗi lối gom theo tiêu chí nào? *(tr. 305–310)*
3. Vì sao Simon Brown ưa "package by component"? "Một nơi để tới" nghĩa là gì? *(tr. 314)*
4. Trong demo, vì sao consumer không vòng qua được business rule? `Object.keys` trả gì? *(mục 4)*
5. "Lạm dụng public" phá kiến trúc thế nào? "Dùng compiler cưỡng chế" nghĩa là gì năm 2026? *(tr. 312, 314)*

## Tóm tắt một trang

```
BÀI 10 — THE MISSING CHAPTER: ĐÓNG GÓI CODE (Simon Brown)
─────────────────────────────────────────────────────────
"ý định thiết kế đẹp có thể TAN TRONG CHỚP MẮT nếu không cân
nhắc chi tiết hiện thực" (tr.320). Vòng tròn đẹp vô dụng nếu xếp
file sai + public bừa.

BỐN LỐI:
   Package by Layer    — theo tầng (web/service/repo); tính năng RẢI khắp
   Package by Feature  — theo tính năng (lát dọc); còn lộ chi tiết
   Ports and Adapters  — inside(domain) vs outside(infra)
   Package by COMPONENT— component có API, giấu nội bộ ← Simon Brown chọn
       "một nơi để tới — OrdersComponent" (tr.314). Bước đệm micro-service.

DEMO  OrdersComponent với #store private thật. Object.keys = [].
   Consumer không vòng qua business rule được.

DEVIL IN DETAILS  "lạm dụng public" phá kiến trúc (tr.314).
   "dùng COMPILER cưỡng chế kiến trúc" (tr.313). "The devil is in
   the implementation details" (tr.320).

2026  = modular monolith + vertical slice. Cưỡng chế bằng
   dependency-cruiser/Nx tags/ESLint boundaries/ArchUnit (CI chặn).
   Mặc định nên ĐÓNG, chỉ export khi cần (ngược bản năng).
```

## Nguồn

- **Robert C. Martin** (chương của **Simon Brown**), *Clean Architecture* (Prentice Hall, 2017) — **Ch.34 "The Missing Chapter"** (`tr. 303–321`): bốn lối tổ chức — package by layer (tr. 305), package by feature (tr. 307), ports and adapters (tr. 308–309), package by component (tr. 310–314); "one place to go—OrdersComponent", "stepping stone to micro-services" (tr. 314); the devil in implementation details, lạm dụng public, "I'd personally like to use the compiler to enforce my architecture" (tr. 312); Périphérique anti-pattern (tr. 319); kết luận "best design intentions… destroyed in a flash", "the devil is in the implementation details" (tr. 320–321). `tai_lieu/Clean.Architecture.2017.9.pdf`
- Bối cảnh 2026 dẫn từ ngoài sách: vertical slice architecture; modular monolith; dependency-cruiser / Nx module boundaries / ESLint boundaries / ArchUnit / JPMS.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 27`.

---

**Bản đồ khoá học:** [Bài 0 — Hai giá trị](bai_00_hai_gia_tri.md) · [Bài 1 — Ba hệ hình lập trình](bai_01_he_hinh_lap_trinh.md) · [Bài 2 — SOLID (1): SRP, OCP](bai_02_solid_srp_ocp.md) · [Bài 3 — SOLID (2): LSP, ISP, DIP](bai_03_solid_lsp_isp_dip.md) · [Bài 4 — Nguyên tắc Component](bai_04_nguyen_tac_component.md) · [Bài 5 — Kiến trúc là gì & Độc lập](bai_05_kien_truc_va_doc_lap.md) · [Bài 6 — Ranh giới & Dependency Rule](bai_06_ranh_gioi_dependency_rule.md) · [Bài 7 — Business Rules & The Clean Architecture](bai_07_clean_architecture.md) · [Bài 8 — Humble Object, Main, Services](bai_08_humble_main_services.md) · [Bài 9 — Chi tiết: DB, Web, Framework](bai_09_chi_tiet.md) · [Bài 10 ← bạn đang ở đây] · [Bài 11 — Case study & tổng kết](bai_11_case_study.md)

Xem thêm [README khoá học](../README.md).
