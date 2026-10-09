# Bài 5 — Kiến trúc là gì & Tính độc lập: giữ ngỏ lựa chọn

> [!info] Về bài này
> Dựng từ **Phần V — Architecture**: **Ch.15 "What Is Architecture?"** và **Ch.16 "Independence"** của *Clean Architecture* (Robert C. Martin, 2017 — `tai_lieu/`, `tr. 135–158`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 27`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Mở đầu Phần V — phần "ruột" của sách. Nối [Bài 4 (Component)](bai_04_nguyen_tac_component.md) và dẫn vào [Bài 6 (Ranh giới)](bai_06_ranh_gioi_dependency_rule.md).
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Kiến trúc sư trước hết là lập trình viên](#1-kiến-trúc-sư-trước-hết-là-lập-trình-viên)
2. [Kiến trúc là *hình dạng*, mục tiêu là *vòng đời*](#2-kiến-trúc-là-hình-dạng-mục-tiêu-là-vòng-đời)
3. [Giữ ngỏ lựa chọn: tối đa hoá quyết định *chưa* ra](#3-giữ-ngỏ-lựa-chọn-tối-đa-hoá-quyết-định-chưa-ra)
4. [Code minh hoạ: hoãn quyết định database](#4-code-minh-hoạ-hoãn-quyết-định-database)
5. [Tính độc lập: bốn thứ kiến trúc phải đỡ](#5-tính-độc-lập-bốn-thứ-kiến-trúc-phải-đỡ)
6. [Tách lớp ngang và lát use-case dọc](#6-tách-lớp-ngang-và-lát-use-case-dọc)
7. [Đối chiếu 2026](#7-đối-chiếu-2026)
8. [Áp dụng vào dự án của bạn](#8-áp-dụng-vào-dự-án-của-bạn)
9. [Từ điển thuật ngữ](#9-từ-điển-thuật-ngữ)
10. [Câu hỏi tự kiểm tra](#10-câu-hỏi-tự-kiểm-tra)
11. [Tóm tắt một trang](#tóm-tắt-một-trang)
12. [Nguồn](#nguồn)

---

## 1. Kiến trúc sư trước hết là lập trình viên

> [!quote] Ch. 15 — What Is Architecture? (tr. 135)
> "a software architect is a programmer; and continues to be a programmer."
>
> *một kiến trúc sư phần mềm **là** một lập trình viên; và **tiếp tục** là lập trình viên.*

Khác xây dựng dân dụng, kiến trúc sư phần mềm không "lên bàn giấy" bỏ code. Họ vẫn viết code, vì chỉ khi trực tiếp chịu đựng các vấn đề do thiết kế gây ra thì mới dẫn dắt được. Đây là tiếng vọng của [`clean-coder`](../../clean-coder/README.md): nghề không tách khỏi tay nghề.

## 2. Kiến trúc là *hình dạng*, mục tiêu là *vòng đời*

> [!quote] Ch. 15 — What Is Architecture? (tr. 135)
> "The architecture of a software system is the shape given to that system by those who build it."
>
> *Kiến trúc của một hệ thống phần mềm là **hình dạng** mà những người xây nó trao cho nó.*

Hình dạng ấy nằm ở cách chia thành component, cách sắp xếp, và cách chúng giao tiếp. Mục đích:

> [!quote] Ch. 15 — What Is Architecture? (tr. 135)
> "The purpose of that shape is to facilitate the development, deployment, operation, and maintenance of the software system."
>
> *Mục đích của hình dạng đó là **tạo thuận lợi** cho việc phát triển, triển khai, vận hành và bảo trì hệ thống.*

Và chiến lược để tạo thuận lợi gói trong một câu — chính là định nghĩa "mềm" của [Bài 0](bai_00_hai_gia_tri.md):

> [!quote] Ch. 15 — What Is Architecture? (tr. 135)
> "The strategy behind that facilitation is to leave as many options open as possible, for as long as possible."
>
> *Chiến lược đằng sau sự thuận lợi đó là **giữ ngỏ càng nhiều lựa chọn càng tốt, càng lâu càng tốt**.*

Lưu ý tinh tế: kiến trúc có *rất ít* liên quan tới chuyện hệ thống có *chạy đúng* hay không (bạn có thể làm hệ chạy với kiến trúc tệ hại). Mục tiêu đầu tiên của kiến trúc là **đỡ vòng đời** — làm hệ dễ hiểu, dễ phát triển, dễ bảo trì, dễ triển khai.

## 3. Giữ ngỏ lựa chọn: tối đa hoá quyết định *chưa* ra

Đây là ý gây tranh cãi nhất — và cũng đắt nhất — của chương:

> [!quote] Ch. 15 — Keeping Options Open (tr. 141)
> "A good architect maximizes the number of decisions not made."
>
> *Một kiến trúc sư giỏi **tối đa hoá số quyết định CHƯA ra**.*

Những quyết định nên hoãn là về **chi tiết** — thứ *không* phải nghiệp vụ cốt lõi. Sách liệt kê thẳng những thứ *không cần quyết sớm*:

| Quyết định có thể hoãn | Vì chính sách mức cao… |
| :--- | :--- |
| Dùng database nào (quan hệ? phân tán? file phẳng?) | không nên quan tâm dữ liệu lưu kiểu gì |
| Dùng web server nào (HTML/AJAX/JSP/JSF) | không nên biết mình được giao qua web |
| Có dùng REST / micro-service / SOA không | nên vô tư với giao diện ra thế giới ngoài |
| Dùng framework DI nào | không nên quan tâm phụ thuộc được giải quyết ra sao |

"Nếu phát triển được chính sách mức cao mà *chưa* cam kết với các chi tiết quanh nó, bạn có thể hoãn quyết định về chúng rất lâu — càng hoãn, càng có nhiều thông tin để quyết đúng, và càng có thể thử nhiều thí nghiệm." (Ch.15, tr.141)

## 4. Code minh hoạ: hoãn quyết định database

Chính sách mức cao (`greet`) chạy được *trước khi* quyết định database — nó chỉ biết một *interface*. Quyết định backend bị hoãn tới tận `main`:

```typescript
import { strict as assert } from "node:assert";

// Chính sách mức cao: use case KHÔNG biết dữ liệu lưu ở đâu
interface UserGateway {
  findName(id: number): string | undefined;
}
function greet(gateway: UserGateway, id: number): string {
  const name = gateway.findName(id);
  return name ? `Xin chào, ${name}!` : "Không tìm thấy người dùng.";
}

// Quyết định DB bị HOÃN: hôm nay in-memory; mai có thể SQL/file — use case không đổi
class InMemoryGateway implements UserGateway {
  private data = new Map<number, string>([[1, "An"], [2, "Bình"]]);
  findName(id: number): string | undefined { return this.data.get(id); }
}
class SqlLikeGateway implements UserGateway {
  // giả lập backend khác (vd kết quả "SELECT name FROM users WHERE id=?")
  findName(id: number): string | undefined {
    const rows: Record<number, string> = { 1: "An", 2: "Bình" };
    return rows[id];
  }
}

// main() là nơi DUY NHẤT chọn backend — quyết định "để mở" tới phút chót
for (const gw of [new InMemoryGateway(), new SqlLikeGateway()]) {
  assert.equal(greet(gw, 1), "Xin chào, An!");
  assert.equal(greet(gw, 99), "Không tìm thấy người dùng.");
}
console.log(greet(new InMemoryGateway(), 1));
console.log(greet(new SqlLikeGateway(), 2));
console.log("greet() không hề biết DB là gì — quyết định được HOÃN tới main().");
```

Kết quả chạy thật:

```
Xin chào, An!
Xin chào, Bình!
greet() không hề biết DB là gì — quyết định được HOÃN tới main().
```

`greet` không nhắc tới `Map`, SQL, hay file — nó chỉ nói chuyện với `UserGateway`. Bạn có thể xây và test toàn bộ use case với `InMemoryGateway`, rồi *nhiều tháng sau* mới quyết dùng Postgres hay Mongo, chỉ bằng cách viết một gateway mới và đổi một dòng ở `main`. Đó là "quyết định chưa ra" thành hiện thực. Và đây chính là nền cho "Database là chi tiết" ở [Bài 9](bai_09_chi_tiet.md).

> [!note] Tự thử
> 1. Viết `FileGateway` đọc từ một object JSON. `greet` có đổi dòng nào không?
> 2. Giả sử bạn đã lỡ cho `greet` gọi thẳng `new InMemoryGateway()` bên trong. Giờ muốn test với dữ liệu khác, bạn kẹt thế nào? (Đó là "quyết định đã ra quá sớm".)
> 3. Thêm method `save(id, name)` vào interface. Hai gateway phải làm gì? Chính sách `greet` có cần biết `save` cài đặt ra sao không?

## 5. Tính độc lập: bốn thứ kiến trúc phải đỡ

Chương 16 liệt kê bốn thứ một kiến trúc tốt phải hỗ trợ:

> [!quote] Ch. 16 — Independence (tr. 147)
> "a good architecture must support: The use cases and operation of the system. The maintenance of the system. The development of the system. The deployment of the system."
>
> *một kiến trúc tốt phải đỡ: **use case và vận hành** của hệ; **bảo trì**; **phát triển**; và **triển khai**.*

Điều quan trọng nhất kiến trúc làm cho *hành vi* là khiến use case **hiện rõ**:

> [!quote] Ch. 16 — Use Cases (tr. 147)
> "A shopping cart application with a good architecture will look like a shopping cart application."
>
> *Một ứng dụng giỏ hàng có kiến trúc tốt sẽ **trông giống một ứng dụng giỏ hàng**.*

(Đây là mầm của "Screaming Architecture" — kiến trúc phải *hét lên* nó là ứng dụng gì, không phải hét lên nó dùng framework gì. Nối [Bài 7](bai_07_clean_architecture.md).)

## 6. Tách lớp ngang và lát use-case dọc

Kiến trúc tốt tách hệ theo *hai* chiều: **lớp ngang** (UI / business rules / database) và **lát use-case dọc** (mỗi use case cắt qua vài lớp). Tách được thì mỗi lớp và mỗi use case phát triển, triển khai độc lập, và dễ thêm use case mới mà không phá cái cũ. Nhưng tách tới *mức* nào thì tuỳ — và đó là một quyết định nên **giữ ngỏ**:

> [!quote] Ch. 16 — Decoupling Modes (tr. 153)
> "a good architecture leaves options open. The decoupling mode is one of those options."
>
> *một kiến trúc tốt giữ ngỏ lựa chọn. **Chế độ tách ghép** (decoupling mode) chính là một trong những lựa chọn đó.*

Ba chế độ tách ghép (decoupling mode), từ nhẹ tới nặng:

| Chế độ | Component tách ở mức | Ví dụ |
| :--- | :--- | :--- |
| **Source level** | mã nguồn (cùng tiến trình, cùng địa chỉ) | module/package trong một monolith |
| **Deployment level** | đơn vị triển khai độc lập | jar/DLL/gem nạp động |
| **Service level** | tiến trình/mạng riêng | micro-service, REST |

Uncle Bob khuyên: giữ *khả năng* lên cấp cao hơn khi cần, nhưng **đừng vội** nhảy thẳng lên service level — đó là quyết định tốn kém, nên hoãn.

## 7. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Chương này là **tâm điểm tranh luận kiến trúc 2026** — và Uncle Bob đứng về phía ngày càng thắng thế.
> - **"Đừng vội lên service level" → modular monolith thắng thế (2026).** Lời khuyên "giữ khả năng tách service nhưng đừng vội" (tr.153) từng bị làn sóng microservices 2015–2020 phớt lờ. Năm 2026 con lắc đã quay lại: **modular monolith** (Shopify, và Amazon Prime Video nổi tiếng gộp microservice về monolith để giảm chi phí 90%) là lựa chọn mặc định cho phần lớn đội. Decoupling ở *source level* trước, chỉ lên *service level* khi có lý do thật (scale độc lập, team độc lập). Đây đúng là điều sách nói từ 2017.
> - **"Maximizes decisions not made" vs YAGNI (ponytail).** Câu này nghe ngược với "đừng build sẵn cho tương lai", nhưng *không* mâu thuẫn: hoãn quyết định *chi tiết* (DB/web/framework) **chính là** không build sẵn cho chúng. Cái bẫy là hiểu nhầm thành "xây sẵn tầng abstraction cho mọi lựa chọn" — đó mới là over-engineering. Giữ-ngỏ đạt bằng *một interface mỏng ở ranh giới*, không bằng *một framework trừu tượng đồ sộ*.
> - **"Hoãn quyết định DB/web" — mạnh hơn nhờ công cụ 2026.** In-memory test, testcontainers, repository pattern, ORM đổi backend bằng config — tất cả khiến việc hoãn-quyết-định-DB rẻ hơn 2017 nhiều.
> - **Vẫn gây tranh cãi:** phe "framework-first" (Rails, Spring Boot, Next.js) lập luận ngược: *ôm* framework sớm để đi nhanh, chấp nhận coupling. Với sản phẩm nhỏ/đời ngắn, họ có lý (xem Bài 0 §Đối chiếu). Clean Architecture trả giá bằng indirection; biết *khi nào* đáng trả mới là nghề.

## 8. Áp dụng vào dự án của bạn

> [!question] Áp dụng vào dự án của bạn
> 1. **Liệt kê quyết định "đã ra quá sớm".** Core logic của bạn có cam kết sớm với DB/web/framework cụ thể nào mà giờ khó gỡ không? Mỗi cái là một "option" đã đóng.
> 2. **Thử phép "trông giống ứng dụng gì".** Nhìn thư mục cấp cao nhất của dự án: nó hét lên "ứng dụng [nghiệp vụ]" hay hét lên "dự án Spring/Next.js"? (Chuẩn bị cho Bài 7.)
> 3. **Chọn decoupling mode có ý thức.** Dự án đang ở mức nào (source/deployment/service)? Việc lên service (microservice) là *quyết định có cân nhắc* hay *theo trend*? Modular monolith có đủ chưa?

## 9. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| :--- | :--- |
| **Architecture = shape** | Hình dạng người xây trao cho hệ: chia component, sắp xếp, giao tiếp (tr. 135). |
| **Facilitate the life cycle** | Mục tiêu kiến trúc: đỡ phát triển/triển khai/vận hành/bảo trì (tr. 135–136). |
| **Keep options open** | Giữ ngỏ lựa chọn càng lâu càng tốt; "maximize decisions not made" (tr. 141). |
| **Details vs policy** | DB/web/framework là *chi tiết* nên hoãn; nghiệp vụ là *chính sách* mức cao. |
| **Independence (4)** | Kiến trúc đỡ: use case/vận hành, bảo trì, phát triển, triển khai (tr. 147). |
| **Decoupling modes** | Source / deployment / service level — chế độ tách ghép, cũng là một lựa chọn để ngỏ (tr. 153). |

## 10. Câu hỏi tự kiểm tra

1. Vì sao "kiến trúc sư vẫn là lập trình viên"? *(tr. 135)*
2. Kiến trúc là *hình dạng* để làm gì? Mục tiêu đầu tiên của nó là gì (không phải "chạy đúng")? *(tr. 135–136)*
3. "Maximize the number of decisions not made" nghĩa là gì? Kể ba quyết định nên hoãn. *(tr. 141)*
4. Trong demo, vì sao `greet` test được *trước khi* chọn database? *(mục 4)*
5. Ba decoupling mode là gì? Vì sao "đừng vội lên service level"? *(tr. 153)*

## Tóm tắt một trang

```
BÀI 5 — KIẾN TRÚC LÀ GÌ & ĐỘC LẬP: GIỮ NGỎ LỰA CHỌN
─────────────────────────────────────────────────────────
KTS = lập trình viên, và TIẾP TỤC là lập trình viên (tr.135).

KIẾN TRÚC = HÌNH DẠNG người xây trao cho hệ (tr.135).
   Mục đích: tạo thuận lợi phát triển/triển khai/vận hành/bảo trì.
   Chiến lược: "giữ ngỏ càng nhiều lựa chọn càng lâu càng tốt" (tr.135).
   Mục tiêu đầu KHÔNG phải "chạy đúng" mà là ĐỠ VÒNG ĐỜI.

GIỮ NGỎ  "KTS giỏi tối đa hoá số quyết định CHƯA ra" (tr.141).
   Hoãn: DB · web server · REST/microservice · DI framework.
   greet(UserGateway): test xong trước khi chọn DB → hoãn tới main().

ĐỘC LẬP  kiến trúc đỡ 4 thứ: use case · bảo trì · phát triển · triển khai (tr.147).
   "app giỏ hàng tốt sẽ TRÔNG GIỐNG app giỏ hàng" (tr.147) → Bài 7.
   Tách LỚP NGANG + LÁT use-case DỌC. Decoupling mode: source/
   deployment/service — "một lựa chọn để ngỏ" (tr.153).

2026  modular monolith thắng thế (đừng vội microservice — đúng ý
   sách từ 2017). "decisions not made" ≠ build sẵn (giữ ngỏ =
   interface mỏng, KHÔNG framework đồ sộ). Framework-first có lý
   cho sản phẩm nhỏ/đời ngắn.
```

## Nguồn

- **Robert C. Martin**, *Clean Architecture* (Prentice Hall, 2017) — **Ch.15 "What Is Architecture?"** (`tr. 135–146`): kiến trúc sư là lập trình viên (tr. 135); kiến trúc = shape, mục đích facilitate vòng đời, "leave options open" (tr. 135–137); keeping options open, danh sách quyết định hoãn, "maximizes decisions not made", device independence (tr. 139–146). **Ch.16 "Independence"** (`tr. 147–158`): bốn thứ kiến trúc phải đỡ, use case hiện rõ, "look like a shopping cart application" (tr. 147–148); tách lớp ngang & lát use-case dọc (tr. 150–152); ba decoupling mode, "a good architecture leaves options open" (tr. 153–156). `tai_lieu/Clean.Architecture.2017.9.pdf`
- Bối cảnh 2026 dẫn từ ngoài sách: modular monolith (Shopify; Amazon Prime Video), microservices backlash; testcontainers; framework-first vs YAGNI.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 27`.

---

**Bản đồ khoá học:** [Bài 0 — Hai giá trị](bai_00_hai_gia_tri.md) · [Bài 1 — Ba hệ hình lập trình](bai_01_he_hinh_lap_trinh.md) · [Bài 2 — SOLID (1): SRP, OCP](bai_02_solid_srp_ocp.md) · [Bài 3 — SOLID (2): LSP, ISP, DIP](bai_03_solid_lsp_isp_dip.md) · [Bài 4 — Nguyên tắc Component](bai_04_nguyen_tac_component.md) · [Bài 5 ← bạn đang ở đây] · [Bài 6 — Ranh giới & Dependency Rule](bai_06_ranh_gioi_dependency_rule.md) · [Bài 7 — Business Rules & The Clean Architecture](bai_07_clean_architecture.md) · [Bài 8 — Humble Object, Main, Services](bai_08_humble_main_services.md) · [Bài 9 — Chi tiết: DB, Web, Framework](bai_09_chi_tiet.md) · [Bài 10 — The Missing Chapter: đóng gói](bai_10_dong_goi.md) · [Bài 11 — Case study & tổng kết](bai_11_case_study.md)

Xem thêm [README khoá học](../README.md).
