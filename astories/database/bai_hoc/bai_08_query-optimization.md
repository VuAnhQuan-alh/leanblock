# Bài 8 — Tối ưu truy vấn (cost-based)

> [!info] Về bài này
> Bài 7 cho ta các *thuật toán* chạy từng phép (join nào, quét ra sao). Nhưng một câu SQL có **vô số** cách ghép các thuật toán và thứ tự — chênh nhau *cấp độ lớn* về chi phí. Bài này là bộ não quyết định: **trình tối ưu (query optimizer)** — biến đổi truy vấn thành các biểu thức tương đương, ước lượng chi phí từng kế hoạch bằng **thống kê**, rồi chọn cái rẻ nhất. Và ta gọi ra chính trình tối ưu thật bằng `EXPLAIN QUERY PLAN`.
> Nguồn (Luật số 1): **Silberschatz** *Database System Concepts 7e* — **Ch16 (Query Optimization)** (offset PDF = tr. + 29).
> **Chạy demo:** **Node 22+**, `node --experimental-sqlite <tên>.ts` (phần EXPLAIN dùng `node:sqlite`; cảnh báo stderr vô hại).
> Nên đọc trước: [Bài 7 — join algorithms](bai_07_query-join.md), [Bài 5 — index](bai_05_index-btree.md), [Bài 1 — đại số quan hệ](bai_01_mo-hinh-quan-he.md).

## Mục lục

