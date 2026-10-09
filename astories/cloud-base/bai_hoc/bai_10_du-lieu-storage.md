# Bài 10 — Dữ liệu trụ 4a: Storage engine (log, index, B-tree vs LSM)

> [!info] Về bài này
> **Trụ 4 (Dữ liệu), mảnh 1/2.** Ba trụ trước xây *quanh* dữ liệu: ảo hoá để chạy, mạng để chuyển, distributed để nhân/chia. Bài này xuống *bên trong một node*: database **lưu và tìm** dữ liệu trên đĩa ra sao? Hoá ra mọi storage engine đều vật lộn với một đánh đổi: **đọc nhanh hay ghi nhanh** — và lựa chọn ấy (B-tree vs LSM-tree) là lý do **RDS/Aurora và DynamoDB hành xử khác nhau**, và vì sao **thêm index tốn write capacity** ở `aws-fund`.
> Nguồn: **DDIA** (ch. 3 — Storage and Retrieval).
> **Trích:** `DDIA (tr. X)` offset **+22**. Câu chốt nguyên văn trong `[!quote]`.
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`).
> Nên đọc trước: [Bài 3 — lưu trữ/journaling](bai_03_os-luu-tru.md) (append-log sẽ trở lại).

## Mục lục

1. [DB đơn giản nhất: append-only log](#1-db-đơn-giản-nhất-append-only-log)
2. [Index: tăng tốc đọc, đánh đổi bằng ghi](#2-index-tăng-tốc-đọc-đánh-đổi-bằng-ghi)
3. [B-tree vs LSM-tree: hai triết lý lưu trữ](#3-b-tree-vs-lsm-tree-hai-triết-lý-lưu-trữ)
4. [Demo: cái giá của index](#4-demo-cái-giá-của-index)
5. [Bảng so sánh: B-tree vs LSM-tree](#5-bảng-so-sánh-b-tree-vs-lsm-tree)
6. [Nối về AWS](#6-nối-về-aws)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. DB đơn giản nhất: append-only log

DDIA bắt đầu từ thứ nhỏ nhất có thể gọi là database:

> [!quote] DDIA (tr. 70)
> "Consider the world's simplest database, implemented as two Bash functions:"
>
> *Hãy xét **database đơn giản nhất thế giới**, viết bằng **hai hàm Bash**:* (một hàm `db_set` nối `key,value` vào cuối một file; một hàm `db_get` tìm key đó).

Ý tưởng: **ghi = nối thêm vào cuối file (append)**. Đây *chính xác* là append-log của journaling ở Bài 3 — và nó ghi cực nhanh vì append là thao tác ghi đơn giản nhất có thể (không phải tìm chỗ, không phải sửa tại chỗ). Giá trị mới nhất của một khoá là bản *cuối cùng* được nối vào. Nhưng cái gì cũng có giá: để **đọc** giá trị của một khoá, `db_get` phải **quét cả file** tìm lần xuất hiện cuối. Ghi O(1), đọc O(n). Với dữ liệu lớn, đọc trở nên thảm hoạ — và đó là lý do index ra đời.

## 2. Index: tăng tốc đọc, đánh đổi bằng ghi

> [!quote] DDIA (tr. 71)
> "An index is an additional structure that is derived from the primary data. Many databases allow you to add and remove indexes, and this doesn't affect the contents of the database; it only affects the performance of queries."
>
> *Một **index** là một **cấu trúc phụ** được **suy ra từ dữ liệu gốc**. Nhiều database cho thêm/bớt index, và việc đó **không đổi nội dung** database; nó chỉ ảnh hưởng **hiệu năng truy vấn**.*

Index là "mục lục" của cuốn sách dữ liệu: nó không thêm nội dung, chỉ giúp *tìm* nhanh hơn. Nhưng mục lục phải được *cập nhật* mỗi khi nội dung đổi — và đó là trái tim của chương:

> [!quote] DDIA (tr. 71)
> "This is an important trade-off in storage systems: well-chosen indexes speed up read queries, but every index slows down writes."
>
> *Đây là một **đánh đổi quan trọng** trong hệ lưu trữ: **index chọn khéo tăng tốc truy vấn đọc, nhưng mỗi index làm chậm ghi**.*

Vì sao chậm ghi? Vì mỗi lần ghi dữ liệu, *mọi* index trên nó cũng phải cập nhật (mục 1: append không index là nhanh nhất có thể). Đây là lý do database **không** tự index mọi cột — nó bắt bạn chọn, dựa trên mẫu truy vấn thực tế. Demo mục 4 đo cả hai đầu của đánh đổi này. Và nó dẫn tới câu hỏi lớn: nếu append ghi nhanh còn index đọc nhanh, có cấu trúc nào dung hoà? Đó là B-tree và LSM-tree.

## 3. B-tree vs LSM-tree: hai triết lý lưu trữ

Hai họ storage engine thống trị, sinh ra từ hai cách trả lời câu hỏi "đọc nhanh hay ghi nhanh":

- **LSM-tree** (Log-Structured Merge): hậu duệ trực tiếp của append-log mục 1. Ghi được gom vào bộ nhớ rồi *tuôn* ra đĩa thành các file bất biến (SSTable), hợp nhất dần ở nền (compaction). Thiên về **ghi nhanh**.
- **B-tree**: cây cân bằng, cập nhật *tại chỗ* trên các trang (page) cố định. Là cấu trúc kinh điển của DB quan hệ. Thiên về **đọc nhanh** và ổn định.

DDIA tóm đánh đổi bằng một "rule of thumb":

> [!quote] DDIA (tr. 83)
> "As a rule of thumb, LSM-trees are typically faster for writes, whereas B-trees are thought to be faster for reads."
>
> *Theo kinh nghiệm, **LSM-tree thường nhanh hơn khi ghi**, còn **B-tree được cho là nhanh hơn khi đọc**.*

DDIA giải thích: đọc trên LSM-tree thường chậm hơn vì phải kiểm tra *nhiều* cấu trúc và SSTable ở các giai đoạn compaction khác nhau. Không có kẻ thắng tuyệt đối — chỉ có "khối lượng công việc của bạn ghi nhiều hay đọc nhiều?". Đây lại là cùng một tinh thần đánh đổi xuyên khoá: TCP vs UDP (Bài 5), strong vs eventual (Bài 8) — *đảm bảo/tốc độ ở đầu này mua bằng chi phí ở đầu kia*.

## 4. Demo: cái giá của index

Dựng "DB đơn giản nhất" (append-log) với 50.000 bản ghi, rồi đo chi phí **đọc** (số record phải quét) có và không có index hash. Đồng thời chỉ ra chi phí **ghi** thêm khi có index.

```typescript
// Storage engine: "DB đơn giản nhất" = append-only log (ghi = nối vào cuối, O(1)).
// Nhưng ĐỌC phải quét ngược cả log (O(n)). Thêm INDEX (hash map) → đọc O(1),
// nhưng mỗi GHI phải cập nhật index nữa. Đó là đánh đổi của DDIA (tr.71).
const N = 50_000;

