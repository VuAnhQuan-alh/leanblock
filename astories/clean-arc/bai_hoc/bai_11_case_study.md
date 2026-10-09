# Bài 11 — Case study Video Sales & tổng kết khoá

> [!info] Về bài này
> Dựng từ **Ch.33 "Case Study: Video Sales"** của *Clean Architecture* (Robert C. Martin, 2017 — `tai_lieu/`, `tr. 297–302`), và tổng kết toàn khoá.
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 27`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Bài cuối: ráp **đủ bốn vòng** vào một ca thật (bán video), rồi gói lại hành trình 12 bài và cây cầu sang bộ ba Uncle Bob.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Ca Video Sales: bắt đầu từ actor và use case](#1-ca-video-sales-bắt-đầu-từ-actor-và-use-case)
2. [Hai chiều tách: theo actor và theo level](#2-hai-chiều-tách-theo-actor-và-theo-level)
3. [Code minh hoạ: ráp đủ bốn vòng cho một ca](#3-code-minh-hoạ-ráp-đủ-bốn-vòng-cho-một-ca)
4. [Cấu trúc trước, triển khai sau](#4-cấu-trúc-trước-triển-khai-sau)
5. [Tổng kết khoá: 12 bài một mạch](#5-tổng-kết-khoá-12-bài-một-mạch)
6. [Đối chiếu 2026: lấy gì, bỏ gì](#6-đối-chiếu-2026-lấy-gì-bỏ-gì)
7. [Áp dụng vào dự án của bạn](#7-áp-dụng-vào-dự-án-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Ca Video Sales: bắt đầu từ actor và use case

Uncle Bob lấy một website bán video dạy lập trình làm ca mẫu — và cách ông *bắt đầu* mới là bài học: không phải chọn DB hay framework, mà **nhận diện actor và use case**. Bốn actor chính: người mua (Viewer), tác giả (Author), quản trị (Admin), và người kiểm soát mua hàng (Purchaser). Theo SRP ([Bài 2](bai_02_solid_srp_ocp.md)):

> [!quote] Ch. 33 — Use Case Analysis (tr. 298)
> "According to the Single Responsibility Principle, these four actors will be the four primary sources of change for the system."
>
> *Theo Nguyên tắc Trách nhiệm Đơn, bốn actor này sẽ là **bốn nguồn thay đổi chính** của hệ thống.*

Vì vậy mục tiêu là *phân vùng* hệ thống sao cho một thay đổi của actor này không ảnh hưởng actor khác — đây là SRP ở tầm kiến trúc, dùng để *chia component*.

## 2. Hai chiều tách: theo actor và theo level

Kết luận chương gói cả cuốn sách vào hai chiều tách:

> [!quote] Ch. 33 — Conclusion (tr. 302)
> "The architecture diagram […] includes two dimensions of separation. The first is the separation of actors based on the Single Responsibility Principle; the second is the Dependency Rule."
>
> *Sơ đồ kiến trúc […] gồm **hai chiều tách**. Thứ nhất là tách theo **actor** dựa trên SRP; thứ hai là **Dependency Rule**.*

Gộp lại: tách theo actor (lý do thay đổi) *và* theo level (tốc độ thay đổi). Bảng hai chiều:

| Chiều tách | Dựa trên | Tách theo | Từ bài |
| :--- | :--- | :--- | :---: |
| Dọc — theo **actor** | SRP | *lý do* thay đổi (Viewer/Author/Admin…) | [Bài 2](bai_02_solid_srp_ocp.md) |
| Ngang — theo **level** | Dependency Rule | *tốc độ* thay đổi (Entity ổn định ↔ UI/DB hay đổi) | [Bài 7](bai_07_clean_architecture.md) |

## 3. Code minh hoạ: ráp đủ bốn vòng cho một ca

Capstone của khoá: một ca "mua video" chạy qua *cả bốn vòng*, gom mọi bài trước — Entity (business rule giảm giá sỉ), Use Case (input/output port), Interface Adapter (Gateway + Presenter, đều là *chi tiết*), và Main (composition root). Mọi phụ thuộc trỏ **vào trong**:

```typescript
import { strict as assert } from "node:assert";

