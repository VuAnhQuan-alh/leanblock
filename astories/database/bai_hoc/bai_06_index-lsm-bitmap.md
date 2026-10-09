# Bài 6 — Index nâng cao: LSM và bitmap

> [!info] Về bài này
> Bài 5 cho ta B+tree — tuyệt cho *đọc*, nhưng mỗi lần ghi phải sửa cây tại chỗ (random I/O). Khi tải **ghi** cực nặng (log, time-series, feed), B+tree hụt hơi. Bài này mở hai index cho hai bài toán khác: **LSM tree** (biến ghi ngẫu nhiên thành ghi tuần tự — nền của Cassandra/RocksDB/LevelDB) và **bitmap index** (cột ít giá trị, truy vấn phân tích nhiều điều kiện). Đây là chỗ index **từ bỏ** "một kích cỡ cho tất cả".
> Nguồn (Luật số 1): **Silberschatz** *Database System Concepts 7e* — **Ch24 (Advanced Indexing Techniques)** (offset PDF = tr. + 29).
> **Chạy demo:** **Node 22+**, `node <tên>.ts` — không cài gói.
> Nên đọc trước: [Bài 5 — B+tree](bai_05_index-btree.md), [Bài 4 — block & I/O](bai_04_luu-tru-buffer.md). Liên hệ: [cloud-base Bài 10 — storage engine](../../cloud-base/bai_hoc/bai_10_du-lieu-storage.md).

## Mục lục

