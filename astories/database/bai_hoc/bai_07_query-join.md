# Bài 7 — Xử lý truy vấn: join algorithms

> [!info] Về bài này
> Có bảng (Bài 1–3), có lưu trữ (Bài 4) và index (Bài 5–6). Giờ: **engine chạy một câu SQL ra sao?** Bài này mở hộp *xử lý truy vấn* — từ SQL tới *kế hoạch thực thi* — rồi đào sâu phần tốn kém nhất: **join**. Ta cài ba thuật toán join (nested-loop, sort-merge, hash) và thấy tận mắt: cùng một kết quả, nhưng chi phí lệch nhau *cấp độ lớn* — chính là lý do Bài 8 (tối ưu) tồn tại.
> Nguồn (Luật số 1): **Silberschatz** *Database System Concepts 7e* — **Ch15 (Query Processing)** (offset PDF = tr. + 29).
> **Chạy demo:** **Node 22+**, `node <tên>.ts` — không cài gói.
> Nên đọc trước: [Bài 1 — đại số quan hệ (join = σθ(r×s))](bai_01_mo-hinh-quan-he.md), [Bài 4 — block I/O](bai_04_luu-tru-buffer.md), [Bài 5 — index](bai_05_index-btree.md).

## Mục lục

1. [Query processing: từ SQL tới kế hoạch chạy](#1-query-processing-từ-sql-tới-kế-hoạch-chạy)
2. [Đo chi phí bằng block I/O](#2-đo-chi-phí-bằng-block-io)
3. [Nested-loop join: thử mọi cặp](#3-nested-loop-join-thử-mọi-cặp)
4. [Sort-merge join và hash join](#4-sort-merge-join-và-hash-join)
5. [Demo: ba thuật toán, một kết quả](#5-demo-ba-thuật-toán-một-kết-quả)
6. [Bản đồ khoá database](#6-bản-đồ-khoá-database)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Query processing: từ SQL tới kế hoạch chạy

Một câu SQL không chạy thẳng. Engine đưa nó qua ba chặng:

```
   SQL  →  [PARSE]  →  cây truy vấn (đại số quan hệ, Bài 1)
                          │
                          ▼
            [OPTIMIZE] → chọn KẾ HOẠCH THỰC THI rẻ nhất
                          │   (dùng index nào? join bằng thuật toán nào? thứ tự?)
                          ▼
            [EXECUTE]  → chạy kế hoạch → kết quả
```

Mấu chốt: *một câu SQL có nhiều cách chạy*, chi phí khác nhau rất xa. Người dùng chỉ nói **muốn gì** (khai báo), engine tự quyết **làm thế nào**.

> [!quote] Silberschatz (tr. 691)
> "it is the responsibility of the system to construct a query-evaluation plan that minimizes the cost of query evaluation; this task is called query optimization."
>
> *trách nhiệm của **hệ thống** là dựng một **kế hoạch thực thi** sao cho **tối thiểu hoá chi phí**; việc này gọi là **query optimization** (tối ưu truy vấn).*

Bài này lo chặng **EXECUTE** (các thuật toán chạy từng phép, nhất là join); Bài 8 lo chặng **OPTIMIZE** (chọn kế hoạch nào). Nhớ lại Bài 1: `r ⋈θ s = σθ(r × s)` — về *nghĩa*. Nhưng engine **không** tính `r × s` (tích Descartes khổng lồ); nó dùng thuật toán join ra thẳng kết quả. Bài này là chính các thuật toán đó.

## 2. Đo chi phí bằng block I/O

"Rẻ" nghĩa là gì? Như Bài 4: chi phí thống trị là **số block đọc/ghi từ đĩa** (và số seek). Sách đo chi phí mỗi thuật toán theo **số block transfer** cộng số seek — không đếm từng byte hay từng dòng. (Ngày nay, với SSD và bộ nhớ lớn, CPU và số phép so sánh cũng được tính thêm, nhưng block I/O vẫn là trục chính.)

Trong demo mục 5 ta dùng **số lần so sánh khoá** làm thước đo đơn giản, tất định (thay cho block I/O) để thấy rõ khác biệt *bậc độ lớn* giữa các thuật toán — ý tưởng y hệt: thuật toán tồi làm việc gấp *bậc độ lớn* thuật toán tốt.

Ký hiệu của sách (nhớ để đọc công thức chi phí): `nr`, `ns` = số *bộ* (tuple) của r, s; `br`, `bs` = số *block* chứa r, s.

## 3. Nested-loop join: thử mọi cặp

Thuật toán ngây thơ nhất — đúng nghĩa đen `σθ(r × s)`:

> [!quote] Silberschatz (tr. 704)
> "This algorithm is called the nested-loop join algorithm, since it basically consists of a pair of nested for loops. Relation r is called the outer relation and relation s the inner relation of the join"
>
> *Thuật toán này gọi là **nested-loop join** vì nó chỉ gồm **một cặp vòng for lồng nhau**. Quan hệ r là **quan hệ ngoài**, s là **quan hệ trong**.*

Ưu điểm lớn: **chạy với mọi điều kiện join**, không cần index, không cần sắp xếp:

> [!quote] Silberschatz (tr. 704)
> "the nested-loop join algorithm requires no indices, and it can be used regardless of what the join condition is."
>
> *nested-loop join **không cần index** và dùng được **bất kể điều kiện join là gì**.*

Nhược điểm chí mạng:

> [!quote] Silberschatz (tr. 704)
> "The nested-loop join algorithm is expensive, since it examines every pair of tuples in the two relations."
>
> *nested-loop join **đắt**, vì nó **xét mọi cặp bộ** của hai quan hệ.*

Số cặp phải xét là `nr ∗ ns` — tức **O(n·m)**. Với hai bảng triệu dòng là *nghìn tỉ* phép so sánh — bất khả thi. (Có biến thể *block nested-loop* và *indexed nested-loop* giảm chi phí khi có buffer/index, nhưng độ phức tạp cơ bản vẫn là tích hai cỡ.) Cần thuật toán tốt hơn cho **equi-join** (join theo `=`) — mục 4.

## 4. Sort-merge join và hash join

Hầu hết join thực tế là **equi-join** (`r.ID = s.ID`). Hai thuật toán khai thác điều đó để xuống **O(n+m)**.

**Sort-merge join** (còn gọi sort-merge-join):

> [!quote] Silberschatz (tr. 708)
> "The merge-join algorithm (also called the sort-merge-join algorithm) can be used to compute natural joins and equi-joins. [...] Suppose that both relations are sorted on the attributes R ∩ S. Then, their join can be computed by a process much like the merge stage in the merge-sort algorithm."
>
> *merge-join (sort-merge) dùng cho natural join và equi-join. [...] Nếu **cả hai quan hệ đã được sắp** theo thuộc tính chung, có thể tính join bằng một quá trình **giống bước trộn của merge-sort**.*

Ý tưởng: sắp cả hai theo khoá join, rồi quét **song song hai con trỏ** — khoá nhỏ hơn thì nhích con trỏ bên đó, bằng nhau thì ghép. Mỗi bộ duyệt *một lần* → **O(n+m)** (sau khi sắp; nếu dữ liệu đã có B+tree sắp sẵn thì khỏi sắp — nối về Bài 5).

**Hash join** — không cần sắp:

> [!quote] Silberschatz (tr. 712)
> "In the hash-join algorithm, a hash function h is used to partition tuples of both relations. The basic idea is to partition the tuples of each of the relations into sets that have the same hash value on the join attributes."
>
> *trong hash-join, một hàm băm h dùng để **phân hoạch** các bộ của **cả hai** quan hệ thành các nhóm **cùng giá trị băm** trên khoá join.*

Vì sao đúng: hai bộ khớp join thì *cùng khoá* → *cùng giá trị băm* → rơi vào *cùng nhóm*. Nên chỉ cần so các bộ **trong cùng nhóm**, không cần so chéo toàn bộ:

> [!quote] Silberschatz (tr. 712)
> "Suppose that an r tuple and an s tuple satisfy the join condition; then, they have the same value for the join attributes. If that value is hashed to some value i, the r tuple has to be in ri and the s tuple in si."

Thực dụng: **băm một bên** vào bảng băm (build), rồi **dò bên kia** (probe) — mỗi bộ xử lý một lần, **O(n+m)** kỳ vọng. Demo mục 5 cài cả ba và đếm công việc.

## 5. Demo: ba thuật toán, một kết quả

Cùng phép `instructor ⋈ teaches ON ID`, ba thuật toán — kết quả **y hệt**, chi phí **khác nhau**:

```typescript
import { strict as assert } from "node:assert";

type Row = Record<string, string>;
type JoinResult = { rows: Row[]; comps: number };   // comps = số lần SO SÁNH khoá

const instructor: Row[] = [
  { ID: "22222", name: "Einstein" },
  { ID: "12121", name: "Wu" },
  { ID: "33456", name: "Gold" },
  { ID: "10101", name: "Srinivasan" },
  { ID: "45565", name: "Katz" },
];
const teaches: Row[] = [
  { ID: "22222", course: "PHY-101" },
  { ID: "10101", course: "CS-101" },
  { ID: "10101", course: "CS-347" },
  { ID: "45565", course: "CS-319" },
];
const join1 = (a: Row, b: Row): Row => ({ name: a.name, course: b.course });
const fmt = (rs: Row[]) => [...rs].sort((x, y) => (x.name + x.course < y.name + y.course ? -1 : 1))
  .map(r => `${r.name}→${r.course}`).join(", ");

// (1) NESTED-LOOP JOIN: thử MỌI cặp (như σθ(r×s) của Bài 1). Đơn giản, đắt: O(n·m).
function nestedLoop(r: Row[], s: Row[], key: string): JoinResult {
  const rows: Row[] = []; let comps = 0;
  for (const a of r) for (const b of s) { comps++; if (a[key] === b[key]) rows.push(join1(a, b)); }
  return { rows, comps };
}

// (2) MERGE (SORT-MERGE) JOIN: sắp cả hai theo khoá rồi quét SONG SONG hai con trỏ. O(n+m) sau khi sắp.
function sortMerge(r: Row[], s: Row[], key: string): JoinResult {
  const R = [...r].sort((a, b) => a[key] < b[key] ? -1 : 1);
  const S = [...s].sort((a, b) => a[key] < b[key] ? -1 : 1);
  const rows: Row[] = []; let comps = 0, i = 0, j = 0;
  while (i < R.length && j < S.length) {
    comps++;
    if (R[i][key] < S[j][key]) i++;
    else if (R[i][key] > S[j][key]) j++;
    else {                                            // khớp: ghép mọi bộ cùng khoá ở hai bên
      let k = j; while (k < S.length && S[k][key] === R[i][key]) k++;
      let m = i; while (m < R.length && R[m][key] === R[i][key]) m++;
      for (let x = i; x < m; x++) for (let y = j; y < k; y++) rows.push(join1(R[x], S[y]));
      i = m; j = k;
    }
  }
  return { rows, comps };
}

// (3) HASH JOIN: băm một bên vào bảng băm, rồi DÒ bên kia. O(n+m) kỳ vọng, không cần sắp.
function hashJoin(r: Row[], s: Row[], key: string): JoinResult {
  const table = new Map<string, Row[]>(); let comps = 0;
  for (const b of s) { comps++; const g = table.get(b[key]); if (g) g.push(b); else table.set(b[key], [b]); }  // build
  const rows: Row[] = [];
  for (const a of r) { comps++; for (const b of table.get(a[key]) ?? []) rows.push(join1(a, b)); }     // probe
  return { rows, comps };
}

console.log("Cùng một phép JOIN (instructor ⋈ teaches ON ID), ba thuật toán:");
const nl = nestedLoop(instructor, teaches, "ID");
const mj = sortMerge(instructor, teaches, "ID");
const hj = hashJoin(instructor, teaches, "ID");
console.log(`  nested-loop : ${fmt(nl.rows)}   [${nl.comps} so sánh]`);
console.log(`  sort-merge  : ${fmt(mj.rows)}   [${mj.comps} so sánh]`);
console.log(`  hash join   : ${fmt(hj.rows)}   [${hj.comps} thao tác băm]`);

// Cả ba cho KẾT QUẢ Y HỆT — chỉ khác CHI PHÍ. (Đây là lý do có trình tối ưu, Bài 8.)
assert.equal(fmt(nl.rows), fmt(mj.rows));
assert.equal(fmt(mj.rows), fmt(hj.rows));
console.log("\nBa kết quả giống hệt nhau?", fmt(nl.rows) === fmt(mj.rows) && fmt(mj.rows) === fmt(hj.rows));

console.log("\nChi phí tăng theo cỡ bảng (n = m bản ghi):");
for (const n of [100, 1_000, 10_000]) {
  const nested = n * n;                 // O(n·m) — mọi cặp
  const smart = 2 * n;                  // O(n+m) — merge/hash quét tuyến tính
  console.log(`  n=${n.toLocaleString("en")}: nested-loop ~${nested.toLocaleString("en")} so sánh  vs  merge/hash ~${smart.toLocaleString("en")}`);
}
console.log("Engine KHÔNG tính tích Descartes (Bài 1) — nó chọn merge/hash để tránh O(n·m).");
```

Kết quả chạy thật *(tất định)*:

```
Cùng một phép JOIN (instructor ⋈ teaches ON ID), ba thuật toán:
  nested-loop : Einstein→PHY-101, Katz→CS-319, Srinivasan→CS-101, Srinivasan→CS-347   [20 so sánh]
  sort-merge  : Einstein→PHY-101, Katz→CS-319, Srinivasan→CS-101, Srinivasan→CS-347   [5 so sánh]
  hash join   : Einstein→PHY-101, Katz→CS-319, Srinivasan→CS-101, Srinivasan→CS-347   [9 thao tác băm]

Ba kết quả giống hệt nhau? true

Chi phí tăng theo cỡ bảng (n = m bản ghi):
  n=100: nested-loop ~10,000 so sánh  vs  merge/hash ~200
  n=1,000: nested-loop ~1,000,000 so sánh  vs  merge/hash ~2,000
  n=10,000: nested-loop ~100,000,000 so sánh  vs  merge/hash ~20,000
Engine KHÔNG tính tích Descartes (Bài 1) — nó chọn merge/hash để tránh O(n·m).
```

Bốn điều đáng thấm. **(1)** Ba thuật toán cho **cùng một tập kết quả** — chúng là ba *cách tính* cùng một phép đại số (Bài 1), nên phải ra như nhau; chỉ **chi phí** khác. **(2)** Với dữ liệu nhỏ này: nested-loop **20** so sánh (5×4, mọi cặp), sort-merge **5**, hash **9** — nested-loop đã làm việc gấp 2–4 lần. **(3)** Khác biệt *bùng nổ* theo cỡ bảng: n=10.000 thì nested-loop làm **100 triệu** so sánh còn merge/hash chỉ **20.000** — gấp *5.000 lần*. Đó là ranh giới chạy-được và treo-máy. **(4)** sort-merge cần dữ liệu *đã sắp* (B+tree, Bài 5, cho sẵn thứ tự → khỏi sắp lại); hash join không cần sắp nhưng cần RAM cho bảng băm. *Không có thuật toán nào luôn thắng* — tuỳ dữ liệu, index, bộ nhớ. Chọn cái nào là việc của Bài 8.

> [!note] Tự thử
> 1. Thêm 3 giảng viên nữa (ID mới, không dạy môn nào) rồi chạy lại: số so sánh của nested-loop tăng thế nào so với hash? Vì sao hash join ít nhạy với bộ nhân vô dụng?
> 2. `sort-merge` giả định đầu vào đã sắp để đạt O(n+m). Nếu phải *tự sắp* trước, chi phí thêm là bao nhiêu (gợi ý: O(n log n))? Khi nào index B+tree (Bài 5) giúp bỏ bước sắp?
> 3. Đổi điều kiện join thành *bất đẳng thức* `instructor.ID < teaches.ID`. Thuật toán nào còn dùng được, cái nào *không*? (gợi ý: hash/merge chỉ cho `=`.)
> 4. Trong hash join, nếu *mọi* khoá băm về cùng một ô (hàm băm tồi), chi phí thoái hoá về đâu? (gợi ý: lại thành O(n·m) — vì sao "goodness" của hàm băm quan trọng.)

## 6. Bản đồ khoá database

| # | Bài | Mảng | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | DBMS là gì & vì sao cần | động lực, trừu tượng hoá | Silberschatz Ch1 |
| 1 | Mô hình quan hệ & đại số quan hệ | nền toán của bảng/SQL | Ch2 |
| 2 | SQL từ nền tới sâu | truy vấn, join, view | Ch3–5 |
| 3 | Thiết kế & chuẩn hoá (E-R, FD, BCNF) | thiết kế đúng | Ch6–7 |
| 4 | Lưu trữ vật lý & buffer manager | dữ liệu trên đĩa/RAM | Ch12–13 |
| 5 | Index: B+tree | tra cứu nhanh | Ch14 |
| 6 | Index nâng cao: LSM & bitmap | tối ưu ghi/phân tích | Ch24 |
| 7 | **Xử lý truy vấn: join algorithms** ← *đang ở đây* | thực thi truy vấn | Ch15 |
| 8 | Tối ưu truy vấn (cost-based) | chọn kế hoạch rẻ nhất | Ch16 |
| 9 | Transaction & ACID, isolation | đúng khi có lỗi | Ch17 |
| 10 | Đồng thời: 2PL / MVCC | đúng khi song song | Ch18 |
| 11 | Phục hồi: WAL / ARIES | sống sót sau sập | Ch19 |
| 12 | Song song & phân tán (góc DB) | mở rộng ra nhiều máy | Ch20–23 + Red Book |

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 7.1 — Ba chặng xử lý một câu SQL là gì?
> **Đáp:** **parse** (SQL → cây đại số quan hệ) → **optimize** (chọn kế hoạch rẻ nhất = query optimization) → **execute** (chạy kế hoạch). Người dùng khai báo *muốn gì*, engine quyết *làm thế nào*.

> [!question] Thẻ 7.2 — Vì sao engine không tính `r × s` rồi lọc như định nghĩa `σθ(r×s)`?
> **Đáp:** tích Descartes là `nr ∗ ns` bộ — khổng lồ. Engine dùng thuật toán join (merge/hash) ra thẳng kết quả, tránh vật chất hoá tích.

> [!question] Thẻ 7.3 — Nested-loop join: ưu, nhược, độ phức tạp?
> **Đáp:** ưu: không cần index/sắp, chạy với **mọi** điều kiện join. Nhược: xét **mọi cặp** → **O(nr·ns)**, đắt khủng khiếp với bảng lớn.

> [!question] Thẻ 7.4 — Sort-merge và hash join khác nested-loop ra sao? Điều kiện dùng?
> **Đáp:** cả hai cho **equi-join** (`=`), đạt **O(n+m)**. Sort-merge: cần dữ liệu **đã sắp** (quét 2 con trỏ song song). Hash: **băm** rồi dò, không cần sắp nhưng cần RAM cho bảng băm. Không dùng được cho bất đẳng thức.

> [!question] Thẻ 7.5 — Vì sao "goodness" (ngẫu nhiên, đều) của hàm băm quan trọng trong hash join?
> **Đáp:** băm tồi → nhiều khoá dồn một ô → so sánh chéo nhiều → thoái hoá về gần O(n·m), mất hết lợi thế.

## 8. Câu hỏi tự kiểm tra

1. Mô tả ba chặng parse/optimize/execute. Query optimization thuộc chặng nào, lo việc gì? *(mục 1)*
2. Vì sao đo chi phí truy vấn bằng block I/O chứ không bằng số byte hay số dòng? *(mục 2, Bài 4)*
3. Nested-loop join có độ phức tạp gì? Vì sao nó vẫn hữu ích dù đắt? *(mục 3)*
4. So sánh điều kiện áp dụng của sort-merge và hash join. Cái nào tận dụng được B+tree có sẵn? *(mục 4)*
5. Chạy demo mục 5, làm Tự thử 2 (tính thêm chi phí sắp). Khi nào ba thuật toán ra kết quả *khác* nhau? (gợi ý: không bao giờ — vì sao?) *(mục 5)*

## Tóm tắt một trang

```
BÀI 7 — XỬ LÝ TRUY VẤN: JOIN ALGORITHMS
─────────────────────────────────────────────────────────
BA CHẶNG  SQL → PARSE (cây đại số) → OPTIMIZE (chọn kế hoạch rẻ nhất = query
   optimization, tr.691) → EXECUTE. Khai báo "muốn gì", engine quyết "làm sao".

ĐO CHI PHÍ  bằng BLOCK I/O (Bài 4), không bằng byte/dòng. Engine KHÔNG tính r×s
   (Bài 1) — dùng thuật toán join ra thẳng kết quả.

NESTED-LOOP (tr.704)  cặp vòng for lồng: xét MỌI cặp → O(nr·ns). Ưu: không cần
   index/sắp, mọi điều kiện join. Nhược: đắt khủng khiếp.

SORT-MERGE (tr.708)  equi-join: sắp 2 bên rồi quét 2 con trỏ song song → O(n+m).
   Cần dữ liệu ĐÃ SẮP (B+tree Bài 5 cho sẵn).
HASH JOIN (tr.712)  equi-join: BĂM phân hoạch cả 2, chỉ so trong cùng nhóm → O(n+m)
   kỳ vọng. Không cần sắp, cần RAM. Hàm băm phải "tốt".

DEMO  3 thuật toán, cùng kết quả, khác chi phí: nested 20 / merge 5 / hash 9.
   n=10.000: nested 100 TRIỆU vs merge/hash 20.000 (gấp 5.000×). → cần Bài 8 chọn.
```

## Nguồn

- **Silberschatz, Korth, Sudarshan — *Database System Concepts*, 7th ed.** — **Ch15 Query Processing**: ba chặng & query optimization (tr. 691), đo chi phí (§15.2), nested-loop join (tr. 704), sort-merge join (tr. 708), hash join (tr. 712). `tai_lieu/Database System Concepts 7th Edition...pdf` (offset **PDF = tr. + 29**).
- Liên hệ: [Bài 1 — join = σθ(r×s)](bai_01_mo-hinh-quan-he.md), [Bài 5 — B+tree cho sort-merge](bai_05_index-btree.md); [Bài 8 — optimizer chọn thuật toán join](bai_08_query-optimization.md).

---

**Bản đồ khoá học:** [Bài 0 — DBMS là gì](bai_00_dbms-la-gi.md) · [Bài 1 — Mô hình quan hệ & đại số quan hệ](bai_01_mo-hinh-quan-he.md) · [Bài 2 — SQL từ nền tới sâu](bai_02_sql.md) · [Bài 3 — Thiết kế & chuẩn hoá](bai_03_thiet-ke-chuan-hoa.md) · [Bài 4 — Lưu trữ & buffer manager](bai_04_luu-tru-buffer.md) · [Bài 5 — Index: B+tree](bai_05_index-btree.md) · [Bài 6 — Index nâng cao: LSM & bitmap](bai_06_index-lsm-bitmap.md) · **[Bài 7 — Xử lý truy vấn: join algorithms] ← bạn đang ở đây** · [Bài 8 — Tối ưu truy vấn](bai_08_query-optimization.md) · [Bài 9 — Transaction & ACID](bai_09_transaction-acid.md) · [Bài 10 — Đồng thời: 2PL/MVCC](bai_10_concurrency.md) · [Bài 11 — Phục hồi: WAL/ARIES](bai_11_recovery.md) · [Bài 12 — Song song & phân tán](bai_12_phan-tan.md)

Xem thêm [README khoá học](../README.md).