// --- log: mỗi lần "ghi" nối (key,value) vào cuối; bản mới nhất thắng ---
const log: Array<[string, string]> = [];
const index = new Map<string, string>();     // index: key -> value mới nhất

function writeNoIndex(key: string, value: string): void { log.push([key, value]); }
function writeWithIndex(key: string, value: string): void {
  log.push([key, value]);
  index.set(key, value);                      // CHI PHÍ GHI THÊM: cập nhật index
}

// đọc không index: quét từ CUỐI (bản mới nhất), đếm số record phải so sánh
function getNoIndex(key: string): { value: string | null; scanned: number } {
  let scanned = 0;
  for (let i = log.length - 1; i >= 0; i--) {
    scanned++;
    if (log[i][0] === key) return { value: log[i][1], scanned };
  }
  return { value: null, scanned };
}
function getWithIndex(key: string): { value: string | null; scanned: number } {
  return { value: index.get(key) ?? null, scanned: 1 };  // 1 bước
}

for (let i = 0; i < N; i++) { writeNoIndex(`k${i}`, `v${i}`); writeWithIndex(`k${i}`, `v${i}`); }

// đọc 5 khoá nằm GẦN ĐẦU log (trường hợp xấu cho quét-từ-cuối)
const probes = ["k0", "k1", "k2", "k3", "k4"];
let totalNo = 0, totalIdx = 0;
for (const k of probes) { totalNo += getNoIndex(k).scanned; totalIdx += getWithIndex(k).scanned; }