// VÒNG 1 — ENTITY: Critical Business Rule (mua >=5 giảm 10%)
class VideoOrder {
  #unitPriceCents: number;
  #quantity: number;
  constructor(unitPriceCents: number, quantity: number) {
    this.#unitPriceCents = unitPriceCents;
    this.#quantity = quantity;
  }
  totalCents(): number {
    const raw = this.#unitPriceCents * this.#quantity;
    return this.#quantity >= 5 ? Math.round(raw * 0.9) : raw;
  }
}

// VÒNG 2 — USE CASE: ports (gateway vào, presenter ra)
interface VideoGateway { priceCents(videoId: string): number; }
interface PurchaseOutput { present(totalCents: number): void; }
class PurchaseVideoUseCase {
  #gateway: VideoGateway;
  #output: PurchaseOutput;
  constructor(gateway: VideoGateway, output: PurchaseOutput) {
    this.#gateway = gateway;
    this.#output = output;
  }
  execute(videoId: string, quantity: number): void {
    const unit = this.#gateway.priceCents(videoId);
    const order = new VideoOrder(unit, quantity);
    this.#output.present(order.totalCents());
  }
}

// VÒNG 3 — INTERFACE ADAPTERS: gateway (DB) + presenter (UI) — đều là CHI TIẾT
class InMemoryVideoGateway implements VideoGateway {
  priceCents(videoId: string): number {
    const prices: Record<string, number> = { "clean-arch": 20000 };
    return prices[videoId] ?? 0;
  }
}
class TextPresenter implements PurchaseOutput {
  view = "";
  present(totalCents: number): void { this.view = `Tổng: ${(totalCents / 100).toFixed(2)}đ`; }
}

// VÒNG 4 — MAIN: lắp ráp; mọi phụ thuộc trỏ VÀO TRONG
const presenter = new TextPresenter();
const useCase = new PurchaseVideoUseCase(new InMemoryVideoGateway(), presenter);

useCase.execute("clean-arch", 1);
console.log("mua 1:", presenter.view);
assert.equal(presenter.view, "Tổng: 200.00đ");

