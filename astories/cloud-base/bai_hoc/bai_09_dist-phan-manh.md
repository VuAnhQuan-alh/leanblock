# Bài 9 — Distributed trụ 3c: Phân mảnh và consensus

> [!info] Về bài này
> **Trụ 3 (Distributed Systems), mảnh 3/3 — khép trụ Distributed.** [Bài 8](bai_08_dist-nhat-quan.md) nhân bản để *chịu lỗi* và *giảm latency*. Nhưng nhân bản không giải quyết được *một* vấn đề: dữ liệu **quá lớn cho một máy**. Lời giải là **phân mảnh (sharding)** — và nó đặt ra bài toán đối ngẫu: khi nhiều node phải **đồng ý** một quyết định (ai giữ ghế cuối, node nào là leader), ta cần **consensus**. Đây là nền của **partition key của DynamoDB, cơ chế bầu leader, và vì sao chọn sai khoá phân mảnh gây hot partition** ở `aws-fund`.
> Nguồn: **DDIA** (ch. 6 Partitioning, ch. 9 Consensus).
> **Trích:** `DDIA (tr. X)` offset **+22**. Câu chốt nguyên văn trong `[!quote]`.
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`).
> Nên đọc trước: [Bài 8 — nhân bản & nhất quán](bai_08_dist-nhat-quan.md).

## Mục lục

1. [Phân mảnh (sharding): chia dữ liệu quá lớn](#1-phân-mảnh-sharding-chia-dữ-liệu-quá-lớn)
2. [Hash vs range: trải đều hay hot spot](#2-hash-vs-range-trải-đều-hay-hot-spot)
3. [Consensus: nhiều node đồng ý một giá trị](#3-consensus-nhiều-node-đồng-ý-một-giá-trị)
4. [Demo: sharding và quorum giành ghế cuối](#4-demo-sharding-và-quorum-giành-ghế-cuối)
5. [Bảng so sánh: nhân bản vs phân mảnh](#5-bảng-so-sánh-nhân-bản-vs-phân-mảnh)
6. [Nối về AWS](#6-nối-về-aws)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Phân mảnh (sharding): chia dữ liệu quá lớn

Nhân bản (Bài 8) đặt *cùng* dữ liệu lên nhiều máy. Phân mảnh làm điều ngược lại: đặt *các phần khác nhau* của dữ liệu lên các máy khác nhau.

> [!quote] DDIA (tr. 199)
> "For very large datasets, or very high query throughput, that is not sufficient: we need to break the data up into partitions, also known as sharding."
>
> *Với tập dữ liệu **rất lớn**, hoặc throughput truy vấn **rất cao**, (nhân bản) là **không đủ**: ta cần **chia dữ liệu thành các partition**, còn gọi là **sharding (phân mảnh)**.*

Lý do cốt lõi, DDIA nói thẳng:

> [!quote] DDIA (tr. 199)
> "The main reason for wanting to partition data is scalability. Different partitions can be placed on different nodes in a shared-nothing cluster."
>
> *Lý do chính để phân mảnh dữ liệu là **khả năng mở rộng (scalability)**. Các partition khác nhau có thể đặt trên **các node khác nhau** trong một cụm shared-nothing.*

Nhân bản và phân mảnh là **hai trục độc lập** (bảng mục 5): nhân bản chống *mất dữ liệu*, phân mảnh chống *quá tải một máy*. Hệ thực tế dùng cả hai — mỗi shard lại được nhân bản. Nhưng phân mảnh có một cạm bẫy riêng mà nhân bản không có: **chia sao cho đều**.

## 2. Hash vs range: trải đều hay hot spot

Chìa khoá của phân mảnh là *quy tắc* quyết định mỗi mẩu dữ liệu về node nào. Hai họ phổ biến:

- **Partition theo range (khoảng):** chia theo khoảng khoá liền mạch (vd. tên A–I → node 0, J–R → node 1...). Ưu: quét khoảng (range scan) nhanh. Nhược: dễ **lệch** nếu khoá dồn cục — ví dụ khoá là *timestamp*, mọi ghi mới đều dồn vào partition cuối → một node nóng rực, các node kia ngồi chơi.
- **Partition theo hash:** băm khoá rồi lấy dư → trải đều ngẫu nhiên. Ưu: cân tải tốt. Nhược: mất tính liền mạch (range scan phải hỏi mọi node).

Cái bẫy có tên: **hot spot** (điểm nóng) — một partition nhận phần lớn tải trong khi phần còn lại nhàn. Nó phá tan chính mục tiêu "scalability" của mục 1: thêm node cũng vô ích nếu tải vẫn dồn vào một chỗ. Demo mục 4 cho thấy cùng 12 khoá, hash trải đều còn range (trên khoá dồn cục) thì lệch hẳn về một node.

## 3. Consensus: nhiều node đồng ý một giá trị

Một khi dữ liệu nằm rải trên nhiều node *có thể hỏng* (Bài 7), các node thường phải **cùng đồng ý** một điều: ai là leader, giao dịch này commit hay abort, ai giữ ghế cuối. Đó là consensus:

> [!quote] DDIA (tr. 364)
> "Informally, consensus means getting several nodes to agree on something. For example, if several people concurrently try to book the last seat on an airplane, or the same seat in a theater, or try to register an account with the same username, then a consensus algorithm could be used to determine which one of these mutually incompatible operations should be the winner."
>
> *Nói nôm na, **consensus (đồng thuận)** là làm cho **nhiều node đồng ý một điều gì đó**. Ví dụ, nếu nhiều người **đồng thời** đặt ghế cuối trên máy bay, hay cùng một ghế trong rạp, hay đăng ký cùng một username, thì một **thuật toán consensus** có thể quyết **ai là người thắng** trong các thao tác loại trừ lẫn nhau đó.*

Để ý: đây đúng là **race condition của Bài 2** và **"all or nothing" của atomicity**, nhưng ở quy mô nhiều máy — các thao tác "loại trừ lẫn nhau" cần một người thắng duy nhất. Cách thực dụng để đạt consensus là **quorum** (đa số): một quyết định chỉ có hiệu lực khi **đa số node** đồng ý. Vì hai nhóm "đa số" bất kỳ *luôn giao nhau* (không thể có hai đa số rời nhau trong cùng một cụm), không bao giờ có hai quyết định mâu thuẫn cùng thắng. Demo mục 4 dựng đúng cơ chế này cho "ghế cuối".

## 4. Demo: sharding và quorum giành ghế cuối

Hai phần. (A) chia 12 khoá cho 3 node bằng hash vs range, xem cái nào trải đều. (B) hai client giành ghế cuối trên 3 bản sao; ai được **đa số (2/3)** thì thắng — và không bao giờ cả hai cùng thắng.

```typescript
// Hai ý trụ 3b: (A) PHÂN MẢNH (sharding) — chia dữ liệu quá lớn cho nhiều node;
// (B) CONSENSUS — nhiều node ĐỒNG Ý một giá trị (vd: ai giành ghế cuối).
import { createHash } from "node:crypto";

