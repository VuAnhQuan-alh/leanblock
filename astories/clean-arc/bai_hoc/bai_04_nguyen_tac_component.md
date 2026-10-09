# Bài 4 — Nguyên tắc Component: cohesion và coupling

> [!info] Về bài này
> Dựng từ **Phần IV — Component Principles**: **Ch.12 Components**, **Ch.13 Component Cohesion**, **Ch.14 Component Coupling** của *Clean Architecture* (Robert C. Martin, 2017 — `tai_lieu/`, `tr. 95–132`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 27`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Nối [Bài 2–3 (SOLID)](bai_02_solid_srp_ocp.md): nếu SOLID sắp *lớp*, thì Phần IV sắp *component* (đơn vị triển khai).
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Component là gì](#1-component-là-gì)
2. [Ba nguyên tắc cohesion: REP, CCP, CRP](#2-ba-nguyên-tắc-cohesion-rep-ccp-crp)
3. [Tam giác căng: ba nguyên tắc cohesion cãi nhau](#3-tam-giác-căng-ba-nguyên-tắc-cohesion-cãi-nhau)
4. [Ba nguyên tắc coupling: ADP, SDP, SAP](#4-ba-nguyên-tắc-coupling-adp-sdp-sap)
5. [Code minh hoạ: đo Instability và dò chu trình](#5-code-minh-hoạ-đo-instability-và-dò-chu-trình)
6. [Main Sequence: cân giữa trừu tượng và ổn định](#6-main-sequence-cân-giữa-trừu-tượng-và-ổn-định)
7. [Đối chiếu 2026](#7-đối-chiếu-2026)
8. [Áp dụng vào dự án của bạn](#8-áp-dụng-vào-dự-án-của-bạn)
9. [Từ điển thuật ngữ](#9-từ-điển-thuật-ngữ)
10. [Câu hỏi tự kiểm tra](#10-câu-hỏi-tự-kiểm-tra)
11. [Tóm tắt một trang](#tóm-tắt-một-trang)
12. [Nguồn](#nguồn)

---

## 1. Component là gì

> [!quote] Ch. 12 — Components (tr. 95)
> "Components are the units of deployment. They are the smallest entities that can be deployed as part of a system."
>
> *Component là các **đơn vị triển khai** (deployment). Chúng là thực thể nhỏ nhất có thể được triển khai như một phần của hệ thống.*

Trong Java là `.jar`, trong .NET là DLL, trong Ruby là gem. Chúng có thể được nối (link) tĩnh hay nạp động như plugin. Phần IV trả lời hai câu: *class nào gộp vào cùng một component* (cohesion — Ch.13) và *các component phụ thuộc nhau ra sao* (coupling — Ch.14).

## 2. Ba nguyên tắc cohesion: REP, CCP, CRP

| Viết tắt | Tên đầy đủ | Nói gì | Liên hệ |
| :---: | :--- | :--- | :--- |
| **REP** | Reuse/Release Equivalence Principle | đơn vị tái dùng = đơn vị phát hành; component phải có **số phiên bản** | nền của quản lý release |
| **CCP** | Common Closure Principle | gộp vào một component các class **đổi cùng lúc, cùng lý do** | = **SRP** cho component |
| **CRP** | Common Reuse Principle | đừng gộp các class *không* dùng chung; **đừng bắt người khác phụ thuộc thứ họ không cần** | = **ISP** cho component |

**REP**: người ta không tái dùng được một component nếu nó không được theo dõi qua quy trình phát hành và gán số phiên bản — vì cần biết khi nào có bản mới và nó đổi gì.

**CCP** chính là SRP ở tầm component: gộp những class *đổi vì cùng một lý do, cùng một lúc*; tách những class đổi vì lý do khác nhau. Đây là "closure" theo nghĩa OCP ([Bài 2](bai_02_solid_srp_ocp.md)).

**CRP** là ISP ở tầm component, và rút gọn được thành một câu:

> [!quote] Ch. 13 — Common Reuse Principle (tr. 107)
> "Don't depend on things you don't need."
>
> *Đừng phụ thuộc vào những thứ bạn không cần.*

## 3. Tam giác căng: ba nguyên tắc cohesion cãi nhau

Điều tinh tế: ba nguyên tắc **kéo ngược nhau**.

> [!quote] Ch. 13 — The Tension Diagram (tr. 108)
> "The REP and CCP are inclusive principles […] The CRP is an exclusive principle, driving components to be smaller."
>
> *REP và CCP là nguyên tắc **bao hàm** (cả hai đẩy component to ra). CRP là nguyên tắc **loại trừ**, đẩy component **nhỏ lại**.*

```
                         REP
                   (dễ tái dùng/release)
                        /    \
          bỏ REP →     /      \    ← bỏ CRP
      "quá nhiều bản  /        \  "quá nhiều component
       release"      /          \  bị ảnh hưởng khi đổi"
                    /            \
                 CCP ──────────── CRP
          (gộp cái đổi cùng)   (tách cái không dùng chung)
                   ↑ bỏ CCP: "quá nhiều component đổi theo một thay đổi"
```

Mỗi cạnh tam giác là *cái giá phải trả khi bỏ nguyên tắc ở đỉnh đối diện*. Kiến trúc sư giỏi không chọn một đỉnh cố định — họ **di chuyển trong tam giác** theo giai đoạn dự án: dự án non trẻ nghiêng về CCP (dễ đổi), dự án trưởng thành nghiêng về REP/CRP (dễ tái dùng).

## 4. Ba nguyên tắc coupling: ADP, SDP, SAP

| Viết tắt | Tên đầy đủ | Nói gì |
| :---: | :--- | :--- |
| **ADP** | Acyclic Dependencies Principle | **không chu trình** trong đồ thị phụ thuộc component |
| **SDP** | Stable Dependencies Principle | phụ thuộc **theo chiều ổn định** |
| **SAP** | Stable Abstractions Principle | component càng ổn định càng phải **trừu tượng** |

**ADP** — luật chống "hội chứng sáng thứ Hai" (code người khác phá build của bạn qua đêm):

> [!quote] Ch. 14 — The Acyclic Dependencies Principle (tr. 111)
> "Allow no cycles in the component dependency graph."
>
> *Không cho phép **chu trình** nào trong đồ thị phụ thuộc component.*

Đồ thị phải là **DAG** (directed acyclic graph). Có chu trình (A→B→C→A) thì ba component dính thành một khối, không build/test/deploy độc lập được. Gỡ chu trình bằng DIP (chèn interface) hoặc tạo component mới.

**SDP** — đo độ bất ổn bằng chỉ số **I** (Instability):

> [!quote] Ch. 14 — The Stable Dependencies Principle (tr. 119)
> "Depend in the direction of stability."
>
> *Hãy phụ thuộc **theo chiều ổn định**.*

`I = Fan-out / (Fan-in + Fan-out)`. `I = 0` là ổn định tối đa (nhiều kẻ phụ thuộc vào nó, nó không phụ thuộc ai — khó đổi); `I = 1` là bất ổn tối đa. SDP đòi: I của một component phải **lớn hơn** I của các component mà nó phụ thuộc — tức mũi tên luôn trỏ *về phía ổn định hơn*.

## 5. Code minh hoạ: đo Instability và dò chu trình

Hai chỉ số trừu tượng trên hoàn toàn *tính được*. Demo dưới tính `I` cho từng component và dò chu trình (ADP):

```typescript
import { strict as assert } from "node:assert";

// đồ thị phụ thuộc component: "A -> B" nghĩa là A phụ thuộc B
type Graph = Record<string, string[]>;

// I = Fan-out / (Fan-in + Fan-out): 0 = ổn định tối đa, 1 = bất ổn tối đa
function instability(g: Graph): Record<string, number> {
  const comps = Object.keys(g);
  const fanOut: Record<string, number> = {};
  const fanIn: Record<string, number> = {};
  for (const c of comps) { fanOut[c] = 0; fanIn[c] = 0; }
  for (const c of comps) for (const dep of g[c]) {
    fanOut[c] += 1;
    fanIn[dep] = (fanIn[dep] ?? 0) + 1;
  }
  const I: Record<string, number> = {};
  for (const c of comps) {
    const total = fanOut[c] + fanIn[c];
    I[c] = total === 0 ? 0 : fanOut[c] / total;
  }
  return I;
}

function hasCycle(g: Graph): boolean {
  const color: Record<string, number> = {}; // 0=trắng 1=xám 2=đen
  for (const c of Object.keys(g)) color[c] = 0;
  let found = false;
  function dfs(u: string): void {
    color[u] = 1;
    for (const v of g[u] ?? []) {
      if (color[v] === 1) found = true;
      else if (color[v] === 0) dfs(v);
    }
    color[u] = 2;
  }
  for (const c of Object.keys(g)) if (color[c] === 0) dfs(c);
  return found;
}

// hệ TỐT: không chu trình; phụ thuộc trỏ về phía ỔN ĐỊNH (I giảm dần)
const good: Graph = {
  UI: ["Interactor"],
  Controller: ["Interactor"],
  Interactor: [], // ổn định nhất: không phụ thuộc ai
};
const I = instability(good);
console.log("I(UI)         =", I.UI.toFixed(2));
console.log("I(Controller) =", I.Controller.toFixed(2));
console.log("I(Interactor) =", I.Interactor.toFixed(2));
console.log("hệ tốt có chu trình?", hasCycle(good));
assert.equal(I.Interactor, 0); // ổn định
assert.equal(I.UI, 1); // bất ổn
assert.equal(hasCycle(good), false);

// hệ XẤU: A->B->C->A, có chu trình (vi phạm ADP)
const bad: Graph = { A: ["B"], B: ["C"], C: ["A"] };
console.log("hệ xấu có chu trình?", hasCycle(bad), "← vi phạm ADP");
assert.equal(hasCycle(bad), true);
console.log("SDP: UI(I=1) phụ thuộc Interactor(I=0) — trỏ VỀ phía ổn định.");
```

Kết quả chạy thật:

```
I(UI)         = 1.00
I(Controller) = 1.00
I(Interactor) = 0.00
hệ tốt có chu trình? false
hệ xấu có chu trình? true ← vi phạm ADP
SDP: UI(I=1) phụ thuộc Interactor(I=0) — trỏ VỀ phía ổn định.
```

`Interactor` (business rules) có `I = 0` — ổn định nhất, ai cũng phụ thuộc vào nó, nó không phụ thuộc ai. `UI`/`Controller` có `I = 1` — dễ đổi, nằm ở rìa. Mũi tên phụ thuộc trỏ từ bất-ổn *về* ổn định: đúng SDP. Và hệ không có chu trình: đúng ADP. Chính là bộ xương của vòng tròn Clean Architecture ([Bài 7](bai_07_clean_architecture.md)).

> [!note] Tự thử
> 1. Thêm `Interactor: ["UI"]` vào hệ tốt. `hasCycle` báo gì? Bạn vừa tạo chu trình UI↔Interactor.
> 2. Thêm một component `Database: ["Interactor"]`. I của `Interactor` đổi thế nào (fan-in tăng)?
> 3. Nếu `Interactor` (ổn định) buộc phải đổi khi `UI` đổi, SDP bị vi phạm. Làm sao đảo mũi tên đó bằng DIP? (Gợi ý: interface do Interactor sở hữu.)

## 6. Main Sequence: cân giữa trừu tượng và ổn định

SAP buộc *ổn định* phải đi đôi với *trừu tượng*:

> [!quote] Ch. 14 — The Stable Abstractions Principle (tr. 125)
> "A component should be as abstract as it is stable."
>
> *Một component nên **trừu tượng** đúng bằng mức nó **ổn định**.*

Vì component ổn định (khó đổi) mà lại *cụ thể* (concrete) thì hoá ra cứng nhắc — khó đổi mà vẫn hay phải đổi. Ngược lại, component bất ổn thì nên cụ thể (dễ viết, dễ bỏ). Đo độ trừu tượng bằng `A = Na / Nc` (số lớp trừu tượng / tổng số lớp). Vẽ A theo I lên đồ thị, đường chéo lý tưởng A + I = 1 gọi là **Main Sequence**. Hai góc chết:

| Vùng | Vị trí (I, A) | Vì sao chết |
| :--- | :--- | :--- |
| **Zone of Pain** | I≈0, A≈0 (ổn định + cụ thể) | cứng nhắc: khó đổi mà vẫn phải đổi (vd schema DB) |
| **Zone of Uselessness** | I≈1, A≈1 (bất ổn + trừu tượng) | trừu tượng mà không ai dùng — code chết |

Component tốt nằm *gần Main Sequence* — xa cả hai vùng chết.

## 7. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Phần Component là phần **ít được nhắc nhất** nhưng vẫn ngầm định hình thực hành 2026:
> - **ADP = công cụ tự động 2026.** "Không chu trình" giờ do máy canh: ESLint `import/no-cycle`, `madge --circular`, Nx/Turborepo module boundaries, `dependency-cruiser`. Chu trình bị chặn ngay trong CI, không chờ "sáng thứ Hai".
> - **REP/CCP/CRP ↔ monorepo & package.** Thời của npm/Nx/Cargo workspace, "component = đơn vị phát hành có số phiên bản" là chuyện hằng ngày. Tam giác căng REP↔CCP↔CRP chính là tranh luận **monolith vs nhiều package nhỏ** / **modular monolith vs microservices**: gộp to (CCP, dễ đổi) hay tách nhỏ (CRP, dễ tái dùng độc lập).
> - **Chỉ số I/A/Main Sequence — ít ai đo bằng tay 2026**, nhưng ý tưởng sống trong các công cụ "architecture fitness function" (ArchUnit, dependency-cruiser rules) và linter boundary. Đừng thờ con số; dùng nó như *trực giác về chiều phụ thuộc*.
> - **Zone of Pain vẫn thật và đau (ponytail):** schema database và các "stable concrete" khác đúng là khó đổi mà hay phải đổi — đó là lý do [Bài 9 "Database là chi tiết"](bai_09_chi_tiet.md) đẩy nó ra rìa. Nhưng đừng trừu tượng hoá *mọi* thứ để "thoát Zone of Pain" — nhiều thứ cụ-thể-ổn-định (một enum cấu hình) chẳng đau gì.

## 8. Áp dụng vào dự án của bạn

> [!question] Áp dụng vào dự án của bạn
> 1. **Dò chu trình.** Chạy `madge --circular` (hoặc `dependency-cruiser`) trên dự án. Có chu trình import nào không? Mỗi cái là một vi phạm ADP cần gỡ.
> 2. **Định vị tam giác cohesion.** Dự án bạn đang nghiêng đỉnh nào — gộp to dễ đổi (CCP), hay tách nhỏ dễ tái dùng (CRP)? Có hợp giai đoạn hiện tại không?
> 3. **Tìm Zone of Pain.** Có module nào vừa *khó đổi* (nhiều thứ phụ thuộc) vừa *hay phải đổi* không? Đó là điểm đau — cân nhắc chèn abstraction để đảo phụ thuộc.

## 9. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| :--- | :--- |
| **Component** | Đơn vị triển khai nhỏ nhất (jar/DLL/gem) (tr. 95). |
| **REP** | Đơn vị tái dùng = đơn vị phát hành; cần số phiên bản (tr. 104). |
| **CCP** | Gộp class đổi cùng lúc/cùng lý do; = SRP cho component (tr. 105). |
| **CRP** | Đừng phụ thuộc thứ không cần; = ISP cho component (tr. 107). |
| **ADP** | Không chu trình trong đồ thị phụ thuộc (tr. 111). |
| **SDP** | Phụ thuộc theo chiều ổn định; I = Fan-out/(Fan-in+Fan-out) (tr. 119). |
| **SAP** | Trừu tượng đúng bằng mức ổn định (tr. 125). |
| **Main Sequence / Zone of Pain** | Đường A+I=1 lý tưởng; góc ổn-định-cụ-thể là vùng đau (tr. 125–126). |

## 10. Câu hỏi tự kiểm tra

1. Component là gì? Cho ba ví dụ theo ngôn ngữ. *(tr. 95)*
2. REP, CCP, CRP mỗi cái nói gì? CCP và CRP tương ứng nguyên tắc SOLID nào? *(tr. 104–107)*
3. Vì sao ba nguyên tắc cohesion "kéo ngược nhau"? Kiến trúc sư xử lý ra sao? *(tr. 108)*
4. Chỉ số I tính thế nào? SDP đòi mũi tên phụ thuộc trỏ theo chiều nào? *(tr. 119)*
5. Zone of Pain và Zone of Uselessness là gì? Vì sao chúng "chết"? *(tr. 125–126)*

## Tóm tắt một trang

```
BÀI 4 — NGUYÊN TẮC COMPONENT: COHESION & COUPLING
─────────────────────────────────────────────────────────
COMPONENT = đơn vị triển khai (jar/DLL/gem) (tr.95).

COHESION (class nào gộp chung — Ch.13)
   REP: đơn vị tái dùng = đơn vị phát hành (có version)
   CCP: gộp cái đổi cùng lúc/lý do  = SRP cho component
   CRP: "đừng phụ thuộc thứ không cần" (tr.107) = ISP cho component
   TAM GIÁC CĂNG: REP+CCP đẩy TO, CRP đẩy NHỎ (tr.108). Di chuyển
   theo giai đoạn dự án.

COUPLING (component phụ thuộc nhau — Ch.14)
   ADP: "không chu trình" (tr.111) → đồ thị là DAG.
   SDP: "phụ thuộc theo chiều ổn định" (tr.119). I=Fanout/(Fanin+Fanout).
        Interactor I=0 (ổn định), UI I=1 (bất ổn). Mũi tên trỏ VỀ ổn định.
   SAP: "trừu tượng đúng bằng mức ổn định" (tr.125). A=Na/Nc.
        Main Sequence A+I=1. Zone of Pain (ổn định+cụ thể) = đau.

2026  ADP tự động (madge/dependency-cruiser/Nx). REP/CCP/CRP ↔
   monorepo & modular monolith vs microservices. I/A sống trong
   fitness function. Đừng thờ con số; dùng như trực giác.
```

## Nguồn

- **Robert C. Martin**, *Clean Architecture* (Prentice Hall, 2017) — **Ch.12 "Components"** (`tr. 95–102`): "units of deployment", lịch sử linking (tr. 95–102). **Ch.13 "Component Cohesion"** (`tr. 103–110`): REP (tr. 103–104); CCP = SRP cho component (tr. 105–106); CRP = ISP cho component, "don't depend on things you don't need" (tr. 106–107); tam giác căng (tr. 108–109). **Ch.14 "Component Coupling"** (`tr. 111–132`): ADP "allow no cycles", weekly build / morning-after syndrome (tr. 111–118); SDP "depend in the direction of stability", chỉ số I (tr. 119–124); SAP "as abstract as it is stable", chỉ số A, Main Sequence, Zone of Pain/Uselessness (tr. 125–132). `tai_lieu/Clean.Architecture.2017.9.pdf`
- Bối cảnh 2026 dẫn từ ngoài sách: `madge`/`dependency-cruiser`/ESLint `import/no-cycle`, Nx/Turborepo boundaries, ArchUnit; monorepo; modular monolith vs microservices.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 27`.

---

**Bản đồ khoá học:** [Bài 0 — Hai giá trị](bai_00_hai_gia_tri.md) · [Bài 1 — Ba hệ hình lập trình](bai_01_he_hinh_lap_trinh.md) · [Bài 2 — SOLID (1): SRP, OCP](bai_02_solid_srp_ocp.md) · [Bài 3 — SOLID (2): LSP, ISP, DIP](bai_03_solid_lsp_isp_dip.md) · [Bài 4 ← bạn đang ở đây] · [Bài 5 — Kiến trúc là gì & Độc lập](bai_05_kien_truc_va_doc_lap.md) · [Bài 6 — Ranh giới & Dependency Rule](bai_06_ranh_gioi_dependency_rule.md) · [Bài 7 — Business Rules & The Clean Architecture](bai_07_clean_architecture.md) · [Bài 8 — Humble Object, Main, Services](bai_08_humble_main_services.md) · [Bài 9 — Chi tiết: DB, Web, Framework](bai_09_chi_tiet.md) · [Bài 10 — The Missing Chapter: đóng gói](bai_10_dong_goi.md) · [Bài 11 — Case study & tổng kết](bai_11_case_study.md)

Xem thêm [README khoá học](../README.md).