1. [B+tree giỏi đọc, kém ghi](#1-btree-giỏi-đọc-kém-ghi)
2. [LSM tree: biến ghi ngẫu nhiên thành ghi tuần tự](#2-lsm-tree-biến-ghi-ngẫu-nhiên-thành-ghi-tuần-tự)
3. [Đọc, xoá (tombstone), và compaction](#3-đọc-xoá-tombstone-và-compaction)
4. [Bitmap index: cột ít giá trị, truy vấn nhiều điều kiện](#4-bitmap-index-cột-ít-giá-trị-truy-vấn-nhiều-điều-kiện)
5. [Demo: LSM và bitmap](#5-demo-lsm-và-bitmap)
6. [Bản đồ khoá database](#6-bản-đồ-khoá-database)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. B+tree giỏi đọc, kém ghi

B+tree (Bài 5) đọc nhanh vì cân bằng và béo-lùn. Nhưng mỗi **ghi** (chèn/sửa/xoá) phải tìm đúng lá rồi **sửa tại chỗ** — một thao tác **I/O ngẫu nhiên** (random I/O): nhảy đầu đọc tới một block bất kỳ trên đĩa. Trên đĩa từ, mỗi lần nhảy tốn ~10ms (Bài 4). Tải ghi nặng → nghìn random I/O/giây → nghẽn.

> [!quote] Silberschatz (tr. 1176)
> "B+-tree indices are not efficient for workloads with a very high number of writes, and alternative index structures have been proposed to handle such workloads."
>
> *B+-tree **không hiệu quả** với tải có **rất nhiều ghi**; người ta đã đề xuất các cấu trúc index khác để xử lý tải kiểu đó.*

Mấu chốt: đĩa (và cả SSD) ghi **tuần tự** (sequential) nhanh hơn ghi **ngẫu nhiên** (random) *rất* nhiều — nối thêm vào cuối một file thì khỏi nhảy đầu đọc. Ý tưởng lớn của LSM: *đừng sửa tại chỗ, hãy nối thêm*.

## 2. LSM tree: biến ghi ngẫu nhiên thành ghi tuần tự

> [!quote] Silberschatz (tr. 1176)
> "The key idea of the log-structured merge tree (LSM tree) is to replace random I/O operations during tree inserts, updates, and deletes with a smaller number of sequential I/O operations."
>
> *Ý tưởng cốt lõi của **LSM tree** là **thay I/O ngẫu nhiên** khi chèn/sửa/xoá bằng **số ít I/O tuần tự**.*

Cấu trúc gồm một cây trong RAM và nhiều cây bất biến trên đĩa:

> [!quote] Silberschatz (tr. 1176)
> "An LSM tree consists of several B+-trees, starting with an in-memory tree, called L0, and on-disk trees L1, L2, …, Lk for some k, where k is called the level."
>
> *Một LSM tree gồm **nhiều B+-tree**: bắt đầu bằng cây trong-bộ-nhớ **L0**, rồi các cây trên-đĩa **L1, L2, …, Lk**.*

```
   GHI →  ┌──────────────┐
          │  L0 (RAM)    │  memtable: sắp theo khoá, ghi RAM (nhanh)
          └──────┬───────┘
                 │ đầy → FLUSH (ghi TUẦN TỰ xuống đĩa, bất biến)
          ┌──────▼───────┐
          │  L1 (đĩa)    │  SSTable: file sắp sẵn, KHÔNG sửa
          │  L2 (đĩa)    │  đầy → trộn (merge) xuống level sau
          │  ...         │
          └──────────────┘
```

Cơ chế ghi: mọi ghi vào **L0** (memtable, trong RAM). Khi L0 đầy, **flush** toàn bộ xuống đĩa thành một cây bất biến — một thao tác **ghi tuần tự**, không nhảy đầu đọc. Khi một level đầy, trộn xuống level kế. Giá phải trả:

> [!quote] Silberschatz (tr. 1177)
> "the entire contents of the tree are copied each time a set of entries from L0 are copied into L1."
>
> *toàn bộ nội dung cây bị **chép lại** mỗi lần trộn L0 vào L1.*

Đây là **khuếch đại ghi (write amplification)**: một byte dữ liệu bị ghi lại nhiều lần qua các lần trộn. Đánh đổi LSM: **ghi rẻ** (tuần tự) + **đọc đắt hơn** (phải xét nhiều cây) + chép lại khi trộn. Ngược hẳn B+tree. Đây chính là cặp đánh đổi "B-tree vs LSM" mà [cloud-base Bài 10](../../cloud-base/bai_hoc/bai_10_du-lieu-storage.md) nhìn từ góc ứng dụng — giờ ta thấy *cơ chế* bên trong.

## 3. Đọc, xoá (tombstone), và compaction

**Đọc** trong LSM khó hơn B+tree: dữ liệu một khoá có thể nằm ở L0 *hoặc* bất kỳ Li nào. Phải tra **từ mới tới cũ** (L0 trước, rồi L1, L2...) và **bản gặp đầu tiên thắng** (vì nó mới nhất). Đây là **khuếch đại đọc (read amplification)** — cái giá của ghi rẻ.

**Xoá** mới thú: không thể sửa SSTable bất biến để bỏ một khoá. Thay vào đó:

> [!quote] Silberschatz (tr. 1178)
> "deletion results in insertion of a new deletion entry that indicates which index entry is to be deleted."
>
> *xoá = **chèn một bản ghi xoá** (deletion entry) báo rằng mục nào cần bị xoá.*

Bản ghi xoá này gọi là **tombstone** (bia mộ). Khi đọc, nếu gặp tombstone trước thì coi như khoá *đã bị xoá*. **Cập nhật** cũng vậy — chèn bản mới, đọc trả về bản mới nhất:

> [!quote] Silberschatz (tr. 1179)
> "Lookups need to match update entries with the original entries and return the latest value."

**Compaction** (nén/dọn) là bước trộn các SSTable lại: với mỗi khoá giữ bản *mới nhất*, và **vứt bỏ tombstone** cùng bản cũ nó che. Compaction vừa thu hồi chỗ, vừa giảm số SSTable phải tra khi đọc → cân lại read amplification. Demo mục 5 cài đủ: flush, đọc-mới-thắng, tombstone, compaction.

## 4. Bitmap index: cột ít giá trị, truy vấn nhiều điều kiện

Bài toán khác hẳn: phân tích dữ liệu (analytics) với điều kiện trên **cột ít giá trị** — `gender ∈ {m,f}`, `income_level ∈ {L1..L5}`, `active ∈ {true,false}`.

> [!quote] Silberschatz (tr. 1182)
> "Bitmaps work best for attributes that take only a small number of distinct values."
>
> *Bitmap hiệu quả nhất cho các thuộc tính chỉ nhận **ít giá trị phân biệt**.*

Cấu trúc đơn giản đến bất ngờ:

> [!quote] Silberschatz (tr. 1182)
> "a bitmap index on the attribute A of relation r consists of one bitmap for each value that A can take. Each bitmap has as many bits as the number of records in the relation. The ith bit of the bitmap for value vj is set to 1 if the record numbered i has the value vj for attribute A."
>
> *bitmap index trên thuộc tính A gồm **một bitmap cho mỗi giá trị** mà A có thể nhận. Mỗi bitmap dài bằng số bản ghi; **bit thứ i = 1** nếu bản ghi i mang giá trị đó.*

```
   records:     rec1  rec2  rec3  rec4  rec5
   gender:       m     f     f     m     f
   bitmap f:     0     1     1     0     1      →  01101
   income:      L1    L2    L1    L1    L1
   bitmap L2:    0     1     0     0     0      →  01000

   "nữ VÀ income L2":  01101 AND 01000 = 01000  →  chỉ rec2
```

Sức mạnh nằm ở **truy vấn nhiều điều kiện**: `WHERE gender='f' AND income='L2'` = **AND** hai bitmap (phép bit cực nhanh). Một mình thì bitmap không giúp mấy (vẫn phải đọc gần hết block), nhưng kết hợp nhiều điều kiện thì lọc xuống phần rất nhỏ — và **đếm** (`COUNT`) thì chỉ cần đếm bit 1 trong bitmap giao, *không cần đọc bảng*. Rất hợp kho phân tích. Bitmap cũng **tí hon**: một bit/bản ghi thay vì hàng trăm byte.

## 5. Demo: LSM và bitmap

Phần A dựng một LSM thu nhỏ (memtable + SSTable, flush khi đầy 3, đọc mới-thắng, tombstone, compaction). Phần B tái hiện đúng Figure 24.3 của Silberschatz (bitmap AND):

```typescript
import { strict as assert } from "node:assert";

// ─── PHẦN A: LSM tree (log-structured merge) — tối ưu GHI ───
// Ghi vào memtable (RAM, sắp theo khoá). Đầy → FLUSH xuống một SSTable bất biến
// (ghi tuần tự, nhanh). Đọc: memtable trước, rồi các SSTable mới→cũ, HIT đầu thắng.
// Xoá = ghi "bia mộ" (tombstone). Compaction = trộn các SSTable, giá trị mới thắng,
// bỏ tombstone. Đối cực với B+tree (Bài 5): B+tree ghi tại chỗ (random I/O), LSM nối-thêm.
const TOMB = Symbol("deleted");
type Val = number | typeof TOMB;
type SSTable = Map<string, Val>;      // bất biến, sắp theo khoá

let memtable: Map<string, Val> = new Map();
const sstables: SSTable[] = [];        // sstables[0] = MỚI nhất
const THRESHOLD = 3;

function flush() {
  if (memtable.size === 0) return;
  const sorted: SSTable = new Map([...memtable.entries()].sort((a, b) => a[0] < b[0] ? -1 : 1));
  sstables.unshift(sorted);            // đẩy lên đầu = mới nhất
  memtable = new Map();
  console.log(`  [flush] SSTable#${sstables.length} = {${[...sorted].map(([k, v]) => `${k}:${v === TOMB ? "DEL" : v}`).join(", ")}}`);
}
function put(k: string, v: number) { memtable.set(k, v); if (memtable.size >= THRESHOLD) flush(); }
function del(k: string)            { memtable.set(k, TOMB); if (memtable.size >= THRESHOLD) flush(); }
function get(k: string): string {
  const levels: [string, Map<string, Val>][] = [["mem", memtable], ...sstables.map((s, i) => [`SST#${sstables.length - i}`, s] as [string, Map<string, Val>])];
  for (const [name, lv] of levels)
    if (lv.has(k)) { const v = lv.get(k)!; return v === TOMB ? `XOÁ (tombstone ở ${name})` : `${v} (từ ${name})`; }
  return "KHÔNG có";
}
function compact() {                   // trộn mọi SSTable → một cái; mới thắng; bỏ tombstone
  const merged: SSTable = new Map();
  for (let i = sstables.length - 1; i >= 0; i--) for (const [k, v] of sstables[i]) merged.set(k, v);
  const live = new Map([...merged].filter(([, v]) => v !== TOMB).sort((a, b) => a[0] < b[0] ? -1 : 1));
  sstables.length = 0; sstables.push(live);
}

console.log("PHẦN A — LSM tree (THRESHOLD flush = 3):");
put("a", 1); put("b", 2); put("c", 3);        // memtable đầy → flush SSTable#1
put("a", 10); del("b"); put("d", 4);          // a cập nhật, b xoá → flush SSTable#2
console.log(`  (có ${sstables.length} SSTable; đọc phải xét memtable + mọi SSTable)`);
console.log("  get a:", get("a"), "  ← bản MỚI thắng (SSTable mới hơn)");
console.log("  get b:", get("b"), " ← tombstone che bản cũ");
console.log("  get c:", get("c"), "  ← phải lần xuống SSTable cũ");
console.log("  get d:", get("d"));
compact();
console.log("  [compact] trộn còn 1 SSTable:", `{${[...sstables[0]].map(([k, v]) => `${k}:${v}`).join(", ")}}`);
console.log("  get b sau compact:", get("b"), "(tombstone đã dọn)");
assert.equal([...sstables[0].keys()].join(","), "a,c,d");

// ─── PHẦN B: Bitmap index — tối ưu truy vấn nhiều khoá, cột ÍT GIÁ TRỊ ───
// Mỗi GIÁ TRỊ một bitmap; bit i = 1 nếu bản ghi i mang giá trị đó. Truy vấn nhiều
// điều kiện = AND các bitmap. (Tái hiện Figure 24.3 của Silberschatz.)
const records = [
  { gender: "m", income: "L1" },   // rec1
  { gender: "f", income: "L2" },   // rec2
  { gender: "f", income: "L1" },   // rec3
  { gender: "m", income: "L1" },   // rec4
  { gender: "f", income: "L1" },   // rec5
];
function bitmap(attr: "gender" | "income", value: string): number[] {
  return records.map(r => r[attr] === value ? 1 : 0);
}
const and = (x: number[], y: number[]) => x.map((b, i) => b & y[i]);

console.log("\nPHẦN B — Bitmap index (tái hiện Figure 24.3):");
const bf = bitmap("gender", "f"), bL2 = bitmap("income", "L2");
console.log("  bitmap gender=f :", bf.join(""));
console.log("  bitmap income=L2:", bL2.join(""));
const res = and(bf, bL2);
console.log("  f AND L2        :", res.join(""), "← giao hai bitmap");
const matches = res.flatMap((b, i) => b ? [i + 1] : []);
console.log(`  → bản ghi khớp: rec${matches.join(", rec")}  (đếm = ${res.reduce((s, b) => s + b, 0)}, không cần đọc bảng)`);
assert.deepEqual(res, [0, 1, 0, 0, 0]);   // đúng 01000 như sách
```

Kết quả chạy thật *(tất định)*:

```
PHẦN A — LSM tree (THRESHOLD flush = 3):
  [flush] SSTable#1 = {a:1, b:2, c:3}
  [flush] SSTable#2 = {a:10, b:DEL, d:4}
  (có 2 SSTable; đọc phải xét memtable + mọi SSTable)
  get a: 10 (từ SST#2)   ← bản MỚI thắng (SSTable mới hơn)
  get b: XOÁ (tombstone ở SST#2)  ← tombstone che bản cũ
  get c: 3 (từ SST#1)   ← phải lần xuống SSTable cũ
  get d: 4 (từ SST#2)
  [compact] trộn còn 1 SSTable: {a:10, c:3, d:4}
  get b sau compact: KHÔNG có (tombstone đã dọn)

PHẦN B — Bitmap index (tái hiện Figure 24.3):
  bitmap gender=f : 01101
  bitmap income=L2: 01000
  f AND L2        : 01000 ← giao hai bitmap
  → bản ghi khớp: rec2  (đếm = 1, không cần đọc bảng)
```

Năm điều đáng thấm. **(1)** Ghi chỉ vào memtable, đầy thì flush cả cụm xuống đĩa *một lần tuần tự* — không sửa tại chỗ. **(2)** `get a` trả `10 (từ SST#2)` chứ không phải `1`: bản ở SSTable **mới hơn** thắng, nên đọc phải quét từ mới tới cũ. **(3)** `get b` thấy **tombstone** ở SST#2 → báo đã xoá, dù bản gốc `b:2` vẫn nằm ở SST#1 (chưa bị dọn). **(4)** Compaction trộn hai SSTable còn một `{a:10, c:3, d:4}`: lấy bản mới, **vứt tombstone** → sau đó `get b` = KHÔNG có. **(5)** Bitmap: `01101 AND 01000 = 01000` cho ra đúng `rec2` — và đếm được *không cần đọc bảng*, đúng như Figure 24.3 của sách.

> [!note] Tự thử
> 1. Thêm `put("a", 20)` vào memtable *sau* compact rồi `get a`: kết quả? Vì sao memtable luôn được xét *trước* mọi SSTable?
> 2. Giảm `THRESHOLD` xuống 2: số SSTable tạo ra nhiều hơn hay ít hơn? Nhiều SSTable ảnh hưởng *đọc* thế nào (read amplification)?
> 3. Ở bitmap, thêm truy vấn `gender='m' AND income='L1'` (dùng OR nếu cần hàm `or`). Kết quả bitmap và các rec khớp?
> 4. Vì sao bitmap **tệ** cho cột nhiều giá trị (vd `email`, cả triệu giá trị)? (gợi ý: số bitmap = số giá trị phân biệt.)
> 5. So sánh: với tải "ghi 90% / đọc 10%, hiếm range query", chọn B+tree hay LSM? Còn "đọc nặng, nhiều range query, ghi ít"?

## 6. Bản đồ khoá database

| # | Bài | Mảng | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | DBMS là gì & vì sao cần | động lực, trừu tượng hoá | Silberschatz Ch1 |
| 1 | Mô hình quan hệ & đại số quan hệ | nền toán của bảng/SQL | Ch2 |
| 2 | SQL từ nền tới sâu | truy vấn, join, view | Ch3–5 |
| 3 | Thiết kế & chuẩn hoá (E-R, FD, BCNF) | thiết kế đúng | Ch6–7 |
| 4 | Lưu trữ vật lý & buffer manager | dữ liệu trên đĩa/RAM | Ch12–13 |
| 5 | Index: B+tree | tra cứu nhanh | Ch14 |
| 6 | **Index nâng cao: LSM & bitmap** ← *đang ở đây* | tối ưu ghi/phân tích | Ch24 |
| 7 | Xử lý truy vấn: join algorithms | thực thi truy vấn | Ch15 |
| 8 | Tối ưu truy vấn (cost-based) | chọn kế hoạch rẻ nhất | Ch16 |
| 9 | Transaction & ACID, isolation | đúng khi có lỗi | Ch17 |
| 10 | Đồng thời: 2PL / MVCC | đúng khi song song | Ch18 |
| 11 | Phục hồi: WAL / ARIES | sống sót sau sập | Ch19 |
| 12 | Song song & phân tán (góc DB) | mở rộng ra nhiều máy | Ch20–23 + Red Book |

Hết phần **index** (Bài 5–6). Từ Bài 7 ta chuyển sang *thực thi truy vấn*: có bảng và index rồi, engine chạy một câu SQL ra sao.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 6.1 — Vì sao B+tree kém với tải ghi nặng?
> **Đáp:** mỗi ghi sửa cây *tại chỗ* = **I/O ngẫu nhiên** (nhảy đầu đọc, ~10ms/lần trên đĩa từ). Tải ghi nặng → nghìn random I/O → nghẽn.

> [!question] Thẻ 6.2 — Ý tưởng cốt lõi và cấu trúc của LSM tree?
> **Đáp:** thay **random I/O** bằng **sequential I/O**: ghi vào memtable L0 (RAM), đầy thì **flush tuần tự** xuống SSTable bất biến trên đĩa (L1, L2...). Đọc quét từ mới tới cũ.

> [!question] Thẻ 6.3 — LSM xoá và cập nhật thế nào? Compaction làm gì?
> **Đáp:** xoá = chèn **tombstone** (SSTable bất biến, không sửa được); cập nhật = chèn bản mới (đọc trả bản mới nhất). **Compaction** trộn SSTable: giữ bản mới nhất, vứt tombstone → thu hồi chỗ + giảm read amplification.

> [!question] Thẻ 6.4 — Đánh đổi B+tree vs LSM?
> **Đáp:** B+tree: đọc nhanh, ghi chậm (random, sửa tại chỗ). LSM: ghi nhanh (tuần tự, nối thêm), đọc chậm hơn (nhiều SSTable) + **write amplification** (chép lại khi trộn).

> [!question] Thẻ 6.5 — Bitmap index hợp loại cột nào? Mạnh ở truy vấn gì?
> **Đáp:** cột **ít giá trị phân biệt** (gender, trạng thái). Một bitmap/giá trị, bit i=1 nếu rec i mang giá trị đó. Mạnh ở **nhiều điều kiện** (AND/OR bitmap) và **đếm** (không cần đọc bảng). Tệ cho cột nhiều giá trị.

## 8. Câu hỏi tự kiểm tra

1. Vì sao ghi tuần tự nhanh hơn ghi ngẫu nhiên, và LSM khai thác điều đó thế nào? *(mục 1, 2)*
2. Mô tả đường đi của một `get(k)` trong LSM. Vì sao phải quét từ mới tới cũ? *(mục 3, 5)*
3. Tombstone là gì? Vì sao LSM cần nó thay vì xoá trực tiếp? Compaction dọn nó khi nào? *(mục 3)*
4. Bitmap `gender='f'` = 01101, `income='L2'` = 01000. Tính `f AND L2` và chỉ ra rec khớp. Vì sao đếm được mà không đọc bảng? *(mục 4, 5)*
5. Chạy demo mục 5, làm Tự thử 5 (chọn index theo tải). Khi nào B+tree thắng, khi nào LSM thắng? *(mục 2, 5)*

## Tóm tắt một trang

```
BÀI 6 — INDEX NÂNG CAO: LSM & BITMAP
─────────────────────────────────────────────────────────
B+TREE KÉM GHI  ghi = sửa cây TẠI CHỖ = random I/O (~10ms/lần). Tải ghi nặng → nghẽn
   (Silberschatz tr.1176).

LSM TREE  thay random I/O bằng SEQUENTIAL I/O (tr.1176). Ghi→memtable L0 (RAM), đầy→
   FLUSH tuần tự xuống SSTable bất biến L1,L2... Đọc: quét MỚI→CŨ, bản đầu thắng
   (read amplification). Giá: chép lại khi trộn = WRITE AMPLIFICATION (tr.1177).

XOÁ/SỬA  xoá = TOMBSTONE (chèn bản ghi xoá, tr.1178); sửa = chèn bản mới, đọc trả bản
   mới nhất (tr.1179). COMPACTION: trộn SSTable, giữ mới nhất, VỨT tombstone.
   Đối cực B+tree: LSM ghi rẻ/đọc đắt; B+tree đọc rẻ/ghi đắt.

BITMAP  cột ÍT giá trị (tr.1182): 1 bitmap/giá trị, bit i=1 nếu rec i mang giá trị đó
   (tr.1182). Truy vấn nhiều điều kiện = AND/OR bitmap; đếm không cần đọc bảng.
   01101 AND 01000 = 01000 → rec2 (Figure 24.3). Tệ cho cột nhiều giá trị.

DEMO  LSM: flush, get mới-thắng, tombstone, compact dọn. Bitmap: f AND L2 → rec2.
```

## Nguồn

- **Silberschatz, Korth, Sudarshan — *Database System Concepts*, 7th ed.** — **Ch24 Advanced Indexing Techniques**: LSM tree key idea & cấu trúc L0..Lk (tr. 1176), chi phí chép lại / write amplification (tr. 1177), xoá bằng tombstone (tr. 1178), cập nhật & lookup bản mới nhất (tr. 1179); bitmap cho cột ít giá trị (tr. 1182), cấu trúc bitmap (tr. 1182), truy vấn AND nhiều điều kiện (tr. 1183). `tai_lieu/Database System Concepts 7th Edition...pdf` (offset **PDF = tr. + 29**).
- Liên hệ: [cloud-base Bài 10 — storage engine](../../cloud-base/bai_hoc/bai_10_du-lieu-storage.md) (B-tree vs LSM, append-log ở góc data-intensive — DDIA).

---

**Bản đồ khoá học:** [Bài 0 — DBMS là gì](bai_00_dbms-la-gi.md) · [Bài 1 — Mô hình quan hệ & đại số quan hệ](bai_01_mo-hinh-quan-he.md) · [Bài 2 — SQL từ nền tới sâu](bai_02_sql.md) · [Bài 3 — Thiết kế & chuẩn hoá](bai_03_thiet-ke-chuan-hoa.md) · [Bài 4 — Lưu trữ & buffer manager](bai_04_luu-tru-buffer.md) · [Bài 5 — Index: B+tree](bai_05_index-btree.md) · **[Bài 6 — Index nâng cao: LSM & bitmap] ← bạn đang ở đây** · [Bài 7 — Join algorithms](bai_07_query-join.md) · [Bài 8 — Tối ưu truy vấn](bai_08_query-optimization.md) · [Bài 9 — Transaction & ACID](bai_09_transaction-acid.md) · [Bài 10 — Đồng thời: 2PL/MVCC](bai_10_concurrency.md) · [Bài 11 — Phục hồi: WAL/ARIES](bai_11_recovery.md) · [Bài 12 — Song song & phân tán](bai_12_phan-tan.md)

Xem thêm [README khoá học](../README.md).
