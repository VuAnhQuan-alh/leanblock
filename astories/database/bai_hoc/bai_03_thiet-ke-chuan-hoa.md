# Bài 3 — Thiết kế và chuẩn hoá

> [!info] Về bài này
> Bài 1–2 cho ta *bảng* và *SQL*. Nhưng **bảng nào**? Nhồi mọi thứ vào một bảng to thì truy vấn dễ mà dữ liệu *mục ruỗng* vì lặp. Bài này dạy cách **thiết kế đúng**: vẽ thế giới bằng **E-R**, phát hiện lặp bằng **phụ thuộc hàm (FD)**, và cắt bảng về dạng chuẩn **BCNF** — có thuật toán, không phải cảm tính.
> Nguồn (Luật số 1): **Silberschatz** *Database System Concepts 7e* — **Ch6 (E-R Model)**, **Ch7 (Relational Database Design)** (offset PDF = tr. + 29).
> **Chạy demo:** **Node 22+**, `node <tên>.ts` — không cài gói.
> Nên đọc trước: [Bài 1 — Mô hình quan hệ](bai_01_mo-hinh-quan-he.md) (khoá, domain atomic), [Bài 2 — SQL](bai_02_sql.md).

## Mục lục

1. [Thiết kế tồi: bảng gộp và dư thừa](#1-thiết-kế-tồi-bảng-gộp-và-dư-thừa)
2. [E-R: vẽ thế giới trước khi dựng bảng](#2-e-r-vẽ-thế-giới-trước-khi-dựng-bảng)
3. [Phụ thuộc hàm: ngôn ngữ của ràng buộc](#3-phụ-thuộc-hàm-ngôn-ngữ-của-ràng-buộc)
4. [BCNF: định nghĩa và cách phân rã](#4-bcnf-định-nghĩa-và-cách-phân-rã)
5. [Demo: kiểm FD và phân rã BCNF](#5-demo-kiểm-fd-và-phân-rã-bcnf)
6. [Bản đồ khoá database](#6-bản-đồ-khoá-database)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Thiết kế tồi: bảng gộp và dư thừa

Giả sử để khỏi phải `JOIN`, ta gộp *giảng viên* và *khoa* vào một bảng `in_dep`:

```
in_dep(ID, name, salary, dept_name, building, budget)

ID     name        salary  dept_name    building  budget
22222  Einstein    95000   Physics      Watson    70000
33456  Gold        87000   Physics      Watson    70000     ← Watson, 70000 LẶP LẠI
10101  Srinivasan  65000   Comp. Sci.   Taylor    100000
45565  Katz        75000   Comp. Sci.   Taylor    100000    ← Taylor, 100000 LẶP LẠI
12121  Wu          90000   Finance      Painter   120000
```

Mỗi khoa có *một* toà nhà và *một* ngân sách — nhưng thông tin đó bị **chép lại cho mỗi giảng viên** của khoa. Hậu quả (chính là "bệnh 1" ở Bài 0, nay nhìn ở tầng thiết kế):

- **Dư thừa**: `(Physics, Watson, 70000)` lưu 2 lần, `(Comp. Sci., Taylor, 100000)` 2 lần.
- **Bất thường cập nhật**: Physics đổi ngân sách → phải sửa *mọi* dòng Physics; sót một dòng là dữ liệu mâu thuẫn.
- **Bất thường chèn**: không thể thêm một khoa *chưa có giảng viên nào* (thiếu ID — mà ID là khoá).
- **Bất thường xoá**: xoá giảng viên cuối của một khoa → *mất luôn* thông tin toà nhà/ngân sách của khoa đó.

Cách chữa duy nhất: **tách** `in_dep` thành hai bảng nhỏ (`instructor`, `department`). Nhưng tách *thế nào* cho đúng, không mất thông tin? Cần công cụ hình thức — mục 3, 4.

## 2. E-R: vẽ thế giới trước khi dựng bảng

Trước khi nghĩ tới bảng, nhà thiết kế mô hình *thế giới thực* bằng **mô hình thực thể–liên kết (E-R)**:

> [!quote] Silberschatz (tr. 244)
> "The E-R data model employs three basic concepts: entity sets, relationship sets, and attributes."
>
> *Mô hình E-R dùng **ba khái niệm nền**: tập thực thể (entity set), tập liên kết (relationship set), và thuộc tính (attribute).*

- **Entity** (thực thể) = một "vật" phân biệt được: một *giảng viên*, một *khoa*. Tập các thực thể cùng loại = **entity set** → thường thành **một bảng**.
- **Relationship** (liên kết) = mối quan hệ giữa các thực thể: giảng viên *thuộc* khoa, giảng viên *dạy* môn.
- **Attribute** (thuộc tính) = tính chất: tên, lương.

Điểm mấu chốt về thiết kế nằm ở **lực lượng (cardinality)** của liên kết — một–một, một–nhiều, nhiều–nhiều — vì nó quyết định *nên có mấy bảng*. Quan hệ "giảng viên thuộc khoa" là **nhiều giảng viên – một khoa**: chính vì "một khoa" mà toà nhà/ngân sách thuộc về *khoa*, không thuộc *giảng viên* → nhồi chúng vào bảng giảng viên là sai. E-R vẽ ra điều đó *trước*, còn FD (mục 3) *chứng minh* điều đó bằng toán.

> [!note] E-R → bảng (rút gọn)
> Quy tắc dịch: mỗi entity set → một bảng (khoá chính = khoá của thực thể). Liên kết **nhiều–một** → nhét khoá bên "một" làm **foreign key** vào bảng bên "nhiều". Liên kết **nhiều–nhiều** → phải tạo **bảng riêng** chứa cặp khoá. (Ta đã thấy foreign key ở Bài 1.)

## 3. Phụ thuộc hàm: ngôn ngữ của ràng buộc

Khoá (Bài 1) nói "tập thuộc tính này định danh *cả bộ*". **Phụ thuộc hàm (functional dependency)** tổng quát hơn: "tập thuộc tính này định danh *giá trị của vài thuộc tính khác*".

> [!quote] Silberschatz (tr. 310)
> "we say that the instance satisfies the functional dependency α → β if for all pairs of tuples t1 and t2 in the instance such that t1[α] = t2[α], it is also the case that t1[β] = t2[β]."
>
> *instance **thoả** phụ thuộc hàm α → β nếu: với **mọi** cặp bộ t1, t2 mà **bằng nhau trên α**, chúng cũng **bằng nhau trên β**.*

Dịch nôm na: *"biết α thì biết β, không nhập nhằng"*. Trong `in_dep`:

- `dept_name → building, budget` **đúng** — mỗi khoa có đúng một toà nhà và một ngân sách.
- `dept_name → salary` **sai** — cùng khoa Physics mà Einstein 95000, Gold 87000.

Khoá chính là trường hợp đặc biệt của FD:

> [!quote] Silberschatz (tr. 310)
> "K is a superkey for r(R) if the functional dependency K → R holds on r(R)."
>
> *K là **superkey** của r(R) nếu phụ thuộc hàm **K → R** đúng* (K xác định *toàn bộ* thuộc tính).

Công cụ then chốt để *tính toán* với FD là **đóng thuộc tính** `α+` (attribute closure): tập **mọi** thuộc tính suy ra được từ α qua các FD. Nó cho ta cách kiểm superkey bằng máy: **α là superkey ⟺ `α+` chứa mọi thuộc tính của bảng**. Demo mục 5 cài đúng thuật toán này — nó cũng là trái tim của bộ kiểm BCNF.

## 4. BCNF: định nghĩa và cách phân rã

**Dạng chuẩn (normal form)** là tiêu chuẩn cho "bảng không còn dư thừa kiểu FD". Mạnh và sạch nhất trong nhóm cơ bản là **Boyce–Codd (BCNF)**.

> [!quote] Silberschatz (tr. 313–314)
> "A relation schema R is in BCNF with respect to a set F of functional dependencies if, for all functional dependencies in F+ of the form α → β [...] at least one of the following holds:
> • α → β is a trivial functional dependency (i.e., β ⊆ α).
> • α is a superkey for schema R."
>
> *R ở dạng BCNF nếu với **mọi** FD `α → β`, **ít nhất một** điều sau đúng: (1) FD **tầm thường** (β ⊆ α); hoặc (2) **α là superkey**.*

Diễn giải: trong một bảng BCNF, *vế trái của mọi FD không-tầm-thường phải là superkey*. `in_dep` **vi phạm** vì `dept_name → building, budget` không tầm thường mà `dept_name` **không** là superkey (một khoa có nhiều giảng viên) → đó chính là nguồn gốc dư thừa.

Sách cho **thuật toán phân rã** (tr. 314): tìm FD vi phạm `α → β`, thay R bằng hai bảng:

```
   (α ∪ β)            ← đóng gói đúng sự thật "α xác định β"
   (R − (β − α))      ← phần còn lại, vẫn giữ α để JOIN lại được (lossless)
```

Với `in_dep`: `α = dept_name`, `β = {building, budget}` →

```
   (dept_name, building, budget)        = bảng department
   (ID, name, salary, dept_name)        = bảng instructor
```

Nếu mảnh kết quả vẫn vi phạm thì **phân rã tiếp**, cho tới khi mọi mảnh đạt BCNF. Hai điều kiện sống còn của một phân rã tốt: **lossless** (JOIN hai mảnh lại ra đúng bảng gốc — bảo đảm bằng việc giữ `dept_name` ở cả hai) và không đẻ dữ liệu ma.

> [!warning] BCNF vs 3NF — vì sao đôi khi dừng ở 3NF
> BCNF xoá *mọi* dư thừa kiểu FD, nhưng có giá: đôi khi nó khiến một FD **không kiểm được trên một bảng đơn** (phải JOIN mới kiểm được ràng buộc) — gọi là mất *dependency preservation*. **Dạng chuẩn 3 (3NF)** yếu hơn một chút: cho phép giữ lại chút dư thừa để *luôn* bảo toàn được việc kiểm FD. Thực chiến: nhắm BCNF, lùi về 3NF khi BCNF phá mất khả năng kiểm ràng buộc rẻ. (Silberschatz §7.3.)

## 5. Demo: kiểm FD và phân rã BCNF

Hai phần: (A) kiểm một instance có thoả FD không + đo dư thừa; (B) đóng thuộc tính → kiểm superkey → **phân rã BCNF tự động** đúng thuật toán sách:

```typescript
import { strict as assert } from "node:assert";

type Row = Record<string, string | number>;
type FD = { lhs: string[]; rhs: string[] };

// ─── PHẦN A: kiểm một instance có THOẢ phụ thuộc hàm α→β không ───
// FD α→β đúng nếu: hai hàng bằng nhau trên α thì BẮT BUỘC bằng nhau trên β.
function satisfies(rows: Row[], fd: FD): boolean {
  const seen = new Map<string, string>();
  for (const r of rows) {
    const a = fd.lhs.map(c => r[c]).join("|");
    const b = fd.rhs.map(c => r[c]).join("|");
    if (seen.has(a) && seen.get(a) !== b) return false;  // cùng α mà khác β → vi phạm
    seen.set(a, b);
  }
  return true;
}

// Bảng in_dep = gộp instructor + department (Figure 7.2) → có DƯ THỪA.
const in_dep: Row[] = [
  { ID: "22222", name: "Einstein",   salary: 95000, dept_name: "Physics",    building: "Watson",  budget: 70000 },
  { ID: "33456", name: "Gold",       salary: 87000, dept_name: "Physics",    building: "Watson",  budget: 70000 },
  { ID: "10101", name: "Srinivasan", salary: 65000, dept_name: "Comp. Sci.", building: "Taylor",  budget: 100000 },
  { ID: "45565", name: "Katz",       salary: 75000, dept_name: "Comp. Sci.", building: "Taylor",  budget: 100000 },
  { ID: "12121", name: "Wu",         salary: 90000, dept_name: "Finance",    building: "Painter", budget: 120000 },
];

console.log("PHẦN A — kiểm FD trên instance in_dep:");
console.log("  dept_name → {building,budget} ?", satisfies(in_dep, { lhs: ["dept_name"], rhs: ["building", "budget"] }), "(đúng: mỗi khoa 1 nhà+ngân sách)");
console.log("  dept_name → salary           ?", satisfies(in_dep, { lhs: ["dept_name"], rhs: ["salary"] }), "(sai: cùng khoa, lương khác nhau)");
const distinctDeptFacts = new Set(in_dep.map(r => `${r.dept_name}:${r.building},${r.budget}`)).size;
console.log(`  dư thừa: ${in_dep.length} hàng nhưng chỉ ${distinctDeptFacts} sự thật (dept_name→nhà,ngân sách) → lặp ${in_dep.length - distinctDeptFacts} lần`);

// ─── PHẦN B: đóng thuộc tính → kiểm superkey → phân rã BCNF ───
const R = ["ID", "name", "salary", "dept_name", "building", "budget"];
const F: FD[] = [
  { lhs: ["ID"], rhs: ["name", "salary", "dept_name"] },   // ID xác định thông tin giảng viên
  { lhs: ["dept_name"], rhs: ["building", "budget"] },     // dept_name xác định nhà + ngân sách
];

// α+ : tập mọi thuộc tính suy ra được từ α qua F (thuật toán điểm bất động).
function closure(attrs: string[], fds: FD[]): string[] {
  const res = new Set(attrs);
  let changed = true;
  while (changed) {
    changed = false;
    for (const fd of fds)
      if (fd.lhs.every(a => res.has(a)))
        for (const b of fd.rhs) if (!res.has(b)) { res.add(b); changed = true; }
  }
  return R.filter(a => res.has(a));   // giữ thứ tự R cho tất định
}
const isSuperkey = (attrs: string[], schema: string[], fds: FD[]) =>
  schema.every(a => closure(attrs, fds).includes(a));

console.log("\nPHẦN B — đóng thuộc tính & superkey:");
console.log("  {ID}+   =", closure(["ID"], F).join(","), "→ superkey?", isSuperkey(["ID"], R, F));
console.log("  {dept_name}+ =", closure(["dept_name"], F).join(","), "→ superkey?", isSuperkey(["dept_name"], R, F));

// Tìm FD vi phạm BCNF: α→β không tầm thường và α KHÔNG là superkey.
function bcnfViolation(schema: string[], fds: FD[]): FD | null {
  for (const fd of fds) {
    const lhsIn = fd.lhs.every(a => schema.includes(a));
    const rhsNew = fd.rhs.filter(b => schema.includes(b) && !fd.lhs.includes(b));
    if (lhsIn && rhsNew.length > 0 && !isSuperkey(fd.lhs, schema, fds))
      return { lhs: fd.lhs, rhs: rhsNew };
  }
  return null;
}

// Phân rã BCNF (đệ quy): thay R bằng (α∪β) và (R−(β−α)) cho tới khi mọi mảnh đạt BCNF.
function decomposeBCNF(schema: string[], fds: FD[]): string[][] {
  const v = bcnfViolation(schema, fds);
  if (!v) return [schema];
  const ab = R.filter(a => v.lhs.includes(a) || v.rhs.includes(a));          // α ∪ β
  const rest = schema.filter(a => !(v.rhs.includes(a) && !v.lhs.includes(a))); // R − (β−α)
  console.log(`  vi phạm: {${v.lhs}} → {${v.rhs}}  (${v.lhs} không là superkey) → tách:`);
  return [...decomposeBCNF(ab, fds), ...decomposeBCNF(rest, fds)];
}

console.log("\nPhân rã in_dep về BCNF:");
const result = decomposeBCNF(R, F);
for (const s of result) console.log("   schema BCNF:", `(${s.join(", ")})`);
for (const s of result) assert.equal(bcnfViolation(s, F), null);   // mọi mảnh đã đạt BCNF
console.log("\nMỗi mảnh giờ không còn FD nào vi phạm → hết dư thừa dept_name→nhà,ngân sách.");
```

Kết quả chạy thật *(tất định)*:

```
PHẦN A — kiểm FD trên instance in_dep:
  dept_name → {building,budget} ? true (đúng: mỗi khoa 1 nhà+ngân sách)
  dept_name → salary           ? false (sai: cùng khoa, lương khác nhau)
  dư thừa: 5 hàng nhưng chỉ 3 sự thật (dept_name→nhà,ngân sách) → lặp 2 lần

PHẦN B — đóng thuộc tính & superkey:
  {ID}+   = ID,name,salary,dept_name,building,budget → superkey? true
  {dept_name}+ = dept_name,building,budget → superkey? false

Phân rã in_dep về BCNF:
  vi phạm: {dept_name} → {building,budget}  (dept_name không là superkey) → tách:
   schema BCNF: (dept_name, building, budget)
   schema BCNF: (ID, name, salary, dept_name)

Mỗi mảnh giờ không còn FD nào vi phạm → hết dư thừa dept_name→nhà,ngân sách.
```

Bốn điều đáng thấm. **(1)** `satisfies` biến định nghĩa toán của FD thành một phép quét hàng — `dept_name→building,budget` đúng, `dept_name→salary` sai, *tính được* chứ không phán bừa. **(2)** Dư thừa đo được: 5 hàng chỉ mang 3 sự thật về khoa → đúng cái lãng phí mục 1 chỉ ra. **(3)** `{ID}+` ra *mọi* thuộc tính → superkey; `{dept_name}+` chỉ ra 3 → **không** superkey, và đó chính là vế trái FD gây dư thừa. **(4)** Thuật toán phân rã chạy ra đúng hai bảng `department` và `instructor` như sách — thiết kế đúng là *kết quả của một thuật toán*, không phải trực giác.

> [!note] Tự thử
> 1. Thêm FD `building → budget` (giả định mỗi toà nhà một ngân sách) vào `F`. `{building}+` giờ là gì? Nó có thành superkey không? Phân rã đổi thế nào?
> 2. Sửa dữ liệu: cho Gold (Physics) toà nhà `"Painter"`. Chạy lại Phần A: `dept_name→building,budget` còn đúng không? Đây là *vi phạm ràng buộc* mà một DBMS sẽ chặn.
> 3. Đổi `in_dep` thêm giảng viên khoa Physics thứ ba → số "hàng" tăng nhưng "sự thật về khoa" vẫn 3: tỉ lệ dư thừa càng tệ. In lại con số.
> 4. Cài thêm kiểm **lossless**: JOIN hai schema kết quả trên `dept_name` rồi so số thuộc tính với R. Vì sao giữ `dept_name` ở cả hai mảnh là điều kiện để JOIN lại không mất/thừa thông tin?

## 6. Bản đồ khoá database

| # | Bài | Mảng | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | DBMS là gì & vì sao cần | động lực, trừu tượng hoá | Silberschatz Ch1 |
| 1 | Mô hình quan hệ & đại số quan hệ | nền toán của bảng/SQL | Ch2 |
| 2 | SQL từ nền tới sâu | truy vấn, join, view | Ch3–5 |
| 3 | **Thiết kế & chuẩn hoá (E-R, FD, BCNF)** ← *đang ở đây* | thiết kế đúng | Ch6–7 |
| 4 | Lưu trữ vật lý & buffer manager | dữ liệu trên đĩa/RAM | Ch12–13 |
| 5 | Index: B+tree | tra cứu nhanh | Ch14 |
| 6 | Index nâng cao: LSM & bitmap | tối ưu ghi/phân tích | Ch24 |
| 7 | Xử lý truy vấn: join algorithms | thực thi truy vấn | Ch15 |
| 8 | Tối ưu truy vấn (cost-based) | chọn kế hoạch rẻ nhất | Ch16 |
| 9 | Transaction & ACID, isolation | đúng khi có lỗi | Ch17 |
| 10 | Đồng thời: 2PL / MVCC | đúng khi song song | Ch18 |
| 11 | Phục hồi: WAL / ARIES | sống sót sau sập | Ch19 |
| 12 | Song song & phân tán (góc DB) | mở rộng ra nhiều máy | Ch20–23 + Red Book |

Hết phần **nền** (Bài 0–3). Từ Bài 4 ta mở nắp ca-pô: dữ liệu *thực sự* nằm ở đâu trên đĩa.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 3.1 — Gộp mọi thứ vào một bảng to gây ra những bất thường gì?
> **Đáp:** dư thừa (lặp thông tin) → bất thường **cập nhật** (sửa sót → mâu thuẫn), **chèn** (không thêm được khoa chưa có giảng viên), **xoá** (mất thông tin khoa khi xoá giảng viên cuối).

> [!question] Thẻ 3.2 — Phụ thuộc hàm α → β nghĩa là gì?
> **Đáp:** mọi cặp bộ bằng nhau trên α thì cũng bằng nhau trên β ("biết α là biết β"). Superkey là trường hợp `K → R` (K xác định toàn bộ).

> [!question] Thẻ 3.3 — Đóng thuộc tính α+ dùng để làm gì?
> **Đáp:** α+ = mọi thuộc tính suy ra từ α qua F. Dùng kiểm superkey: **α là superkey ⟺ α+ = toàn bộ thuộc tính bảng**. Là lõi của kiểm BCNF.

> [!question] Thẻ 3.4 — Điều kiện BCNF là gì?
> **Đáp:** với mọi FD không-tầm-thường `α → β`, **α phải là superkey**. Vi phạm = có FD mà vế trái không định danh cả bộ → nguồn dư thừa.

> [!question] Thẻ 3.5 — Quy tắc phân rã một bảng vi phạm BCNF?
> **Đáp:** tìm FD vi phạm `α → β`, thay R bằng `(α ∪ β)` và `(R − (β − α))`; lặp tới khi mọi mảnh đạt BCNF. Giữ α ở cả hai mảnh → **lossless** (JOIN lại ra đúng gốc).

## 8. Câu hỏi tự kiểm tra

1. Chỉ ra ba loại "bất thường" trong bảng `in_dep` và ví dụ cụ thể cho mỗi loại. *(mục 1)*
2. E-R dùng ba khái niệm nào? Lực lượng "nhiều giảng viên – một khoa" gợi ý điều gì về thiết kế bảng? *(mục 2)*
3. Viết định nghĩa FD `α → β`. Vì sao `dept_name → budget` đúng còn `dept_name → salary` sai trong `in_dep`? *(mục 3)*
4. Phát biểu điều kiện BCNF. Vì sao `in_dep` vi phạm? *(mục 4)*
5. Chạy demo mục 5, làm Tự thử 1 (thêm `building → budget`). Giải thích kết quả phân rã mới. *(mục 5)*

## Tóm tắt một trang

```
BÀI 3 — THIẾT KẾ & CHUẨN HOÁ
─────────────────────────────────────────────────────────
BẢNG GỘP TO = DƯ THỪA  nhồi instructor+department vào in_dep → (dept_name→nhà,ngân sách)
   lặp cho mỗi giảng viên → bất thường CẬP NHẬT / CHÈN / XOÁ.

E-R  ba khái niệm: entity set, relationship set, attribute (Silberschatz tr.244).
   Lực lượng liên kết (1–1, 1–nhiều, nhiều–nhiều) quyết định số bảng. Vẽ thế giới
   TRƯỚC khi dựng bảng.

PHỤ THUỘC HÀM (FD)  α→β: bằng nhau trên α ⇒ bằng nhau trên β ("biết α là biết β",
   tr.310). Superkey = FD K→R. ĐÓNG THUỘC TÍNH α+ = mọi thuộc tính suy từ α →
   kiểm superkey: α superkey ⟺ α+ = toàn bộ.

BCNF  mọi FD không-tầm-thường: vế trái α PHẢI là superkey (tr.313–314). Vi phạm =
   dư thừa. PHÂN RÃ: thay R bằng (α∪β) và (R−(β−α)), lặp tới sạch; giữ α 2 bên →
   LOSSLESS. BCNF có thể mất dependency-preservation → đôi khi dừng ở 3NF.

DEMO  satisfies() kiểm FD; closure() kiểm superkey; decomposeBCNF() ra đúng
   (dept_name,building,budget) + (ID,name,salary,dept_name) như sách. Thiết kế = THUẬT TOÁN.
```

## Nguồn

- **Silberschatz, Korth, Sudarshan — *Database System Concepts*, 7th ed.** — **Ch6 Database Design Using the E-R Model**: entity/relationship/attribute (tr. 244); **Ch7 Relational Database Design**: dư thừa & phân rã (tr. 303–308), phụ thuộc hàm & superkey (tr. 310), BCNF định nghĩa (tr. 313–314) và thuật toán phân rã (tr. 314), 3NF & dependency preservation (§7.3). `tai_lieu/Database System Concepts 7th Edition...pdf` (offset **PDF = tr. + 29**).
- Liên hệ: [Bài 1 — domain atomic (1NF)](bai_01_mo-hinh-quan-he.md); [cloud-base Bài 17 — data models](../../cloud-base/bai_hoc/bai_17_du-lieu-data-models.md) (khi nào *cố ý* phi chuẩn hoá cho NoSQL).

---

**Bản đồ khoá học:** [Bài 0 — DBMS là gì](bai_00_dbms-la-gi.md) · [Bài 1 — Mô hình quan hệ & đại số quan hệ](bai_01_mo-hinh-quan-he.md) · [Bài 2 — SQL từ nền tới sâu](bai_02_sql.md) · **[Bài 3 — Thiết kế & chuẩn hoá] ← bạn đang ở đây** · [Bài 4 — Lưu trữ & buffer manager](bai_04_luu-tru-buffer.md) · [Bài 5 — Index: B+tree](bai_05_index-btree.md) · [Bài 6 — Index nâng cao: LSM & bitmap](bai_06_index-lsm-bitmap.md) · [Bài 7 — Join algorithms](bai_07_query-join.md) · [Bài 8 — Tối ưu truy vấn](bai_08_query-optimization.md) · [Bài 9 — Transaction & ACID](bai_09_transaction-acid.md) · [Bài 10 — Đồng thời: 2PL/MVCC](bai_10_concurrency.md) · [Bài 11 — Phục hồi: WAL/ARIES](bai_11_recovery.md) · [Bài 12 — Song song & phân tán](bai_12_phan-tan.md)

Xem thêm [README khoá học](../README.md).
