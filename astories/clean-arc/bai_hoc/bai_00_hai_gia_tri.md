# Bài 0 — Hai giá trị: hành vi và cấu trúc

> [!info] Về bài này
> Dựng từ **Phần I — Introduction**: **Chương 1 "What Is Design and Architecture?"** và **Chương 2 "A Tale of Two Values"** của *Clean Architecture* (Robert C. Martin — "Uncle Bob", Prentice Hall, 2017 — `tai_lieu/`, `tr. 3–17`).
> Trích theo `Ch. N` (chương) và `tr. X` (số trang **in trong sách**; muốn tra tệp PDF thì cộng 27 → PDF = `tr. + 27`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn — vì nguồn là tiếng Anh.
> Đây là khoá **khái niệm + sơ đồ**: trục chính là giảng kiến trúc, vẽ lại sơ đồ cốt lõi bằng ASCII, và đóng gói các phân loại của sách thành **bảng so sánh**; chỉ nhúng demo TypeScript **chạy được** ở nơi code thật sự soi sáng.
> Đây là **tập cuối bộ ba** Uncle Bob — sau [`clean-coder`](../../clean-coder/README.md) (hành xử nghề) và [`clean-code`](../../clean-code/README.md) (viết code), cuốn này nói về *cấu trúc hệ thống*.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`. Không cần cài gói.

## Mục lục

1. [Mở đầu: code đắt gấp 40 lần sau tám release](#1-mở-đầu-code-đắt-gấp-40-lần-sau-tám-release)
2. [Design và Architecture là một](#2-design-và-architecture-là-một)
3. [Rùa và Thỏ: lời nói dối "dọn sau"](#3-rùa-và-thỏ-lời-nói-dối-dọn-sau)
4. [Hai giá trị: hành vi và cấu trúc](#4-hai-giá-trị-hành-vi-và-cấu-trúc)
5. [Code minh hoạ: "mềm" so với "cứng"](#5-code-minh-hoạ-mềm-so-với-cứng)
6. [Giá trị nào lớn hơn? Ma trận Eisenhower](#6-giá-trị-nào-lớn-hơn-ma-trận-eisenhower)
7. [Đối chiếu 2026](#7-đối-chiếu-2026)
8. [Áp dụng vào dự án của bạn](#8-áp-dụng-vào-dự-án-của-bạn)
9. [Từ điển thuật ngữ](#9-từ-điển-thuật-ngữ)
10. [Câu hỏi tự kiểm tra](#10-câu-hỏi-tự-kiểm-tra)
11. [Tóm tắt một trang](#tóm-tắt-một-trang)
12. [Nguồn](#nguồn)

---

## 1. Mở đầu: code đắt gấp 40 lần sau tám release

Uncle Bob mở sách bằng số liệu thật của một công ty giấu tên. Đội kỹ sư tăng đều qua tám release — nhìn đồ thị nhân sự thì như một câu chuyện thành công. Nhưng ông đặt cạnh nó hai đồ thị khác: *năng suất* (đo thô bằng số dòng code mỗi release) tiệm cận một đường ngang, còn *chi phí mỗi dòng code* thì vọt dựng đứng.


| Mốc       | Lương kỹ thuật / tháng | Ghi chú của sách               |
| :--------- | ----------------------: | :------------------------------ |
| Release 1 | vài trăm nghìn đô      | mua được *rất nhiều* tính năng |
| Release 2 | thêm vài trăm nghìn    | —                              |
| Release 8 | **\~20 triệu đô**      | mua được *gần như không gì*    |


> [!quote] Ch. 1 — Case Study (tr. 5)
> "Why was the code 40 times more expensive to produce in release 8 as opposed to release 1?"
>
> *Vì sao code ở release 8 lại đắt gấp **40 lần** so với release 1?*

Đồ thị "năng suất theo release" (Figure 1.4) cho thấy đội khởi đầu ở gần 100% năng suất rồi tụt dần, tới release 4 thì rõ ràng đang tiệm cận 0. Điều đau nhất: *không ai lười cả*. Mọi người vẫn cày, vẫn tăng ca, vẫn tận tuỵ — nhưng công sức bị hút hết vào việc **dời mớ hỗn độn** từ chỗ này sang chỗ khác để nhét thêm một tính năng còm. Uncle Bob gọi hình dạng đồ thị ấy bằng một cái tên:

> [!quote] Ch. 1 — The Signature of a Mess (tr. 6)
> "What you are looking at is the signature of a mess."
>
> *Cái bạn đang nhìn là **chữ ký của một mớ hỗn độn**.*

Từ góc nhìn CFO, hai đồ thị (lương dựng đứng, tính năng nằm ngang) là lời cảnh báo phải hành động ngay. Đây cũng là bài học của [`clean-code` Bài 0](../../clean-code/bai_hoc/bai_00_clean_code_la_gi.md), nay nhìn ở tầm *hệ thống* và quy ra *tiền*.

## 2. Design và Architecture là một

Nhiều người tưởng "architecture" là chuyện mức cao, tách khỏi "design" mức thấp. Uncle Bob bác bỏ ngay từ câu đầu:

> [!quote] Ch. 1 — What Is Design and Architecture? (tr. 3)
> "I'll assert that there is no difference between them. None at all."
>
> *Tôi khẳng định rằng chẳng có khác biệt nào giữa chúng. **Không một chút nào.***

Ông ví với bản vẽ ngôi nhà mình: kiến trúc sư vẽ cả hình khối, mặt đứng, bố trí phòng (mức cao) *lẫn* vị trí từng ổ cắm, công tắc nào điều khiển đèn nào, chỗ đặt bình nước nóng, cách dựng tường-mái-móng (mức thấp). Tất cả là **một tấm vải liền mạch** — "một dải liên tục các quyết định từ cao nhất tới thấp nhất", không có lằn ranh rạch ròi. Và mục tiêu của toàn bộ dải quyết định ấy gói trong một câu — Uncle Bob gọi là "mô tả không tưởng" của mình:

> [!quote] Ch. 1 — The Goal? (tr. 4)
> "The goal of software architecture is to minimize the human resources required to build and maintain the required system."
>
> *Mục tiêu của kiến trúc phần mềm là **tối thiểu hoá nhân lực** cần để **xây và bảo trì** hệ thống.*

Từ đó suy ra thước đo chất lượng thiết kế — đơn giản đến bất ngờ: *công sức bỏ ra để đáp ứng nhu cầu khách hàng*. Công sức thấp và **giữ thấp suốt đời** hệ thống → thiết kế tốt. Nó tăng dần theo mỗi release (như case study ở mục 1) → thiết kế tồi. "Đơn giản vậy thôi."

## 3. Rùa và Thỏ: lời nói dối "dọn sau"

Vì sao các đội rơi vào "chữ ký của mớ hỗn độn"? Uncle Bob mượn ngụ ngôn Rùa và Thỏ (Aesop, \~2600 năm trước): Thỏ quá tự tin vào tốc độ nên ngủ quên. Lập trình viên hiện đại cũng *tự tin thái quá* y vậy — không phải họ ngủ (họ cày bục mặt), mà là *một phần trí não* ngủ quên: phần biết rằng code sạch, thiết kế tốt mới là thứ quan trọng. Họ tin vào một lời nói dối quen thuộc:

> [!quote] Ch. 1 — What Went Wrong? (tr. 9)
> "We can clean it up later; we just have to get to market first!"
>
> *"Dọn sau cũng được; giờ cứ phải ra thị trường trước đã!"*

Nhưng "sau" không bao giờ tới, vì áp lực thị trường chẳng bao giờ ngớt. Và đây là *lời nói dối lớn hơn*: rằng bày bừa giúp đi nhanh trong ngắn hạn, chỉ chậm lại về dài hạn. Uncle Bob bác thẳng:

> [!quote] Ch. 1 — What Went Wrong? (tr. 9)
> "making messes is always slower than staying clean, no matter which time scale you are using."
>
> *bày bừa **luôn luôn** chậm hơn giữ sạch, bất kể bạn đo trên thang thời gian nào.*

Ông dẫn thí nghiệm của Jason Gorman: sáu ngày, mỗi ngày viết lại cùng một chương trình đổi số sang chữ số La Mã; ngày 1-3-5 dùng TDD, ngày 2-4-6 không. Kết quả: ngày dùng TDD nhanh hơn \~10%, và *ngày TDD chậm nhất vẫn nhanh hơn ngày không-TDD nhanh nhất*. Chân lý ông rút ra — và sẽ lặp lại suốt sách:

> [!quote] Ch. 1 — What Went Wrong? (tr. 10)
> "The only way to go fast, is to go well."
>
> *Cách duy nhất để đi **nhanh** là đi cho **đàng hoàng**.*

## 4. Hai giá trị: hành vi và cấu trúc

Đây là luận đề nền của cả cuốn sách:

> [!quote] Ch. 2 — A Tale of Two Values (tr. 13)
> "Every software system provides two different values to the stakeholders: behavior and structure."
>
> *Mọi hệ thống phần mềm cung cấp hai giá trị khác nhau cho các bên liên quan: **hành vi** và **cấu trúc**.*

Lập trình viên hay dồn hết tâm sức cho giá trị thứ nhất và bỏ bê giá trị thứ hai — thậm chí bỏ bê đúng cái *lớn hơn*. Bảng đối chiếu hai giá trị (gói lại cả Chương 2):


|                                | **Hành vi** (behavior)                   | **Cấu trúc** (architecture)          |
| :------------------------------ | :---------------------------------------- | :------------------------------------ |
| Là gì                          | làm máy chạy đúng yêu cầu, sinh/giữ tiền | giữ phần mềm **"mềm"** — dễ thay đổi |
| Nằm ở đâu trong chữ "software" | "ware" (sản phẩm)                        | **"soft"**                           |
| Tính khẩn cấp                  | **khẩn** — có bug là phải sửa ngay       | không bao giờ thật khẩn              |
| Tầm quan trọng                 | không phải lúc nào cũng quan trọng       | **luôn** quan trọng                  |
| Ai dễ thấy / lo                | ai cũng thấy, ai cũng lo                 | dễ bị bỏ quên                        |
| Hỏng thì sao                   | sai yêu cầu → debug                      | hệ thống cứng lại → dần vô dụng      |


Về giá trị thứ hai, Uncle Bob truy nguyên từ chính cái tên:

> [!quote] Ch. 2 — Architecture (tr. 13)
> "Software was invented to be 'soft.' It was intended to be a way to easily change the behavior of machines."
>
> \*Phần mềm được phát minh ra để **"mềm"**. Nó vốn là cách để **dễ dàng thay đổi** hành vi của máy.\*

Nếu muốn hành vi *khó* đổi, ta đã gọi nó là "hardware". Độ khó của một thay đổi nên tỉ lệ với **phạm vi** (scope) — nó *to hay nhỏ* — chứ không với **hình dạng** (shape) — nó *khớp hay không khớp* kết cấu hiện có. Khi kiến trúc "thiên vị" một hình dạng, mọi yêu cầu mới lại như *mảnh ghép hình vuông nhét vào lỗ tròn*, và chi phí phát triển phình ra ngoài tỉ lệ với kích thước yêu cầu. Nên:

> [!quote] Ch. 2 — Architecture (tr. 14)
> "architectures should be as shape agnostic are practical."
>
> *kiến trúc nên **vô tư với hình dạng** (shape-agnostic) hết mức có thể.* (Nguyên văn sách in nhầm "are" thay vì "as".)

## 5. Code minh hoạ: "mềm" so với "cứng"

Hai hàm tính giá dưới đây cho **cùng hành vi hôm nay**. Khác biệt — tức *hình dạng* — chỉ lộ ra khi yêu cầu đổi:

```typescript
import { strict as assert } from "node:assert";

// ===== Chỉ coi trọng HÀNH VI: chạy đúng hôm nay, nhưng "cứng" =====
// thêm nước mới = mổ chính hàm này (sửa + test lại + rủi ro)
function priceRigid(amount: number, country: string): number {
  if (country === "VN") return Math.round(amount * 1.10);
  else if (country === "US") return Math.round(amount * 1.07);
  else if (country === "EU") return Math.round(amount * 1.20);
  else return amount;
}

// ===== Coi trọng CẤU TRÚC: cùng hành vi, nhưng "mềm" =====
// thêm nước mới = thêm MỘT dòng dữ liệu, không đụng logic
const VAT: Record<string, number> = { VN: 1.10, US: 1.07, EU: 1.20 };
function priceSoft(amount: number, country: string): number {
  const rate = VAT[country] ?? 1.0;
  return Math.round(amount * rate);
}

// hôm nay: hành vi hai bản GIỐNG HỆT
for (const c of ["VN", "US", "EU", "XX"]) {
  assert.equal(priceRigid(1000, c), priceSoft(1000, c));
}
console.log("hành vi hôm nay khớp:", ["VN", "US", "EU", "XX"].map((c) => priceSoft(1000, c)));

// ngày mai yêu cầu đổi: thêm "JP" thuế 10%
VAT["JP"] = 1.10; // bản MỀM: thêm 1 dòng dữ liệu
console.log("thêm JP vào bản mềm :", priceSoft(1000, "JP"), "(chạy ngay)");
console.log("bản CỨNG với JP     :", priceRigid(1000, "JP"), "(trả như 'không thuế' — phải SỬA CODE)");
```

Kết quả chạy thật:

```
hành vi hôm nay khớp: [ 1100, 1070, 1200, 1000 ]
thêm JP vào bản mềm : 1100 (chạy ngay)
bản CỨNG với JP     : 1000 (trả như 'không thuế' — phải SỬA CODE)
```

Hôm nay hai bản khớp từng số — *hành vi* như nhau. Nhưng khi yêu cầu "thêm Nhật" tới: bản *mềm* chỉ thêm một dòng dữ liệu là đúng (1100); bản *cứng* trả 1000 (như thể không thuế) cho tới khi có người *mổ code*. Cùng một **phạm vi** thay đổi bé tí, nhưng **hình dạng** của bản cứng khiến nó đắt. Cấu trúc tốt chính là thứ giữ cái giá ấy luôn thấp.

> [!note] Tự thử
>
> 1. Thêm "KR" thuế 10% vào *cả hai* bản. Bản nào bạn sửa trong **dữ liệu**, bản nào buộc sửa **logic**?
> 2. Đổi thuế VN từ 10% xuống 8%. Đếm số chỗ phải chạm ở mỗi bản.
> 3. Tưởng tượng 50 nước. Bản cứng dài bao nhiêu `else if`? Đây là "chữ ký mớ hỗn độn" ở mục 1 nảy mầm.

## 6. Giá trị nào lớn hơn? Ma trận Eisenhower

Hành vi hay cấu trúc quan trọng hơn? Quản lý nghiệp vụ (và cả nhiều dev) thường chọn "chạy được quan trọng hơn". Uncle Bob chứng minh đó là *thái độ sai* bằng cách xét hai cực:


| Cho tôi một chương trình…             | Thì…                                             | Kết cục              |
| :------------------------------------- | :------------------------------------------------ | :-------------------- |
| chạy hoàn hảo nhưng **không thể đổi** | yêu cầu đổi → hết chạy đúng, không sửa nổi       | **vô dụng**          |
| **chưa chạy** nhưng **dễ đổi**        | tôi làm cho nó chạy, giữ nó chạy khi yêu cầu đổi | **hữu dụng lâu dài** |


> [!quote] Ch. 2 — The Greater Value (tr. 15)
> "If you give me a program that works perfectly but is impossible to change, then it won't work when the requirements change, and I won't be able to make it work. Therefore the program will become useless."
>
> *Cho tôi một chương trình chạy hoàn hảo nhưng **không thể thay đổi**, thì khi yêu cầu đổi nó sẽ hết chạy đúng, mà tôi lại không sửa được. Vậy chương trình sẽ thành **vô dụng**.*

Để sắp ưu tiên, ông mượn **ma trận Eisenhower** (quan trọng vs khẩn cấp). Eisenhower nói: "Tôi có hai loại vấn đề, khẩn và quan trọng. Cái khẩn thì không quan trọng, cái quan trọng thì không bao giờ khẩn."

```
                 KHẨN CẤP              KHÔNG KHẨN CẤP
              ┌─────────────────────┬──────────────────────┐
  QUAN TRỌNG  │  1. khẩn +          │  2. KHÔNG khẩn +     │
              │     quan trọng      │     QUAN TRỌNG       │
              │                     │   ← KIẾN TRÚC ở đây  │
              ├─────────────────────┼──────────────────────┤
  KHÔNG       │  3. khẩn, KHÔNG     │  4. không khẩn,      │
  QUAN TRỌNG  │     quan trọng      │     không quan trọng │
              └─────────────────────┴──────────────────────┘
```

Xếp bốn ô thành thứ tự ưu tiên, và đặt hai giá trị phần mềm vào:


| Ưu tiên | Ô (khẩn / quan trọng)        | Giá trị phần mềm rơi vào đây                   |
| :-------: | :---------------------------- | :---------------------------------------------- |
| 1       | khẩn **+** quan trọng        | một phần **hành vi** cốt + kiến trúc cấp thiết |
| 2       | không khẩn **+** quan trọng  | **← CẤU TRÚC (kiến trúc)**                     |
| 3       | khẩn, không quan trọng       | phần lớn **hành vi**/tính năng                 |
| 4       | không khẩn, không quan trọng | —                                              |


> [!quote] Ch. 2 — Eisenhower's Matrix (tr. 16)
> "The first value of software—behavior—is urgent but not always particularly important. The second value of software—architecture—is important but never particularly urgent."
>
> *Giá trị thứ nhất — hành vi — thì **khẩn** nhưng không phải lúc nào cũng quan trọng. Giá trị thứ hai — kiến trúc — thì **quan trọng** nhưng không bao giờ khẩn.*

Sai lầm kinh điển: nâng các việc ở **ô 3** (khẩn, không quan trọng) lên thành **ô 1**, rồi bỏ bê kiến trúc ở ô 2. Và vì quản lý nghiệp vụ *không đủ chuyên môn* để đánh giá tầm quan trọng của kiến trúc:

> [!quote] Ch. 2 — Eisenhower's Matrix (tr. 17)
> "it is the responsibility of the software development team to assert the importance of architecture over the urgency of features."
>
> *trách nhiệm của đội phát triển là **khẳng định tầm quan trọng của kiến trúc** trước sự khẩn cấp của tính năng.*

(Đây là tiếng vọng của [`clean-coder` Bài 2 — Nói Không](../../clean-coder/bai_hoc/bai_02_noi_khong.md): bảo vệ cái đúng về kỹ thuật là việc của bạn, không phải của sếp.)

## 7. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Luận đề "hai giá trị" **bất tử** — nó đúng với mọi mô hình kiến trúc, mọi thời. Nhưng vài sắc thái năm 2026 đáng thêm:
>
> - **"Kiến trúc quan trọng hơn hành vi" — đúng, nhưng dễ bị lạm dụng.** Phe over-engineering hay trích câu này để biện minh cho việc vẽ vời kiến trúc phức tạp *trước khi có hành vi nào*. Cân bằng 2026 (ponytail): với app nhỏ, prototype, hay thứ có thể chết trong sáu tháng — "cấu trúc" tối giản là *đủ*. Uncle Bob nói kiến trúc phải *giữ ngỏ lựa chọn*, không phải *quyết sẵn mọi thứ*. Đừng xây cathedral cho một cái lều.
> - **"Chi phí đổi tỉ lệ scope, không phải shape"** là ý cốt lõi còn nguyên giá trị, và chính là cái mà *evolutionary architecture* (Neal Ford) + *fitness function* đo lường năm 2026.
> - **"The only way to go fast is to go well" (tr. 10)** — càng đúng trong kỷ nguyên AI: AI sinh *hành vi* (ô 1/3) rẻ chưa từng thấy, khiến *cấu trúc* (ô 2) — thứ AI chưa làm tốt — thành chỗ lập trình viên còn giá trị nhất. Nối [`clean-code` Bài 13](../../clean-code/bai_hoc/bai_13_xem_code_nay_sinh.md).
> - **Số "40 lần" và các đồ thị**: minh hoạ vẫn đắt, nhưng đây là một ca ẩn danh, không phải nghiên cứu đối chứng diện rộng — đọc như một *câu chuyện cảnh báo*, không phải bằng chứng thống kê. (Thí nghiệm TDD của Gorman cũng là mẫu nhỏ, một người.)

## 8. Áp dụng vào dự án của bạn

> [!question] Ba việc trước khi sang Bài 1
>
> 1. **Đo "shape vs scope".** Nhớ lần gần nhất một yêu cầu *nghe* đơn giản mà sửa lại *rất* lâu. Vì sao? Có phải hình dạng hệ thống không khớp hình dạng yêu cầu (như `priceRigid`)?
> 2. **Định vị trên ma trận Eisenhower.** Liệt kê 5 việc đội bạn đang làm, xếp mỗi việc vào 1 trong 4 ô. Có việc "khẩn nhưng không quan trọng" (ô 3) nào đang chiếm chỗ của kiến trúc (ô 2)?
> 3. **Tìm một "lời nói dối".** Dự án bạn có câu "dọn sau, giờ phải kịp ra mắt" không? Ghi lại một chỗ bạn định "dọn sau" — cuối khoá đối chiếu xem "sau" đã tới chưa.

## 9. Từ điển thuật ngữ


| Thuật ngữ                 | Nghĩa trong khoá                                                                   |
| :------------------------- | :---------------------------------------------------------------------------------- |
| **Design = Architecture** | Không có ranh giới giữa hai từ; một dải liên tục từ mức cao tới chi tiết (tr. 3).  |
| **Goal of architecture**  | Tối thiểu hoá nhân lực để xây **và** bảo trì hệ thống (tr. 4).                     |
| **Signature of a mess**   | Hình dạng đồ thị năng suất tụt / chi phí vọt của một hệ bị bỏ bê cấu trúc (tr. 6). |
| **Behavior (hành vi)**    | Giá trị thứ nhất: máy chạy đúng yêu cầu — khẩn, không luôn quan trọng (tr. 13).    |
| **Structure (cấu trúc)**  | Giá trị thứ hai: giữ phần mềm "mềm", dễ đổi — quan trọng, không khẩn (tr. 13).     |
| **Shape vs scope**        | Độ khó thay đổi nên tỉ lệ với *phạm vi*, không với *hình dạng* hệ thống (tr. 14).  |
| **Eisenhower matrix**     | Khẩn vs quan trọng; kiến trúc ở ô "quan trọng, không khẩn" (tr. 16).               |


## 10. Câu hỏi tự kiểm tra

1. Vì sao Uncle Bob nói design và architecture *không* khác nhau? *(tr. 3)*
2. Phát biểu "mục tiêu của kiến trúc" và cách đo chất lượng thiết kế. *(tr. 4)*
3. Ngụ ngôn Rùa và Thỏ minh hoạ "lời nói dối" nào của lập trình viên? *(tr. 9)*
4. Hai giá trị của phần mềm là gì? Điền vào bảng: cái nào khẩn, cái nào quan trọng? *(tr. 13, 16)*
5. "Shape vs scope" nghĩa là gì? `priceRigid` minh hoạ ra sao? *(tr. 14, mục 5)*
6. Vì sao khẳng định tầm quan trọng của kiến trúc là việc của *đội dev*, không phải của sếp? *(tr. 17)*

## Tóm tắt một trang

```
BÀI 0 — HAI GIÁ TRỊ: HÀNH VI VÀ CẤU TRÚC
─────────────────────────────────────────────────────────
CASE STUDY  code release 8 đắt GẤP 40 LẦN release 1 (tr.5);
          lương đội lên ~$20tr/tháng mà gần như 0 tính năng
          = "chữ ký của một mớ hỗn độn" (tr.6). Không ai lười.

DESIGN = ARCHITECTURE  không ranh giới (tr.3). Mục tiêu:
          TỐI THIỂU NHÂN LỰC xây + bảo trì (tr.4).

RÙA & THỎ  lời nói dối "dọn sau, ra mắt trước đã" (tr.9).
          "bày bừa LUÔN chậm hơn giữ sạch" (tr.9).
          "the only way to go fast is to go well" (tr.10).

HAI GIÁ TRỊ (tr.13)
   HÀNH VI  : máy chạy đúng — KHẨN, không luôn quan trọng
   CẤU TRÚC : phần mềm "mềm", dễ đổi — QUAN TRỌNG, không khẩn
   shape vs scope: độ khó đổi nên tỉ lệ SCOPE, không SHAPE (tr.14)

priceRigid vs priceSoft: cùng hành vi hôm nay; thêm "JP" →
   mềm thêm 1 dòng chạy ngay, cứng phải MỔ CODE.

GIÁ TRỊ LỚN HƠN = CẤU TRÚC: "chạy hoàn hảo mà không đổi được →
   vô dụng" (tr.15). Eisenhower: kiến trúc ở ô 2 (quan trọng,
   không khẩn). ĐỪNG nâng ô 3 lên ô 1. Khẳng định kiến trúc
   là việc của ĐỘI DEV (tr.17).