console.log(`Log ${N.toLocaleString("en")} bản ghi. Đọc ${probes.length} khoá gần đầu log:`);
console.log(`  KHÔNG index: quét tổng ${totalNo.toLocaleString("en")} record  (O(n) mỗi lần)`);
console.log(`  CÓ index   : quét tổng ${totalIdx} record  (O(1) mỗi lần)`);
console.log(`  → đọc nhanh hơn ~${Math.round(totalNo / totalIdx).toLocaleString("en")}x`);
console.log(`\nĐổi lại: mỗi GHI có index phải làm thêm 1 bước (cập nhật map).`);
console.log(`"well-chosen indexes speed up reads, but every index slows down writes" (DDIA tr.71).`);
```

Kết quả chạy thật *(số record quét là tất định; "nhanh hơn" tính theo số bước, không theo ms)*:

```
Log 50,000 bản ghi. Đọc 5 khoá gần đầu log:
  KHÔNG index: quét tổng 499,975 record  (O(n) mỗi lần)
  CÓ index   : quét tổng 5 record  (O(1) mỗi lần)
  → đọc nhanh hơn ~99,995x

Đổi lại: mỗi GHI có index phải làm thêm 1 bước (cập nhật map).
"well-chosen indexes speed up reads, but every index slows down writes" (DDIA tr.71).
```

Không index, đọc 5 khoá gần đầu log phải quét gần **nửa triệu** record (mỗi lần quét ngược gần hết 50.000). Có index, mỗi lần là **1 bước**. Nhưng — và đây là nửa thường bị quên của câu trích — index đó không từ trên trời rơi xuống: mỗi lần ghi, ta trả thêm một `index.set`. Với 50.000 ghi là 50.000 bước thừa, và với *nhiều* index thì nhân lên. Đó chính xác là "đọc nhanh hơn, ghi chậm hơn" — và là lý do mục 6 cho thấy mỗi Global Secondary Index của DynamoDB *ngốn write capacity* riêng.

> [!note] Tự thử
> - Đọc khoá ở *cuối* log (`k49999`) không index: chỉ quét 1 record (gặp ngay). Cho thấy O(n) là *trường hợp xấu/trung bình*, không phải mọi lần — nhưng bạn không kiểm soát được khoá nào bị hỏi.
> - Thêm index thứ hai (vd. theo value): mỗi ghi giờ +2 bước. Minh hoạ "mỗi index làm chậm ghi" cộng dồn.
> - Biến log thành *bất biến theo đợt* (gom 1000 ghi rồi "tuôn" ra một mảng mới): bạn vừa phác thảo ý tưởng SSTable/LSM-tree của mục 3.

## 5. Bảng so sánh: B-tree vs LSM-tree

| Tiêu chí           | B-tree                              | LSM-tree                                |
| :----------------- | :---------------------------------- | :-------------------------------------- |
| Cách ghi           | cập nhật **tại chỗ** trên trang     | **append** + tuôn ra SSTable bất biến   |
| Thiên về           | **đọc** nhanh, ổn định              | **ghi** nhanh, throughput cao           |
| Đọc                | thường 1 đường xuống cây            | phải kiểm nhiều SSTable (chậm hơn)      |
| Chi phí nền        | ít                                  | **compaction** (hợp nhất SSTable)       |
| Nền / AWS          | PostgreSQL/MySQL → **RDS/Aurora**   | LevelDB/RocksDB/Cassandra → kiểu **DynamoDB** |

Quy luật chọn (lặp lại chủ đề đánh đổi của cả khoá): **workload ghi-nhiều → nghiêng LSM; đọc-nhiều, cần độ trễ đọc ổn định → nghiêng B-tree.** Không có "tốt hơn" tuyệt đối. Nhìn rộng ra, append-log của mục 1 là tổ tiên của LSM, còn journaling của Bài 3 cũng là append-log — một ý tưởng (ghi tuần tự nhanh hơn ghi ngẫu nhiên) chạy từ file system lên tới database phân tán.

## 6. Nối về AWS

> [!note] Nối về AWS
> Đánh đổi đọc/ghi của bài này quyết định hành vi và *hoá đơn* của DB trên AWS — xem [`aws-fund` Bài 3 — Database & Storage](../../aws-fund/bai_hoc/bai_03_database-storage.md):
> - **RDS/Aurora (B-tree) vs DynamoDB (LSM-style):** RDS chạy PostgreSQL/MySQL dùng B-tree → mạnh cho truy vấn đọc phức tạp, join, range scan. DynamoDB thiên ghi-nhanh, throughput cao, đổi lại mô hình truy vấn hạn chế hơn (query theo key). Chọn DB = chọn vị trí trên trục mục 5.
> - **Mỗi index tốn tiền ghi.** Global Secondary Index (GSI) của DynamoDB *tiêu write capacity riêng*: mỗi lần ghi item, mọi GSI liên quan cũng được ghi → đúng "every index slows down writes" (tr.71), giờ hiện thành **WCU** trên hoá đơn. Thêm GSI bừa = nhân chi phí ghi.
> - **Chọn index theo mẫu truy vấn**, đúng lời DDIA ở mục 2: đừng index mọi thứ "cho chắc" — mỗi index là chi phí ghi + lưu trữ. Thiết kế từ câu hỏi thực tế bạn sẽ hỏi dữ liệu.
> - **Append-log ở khắp nơi:** DynamoDB Streams, Kinesis, write-ahead log của Aurora — tất cả là append-log của mục 1 phóng lên (và là cầu sang [Bài 11](bai_11_du-lieu-batch-stream.md): log *chính là* một stream sự kiện).

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 10.1 — "DB đơn giản nhất" ghi/đọc thế nào? Độ phức tạp mỗi phía?
> **Đáp:** ghi = append vào cuối file (O(1), nhanh nhất có thể); đọc = quét tìm lần xuất hiện cuối của khoá (O(n), chậm khi lớn).

> [!question] Thẻ 10.2 — Index là gì? Nó đổi nội dung DB không?
> **Đáp:** cấu trúc **phụ** suy ra từ dữ liệu gốc; **không** đổi nội dung, chỉ đổi hiệu năng truy vấn. Phải cập nhật mỗi khi dữ liệu đổi.

> [!question] Thẻ 10.3 — Đánh đổi cốt lõi của index (DDIA)?
> **Đáp:** "index chọn khéo **tăng tốc đọc**, nhưng **mỗi index làm chậm ghi**" — vì mỗi ghi phải cập nhật mọi index. Nên DB bắt bạn chọn index thủ công.

> [!question] Thẻ 10.4 — B-tree vs LSM-tree: cái nào nhanh ghi, cái nào nhanh đọc? Vì sao?
> **Đáp:** LSM nhanh **ghi** (append + SSTable), B-tree nhanh **đọc** (cập nhật tại chỗ, 1 đường xuống cây). LSM đọc chậm hơn vì phải kiểm nhiều SSTable.

> [!question] Thẻ 10.5 — Vì sao mỗi GSI của DynamoDB tốn thêm WCU?
> **Đáp:** GSI là một index; mỗi lần ghi item, GSI cũng được ghi → "every index slows down writes" hiện thành write capacity trên hoá đơn.

> [!question] Thẻ 10.6 — Vì sao RDS hợp truy vấn phức tạp còn DynamoDB thiên throughput?
> **Đáp:** RDS dùng B-tree (đọc/join/range mạnh); DynamoDB kiểu LSM (ghi nhanh, throughput cao, truy vấn theo key). Chọn theo workload.

## 8. Câu hỏi tự kiểm tra

1. Mô tả "DB đơn giản nhất". Vì sao ghi nhanh mà đọc chậm? Liên hệ journaling Bài 3. *(mục 1, tr. 70)*
2. Index là gì? Vì sao nó không đổi nội dung mà đổi hiệu năng? *(mục 2, tr. 71)*
3. Phát biểu đánh đổi index. Vì sao DB không tự index mọi cột? *(mục 2, tr. 71)*
4. B-tree vs LSM-tree: cơ chế ghi khác nhau ra sao, dẫn tới đánh đổi gì? *(mục 3, tr. 83)*
5. Chạy demo mục 4. Giải thích cả hai đầu đánh đổi (đọc nhanh hơn, ghi tốn thêm). *(mục 4)*
6. Vì sao GSI của DynamoDB tốn WCU? RDS vs DynamoDB khác nhau gì về storage engine? *(mục 6)*

## Tóm tắt một trang

```
BÀI 10 — DỮ LIỆU TRỤ 4a: STORAGE ENGINE (log · index · B-tree/LSM)
─────────────────────────────────────────────────────────
DB ĐƠN GIẢN NHẤT  append-only log (DDIA tr.70): ghi = nối vào cuối (O(1),
   nhanh nhất); đọc = quét tìm bản cuối (O(n), chậm). = journaling Bài 3.