// ---------- (A) Sharding: hash trải đều, range dễ lệch (hot spot) ----------
const N = 3;
const keys = ["user:alice", "user:amy", "user:ann", "user:bob", "user:ben",
              "user:bill", "user:carol", "user:dave", "user:eve", "user:frank",
              "user:grace", "user:heidi"];

function byHash(k: string): number {
  const h = createHash("sha1").update(k).digest();  // tất định
  return h[0] % N;
}
function byRange(k: string): number {               // theo chữ cái đầu của tên
  const c = k.split(":")[1][0];
  if (c <= "i") return 0; if (c <= "r") return 1; return 2;
}
function spread(fn: (k: string) => number): number[] {
  const count = Array(N).fill(0);
  for (const k of keys) count[fn(k)]++;
  return count;
}
console.log("(A) SHARDING — chia 12 key cho 3 node:");
console.log(`   hash  → node [${spread(byHash).join(", ")}]  (trải khá đều)`);
console.log(`   range → node [${spread(byRange).join(", ")}]  ← lệch: node0 quá tải (hot spot)`);

// ---------- (B) Consensus: 3 bản sao, 2 client giành "ghế cuối" ----------
// Mỗi node cấp ghế cho client ĐẦU TIÊN nó nghe. Ai được ĐA SỐ (>=2/3) thì thắng.
const granted: Array<string | null> = [null, null, null];
function requestSeat(client: string, reachNodes: number[]): number {
  let votes = 0;
  for (const n of reachNodes) {
    if (granted[n] === null) granted[n] = client;   // node cấp cho người đến trước
    if (granted[n] === client) votes++;
  }
  return votes;
}
const votesA = requestSeat("A", [0, 1]);   // A tới node 0,1 trước
const votesB = requestSeat("B", [1, 2]);   // B tới node 1,2 — node1 đã cấp cho A
const majority = Math.floor(N / 2) + 1;    // = 2
console.log("\n(B) CONSENSUS — 2 client giành ghế cuối, cần đa số 2/3:");
console.log(`   client A: ${votesA} phiếu ${votesA >= majority ? "→ THẮNG" : ""}`);
console.log(`   client B: ${votesB} phiếu ${votesB >= majority ? "→ THẮNG" : "→ thua"}`);
console.log(`   node đã cấp: [${granted.join(", ")}]`);
console.log("\nĐa số không thể cấp cho CẢ HAI (2+2>3) → không bao giờ bán trùng ghế.");
```

Kết quả chạy thật *(tất định)*:

```
(A) SHARDING — chia 12 key cho 3 node:
   hash  → node [5, 5, 2]  (trải khá đều)
   range → node [12, 0, 0]  ← lệch: node0 quá tải (hot spot)

