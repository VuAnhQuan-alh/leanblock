# Bài 6 — Ranh giới & Dependency Rule: vẽ lằn ranh, hướng mũi tên

> [!info] Về bài này
> Dựng từ **Phần V — Architecture**: **Ch.17 "Boundaries: Drawing Lines"**, **Ch.18 "Boundary Anatomy"**, **Ch.19 "Policy and Level"** của *Clean Architecture* (Robert C. Martin, 2017 — `tai_lieu/`, `tr. 159–188`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 27`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Đây là trái tim cơ chế của Phần V, dẫn thẳng vào vòng tròn Clean Architecture ([Bài 7](bai_07_clean_architecture.md)). Nối DIP ([Bài 3](bai_03_solid_lsp_isp_dip.md)) và đa hình ([Bài 1](bai_01_he_hinh_lap_trinh.md)).
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Kiến trúc là nghệ thuật vẽ lằn ranh](#1-kiến-trúc-là-nghệ-thuật-vẽ-lằn-ranh)
2. [Ranh giới tách cái cốt lõi khỏi cái phụ thuộc trì hoãn được](#2-ranh-giới-tách-cái-cốt-lõi-khỏi-cái-phụ-thuộc-trì-hoãn-được)
3. [Code minh hoạ: mũi tên trỏ vào, ngược luồng điều khiển](#3-code-minh-hoạ-mũi-tên-trỏ-vào-ngược-luồng-điều-khiển)
4. [Giải phẫu ranh giới: các kiểu lằn ranh](#4-giải-phẫu-ranh-giới-các-kiểu-lằn-ranh)
5. [Policy và Level: level = khoảng cách tới input/output](#5-policy-và-level-level--khoảng-cách-tới-inputoutput)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào dự án của bạn](#7-áp-dụng-vào-dự-án-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Kiến trúc là nghệ thuật vẽ lằn ranh

> [!quote] Ch. 17 — Boundaries: Drawing Lines (tr. 159)
> "Software architecture is the art of drawing lines that I call boundaries."
>
> *Kiến trúc phần mềm là **nghệ thuật vẽ những lằn ranh** mà tôi gọi là ranh giới (boundary).*

Những lằn ranh ấy tách các phần tử phần mềm ra, và *hạn chế phần bên này biết về phần bên kia*. Mục đích cốt yếu, lặp lại từ [Bài 5](bai_05_kien_truc_va_doc_lap.md): tách cái **nghiệp vụ cốt lõi** khỏi cái **không cốt lõi** (GUI, database) — để hoãn và cô lập quyết định về cái sau.

## 2. Ranh giới tách cái cốt lõi khỏi cái phụ thuộc trì hoãn được

Hai quyết định "dùng database nào" và "dùng GUI nào" đều là *ancillary* (phụ) và **trì hoãn được**. Khi tách chúng sau một ranh giới, ta có một **kiến trúc plugin**:

> [!quote] Ch. 17 — Plugin Architecture (tr. 170)
> "The core business rules are kept separate from, and independent of, those components that are either optional or that can be implemented in many different forms."
>
> *Các **business rule cốt lõi** được giữ tách biệt và **độc lập** với những component tuỳ chọn, hoặc có thể hiện thực theo nhiều dạng khác nhau.*

Ví dụ tuyệt vời của sách: ReSharper (JetBrains, Nga) là plugin của Visual Studio (Microsoft, Mỹ). Mã nguồn ReSharper *phụ thuộc* mã nguồn Visual Studio, không ngược lại. Vậy VS **miễn nhiễm** với ReSharper, còn ReSharper thì *dễ tổn thương* trước thay đổi của VS. Cấu trúc phụ thuộc quyết định *ai làm hại được ai*. Đó chính là ý nghĩa thực tiễn của việc chọn chiều mũi tên: ta muốn business rules nằm ở vị trí **miễn nhiễm** như Visual Studio.

## 3. Code minh hoạ: mũi tên trỏ vào, ngược luồng điều khiển

Điều tinh tế nhất: tại một ranh giới, **luồng điều khiển** (lúc chạy) và **phụ thuộc mã nguồn** có thể đi *ngược* chiều nhau. Vòng trong (business rule) *sở hữu* một interface (output port); plugin vòng ngoài *hiện thực* nó:

```
   luồng điều khiển lúc chạy ───────────────────────────►
┌────────────────┐     ┌────────────────────┐     ┌───────────────┐
│ processPayment │ ──► │ PaymentNotifier    │ ◄── │ EmailNotifier │
│ (vòng trong,   │     │ (interface, do     │     │ (plugin,      │
│ business rule) │     │ vòng trong sở hữu) │     │ vòng ngoài)   │
└────────────────┘     └────────────────────┘     └───────────────┘
   phụ thuộc mã nguồn ◄───────────────────  (trỏ VÀO vòng trong)
```

```typescript
import { strict as assert } from "node:assert";

// ===== VÒNG TRONG (business rules): SỞ HỮU interface output (ranh giới) =====
interface PaymentNotifier {
  notify(amount: number): string;
}
function processPayment(amount: number, notifier: PaymentNotifier): string {
  if (amount <= 0) throw new Error("Số tiền phải dương"); // business rule
  return notifier.notify(amount); // luồng điều khiển đi RA; phụ thuộc mã nguồn trỏ VÀO
}

// ===== VÒNG NGOÀI (chi tiết/plugin): HIỆN THỰC interface của vòng trong =====
class EmailNotifier implements PaymentNotifier {
  notify(amount: number): string { return `[email] đã thu ${amount}đ`; }
}
class SmsNotifier implements PaymentNotifier {
  notify(amount: number): string { return `[sms] +${amount}d`; }
}

console.log(processPayment(1000, new EmailNotifier()));
console.log(processPayment(1000, new SmsNotifier()));
assert.equal(processPayment(1000, new EmailNotifier()), "[email] đã thu 1000đ");

let threw = false;
try { processPayment(-5, new SmsNotifier()); } catch { threw = true; }
assert.equal(threw, true);
console.log("business rule chặn số âm — và không đổi khi thêm/đổi notifier (plugin).");
```

Kết quả chạy thật:

```
[email] đã thu 1000đ
[sms] +1000d
business rule chặn số âm — và không đổi khi thêm/đổi notifier (plugin).
```

Lúc chạy, `processPayment` *gọi ra* `notifier.notify()` (điều khiển đi ra ngoài). Nhưng về **mã nguồn**, `EmailNotifier`/`SmsNotifier` mới là bên *phụ thuộc vào* `PaymentNotifier` — interface do vòng trong sở hữu. Mũi tên phụ thuộc **trỏ vào trong**, ngược luồng điều khiển. Nhờ vậy business rule (chặn số âm) *miễn nhiễm* với mọi thay đổi của plugin thông báo — đúng vị trí "Visual Studio". Đây chính là DIP ([Bài 3](bai_03_solid_lsp_isp_dip.md)) dùng để vẽ một lằn ranh, và là viên gạch của **Dependency Rule** ([Bài 7](bai_07_clean_architecture.md)).

> [!note] Tự thử
> 1. Thêm `PushNotifier`. `processPayment` có đổi dòng nào không? Mũi tên phụ thuộc của nó trỏ đi đâu?
> 2. Thử cho `processPayment` `import` thẳng `EmailNotifier` và `new` nó bên trong. Giờ mũi tên phụ thuộc trỏ chiều nào? Business rule còn "miễn nhiễm" không?
> 3. Ai "làm hại" được ai: nếu bạn đổi `EmailNotifier`, `processPayment` có phải build lại không? Nếu đổi `processPayment` thì sao? (Liên hệ ReSharper/VS.)

## 4. Giải phẫu ranh giới: các kiểu lằn ranh

Một ranh giới không nhất thiết là ranh giới *mạng*. Ch.18 liệt kê các *mức* vật lý của một lằn ranh (từ nhẹ tới nặng) — khớp với các *decoupling mode* ở [Bài 5](bai_05_kien_truc_va_doc_lap.md):

| Kiểu ranh giới | Vượt ranh giới bằng | Chi phí |
| :--- | :--- | :---: |
| **Trong một nguồn (monolith)** | gọi hàm thường, kỷ luật phụ thuộc | thấp nhất |
| **Component triển khai** | gọi qua jar/DLL/gem nạp động | thấp–vừa |
| **Luồng (threads)** | cùng tiến trình, khác luồng | vừa |
| **Tiến trình cục bộ** | socket/shared memory liên tiến trình | cao |
| **Dịch vụ (service)** | mạng (REST/gRPC), tuần tự hoá | cao nhất |

Điểm chung: **vượt ranh giới theo chiều ít tốn nhất, và luôn giữ chiều phụ thuộc mã nguồn trỏ về phía nghiệp vụ cốt lõi** — bất kể ranh giới nằm ở mức vật lý nào.

## 5. Policy và Level: level = khoảng cách tới input/output

> [!quote] Ch. 19 — Policy and Level (tr. 183)
> "Software systems are statements of policy."
>
> *Hệ thống phần mềm là những **phát biểu về chính sách** (policy).*

Một chương trình, ở cốt lõi, chỉ là mô tả chính sách biến *input* thành *output*. Chính sách lớn tách thành nhiều chính sách nhỏ. Và "level" có định nghĩa chặt:

> [!quote] Ch. 19 — Level (tr. 183)
> "A strict definition of 'level' is 'the distance from the inputs and outputs.' The farther a policy is from both the inputs and the outputs of the system, the higher its level."
>
> *Định nghĩa chặt của "level" là **"khoảng cách tới input và output"**. Một chính sách càng xa cả input lẫn output của hệ thống thì level của nó càng **cao**.*

Chính sách quản lý input/output là *thấp nhất*. Quy tắc vàng theo sau: **component mức thấp phải phụ thuộc component mức cao** (không ngược lại) — để business rules mức cao không bị cuốn theo mỗi khi thiết bị I/O mức thấp đổi. Đây là lý do `readChar`/`writeChar` (thấp) phụ thuộc chính sách dịch (cao), chứ không phải ngược lại.

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Cơ chế "vẽ lằn ranh + hướng mũi tên về cốt lõi" là phần **bất tử và hội tụ** nhất của sách — nhiều trường phái cùng tới đây.
> - **Hội tụ kiến trúc:** Ports & Adapters (Hexagonal, Cockburn 2005), Onion Architecture (Palermo 2008), và Clean Architecture (2017) **nói cùng một điều** bằng từ khác nhau: cô lập nghiệp vụ sau các *port*, để chi tiết là *adapter/plugin*. Năm 2026 chúng thường được gọi gộp là "kiến trúc port-and-adapter". Demo mục 3 chính là một *output port* + hai *adapter*.
> - **"Mũi tên trỏ vào trong" = quy tắc có thể kiểm tự động 2026.** `dependency-cruiser`, ESLint boundaries, ArchUnit, Nx tags cho phép *khai báo* "layer domain không được import layer infra" và CI chặn vi phạm. Lằn ranh của Uncle Bob giờ là một rule trong pipeline.
> - **Chi phí ranh giới service là thật (ponytail).** Bảng mục 4 nhắc: service level đắt nhất. Làn sóng microservices từng bỏ qua điều này; 2026 (modular monolith) thừa nhận: hãy vẽ ranh giới *logic* trước (source level), chỉ "cứng hoá" thành service khi có lý do vận hành thật. Đừng trả giá mạng cho một lằn ranh mà một interface là đủ.
> - **"Hệ thống là phát biểu chính sách" ↔ DDD.** Ý "level = khoảng cách tới I/O" cộng hưởng với DDD: domain model (chính sách cao nhất) ở trung tâm, application/infrastructure ở ngoài. Nối [Bài 7](bai_07_clean_architecture.md).
> - **Vẫn gây tranh cãi:** với CRUD đơn giản, vẽ nhiều lằn ranh + port/adapter là over-engineering — một controller gọi thẳng ORM có thể là *đủ*. Biết *khi nào* một lằn ranh đáng vẽ mới là nghề.

## 7. Áp dụng vào dự án của bạn

> [!question] Áp dụng vào dự án của bạn
> 1. **Tìm một mũi tên sai chiều.** Business logic của bạn có `import` thẳng DB/HTTP/UI framework không? Đó là mũi tên trỏ *từ* cốt lõi *ra* chi tiết — ngược Dependency Rule. Chèn một port (interface) để đảo nó.
> 2. **Ai làm hại được ai (ReSharper/VS).** Chọn hai module. Đổi module này có buộc build lại module kia không? Nếu cốt lõi phải build lại khi chi tiết đổi, cốt lõi đang ở vị trí *dễ tổn thương* — sai.
> 3. **Chọn mức ranh giới có ý thức.** Một lằn ranh trong dự án: nó đang ở mức nào (hàm / component / service)? Có đang trả *giá service* (mạng, tuần tự hoá) cho thứ mà *source level* là đủ không?

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| :--- | :--- |
| **Boundary (ranh giới)** | Lằn ranh tách phần tử, hạn chế bên này biết về bên kia (tr. 159). |
| **Plugin architecture** | Business rules độc lập; GUI/DB là plugin cắm vào (tr. 170). |
| **Boundary crossing** | Vượt ranh giới: luồng điều khiển và phụ thuộc mã nguồn có thể ngược chiều (mục 3). |
| **Output port** | Interface do vòng trong sở hữu; plugin ngoài hiện thực (mục 3). |
| **Boundary anatomy** | Mức vật lý của lằn ranh: monolith/component/thread/process/service (Ch.18). |
| **Policy** | Phát biểu biến input thành output; hệ thống = tập chính sách (tr. 183). |
| **Level** | Khoảng cách tới input/output; càng xa càng cao; thấp phụ thuộc cao (tr. 183). |

## 9. Câu hỏi tự kiểm tra

1. "Kiến trúc là nghệ thuật vẽ lằn ranh" — lằn ranh tách cái gì khỏi cái gì? *(tr. 159)*
2. Trong demo, luồng điều khiển và phụ thuộc mã nguồn đi ngược chiều ra sao? Business rule "miễn nhiễm" nhờ đâu? *(mục 3)*
3. Ví dụ ReSharper/Visual Studio dạy gì về chiều mũi tên và "ai hại được ai"? *(tr. 170)*
4. Kể các mức vật lý của một ranh giới, từ rẻ tới đắt. *(Ch.18, mục 4)*
5. Định nghĩa chặt của "level" là gì? Vì sao component thấp nên phụ thuộc component cao? *(tr. 183)*

## Tóm tắt một trang

```
BÀI 6 — RANH GIỚI & DEPENDENCY RULE: VẼ LẰN RANH, HƯỚNG MŨI TÊN
─────────────────────────────────────────────────────────
"Kiến trúc = nghệ thuật VẼ LẰN RANH" (tr.159). Tách nghiệp vụ
   cốt lõi khỏi GUI/DB (ancillary, trì hoãn được).

PLUGIN  business rules ĐỘC LẬP; GUI/DB là plugin cắm vào (tr.170).
   ReSharper phụ thuộc Visual Studio → VS MIỄN NHIỄM. Chiều mũi tên
   quyết định AI HẠI ĐƯỢC AI. Đặt business rule ở vị trí "VS".

VƯỢT RANH GIỚI  luồng điều khiển ĐI RA, phụ thuộc mã nguồn TRỎ VÀO
   (ngược nhau). processPayment sở hữu PaymentNotifier; Email/Sms
   HIỆN THỰC nó → business rule miễn nhiễm với plugin.

GIẢI PHẪU  mức ranh giới: monolith < component < thread < process
   < service (đắt nhất). Chọn mức rẻ nhất đủ dùng.

POLICY & LEVEL  "hệ thống = phát biểu chính sách" (tr.183).
   level = KHOẢNG CÁCH tới input/output (tr.183). Thấp phụ thuộc cao.

2026  hội tụ Ports&Adapters / Hexagonal / Onion / Clean = CÙNG MỘT Ý.
   "mũi tên trỏ vào" kiểm tự động (dependency-cruiser/ArchUnit/Nx).
   Giá service là thật → source-level trước (modular monolith).
```

## Nguồn

- **Robert C. Martin**, *Clean Architecture* (Prentice Hall, 2017) — **Ch.17 "Boundaries: Drawing Lines"** (`tr. 159–174`): "art of drawing lines", hoãn quyết định (tr. 159); GUI/DB là ancillary, boundary crossing (tr. 160–169); plugin architecture, core business rules độc lập (tr. 170); ReSharper/Visual Studio, "ai hại được ai" (tr. 170–174). **Ch.18 "Boundary Anatomy"** (`tr. 175–182`): các mức ranh giới — monolith, deployment component, thread, local process, service (tr. 175–182). **Ch.19 "Policy and Level"** (`tr. 183–188`): "systems are statements of policy", "level = distance from inputs/outputs", thấp phụ thuộc cao (tr. 183–188). `tai_lieu/Clean.Architecture.2017.9.pdf`
- Bối cảnh 2026 dẫn từ ngoài sách: Hexagonal/Ports & Adapters (Cockburn), Onion (Palermo); dependency-cruiser/ArchUnit/Nx tags; modular monolith; DDD.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 27`.

---

**Bản đồ khoá học:** [Bài 0 — Hai giá trị](bai_00_hai_gia_tri.md) · [Bài 1 — Ba hệ hình lập trình](bai_01_he_hinh_lap_trinh.md) · [Bài 2 — SOLID (1): SRP, OCP](bai_02_solid_srp_ocp.md) · [Bài 3 — SOLID (2): LSP, ISP, DIP](bai_03_solid_lsp_isp_dip.md) · [Bài 4 — Nguyên tắc Component](bai_04_nguyen_tac_component.md) · [Bài 5 — Kiến trúc là gì & Độc lập](bai_05_kien_truc_va_doc_lap.md) · [Bài 6 ← bạn đang ở đây] · [Bài 7 — Business Rules & The Clean Architecture](bai_07_clean_architecture.md) · [Bài 8 — Humble Object, Main, Services](bai_08_humble_main_services.md) · [Bài 9 — Chi tiết: DB, Web, Framework](bai_09_chi_tiet.md) · [Bài 10 — The Missing Chapter: đóng gói](bai_10_dong_goi.md) · [Bài 11 — Case study & tổng kết](bai_11_case_study.md)

Xem thêm [README khoá học](../README.md).
