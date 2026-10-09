# Bài 7 — Business Rules & The Clean Architecture: vòng tròn đồng tâm

> [!info] Về bài này
> Dựng từ **Phần V — Architecture**: **Ch.20 "Business Rules"**, **Ch.21 "Screaming Architecture"**, **Ch.22 "The Clean Architecture"** của *Clean Architecture* (Robert C. Martin, 2017 — `tai_lieu/`, `tr. 189–210`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 27`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> **Đây là bài trung tâm của khoá** — nơi mọi thứ (SOLID, component, ranh giới) hội tụ vào sơ đồ vòng tròn đồng tâm nổi tiếng và **Dependency Rule**.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Business Rules: Entity và Use Case](#1-business-rules-entity-và-use-case)
2. [Screaming Architecture: kiến trúc phải *hét* lên nó là gì](#2-screaming-architecture-kiến-trúc-phải-hét-lên-nó-là-gì)
3. [Vòng tròn đồng tâm và Dependency Rule](#3-vòng-tròn-đồng-tâm-và-dependency-rule)
4. [Code minh hoạ: ráp đủ bốn vòng](#4-code-minh-hoạ-ráp-đủ-bốn-vòng)
5. [Vượt ranh giới: luồng dữ liệu qua các vòng](#5-vượt-ranh-giới-luồng-dữ-liệu-qua-các-vòng)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào dự án của bạn](#7-áp-dụng-vào-dự-án-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Business Rules: Entity và Use Case

Business rules là lý do một hệ phần mềm tồn tại — những quy tắc *làm ra hoặc tiết kiệm tiền*, đúng ngay cả khi thực hiện thủ công. Uncle Bob chia hai tầng:

**Entity** chứa *Critical Business Rules* + *Critical Business Data*:

> [!quote] Ch. 20 — Business Rules (tr. 189)
> "An Entity is an object within our computer system that embodies a small set of critical business rules operating on Critical Business Data."
>
> *Một **Entity** là một object trong hệ thống, hiện thân cho một tập nhỏ **critical business rules** thao tác trên **Critical Business Data**.*

Entity "thuần nghiệp vụ và không gì khác" — không vương vấn database, UI, hay framework. Nó phục vụ được *bất kỳ* hệ thống nào, bất kể giao diện hay cách lưu trữ ra sao.

**Use Case** chứa *application-specific business rules* — điều phối dòng dữ liệu ra/vào Entity để đạt mục tiêu của một ca sử dụng cụ thể. Bảng phân biệt:

| | **Entity** | **Use Case** |
| :--- | :--- | :--- |
| Chứa quy tắc | *enterprise-wide* Critical Business Rules | *application-specific* rules |
| Dùng được ở | nhiều ứng dụng trong doanh nghiệp | một ứng dụng cụ thể |
| Khả năng đổi | ít đổi nhất (ổn định nhất) | đổi khi *cách vận hành* ứng dụng đổi |
| Biết gì về DB/UI | **không gì cả** | **không gì cả** |

## 2. Screaming Architecture: kiến trúc phải *hét* lên nó là gì

Nhìn bản vẽ một ngôi nhà thì biết ngay đó là nhà; nhìn thư viện thì biết là thư viện. Vậy:

> [!quote] Ch. 21 — Screaming Architecture (tr. 195)
> "So what does the architecture of your application scream? […] do they scream 'Health Care System,' or 'Accounting System,' or 'Inventory Management System'? Or do they scream 'Rails,' or 'Spring/..."
>
> *Vậy kiến trúc ứng dụng của bạn **hét** lên điều gì? […] nó hét "Hệ thống Y tế", "Hệ thống Kế toán", "Quản lý Kho"? Hay nó hét "Rails", "Spring"?*

Kiến trúc tốt phải hét lên *use case* (nghiệp vụ), không phải framework được dùng. Vì:

> [!quote] Ch. 21 — But What About the Web? (tr. 196)
> "Frameworks are tools to be used, not architectures to be conformed to. If your architecture is based on frameworks, then it cannot be based on your use cases."
>
> *Framework là **công cụ để dùng**, không phải **kiến trúc để tuân theo**. Nếu kiến trúc của bạn dựa trên framework, thì nó không thể dựa trên use case của bạn.*

Web (và mọi framework) chỉ là một *delivery mechanism* — một chi tiết nên bị đẩy ra rìa.

## 3. Vòng tròn đồng tâm và Dependency Rule

Đây là sơ đồ nổi tiếng nhất của cả cuốn sách — bốn vòng đồng tâm, ngoài là *cơ chế*, trong là *chính sách*:

```
┌─────────────────────────────────────────────────────────────────────────┐
│ VÒNG 4: Frameworks & Drivers (Web, DB, UI) — CHI TIẾT                   │  ← cơ chế
│   ┌─────────────────────────────────────────────────────────────────┐   │
│   │ VÒNG 3: Interface Adapters (Controllers, Presenters, Gateways)  │   │
│   │   ┌─────────────────────────────────────────────────────────┐   │   │
│   │   │ VÒNG 2: Use Cases (application-specific business rules) │   │   │
│   │   │   ┌────────────────────────────────────────────┐        │   │   │
│   │   │   │ VÒNG 1: Entities (Critical Business Rules) │        │   │   │
│   │   │   └────────────────────────────────────────────┘        │   │   │
│   │   └─────────────────────────────────────────────────────────┘   │   │
│   └─────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
     phụ thuộc mã nguồn CHỈ ĐƯỢC trỏ VÀO TRONG  ───►
```

> [!quote] Ch. 22 — The Dependency Rule (tr. 202)
> "Source code dependencies must point only inward, toward higher-level policies."
>
> *Phụ thuộc mã nguồn **chỉ được** trỏ **vào trong**, về phía các chính sách mức cao hơn.*

Và hệ quả tuyệt đối:

> [!quote] Ch. 22 — The Dependency Rule (tr. 202)
> "Nothing in an inner circle can know anything at all about something in an outer circle."
>
> *Không gì ở vòng trong được biết **bất cứ điều gì** về thứ ở vòng ngoài.*

Nghĩa là: tên một class/hàm/biến khai ở vòng ngoài **không được** xuất hiện trong code vòng trong; định dạng dữ liệu do framework ngoài sinh ra **không được** dùng ở vòng trong. Hai định nghĩa vòng trong:

> [!quote] Ch. 22 — Entities / Use Cases (tr. 203)
> "Entities encapsulate enterprise-wide Critical Business Rules. […] The software in the use cases layer contains application-specific business rules."
>
> *Entity đóng gói Critical Business Rules toàn doanh nghiệp. […] Phần mềm ở tầng use case chứa business rule riêng của ứng dụng.*

## 4. Code minh hoạ: ráp đủ bốn vòng

Demo dưới đây là một Clean Architecture thu nhỏ nhưng *đủ bốn vòng*: Entity (`Account`), Use Case (`WithdrawUseCase` + output port), Interface Adapter (`Controller`, `Presenter`), và Main lắp ráp. Mọi `import`/phụ thuộc trỏ **vào trong**:

```typescript
import { strict as assert } from "node:assert";

// ============ VÒNG 1 — ENTITIES: Critical Business Rules ============
class Account {
  private balanceCents: number;
  constructor(balanceCents: number) { this.balanceCents = balanceCents; }
  balance(): number { return this.balanceCents; }
  withdraw(amountCents: number): void { // business rule: không rút quá số dư
    if (amountCents > this.balanceCents) throw new Error("Không đủ số dư");
    this.balanceCents -= amountCents;
  }
}

// ============ VÒNG 2 — USE CASES: application rules + output port ============
interface WithdrawOutput { present(newBalanceCents: number): void; }
class WithdrawUseCase {
  private account: Account;
  private output: WithdrawOutput;
  constructor(account: Account, output: WithdrawOutput) {
    this.account = account; this.output = output;
  }
  execute(amountCents: number): void {
    this.account.withdraw(amountCents);           // điều khiển entity
    this.output.present(this.account.balance());  // đẩy ra qua output port
  }
}

// ============ VÒNG 3 — INTERFACE ADAPTERS: Controller + Presenter ============
class WithdrawPresenter implements WithdrawOutput {
  public view = "";
  present(newBalanceCents: number): void {
    this.view = `Số dư còn: ${(newBalanceCents / 100).toFixed(2)}đ`; // định dạng cho UI
  }
}
class WithdrawController {
  private useCase: WithdrawUseCase;
  constructor(useCase: WithdrawUseCase) { this.useCase = useCase; }
  handle(amountDong: number): void {
    this.useCase.execute(Math.round(amountDong * 100)); // input ngoài -> dạng trong
  }
}

// ============ VÒNG 4 — MAIN: lắp ráp; mọi phụ thuộc trỏ VÀO TRONG ============
const account = new Account(10000); // 100.00đ
const presenter = new WithdrawPresenter();
const useCase = new WithdrawUseCase(account, presenter);
const controller = new WithdrawController(useCase);

controller.handle(30); // rút 30đ
console.log(presenter.view);
assert.equal(presenter.view, "Số dư còn: 70.00đ");

let threw = false;
try { controller.handle(1000); } catch { threw = true; } // rút 1000đ > số dư
assert.equal(threw, true);
console.log("rút quá số dư bị Entity chặn — business rule ở vòng trong cùng, miễn nhiễm.");
```

Kết quả chạy thật:

```
Số dư còn: 70.00đ
rút quá số dư bị Entity chặn — business rule ở vòng trong cùng, miễn nhiễm.
```

Chú ý chiều phụ thuộc: `Controller`→`UseCase`→`Account` và `Presenter` *hiện thực* `WithdrawOutput` (do Use Case sở hữu) — tất cả trỏ **vào trong**. `Account` (Entity) không biết gì về `Presenter`, `Controller`, hay định dạng `"70.00đ"`. Muốn đổi UI (web→CLI→mobile) chỉ cần viết `Presenter`/`Controller` mới; muốn đổi DB chỉ cần một Gateway mới — Entity và Use Case **bất động**. Đây là toàn bộ lời hứa của Clean Architecture, thu vào 40 dòng.

> [!note] Tự thử
> 1. Viết `JsonPresenter implements WithdrawOutput` trả JSON thay vì chuỗi. `Account`, `WithdrawUseCase` có đổi dòng nào không?
> 2. Thử cho `Account` (Entity) `import` và gọi `WithdrawPresenter`. Bạn vừa vi phạm Dependency Rule — vì sao đó là thảm hoạ? (Gợi ý: Entity giờ biết về định dạng UI.)
> 3. Thêm một `AccountGateway` interface (do Use Case sở hữu) + `InMemoryAccountGateway` (vòng 4) để nạp `Account`. Mũi tên phụ thuộc của gateway trỏ chiều nào?

## 5. Vượt ranh giới: luồng dữ liệu qua các vòng

Một nghịch lý tưởng chừng: luồng điều khiển đi từ ngoài vào (Controller gọi Use Case) *rồi lại đi ra* (Use Case gọi Presenter) — nhưng phụ thuộc mã nguồn *luôn* trỏ vào trong. Giải bằng DIP ([Bài 3](bai_03_solid_lsp_isp_dip.md)): Use Case định nghĩa một *output port* (interface `WithdrawOutput`), Presenter ở vòng ngoài *hiện thực* nó. Dữ liệu vượt ranh giới luôn là **cấu trúc đơn giản** (số, DTO, struct) — "không bao giờ truyền Entity hay row database ra ngoài", và luôn ở dạng *tiện nhất cho vòng trong*. Đây đúng cơ chế boundary-crossing của [Bài 6](bai_06_ranh_gioi_dependency_rule.md), nay thành khung tiêu chuẩn bốn vòng.

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Sơ đồ vòng tròn là biểu tượng được trích dẫn nhiều nhất — và cũng bị tranh cãi nhiều nhất — của kiến trúc phần mềm 2026.
> - **Hội tụ "clean/hexagonal/onion".** Dependency Rule là *mẫu số chung* của Ports & Adapters, Onion, và Clean Architecture. Năm 2026 nhiều template (NestJS, .NET, Go) sinh sẵn cấu trúc này. Lợi: testable, đổi-DB/UI rẻ, nghiệp vụ rõ.
> - **Phê bình lớn nhất (ponytail): quá nhiều tầng/indirection cho app vừa và nhỏ.** Đủ bốn vòng + port + presenter + mapper DTO cho một CRUD nhỏ là *over-engineering* điển hình — bạn viết 5 file để làm việc 1 file làm được. Phản ứng 2026: **Vertical Slice Architecture** (Jimmy Bogard) gom code theo *tính năng* xuyên tầng thay vì theo *tầng ngang*, chấp nhận ít trừu tượng hơn để đổi lấy sự trực tiếp. Dùng Clean Architecture khi *nghiệp vụ phức tạp và sống lâu*; đừng dùng cho mọi endpoint.
> - **"Screaming Architecture" vs framework convention.** Rails/Next.js/Spring Boot *cố ý* dictate cấu trúc theo framework để đi nhanh — ngược hẳn lời khuyên Ch.21. Với sản phẩm nhỏ/đời ngắn, "ôm framework" có lý (xem Bài 0, Bài 5). Đây là đánh đổi tốc-độ-ngắn-hạn vs độc-lập-dài-hạn.
> - **"Web/DB là chi tiết" trong kỷ nguyên serverless/edge:** càng đúng — business rule không nên biết nó chạy trên Lambda, container, hay edge. Nhưng ranh giới *testability* quan trọng hơn ranh giới *lý thuyết*: vẽ lằn ranh ở chỗ giúp bạn test và thay thế, không phải ở mọi tầng cho đủ sơ đồ.
> - **Vẫn vàng:** Dependency Rule (phụ thuộc trỏ vào trong), Entity thuần nghiệp vụ, và "framework là công cụ, không phải kiến trúc".

## 7. Áp dụng vào dự án của bạn

> [!question] Áp dụng vào dự án của bạn
> 1. **Kiểm Dependency Rule.** Mở một file "business logic" cốt lõi. Nó có `import` tên nào từ web framework/ORM/UI không? Nếu có, mũi tên đang trỏ *ra ngoài* — vi phạm. Đây là bài kiểm 30 giây cho Clean Architecture.
> 2. **Phép "hét lên".** Nhìn thư mục top-level: nó hét tên *nghiệp vụ* hay tên *framework*? (Từ Bài 5, giờ áp cho thật.)
> 3. **Cân nhắc có đáng bốn vòng không.** Phần bạn đang làm: nghiệp vụ phức tạp & sống lâu (→ Clean Architecture đáng) hay CRUD mỏng (→ vertical slice / gọi thẳng có thể đủ)? Đừng mặc định đủ bốn vòng cho mọi thứ.

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| :--- | :--- |
| **Entity** | Object chứa Critical Business Rules + Data; thuần nghiệp vụ, dùng được mọi app (tr. 189). |
| **Use Case** | Application-specific rules; điều phối Entity cho một ca dùng (tr. 203). |
| **Screaming Architecture** | Kiến trúc phải hét lên *nghiệp vụ*, không phải framework (tr. 195). |
| **The Dependency Rule** | Phụ thuộc mã nguồn chỉ được trỏ vào trong, về chính sách cao hơn (tr. 202). |
| **4 vòng** | Entities · Use Cases · Interface Adapters · Frameworks & Drivers (tr. 203+). |
| **Output port** | Interface do use case sở hữu; presenter/gateway ngoài hiện thực (mục 4–5). |
| **Vertical Slice** | (2026) Gom code theo tính năng xuyên tầng; đối trọng với bốn-vòng cho app nhỏ. |

## 9. Câu hỏi tự kiểm tra

1. Phân biệt Entity và Use Case: cái nào *enterprise-wide*, cái nào *application-specific*? Cái nào ổn định hơn? *(tr. 189, 203)*
2. "Kiến trúc của bạn hét lên điều gì?" — nên hét gì, không nên hét gì? *(tr. 195)*
3. Phát biểu Dependency Rule. Vì sao "không gì ở vòng trong được biết về vòng ngoài"? *(tr. 202)*
4. Trong demo, vì sao `Account` không bị ảnh hưởng khi đổi `Presenter`? Mũi tên phụ thuộc trỏ chiều nào? *(mục 4)*
5. Vì sao Vertical Slice được nêu như đối trọng của bốn-vòng năm 2026? *(Đối chiếu 2026)*

## Tóm tắt một trang

```
BÀI 7 — BUSINESS RULES & THE CLEAN ARCHITECTURE (bài trung tâm)
─────────────────────────────────────────────────────────
ENTITY  Critical Business Rules + Data; THUẦN nghiệp vụ, không biết
   DB/UI/framework (tr.189). USE CASE: application-specific rules (tr.203).

SCREAMING  "kiến trúc HÉT lên điều gì?" (tr.195) — nên hét "Hệ Kế toán",
   không hét "Rails/Spring". "framework là CÔNG CỤ, không phải kiến
   trúc để tuân theo" (tr.196).

4 VÒNG (ngoài=cơ chế, trong=chính sách):
   Frameworks&Drivers ▸ Interface Adapters ▸ Use Cases ▸ Entities
   DEPENDENCY RULE: "phụ thuộc mã nguồn CHỈ trỏ VÀO TRONG" (tr.202).
   "không gì ở vòng trong biết về vòng ngoài" (tr.202).

DEMO 4 vòng: Account(entity) ◄ UseCase ◄ Controller; Presenter hiện
   thực output port. Đổi UI/DB → Entity bất động. Rút quá số dư bị chặn.

VƯỢT RANH GIỚI  điều khiển ra-vào, phụ thuộc LUÔN vào trong (DIP + output port).
   Dữ liệu vượt ranh = struct đơn giản, không truyền Entity ra ngoài.

2026  hội tụ clean/hexagonal/onion. Phê bình: quá nhiều tầng cho app
   nhỏ → VERTICAL SLICE (Bogard). Dùng khi nghiệp vụ phức tạp & sống lâu.
```

## Nguồn

- **Robert C. Martin**, *Clean Architecture* (Prentice Hall, 2017) — **Ch.20 "Business Rules"** (`tr. 189–194`): Critical Business Rules/Data, định nghĩa Entity, "pure business and nothing else", Use Cases application-specific (tr. 189–192). **Ch.21 "Screaming Architecture"** (`tr. 195–200`): "what does your architecture scream", Rails/Spring, "frameworks are tools… not architectures to be conformed to", web là delivery mechanism (tr. 195–197). **Ch.22 "The Clean Architecture"** (`tr. 201–210`): bốn vòng đồng tâm, The Dependency Rule "point only inward", "nothing in an inner circle…", Entities, Use Cases, Interface Adapters, Frameworks & Drivers, crossing boundaries, DTO vượt ranh giới (tr. 202–210). `tai_lieu/Clean.Architecture.2017.9.pdf`
- Bối cảnh 2026 dẫn từ ngoài sách: hội tụ Hexagonal/Onion/Clean; Vertical Slice Architecture (Jimmy Bogard); framework convention (Rails/Next.js); serverless/edge.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 27`.

---

**Bản đồ khoá học:** [Bài 0 — Hai giá trị](bai_00_hai_gia_tri.md) · [Bài 1 — Ba hệ hình lập trình](bai_01_he_hinh_lap_trinh.md) · [Bài 2 — SOLID (1): SRP, OCP](bai_02_solid_srp_ocp.md) · [Bài 3 — SOLID (2): LSP, ISP, DIP](bai_03_solid_lsp_isp_dip.md) · [Bài 4 — Nguyên tắc Component](bai_04_nguyen_tac_component.md) · [Bài 5 — Kiến trúc là gì & Độc lập](bai_05_kien_truc_va_doc_lap.md) · [Bài 6 — Ranh giới & Dependency Rule](bai_06_ranh_gioi_dependency_rule.md) · [Bài 7 ← bạn đang ở đây] · [Bài 8 — Humble Object, Main, Services](bai_08_humble_main_services.md) · [Bài 9 — Chi tiết: DB, Web, Framework](bai_09_chi_tiet.md) · [Bài 10 — The Missing Chapter: đóng gói](bai_10_dong_goi.md) · [Bài 11 — Case study & tổng kết](bai_11_case_study.md)

Xem thêm [README khoá học](../README.md).
