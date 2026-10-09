# Bài 8 — Humble Object, Main, và Services lớn-nhỏ

> [!info] Về bài này
> Chưng cất từ **Phần V — Architecture**: **Ch.23 "Presenters and Humble Objects"**, **Ch.24 "Partial Boundaries"**, **Ch.25 "Layers and Boundaries"**, **Ch.26 "The Main Component"**, **Ch.27 "Services: Great and Small"**, **Ch.28 "The Test Boundary"** của *Clean Architecture* (Robert C. Martin, 2017 — `tai_lieu/`, `tr. 211–254`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 27`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Gom các chương "chiến thuật" quanh vòng tròn [Bài 7](bai_07_clean_architecture.md): làm sao *test được* ranh giới, lắp ráp ở đâu, và micro-service có tự cho bạn kiến trúc không.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Humble Object: tách cái khó-test khỏi cái dễ-test](#1-humble-object-tách-cái-khó-test-khỏi-cái-dễ-test)
2. [Code minh hoạ: Presenter test được, View humble](#2-code-minh-hoạ-presenter-test-được-view-humble)
3. [Ranh giới một phần: ranh giới tốn tiền](#3-ranh-giới-một-phần-ranh-giới-tốn-tiền)
4. [Main Component: chi tiết bẩn nhất, ngoài cùng nhất](#4-main-component-chi-tiết-bẩn-nhất-ngoài-cùng-nhất)
5. [Services lớn-nhỏ: micro-service không tự cho bạn kiến trúc](#5-services-lớn-nhỏ-micro-service-không-tự-cho-bạn-kiến-trúc)
6. [Test Boundary: test là một phần của hệ thống](#6-test-boundary-test-là-một-phần-của-hệ-thống)
7. [Đối chiếu 2026](#7-đối-chiếu-2026)
8. [Áp dụng vào dự án của bạn](#8-áp-dụng-vào-dự-án-của-bạn)
9. [Từ điển thuật ngữ](#9-từ-điển-thuật-ngữ)
10. [Câu hỏi tự kiểm tra](#10-câu-hỏi-tự-kiểm-tra)
11. [Tóm tắt một trang](#tóm-tắt-một-trang)
12. [Nguồn](#nguồn)

---

## 1. Humble Object: tách cái khó-test khỏi cái dễ-test

Presenter (vòng Interface Adapter ở [Bài 7](bai_07_clean_architecture.md)) là một dạng của **Humble Object pattern**:

> [!quote] Ch. 23 — Presenters and Humble Objects (tr. 211)
> "The Humble Object pattern […] is a design pattern that was originally identified as a way to help unit testers to separate behaviors that are hard to test from behaviors that are easy to test."
>
> *Mẫu **Humble Object** là một mẫu thiết kế ban đầu được nhận ra như một cách giúp người viết unit test **tách hành vi khó test khỏi hành vi dễ test**.*

Ý tưởng cực đơn giản: chẻ hành vi thành hai module. Một module là *humble* (khiêm nhường) — chứa phần khó test, bị lột xuống còn tối thiểu (ví dụ: GUI chỉ đặt chữ lên màn hình). Module kia chứa *mọi* hành vi test được, đã bị tách ra khỏi humble object. Với GUI: logic *quyết định hiển thị gì* (Presenter) là dễ test; việc *thực sự vẽ lên màn hình* (View) là humble.

## 2. Code minh hoạ: Presenter test được, View humble

```typescript
import { strict as assert } from "node:assert";

// ViewModel: dữ liệu đã format sẵn, chỉ việc hiển thị
type ScoreViewModel = { label: string; color: string };

// ===== PHẦN DỄ TEST (Presenter): toàn bộ LOGIC format nằm đây =====
function presentScore(score: number): ScoreViewModel {
  const label = `Điểm: ${score}/100`;
  const color = score >= 50 ? "green" : "red";
  return { label, color };
}

// ===== PHẦN HUMBLE (View): KHÔNG logic, chỉ "vẽ" ViewModel =====
// (ở đời là GUI khó test; ở đây mô phỏng bằng render chuỗi)
function humbleView(vm: ScoreViewModel): string {
  return `<span style="color:${vm.color}">${vm.label}</span>`;
}

// test PHẦN LOGIC mà KHÔNG cần GUI nào
assert.deepEqual(presentScore(80), { label: "Điểm: 80/100", color: "green" });
assert.deepEqual(presentScore(30), { label: "Điểm: 30/100", color: "red" });
console.log("present(80):", JSON.stringify(presentScore(80)));
console.log("present(30):", JSON.stringify(presentScore(30)));
console.log("view(80)   :", humbleView(presentScore(80)));
console.log("toàn bộ logic trong Presenter (test được); View chỉ vẽ ViewModel (humble).");
```

Kết quả chạy thật:

```
present(80): {"label":"Điểm: 80/100","color":"green"}
present(30): {"label":"Điểm: 30/100","color":"red"}
view(80)   : <span style="color:green">Điểm: 80/100</span>
toàn bộ logic trong Presenter (test được); View chỉ vẽ ViewModel (humble).
```

Mọi *quyết định* (nhãn gì, màu gì theo ngưỡng 50) nằm trong `presentScore` — một hàm thuần, test bằng `assert.deepEqual` không cần trình duyệt. `humbleView` chỉ bơm ViewModel vào khung HTML, không có nhánh logic nào để sai → *không cần* test. Ranh giới "test được / khó test" được vẽ ngay giữa Presenter và View. Đây là cách Clean Architecture làm cho các ranh giới ([Bài 6](bai_06_ranh_gioi_dependency_rule.md)) *test được*.

> [!note] Tự thử
> 1. Thêm ngưỡng thứ ba: score ≥ 80 → `"gold"`. Bạn sửa `presentScore` hay `humbleView`? Test nằm ở đâu?
> 2. `humbleView` có nhánh `if` nào không? Vì sao "không logic" nghĩa là "không cần test"?
> 3. Nếu bạn nhét logic chọn màu vào trong `humbleView` (phần GUI), vì sao nó thành khó test? (Đó là lý do phải *lột* humble object xuống tối thiểu.)

## 3. Ranh giới một phần: ranh giới tốn tiền

Vẽ một ranh giới *đầy đủ* (interface hai chiều + input/output data struct + hai lớp adapter) rất tốn — nhiều code, nhiều "cơ sở hạ tầng". Khi bạn *ngờ* sẽ cần một ranh giới nhưng chưa chắc, Ch.24 đưa các **ranh giới một phần** (partial boundary) rẻ hơn:

| Kiểu ranh giới một phần | Làm gì | Đánh đổi |
| :--- | :--- | :--- |
| Bỏ bước cuối | dựng đủ interface hai chiều nhưng để *chung một component* | giữ sẵn khả năng tách, chưa trả giá tách |
| Một chiều (one-dimensional) | chỉ một interface (Strategy) thay vì hai | rẻ hơn, nhưng dễ bị "rò" phụ thuộc ngược |
| **Facade** | một lớp mặt tiền gom lời gọi | rẻ nhất, nhưng *không* đảo được phụ thuộc |

Thông điệp: ranh giới là một *quyết định có giá*; chọn mức đầu tư khớp với mức bạn *tin* rằng sẽ cần — đúng tinh thần "giữ ngỏ lựa chọn" ([Bài 5](bai_05_kien_truc_va_doc_lap.md)) và YAGNI.

## 4. Main Component: chi tiết bẩn nhất, ngoài cùng nhất

Mọi hệ cần một nơi lắp ráp — và nó nằm ở *vòng ngoài cùng*:

> [!quote] Ch. 26 — The Main Component (tr. 231)
> "The Main component is the ultimate detail—the lowest-level policy. It is the initial entry point of the system."
>
> *Component **Main** là **chi tiết tối hậu** — chính sách mức thấp nhất. Nó là điểm vào ban đầu của hệ thống.*

Main là nơi tạo mọi object, nối mọi dây, rồi trao quyền điều khiển cho phần mức cao. Nó *được phép* bẩn:

> [!quote] Ch. 26 — The Main Component (tr. 231)
> "Think of Main as the dirtiest of all the dirty components."
>
> *Hãy coi Main là **component bẩn nhất trong mọi component bẩn**.*

Vì Main là *plugin của ứng dụng* — plugin cài đặt cấu hình ban đầu, nối dependency, rồi lùi ra. Đây chính là *composition root* đã gặp ở [Bài 10 `clean-code`](../../clean-code/bai_hoc/bai_10_he_thong.md) và là vòng 4 trong demo [Bài 7](bai_07_clean_architecture.md): `main()` biết mọi thứ cụ thể để phần còn lại khỏi phải biết.

## 5. Services lớn-nhỏ: micro-service không tự cho bạn kiến trúc

Chương gây tỉnh ngộ nhất Phần V — phản biện trực tiếp cơn sốt micro-service:

> [!quote] Ch. 27 — Service Architecture? (tr. 239)
> "services, in and of themselves, do not define an architecture."
>
> *bản thân các **service**, tự chúng, **không** định nghĩa một kiến trúc.*

Hai ngộ nhận Uncle Bob đập:

- **"Service tách ghép mạnh" là *decoupling fallacy*.** Service tách ghép ở mức biến/bộ nhớ, đúng; nhưng chúng vẫn có thể *ghép chặt* qua **dữ liệu chia sẻ** và **cross-cutting concern**. Một thay đổi nghiệp vụ xuyên suốt (thêm một field vào một khái niệm dùng chung) buộc *mọi* service đổi theo → "các service đều ghép, không phát triển độc lập được".
- **"Service cho phép phát triển/triển khai độc lập" — chỉ đúng một phần.** Hệ lớn dựng được từ monolith và hệ component *cũng tốt như* hệ service. Service **không phải** cách duy nhất.

Lời giải của sách: dù dùng service hay không, *vẫn phải* áp Dependency Rule và component bên trong mỗi service (ví dụ thiết kế theo tính năng "Kitty" cắt dọc, giữ nó tách ghép thật). Kiến trúc nằm ở *ranh giới và chiều phụ thuộc*, không ở chỗ có gọi qua mạng hay không.

## 6. Test Boundary: test là một phần của hệ thống

> [!quote] Ch. 28 — The Test Boundary (tr. 249)
> "The tests are part of the system, and they participate in the architecture just like every other part of the system does."
>
> *Test **là một phần của hệ thống**, và chúng tham gia vào kiến trúc y như mọi phần khác.*

Test là component *cô lập nhất* (không ai phụ thuộc test) và *triển khai độc lập*. Nhưng nếu test ghép chặt vào cấu trúc *khả biến* của hệ (ví dụ mọi test gọi qua GUI, hay bám sát schema), thì một thay đổi nhỏ làm *hàng trăm* test gãy:

> [!quote] Ch. 28 — Design for Testability (tr. 251)
> "Tests that are not well integrated into the design of the system tend to be fragile, and they make the system rigid and difficult to change."
>
> *Test **không được tích hợp tốt** vào thiết kế hệ thống thường **mong manh**, và khiến hệ thống cứng nhắc, khó đổi.*

Đây là **Fragile Tests Problem**. Lời giải: đừng để test phụ thuộc thứ hay đổi; test qua các API ổn định (một *test API* riêng), đúng tinh thần F.I.R.S.T ở [`clean-code` Bài 8](../../clean-code/bai_hoc/bai_08_unit_test.md).

## 7. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Chương 27 (Services) là chỗ Uncle Bob **tiên tri đúng nhất** cho thập niên sau:
> - **"Micro-service không tự cho bạn kiến trúc" — 2026 đã thấm bằng máu.** Viết 2017 giữa đỉnh sốt microservices, câu này nay là đồng thuận: **distributed monolith** (các service ghép chặt qua dữ liệu chia sẻ, phải deploy cùng nhau) là phản mẫu phổ biến — đúng *decoupling fallacy* sách cảnh báo. Amazon Prime Video (2023) gộp microservice về monolith giảm 90% chi phí; làn sóng **modular monolith** lên ngôi. Kiến trúc *bên trong* mỗi service (Dependency Rule, component) quan trọng hơn việc có bao nhiêu service.
> - **Humble Object — sống khoẻ và tự động hoá.** Năm 2026 đây là nền của **Testing Library** (test hành vi qua ViewModel/DOM, không test chi tiết render), MVVM, MVP, và "tách logic khỏi framework UI" (React: tách custom hook khỏi component). "Lột GUI xuống tối thiểu" = component mỏng + logic trong hook/presenter.
> - **Fragile Tests Problem → cảnh báo về test coupling 2026.** Test E2E bám UI dễ gãy là lý do Testing Trophy ([`clean-code` Bài 8](../../clean-code/bai_hoc/bai_08_unit_test.md)) nhấn integration test ổn định hơn. "Test là một phần kiến trúc" = test cũng phải tuân Dependency Rule.
> - **Partial boundaries ↔ YAGNI (ponytail).** Ranh giới một phần chính là câu trả lời thực dụng cho "đừng vẽ ranh giới đầy đủ khi chưa cần": bắt đầu bằng Facade/một-chiều rẻ, nâng cấp khi *thật sự* cần tách. Đây là liều giải độc cho over-engineering của Clean Architecture.
> - **Main = composition root** vẫn chuẩn 2026 (dù nay thường là DI container cấu hình ở bootstrap — xem [`clean-code` Bài 10](../../clean-code/bai_hoc/bai_10_he_thong.md)).

## 8. Áp dụng vào dự án của bạn

> [!question] Áp dụng vào dự án của bạn
> 1. **Tìm logic kẹt trong GUI.** Component UI của bạn có nhánh `if`/tính toán/format nào *bên trong* không? Rút ra một presenter/hook thuần để test được — để lại View humble.
> 2. **Soi "distributed monolith".** Nếu dự án có nhiều service: đổi một khái niệm nghiệp vụ có buộc deploy nhiều service cùng lúc không? Nếu có, bạn đang dính decoupling fallacy — service đang ghép chặt.
> 3. **Tìm Fragile Test.** Có thay đổi nhỏ nào từng làm *hàng loạt* test gãy không? Chúng bám vào cấu trúc khả biến gì (GUI? schema?)? Tách chúng ra sau một API ổn định.
> 4. **Chọn mức ranh giới rẻ.** Chỗ bạn *ngờ* sẽ cần tách: thử một Facade/interface một-chiều trước, đừng dựng ranh giới đầy đủ vội.

## 9. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| :--- | :--- |
| **Humble Object** | Tách hành vi khó-test (humble, tối thiểu) khỏi hành vi dễ-test (logic) (tr. 211). |
| **Presenter / View** | Presenter format → ViewModel (test được); View chỉ vẽ (humble). |
| **Partial boundary** | Ranh giới rẻ hơn ranh giới đầy đủ: bỏ bước cuối / một chiều / Facade (Ch.24). |
| **Main Component** | Chi tiết tối hậu, bẩn nhất, ngoài cùng; composition root (tr. 231). |
| **Decoupling fallacy** | Ngộ nhận rằng service tự tách ghép — chúng vẫn ghép qua dữ liệu/cross-cutting (tr. 239+). |
| **Fragile Tests Problem** | Test ghép chặt cấu trúc khả biến → đổi nhỏ gãy hàng loạt test (tr. 251). |

## 10. Câu hỏi tự kiểm tra

1. Humble Object tách cái gì khỏi cái gì? Presenter và View, cái nào test được? *(tr. 211, mục 2)*
2. Vì sao `humbleView` trong demo "không cần test"? *(mục 2)*
3. Vì sao Main "được phép bẩn nhất"? Nó làm gì rồi lùi ra? *(tr. 231)*
4. "Decoupling fallacy" của service là gì? Service có tự cho bạn kiến trúc không? *(tr. 239)*
5. Fragile Tests Problem xảy ra khi nào? Cách tránh? *(tr. 251)*

## Tóm tắt một trang

```
BÀI 8 — HUMBLE OBJECT, MAIN, SERVICES LỚN-NHỎ
─────────────────────────────────────────────────────────
HUMBLE OBJECT (tr.211)  tách KHÓ-test (humble, tối thiểu) khỏi
   DỄ-test (logic). Presenter format→ViewModel (test được);
   View chỉ vẽ (humble, không cần test).

RANH GIỚI MỘT PHẦN (Ch.24)  ranh giới ĐẦY ĐỦ tốn tiền → bỏ-bước-cuối /
   một-chiều / Facade. Khớp đầu tư với mức TIN là sẽ cần (YAGNI).

MAIN (tr.231)  "chi tiết tối hậu, bẩn nhất", ngoài cùng. Lắp ráp mọi
   dây rồi lùi ra = composition root.

SERVICES (tr.239)  "service tự nó KHÔNG định nghĩa kiến trúc".
   decoupling fallacy: service vẫn ghép qua dữ liệu + cross-cutting.
   Monolith/component cũng tốt. Kiến trúc nằm ở RANH GIỚI, không ở mạng.

TEST (tr.249)  "test LÀ một phần hệ thống". Fragile Tests Problem (tr.251):
   test bám cấu trúc khả biến → đổi nhỏ gãy hàng loạt. Test qua API ổn định.

2026  "microservice không tự cho kiến trúc" = đồng thuận (distributed
   monolith là phản mẫu; Prime Video gộp về monolith). Humble Object
   = Testing Library/MVVM/React hook. Partial boundary = liều giải độc
   over-engineering.
```

## Nguồn

- **Robert C. Martin**, *Clean Architecture* (Prentice Hall, 2017) — **Ch.23 "Presenters and Humble Objects"** (`tr. 211–216`): định nghĩa Humble Object, GUI khó test, Presenter/View (tr. 211–213). **Ch.24 "Partial Boundaries"** (`tr. 217–220`): bỏ bước cuối, một chiều, Facade. **Ch.25 "Layers and Boundaries"** (`tr. 221–230`): bao nhiêu ranh giới, Hunt the Wumpus, ranh giới tốn tiền. **Ch.26 "The Main Component"** (`tr. 231–238`): "ultimate detail", "dirtiest of all", composition root (tr. 231–237). **Ch.27 "Services: Great and Small"** (`tr. 239–248`): "services do not define an architecture", decoupling fallacy, cross-cutting concerns, Kitty feature (tr. 239–247). **Ch.28 "The Test Boundary"** (`tr. 249–254`): "tests are part of the system", Fragile Tests Problem, design for testability (tr. 249–252). `tai_lieu/Clean.Architecture.2017.9.pdf`
- Bối cảnh 2026 dẫn từ ngoài sách: distributed monolith; Amazon Prime Video 2023; modular monolith; Testing Library/MVVM; React custom hooks; YAGNI.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 27`.

---

**Bản đồ khoá học:** [Bài 0 — Hai giá trị](bai_00_hai_gia_tri.md) · [Bài 1 — Ba hệ hình lập trình](bai_01_he_hinh_lap_trinh.md) · [Bài 2 — SOLID (1): SRP, OCP](bai_02_solid_srp_ocp.md) · [Bài 3 — SOLID (2): LSP, ISP, DIP](bai_03_solid_lsp_isp_dip.md) · [Bài 4 — Nguyên tắc Component](bai_04_nguyen_tac_component.md) · [Bài 5 — Kiến trúc là gì & Độc lập](bai_05_kien_truc_va_doc_lap.md) · [Bài 6 — Ranh giới & Dependency Rule](bai_06_ranh_gioi_dependency_rule.md) · [Bài 7 — Business Rules & The Clean Architecture](bai_07_clean_architecture.md) · [Bài 8 ← bạn đang ở đây] · [Bài 9 — Chi tiết: DB, Web, Framework](bai_09_chi_tiet.md) · [Bài 10 — The Missing Chapter: đóng gói](bai_10_dong_goi.md) · [Bài 11 — Case study & tổng kết](bai_11_case_study.md)

Xem thêm [README khoá học](../README.md).