INDEX  cấu trúc PHỤ suy từ dữ liệu gốc (tr.71); không đổi nội dung, chỉ đổi
   hiệu năng. ĐÁNH ĐỔI: "index tăng tốc ĐỌC, nhưng mỗi index làm chậm GHI"
   (mỗi ghi phải cập nhật mọi index). → DB bắt chọn index thủ công.

B-TREE vs LSM  LSM = append+SSTable → nhanh GHI; B-tree cập nhật tại chỗ
   nhanh ĐỌC (tr.83). LSM đọc chậm vì kiểm nhiều SSTable. Không ai thắng tuyệt đối.

DEMO  log 50k: đọc 5 khoá gần đầu — không index quét ~500k record; có index
   5 bước (~100.000x). Đổi lại mỗi ghi +1 bước cập nhật index.

NỐI VỀ AWS  RDS/Aurora=B-tree (đọc/join mạnh); DynamoDB=LSM-style (ghi
   nhanh, query theo key). Mỗi GSI tốn WCU ("index chậm ghi" → hoá đơn).
   Chọn index theo mẫu truy vấn. Append-log = Streams/Kinesis/WAL (→ Bài 11).
```

## Nguồn

- **Martin Kleppmann**, *Designing Data-Intensive Applications* (O'Reilly, 2017) — **ch. 3 (Storage and Retrieval)**: world's simplest database (tr. 70), index & trade-off (tr. 71), LSM vs B-tree rule of thumb (tr. 83). Offset **PDF = tr. + 22**.
- Nối về AWS: [`aws-fund` Bài 3 — Database & Storage](../../aws-fund/bai_hoc/bai_03_database-storage.md) (RDS vs DynamoDB, GSI/WCU).
- Tiếp: [Bài 11 — batch & stream](bai_11_du-lieu-batch-stream.md) — khép khoá: append-log chính là một *stream sự kiện*, và từ đó là hai cách xử lý dữ liệu ở quy mô.

---

**Bản đồ khoá học — lõi:** [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md) · [Bài 1 — OS: ảo hoá](bai_01_os-ao-hoa.md) · [Bài 2 — OS: concurrency](bai_02_os-concurrency.md) · [Bài 3 — OS: lưu trữ](bai_03_os-luu-tru.md) · [Bài 4 — Mạng: phân tầng, HTTP, DNS](bai_04_mang-http-dns.md) · [Bài 5 — Mạng: TCP, TLS](bai_05_mang-tcp-tls.md) · [Bài 6 — Mạng: hiệu năng, CDN](bai_06_mang-hieu-nang.md) · [Bài 7 — Distributed: giao tiếp & thất bại](bai_07_dist-giao-tiep.md) · [Bài 8 — Distributed: nhân bản & nhất quán](bai_08_dist-nhat-quan.md) · [Bài 9 — Distributed: phân mảnh & consensus](bai_09_dist-phan-manh.md) · **[Bài 10 — Dữ liệu: storage engine] ← bạn đang ở đây** · [Bài 11 — Dữ liệu: batch & stream](bai_11_du-lieu-batch-stream.md)

**Chuyên đề nâng cao:** [Bài 12 — OS nâng cao: bộ nhớ ảo](bai_12_os-bo-nho-ao.md) · [Bài 13 — OS nâng cao: scheduling & locks](bai_13_os-scheduling-locks.md) · [Bài 14 — Mạng nâng cao: bảo mật & mật mã](bai_14_mang-bao-mat.md) · [Bài 15 — Distributed nâng cao: đồng hồ](bai_15_dist-dong-ho.md) · [Bài 16 — Distributed nâng cao: transaction & saga](bai_16_dist-transaction-saga.md) · [Bài 17 — Dữ liệu nâng cao: data models](bai_17_du-lieu-data-models.md) · [Bài 18 — Dữ liệu nâng cao: encoding & schema](bai_18_du-lieu-encoding.md)

Xem thêm [README khoá học](../README.md).
