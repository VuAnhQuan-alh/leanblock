# Bài 1 — Mô hình quan hệ và đại số quan hệ

> [!info] Về bài này
> Bài 0 cho thấy *vì sao* cần DBMS. Giờ ta dựng **nền**: mô hình thống trị ngành — **mô hình quan hệ** (dữ liệu là các *bảng*) — và cỗ máy toán nằm dưới mọi câu SQL: **đại số quan hệ**. Hiểu lớp này thì Bài 2 (SQL) chỉ còn là cú pháp, và Bài 8 (tối ưu truy vấn) mới có chỗ bấu víu.
> Nguồn (Luật số 1): **Silberschatz** *Database System Concepts 7e* — **Chapter 2: Introduction to the Relational Model** (offset PDF = tr. + 29).
> **Chạy demo:** **Node 22+**, `node <tên>.ts` — không cài gói.
> Nên đọc trước: [Bài 0 — DBMS là gì](bai_00_dbms-la-gi.md).

## Mục lục

1. [Vì sao dữ liệu dạng bảng lại thống trị](#1-vì-sao-dữ-liệu-dạng-bảng-lại-thống-trị)
2. [Thuật ngữ chính xác: relation, tuple, attribute](#2-thuật-ngữ-chính-xác-relation-tuple-attribute)
3. [Khoá: cách phân biệt và nối các bộ](#3-khoá-cách-phân-biệt-và-nối-các-bộ)
4. [Đại số quan hệ: sáu toán tử nền](#4-đại-số-quan-hệ-sáu-toán-tử-nền)
5. [Demo: tự viết evaluator đại số quan hệ](#5-demo-tự-viết-evaluator-đại-số-quan-hệ)
6. [Bản đồ khoá database](#6-bản-đồ-khoá-database)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Vì sao dữ liệu dạng bảng lại thống trị

Trước mô hình quan hệ, dữ liệu được tổ chức theo *mạng* (network) hay *phân cấp* (hierarchical) — lập trình viên phải tự lần theo con trỏ giữa các bản ghi. E.F. Codd (1970) đề xuất một ý tưởng cấp tiến: biểu diễn *mọi thứ* bằng **bảng**, và truy vấn bằng **toán học** thay vì duyệt con trỏ tay.

> [!quote] Silberschatz (tr. 37)
> "The relational model remains the primary data model for commercial data-processing applications. It attained its primary position because of its simplicity, which eases the job of the programmer [...] The relational model's independence from any specific underlying low-level data structures has allowed it to persist [...]"
>
> *Mô hình quan hệ vẫn là mô hình dữ liệu **chính** cho ứng dụng thương mại. Nó lên ngôi nhờ **sự đơn giản**, làm nhẹ việc của lập trình viên [...] Việc **độc lập với cấu trúc lưu trữ cấp thấp** giúp nó tồn tại bền bỉ [...]*

Hai chữ vàng: **đơn giản** (bảng ai cũng hiểu) và **độc lập vật lý** (bạn viết truy vấn trên *bảng*, DBMS tự lo lưu bằng B-tree hay column-store (lưu theo cột) dưới đất — chính là mức *logic* vs *vật lý* ở Bài 0). Nhờ độc lập đó, mô hình quan hệ sống qua nửa thế kỷ dù phần cứng và cách lưu trữ thay đổi hoàn toàn.

## 2. Thuật ngữ chính xác: relation, tuple, attribute

Dân lập trình quen gọi "bảng / hàng / cột". Lý thuyết quan hệ dùng từ chính xác hơn — và sự chính xác đó có hệ quả:

> [!quote] Silberschatz (tr. 39)
> "in the relational model the term relation is used to refer to a table, while the term tuple is used to refer to a row. Similarly, the term attribute refers to a column of a table."
>
> *trong mô hình quan hệ, **relation** (quan hệ) chỉ một **bảng**, **tuple** (bộ) chỉ một **hàng**, và **attribute** (thuộc tính) chỉ một **cột**.*

Vì sao tên "relation"? Vì một hàng là một *bộ n giá trị* (n-tuple) — biểu diễn toán học của "mối quan hệ giữa n giá trị". Một bảng = một *tập* các bộ → gần đúng khái niệm **quan hệ** trong toán. Chữ "tập" (set) kéo theo hai tính chất **sống còn**:

> [!quote] Silberschatz (tr. 39)
> "The order in which tuples appear in a relation is irrelevant, since a relation is a set of tuples."
>
> *Thứ tự các bộ trong một quan hệ **không quan trọng**, vì quan hệ là một **tập** các bộ.*

- **Không thứ tự.** Bảng sắp hay chưa sắp vẫn là *cùng một* quan hệ. (Nên khi cần thứ tự trong SQL, bạn phải nói rõ `ORDER BY` — Bài 2.)
- **Không trùng.** Tập không có phần tử lặp → về lý thuyết không có hai bộ y hệt. *(Lưu ý: SQL thực tế **nới** điều này, cho phép hàng trùng — multiset; ta bàn ở Bài 2.)*

Thêm ba khái niệm nền:

- **Domain** (miền giá trị) của một thuộc tính = tập giá trị được phép. Yêu cầu: domain phải **atomic** — "nguyên tử", không chia nhỏ. Lưu một *tập* số điện thoại vào một ô là vi phạm (Bài 3 — chuẩn hoá 1NF sẽ mổ kỹ).
- **Null** = giá trị đặc biệt báo *không biết* hoặc *không tồn tại*. Sách cảnh báo thẳng: null *"should be eliminated if at all possible"* vì nó gây rối khi truy vấn/cập nhật.
- **Schema vs instance** (nhắc lại Bài 0): `instructor(ID, name, dept_name, salary)` là **schema** (đổi hiếm); 12 dòng dữ liệu cụ thể là một **instance** (đổi liên tục).

## 3. Khoá: cách phân biệt và nối các bộ

Nếu không có hai bộ trùng nhau, phải có cách *chỉ mặt* từng bộ. Đó là **khoá** — và có một thang bậc:

> [!quote] Silberschatz (tr. 43)
> "A superkey is a set of one or more attributes that, taken collectively, allow us to identify uniquely a tuple in the relation."
>
> ***Superkey** (siêu khoá) là tập một-hoặc-nhiều thuộc tính mà, **gộp lại**, cho phép nhận diện **duy nhất** một bộ trong quan hệ.*

- **Superkey** — bất kỳ tập thuộc tính nào định danh được bộ. `{ID}` là superkey; `{ID, name}` cũng là (nhưng thừa).
- **Candidate key** (khoá dự tuyển) — superkey **tối tiểu** (bỏ bớt thuộc tính nào cũng mất tính định danh). `{ID}` là candidate key; `{ID, name}` thì không (vì `{ID}` đã đủ).
- **Primary key** (khoá chính) — candidate key *được nhà thiết kế chọn* làm phương tiện định danh chính.

> [!quote] Silberschatz (tr. 44)
> "We shall use the term primary key to denote a candidate key that is chosen by the database designer as the principal means of identifying tuples within a relation."

Nguyên tắc chọn primary key: giá trị **gần như không bao giờ đổi** (đừng lấy địa chỉ làm khoá — nó đổi; số định danh sinh ra thì bền).

- **Foreign key** (khoá ngoại, tr. 45) — ràng buộc rằng giá trị một thuộc tính ở bảng này **phải tồn tại** làm primary key ở bảng kia. `instructor.dept_name` là foreign key trỏ tới `department.dept_name`: không cho phép giảng viên thuộc một khoa *không có thật*. Đây là chốt giữ **toàn vẹn tham chiếu** — chữa "bệnh 4" ở Bài 0.

## 4. Đại số quan hệ: sáu toán tử nền

Làm sao *hỏi* dữ liệu một cách hình thức? Đại số quan hệ.

> [!quote] Silberschatz (tr. 48)
> "The relational algebra consists of a set of operations that take one or two relations as input and produce a new relation as their result."
>
> *Đại số quan hệ gồm một tập toán tử, **nhận một hoặc hai quan hệ** làm đầu vào và **sinh ra một quan hệ mới** làm kết quả.*

Câu này chứa ý tưởng mạnh nhất của cả chương: **tính đóng** (closure). Vì mỗi toán tử *trả về một relation*, kết quả lại làm đầu vào cho toán tử tiếp theo — hệt như `(3 + 4) × 2` ghép các phép số học. Nhờ đó mọi truy vấn phức tạp đều là **biểu thức** ghép từ ít toán tử nền:

| Toán tử | Ký hiệu | Làm gì | Ngôi |
| :-- | :--: | :-- | :-- |
| Select (chọn) | σ | giữ các bộ *thoả điều kiện* | 1 |
| Project (chiếu) | Π | giữ một số *cột* (khử trùng) | 1 |
| Cartesian product (tích) | × | ghép **mọi cặp** bộ của hai quan hệ | 2 |
| Union (hợp) | ∪ | bộ có ở quan hệ này *hoặc* kia | 2 |
| Set difference (hiệu) | − | bộ có ở quan hệ này *mà không* ở kia | 2 |
| Rename (đổi tên) | ρ | đặt tên mới cho quan hệ/cột | 1 |

Sáu cái trên là **đủ** (các phép khác suy ra được). Quan trọng nhất về mặt engine là **join** `⋈` — và nó *không phải* toán tử nền, mà là viết gọn của hai phép:

> [!quote] Silberschatz (tr. 53)
> "The join operation allows us to combine a selection and a Cartesian product into a single operation. [...] r ⋈θ s = σθ (r × s)"
>
> *Phép **join** gộp một phép **chọn** và một phép **tích Descartes** thành một. [...] `r ⋈θ s = σθ(r × s)`*

Nhớ đẳng thức `r ⋈θ s = σθ(r × s)` này — nó là lý do Bài 7 (join algorithms) và Bài 8 (tối ưu) tồn tại: tích Descartes thì *khổng lồ* (|r|×|s| hàng), nên engine **không bao giờ** tính nó rồi mới lọc; nó tìm cách ra thẳng kết quả join. Mục 5 cài đúng đẳng thức này để thấy nó đúng từng hàng.

## 5. Demo: tự viết evaluator đại số quan hệ

Ta cài sáu toán tử như *hàm trên tập hàng*, rồi chứng minh `⋈ = σθ(×)` và tính đóng (ghép Π sau σ):

```typescript
import { strict as assert } from "node:assert";

// Một quan hệ (relation) = TẬP các bộ (tuple). Bộ = hàng; thuộc tính = cột.
type Row = Record<string, string | number>;
type Relation = Row[];

// Vì relation là TẬP: không trùng, không thứ tự quan trọng. Ta khử trùng theo
// nội dung hàng (sắp khoá để {a,b} == {b,a}).
const rowKey = (r: Row) => JSON.stringify(Object.keys(r).sort().map(k => [k, r[k]]));
function dedup(rel: Relation): Relation {
  const seen = new Set<string>(); const out: Relation = [];
  for (const r of rel) { const k = rowKey(r); if (!seen.has(k)) { seen.add(k); out.push(r); } }
  return out;
}

// ─── Sáu toán tử nền của đại số quan hệ — MỖI toán tử nhận relation, TRẢ relation
//     (tính "đóng" → ghép tự do thành biểu thức, như +−×÷ của số học) ───
const select  = (rel: Relation, pred: (r: Row) => boolean): Relation => rel.filter(pred);            // σ
const project = (rel: Relation, cols: string[]): Relation =>                                          // Π
  dedup(rel.map(r => Object.fromEntries(cols.map(c => [c, r[c]]))));
function product(a: Relation, b: Relation): Relation {                                                // ×
  const out: Relation = [];
  for (const x of a) for (const y of b) {
    const row: Row = {};
    for (const k in x) row[`l.${k}`] = x[k];   // gắn tiền tố để ID của 2 bên không đè nhau
    for (const k in y) row[`r.${k}`] = y[k];
    out.push(row);
  }
  return out;
}
const join = (a: Relation, b: Relation, pred: (r: Row) => boolean): Relation => select(product(a, b), pred); // ⋈ = σθ(a×b)
const union      = (a: Relation, b: Relation): Relation => dedup([...a, ...b]);                        // ∪
const difference = (a: Relation, b: Relation): Relation => {                                           // −
  const inB = new Set(b.map(rowKey)); return a.filter(r => !inB.has(rowKey(r)));
};

const show = (rel: Relation) =>
  rel.length ? rel.map(r => Object.entries(r).map(([k, v]) => `${k}=${v}`).join(", ")).join(" | ") : "(rỗng)";

// ─── Dữ liệu mẫu (rút gọn từ bảng đại học của Silberschatz) ───
const instructor: Relation = [
  { ID: "22222", name: "Einstein",   dept_name: "Physics",    salary: 95000 },
  { ID: "12121", name: "Wu",         dept_name: "Finance",    salary: 90000 },
  { ID: "33456", name: "Gold",       dept_name: "Physics",    salary: 87000 },
  { ID: "10101", name: "Srinivasan", dept_name: "Comp. Sci.", salary: 65000 },
];
const teaches: Relation = [
  { ID: "22222", course: "PHY-101" },
  { ID: "10101", course: "CS-101" },
  { ID: "10101", course: "CS-347" },
];

console.log("σ  dept_name=Physics          :", show(select(instructor, r => r.dept_name === "Physics")));
console.log("Π  name,salary           :", show(project(instructor, ["name", "salary"])));
console.log("Π name(σ dept_name=Physics)   :", show(project(select(instructor, r => r.dept_name === "Physics"), ["name"])));
console.log(`×  instructor×teaches     : ${product(instructor, teaches).length} hàng (= 4×3, ghép mọi cặp)`);

const joined = join(instructor, teaches, r => r["l.ID"] === r["r.ID"]);
console.log("⋈  instructor.ID=teaches.ID:");
for (const r of joined) console.log(`     ${r["l.name"]} dạy ${r["r.course"]}`);
console.log("   → Wu, Gold không dạy môn nào nên BIẾN MẤT khỏi join");

// Chân lý nền: JOIN chỉ là CHỌN trên TÍCH DESCARTES — assert khớp từng hàng.
const viaDef = select(product(instructor, teaches), r => r["l.ID"] === r["r.ID"]);
assert.deepEqual(joined, viaDef);
console.log("\n⋈ == σθ(r×s) ?           :", JSON.stringify(joined) === JSON.stringify(viaDef));

// relation là TẬP → Π tự khử trùng: 4 giảng viên nhưng chỉ 3 khoa khác nhau.
console.log("Π dept_name (khử trùng)       :", show(project(instructor, ["dept_name"])), "→ 3 khoa, không phải 4");

// ∪ và − trên hai tập môn học
const fall   = [{ course: "CS-101" }, { course: "PHY-101" }];
const spring = [{ course: "CS-101" }, { course: "CS-347" }];
console.log("∪  fall ∪ spring         :", show(union(fall, spring)), "→ CS-101 chỉ 1 lần");
console.log("−  fall − spring         :", show(difference(fall, spring)));

console.log("\n6 toán tử đóng kín trên 'relation' → ghép thành biểu thức bất kỳ.");
console.log("Đây là NỀN TOÁN của SQL (Bài 2) và của trình tối ưu truy vấn (Bài 8).");
```

Kết quả chạy thật *(tất định)*:

```
σ  dept_name=Physics          : ID=22222, name=Einstein, dept_name=Physics, salary=95000 | ID=33456, name=Gold, dept_name=Physics, salary=87000
Π  name,salary           : name=Einstein, salary=95000 | name=Wu, salary=90000 | name=Gold, salary=87000 | name=Srinivasan, salary=65000
Π name(σ dept_name=Physics)   : name=Einstein | name=Gold
×  instructor×teaches     : 12 hàng (= 4×3, ghép mọi cặp)
⋈  instructor.ID=teaches.ID:
     Einstein dạy PHY-101
     Srinivasan dạy CS-101
     Srinivasan dạy CS-347
   → Wu, Gold không dạy môn nào nên BIẾN MẤT khỏi join

⋈ == σθ(r×s) ?           : true
Π dept_name (khử trùng)       : dept_name=Physics | dept_name=Finance | dept_name=Comp. Sci. → 3 khoa, không phải 4
∪  fall ∪ spring         : course=CS-101 | course=PHY-101 | course=CS-347 → CS-101 chỉ 1 lần
−  fall − spring         : course=PHY-101

6 toán tử đóng kín trên 'relation' → ghép thành biểu thức bất kỳ.
Đây là NỀN TOÁN của SQL (Bài 2) và của trình tối ưu truy vấn (Bài 8).
```

Bốn điều đáng thấm. **(1) Mỗi toán tử trả về relation** → `project(select(...))` ghép được tự nhiên: đó là *tính đóng*, là lý do đại số này mạnh. **(2) `⋈ == σθ(r×s)` in ra `true`** — join đúng là "chọn trên tích Descartes", y hệt định nghĩa sách. **(3) Join loại bỏ bộ không khớp:** Wu và Gold biến mất vì không có dòng teaches nào khớp ID — đây là *inner join*, khác `LEFT JOIN` (Bài 2). **(4) `Π dept_name` trả 3 chứ không 4** — relation là *tập*, trùng tự biến mất. Cài thật một lần, các khái niệm này hết trừu tượng.

> [!warning] Vì sao engine không làm y hệt demo
> Demo tính `×` (12 hàng) rồi mới lọc còn 3. Với bảng triệu dòng, tích Descartes là *tỉ tỉ* hàng — bất khả thi. Trình tối ưu (Bài 8) *không bao giờ* vật chất hoá `×`; nó dùng **thuật toán join** (hash/merge, Bài 7) để ra thẳng 3 hàng. Đại số cho biết *kết quả đúng là gì*; engine tự do chọn *đường tính rẻ nhất* — miễn ra cùng một relation.

> [!note] Tự thử
> 1. Thêm toán tử **intersection** `∩` (giao): `a ∩ b` = bộ có ở *cả hai*. Viết bằng `difference` (gợi ý: `a − (a − b)`), rồi kiểm với `fall`, `spring` (phải ra `CS-101`).
> 2. Đổi predicate join thành `r["l.salary"] > 90000 && r["l.ID"] === r["r.ID"]` — "giảng viên lương > 90k và môn họ dạy". Ai còn lại?
> 3. `product` hiện gắn tiền tố `l.`/`r.`. Bỏ tiền tố đi rồi join hai bảng cùng có cột `ID` — chuyện gì xảy ra, và vì sao ta *cần* `rename`/tiền tố?
> 4. `union(instructor, teaches)` sẽ ra gì về mặt cột? Vì sao đại số đòi hai quan hệ **tương thích** (cùng số cột, cùng kiểu) mới cho hợp?

## 6. Bản đồ khoá database

| # | Bài | Mảng | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | DBMS là gì & vì sao cần | động lực, trừu tượng hoá | Silberschatz Ch1 |
| 1 | **Mô hình quan hệ & đại số quan hệ** ← *đang ở đây* | nền toán của bảng/SQL | Ch2 |
| 2 | SQL từ nền tới sâu | truy vấn, join, view | Ch3–5 |
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

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 1.1 — relation, tuple, attribute lần lượt là gì?
> **Đáp:** relation = bảng; tuple = hàng; attribute = cột. Relation là một *tập* các tuple.

> [!question] Thẻ 1.2 — "Relation là một tập" kéo theo hai tính chất gì?
> **Đáp:** (1) **không thứ tự** (sắp hay không vẫn cùng một quan hệ → cần `ORDER BY` khi muốn thứ tự); (2) **không trùng** bộ (SQL thực tế nới thành multiset).

> [!question] Thẻ 1.3 — Phân biệt superkey, candidate key, primary key.
> **Đáp:** superkey = tập thuộc tính định danh duy nhất một bộ (có thể thừa); candidate key = superkey *tối tiểu*; primary key = candidate key *được chọn* làm chính. Foreign key = ràng buộc trỏ tới primary key bảng khác (toàn vẹn tham chiếu).

> [!question] Thẻ 1.4 — "Tính đóng" của đại số quan hệ là gì? Vì sao quan trọng?
> **Đáp:** mỗi toán tử *nhận relation, trả relation* → kết quả ghép được làm đầu vào toán tử sau. Nhờ đó mọi truy vấn phức tạp = biểu thức ghép từ vài toán tử nền.

> [!question] Thẻ 1.5 — Viết join theo select và cartesian product.
> **Đáp:** `r ⋈θ s = σθ(r × s)` — join = chọn (theo θ) trên tích Descartes. Engine không tính `×` thật mà dùng thuật toán join (Bài 7).

## 8. Câu hỏi tự kiểm tra

1. Vì sao mô hình quan hệ "độc lập vật lý" lại giúp nó sống bền nửa thế kỷ? Liên hệ 3 mức trừu tượng Bài 0. *(mục 1)*
2. Một quan hệ có được phép có hai hàng y hệt không, theo lý thuyết? SQL thực tế thì sao? *(mục 2)*
3. Cho bảng `student(ID, email, name)` với cả `ID` lẫn `email` đều duy nhất. Liệt kê superkey, candidate key; nên chọn primary key nào, vì sao? *(mục 3)*
4. Giải thích `r ⋈θ s = σθ(r × s)`. Vì sao engine *không* tính theo đúng công thức này? *(mục 4, 5 warning)*
5. Chạy demo mục 5, làm Tự thử 1 (thêm `∩`). Vì sao `∩` suy ra được từ `−`? *(mục 5)*

## Tóm tắt một trang

```
BÀI 1 — MÔ HÌNH QUAN HỆ & ĐẠI SỐ QUAN HỆ
─────────────────────────────────────────────────────────
VÌ SAO BẢNG THỐNG TRỊ  đơn giản + ĐỘC LẬP VẬT LÝ (viết truy vấn trên bảng,
   DBMS tự lo lưu dưới đất) → sống bền nửa thế kỷ (Silberschatz tr.37).

THUẬT NGỮ  relation=bảng, tuple=hàng, attribute=cột. Relation là TẬP →
   (1) KHÔNG thứ tự  (2) KHÔNG trùng (SQL nới thành multiset). domain atomic;
   null nên tránh. schema (thiết kế) vs instance (dữ liệu lúc chạy).

KHOÁ  superkey (định danh, có thể thừa) ⊃ candidate key (tối tiểu) → primary
   key (được chọn; giá trị bền, đừng đổi). foreign key → trỏ PK bảng khác =
   toàn vẹn tham chiếu.

ĐẠI SỐ QUAN HỆ  6 toán tử nền: σ chọn, Π chiếu, × tích, ∪ hợp, − hiệu, ρ đổi tên.
   TÍNH ĐÓNG: mỗi op trả relation → ghép thành biểu thức. JOIN ⋈ = σθ(r×s)
   (KHÔNG phải toán tử nền). Engine KHÔNG tính × thật → dùng join algo (Bài 7).

NỀN CHO  SQL (Bài 2) = cú pháp của đại số này; tối ưu truy vấn (Bài 8) = chọn
   biểu thức tương đương RẺ nhất.
```

## Nguồn

- **Silberschatz, Korth, Sudarshan — *Database System Concepts*, 7th ed.** — **Chapter 2: Introduction to the Relational Model**: cấu trúc quan hệ (relation/tuple/attribute/domain/null), schema vs instance, khoá (super/candidate/primary/foreign, tr. 43–45), đại số quan hệ (σ Π × ∪ − ρ, join = σθ(r×s), tr. 48–57). `tai_lieu/Database System Concepts 7th Edition...pdf` (offset **PDF = tr. + 29**).
- Liên hệ: [cloud-base Bài 17 — data models](../../cloud-base/bai_hoc/bai_17_du-lieu-data-models.md) nhìn quan hệ/document/graph từ góc chọn mô hình cho ứng dụng.

---

**Bản đồ khoá học:** [Bài 0 — DBMS là gì](bai_00_dbms-la-gi.md) · **[Bài 1 — Mô hình quan hệ & đại số quan hệ] ← bạn đang ở đây** · [Bài 2 — SQL từ nền tới sâu](bai_02_sql.md) · [Bài 3 — Thiết kế & chuẩn hoá](bai_03_thiet-ke-chuan-hoa.md) · [Bài 4 — Lưu trữ & buffer manager](bai_04_luu-tru-buffer.md) · [Bài 5 — Index: B+tree](bai_05_index-btree.md) · [Bài 6 — Index nâng cao: LSM & bitmap](bai_06_index-lsm-bitmap.md) · [Bài 7 — Join algorithms](bai_07_query-join.md) · [Bài 8 — Tối ưu truy vấn](bai_08_query-optimization.md) · [Bài 9 — Transaction & ACID](bai_09_transaction-acid.md) · [Bài 10 — Đồng thời: 2PL/MVCC](bai_10_concurrency.md) · [Bài 11 — Phục hồi: WAL/ARIES](bai_11_recovery.md) · [Bài 12 — Song song & phân tán](bai_12_phan-tan.md)

Xem thêm [README khoá học](../README.md).
