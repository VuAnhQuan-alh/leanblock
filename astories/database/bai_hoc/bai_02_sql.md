# Bài 2 — SQL từ nền tới sâu

> [!info] Về bài này
> Bài 1 cho ta *đại số quan hệ* — ngôn ngữ toán để hỏi dữ liệu. **SQL là ngôn ngữ thực tế** hiện thực hoá đại số đó, cộng thêm những thứ thực dụng mà lý thuyết tập hợp bỏ qua: **multiset** (cho trùng), **outer join**, **gom nhóm**, **subquery**, **view**. Bài này đi từ `SELECT-FROM-WHERE` tới view, luôn soi ngược về đại số quan hệ để thấy cái gì là *toán*, cái gì là *kỹ thuật*.
> Nguồn (Luật số 1): **Silberschatz** *Database System Concepts 7e* — **Ch3 (Introduction to SQL)**, **Ch4 (Intermediate SQL)**, Ch5 (offset PDF = tr. + 29).
> **Chạy demo:** **Node 22+**, `node --experimental-sqlite <tên>.ts` (SQL thật qua `node:sqlite`, không cài gói; cảnh báo *ExperimentalWarning* ở stderr là bình thường).
> Nên đọc trước: [Bài 1 — Mô hình quan hệ & đại số quan hệ](bai_01_mo-hinh-quan-he.md).

## Mục lục

