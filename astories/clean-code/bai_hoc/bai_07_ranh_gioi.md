# Bài 7 — Ranh giới: giữ code bên ngoài ở đúng rìa hệ thống

> [!info] Về bài này
> Dựng từ **Chương 8 — "Boundaries"** (tác giả James Grenning) của *Clean Code* (Robert C. Martin, 2008 — `tai_lieu/`, `tr. 113–120`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 31`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Mạch bài: *code ngoài rò rỉ khắp nơi → gọi tên vấn đề → bản sạch (TypeScript, chạy được) → nguyên tắc → đối chiếu 2026 → áp dụng*.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: căng thẳng giữa người cung và người dùng giao diện](#1-mở-đầu-căng-thẳng-giữa-người-cung-và-người-dùng-giao-diện)
2. [Code minh hoạ: bọc giao diện ranh giới](#2-code-minh-hoạ-bọc-giao-diện-ranh-giới)
3. [Learning test: học API bằng test](#3-learning-test-học-api-bằng-test)
4. [Dùng code chưa tồn tại: giao diện ta ước có](#4-dùng-code-chưa-tồn-tại-giao-diện-ta-ước-có)
5. [Ranh giới sạch](#5-ranh-giới-sạch)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào codebase của bạn](#7-áp-dụng-vào-codebase-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mở đầu: căng thẳng giữa người cung và người dùng giao diện

Ta hiếm khi kiểm soát toàn bộ phần mềm trong hệ thống của mình: có gói bên thứ ba, có mã nguồn mở, có component do đội khác làm. Phải tích hợp đám code "ngoại lai" ấy cho sạch sẽ. Gốc của vấn đề:

> [!quote] Ch. 8 — Using Third-Party Code (tr. 114)
> "There is a natural tension between the provider of an interface and the user of an interface."
>
> *Có một sự căng thẳng tự nhiên giữa **người cung cấp** một giao diện và **người dùng** giao diện đó.*

Người cung (ví dụ `java.util.Map`) muốn giao diện *rộng* để hợp nhiều hoàn cảnh; người dùng muốn giao diện *hẹp*, đúng nhu cầu mình. Một `Map` trần truyền đi khắp hệ thống kéo theo đủ method thừa (`clear()`, `remove()`…) mà ai cũng gọi được, và buộc mọi caller tự ép kiểu.

## 2. Code minh hoạ: bọc giao diện ranh giới

Lời giải: **bọc** giao diện ranh giới trong một lớp đo ni theo nhu cầu của bạn.

> [!quote] Ch. 8 — Using Third-Party Code (tr. 115)
> "If you use a boundary interface like Map, keep it inside the class, or close family of classes, where it is used. Avoid returning it from, or accepting it as an argument to, public APIs."
>
> *Nếu bạn dùng một giao diện ranh giới như `Map`, hãy giữ nó **bên trong** lớp (hoặc một nhóm lớp gần gũi) nơi nó được dùng. Tránh trả nó ra, hoặc nhận nó làm tham số, ở các API công khai.*

```typescript
import { strict as assert } from "node:assert";

type Sensor = { id: string; value: number };

// ===== Bản bẩn: truyền thẳng Map (giao diện ranh giới) đi khắp nơi =====
// Mọi caller phải tự ép kiểu, và dính mọi method thừa của Map (clear, delete...)
function readValueDirty(sensors: Map<string, unknown>, id: string): number {
  const s = sensors.get(id) as Sensor; // ép kiểu lặp đi lặp lại khắp nơi
  return s.value;
}

// ===== Bản sạch: bọc Map trong một lớp đo ni theo nhu cầu =====
class Sensors {
  private sensors: Map<string, Sensor> = new Map();
  add(sensor: Sensor): void {
    this.sensors.set(sensor.id, sensor);
  }
  getById(id: string): Sensor | undefined {
    return this.sensors.get(id); // ép kiểu + quản lý Map được giấu ở đây
  }
}

const raw = new Map<string, unknown>();
raw.set("s1", { id: "s1", value: 42 });

const wrapped = new Sensors();
wrapped.add({ id: "s1", value: 42 });

assert.equal(readValueDirty(raw, "s1"), wrapped.getById("s1")!.value);
console.log("giá trị qua Map trần:", readValueDirty(raw, "s1"));
console.log("giá trị qua Sensors :", wrapped.getById("s1")!.value);

// ===== "Giao diện ta ước có" + Adapter cho code CHƯA tồn tại =====
interface Transmitter {
  transmit(frequency: number, data: string): string;
}
class FakeTransmitter implements Transmitter {
  // dùng để test khi API thật chưa được định nghĩa
  transmit(frequency: number, data: string): string {
    return `[fake @${frequency}MHz] ${data}`;
  }
}
const tx: Transmitter = new FakeTransmitter();
console.log("qua ranh giới 'code chưa tồn tại':", tx.transmit(101, "xin chào"));
```

Kết quả chạy thật:

```
giá trị qua Map trần: 42
giá trị qua Sensors : 42
qua ranh giới 'code chưa tồn tại': [fake @101MHz] xin chào
```

Lớp `Sensors` giấu `Map` bên trong: nó có thể tiến hoá (đổi sang cấu trúc khác) mà gần như không ảnh hưởng phần còn lại; việc ép kiểu được gom một chỗ; và nó *đo ni* đúng nhu cầu — dễ hiểu, khó dùng sai. Đây chính là nguyên tắc "giấu cài đặt" của [Bài 5](bai_05_object_va_du_lieu.md) áp vào code của người khác.

> [!note] Tự thử
> 1. Thêm method `clear()` vào `Sensors` nhưng *cố ý không thêm*. Giờ caller có xoá sạch sensors được không? So với `Map` trần (ai cũng gọi `.clear()` được).
> 2. Đổi ruột `Sensors` từ `Map` sang mảng `Sensor[]`. Có bao nhiêu dòng *ngoài* lớp `Sensors` phải sửa? (Gợi ý: 0.)
> 3. Viết `RealTransmitter` cũng `implements Transmitter` nhưng trả chuỗi khác. Code dùng `tx` có phải đổi dòng nào không?

## 3. Learning test: học API bằng test

Không phải việc của ta để *test* code bên thứ ba, nhưng viết test để **học** nó thì rất đáng. Thay vì thử nghiệm API lạ ngay trong code sản xuất (rồi sa lầy gỡ lỗi không biết lỗi của mình hay của họ), hãy viết **learning test** — thí nghiệm có kiểm soát để kiểm tra *hiểu biết* của ta về API đó. Chương kể lại việc tự mò ra cách dùng log4j qua một chuỗi test nhỏ dần.

> [!quote] Ch. 8 — Learning Tests Are Better Than Free (tr. 118)
> "The learning tests end up costing nothing. We had to learn the API anyway, and writing those tests was an easy and isolated way to get that knowledge."
>
> *Learning test rốt cuộc chẳng tốn gì. Đằng nào ta cũng phải học API, và viết những test ấy là một cách dễ dàng, tách biệt để thu lấy tri thức đó.*

Hơn cả miễn phí: khi gói bên thứ ba ra bản mới, chạy lại learning test là biết ngay có thay đổi hành vi phá vỡ giả định của ta hay không.

## 4. Dùng code chưa tồn tại: giao diện ta ước có

Có một loại ranh giới khác — ranh giới giữa *cái đã biết* và *cái chưa biết*. Khi một hệ con (ví dụ "Transmitter") còn chưa định nghĩa API, đừng để bị chặn: hãy tự định nghĩa **giao diện mà ta ước mình có**.

> [!quote] Ch. 8 — Using Code That Does Not Yet Exist (tr. 119)
> "To keep from being blocked, we defined our own interface. […] This was the interface we wished we had."
>
> *Để khỏi bị chặn, chúng tôi tự định nghĩa giao diện của mình. […] Đây là giao diện mà chúng tôi **ước** mình có.*

Vì giao diện ấy *dưới quyền kiểm soát của ta*, code phía client sạch và tập trung. Khi API thật ra đời, chỉ cần viết một **Adapter** để bắc cầu — một chỗ duy nhất phải đổi khi API tiến hoá. Thiết kế này còn cho một "đường may" (*seam*) tiện lợi để test: dùng một `FakeTransmitter` là test được `CommunicationsController` mà không cần phần cứng thật.

## 5. Ranh giới sạch

> [!quote] Ch. 8 — Clean Boundaries (tr. 120)
> "It's better to depend on something you control than on something you don't control, lest it end up controlling you."
>
> *Thà phụ thuộc vào thứ bạn **kiểm soát** còn hơn phụ thuộc vào thứ bạn **không** kiểm soát — kẻo rốt cuộc chính nó kiểm soát bạn.*

Quản lý ranh giới bằng cách để **rất ít** nơi trong code nhắc tới code ngoài: hoặc bọc (như `Map` → `Sensors`), hoặc dùng Adapter đổi từ "giao diện hoàn hảo của ta" sang giao diện mà bên ngoài cung cấp. Dù cách nào, code cũng nói với ta rõ hơn, dùng nhất quán hơn, và có ít điểm phải bảo trì hơn khi bên thứ ba đổi.

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Đây là chương **già đi rất tốt** — nguyên tắc "cô lập cái bên ngoài" càng ngày càng đúng, và năm 2026 còn được nâng tầm thành kiến trúc.
> - **Bọc ranh giới = Ports & Adapters / Hexagonal / Clean Architecture.** Điều Grenning gọi là "giao diện ta ước có" + Adapter chính là *port* và *adapter* trong kiến trúc hình lục giác (Alistair Cockburn) và *Clean Architecture* (chính Uncle Bob, 2017). Năm 2026 đây là mẫu chủ đạo để cô lập DB, API ngoài, hàng đợi khỏi lõi nghiệp vụ — nối thẳng sang [Bài 10 (Hệ thống)](bai_10_he_thong.md) và khoá *Clean Architecture*.
> - **Learning test**: còn nguyên giá trị, và 2026 có thêm **contract testing** (Pact) cho ranh giới dịch vụ, và **snapshot/golden test** cho API. Tinh thần y hệt: ghim hành vi mong đợi của bên ngoài vào test tự động.
> - **Hệ kiểu mạnh làm phần "bọc" nhẹ hơn.** TypeScript generic (`Map<string, Sensor>`) đã bỏ được phần lớn việc ép kiểu thủ công mà ví dụ Java 2008 phải làm — nhưng *vẫn* nên bọc, vì lý do thật sự không phải ép kiểu mà là **giới hạn bề mặt** và **dễ thay thế**.
> - **Cân bằng (ponytail):** đừng bọc *mọi* thứ. Bọc thư viện bạn **có thể sẽ đổi** hoặc có bề mặt rộng nguy hiểm; đừng viết một lớp vô nghĩa quanh một hàm stdlib ổn định. "Thà phụ thuộc thứ mình kiểm soát" không có nghĩa là bọc cả `Math.max`.
> - **Vẫn vàng**: ít điểm chạm với code ngoài, Adapter một-chỗ-để-đổi, và "thà phụ thuộc thứ mình kiểm soát".

## 7. Áp dụng vào codebase của bạn

> [!question] Áp dụng vào codebase của bạn
> 1. **Đếm điểm chạm.** Chọn một thư viện bên thứ ba quan trọng (ORM, HTTP client, SDK). `grep` xem tên nó xuất hiện ở bao nhiêu file. Nhiều → bề mặt phụ thuộc rộng, khó thay.
> 2. **Bọc một ranh giới.** Chọn một chỗ bạn truyền thẳng kiểu của thư viện ngoài qua API nội bộ. Bọc nó trong một lớp/giao diện của bạn. Thử tưởng tượng đổi thư viện — giờ dễ hơn chứ?
> 3. **Viết một learning test.** Lần tới dùng một API lạ, viết 2–3 test nhỏ kiểm tra *hiểu biết* của bạn về nó, thay vì thử ngay trong code thật. Giữ chúng — chúng sẽ báo động khi bản mới đổi hành vi.
> 4. **"Giao diện ta ước có".** Có hệ con nào đang chặn bạn vì chưa xong không? Định nghĩa interface bạn *muốn*, code tiếp với một Fake, bắc Adapter sau.

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Boundary** | Rìa nơi code của ta gặp code ta không kiểm soát (thư viện, đội khác, hệ con) (tr. 113). |
| **Provider/user tension** | Người cung muốn giao diện rộng, người dùng muốn hẹp (tr. 114). |
| **Wrapping** | Bọc giao diện ranh giới trong lớp đo ni theo nhu cầu, giấu nó khỏi phần còn lại (tr. 115). |
| **Learning test** | Test nhỏ để *học* API bên thứ ba; miễn phí và báo động khi bản mới đổi (tr. 116–118). |
| **"Interface we wish we had"** | Tự định nghĩa giao diện mong muốn khi code thật chưa tồn tại (tr. 119). |
| **Adapter** | Lớp bắc cầu từ giao diện của ta sang API thật; một chỗ để đổi (tr. 119). |
| **Seam** | "Đường may" trong code cho phép chèn Fake để test (tr. 119). |

## 9. Câu hỏi tự kiểm tra

1. "Căng thẳng giữa người cung và người dùng giao diện" là gì? `Map` minh hoạ ra sao? *(tr. 114)*
2. Vì sao không nên truyền `Map` (hay giao diện ranh giới) qua API công khai? *(tr. 115)*
3. Learning test là gì, và vì sao nó "hơn cả miễn phí"? *(tr. 116–118)*
4. "Giao diện ta ước có" + Adapter giúp gì khi code bên kia chưa tồn tại? *(tr. 119)*
5. Năm 2026, nguyên tắc bọc ranh giới của chương này lớn lên thành kiến trúc nào?

## Tóm tắt một trang

```
BÀI 7 — RANH GIỚI: GIỮ CODE NGOÀI Ở ĐÚNG RÌA
─────────────────────────────────────────────────────────
CĂNG THẲNG  người cung muốn giao diện RỘNG, người dùng muốn
            HẸP (tr.114). Map trần → method thừa + ép kiểu khắp nơi.

BỌC    giữ giao diện ranh giới BÊN TRONG một lớp (tr.115).
       Map → lớp Sensors; đổi ruột Map↔mảng, ngoài không đổi dòng nào.
       Đừng trả/nhận giao diện ranh giới ở API công khai.

LEARNING TEST  học API bên thứ ba bằng test nhỏ (tr.116).
       "hơn cả miễn phí" (tr.118): báo động khi bản mới đổi hành vi.

CODE CHƯA TỒN TẠI  tự định nghĩa "giao diện ta ước có" (tr.119),
       code tiếp với Fake, bắc ADAPTER khi API thật ra đời.

NGUYÊN TẮC  "thà phụ thuộc thứ MÌNH kiểm soát" (tr.120).

2026   = Ports & Adapters / Hexagonal / Clean Architecture.
       Contract test (Pact). Generic bỏ bớt ép kiểu — nhưng vẫn
       bọc vì GIỚI HẠN BỀ MẶT + DỄ THAY. Đừng bọc cả Math.max.
```

## Nguồn

- **Robert C. Martin**, *Clean Code* (Prentice Hall, 2008) — **Chương 8, "Boundaries"** (James Grenning) (`tr. 113–120`): tích hợp code ngoại lai (tr. 113); căng thẳng cung/dùng, ví dụ `Map`, bọc thành `Sensors` (tr. 114–115); khám phá & học ranh giới, learning test, log4j (tr. 116–118); learning test "hơn cả miễn phí" (tr. 118); dùng code chưa tồn tại, "giao diện ta ước có", Adapter, seam (tr. 119–120); ranh giới sạch, "thà phụ thuộc thứ mình kiểm soát" (tr. 120). `tai_lieu/Clean.Code.2008.8.pdf`
- Bổ sung 2026 dẫn từ ngoài sách: Alistair Cockburn (*Hexagonal / Ports & Adapters*); Robert C. Martin, *Clean Architecture* (2017); contract testing (Pact).
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 31`.

---

**Bản đồ khoá học:** [Bài 0 — Clean Code là gì](bai_00_clean_code_la_gi.md) · [Bài 1 — Đặt tên](bai_01_dat_ten.md) · [Bài 2 — Hàm](bai_02_ham.md) · [Bài 3 — Comment](bai_03_comment.md) · [Bài 4 — Định dạng](bai_04_dinh_dang.md) · [Bài 5 — Object & dữ liệu](bai_05_object_va_du_lieu.md) · [Bài 6 — Xử lý lỗi](bai_06_xu_ly_loi.md) · [Bài 7 ← bạn đang ở đây] · [Bài 8 — Unit test](bai_08_unit_test.md) · [Bài 9 — Class](bai_09_class.md) · [Bài 10 — Hệ thống](bai_10_he_thong.md) · [Bài 11 — Thiết kế nổi lên](bai_11_thiet_ke_noi_len.md) · [Bài 12 — Concurrency](bai_12_concurrency.md) · [Bài 13 — Xem code sạch nảy sinh](bai_13_xem_code_nay_sinh.md) · [Bài 14 — Refactor ngoài đời](bai_14_refactor_ngoai_doi.md) · [Bài 15 — Danh mục mùi code](bai_15_danh_muc_mui_code.md)

Xem thêm [README khoá học](../README.md).
