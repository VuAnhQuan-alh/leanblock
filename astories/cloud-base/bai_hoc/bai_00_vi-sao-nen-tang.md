# Bài 0 — Vì sao cần kiến thức nền, và bản đồ bốn trụ

> [!info] Về bài này
> Khoá **`cloud-base`** là *nền tảng cho cloud* — curate từ **5 cuốn kinh điển** để hiểu **sâu** điều mà khoá [`aws-fund`](../../aws-fund/README.md) chỉ dùng được ở bề mặt. Tổ chức **bottom-up theo bốn trụ**: OS → Mạng → Distributed Systems → Dữ liệu.
> Nguồn (trích nguyên văn — Luật số 1, không viết theo trí nhớ):
> - **OSTEP** — *Operating Systems: Three Easy Pieces* (Remzi & Andrea Arpaci-Dusseau)
> - **Kurose** — *Computer Networking: A Top-Down Approach, 8th* (Kurose & Ross)
> - **HPBN** — *High Performance Browser Networking* (Ilya Grigorik)
> - **UDS** — *Understanding Distributed Systems, 2nd* (Roberto Vitillo)
> - **DDIA** — *Designing Data-Intensive Applications* (Martin Kleppmann)
>
> Trích theo `[Mã sách] tr. X` (số trang **in trong sách**; mỗi cuốn một offset PDF, ghi ở mục Nguồn). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Mỗi bài có hộp **"Nối về AWS"** cross-link `aws-fund`: *đây chính là vì sao dịch vụ X hành xử như Y*.
>
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: cơn bão buzzword](#1-mở-đầu-cơn-bão-buzzword)
2. [Luận đề: nguyên tắc bền hơn công cụ](#2-luận-đề-nguyên-tắc-bền-hơn-công-cụ)
3. [Demo: abstraction rò rỉ ở đâu — bậc thang độ trễ](#3-demo-abstraction-rò-rỉ-ở-đâu--bậc-thang-độ-trễ)
4. [Bản đồ bốn trụ](#4-bản-đồ-bốn-trụ)
5. [Phương pháp học & quy ước "Nối về AWS"](#5-phương-pháp-học--quy-ước-nối-về-aws)
6. [Thẻ ôn (active recall)](#6-thẻ-ôn-active-recall)
7. [Câu hỏi tự kiểm tra](#7-câu-hỏi-tự-kiểm-tra)
8. [Tóm tắt một trang](#tóm-tắt-một-trang)
9. [Nguồn](#nguồn)

---

## 1. Mở đầu: cơn bão buzzword

Nếu bạn làm backend vài năm gần đây, hẳn đã bị *dội bom* bởi một rừng từ khoá — đúng như Kleppmann mở đầu DDIA:

> [!quote] DDIA — Preface
> "you have probably been bombarded with a plethora of buzzwords relating to storage and processing of data. NoSQL! Big Data! Web-scale! Sharding! Eventual consistency! ACID! CAP theorem! Cloud services! MapReduce! Real-time!"
>
> *bạn hẳn đã bị **dội bom** bởi vô số buzzword về lưu trữ và xử lý dữ liệu. NoSQL! Big Data! Web-scale! Sharding! Eventual consistency! ACID! CAP theorem! Cloud services! MapReduce! Real-time!*

Để ý: *Eventual consistency, Sharding, CAP theorem, Cloud services* — chính là những thứ bạn đã *dùng* ở `aws-fund` (DynamoDB, S3, Multi-AZ) mà chưa *hiểu* bên dưới. Buzzword là dấu hiệu của hào hứng, nhưng để xây hệ tốt, phải đào sâu hơn nó.

## 2. Luận đề: nguyên tắc bền hơn công cụ

Đây là lý do cả khoá tồn tại — và là câu trả lời cho câu hỏi *"muốn hiểu sâu có cần nền không?"*:

> [!quote] DDIA — Preface
> "as software engineers and architects, we also need to have a technically accurate and precise understanding of the various technologies and their trade-offs if we want to build good applications. For that understanding, we have to dig deeper than buzzwords."
>
> *là kỹ sư và kiến trúc sư, ta cần **hiểu chính xác về mặt kỹ thuật** các công nghệ và **đánh đổi** của chúng nếu muốn xây hệ tốt. Để hiểu được vậy, ta **phải đào sâu hơn buzzword**.*

Và phần thưởng của việc đào sâu — **tính bền**:

> [!quote] DDIA — Preface
> "behind the rapid changes in technology, there are enduring principles that remain true, no matter which version of a particular tool you are using. If you understand those principles, you're in a position to see where each tool fits in, how to make good use of it, and how to avoid its pitfalls."
>
> *sau những thay đổi chóng mặt của công nghệ, có những **nguyên tắc trường tồn** đúng mãi, bất kể bạn dùng phiên bản nào của một công cụ. Hiểu chúng rồi, bạn **thấy mỗi công cụ hợp ở đâu, dùng sao cho đúng, và tránh cạm bẫy của nó**.*

Đây chính là insight cốt lõi: **mỗi dịch vụ AWS = một khái niệm CS nền tảng được "đóng gói managed"**. AWS đổi UI/dịch vụ liên tục, nhưng *CAP theorem, TCP, process scheduling* thì 20 năm nữa vẫn đúng. Học nền = **đầu tư nhớ-lâu nhất**: nó vừa giúp hiểu AWS hôm nay, vừa còn giá trị khi AWS đã khác.

## 3. Demo: abstraction rò rỉ ở đâu — bậc thang độ trễ

Abstraction *luôn rò rỉ đúng chỗ cái nền cắn vào*. Thứ "cắn" đau nhất — và là lý do cả ba trụ OS/Mạng/Distributed tồn tại — là **độ trễ không đồng đều** giữa các tầng. Đo thật: một thao tác trong RAM so với một round-trip mạng (dù chỉ localhost):

```typescript
import { performance } from "node:perf_hooks";
import http from "node:http";

// (1) thao tác trong BỘ NHỚ: cộng 50 triệu phần tử
const N = 50_000_000;
const arr = new Float64Array(8);
let t = performance.now();
let s = 0;
for (let i = 0; i < N; i++) s += arr[i & 7];
const memNs = ((performance.now() - t) * 1e6) / N; // ns mỗi thao tác

// (2) một VÒNG round-trip MẠNG (localhost HTTP)
function ping(): Promise<number> {
  return new Promise((resolve) => {
    const start = performance.now();
    const req = http.get({ host: "127.0.0.1", port: 4566, path: "/_localstack/health" }, (res) => {
      res.on("data", () => {}); res.on("end", () => resolve(performance.now() - start));
    });
    req.on("error", () => resolve(-1));
  });
}
let net = await ping(); net = await ping(); // bỏ lần đầu (ấm máy)
const netNs = net * 1e6;

console.log(`(1) thao tác bộ nhớ (RAM)     : ~${memNs.toFixed(2)} ns`);
console.log(`(2) round-trip mạng localhost : ~${(netNs/1e6).toFixed(2)} ms  = ~${Math.round(netNs/memNs).toLocaleString("en")}x chậm hơn RAM`);
console.log(`\nQuy đổi sang thang CON NGƯỜI (1 thao tác RAM = 1 giây):`);
console.log(`  RAM            : 1 giây`);
console.log(`  mạng localhost : ~${Math.round(netNs/memNs).toLocaleString("en")} giây  (~${(netNs/memNs/86400).toFixed(1)} ngày)`);
console.log(`  (mạng cross-region ~70ms còn gấp thêm chục lần nữa)`);
```

Kết quả chạy thật *(cần LocalStack đang chạy ở cổng 4566; con số tùy máy/lần chạy — điều quan trọng là **bậc độ lớn**)*:

```
(1) thao tác bộ nhớ (RAM)     : ~0.67 ns
(2) round-trip mạng localhost : ~1.97 ms  = ~2,941,792x chậm hơn RAM

Quy đổi sang thang CON NGƯỜI (1 thao tác RAM = 1 giây):
  RAM            : 1 giây
  mạng localhost : ~2,941,792 giây  (~34.0 ngày)
  (mạng cross-region ~70ms còn gấp thêm chục lần nữa)
```

Một round-trip mạng chậm hơn một thao tác RAM **~triệu lần**. Quy sang thang người: nếu truy cập RAM là *1 giây*, thì một lời gọi mạng là *~34 ngày*. Đây là *fact nền tảng số một* của cloud, và nó giải thích gần như mọi quyết định kiến trúc:

- vì sao **cache** (giữ dữ liệu gần hơn) quan trọng đến thế,
- vì sao **cold start** (Lambda phải kéo code qua mạng + dựng container) tốn hàng trăm ms,
- vì sao hệ **distributed** phải chịu đựng *độ trễ + thất bại* của mạng (trụ 3),
- vì sao **CDN** (CloudFront) đẩy nội dung tới rìa gần người dùng.

> [!note] Nối về AWS
> Bậc thang này là *vì sao* nhiều cạm bẫy ở `aws-fund` tồn tại: [cold start của Lambda](../../aws-fund/bai_hoc/bai_02_compute.md) (mạng + khởi tạo container), [CloudFront cache](../../aws-fund/bai_hoc/bai_05_networking.md) (né round-trip xa), và toàn bộ messaging ([SQS/SNS](../../aws-fund/bai_hoc/bai_04_messaging.md) — ghép nối rời vì mạng *sẽ* chậm và *sẽ* hỏng).

## 4. Bản đồ bốn trụ

Khoá xây **bottom-up** — càng xuống dưới càng *bền* (ít đổi theo thời gian), và tầng trên dựa trên tầng dưới:

```
   Ứng dụng cloud  —  mỗi dịch vụ AWS = "managed [khái niệm nền]"
   (EC2 · S3 · DynamoDB · Lambda · API Gateway · SQS · CloudFront ...)
   ════════════════════════════════════════════════════════════════════════════════════════
   trụ 4 · DỮ LIỆU         storage engine, SQL/NoSQL, index, batch/stream   (DDIA)
   trụ 3 · DISTRIBUTED     nhân bản, nhất quán (CAP), phân mảnh, consensus   (DDIA, UDS)
   trụ 2 · MẠNG            HTTP/DNS, TCP/UDP/TLS, latency, HTTP2/QUIC, CDN   (Kurose, HPBN)
   trụ 1 · OS & ẢO HOÁ     process, bộ nhớ, concurrency, I/O & lưu trữ       (OSTEP)
   ════════════════════════════════════════════════════════════════════════════════════════
            ▲ càng xuống BỀN hơn (TCP/CAP 20 năm nữa vẫn đúng)
```

Trụ nền nhất là OS. Nó được tổ chức quanh **ba mảnh**:

> [!quote] OSTEP — Preface
> "The three easy pieces refer to the three major thematic elements the book is organized around: virtualization, concurrency, and persistence."
>
> *"Ba mảnh dễ" chỉ ba chủ đề lớn mà cuốn sách xoay quanh: **ảo hoá (virtualization), đồng thời (concurrency), và lưu trữ bền (persistence)**.*

Ba mảnh đó chính là ba bài đầu của khoá (Bài 1–3): ảo hoá (process/CPU/memory → EC2/Lambda), concurrency (→ race, idempotency), persistence (I/O & filesystem → EBS/S3). Rồi leo lên Mạng (Bài 4–6), Distributed (Bài 7–9), Dữ liệu (Bài 10–11).

## 5. Phương pháp học & quy ước "Nối về AWS"

Khoá giữ nguyên bộ **nhớ-lâu** đã dùng ở [`aws-fund` Bài 0](../../aws-fund/bai_hoc/bai_00_hoc-aws-nho-lau-va-localstack.md) — vì nó hiệu quả: **active recall** (thẻ ôn, tự trả lời trước khi xem), **spaced repetition** (ôn giãn cách), **decision/so-sánh tables**, **generation effect** (demo chạy được), và **elaboration** (Feynman: tự giải thích lại trong 3 câu).

Điểm khác biệt của khoá này là **hộp "Nối về AWS"** cuối mỗi khái niệm: nó *neo* kiến thức nền trừu tượng vào một *hiện tượng AWS cụ thể* bạn đã gặp — đây là **elaboration mạnh nhất**: kiến thức mới (nền) treo vào kiến thức cũ (AWS), hai chiều cùng khắc sâu.

> [!note] Cách đọc khoá cho hiệu quả
> - **Học xen kẽ với `aws-fund`.** Mỗi khi gặp "Nối về AWS", mở lại bài AWS tương ứng — bạn sẽ thấy nó *sáng ra*.
> - **Đừng cố nhớ hết 5 cuốn.** Khoá đã curate phần *làm cloud sáng ra*; muốn sâu hơn nữa thì đọc thẳng cuốn gốc (mục Nguồn chỉ rõ chương).
> - **Gõ lại demo**, đừng chỉ đọc. Bậc thang độ trễ chỉ "thấm" khi bạn tự chạy và thấy con số.

## 6. Thẻ ôn (active recall)

> [!question] Thẻ 0.1 — Vì sao học nền tảng là đầu tư "nhớ lâu" nhất?
> **Đáp:** nguyên tắc nền (TCP, CAP, scheduling) *trường tồn* bất kể phiên bản công cụ; AWS đổi liên tục nhưng nền thì không. Hiểu nền → thấy mỗi công cụ hợp ở đâu + tránh cạm bẫy.

> [!question] Thẻ 0.2 — "Mỗi dịch vụ AWS = ?" theo luận đề của khoá.
> **Đáp:** = một khái niệm CS nền tảng được "đóng gói managed". Hiểu sâu = thấy cái bên dưới (abstraction rò rỉ đúng chỗ nền cắn vào).

> [!question] Thẻ 0.3 — Fact nền số một: round-trip mạng chậm hơn RAM cỡ nào?
> **Đáp:** ~**triệu lần** (RAM ~nanosecond, mạng ~mili-giây). Thang người: 1 giây vs ~tháng. → cache, CDN, decouple, cold start đều từ đây.

> [!question] Thẻ 0.4 — Ba mảnh của OS (OSTEP)?
> **Đáp:** virtualization (ảo hoá), concurrency (đồng thời), persistence (lưu trữ bền).

> [!question] Thẻ 0.5 — Bốn trụ của khoá, từ dưới lên?
> **Đáp:** OS & ảo hoá → Mạng → Distributed systems → Dữ liệu. Càng dưới càng bền.

## 7. Câu hỏi tự kiểm tra

1. Vì sao "đào sâu hơn buzzword" lại cần cho việc xây hệ tốt? *(DDIA Preface)*
2. "Nguyên tắc trường tồn" nghĩa là gì, và vì sao nó làm kiến thức nền đáng học? *(mục 2)*
3. Giải thích bậc thang độ trễ. Kể ba quyết định kiến trúc *sinh ra từ* nó. *(mục 3)*
4. Kể bốn trụ bottom-up và một ví dụ AWS mỗi trụ mở khoá. *(mục 4)*
5. Ba mảnh của OS là gì? Chúng ứng với ba bài đầu ra sao? *(OSTEP Preface)*

## Tóm tắt một trang

```
BÀI 0 — VÌ SAO CẦN NỀN + BẢN ĐỒ BỐN TRỤ
─────────────────────────────────────────────────────────
BUZZWORD  "bị dội bom NoSQL/CAP/eventual consistency/cloud..." (DDIA).
   Chính thứ bạn DÙNG ở aws-fund mà chưa HIỂU bên dưới.

LUẬN ĐỀ  "phải đào sâu hơn buzzword" (DDIA). Phần thưởng: "nguyên tắc
   TRƯỜNG TỒN bất kể phiên bản công cụ" (DDIA). Mỗi dịch vụ AWS =
   "managed [khái niệm nền]". Học nền = đầu tư NHỚ-LÂU nhất.

DEMO BẬC THANG ĐỘ TRỄ  RAM ~0.67ns vs mạng ~2ms = ~TRIỆU LẦN chậm.
   Thang người: 1 giây vs ~34 ngày. → cache, CDN, decouple, cold start.

BỐN TRỤ (bottom-up, càng dưới càng bền):
   1 OS & ảo hoá (OSTEP) — 3 mảnh: virtualization/concurrency/persistence
   2 Mạng (Kurose, HPBN)
   3 Distributed systems (DDIA, UDS)
   4 Dữ liệu (DDIA)

PHƯƠNG PHÁP  giữ bộ nhớ-lâu của aws-fund + hộp "NỐI VỀ AWS" mỗi khái
   niệm (elaboration: nền trừu tượng neo vào hiện tượng AWS cụ thể).
```

## Nguồn

- **Martin Kleppmann**, *Designing Data-Intensive Applications* (O'Reilly, 2017) — **Preface**: cơn bão buzzword, "dig deeper than buzzwords", "enduring principles that remain true no matter which version of a tool". `tai_lieu/Designing Data Intensive Applications by Martin Kleppmann.pdf`
- **Remzi H. & Andrea C. Arpaci-Dusseau**, *Operating Systems: Three Easy Pieces* — **Preface**: ba mảnh virtualization/concurrency/persistence. `tai_lieu/Operating systems three easy pieces.pdf`
- Các cuốn trụ còn lại dùng ở bài sau: **Kurose & Ross** *Computer Networking: A Top-Down Approach 8th* (mạng); **Ilya Grigorik** *High Performance Browser Networking* (mạng/hiệu năng); **Roberto Vitillo** *Understanding Distributed Systems 2nd* (distributed).
- Phương pháp học: xem [`aws-fund` Bài 0](../../aws-fund/bai_hoc/bai_00_hoc-aws-nho-lau-va-localstack.md) (active recall, spaced repetition, generation effect, elaboration).
- Quy ước trích: `[Mã sách] tr. X` = số trang in; offset PDF mỗi cuốn ghi ở bài dùng tới (preface dùng số La Mã, không auto-verify).

---

**Bản đồ khoá học — lõi:** **[Bài 0 — Vì sao cần nền] ← bạn đang ở đây** · [Bài 1 — OS: ảo hoá](bai_01_os-ao-hoa.md) · [Bài 2 — OS: concurrency](bai_02_os-concurrency.md) · [Bài 3 — OS: lưu trữ](bai_03_os-luu-tru.md) · [Bài 4 — Mạng: phân tầng, HTTP, DNS](bai_04_mang-http-dns.md) · [Bài 5 — Mạng: TCP, TLS](bai_05_mang-tcp-tls.md) · [Bài 6 — Mạng: hiệu năng, CDN](bai_06_mang-hieu-nang.md) · [Bài 7 — Distributed: giao tiếp & thất bại](bai_07_dist-giao-tiep.md) · [Bài 8 — Distributed: nhân bản & nhất quán](bai_08_dist-nhat-quan.md) · [Bài 9 — Distributed: phân mảnh & consensus](bai_09_dist-phan-manh.md) · [Bài 10 — Dữ liệu: storage engine](bai_10_du-lieu-storage.md) · [Bài 11 — Dữ liệu: batch & stream](bai_11_du-lieu-batch-stream.md)

**Chuyên đề nâng cao:** [Bài 12 — OS nâng cao: bộ nhớ ảo](bai_12_os-bo-nho-ao.md) · [Bài 13 — OS nâng cao: scheduling & locks](bai_13_os-scheduling-locks.md) · [Bài 14 — Mạng nâng cao: bảo mật & mật mã](bai_14_mang-bao-mat.md) · [Bài 15 — Distributed nâng cao: đồng hồ](bai_15_dist-dong-ho.md) · [Bài 16 — Distributed nâng cao: transaction & saga](bai_16_dist-transaction-saga.md) · [Bài 17 — Dữ liệu nâng cao: data models](bai_17_du-lieu-data-models.md) · [Bài 18 — Dữ liệu nâng cao: encoding & schema](bai_18_du-lieu-encoding.md)

Xem thêm [README khoá học](../README.md).