useCase.execute("clean-arch", 5); // mua sỉ -> giảm 10%
console.log("mua 5:", presenter.view);
assert.equal(presenter.view, "Tổng: 900.00đ");
console.log("đủ 4 vòng: Entity(giảm giá) ◄ UseCase(ports) ◄ Gateway/Presenter(chi tiết) ◄ Main.");
```

Kết quả chạy thật:

```
mua 1: Tổng: 200.00đ
mua 5: Tổng: 900.00đ
đủ 4 vòng: Entity(giảm giá) ◄ UseCase(ports) ◄ Gateway/Presenter(chi tiết) ◄ Main.
```

Toàn bộ khoá hội tụ ở đây: business rule (giảm giá sỉ) nằm trong `VideoOrder` (Entity) — [Bài 7](bai_07_clean_architecture.md); use case nói chuyện qua *port* — [Bài 6](bai_06_ranh_gioi_dependency_rule.md); Gateway/Presenter là *chi tiết* có thể thay (DB/UI) — [Bài 9](bai_09_chi_tiet.md); phụ thuộc đảo bằng interface — [Bài 1](bai_01_he_hinh_lap_trinh.md), [Bài 3](bai_03_solid_lsp_isp_dip.md); Main là composition root — [Bài 8](bai_08_humble_main_services.md). Đổi `InMemoryVideoGateway`→`SqlVideoGateway` hay `TextPresenter`→`JsonPresenter`: `VideoOrder` và `PurchaseVideoUseCase` *bất động*.

> [!note] Tự thử
> 1. Viết `JsonPresenter` trả `{"totalCents": n}`. Use case/Entity có đổi dòng nào không?
> 2. Thêm business rule: đơn > 1 triệu giảm thêm 5%. Bạn sửa vòng nào? (Chỉ Entity.)
> 3. Thêm actor "Author xem doanh thu" = một use case *mới* (`AuthorSalesUseCase`) dùng lại `VideoGateway`. Nó có buộc đổi `PurchaseVideoUseCase` không? (SRP: tách theo actor.)

## 4. Cấu trúc trước, triển khai sau

Điểm cuối của ca: một khi đã tách đúng theo actor + Dependency Rule, *cách triển khai* trở thành quyết định để-ngỏ:

> [!quote] Ch. 33 — Conclusion (tr. 302)
> "Once you have structured the code this way, you can mix and match how you want to actually deploy the system."
>
> *Một khi đã cấu trúc code theo lối này, bạn có thể **trộn và ghép** tuỳ ý cách thực sự triển khai hệ thống.*

Gom các component thành đơn vị triển khai (monolith, vài service, nhiều service) theo cách *hợp lý lúc này*, và đổi cách gom khi điều kiện đổi — đúng "giữ ngỏ decoupling mode" ([Bài 5](bai_05_kien_truc_va_doc_lap.md), [Bài 8](bai_08_humble_main_services.md)).

## 5. Tổng kết khoá: 12 bài một mạch

Toàn bộ khoá là *một* lập luận liền mạch, từ "vì sao" tới "làm sao":

| Bài | Mảnh ghép | Một câu |
| :---: | :--- | :--- |
| 0 | Hai giá trị | cấu trúc > hành vi về dài hạn; giữ phần mềm "mềm" |
| 1 | Ba hệ hình | OO cho ta quyền *đảo chiều phụ thuộc* (đa hình) |
| 2–3 | SOLID | SRP(actor) · OCP · LSP · ISP · DIP — luật về chiều phụ thuộc |
| 4 | Component | cohesion (REP/CCP/CRP) + coupling (ADP/SDP/SAP), không chu trình |
| 5 | Kiến trúc & độc lập | kiến trúc = giữ ngỏ lựa chọn càng lâu càng tốt |
| 6 | Ranh giới | vẽ lằn ranh; mũi tên trỏ về nghiệp vụ cốt lõi |
| 7 | **The Clean Architecture** | bốn vòng + Dependency Rule (phụ thuộc trỏ vào trong) |
| 8 | Humble/Main/Services | test được ranh giới; micro-service không tự cho kiến trúc |
| 9 | Chi tiết | DB/web/framework đều là chi tiết ở vòng ngoài |
| 10 | Đóng gói | ánh xạ thiết kế → thư mục; compiler cưỡng chế ranh giới |
| 11 | Case study | ráp đủ, tách theo actor + level, triển khai sau |

Hạt nhân của cả 12 bài, nếu phải rút về một câu: **đặt business rule vào trung tâm, đẩy mọi chi tiết (DB, web, framework, UI) ra rìa, và bắt mọi phụ thuộc mã nguồn trỏ vào trong.**

## 6. Đối chiếu 2026: lấy gì, bỏ gì

> [!warning] Đối chiếu 2026 — tổng hợp cả khoá
> Sau 12 bài, đây là bản cân cuối cùng cho năm 2026:
> - **LẤY (bất tử):** Dependency Rule, business rule độc lập chi tiết, "framework là công cụ không phải kiến trúc", "database/web là chi tiết", test là một phần kiến trúc, tách theo actor + level. Những điều này đúng với *mọi* phong cách (hexagonal/onion/clean hội tụ).
> - **CÂN (tuỳ ngữ cảnh):** *mức* trừu tượng. Clean Architecture đầy đủ (4 vòng + port + presenter + DTO mapper) **đáng** cho nghiệp vụ phức tạp, sống lâu, nhiều actor. Nó là **over-engineering** cho CRUD nhỏ, prototype, app đời ngắn — nơi **vertical slice** hoặc gọi thẳng framework nhanh hơn và đủ. Chính Uncle Bob đã mở đường cho sự thực dụng này: "giữ ngỏ lựa chọn", "ranh giới một phần", Simon Brown "be pragmatic".
> - **BỎ / cập nhật:** ví dụ công nghệ (EJB, Spring XML, AspectJ) đã cũ; micro-service-vì-trend đã thoái trào (modular monolith lên); FP từ ngách thành chủ đạo. Tinh thần giữ nguyên, công cụ đổi.
> - **Thời AI (2026):** AI sinh *hành vi* và *scaffold framework* cực rẻ → giá trị dịch về phía *cấu trúc* và *ranh giới* — thứ cần phán đoán con người. Khoá này dạy đúng phần đó.
> - **Kim chỉ nam ponytail:** vẽ một lằn ranh *khi và chỉ khi* nó giúp bạn test, thay thế, hoặc chia việc — không phải để đủ sơ đồ. "The only way to go fast is to go well" ([Bài 0](bai_00_hai_gia_tri.md)) đúng; nhưng "go well" ≠ "vẽ mọi vòng cho mọi thứ".

## 7. Áp dụng vào dự án của bạn

> [!question] Khép lại: ba việc sau khoá
> 1. **Chạy "bài kiểm 30 giây".** Mở business logic cốt lõi: nó `import` tên nào từ DB/web/framework không? 0 → kiến trúc sạch; có → bạn vừa tìm ra nợ kiến trúc đầu tiên để trả.
> 2. **Vẽ hai chiều tách cho dự án của bạn.** Liệt kê các *actor* (ai yêu cầu đổi) và các *level* (ổn định ↔ hay đổi). Code của bạn có tách theo cả hai không?
> 3. **Quyết mức đầu tư có ý thức.** Phần bạn đang làm xứng mấy vòng? Nghiệp vụ phức tạp & lâu dài → tiến tới bốn vòng. CRUD mỏng → vertical slice là đủ. Ghi lại lý do — đó là tư duy kiến trúc sư.
> 4. **Nối sang nghề.** Bạn vừa xong bộ ba: [`clean-code`](../../clean-code/README.md) (viết code sạch) → `clean-arc` (cấu trúc sạch) → [`clean-coder`](../../clean-coder/README.md) (hành xử sạch). Cả ba là một: *giá trị dẫn dắt kỷ luật*.

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| :--- | :--- |
| **Actor** | Nhóm yêu cầu thay đổi; nguồn thay đổi để tách component theo SRP (tr. 298). |
| **Hai chiều tách** | Theo actor (SRP, *lý do* đổi) + theo level (Dependency Rule, *tốc độ* đổi) (tr. 302). |
| **Mix and match deploy** | Cấu trúc đúng rồi thì cách triển khai (monolith/service) để ngỏ, đổi được (tr. 302). |
| **Composition root** | `Main` — nơi lắp ráp mọi phụ thuộc (Bài 8). |
| **Vertical slice** | (2026) Gom theo tính năng xuyên tầng; đối trọng thực dụng của bốn-vòng. |

## 9. Câu hỏi tự kiểm tra

1. Uncle Bob *bắt đầu* thiết kế ca Video Sales bằng gì (không phải DB/framework)? *(tr. 297–298)*
2. "Hai chiều tách" là gì? Mỗi chiều dựa trên nguyên tắc nào? *(tr. 302)*
3. Trong demo, đổi Gateway (DB) hay Presenter (UI) có buộc đổi Entity/Use Case không? Vì sao? *(mục 3)*
4. "Mix and match deploy" nghĩa là gì, và vì sao chỉ làm được *sau khi* cấu trúc đúng? *(tr. 302)*
5. Khi nào Clean Architecture đầy đủ là *đáng*, khi nào là *over-engineering*? *(Đối chiếu 2026)*

## Tóm tắt một trang

```
BÀI 11 — CASE STUDY VIDEO SALES & TỔNG KẾT
─────────────────────────────────────────────────────────
BẮT ĐẦU từ ACTOR + USE CASE, không phải DB/framework.
   "4 actor = 4 nguồn thay đổi chính" (SRP, tr.298).

