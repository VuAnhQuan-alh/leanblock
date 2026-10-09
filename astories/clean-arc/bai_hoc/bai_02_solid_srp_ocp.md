# Bài 2 — SOLID (1): SRP và OCP ở tầm kiến trúc

> [!info] Về bài này
> Dựng từ **Phần III — Design Principles**: **Ch.7 "SRP: The Single Responsibility Principle"** và **Ch.8 "OCP: The Open-Closed Principle"** của *Clean Architecture* (Robert C. Martin, 2017 — `tai_lieu/`, `tr. 61–76`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 27`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> **Chống trùng với [`clean-code` Bài 9](../../clean-code/bai_hoc/bai_09_class.md):** ở đó SOLID nhìn ở mức *class*; ở đây nhìn ở mức *actor / component / kiến trúc*. Bài này nhấn đúng tầng đó.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: SOLID là gì, ở tầng nào](#1-mở-đầu-solid-là-gì-ở-tầng-nào)
2. [SRP: trách nhiệm trước MỘT actor, không phải "làm một việc"](#2-srp-trách-nhiệm-trước-một-actor-không-phải-làm-một-việc)
3. [Code minh hoạ: thay đổi của CFO rò rỉ sang COO](#3-code-minh-hoạ-thay-đổi-của-cfo-rò-rỉ-sang-coo)
4. [OCP: mở cho mở rộng, đóng với sửa đổi](#4-ocp-mở-cho-mở-rộng-đóng-với-sửa-đổi)
5. [OCP ở tầm component: chiều phụ thuộc để bảo vệ](#5-ocp-ở-tầm-component-chiều-phụ-thuộc-để-bảo-vệ)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào dự án của bạn](#7-áp-dụng-vào-dự-án-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mở đầu: SOLID là gì, ở tầng nào

SOLID là năm nguyên tắc sắp xếp *hàm và cấu trúc dữ liệu thành lớp*, và cách nối các lớp ấy. Nhưng trong *Clean Architecture*, Uncle Bob nhấn: cùng những nguyên tắc đó áp **ở mức component và kiến trúc**, không chỉ mức class. Bảng năm nguyên tắc (sẽ trải qua Bài 2–3):

| Chữ | Nguyên tắc | Một câu | Chương |
| :---: | :--- | :--- | :---: |
| **S** | Single Responsibility | một module trách nhiệm trước **một actor** | Ch.7 |
| **O** | Open-Closed | mở cho mở rộng, đóng với sửa đổi | Ch.8 |
| **L** | Liskov Substitution | lớp con thay được lớp cha | Ch.9 |
| **I** | Interface Segregation | đừng ép phụ thuộc thứ không dùng | Ch.10 |
| **D** | Dependency Inversion | phụ thuộc trừu tượng, không chi tiết | Ch.11 |

## 2. SRP: trách nhiệm trước MỘT actor, không phải "làm một việc"

SRP là nguyên tắc **bị hiểu nhầm nhiều nhất**, vì cái tên dễ khiến người ta tưởng "mỗi module chỉ làm một việc". Uncle Bob tách bạch:

> [!quote] Ch. 7 — SRP (tr. 61)
> "A function should do one, and only one, thing. We use that principle when we are refactoring large functions into smaller functions […] But it is not one of the SOLID principles—it is not the SRP."
>
> *Một **hàm** nên làm một, và chỉ một, việc. Ta dùng nguyên tắc đó khi refactor hàm lớn thành hàm nhỏ […] Nhưng đó **không** phải một nguyên tắc SOLID — nó **không** phải SRP.*

"Làm một việc" là chuyện mức hàm ([`clean-code` Bài 2](../../clean-code/bai_hoc/bai_02_ham.md)). SRP thì khác tầng. Lịch sử nó là "một lý do để thay đổi", mà "lý do" chính là *người* muốn thay đổi — gom lại thành **actor**:

> [!quote] Ch. 7 — SRP (tr. 61)
> "A module should be responsible to one, and only one, actor."
>
> *Một module nên chịu trách nhiệm trước một, và chỉ một, **actor** (nhóm người yêu cầu thay đổi).*

Và "module" đơn giản nhất là một *source file* — một tập hàm + dữ liệu *cohesive*. "Cohesion chính là lực gắn kết đoạn code cùng phục vụ một actor" (tr. 62). Vi phạm SRP lộ ra qua các *triệu chứng*, mà triệu chứng số một là **trùng lặp tình cờ** (accidental duplication).

## 3. Code minh hoạ: thay đổi của CFO rò rỉ sang COO

Ví dụ ruột của chương: lớp `Employee` có ba method phục vụ **ba actor khác nhau** — `calculatePay()` (kế toán, báo cáo lên **CFO**), `reportHours()` (nhân sự, lên **COO**), `save()` (DBA, lên **CTO**). Nguy hiểm nảy sinh khi hai actor *dùng chung* một hàm phụ:

```typescript
import { strict as assert } from "node:assert";
type EmployeeData = { hoursWorked: number; hourlyRate: number };

// ===== VI PHẠM SRP: regularHours() dùng CHUNG cho CFO và COO =====
function makeBad(cap: number) {
  const regularHours = (d: EmployeeData) => Math.min(d.hoursWorked, cap);
  return {
    calculatePay: (d: EmployeeData) => regularHours(d) * d.hourlyRate, // actor: CFO
    reportHours: (d: EmployeeData) => regularHours(d), // actor: COO (DÙNG CHUNG)
  };
}

// ===== TÁCH theo actor: COO có định nghĩa RIÊNG, không dính CFO =====
function payCalculator(cap: number) {
  return { calculatePay: (d: EmployeeData) => Math.min(d.hoursWorked, cap) * d.hourlyRate };
}
const hourReporter = { reportHours: (d: EmployeeData) => d.hoursWorked }; // COO: giờ THẬT

const emp: EmployeeData = { hoursWorked: 50, hourlyRate: 10 };

// CFO đổi chính sách: cap 40 -> 45 (tính thêm 5 giờ vào lương thường)
const badBefore = makeBad(40);
const badAfter = makeBad(45);
console.log("[BẨN] COO báo cáo giờ, cap=40:", badBefore.reportHours(emp));
console.log("[BẨN] COO báo cáo giờ, cap=45:", badAfter.reportHours(emp), "← COO không yêu cầu mà số ĐỔI!");

// bản tách: COO luôn báo cáo giờ thật, bất kể CFO đổi gì
console.log("[SẠCH] COO báo cáo giờ (tách):", hourReporter.reportHours(emp));
assert.equal(hourReporter.reportHours(emp), 50);
console.log("thay đổi của CFO không còn rò rỉ sang báo cáo của COO.");
```

Kết quả chạy thật:

```
[BẨN] COO báo cáo giờ, cap=40: 40
[BẨN] COO báo cáo giờ, cap=45: 45 ← COO không yêu cầu mà số ĐỔI!
[SẠCH] COO báo cáo giờ (tách): 50
thay đổi của CFO không còn rò rỉ sang báo cáo của COO.
```

Đây là trùng lặp tình cờ: CFO yêu cầu đổi cách tính lương (cap 40→45), lập trình viên sửa `regularHours()` — và **báo cáo giờ của COO đổi theo** dù COO chẳng yêu cầu gì. Một hàm phục vụ hai actor là một quả bom hẹn giờ. Lời giải SRP: tách code theo actor, chỉ **dùng chung dữ liệu** (`EmployeeData`), còn logic mỗi actor để riêng.

> [!note] Tự thử
> 1. Thêm actor thứ ba `save()` (CTO) vào bản bẩn, dùng chung `regularHours`. Giờ ba actor dính một hàm — rủi ro nhân lên thế nào?
> 2. Ở bản tách, đổi `cap` của `payCalculator` thành 45. `hourReporter` có đổi output không? Vì sao đó là SRP?
> 3. Tại sao "gộp hai actor dùng chung một hàm" trông *giống* DRY ([`clean-code` Bài 2](../../clean-code/bai_hoc/bai_02_ham.md)) nhưng thực ra là bẫy? (Gợi ý: trùng lặp *thật* vs trùng lặp *tình cờ*.)

## 4. OCP: mở cho mở rộng, đóng với sửa đổi

> [!quote] Ch. 8 — OCP (tr. 69)
> "A software artifact should be open for extension but closed for modification."
>
> *Một tạo tác phần mềm nên **mở** cho mở rộng nhưng **đóng** với sửa đổi.*

Bertrand Meyer đặt tên nguyên tắc này năm 1988. Ý tưởng: thêm *hành vi mới* nên làm bằng cách *thêm code mới*, không phải *sửa code cũ*. Ví dụ của sách: một hệ thống hiển thị tóm tắt tài chính. Khi yêu cầu mới tới — cũng dữ liệu đó nhưng in ra giấy đen trắng (số âm trong ngoặc) thay vì web — một thiết kế tốt phải khiến lượng code *phải sửa* là **tối thiểu**, lý tưởng là 0. Cách đạt: tách thành các component và sắp **chiều phụ thuộc** cho đúng.

## 5. OCP ở tầm component: chiều phụ thuộc để bảo vệ

Đây là chỗ OCP ở *Clean Architecture* vượt lên mức class. Quy tắc gói trong một câu:

> [!quote] Ch. 8 — OCP (tr. 73)
> "If component A should be protected from changes in component B, then component B should depend on component A."
>
> *Nếu component A cần được **bảo vệ** khỏi thay đổi trong component B, thì B phải **phụ thuộc vào** A.*

Mũi tên phụ thuộc trỏ *về phía* cái ta muốn bảo vệ. Business rules (Interactor) chứa chính sách *cao nhất* nên phải được bảo vệ khỏi mọi thứ — vì vậy mọi thứ (Controller, Presenter, View, Database) phụ thuộc *vào* nó, không ngược lại:

```
          cần được BẢO VỆ nhất
                  │
   View ──► Presenter ──► Controller ──► Interactor ◄── Database
   (dễ đổi)                         (business rules, cao nhất)
            mũi tên phụ thuộc đều TRỎ VỀ Interactor
```

Đây chính là đa hình/đảo-phụ-thuộc của [Bài 1](bai_01_he_hinh_lap_trinh.md) dùng ở tầm kiến trúc, và là bộ xương của vòng tròn Clean Architecture ([Bài 7](bai_07_clean_architecture.md)). OCP, nói cho cùng, là *lý do chính* ta bận tâm tới kiến trúc component.

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> SRP-theo-actor và OCP-theo-chiều-phụ-thuộc là hai ý **bền và sâu** nhất của SOLID năm 2026 — nhưng cũng là nơi dễ áp dụng máy móc.
> - **SRP-theo-actor giải oan cho SRP.** Định nghĩa 2017 này rõ hơn hẳn "một lý do để thay đổi" mơ hồ. Năm 2026 nó cộng hưởng với **DDD bounded context** (mỗi context phục vụ một nhóm nghiệp vụ) và là lập luận nền cho **vertical slice** / **modular monolith**: nhóm code theo *actor/tính năng*, không theo *tầng kỹ thuật*.
> - **Coi chừng chia SRP quá vụn.** Giống [`clean-code` Bài 9](../../clean-code/bai_hoc/bai_09_class.md), tách mỗi method một lớp vì "SRP" là hiểu sai — SRP nói về *actor*, không về *số method*. Nếu hai hàm cùng đổi vì cùng một actor, để chung.
> - **OCP vs YAGNI (ponytail).** "Đóng với sửa đổi" dễ bị đẩy thành "tạo sẵn interface/abstraction cho mọi thứ phòng khi cần". Uncle Bob nói đúng ở Ch.8: chỉ cần *tối thiểu hoá* code phải sửa, không phải *loại bỏ* nó. Đừng trừu tượng hoá trước khi có trục thay đổi thật (Rule of Three — xem [`clean-code` Bài 11](../../clean-code/bai_hoc/bai_11_thiet_ke_noi_len.md)).
> - **Phê bình chung về SOLID (2026):** phe functional/data-oriented (Casey Muratori) cho rằng SOLID cổ vũ quá nhiều lớp nhỏ + gián tiếp, hại hiệu năng và tính dễ đọc. Cân bằng: SOLID là *heuristic về chiều phụ thuộc*, không phải luật bắt-buộc-mọi-chỗ.

## 7. Áp dụng vào dự án của bạn

> [!question] Áp dụng vào dự án của bạn
> 1. **Vẽ actor cho một lớp.** Chọn một lớp "to" trong dự án. Mỗi method phục vụ *actor* nào (nhóm người/nghiệp vụ nào yêu cầu nó đổi)? Nhiều actor → ứng viên tách theo SRP.
> 2. **Săn "trùng lặp tình cờ".** Có hàm phụ nào được hai tính năng *khác nghiệp vụ* dùng chung không? Đổi nó cho bên này có thể âm thầm phá bên kia — như demo CFO/COO.
> 3. **Kiểm chiều mũi tên OCP.** Business logic cốt lõi của bạn có `import` thẳng DB/UI/framework không? Nếu có, cái cần-được-bảo-vệ-nhất lại đang phụ thuộc vào cái dễ đổi nhất — ngược OCP.

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| :--- | :--- |
| **SRP** | Module chịu trách nhiệm trước một, và chỉ một, **actor** (tr. 61). |
| **Actor** | Nhóm người/stakeholder cùng yêu cầu một thay đổi (tr. 61). |
| **Accidental duplication** | Hai actor dùng chung một hàm → đổi cho bên này phá bên kia (tr. 62–64). |
| **Cohesion** | Lực gắn kết code cùng phục vụ một actor (tr. 62). |
| **OCP** | Mở cho mở rộng, đóng với sửa đổi (tr. 69). |
| **Protect direction** | Nếu A cần bảo vệ khỏi B, thì B phụ thuộc A (tr. 73). |

## 9. Câu hỏi tự kiểm tra

1. Vì sao SRP *không* phải "mỗi module làm một việc"? "Làm một việc" là nguyên tắc ở mức nào? *(tr. 61)*
2. "Actor" là gì? Lớp `Employee` phục vụ mấy actor, là những ai? *(tr. 61–62)*
3. Trong demo, đổi chính sách của CFO đã phá cái gì của COO, và vì sao? *(mục 3)*
4. Phát biểu OCP. Ví dụ "tóm tắt tài chính web → giấy in" minh hoạ điều gì? *(tr. 69)*
5. Câu "nếu A cần bảo vệ khỏi B thì B phụ thuộc A" quyết định chiều mũi tên thế nào? *(tr. 73)*

## Tóm tắt một trang

```
BÀI 2 — SOLID (1): SRP & OCP Ở TẦM KIẾN TRÚC
─────────────────────────────────────────────────────────
SOLID = S.R.P · O.C.P · L.S.P · I.S.P · D.I.P (năm nguyên tắc)
   Ở ĐÂY nhìn mức ACTOR/COMPONENT, không mức class (≠ clean-code B9).

SRP   KHÔNG phải "làm một việc" (đó là mức HÀM, tr.61).
   = "trách nhiệm trước MỘT ACTOR" (tr.61).
   Employee: calculatePay→CFO · reportHours→COO · save→CTO.
   Triệu chứng vi phạm: TRÙNG LẶP TÌNH CỜ.
   DEMO: đổi cap của CFO (40→45) → báo cáo COO đổi theo (bug!).
   Fix: tách theo actor, chỉ dùng chung DỮ LIỆU.

OCP   "mở cho mở rộng, đóng với sửa đổi" (Meyer 1988, tr.69).
   Tầm component: "nếu A cần bảo vệ khỏi B thì B phụ thuộc A" (tr.73).
   Mũi tên trỏ VỀ cái cần bảo vệ nhất = business rules.

2026  SRP-actor ↔ DDD bounded context, vertical slice, modular
   monolith. Đừng chia vụn (SRP về actor, không về số method).
   OCP vs YAGNI: tối thiểu code-phải-sửa, đừng trừu tượng hoá sớm.
```

## Nguồn

- **Robert C. Martin**, *Clean Architecture* (Prentice Hall, 2017) — **Ch.7 "SRP"** (`tr. 61–68`): SRP bị hiểu nhầm, "function do one thing" ≠ SRP, "responsible to one actor", module=source file, cohesion (tr. 61–62); triệu chứng 1 trùng lặp tình cờ, Employee/CFO/COO/CTO (tr. 62–64); các triệu chứng khác, giải pháp tách (tr. 64–68). **Ch.8 "OCP"** (`tr. 69–76`): định nghĩa Meyer 1988 (tr. 69); ví dụ tóm tắt tài chính (tr. 70–72); chiều phụ thuộc bảo vệ, "if A protected from B then B depends on A", Interactor (tr. 73); kết luận (tr. 74–76). `tai_lieu/Clean.Architecture.2017.9.pdf`
- Bối cảnh 2026 dẫn từ ngoài sách: DDD bounded context; vertical slice / modular monolith; phê bình SOLID (Casey Muratori); Rule of Three.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 27`.

---

**Bản đồ khoá học:** [Bài 0 — Hai giá trị](bai_00_hai_gia_tri.md) · [Bài 1 — Ba hệ hình lập trình](bai_01_he_hinh_lap_trinh.md) · [Bài 2 ← bạn đang ở đây] · [Bài 3 — SOLID (2): LSP, ISP, DIP](bai_03_solid_lsp_isp_dip.md) · [Bài 4 — Nguyên tắc Component](bai_04_nguyen_tac_component.md) · [Bài 5 — Kiến trúc là gì & Độc lập](bai_05_kien_truc_va_doc_lap.md) · [Bài 6 — Ranh giới & Dependency Rule](bai_06_ranh_gioi_dependency_rule.md) · [Bài 7 — Business Rules & The Clean Architecture](bai_07_clean_architecture.md) · [Bài 8 — Humble Object, Main, Services](bai_08_humble_main_services.md) · [Bài 9 — Chi tiết: DB, Web, Framework](bai_09_chi_tiet.md) · [Bài 10 — The Missing Chapter: đóng gói](bai_10_dong_goi.md) · [Bài 11 — Case study & tổng kết](bai_11_case_study.md)

Xem thêm [README khoá học](../README.md).
