# Bài 1 — Ba hệ hình lập trình: mỗi cái lấy đi một quyền năng

> [!info] Về bài này
> Dựng từ **Phần II — Programming Paradigms**: **Ch.3 Paradigm Overview**, **Ch.4 Structured Programming**, **Ch.5 Object-Oriented Programming**, **Ch.6 Functional Programming** của *Clean Architecture* (Robert C. Martin, 2017 — `tai_lieu/`, `tr. 21–56`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 27`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Mạch bài: *ba hệ hình → mỗi cái lấy đi gì → vì sao điều đó quan trọng với kiến trúc → demo TS (sức mạnh OO) → đối chiếu 2026 → áp dụng*.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: ba hệ hình, mỗi cái *lấy đi* một thứ](#1-mở-đầu-ba-hệ-hình-mỗi-cái-lấy-đi-một-thứ)
2. [Structured: kỷ luật trên luồng điều khiển trực tiếp](#2-structured-kỷ-luật-trên-luồng-điều-khiển-trực-tiếp)
3. [Object-Oriented: kỷ luật trên luồng điều khiển gián tiếp](#3-object-oriented-kỷ-luật-trên-luồng-điều-khiển-gián-tiếp)
4. [Code minh hoạ: sức mạnh kiến trúc của OO](#4-code-minh-hoạ-sức-mạnh-kiến-trúc-của-oo)
5. [Functional: kỷ luật trên phép gán](#5-functional-kỷ-luật-trên-phép-gán)
6. [Ba hệ hình khớp ba mối bận tâm kiến trúc](#6-ba-hệ-hình-khớp-ba-mối-bận-tâm-kiến-trúc)
7. [Đối chiếu 2026](#7-đối-chiếu-2026)
8. [Áp dụng vào dự án của bạn](#8-áp-dụng-vào-dự-án-của-bạn)
9. [Từ điển thuật ngữ](#9-từ-điển-thuật-ngữ)
10. [Câu hỏi tự kiểm tra](#10-câu-hỏi-tự-kiểm-tra)
11. [Tóm tắt một trang](#tóm-tắt-một-trang)
12. [Nguồn](#nguồn)

---

## 1. Mở đầu: ba hệ hình, mỗi cái *lấy đi* một thứ

Có đúng ba hệ hình lập trình, cả ba đều được phát minh trong khoảng **mười năm 1958–1968**, và từ đó tới nay không có hệ hình thứ tư nào. Điều Uncle Bob muốn ta thấy là một khuôn mẫu bất ngờ:

> [!quote] Ch. 3 — Food for Thought (tr. 22)
> "Each of the paradigms removes capabilities from the programmer. None of them adds new capabilities."
>
> *Mỗi hệ hình **lấy đi** một năng lực của lập trình viên. Không hệ hình nào **thêm** năng lực mới.*

Mỗi hệ hình áp một kỷ luật *mang tính phủ định* — nói cho ta biết điều **không** được làm. Ba hệ hình lấy đi lần lượt: `goto`, con trỏ hàm, và phép gán. Bảng tổng quan (từ Ch.3):

| Hệ hình | Lấy đi (áp kỷ luật lên) | Người phát minh | Năm |
| :--- | :--- | :--- | :---: |
| **Structured** | `goto` — luồng điều khiển **trực tiếp** | Edsger Dijkstra | 1968 |
| **Object-Oriented** | con trỏ hàm — luồng điều khiển **gián tiếp** | Dahl & Nygaard | 1966 |
| **Functional** | phép gán — **biến khả biến** (mutable) | Alonzo Church (λ-calculus) → LISP | 1936 / 1958 |

## 2. Structured: kỷ luật trên luồng điều khiển trực tiếp

> [!quote] Ch. 3 — Structured Programming (tr. 21)
> "Structured programming imposes discipline on direct transfer of control."
>
> *Lập trình cấu trúc áp kỷ luật lên việc **chuyển điều khiển trực tiếp**.*

Dijkstra chứng minh `goto` tự do có hại, thay nó bằng `if/then/else` và `do/while/until`. Điều này cho phép **phân rã chức năng** (functional decomposition): bẻ module lớn thành các đơn vị nhỏ chứng minh được. Nhưng Dijkstra cũng để lại một hệ quả sâu về bản chất phần mềm, qua một câu nổi tiếng:

> [!quote] Ch. 4 — Tests (tr. 30)
> "Dijkstra once said, 'Testing shows the presence, not the absence, of bugs.' […] a program can be proven incorrect by a test, but it cannot be proven correct."
>
> *Dijkstra từng nói: "Test cho thấy **sự hiện diện** của bug, không phải **sự vắng mặt** của chúng." […] một chương trình có thể bị test chứng minh là **sai**, nhưng không thể được chứng minh là **đúng**.*

Nên phần mềm không phải toán học mà giống **khoa học**: ta chỉ chứng minh được tính đúng *bằng cách thất bại trong việc chứng minh nó sai*. Đây là nền cho cả văn hoá test của [`clean-code` Bài 8](../../clean-code/bai_hoc/bai_08_unit_test.md).

## 3. Object-Oriented: kỷ luật trên luồng điều khiển gián tiếp

> [!quote] Ch. 3 — Object-Oriented Programming (tr. 21)
> "Object-oriented programming imposes discipline on indirect transfer of control."
>
> *Lập trình hướng đối tượng áp kỷ luật lên việc **chuyển điều khiển gián tiếp**.*

"Chuyển điều khiển gián tiếp" chính là con trỏ hàm — và kỷ luật áp lên nó sinh ra **đa hình** (polymorphism). Với kiến trúc sư, đây mới là điều OO *thực sự* mang lại — không phải đóng gói hay kế thừa, mà là **quyền kiểm soát chiều phụ thuộc**:

> [!quote] Ch. 5 — Dependency Inversion (tr. 45)
> "software architects working in systems written in OO languages have absolute control over the direction of all source code dependencies in the system. […] That is power! That is the power that OO provides."
>
> *kiến trúc sư làm việc với ngôn ngữ OO có **quyền kiểm soát tuyệt đối** chiều của mọi phụ thuộc mã nguồn trong hệ thống. […] Đó là sức mạnh! Đó là sức mạnh mà OO mang lại.*

Bình thường, phụ thuộc mã nguồn *buộc phải* cùng chiều với luồng điều khiển (hàm gọi phải "biết" hàm bị gọi). Chèn một interface vào giữa thì phụ thuộc mã nguồn bị **đảo ngược** so với luồng điều khiển — gọi là *dependency inversion*. Hệ quả: UI và database có thể trở thành **plugin** của business rules.

## 4. Code minh hoạ: sức mạnh kiến trúc của OO

Demo dưới đây là bản thu nhỏ của ví dụ "thiết bị IO là plugin" trong sách: hàm `copy` mức cao chỉ biết hai *interface*; các *chi tiết* (viết hoa, đảo ngược) là plugin mà mũi tên phụ thuộc trỏ **vào** `copy`:

```
   luồng điều khiển ───────────────────────────►
┌───────────┐     ┌─────────────┐     ┌───────────┐
│ copy()    │ ──► │ CharSink    │ ◄── │ UpperSink │
│ (mức cao) │     │ (interface) │     │ (plugin)  │
└───────────┘     └─────────────┘     └───────────┘
   phụ thuộc mã nguồn ◄──────────  (ĐẢO NGƯỢC so với luồng)
```

```typescript
import { strict as assert } from "node:assert";

// ===== Chính sách mức cao: KHÔNG biết chi tiết nguồn/đích =====
// phụ thuộc vào TRỪU TƯỢNG (interface), không vào cài đặt cụ thể
interface CharSource { readAll(): string; }
interface CharSink { write(s: string): void; }

function copy(source: CharSource, sink: CharSink): void {
  sink.write(source.readAll()); // mức cao, bất biến
}

// ===== Chi tiết mức thấp = PLUGIN. Mũi tên phụ thuộc trỏ VÀO copy =====
class StringSource implements CharSource {
  private data: string;
  constructor(data: string) { this.data = data; }
  readAll(): string { return this.data; }
}
class UpperSink implements CharSink {
  public out = "";
  write(s: string): void { this.out += s.toUpperCase(); }
}
class ReverseSink implements CharSink {
  public out = "";
  write(s: string): void { this.out += [...s].reverse().join(""); }
}

// đổi plugin mà KHÔNG đụng copy()
const upper = new UpperSink();
copy(new StringSource("clean arch"), upper);
const rev = new ReverseSink();
copy(new StringSource("clean arch"), rev);

assert.equal(upper.out, "CLEAN ARCH");
assert.equal(rev.out, "hcra naelc");
console.log("qua UpperSink  :", upper.out);
console.log("qua ReverseSink:", rev.out);
console.log("copy() không đổi 1 dòng — chi tiết là PLUGIN, phụ thuộc trỏ VÀO chính sách.");
```

Kết quả chạy thật:

```
qua UpperSink  : CLEAN ARCH
qua ReverseSink: hcra naelc
copy() không đổi 1 dòng — chi tiết là PLUGIN, phụ thuộc trỏ VÀO chính sách.
```

`copy` không hề nhắc tên `UpperSink` hay `ReverseSink`. Thêm một đích mới (ví dụ ghi ra file) chỉ cần viết một lớp `implements CharSink` — `copy` bất động. Đây đúng là "kiến trúc plugin" mà Uncle Bob nói OO cho phép dựng *ở bất cứ đâu*. Toàn bộ Phần V của sách (Bài 6–8 khoá này) xây trên chính cơ chế này.

> [!note] Tự thử
> 1. Viết `FileSink` ghi nối chuỗi với tiền tố `"[file] "`. `copy` có đổi dòng nào không?
> 2. Đảo: viết một `CharSource` đọc từ mảng. Chính sách `copy` có cần biết nguồn đến từ đâu không?
> 3. Bỏ hai interface, cho `copy` nhận thẳng `UpperSink`. Giờ muốn đổi sang `ReverseSink` bạn phải sửa `copy` — thấy vì sao interface = "đảo ngược phụ thuộc" chưa?

## 5. Functional: kỷ luật trên phép gán

> [!quote] Ch. 3 — Functional Programming (tr. 22)
> "Functional programming imposes discipline upon assignment."
>
> *Lập trình hàm áp kỷ luật lên **phép gán**.*

Nền của λ-calculus (Church, 1936) là **bất biến** (immutability): giá trị của ký hiệu không đổi — ngôn ngữ hàm thuần không có câu lệnh gán. Vì sao kiến trúc sư phải quan tâm chuyện biến có đổi được hay không?

> [!quote] Ch. 6 — Immutability and Architecture (tr. 51)
> "All race conditions, deadlock conditions, and concurrent update problems are due to mutable variables. You cannot have a race condition or a concurrent update problem if no variable is ever updated."
>
> *Mọi **race condition**, **deadlock**, và lỗi cập nhật đồng thời đều đến từ **biến khả biến**. Bạn không thể có race condition hay lỗi cập nhật đồng thời nếu không biến nào từng bị thay đổi.*

Đây chính là lời giải tận gốc cho mọi rắc rối ở [`clean-code` Bài 12 (Concurrency)](../../clean-code/bai_hoc/bai_12_concurrency.md): không có biến khả biến thì không có race. Thực tế bất biến tuyệt đối khó, nên sách nêu các *thoả hiệp*: tách thành phần bất biến khỏi thành phần khả biến, và **event sourcing** (lưu *chuỗi sự kiện* thay vì *trạng thái*, tính lại trạng thái khi cần).

## 6. Ba hệ hình khớp ba mối bận tâm kiến trúc

Lời kết của Phần II buộc ba hệ hình vào ba trụ của kiến trúc:

> [!quote] Ch. 5 — Conclusion (tr. 46)
> "OO is the ability, through the use of polymorphism, to gain absolute control over every source code dependency in the system. It allows the architect to create a plugin architecture."
>
> *OO là khả năng, thông qua đa hình, giành **quyền kiểm soát tuyệt đối** mọi phụ thuộc mã nguồn trong hệ thống. Nó cho phép kiến trúc sư dựng một **kiến trúc plugin**.*

Gói lại ba hệ hình và vai trò kiến trúc của chúng:

| Hệ hình | Kỷ luật | Dùng trong kiến trúc để… |
| :--- | :--- | :--- |
| Structured | luồng điều khiển trực tiếp | nền thuật toán của mỗi module (function) |
| Object-Oriented | luồng điều khiển gián tiếp | **vượt ranh giới** kiến trúc (separation of components) |
| Functional | phép gán | kỷ luật về **vị trí và truy cập dữ liệu** (data management) |

Và một nhận định khiêm nhường mà đắt: phần mềm **không** phải công nghệ tiến nhanh. "Quy tắc của phần mềm hôm nay vẫn là quy tắc năm 1946… Phần mềm gồm *tuần tự, lựa chọn, lặp, và gián tiếp* (sequence, selection, iteration, indirection). Không gì hơn, không gì kém." (Ch.6, tr.56)

## 7. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Khung "ba hệ hình, mỗi cái lấy đi một thứ" vẫn **đứng vững và sâu sắc** năm 2026 — nhưng thực hành đã dịch mạnh về phía functional.
> - **Functional từ "chỉ mới bắt đầu được dùng" (2017) → chủ đạo (2026).** Uncle Bob viết lúc FP còn ngách; nay bất biến là mặc định ở nhiều nơi: React (state bất biến, `useState`), Redux (reducer thuần), Rust (immutable mặc định, `mut` phải khai), structural sharing (Immer, Immutable.js). Lời khuyên "tách bất biến khỏi khả biến" giờ là *kiến trúc dòng chảy dữ liệu* phổ thông.
> - **Event sourcing + CQRS** đã trưởng thành thành mẫu kiến trúc thật (không chỉ "thoả hiệp"), nhưng (ponytail) nó đắt — đừng dùng cho CRUD thường; chỉ khi thật cần lịch sử/audit.
> - **"OO = kiểm soát chiều phụ thuộc" — vẫn là trái tim của Clean Architecture**, và là điều phân biệt OO-kiến-trúc với "OOP = class + kế thừa" mà nhiều người (và phong trào FP) chê. Lưu ý: *dependency inversion* đạt được bằng interface — mà interface thì FP cũng có (higher-order function, trait). Nên "sức mạnh đảo ngược phụ thuộc" không độc quyền của OO; đó là điểm hội tụ 2026.
> - **"Phần mềm không tiến nhanh; vẫn là sequence/selection/iteration/indirection"** — câu này càng vang trong kỷ nguyên AI: công cụ đổi long trời (Copilot, LLM) nhưng *bản chất* cấu trúc chương trình không đổi.

## 8. Áp dụng vào dự án của bạn

> [!question] Áp dụng vào dự án của bạn
> 1. **Tìm một chỗ "đảo ngược phụ thuộc".** Trong code bạn, business logic có `import` thẳng thư viện DB/HTTP không? Nếu có, mũi tên phụ thuộc đang trỏ *từ* chính sách *tới* chi tiết — ngược với lời khuyên. Thử chèn một interface.
> 2. **Săn biến khả biến chia sẻ.** Có state nào bị nhiều nơi cùng sửa không? Theo Ch.6, đó là nguồn *mọi* race condition. Làm nó bất biến được không?
> 3. **Nhận diện hệ hình trong stack của bạn.** React/Redux (functional), class service (OO), vòng lặp xử lý (structured) — bạn đang dùng mỗi cái cho đúng "mối bận tâm" của nó chưa?

## 9. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| :--- | :--- |
| **Paradigm (hệ hình)** | Lối lập trình áp *kỷ luật phủ định* — lấy đi một năng lực (tr. 22). |
| **Structured programming** | Kỷ luật trên luồng điều khiển trực tiếp; bỏ `goto` (tr. 21). |
| **Object-oriented programming** | Kỷ luật trên luồng điều khiển gián tiếp; sinh đa hình (tr. 21). |
| **Functional programming** | Kỷ luật trên phép gán; nền là bất biến (tr. 22). |
| **Polymorphism → dependency inversion** | Chèn interface để đảo chiều phụ thuộc mã nguồn so với luồng điều khiển (tr. 45). |
| **Plugin architecture** | UI/DB thành plugin của business rules nhờ đảo phụ thuộc (tr. 46). |
| **Immutability** | Giá trị không đổi; diệt tận gốc race/deadlock (tr. 51). |

## 10. Câu hỏi tự kiểm tra

1. Khuôn mẫu chung của ba hệ hình là gì? Mỗi cái *lấy đi* thứ gì? *(tr. 21–22)*
2. "Test cho thấy sự hiện diện, không phải sự vắng mặt của bug" dẫn tới kết luận gì về bản chất phần mềm? *(tr. 30)*
3. Với kiến trúc sư, OO *thực sự* mang lại điều gì (không phải đóng gói/kế thừa)? *(tr. 45)*
4. "Dependency inversion" nghĩa là gì? `copy()` ở mục 4 minh hoạ ra sao? *(tr. 45, mục 4)*
5. Vì sao biến khả biến là mối bận tâm *kiến trúc*? *(tr. 51)*
6. Ba hệ hình khớp ba mối bận tâm kiến trúc nào? *(tr. 46, 23)*

## Tóm tắt một trang

```
BÀI 1 — BA HỆ HÌNH: MỖI CÁI LẤY ĐI MỘT QUYỀN NĂNG
─────────────────────────────────────────────────────────
KHUÔN MẪU  "mỗi hệ hình LẤY ĐI một năng lực, không thêm" (tr.22).
   Cả ba ra đời 1958–1968. Không có hệ hình thứ tư.

STRUCTURED (1968, Dijkstra)  bỏ goto — kỷ luật điều khiển TRỰC TIẾP.
   "test cho thấy sự hiện diện, không vắng mặt của bug" (tr.30)
   → phần mềm như KHOA HỌC, chứng đúng = thất bại chứng sai.

OO (1966, Dahl&Nygaard)  bỏ con trỏ hàm — kỷ luật điều khiển GIÁN TIẾP
   → đa hình → ĐẢO NGƯỢC PHỤ THUỘC. "That is power!" (tr.45).
   copy(CharSource, CharSink): chi tiết là PLUGIN, phụ thuộc trỏ VÀO.
   UI/DB thành plugin của business rules (tr.46).

FUNCTIONAL (1936 Church / 1958 LISP)  bỏ phép gán — BẤT BIẾN.
   "mọi race/deadlock đều do biến khả biến" (tr.51). → event sourcing.

KHỚP KIẾN TRÚC: structured=thuật toán · OO=vượt ranh giới ·
   functional=quản lý dữ liệu.

2026  FP đã chủ đạo (React/Redux/Rust). Event sourcing trưởng thành
   (nhưng đắt). Đảo-phụ-thuộc không độc quyền OO. Bản chất phần mềm
   vẫn: sequence/selection/iteration/indirection (tr.56).
```

## Nguồn

- **Robert C. Martin**, *Clean Architecture* (Prentice Hall, 2017) — **Ch.3 "Paradigm Overview"** (`tr. 21–24`): ba hệ hình, mỗi cái áp kỷ luật phủ định, "each removes capabilities" (tr. 21–22); khớp ba mối bận tâm kiến trúc (tr. 23). **Ch.4 "Structured Programming"** (`tr. 25–32`): Dijkstra, functional decomposition, "testing shows presence not absence", phần mềm như khoa học (tr. 29–31). **Ch.5 "Object-Oriented Programming"** (`tr. 33–47`): đa hình, IO devices là plugin, dependency inversion, "That is power!", UI/DB là plugin, kết luận OO (tr. 44–47). **Ch.6 "Functional Programming"** (`tr. 49–56`): immutability, λ-calculus, "all race conditions… due to mutable variables", event sourcing, kết luận sequence/selection/iteration/indirection (tr. 50–56). `tai_lieu/Clean.Architecture.2017.9.pdf`
- Bối cảnh 2026 dẫn từ ngoài sách: React/Redux/Immer, Rust immutability, event sourcing + CQRS.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 27`.

---

**Bản đồ khoá học:** [Bài 0 — Hai giá trị](bai_00_hai_gia_tri.md) · [Bài 1 ← bạn đang ở đây] · [Bài 2 — SOLID (1): SRP, OCP](bai_02_solid_srp_ocp.md) · [Bài 3 — SOLID (2): LSP, ISP, DIP](bai_03_solid_lsp_isp_dip.md) · [Bài 4 — Nguyên tắc Component](bai_04_nguyen_tac_component.md) · [Bài 5 — Kiến trúc là gì & Độc lập](bai_05_kien_truc_va_doc_lap.md) · [Bài 6 — Ranh giới & Dependency Rule](bai_06_ranh_gioi_dependency_rule.md) · [Bài 7 — Business Rules & The Clean Architecture](bai_07_clean_architecture.md) · [Bài 8 — Humble Object, Main, Services](bai_08_humble_main_services.md) · [Bài 9 — Chi tiết: DB, Web, Framework](bai_09_chi_tiet.md) · [Bài 10 — The Missing Chapter: đóng gói](bai_10_dong_goi.md) · [Bài 11 — Case study & tổng kết](bai_11_case_study.md)

Xem thêm [README khoá học](../README.md).