1. [SQL là đại số quan hệ mặc áo cú pháp](#1-sql-là-đại-số-quan-hệ-mặc-áo-cú-pháp)
2. [SELECT-FROM-WHERE và cái bẫy multiset](#2-select-from-where-và-cái-bẫy-multiset)
3. [JOIN: inner bỏ, outer giữ](#3-join-inner-bỏ-outer-giữ)
4. [Gom nhóm, lọc nhóm, và thứ tự thực thi](#4-gom-nhóm-lọc-nhóm-và-thứ-tự-thực-thi)
5. [Subquery và view](#5-subquery-và-view)
6. [Demo: SQL thật từ cơ bản tới view](#6-demo-sql-thật-từ-cơ-bản-tới-view)
7. [Bản đồ khoá database](#7-bản-đồ-khoá-database)
8. [Thẻ ôn (active recall)](#8-thẻ-ôn-active-recall)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. SQL là đại số quan hệ mặc áo cú pháp

Ở Bài 1, "tìm tên giảng viên khoa Physics" là `Πname(σdept=Physics(instructor))`. Trong SQL:

```
select name                    -- Π  (chiếu: giữ cột name)
from instructor                -- ×  (nguồn: các quan hệ trong from)
where dept_name = 'Physics';   -- σ  (chọn: giữ hàng thoả điều kiện)
```

> [!quote] Silberschatz (tr. 71)
> "The basic structure of an SQL query consists of three clauses: select, from, and where. A query takes as its input the relations listed in the from clause, operates on them as specified in the where and select clauses, and then produces a relation as the result."
>
> *Cấu trúc cơ bản của truy vấn SQL gồm ba mệnh đề: **select, from, where**. Truy vấn nhận đầu vào là các quan hệ trong **from**, xử lý theo **where** và **select**, rồi sinh ra một quan hệ làm kết quả.*

Đọc **xuôi** từ `select` nhưng *hiểu* phải đọc theo thứ tự `from → where → select`: lấy quan hệ (from), lọc hàng (where ↔ σ), rồi giữ cột (select ↔ Π). Mục 4 sẽ cho thứ tự thực thi đầy đủ — nhớ nó thì mọi truy vấn phức tạp tự sáng ra.

## 2. SELECT-FROM-WHERE và cái bẫy multiset

Bài 1 nhấn: *relation là một **tập*** → không có hàng trùng. SQL **phá** quy ước đó vì lý do thực dụng:

> [!quote] Silberschatz (tr. 72)
> "In the formal, mathematical definition of the relational model, a relation is a set. Thus, duplicate tuples would never appear in relations. In practice, duplicate elimination is time-consuming. Therefore, SQL allows duplicates in database relations as well as in the results of SQL expressions."
>
> *Trong định nghĩa toán học, một quan hệ là một **tập** → không bao giờ có bộ trùng. Nhưng trong thực tế, **khử trùng tốn thời gian**. Vì vậy SQL **cho phép trùng** cả trong bảng lẫn trong kết quả truy vấn.*

Nên `select dept_name from instructor` trả về *mỗi giảng viên một dòng, nên tên khoa lặp lại* — có trùng. Muốn khử, thêm `distinct`. Đây là khác biệt nền giữa lý thuyết (set) và SQL (**multiset** / bag):

- Quan hệ toán học = **tập**: `{Physics, Finance, Comp.Sci.}`.
- Kết quả SQL = **multiset**: `[Physics, Finance, Physics, Comp.Sci., Comp.Sci.]` — trừ khi `distinct`.

> [!warning] Vì sao multiset lại *quan trọng*, không chỉ là chi tiết vụn
> `avg(salary)` phải đếm **cả bản trùng**: hai giảng viên cùng lương \$75,000 thì lương đó phải vào trung bình *hai lần*. Nếu SQL tự khử trùng như tập, trung bình sẽ **sai**. Giữ trùng không phải lười — nó *đúng về ngữ nghĩa* cho phép gộp (mục 4). (Silberschatz tr. 91–92 lấy đúng ví dụ này.)

## 3. JOIN: inner bỏ, outer giữ

Nhớ demo Bài 1: join `instructor ⋈ teaches` làm **biến mất** Wu và Gold (họ không dạy môn nào). Đó là hành vi mặc định của SQL:

> [!quote] Silberschatz (tr. 136)
> "To distinguish normal joins from outer joins, normal joins are called inner joins in SQL. [...] The default join type, when the join clause is used without the outer prefix, is the inner join."
>
> *Để phân biệt với outer join, join thường được gọi là **inner join**. [...] Kiểu join **mặc định**, khi dùng `join` không có tiền tố `outer`, là **inner join**.*

Inner join = `σθ(r×s)` của Bài 1 → **mất** những hàng không tìm được bạn khớp. Nhiều lúc đó là lỗi: "liệt kê *mọi* giảng viên kèm môn họ dạy (nếu có)" — Wu, Gold vẫn phải xuất hiện. Cần **outer join**:

> [!quote] Silberschatz (tr. 135)
> "outer join adds null-padded tuples only for those tuples that do not match"
>
> *outer join **thêm các bộ được đệm null** chỉ cho những bộ **không khớp**.*

- **`LEFT [OUTER] JOIN`**: giữ *mọi* hàng của bảng **trái**; bên phải thiếu thì điền `NULL`.
- **`RIGHT`** / **`FULL`**: tương tự cho bên phải / cả hai.

Vậy inner là *giao có điều kiện*, outer là *inner + những kẻ cô đơn được giữ lại với NULL*. Mục 6 cho thấy Wu/Gold vắng mặt ở inner nhưng hiện ra với `NULL` ở left join.

## 4. Gom nhóm, lọc nhóm, và thứ tự thực thi

**Aggregate** (hàm gộp) nén một tập giá trị thành một con số:

> [!quote] Silberschatz (tr. 91)
> "Aggregate functions are functions that take a collection (a set or multiset) of values as input and return a single value."

Năm hàm chuẩn: `avg, min, max, sum, count`. `group by` chia hàng thành **nhóm** (các hàng cùng giá trị khoá nhóm) rồi gộp *từng nhóm*. `having` lọc **trên nhóm** (sau khi gộp) — khác `where` lọc **trên hàng** (trước khi gộp). Lẫn hai cái này là lỗi SQL kinh điển.

Toàn bộ trật tự được định nghĩa rõ trong sách — **học thuộc nó**:

> [!quote] Silberschatz (tr. 95–96)
> "1. [...] the from clause is first evaluated to get a relation.
> 2. If a where clause is present, the predicate in the where clause is applied on the result relation of the from clause.
> 3. Tuples satisfying the where predicate are then placed into groups by the group by clause [...]
> 4. The having clause, if it is present, is applied to each group; the groups that do not satisfy the having clause predicate are removed.
> 5. The select clause uses the remaining groups to generate tuples of the result [...]"

```
   FROM        →  WHERE      →  GROUP BY   →  HAVING      →  SELECT   →  (ORDER BY)
   lấy quan hệ    lọc HÀNG      chia nhóm     lọc NHÓM       giữ cột      sắp xếp
   (×)            (σ)                         (σ trên nhóm)  (Π)
```

Hệ quả hay bị vấp: `where` **không** dùng được hàm gộp (lúc đó nhóm chưa hình thành); muốn lọc theo `avg`/`count` phải dùng `having`. Và `ORDER BY` chạy **cuối** — nhắc lại Bài 1: relation không có thứ tự, muốn thứ tự *phải nói rõ*.

## 5. Subquery và view

**Subquery** (truy vấn lồng) = một `select` nằm trong một `select` khác — tận dụng *tính đóng* của đại số (Bài 1): kết quả một truy vấn lại là quan hệ, nên dùng được làm đầu vào. Ví dụ "giảng viên lương trên trung bình toàn trường": so `salary` với `(select avg(salary) from instructor)`.

**View** (khung nhìn) = đặt tên cho một truy vấn, dùng như một bảng:

> [!quote] Silberschatz (tr. 137)
> "SQL allows a "virtual relation" to be defined by a query, and the relation conceptually contains the result of the query. The virtual relation is not precomputed and stored but instead is computed by executing the query whenever the virtual relation is used."
>
> *SQL cho định nghĩa một **"quan hệ ảo"** bằng một truy vấn; quan hệ này **không** được tính sẵn và lưu lại, mà **tính lại mỗi lần dùng**.*

View là hiện thân của **mức khung nhìn** (Bài 0): một `faculty` view bỏ cột `salary` cho nhân viên đào tạo thấy — vừa tiện (đóng gói truy vấn hay dùng) vừa là lớp **bảo mật**. Lưu ý "tính lại mỗi lần dùng": view *không* lưu dữ liệu, nên luôn khớp bảng gốc (khác *materialized view* — có lưu, phải làm mới; để sau).

## 6. Demo: SQL thật từ cơ bản tới view

Chạy trên SQLite thật qua `node:sqlite`. Tám câu truy vấn phủ hết mục 1–5 — chú ý hàng có trùng, Wu/Gold ở inner vs left join, HAVING loại nhóm, và view giấu lương:

```typescript
import { DatabaseSync } from "node:sqlite";
const db = new DatabaseSync(":memory:");

db.exec(`
  CREATE TABLE instructor(ID TEXT PRIMARY KEY, name TEXT, dept_name TEXT, salary INT);
  INSERT INTO instructor VALUES
    ('22222','Einstein','Physics',95000),
    ('12121','Wu','Finance',90000),
    ('33456','Gold','Physics',87000),
    ('10101','Srinivasan','Comp. Sci.',65000),
    ('45565','Katz','Comp. Sci.',75000);
  CREATE TABLE teaches(ID TEXT, course TEXT);
  INSERT INTO teaches VALUES
    ('22222','PHY-101'),('10101','CS-101'),('10101','CS-347'),('45565','CS-319');
`);
const q = (sql: string) => db.prepare(sql).all() as any[];
const fmt = (rows: any[]) => rows.map(r =>
  Object.values(r).map(v => v === null ? "NULL" : v).join(", ")).join(" | ");

// 1) SELECT-FROM-WHERE = Π(σ(×)) của Bài 1: where↔σ, select↔Π, from↔×
console.log("1) σ+Π: tên GV khoa Physics");
console.log("   ", fmt(q(`SELECT name FROM instructor WHERE dept_name='Physics' ORDER BY name`)));

// 2) SQL là MULTISET (khác 'relation là tập' ở Bài 1): trùng được giữ mặc định
const dup = q(`SELECT dept_name FROM instructor`).length;
const dist = q(`SELECT DISTINCT dept_name FROM instructor`).length;
console.log(`\n2) multiset: SELECT dept_name → ${dup} dòng (có trùng); SELECT DISTINCT dept_name → ${dist} khoa`);

// 3) INNER vs LEFT OUTER JOIN — GV không dạy môn nào: biến mất hay được giữ?
console.log("\n3a) INNER JOIN (mặc định) — chỉ GV có dạy:");
for (const r of q(`SELECT i.name, t.course FROM instructor i JOIN teaches t ON i.ID=t.ID
                   ORDER BY i.name, t.course`))
  console.log(`     ${r.name} → ${r.course}`);
console.log("    (Wu, Gold KHÔNG dạy → vắng mặt, hệt inner join ở Bài 1)");
console.log("3b) LEFT OUTER JOIN — giữ MỌI GV, chỗ thiếu điền NULL:");
for (const r of q(`SELECT i.name, t.course FROM instructor i LEFT JOIN teaches t ON i.ID=t.ID
                   ORDER BY i.name, t.course`))
  console.log(`     ${r.name} → ${r.course ?? "NULL"}`);

// 4) GROUP BY + HAVING: lương trung bình mỗi khoa, chỉ khoa > 80k
console.log("\n4) GROUP BY dept_name + HAVING avg(salary)>80000:");
for (const r of q(`SELECT dept_name, AVG(salary) AS avg_sal FROM instructor
                   GROUP BY dept_name HAVING AVG(salary) > 80000 ORDER BY dept_name`))
  console.log(`     ${r.dept_name}: ${r.avg_sal}`);
console.log("    (Comp. Sci. avg 70000 bị HAVING loại — HAVING lọc NHÓM, WHERE lọc HÀNG)");

// 5) Subquery: GV lương trên mức trung bình toàn trường
const avg = (q(`SELECT AVG(salary) a FROM instructor`)[0] as any).a;
console.log(`\n5) subquery: lương > trung bình toàn trường (${avg}):`);
for (const r of q(`SELECT name, salary FROM instructor
                   WHERE salary > (SELECT AVG(salary) FROM instructor)
                   ORDER BY salary DESC`))
  console.log(`     ${r.name}: ${r.salary}`);

// 6) VIEW: 'quan hệ ảo' che cột salary — không lưu, tính lại mỗi lần dùng
db.exec(`CREATE VIEW faculty AS SELECT ID, name, dept_name FROM instructor`);
console.log("\n6) VIEW faculty (giấu salary):");
console.log("   ", fmt(q(`SELECT * FROM faculty WHERE dept_name='Physics' ORDER BY name`)));

console.log("\nSQL = cú pháp của đại số quan hệ (Bài 1), + multiset, outer join, group/having,");
console.log("subquery, view. Thứ tự hiểu truy vấn: FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY.");
```

Kết quả chạy thật *(tất định)*:

```
1) σ+Π: tên GV khoa Physics
    Einstein | Gold

2) multiset: SELECT dept_name → 5 dòng (có trùng); SELECT DISTINCT dept_name → 3 khoa

3a) INNER JOIN (mặc định) — chỉ GV có dạy:
     Einstein → PHY-101
     Katz → CS-319
     Srinivasan → CS-101
     Srinivasan → CS-347
    (Wu, Gold KHÔNG dạy → vắng mặt, hệt inner join ở Bài 1)
3b) LEFT OUTER JOIN — giữ MỌI GV, chỗ thiếu điền NULL:
     Einstein → PHY-101
     Gold → NULL
     Katz → CS-319
     Srinivasan → CS-101
     Srinivasan → CS-347
     Wu → NULL

4) GROUP BY dept_name + HAVING avg(salary)>80000:
     Finance: 90000
     Physics: 91000
    (Comp. Sci. avg 70000 bị HAVING loại — HAVING lọc NHÓM, WHERE lọc HÀNG)

5) subquery: lương > trung bình toàn trường (82400):
     Einstein: 95000
     Wu: 90000
     Gold: 87000

6) VIEW faculty (giấu salary):
    22222, Einstein, Physics | 33456, Gold, Physics

SQL = cú pháp của đại số quan hệ (Bài 1), + multiset, outer join, group/having,
subquery, view. Thứ tự hiểu truy vấn: FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY.
```

Năm điều đáng thấm. **(1)** `SELECT name ... WHERE dept_name='Physics'` ra đúng `Πname(σ...)` của Bài 1 — SQL *là* đại số quan hệ. **(2)** `SELECT dept_name` cho **5** dòng (trùng), `DISTINCT` cho **3** — SQL là multiset, và chính nhờ giữ trùng mà `AVG` mới đúng. **(3)** Wu/Gold **vắng** ở inner join nhưng hiện với `NULL` ở left join — chọn sai kiểu join là lỗi logic *âm thầm*. **(4)** Comp. Sci. (avg 70000) bị `HAVING` loại: `HAVING` lọc nhóm *sau* khi gộp, `WHERE` lọc hàng *trước*. **(5)** View `faculty` trả dữ liệu không có cột `salary` — mức khung nhìn + bảo mật, tính lại mỗi lần, luôn khớp bảng gốc.

> [!note] Tự thử
> 1. Đổi `LEFT JOIN` ở 3b thành `INNER JOIN` rồi đếm số dòng: vì sao từ 6 xuống 4? Ai mất?
> 2. Ở câu 4, chuyển điều kiện `AVG(salary) > 80000` từ `HAVING` sang `WHERE` → SQLite báo lỗi gì? Vì sao `WHERE` không dùng được hàm gộp? (gợi ý: thứ tự thực thi mục 4.)
> 3. Thêm một giảng viên Comp. Sci. lương 92000. Chạy lại câu 4: Comp. Sci. giờ có qua `HAVING` không? Trung bình mới là bao nhiêu?
> 4. Tạo `CREATE VIEW high_paid AS SELECT name, salary FROM instructor WHERE salary > 85000`, rồi `SELECT * FROM high_paid`. Sửa lương Gold xuống 80000 rồi query lại view — kết quả đổi chứ? Vì sao (view tính lại, không lưu)?
> 5. Viết subquery "khoa có lương trung bình cao nhất" bằng `GROUP BY` lồng trong so sánh với `MAX`. (gợi ý: subquery trả về một bảng (dept_name, avg) rồi lọc.)

## 7. Bản đồ khoá database

| # | Bài | Mảng | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | DBMS là gì & vì sao cần | động lực, trừu tượng hoá | Silberschatz Ch1 |
| 1 | Mô hình quan hệ & đại số quan hệ | nền toán của bảng/SQL | Ch2 |
| 2 | **SQL từ nền tới sâu** ← *đang ở đây* | truy vấn, join, view | Ch3–5 |
| 3 | Thiết kế & chuẩn hoá (E-R, FD, BCNF) | thiết kế đúng | Ch6–7 |
| 4 | Lưu trữ vật lý & buffer manager | dữ liệu trên đĩa/RAM | Ch12–13 |
| 5 | Index: B+tree | tra cứu nhanh | Ch14 |
| 6 | Index nâng cao: LSM & bitmap | tối ưu ghi/phân tích | Ch24 |
| 7 | Xử lý truy vấn: join algorithms | thực thi truy vấn | Ch15 |
| 8 | Tối ưu truy vấn (cost-based) | chọn kế hoạch rẻ nhất | Ch16 |
| 9 | Transaction & ACID, isolation | đúng khi có lỗi | Ch17 |
| 10 | Đồng thời: 2PL / MVCC | đúng khi song song | Ch18 |
| 11 | Phục hồi: WAL / ARIES | sống sót sau sập | Ch19 |
| 12 | Song song & phân tán (góc DB) | mở rộng ra nhiều máy | Ch20–23 + Red Book |

## 8. Thẻ ôn (active recall)

> [!question] Thẻ 2.1 — Ba mệnh đề cơ bản của SQL và chúng ứng với toán tử đại số nào?
> **Đáp:** `from` ↔ × (nguồn quan hệ), `where` ↔ σ (lọc hàng), `select` ↔ Π (giữ cột).

> [!question] Thẻ 2.2 — SQL khác đại số quan hệ ở "tập vs multiset" thế nào? Vì sao?
> **Đáp:** đại số: quan hệ là *tập* (không trùng). SQL: *multiset*, giữ trùng mặc định vì khử trùng tốn kém — và giữ trùng cần cho `AVG`/`SUM` đúng. Muốn khử: `DISTINCT`.

> [!question] Thẻ 2.3 — Inner join và outer join khác nhau ra sao?
> **Đáp:** inner (mặc định) = `σθ(r×s)`, **bỏ** hàng không khớp. `LEFT/RIGHT/FULL OUTER` **giữ** hàng không khớp, đệm `NULL` cho bên thiếu.

> [!question] Thẻ 2.4 — WHERE và HAVING khác nhau chỗ nào? Thứ tự thực thi?
> **Đáp:** `WHERE` lọc **hàng** (trước gộp), `HAVING` lọc **nhóm** (sau gộp, dùng được hàm gộp). Thứ tự: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY.

> [!question] Thẻ 2.5 — View là gì? Nó có lưu dữ liệu không?
> **Đáp:** "quan hệ ảo" định nghĩa bằng một truy vấn; **không** lưu, **tính lại mỗi lần dùng** → luôn khớp bảng gốc. Dùng để đóng gói truy vấn + che cột (bảo mật, mức khung nhìn).

## 9. Câu hỏi tự kiểm tra

1. Viết lại `Πname(σsalary>80000(instructor))` của Bài 1 thành SQL. Chỉ ra phần nào là σ, phần nào Π. *(mục 1)*
2. Vì sao `select dept_name from instructor` trả hàng trùng còn đại số quan hệ thì không? Khi nào *phải* giữ trùng để kết quả đúng? *(mục 2)*
3. Một truy vấn "mọi giảng viên kèm số môn họ dạy (kể cả 0)" nên dùng join kiểu gì? Nếu dùng inner thì sai thế nào? *(mục 3, 6)*
4. Giải thích thứ tự FROM→WHERE→GROUP BY→HAVING→SELECT. Vì sao không thể lọc theo `avg()` trong `WHERE`? *(mục 4)*
5. Chạy demo mục 6, làm Tự thử 4 (view tính lại). View khác bảng thường và materialized view ở điểm nào? *(mục 5, 6)*

## Tóm tắt một trang

```
BÀI 2 — SQL TỪ NỀN TỚI SÂU
─────────────────────────────────────────────────────────
SQL = ĐẠI SỐ QUAN HỆ + thực dụng.  select↔Π, from↔×, where↔σ (Silberschatz tr.71).

MULTISET  đại số: quan hệ là TẬP (không trùng). SQL: MULTISET, giữ trùng mặc định
   (khử trùng tốn kém; và cần cho AVG/SUM đúng). DISTINCT để khử. (tr.72)

JOIN  inner (mặc định) = σθ(r×s), BỎ hàng không khớp (Wu/Gold biến mất).
   LEFT/RIGHT/FULL OUTER = GIỮ hàng không khớp, đệm NULL. (tr.135–136)

GỘP  avg/min/max/sum/count. GROUP BY chia nhóm; HAVING lọc NHÓM (sau gộp),
   WHERE lọc HÀNG (trước gộp). THỨ TỰ: FROM→WHERE→GROUP BY→HAVING→SELECT→ORDER BY
   (tr.95–96). ORDER BY cuối — relation vốn không thứ tự.

SUBQUERY  select trong select (nhờ tính đóng Bài 1).  VIEW = quan hệ ảo định nghĩa
   bằng truy vấn, KHÔNG lưu, tính lại mỗi lần → mức khung nhìn + bảo mật. (tr.137)
```

## Nguồn

- **Silberschatz, Korth, Sudarshan — *Database System Concepts*, 7th ed.** — **Ch3 Introduction to SQL**: cấu trúc select-from-where (tr. 71), multiset/distinct (tr. 72), aggregate + group by + having + thứ tự thực thi (tr. 91–96); **Ch4 Intermediate SQL**: outer join (tr. 135–136), views (tr. 137). `tai_lieu/Database System Concepts 7th Edition...pdf` (offset **PDF = tr. + 29**).
- Liên hệ: [cloud-base Bài 17 — data models](../../cloud-base/bai_hoc/bai_17_du-lieu-data-models.md) (SQL vs NoSQL ở góc ứng dụng).

---

**Bản đồ khoá học:** [Bài 0 — DBMS là gì](bai_00_dbms-la-gi.md) · [Bài 1 — Mô hình quan hệ & đại số quan hệ](bai_01_mo-hinh-quan-he.md) · **[Bài 2 — SQL từ nền tới sâu] ← bạn đang ở đây** · [Bài 3 — Thiết kế & chuẩn hoá](bai_03_thiet-ke-chuan-hoa.md) · [Bài 4 — Lưu trữ & buffer manager](bai_04_luu-tru-buffer.md) · [Bài 5 — Index: B+tree](bai_05_index-btree.md) · [Bài 6 — Index nâng cao: LSM & bitmap](bai_06_index-lsm-bitmap.md) · [Bài 7 — Join algorithms](bai_07_query-join.md) · [Bài 8 — Tối ưu truy vấn](bai_08_query-optimization.md) · [Bài 9 — Transaction & ACID](bai_09_transaction-acid.md) · [Bài 10 — Đồng thời: 2PL/MVCC](bai_10_concurrency.md) · [Bài 11 — Phục hồi: WAL/ARIES](bai_11_recovery.md) · [Bài 12 — Song song & phân tán](bai_12_phan-tan.md)

Xem thêm [README khoá học](../README.md).