(B) CONSENSUS — 2 client giành ghế cuối, cần đa số 2/3:
   client A: 2 phiếu → THẮNG
   client B: 1 phiếu → thua
   node đã cấp: [A, A, B]

Đa số không thể cấp cho CẢ HAI (2+2>3) → không bao giờ bán trùng ghế.
```

Phần (A): 12 khoá đều là tên bắt đầu a–h nên *range* dồn hết vào node 0 (`[12, 0, 0]` — hot spot cực đoan nhưng có thật khi khoá dồn cục), trong khi *hash* băm chúng rải ra `[5, 5, 2]`. Đây là lý do khoá phân mảnh phải chọn để *trải đều tải*, không theo thứ gì dồn cục (timestamp, một khách hàng khổng lồ...). Phần (B): A chạm node 0,1 trước nên giữ 2 phiếu = đa số → thắng; B chỉ còn node 2 (1 phiếu) → thua. Vì bất kỳ hai "đa số" nào cũng giao nhau (ở đây tại node 1), **không thể** có hai người cùng thắng — ghế cuối bán đúng một lần. Đó là race condition của Bài 2, giải bằng quorum thay vì khoá trên một máy.

> [!note] Tự thử
> - Thêm khoá tên bắt đầu s–z vào `keys`: range bớt lệch. Minh hoạ: range *không* xấu nếu khoá phân bố đều — nó xấu khi khoá dồn cục.
> - Cho B chạm `[2, 0]` thay vì `[1, 2]` (giả sử A chậm ở node 0): giờ thứ tự quyết người thắng. Chạy thử vài thứ tự — luôn chỉ một người đạt đa số.
> - Tăng N=5, cho A và B mỗi người chạm 2 node khác nhau (tổng 4 < 5): *cả hai* đều thiếu đa số → *không ai* thắng ngay. Đó là lúc consensus phải thêm vòng — vì sao thuật toán thật (Raft/Paxos) phức tạp.

## 5. Bảng so sánh: nhân bản vs phân mảnh

Hai từ hay bị lẫn, nhưng chúng giải hai vấn đề khác nhau và thường dùng *cùng lúc*:

| Tiêu chí              | Nhân bản (replication, Bài 8)       | Phân mảnh (partitioning, bài này)      |
| :-------------------- | :---------------------------------- | :------------------------------------- |
| Đặt gì lên nhiều node | **cùng** dữ liệu (bản sao)          | **các phần khác nhau** của dữ liệu     |
| Giải vấn đề           | mất dữ liệu / độ sẵn sàng / latency | dữ liệu/throughput quá lớn cho 1 máy   |
| Cạm bẫy chính         | nhất quán giữa bản sao (CAP)        | chia lệch → **hot spot**               |
| Thêm node giúp gì     | chịu lỗi tốt hơn                    | chứa/chịu tải nhiều hơn (nếu chia đều) |
| AWS                   | Multi-AZ, read replica              | DynamoDB partition key, sharding       |

Hệ thực tế **kết hợp**: dữ liệu chia thành nhiều shard (để scale), *mỗi* shard được nhân bản (để chịu lỗi). Và khi các bản sao của một shard cần đồng ý ai là leader hay giá trị nào thắng → **consensus** (mục 3). Ba mảnh của trụ Distributed — thất bại (Bài 7), nhân bản/nhất quán (Bài 8), phân mảnh/consensus (Bài 9) — khớp lại thành bức tranh đầy đủ của một kho dữ liệu phân tán.

## 6. Nối về AWS

> [!note] Nối về AWS
> DynamoDB là hiện thân trực tiếp của bài này — xem [`aws-fund` Bài 3 — Database & Storage](../../aws-fund/bai_hoc/bai_03_database-storage.md):
> - **Partition key của DynamoDB** = quy tắc phân mảnh theo **hash** của mục 2. Chọn khoá *trải đều* (vd. userId) thì tải phân bố đẹp; chọn khoá *dồn cục* (vd. cùng một "status=active", hay ngày hôm nay) thì sinh **hot partition** — đúng cột `[12,0,0]` của demo, và là nguyên nhân throttling số một trong thực tế.
> - **Hot partition = hot spot của mục 2.** Khi một partition key nhận quá nhiều tải, nó bị giới hạn (throttle) dù bảng tổng còn thừa capacity — thêm capacity không cứu nổi vì vấn đề là *phân bố*, không phải *tổng*. Lời chữa: thiết kế khoá rải tải (write sharding, thêm hậu tố ngẫu nhiên).
> - **Consensus chạy ngầm khắp nơi:** bầu leader cho mỗi partition (ai nhận write), commit đa-mục của DynamoDB Transactions, và cả bên trong S3/các dịch vụ quản lý. Bạn hiếm khi *gọi* consensus trực tiếp, nhưng nó là thứ khiến "ghi vào DynamoDB" không bao giờ bán trùng ghế cuối.
> - **Kết hợp nhân bản + phân mảnh:** mỗi partition của DynamoDB được nhân bản qua nhiều AZ (Bài 8) *và* bảng được chia nhiều partition (bài này) — đúng mô hình "chia để scale, nhân để chịu lỗi" của mục 5.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 9.1 — Phân mảnh khác nhân bản ở điểm gốc nào? Giải vấn đề gì?
> **Đáp:** nhân bản đặt **cùng** dữ liệu lên nhiều node (chống mất/tăng sẵn sàng); phân mảnh đặt **các phần khác nhau** lên các node (chống dữ liệu/throughput quá lớn cho 1 máy). Lý do chính của phân mảnh: **scalability**.

> [!question] Thẻ 9.2 — Hash vs range partitioning: ưu/nhược?
> **Đáp:** hash trải đều (tốt cho cân tải) nhưng mất range scan; range cho range scan nhanh nhưng dễ **lệch/hot spot** nếu khoá dồn cục.

> [!question] Thẻ 9.3 — "Hot spot" là gì? Vì sao thêm node không cứu được?
> **Đáp:** một partition nhận phần lớn tải trong khi các partition khác nhàn. Thêm node vô ích vì tải vẫn dồn một chỗ — vấn đề là *phân bố*, không phải *tổng capacity*.

> [!question] Thẻ 9.4 — Consensus là gì (nôm na)? Cho một ví dụ.
> **Đáp:** làm nhiều node **đồng ý một điều**. Ví dụ: ai giành ghế cuối / cùng username / commit hay abort — chọn một người thắng trong các thao tác loại trừ lẫn nhau.

> [!question] Thẻ 9.5 — Vì sao quorum (đa số) ngăn được hai quyết định mâu thuẫn?
> **Đáp:** hai nhóm "đa số" bất kỳ **luôn giao nhau** → không thể có hai đa số rời nhau cùng thắng → chỉ một quyết định có hiệu lực.

> [!question] Thẻ 9.6 — "Hot partition" của DynamoDB sinh từ đâu? Chữa thế nào?
> **Đáp:** từ partition key dồn cục (status chung, ngày hôm nay...). Chữa: chọn khoá trải đều (userId) hoặc write sharding (thêm hậu tố ngẫu nhiên) — không phải thêm capacity.

## 8. Câu hỏi tự kiểm tra

1. Khi nào nhân bản "không đủ" và cần phân mảnh? Lý do chính của phân mảnh? *(mục 1, tr. 199)*
2. So sánh hash vs range partitioning. Khi nào range gây hot spot? *(mục 2)*
3. Định nghĩa consensus. Liên hệ với race condition (Bài 2) và atomicity. *(mục 3, tr. 364)*
4. Chạy demo mục 4. Vì sao range ra `[12,0,0]`? Vì sao quorum không bao giờ để hai người thắng? *(mục 4)*
5. Nhân bản vs phân mảnh: hai trục độc lập ra sao? Hệ thật kết hợp thế nào? *(mục 5)*
6. "Hot partition" của DynamoDB là gì, sinh từ đâu, chữa ra sao? Vì sao thêm capacity không cứu? *(mục 6)*

## Tóm tắt một trang

```
BÀI 9 — DISTRIBUTED TRỤ 3c: PHÂN MẢNH & CONSENSUS
─────────────────────────────────────────────────────────
PHÂN MẢNH (sharding)  dữ liệu/throughput quá lớn cho 1 máy → chia thành
   partition đặt trên các node khác nhau (DDIA tr.199). Lý do: SCALABILITY.
   Khác nhân bản: nhân = CÙNG dữ liệu; phân mảnh = CÁC PHẦN KHÁC NHAU.