2026  luận đề bất tử. Đừng lạm dụng để over-engineer app nhỏ
   (giữ ngỏ lựa chọn ≠ quyết sẵn tất cả). AI làm hành vi rẻ →
   cấu trúc càng là chỗ dev còn giá trị.
```

## Nguồn

- **Robert C. Martin**, *Clean Architecture: A Craftsman's Guide to Software Structure and Design* (Prentice Hall, 2017) — **Chương 1, "What Is Design and Architecture?"** (`tr. 3–11`): design=architecture (tr. 3); mục tiêu kiến trúc (tr. 4); case study code đắt gấp 40 lần, chữ ký mớ hỗn độn, góc nhìn executive (tr. 5–8); Rùa và Thỏ, lời nói dối "dọn sau", "bày bừa luôn chậm hơn", thí nghiệm TDD của Gorman, "the only way to go fast is to go well" (tr. 9–11). **Chương 2, "A Tale of Two Values"** (`tr. 13–17`): hai giá trị hành vi/cấu trúc (tr. 13); "software phải mềm", shape vs scope (tr. 13–14); giá trị lớn hơn, xét hai cực (tr. 15); ma trận Eisenhower, trách nhiệm của đội dev (tr. 16–17). `tai_lieu/Clean.Architecture.2017.9.pdf`
- Bối cảnh 2026 dẫn từ ngoài sách: evolutionary architecture (Neal Ford); tranh luận over-engineering; AI sinh code.
- Quy ước trích: `tr. X` = số trang in trong sách; trang tệp PDF = `X + 27`.

---

**Bản đồ khoá học:** [Bài 0 ← bạn đang ở đây] · [Bài 1 — Ba hệ hình lập trình](bai_01_he_hinh_lap_trinh.md) · [Bài 2 — SOLID (1): SRP, OCP](bai_02_solid_srp_ocp.md) · [Bài 3 — SOLID (2): LSP, ISP, DIP](bai_03_solid_lsp_isp_dip.md) · [Bài 4 — Nguyên tắc Component](bai_04_nguyen_tac_component.md) · [Bài 5 — Kiến trúc là gì &amp; Độc lập](bai_05_kien_truc_va_doc_lap.md) · [Bài 6 — Ranh giới &amp; Dependency Rule](bai_06_ranh_gioi_dependency_rule.md) · [Bài 7 — Business Rules &amp; The Clean Architecture](bai_07_clean_architecture.md) · [Bài 8 — Humble Object, Main, Services](bai_08_humble_main_services.md) · [Bài 9 — Chi tiết: DB, Web, Framework](bai_09_chi_tiet.md) · [Bài 10 — The Missing Chapter: đóng gói](bai_10_dong_goi.md) · [Bài 11 — Case study &amp; tổng kết](bai_11_case_study.md)

Xem thêm [README khoá học](../README.md).