HAI CHIỀU TÁCH (tr.302):
   · theo ACTOR (SRP)  — lý do đổi (Viewer/Author/Admin…)
   · theo LEVEL (Dep. Rule) — tốc độ đổi (Entity ổn ↔ UI/DB hay đổi)

DEMO capstone: VideoOrder(entity, giảm giá sỉ) ◄ PurchaseUseCase(ports)
   ◄ Gateway/Presenter(chi tiết) ◄ Main. mua1=200đ, mua5=900đ.
   Đổi DB/UI → Entity+UseCase bất động.

"cấu trúc xong rồi MỚI mix-and-match cách deploy" (tr.302).

HẠT NHÂN CẢ KHOÁ: business rule vào TRUNG TÂM, chi tiết (DB/web/
   framework/UI) ra RÌA, mọi phụ thuộc mã nguồn trỏ VÀO TRONG.

2026  LẤY: Dependency Rule, chi-tiết-ở-rìa, test-là-kiến-trúc (bất tử).
   CÂN: mức trừu tượng — bốn vòng cho nghiệp vụ phức tạp/lâu dài;
   vertical slice cho CRUD nhỏ. Vẽ lằn ranh KHI nó giúp test/thay/chia việc.
   Bộ ba: clean-code → clean-arc → clean-coder = GIÁ TRỊ DẪN DẮT KỶ LUẬT.