HASH vs RANGE  hash trải đều (cân tải, mất range scan); range cho range
   scan nhưng dễ LỆCH → HOT SPOT nếu khoá dồn cục (timestamp...).
   Hot spot: 1 partition quá tải; thêm node vô ích (vấn đề là PHÂN BỐ).

CONSENSUS  nhiều node ĐỒNG Ý một điều (ghế cuối/username/leader) (tr.364).
   = race condition (Bài 2) ở quy mô máy. QUORUM (đa số): 2 đa số luôn giao
   nhau → không bao giờ 2 quyết định mâu thuẫn cùng thắng.

DEMO  (A) 12 key: hash [5,5,2] đều; range [12,0,0] lệch (hot spot).
   (B) 2 client giành ghế: A được 2/3 phiếu→thắng; B 1 phiếu→thua. Không trùng.

NỐI VỀ AWS  partition key DynamoDB = hash sharding; khoá dồn cục → HOT
   PARTITION (throttle dù bảng còn capacity) → chọn khoá trải đều/write
   sharding; consensus ngầm (bầu leader, Transactions); chia-để-scale +
   nhân-để-chịu-lỗi.
```

## Nguồn

- **Martin Kleppmann**, *Designing Data-Intensive Applications* (O'Reilly, 2017) — **ch. 6 (Partitioning)**: sharding & scalability (tr. 199); **ch. 9 (Consistency and Consensus)**: consensus "agree on something" (tr. 364). Offset **PDF = tr. + 22**.
- Nối về AWS: [`aws-fund` Bài 3 — Database & Storage](../../aws-fund/bai_hoc/bai_03_database-storage.md) (partition key, hot partition, Transactions).
- Khép trụ 3 (Distributed). Tiếp trụ 4 (Dữ liệu): [Bài 10 — storage engine](bai_10_du-lieu-storage.md) — xuống bên trong *một* node: nó lưu và tìm dữ liệu trên đĩa ra sao (B-tree vs LSM).

---

**Bản đồ khoá học — lõi:** [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md) · [Bài 1 — OS: ảo hoá](bai_01_os-ao-hoa.md) · [Bài 2 — OS: concurrency](bai_02_os-concurrency.md) · [Bài 3 — OS: lưu trữ](bai_03_os-luu-tru.md) · [Bài 4 — Mạng: phân tầng, HTTP, DNS](bai_04_mang-http-dns.md) · [Bài 5 — Mạng: TCP, TLS](bai_05_mang-tcp-tls.md) · [Bài 6 — Mạng: hiệu năng, CDN](bai_06_mang-hieu-nang.md) · [Bài 7 — Distributed: giao tiếp & thất bại](bai_07_dist-giao-tiep.md) · [Bài 8 — Distributed: nhân bản & nhất quán](bai_08_dist-nhat-quan.md) · **[Bài 9 — Distributed: phân mảnh & consensus] ← bạn đang ở đây** · [Bài 10 — Dữ liệu: storage engine](bai_10_du-lieu-storage.md) · [Bài 11 — Dữ liệu: batch & stream](bai_11_du-lieu-batch-stream.md)

**Chuyên đề nâng cao:** [Bài 12 — OS nâng cao: bộ nhớ ảo](bai_12_os-bo-nho-ao.md) · [Bài 13 — OS nâng cao: scheduling & locks](bai_13_os-scheduling-locks.md) · [Bài 14 — Mạng nâng cao: bảo mật & mật mã](bai_14_mang-bao-mat.md) · [Bài 15 — Distributed nâng cao: đồng hồ](bai_15_dist-dong-ho.md) · [Bài 16 — Distributed nâng cao: transaction & saga](bai_16_dist-transaction-saga.md) · [Bài 17 — Dữ liệu nâng cao: data models](bai_17_du-lieu-data-models.md) · [Bài 18 — Dữ liệu nâng cao: encoding & schema](bai_18_du-lieu-encoding.md)

Xem thêm [README khoá học](../README.md).
