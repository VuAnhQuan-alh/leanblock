# Bài 9 — Class: nhỏ, một trách nhiệm, phụ thuộc trừu tượng

> [!info] Về bài này
> Dựng từ **Chương 10 — "Classes"** (với Jeff Langr) của *Clean Code* (Robert C. Martin, 2008 — `tai_lieu/`, `tr. 135–151`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 31`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Mạch bài: *lớp ôm đồm → gọi tên vấn đề → bản sạch (TypeScript, chạy được) → nguyên tắc → đối chiếu 2026 → áp dụng*.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: lớp God với 70 method](#1-mở-đầu-lớp-god-với-70-method)
2. [Lớp phải nhỏ — đo bằng trách nhiệm](#2-lớp-phải-nhỏ--đo-bằng-trách-nhiệm)
3. [Nguyên tắc trách nhiệm đơn (SRP)](#3-nguyên-tắc-trách-nhiệm-đơn-srp)
4. [Độ cố kết (cohesion)](#4-độ-cố-kết-cohesion)
5. [Code minh hoạ: tổ chức để thay đổi (OCP + DIP)](#5-code-minh-hoạ-tổ-chức-để-thay-đổi-ocp--dip)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào codebase của bạn](#7-áp-dụng-vào-codebase-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mở đầu: lớp God với 70 method

Những bài trước lo dòng, hàm, comment, định dạng — nhưng chưa thật sạch cho tới khi lo tới *mức tổ chức cao hơn*: lớp. Chương mở bằng `SuperDashboard` — một lớp phơi ra **70 method công khai**, thứ mà nhiều người gọi là "God class". Rồi một câu hỏi bẫy: nếu `SuperDashboard` *chỉ* còn năm method thì sao? Vẫn quá to — vì dù ít method, nó vẫn **ôm quá nhiều trách nhiệm**.

## 2. Lớp phải nhỏ — đo bằng trách nhiệm

> [!quote] Ch. 10 — Classes Should Be Small! (tr. 136)
> "The first rule of classes is that they should be small. The second rule of classes is that they should be smaller than that."
>
> *Quy tắc đầu tiên của lớp: phải nhỏ. Quy tắc thứ hai: phải nhỏ hơn thế nữa.*

(Vâng, giống hệt [Bài 2 (Hàm)](bai_02_ham.md) — nhưng thước đo khác.)

> [!quote] Ch. 10 — Classes Should Be Small! (tr. 136)
> "With functions we measured size by counting physical lines. With classes we use a different measure. We count responsibilities."
>
> *Với hàm, ta đo cỡ bằng số dòng. Với lớp, ta dùng thước khác: ta đếm **trách nhiệm**.*

Tên lớp là manh mối đầu tiên: nếu không đặt được một cái tên *cô đọng* cho lớp, nó hẳn quá to; tên mơ hồ như `Processor`, `Manager`, `Super` thường tố cáo sự ôm đồm. Một phép thử khác: mô tả lớp trong ~25 từ *không* dùng "if", "and", "or", "but" — chữ "and" đầu tiên là dấu hiệu quá nhiều trách nhiệm.

## 3. Nguyên tắc trách nhiệm đơn (SRP)

> [!quote] Ch. 10 — The Single Responsibility Principle (tr. 138)
> "a class or module should have one, and only one, reason to change."
>
> *một lớp hay module nên có một, và chỉ một, **lý do để thay đổi** — đó là Nguyên tắc Trách nhiệm Đơn (SRP).*

`SuperDashboard` dù chỉ năm method vẫn có *hai* lý do để đổi: nó theo dõi số phiên bản (đổi mỗi lần ship) *và* quản lý component Swing. Tách ba method phiên bản ra một lớp `Version` riêng là xong. Uncle Bob nói SRP là một trong những nguyên tắc OO quan trọng *và* dễ hiểu nhất — nhưng lại bị vi phạm nhiều nhất, vì "làm code chạy" và "làm code sạch" là hai hoạt động khác nhau, và phần lớn chúng ta dừng ngay khi code chạy. Ông bác thẳng nỗi sợ "nhiều lớp nhỏ khó nắm bức tranh lớn":

> [!quote] Ch. 10 — The Single Responsibility Principle (tr. 139)
> "We want our systems to be composed of many small classes, not a few large ones."
>
> *Ta muốn hệ thống gồm **nhiều lớp nhỏ**, không phải vài lớp lớn.*

Một hệ nhiều lớp nhỏ không có nhiều "bộ phận chuyển động" hơn hệ vài lớp lớn — chỉ là bạn muốn hộp đồ nghề nhiều ngăn dán nhãn rõ, hay vài ngăn quăng bừa tất cả vào.

## 4. Độ cố kết (cohesion)

Lớp nên có ít biến thực thể, và mỗi method nên thao tác trên một hay nhiều biến đó.

> [!quote] Ch. 10 — Cohesion (tr. 140)
> "A class in which each variable is used by each method is maximally cohesive."
>
> *Một lớp mà **mọi** biến đều được **mọi** method dùng tới thì cố kết tối đa.*

Cố kết cao nghĩa là biến và method "dính" với nhau thành một khối logic. Khi bạn giữ hàm nhỏ và danh sách tham số ngắn, đôi khi sinh ra một đống biến thực thể chỉ phục vụ *một nhóm nhỏ* method — đó là dấu hiệu "có một lớp khác đang muốn chui ra".

> [!quote] Ch. 10 — Cohesion (tr. 141)
> "When classes lose cohesion, split them!"
>
> *Khi lớp mất độ cố kết, hãy **tách** chúng ra!*

## 5. Code minh hoạ: tổ chức để thay đổi (OCP + DIP)

Trong một hệ thống sạch, ta tổ chức lớp để *giảm rủi ro khi đổi*. Lớp `Sql` ban đầu phải "mở ra" sửa mỗi khi thêm loại câu lệnh — rủi ro. Tách mỗi câu lệnh thành một lớp con của `Sql` thì thêm `UpdateSql` mới **không đụng** lớp nào cũ. Đó là **OCP**:

> [!quote] Ch. 10 — Organizing for Change (tr. 148)
> "Classes should be open for extension but closed for modification."
>
> *Lớp nên **mở** cho mở rộng nhưng **đóng** với sửa đổi.*

Và để cô lập khỏi thay đổi, lớp nên phụ thuộc vào *trừu tượng* chứ không vào *chi tiết cụ thể* — đó là **DIP**. Ví dụ `Portfolio` không phụ thuộc thẳng vào `TokyoStockExchange` (biến động, khó test) mà vào interface `StockExchange`:

```typescript
import { strict as assert } from "node:assert";

// ===== DIP: Portfolio phụ thuộc TRỪU TƯỢNG StockExchange, không vào chi tiết =====
interface StockExchange {
  currentPrice(symbol: string): number;
}

class Portfolio {
  private exchange: StockExchange;
  private holdings: Map<string, number> = new Map();
  constructor(exchange: StockExchange) {
    this.exchange = exchange;
  }
  add(shares: number, symbol: string): void {
    this.holdings.set(symbol, (this.holdings.get(symbol) ?? 0) + shares);
  }
  value(): number {
    let total = 0;
    for (const [symbol, shares] of this.holdings) {
      total += shares * this.exchange.currentPrice(symbol);
    }
    return total;
  }
}

// bản stub: cố định giá để test TẤT ĐỊNH (bản thật sẽ gọi API sàn, biến động)
class FixedStockExchangeStub implements StockExchange {
  private prices: Map<string, number> = new Map();
  fix(symbol: string, price: number): void {
    this.prices.set(symbol, price);
  }
  currentPrice(symbol: string): number {
    return this.prices.get(symbol) ?? 0;
  }
}

const exchange = new FixedStockExchangeStub();
exchange.fix("MSFT", 100);
const portfolio = new Portfolio(exchange);
portfolio.add(5, "MSFT");

assert.equal(portfolio.value(), 500);
console.log("5 cổ MSFT @100 => giá trị:", portfolio.value());
console.log("Portfolio test được mà không cần API sàn thật — nhờ DIP (phụ thuộc trừu tượng).");
```

Kết quả chạy thật:

```
5 cổ MSFT @100 => giá trị: 500
Portfolio test được mà không cần API sàn thật — nhờ DIP (phụ thuộc trừu tượng).
```

Nhờ `Portfolio` nhận `StockExchange` qua constructor (dependency injection), test tiêm một `FixedStockExchangeStub` giá cố định → kết quả tất định, không phụ thuộc mạng. Đây chính là liên kết thẳng với [Bài 7 (Ranh giới)](bai_07_ranh_gioi.md) và nền cho [Bài 10 (Hệ thống)](bai_10_he_thong.md):

> [!quote] Ch. 10 — Isolating from Change (tr. 150)
> "the DIP says that our classes should depend upon abstractions, not on concrete details."
>
> *DIP nói rằng lớp của ta nên phụ thuộc vào **trừu tượng**, không phải vào **chi tiết cụ thể**.*

> [!note] Tự thử
> 1. Thêm `exchange.fix("AAPL", 50)` và `portfolio.add(2, "AAPL")`. Giá trị mới là bao nhiêu? Test có cần đổi `Portfolio` không?
> 2. Viết một `RandomStockExchange` (giá ngẫu nhiên) cũng `implements StockExchange`. `Portfolio` có phải đổi dòng nào không? Đó là sức mạnh của DIP.
> 3. Thử bỏ interface `StockExchange`, cho `Portfolio` gọi thẳng một lớp `TokyoStockExchange` gọi `Math.random()`. Giờ viết một test *tất định* khó tới mức nào?

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Chương này đặt nền cho ba trong năm nguyên tắc **SOLID** (SRP, OCP, DIP) — và chúng vẫn là bộ xương của thiết kế hướng đối tượng năm 2026, dù cách hiểu đã tinh tế hơn.
> - **SRP — "một lý do để thay đổi" được làm rõ.** Chính Uncle Bob sau này (*Clean Architecture*, 2017) định nghĩa lại SRP theo **actor**: "một module chịu trách nhiệm trước *một* nhóm người dùng/bên liên quan". Cách hiểu này rõ hơn "một việc" mơ hồ, và tránh được chuyện tách lớp vụn vặt.
> - **"Nhiều lớp nhỏ" — coi chừng quá đà.** Giống chuyện hàm nhỏ ở [Bài 2](bai_02_ham.md), **John Ousterhout** phản biện: tách thành quá nhiều lớp mỏng ("classitis") làm *tăng* tải nhận thức vì phải nhảy giữa chục file. Cân bằng 2026: tách khi có *lý do thay đổi khác nhau* thật, không tách cho đủ chỉ tiêu.
> - **DIP + DI — chuẩn mực tuyệt đối 2026**, nhưng đừng lạm dụng framework. Sách tiêm phụ thuộc bằng tay qua constructor — đúng và đủ cho phần lớn trường hợp. Spring/NestJS/container DI hữu ích ở hệ lớn, nhưng (ponytail) đừng kéo cả một DI container vào chỉ để tiêm một interface; constructor injection thủ công thường là đủ.
> - **OCP — vẫn đúng nhưng đừng "tiên tri".** Đừng tạo sẵn cả cây kế thừa cho mở rộng *tưởng tượng* (YAGNI). Sách nói đúng: chỉ sửa thiết kế "**ngay khi** thấy mình phải mở một lớp ra sửa", không phải trước đó.
> - **Composition over inheritance**: ví dụ `Sql` dùng kế thừa; năm 2026 nhiều nơi ưu tiên *hợp thành* (strategy/function) hơn cây kế thừa — nhưng tinh thần OCP (thêm mà không sửa) giữ nguyên.
> - **Vẫn vàng**: SRP, cohesion cao, phụ thuộc trừu tượng để test được.

## 7. Áp dụng vào codebase của bạn

> [!question] Áp dụng vào codebase của bạn
> 1. **Thử "25 từ".** Chọn lớp lớn nhất trong dự án. Mô tả nó trong ~25 từ không dùng "và/hoặc". Đếm số chữ "và" — mỗi chữ là một trách nhiệm có thể tách.
> 2. **Đếm lý do thay đổi.** Với một lớp, liệt kê những *bên* khác nhau có thể khiến nó đổi (nghiệp vụ, giao diện, định dạng dữ liệu). >1 → ứng viên tách theo SRP-actor.
> 3. **Săn phụ thuộc cụ thể.** Tìm một lớp `new` thẳng một dịch vụ ngoài (DB, HTTP, clock, random) trong ruột nó. Rút thành interface + tiêm qua constructor. Giờ test tất định được chưa?
> 4. **Chống classitis.** Nếu dự án đã nhiều lớp mỏng, tìm hai lớp *luôn đổi cùng nhau*. Chúng có nên gộp lại cho bớt nhảy file không?

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **God class** | Lớp ôm quá nhiều trách nhiệm (ví dụ `SuperDashboard` 70 method) (tr. 136). |
| **SRP** | Single Responsibility Principle — một lớp, một lý do để thay đổi (tr. 138). |
| **Cohesion** | Độ cố kết: biến và method "dính" nhau thành khối logic; mất cố kết thì tách (tr. 140–141). |
| **OCP** | Open-Closed Principle — mở cho mở rộng, đóng với sửa đổi (tr. 148). |
| **DIP** | Dependency Inversion Principle — phụ thuộc trừu tượng, không phụ thuộc chi tiết (tr. 150). |
| **Dependency Injection** | Tiêm phụ thuộc (ví dụ `StockExchange`) qua constructor để test được (tr. 150). |
| **Classitis** | (2026) Tách quá nhiều lớp mỏng, tăng tải nhận thức — thái cực ngược của God class. |

## 9. Câu hỏi tự kiểm tra

1. Lớp "nhỏ" được đo bằng gì (không phải số dòng)? *(tr. 136)*
2. Phát biểu SRP. Vì sao `SuperDashboard` năm-method vẫn vi phạm nó? *(tr. 138)*
3. "Maximally cohesive" nghĩa là gì? Khi nào thì nên tách lớp? *(tr. 140–141)*
4. OCP và DIP khác nhau ra sao? Ví dụ `Sql` minh hoạ OCP, `Portfolio` minh hoạ DIP thế nào? *(tr. 148–150)*
5. Năm 2026, "nhiều lớp nhỏ" bị phản biện ra sao, và SRP được định nghĩa lại thế nào?

## Tóm tắt một trang

```
BÀI 9 — CLASS: NHỎ, MỘT TRÁCH NHIỆM, PHỤ THUỘC TRỪU TƯỢNG
─────────────────────────────────────────────────────────
NHỎ      "nhỏ, rồi nhỏ hơn" — nhưng đo bằng TRÁCH NHIỆM,
         không phải dòng (tr.136). God class = ôm đồm.
         Phép thử: mô tả trong 25 từ không "và/hoặc".

SRP      một lớp, MỘT lý do để thay đổi (tr.138).
         "nhiều lớp nhỏ, không phải vài lớp lớn" (tr.139).

COHESION mọi biến dùng bởi mọi method = cố kết tối đa (tr.140).
         "mất cố kết thì TÁCH" (tr.141).

TỔ CHỨC ĐỂ ĐỔI
  OCP: mở cho mở rộng, đóng với sửa (tr.148). Sql→UpdateSql.
  DIP: phụ thuộc TRỪU TƯỢNG, không chi tiết (tr.150).
       Portfolio(StockExchange) → test bằng stub, ra 500.

2026   SOLID vẫn là xương sống. SRP định nghĩa lại theo ACTOR
       (Clean Architecture 2017). Coi chừng "classitis"
       (Ousterhout). DI thủ công thường đủ — đừng lạm framework.
       OCP: đừng tiên tri (YAGNI). Ưu tiên hợp thành hơn kế thừa.
```

## Nguồn

- **Robert C. Martin**, *Clean Code* (Prentice Hall, 2008) — **Chương 10, "Classes"** (với Jeff Langr) (`tr. 135–151`): tổ chức lớp, đóng gói (tr. 136); lớp phải nhỏ, `SuperDashboard` God class, đo bằng trách nhiệm (tr. 136–138); SRP, tách `Version` (tr. 138–139); nhiều lớp nhỏ (tr. 139–140); cohesion, `Stack`, "mất cố kết thì tách" (tr. 140–141); refactor `PrintPrimes` (tr. 141–145); tổ chức để thay đổi, `Sql`, OCP (tr. 147–149); cô lập khỏi thay đổi, `Portfolio`/`StockExchange`, DIP (tr. 149–151). `tai_lieu/Clean.Code.2008.8.pdf`
- Bổ sung 2026 dẫn từ ngoài sách: Robert C. Martin, *Clean Architecture* (2017, SRP theo actor); John Ousterhout (classitis); composition over inheritance; SOLID.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 31`.

---

**Bản đồ khoá học:** [Bài 0 — Clean Code là gì](bai_00_clean_code_la_gi.md) · [Bài 1 — Đặt tên](bai_01_dat_ten.md) · [Bài 2 — Hàm](bai_02_ham.md) · [Bài 3 — Comment](bai_03_comment.md) · [Bài 4 — Định dạng](bai_04_dinh_dang.md) · [Bài 5 — Object & dữ liệu](bai_05_object_va_du_lieu.md) · [Bài 6 — Xử lý lỗi](bai_06_xu_ly_loi.md) · [Bài 7 — Ranh giới](bai_07_ranh_gioi.md) · [Bài 8 — Unit test](bai_08_unit_test.md) · [Bài 9 ← bạn đang ở đây] · [Bài 10 — Hệ thống](bai_10_he_thong.md) · [Bài 11 — Thiết kế nổi lên](bai_11_thiet_ke_noi_len.md) · [Bài 12 — Concurrency](bai_12_concurrency.md) · [Bài 13 — Xem code sạch nảy sinh](bai_13_xem_code_nay_sinh.md) · [Bài 14 — Refactor ngoài đời](bai_14_refactor_ngoai_doi.md) · [Bài 15 — Danh mục mùi code](bai_15_danh_muc_mui_code.md)

Xem thêm [README khoá học](../README.md).