```

## Nguồn

- **Robert C. Martin**, *Clean Architecture* (Prentice Hall, 2017) — **Ch.33 "Case Study: Video Sales"** (`tr. 297–302`): bắt đầu từ actor + use case, "four actors will be the four primary sources of change" theo SRP (tr. 297–298); abstract use cases, phân vùng theo actor (tr. 299–301); kết luận "two dimensions of separation" (actor theo SRP + Dependency Rule), "mix and match how you want to actually deploy" (tr. 302). `tai_lieu/Clean.Architecture.2017.9.pdf`
- Tổng hợp 2026 dẫn từ ngoài sách: hội tụ Hexagonal/Onion/Clean; vertical slice (Jimmy Bogard); modular monolith; AI scaffolding; YAGNI/ponytail.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 27`.

---

**Bản đồ khoá học:** [Bài 0 — Hai giá trị](bai_00_hai_gia_tri.md) · [Bài 1 — Ba hệ hình lập trình](bai_01_he_hinh_lap_trinh.md) · [Bài 2 — SOLID (1): SRP, OCP](bai_02_solid_srp_ocp.md) · [Bài 3 — SOLID (2): LSP, ISP, DIP](bai_03_solid_lsp_isp_dip.md) · [Bài 4 — Nguyên tắc Component](bai_04_nguyen_tac_component.md) · [Bài 5 — Kiến trúc là gì & Độc lập](bai_05_kien_truc_va_doc_lap.md) · [Bài 6 — Ranh giới & Dependency Rule](bai_06_ranh_gioi_dependency_rule.md) · [Bài 7 — Business Rules & The Clean Architecture](bai_07_clean_architecture.md) · [Bài 8 — Humble Object, Main, Services](bai_08_humble_main_services.md) · [Bài 9 — Chi tiết: DB, Web, Framework](bai_09_chi_tiet.md) · [Bài 10 — The Missing Chapter: đóng gói](bai_10_dong_goi.md) · [Bài 11 ← bạn đang ở đây]

Xem thêm [README khoá học](../README.md).