1. [Một câu SQL, nhiều kế hoạch](#1-một-câu-sql-nhiều-kế-hoạch)
2. [Biểu thức tương đương và đẩy selection](#2-biểu-thức-tương-đương-và-đẩy-selection)
3. [Ước lượng chi phí bằng thống kê](#3-ước-lượng-chi-phí-bằng-thống-kê)
4. [Ba bước của trình tối ưu, và EXPLAIN](#4-ba-bước-của-trình-tối-ưu-và-explain)
5. [Demo: đẩy selection và EXPLAIN thật](#5-demo-đẩy-selection-và-explain-thật)
6. [Bản đồ khoá database](#6-bản-đồ-khoá-database)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Một câu SQL, nhiều kế hoạch

> [!quote] Silberschatz (tr. 743)
> "Query optimization is the process of selecting the most efficient query-evaluation plan from among the many strategies usually possible for processing a given query, especially if the query is complex."
>
> *Tối ưu truy vấn là quá trình **chọn kế hoạch thực thi hiệu quả nhất** trong số **rất nhiều chiến lược** thường có thể dùng để xử lý một truy vấn.*

Vì sao đáng để engine bỏ công? Vì khác biệt là *khổng lồ*:

> [!quote] Silberschatz (tr. 743)
> "The difference in cost (in terms of evaluation time) between a good strategy and a bad strategy is often substantial and may be several orders of magnitude."
>
> *Chênh lệch chi phí giữa chiến lược tốt và tồi thường **rất lớn, có thể tới vài cấp độ lớn** (orders of magnitude).*

Ở Bài 7 ta đã thấy: cùng một join, nested-loop vs hash chênh *5.000 lần*. Giờ nhân thêm chọn **thứ tự join**, **đẩy điều kiện lọc**, **dùng index nào** — không gian kế hoạch bùng nổ. Người dùng chỉ viết *muốn gì*; trình tối ưu tìm kế hoạch *rẻ nhất* cho cùng kết quả. Hai đòn bẩy lớn nhất: **biến đổi tương đương** (mục 2) và **ước lượng chi phí** (mục 3).

## 2. Biểu thức tương đương và đẩy selection

Trình tối ưu được phép *viết lại* truy vấn, miễn kết quả không đổi:

> [!quote] Silberschatz (tr. 747)
> "Two relational-algebra expressions are said to be equivalent if, on every legal database instance, the two expressions generate the same set of tuples."
>
> *Hai biểu thức đại số quan hệ **tương đương** nếu, trên **mọi** instance hợp lệ, chúng sinh ra **cùng một tập bộ**.*

Phép biến đổi quyền năng nhất là **đẩy selection xuống** (selection pushdown). Xét truy vấn "giảng viên khoa Music và môn họ dạy". Cách ngây thơ — **join trước, lọc sau**:

```
   Πname,title( σdept=Music( instructor ⋈ teaches ⋈ course ) )
                              └─────────── trung gian KHỔNG LỒ ───────────┘
```

`instructor ⋈ teaches ⋈ course` ghép *mọi* giảng viên với *mọi* môn họ dạy → kết quả trung gian to, rồi mới vứt gần hết đi vì chỉ giữ Music. Cách tối ưu — **lọc trước, join sau**:

```
   Πname,title( (σdept=Music(instructor)) ⋈ teaches ⋈ course )
                 └── chỉ vài giảng viên ──┘
```

> [!quote] Silberschatz (tr. 744)
> "which is equivalent to our original algebra expression, but which generates smaller intermediate relations."
>
> *(biểu thức này) **tương đương** với biểu thức gốc, nhưng **sinh ra các quan hệ trung gian nhỏ hơn**.*

Lọc `instructor` xuống chỉ vài dòng Music *trước khi* join → trung gian bé tí. Cùng kết quả, nhưng công việc ít hơn cả cấp độ lớn. Đây là *quy tắc tương đương* số 1 trong tay trình tối ưu (còn nhiều: đẩy projection, đổi thứ tự join, gộp/tách selection...). Demo mục 5 đo tận mắt chênh lệch trung gian.

## 3. Ước lượng chi phí bằng thống kê

Biết các kế hoạch tương đương rồi, chọn cái nào? Phải **ước lượng chi phí** mỗi kế hoạch — mà chi phí phụ thuộc *kích thước dữ liệu* và *kết quả trung gian*. Engine không chạy thử; nó **đoán** bằng thống kê lưu trong catalog (từ điển hệ thống):

> [!quote] Silberschatz (tr. 745)
> "As evaluation plans are generated, their costs are estimated by using statistical information about the relations, such as relation sizes and index depths."
>
> *Khi sinh ra các kế hoạch, chi phí được ước lượng bằng **thông tin thống kê** về các quan hệ, như **kích thước bảng** và **độ sâu index**.*

Thống kê điển hình: số bộ mỗi bảng (`nr`), số giá trị phân biệt mỗi cột, độ sâu B+tree. Từ đó engine ước **độ chọn lọc (selectivity)** — một điều kiện `dept='Music'` giữ lại *bao nhiêu phần* số dòng. Ước đúng cỡ kết quả trung gian là *chìa khoá*: chọn sai thứ tự join vì đoán sai kích thước là nguyên nhân số một của truy vấn chậm trong thực tế. (Vì vậy phải chạy `ANALYZE` định kỳ để cập nhật thống kê — thống kê cũ → đoán sai → kế hoạch tồi.)

## 4. Ba bước của trình tối ưu, và EXPLAIN

Gộp lại, trình tối ưu cost-based làm ba bước:

> [!quote] Silberschatz (tr. 745)
> "Generation of query-evaluation plans involves three steps: (1) generating expressions that are logically equivalent to the given expression, (2) annotating the resultant expressions in alternative ways to generate alternative query-evaluation plans, and (3) estimating the cost of each evaluation plan, and choosing the one whose estimated cost is the least."
>
> *Sinh kế hoạch gồm ba bước: (1) **sinh các biểu thức tương đương** về mặt logic; (2) **gắn thuật toán** (annotate) cho từng biểu thức để ra các kế hoạch khác nhau; (3) **ước lượng chi phí** mỗi kế hoạch và **chọn cái rẻ nhất**.*

Bước (1) dùng quy tắc tương đương (mục 2), bước (2) chọn thuật toán cho mỗi phép (join nào — Bài 7, index nào — Bài 5), bước (3) dùng thống kê (mục 3). Muốn *nhìn* kết quả quyết định này, mọi DBMS cho một lệnh:

> [!quote] Silberschatz (tr. 746)
> "many databases support variations of a command "explain <query>", which displays the evaluation plan"
>
> *nhiều hệ hỗ trợ biến thể của lệnh **`explain <query>`**, hiển thị **kế hoạch thực thi**.*

`EXPLAIN` là cửa sổ nhìn vào bộ não optimizer — nó cho biết engine *định* quét toàn bảng hay tra index, dùng join nào, theo thứ tự nào. Đây là công cụ số một để *gỡ truy vấn chậm*. Demo mục 5 dùng `EXPLAIN QUERY PLAN` thật của SQLite.

## 5. Demo: đẩy selection và EXPLAIN thật

Phần A đo chênh lệch kết quả trung gian giữa "join rồi lọc" vs "lọc rồi join" (cùng kết quả). Phần B gọi **trình tối ưu thật** của SQLite qua `EXPLAIN QUERY PLAN` — thấy nó tự đổi từ quét-bảng sang tra-index khi có index:

```typescript
import { strict as assert } from "node:assert";
import { DatabaseSync } from "node:sqlite";

// ─── PHẦN A: ĐẨY SELECTION XUỐNG (selection pushdown) ───
// Cùng truy vấn "giảng viên khoa Music và môn họ dạy", hai kế hoạch TƯƠNG ĐƯƠNG
// (cùng kết quả) nhưng kích thước KẾT QUẢ TRUNG GIAN khác nhau cả cấp độ lớn.
type Row = Record<string, string>;
const instructor: Row[] = [
  { ID: "1", name: "Mozart", dept: "Music" }, { ID: "2", name: "Bach", dept: "Music" },
  { ID: "3", name: "Einstein", dept: "Physics" }, { ID: "4", name: "Gold", dept: "Physics" },
  { ID: "5", name: "Katz", dept: "Comp. Sci." }, { ID: "6", name: "Wu", dept: "Finance" },
  { ID: "7", name: "Kim", dept: "Elec. Eng." }, { ID: "8", name: "Crick", dept: "Biology" },
];
// mỗi giảng viên dạy 2 môn → 16 dòng teaches
const teaches: Row[] = instructor.flatMap(i => [
  { ID: i.ID, course: `C${i.ID}a` }, { ID: i.ID, course: `C${i.ID}b` },
]);
const join = (r: Row[], s: Row[]) => r.flatMap(a => s.filter(b => b.ID === a.ID).map(b => ({ name: a.name, course: b.course })));
const fmt = (rs: any[]) => [...rs].sort((x, y) => x.course < y.course ? -1 : 1).map(r => `${r.name}:${r.course}`).join(", ");

// Kế hoạch NGÂY THƠ: JOIN trước (trung gian to) → rồi mới LỌC Music.
const joined = join(instructor, teaches);                 // trung gian = mọi cặp khớp ID
const naive = joined.filter(r => instructor.find(i => i.name === r.name)!.dept === "Music");
// Kế hoạch TỐI ƯU: LỌC Music trước (nhỏ) → rồi JOIN.
const music = instructor.filter(i => i.dept === "Music");  // lọc Music TRƯỚC: chỉ 2 giảng viên vào join (naive join cả 8)
const smart = join(music, teaches);

console.log("PHẦN A — đẩy selection xuống (cùng kết quả, khác chi phí):");
console.log(`  NGÂY THƠ (join rồi lọc): trung gian ${joined.length} dòng → kết quả ${naive.length}`);
console.log(`  TỐI ƯU  (lọc rồi join) : trung gian ${smart.length} dòng → kết quả ${smart.length}`);
console.log(`  kết quả hai kế hoạch giống nhau? ${fmt(naive) === fmt(smart)}`);
console.log(`  → ${fmt(smart)}`);
assert.equal(fmt(naive), fmt(smart));   // tương đương: cùng tập tuple

// ─── PHẦN B: trình tối ưu THẬT nói gì? EXPLAIN QUERY PLAN (node:sqlite) ───
const db = new DatabaseSync(":memory:");
db.exec(`CREATE TABLE instructor(ID TEXT, name TEXT, dept TEXT);`);
for (const i of instructor) db.prepare("INSERT INTO instructor VALUES (?,?,?)").run(i.ID, i.name, i.dept);
const plan = (q: string) => (db.prepare("EXPLAIN QUERY PLAN " + q).all() as any[]).map(r => r.detail).join(" | ");
const Q = "SELECT name FROM instructor WHERE dept='Music'";

console.log("\nPHẦN B — EXPLAIN QUERY PLAN thật (SQLite tự chọn cách chạy):");
console.log("  CHƯA có index:", plan(Q));
db.exec("CREATE INDEX idx_dept ON instructor(dept)");
console.log("  SAU khi tạo index:", plan(Q));
console.log("  → optimizer tự đổi từ quét-toàn-bảng (SCAN) sang tra INDEX (SEARCH) — không đổi SQL.");
```

Kết quả chạy thật *(tất định)*:

```
PHẦN A — đẩy selection xuống (cùng kết quả, khác chi phí):
  NGÂY THƠ (join rồi lọc): trung gian 16 dòng → kết quả 4
  TỐI ƯU  (lọc rồi join) : trung gian 4 dòng → kết quả 4
  kết quả hai kế hoạch giống nhau? true
  → Mozart:C1a, Mozart:C1b, Bach:C2a, Bach:C2b

PHẦN B — EXPLAIN QUERY PLAN thật (SQLite tự chọn cách chạy):
  CHƯA có index: SCAN instructor
  SAU khi tạo index: SEARCH instructor USING INDEX idx_dept (dept=?)
  → optimizer tự đổi từ quét-toàn-bảng (SCAN) sang tra INDEX (SEARCH) — không đổi SQL.
```

Bốn điều đáng thấm. **(1)** Hai kế hoạch cho **cùng kết quả** (`true`) — chúng *tương đương*, đúng định nghĩa tr. 747. **(2)** Nhưng "join rồi lọc" tạo **16** dòng trung gian, "lọc rồi join" chỉ **4** — đẩy selection xuống cắt trung gian xuống còn 1/4 *ở đây*, và tỉ lệ càng tệ khi bảng càng to (chỉ 2/8 giảng viên là Music, nhưng naive vẫn join hết). **(3)** Phần B: với *cùng câu SQL*, optimizer đổi từ `SCAN instructor` (quét toàn bảng) sang `SEARCH instructor USING INDEX idx_dept` (tra index) **chỉ vì ta tạo index** — ta không đổi truy vấn, engine tự quyết. **(4)** `EXPLAIN` là cách ta *kiểm tra* quyết định đó: thấy `SCAN` trên bảng lớn trong câu nóng = dấu hiệu thiếu index.

> [!note] Tự thử
> 1. Trong phần A, tăng số giảng viên non-Music lên 100 (mỗi người 2 môn): trung gian "naive" thành bao nhiêu, "smart" vẫn mấy? Tỉ lệ lãng phí đổi ra sao?
> 2. Phần B: thêm `EXPLAIN QUERY PLAN` cho một `JOIN` hai bảng, xem SQLite chọn chiến lược gì. Tạo index trên khoá join rồi so lại.
> 3. Vì sao thống kê *cũ* (quên `ANALYZE`) có thể khiến optimizer chọn kế hoạch tồi? Cho một tình huống. *(mục 3)*
> 4. Đẩy **projection** xuống (chỉ giữ cột cần *sớm*) cũng là một quy tắc tương đương. Nó giúp gì (gợi ý: bộ trung gian hẹp hơn → ít byte hơn mỗi dòng)?

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
| 7 | Xử lý truy vấn: join algorithms | thực thi truy vấn | Ch15 |
| 8 | **Tối ưu truy vấn (cost-based)** ← *đang ở đây* | chọn kế hoạch rẻ nhất | Ch16 |
| 9 | Transaction & ACID, isolation | đúng khi có lỗi | Ch17 |
| 10 | Đồng thời: 2PL / MVCC | đúng khi song song | Ch18 |
| 11 | Phục hồi: WAL / ARIES | sống sót sau sập | Ch19 |
| 12 | Song song & phân tán (góc DB) | mở rộng ra nhiều máy | Ch20–23 + Red Book |

Hết phần **xử lý & tối ưu truy vấn** (Bài 7–8). Từ Bài 9 ta chuyển sang *tính đúng đắn*: giữ dữ liệu nhất quán khi có lỗi và khi chạy song song.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 8.1 — Query optimization là gì? Vì sao đáng để engine bỏ công?
> **Đáp:** chọn **kế hoạch thực thi rẻ nhất** trong vô số chiến lược cho cùng truy vấn. Đáng, vì chênh lệch tốt/tồi có thể tới **vài cấp độ lớn** (orders of magnitude).

> [!question] Thẻ 8.2 — "Hai biểu thức tương đương" nghĩa là gì? Đẩy selection xuống khai thác điều đó ra sao?
> **Đáp:** sinh **cùng tập bộ** trên mọi instance. Đẩy selection: **lọc trước, join sau** → kết quả trung gian nhỏ hơn mà kết quả cuối không đổi.

> [!question] Thẻ 8.3 — Optimizer ước lượng chi phí bằng gì?
> **Đáp:** **thống kê** trong catalog: kích thước bảng, số giá trị phân biệt, độ sâu index → ước **selectivity** và cỡ kết quả trung gian. Cần `ANALYZE` để thống kê tươi.

> [!question] Thẻ 8.4 — Ba bước sinh kế hoạch của optimizer cost-based?
> **Đáp:** (1) sinh biểu thức **tương đương** (quy tắc); (2) **gắn thuật toán** (join/index) → các kế hoạch; (3) **ước chi phí** mỗi kế hoạch, chọn **rẻ nhất**.

> [!question] Thẻ 8.5 — EXPLAIN dùng để làm gì? Thấy "SCAN" trên bảng lớn nghĩa là gì?
> **Đáp:** hiển thị kế hoạch optimizer chọn (quét bảng hay tra index, join nào). `SCAN` bảng lớn trong câu nóng = thường **thiếu index** → cần tạo index.

## 8. Câu hỏi tự kiểm tra

1. Vì sao cùng một câu SQL lại có nhiều kế hoạch, và chênh lệch chi phí lớn tới đâu? *(mục 1)*
2. Giải thích đẩy selection xuống trên ví dụ Music. Vì sao nó *tương đương* mà vẫn rẻ hơn? *(mục 2, 5)*
3. Optimizer đoán chi phí thế nào khi chưa chạy truy vấn? Thống kê cũ gây hại gì? *(mục 3)*
4. Liệt kê ba bước của trình tối ưu cost-based, mỗi bước liên hệ bài nào đã học. *(mục 4)*
5. Chạy demo mục 5, làm Tự thử 1 (tăng non-Music lên 100). Giải thích vì sao đẩy selection càng quan trọng khi bảng càng to. *(mục 5)*

## Tóm tắt một trang

```
BÀI 8 — TỐI ƯU TRUY VẤN (COST-BASED)
─────────────────────────────────────────────────────────
VẤN ĐỀ  một SQL → vô số kế hoạch; chênh tốt/tồi tới VÀI CẤP ĐỘ LỚN (tr.743).
   User khai báo "muốn gì", optimizer chọn kế hoạch RẺ NHẤT.

BIẾN ĐỔI TƯƠNG ĐƯƠNG  hai biểu thức tương đương = cùng tập bộ trên mọi instance
   (tr.747). ĐẨY SELECTION XUỐNG: lọc TRƯỚC, join SAU → trung gian nhỏ hơn mà
   kết quả không đổi (tr.744). Còn: đẩy projection, đổi thứ tự join...

ƯỚC CHI PHÍ  bằng THỐNG KÊ catalog: kích thước bảng, độ sâu index (tr.745) →
   ước SELECTIVITY & cỡ trung gian. Thống kê cũ (quên ANALYZE) → kế hoạch tồi.

BA BƯỚC (tr.745)  (1) sinh biểu thức tương đương; (2) gắn thuật toán (join Bài 7,
   index Bài 5); (3) ước chi phí, chọn rẻ nhất. EXPLAIN (tr.746) = nhìn kế hoạch.

DEMO  pushdown: trung gian 16 (join rồi lọc) vs 4 (lọc rồi join), cùng kết quả.
   EXPLAIN thật: tạo index → optimizer tự đổi SCAN→SEARCH USING INDEX (không đổi SQL).
```

## Nguồn

- **Silberschatz, Korth, Sudarshan — *Database System Concepts*, 7th ed.** — **Ch16 Query Optimization**: định nghĩa & chênh lệch chi phí (tr. 743), đẩy selection / kết quả trung gian nhỏ hơn (tr. 744), ba bước sinh kế hoạch & ước chi phí bằng thống kê (tr. 745), lệnh explain (tr. 746), biểu thức tương đương (tr. 747). `tai_lieu/Database System Concepts 7th Edition...pdf` (offset **PDF = tr. + 29**).
- Liên hệ: [Bài 7 — optimizer chọn join nào](bai_07_query-join.md), [Bài 5 — index để optimizer dùng](bai_05_index-btree.md), [Bài 1 — đại số quan hệ & tương đương](bai_01_mo-hinh-quan-he.md).

---

**Bản đồ khoá học:** [Bài 0 — DBMS là gì](bai_00_dbms-la-gi.md) · [Bài 1 — Mô hình quan hệ & đại số quan hệ](bai_01_mo-hinh-quan-he.md) · [Bài 2 — SQL từ nền tới sâu](bai_02_sql.md) · [Bài 3 — Thiết kế & chuẩn hoá](bai_03_thiet-ke-chuan-hoa.md) · [Bài 4 — Lưu trữ & buffer manager](bai_04_luu-tru-buffer.md) · [Bài 5 — Index: B+tree](bai_05_index-btree.md) · [Bài 6 — Index nâng cao: LSM & bitmap](bai_06_index-lsm-bitmap.md) · [Bài 7 — Xử lý truy vấn: join algorithms](bai_07_query-join.md) · **[Bài 8 — Tối ưu truy vấn (cost-based)] ← bạn đang ở đây** · [Bài 9 — Transaction & ACID](bai_09_transaction-acid.md) · [Bài 10 — Đồng thời: 2PL/MVCC](bai_10_concurrency.md) · [Bài 11 — Phục hồi: WAL/ARIES](bai_11_recovery.md) · [Bài 12 — Song song & phân tán](bai_12_phan-tan.md)

Xem thêm [README khoá học](../README.md).
