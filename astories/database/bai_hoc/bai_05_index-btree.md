# Bài 5 — Index: B+tree

> [!info] Về bài này
> Bài 4 cho biết dữ liệu nằm trong các **block** trên đĩa, đọc qua **buffer**. Nhưng tìm một dòng trong triệu dòng mà *quét hết* thì chết — cần **index**. Bài này dựng cấu trúc index thống trị mọi RDBMS: **B+tree** — cây cân bằng, "béo và lùn", mỗi nút đúng một block, biến tra cứu từ *triệu block đọc* xuống *ba bốn block đọc*. Và ta sẽ **tự dựng một cái** bằng TypeScript.
> Nguồn (Luật số 1): **Silberschatz** *Database System Concepts 7e* — **Ch14 (Indexing)** (offset PDF = tr. + 29).
> **Chạy demo:** **Node 22+**, `node <tên>.ts` — không cài gói.
> Nên đọc trước: [Bài 4 — Lưu trữ & buffer manager](bai_04_luu-tru-buffer.md) (block, buffer). Liên hệ: [cloud-base Bài 10 — storage engine](../../cloud-base/bai_hoc/bai_10_du-lieu-storage.md).

## Mục lục

1. [Vì sao cần index](#1-vì-sao-cần-index)
2. [Index có thứ tự: dense và sparse](#2-index-có-thứ-tự-dense-và-sparse)
3. [B+tree: cây cân bằng, béo và lùn](#3-btree-cây-cân-bằng-béo-và-lùn)
4. [Tìm, chèn (tách nút), và quét khoảng](#4-tìm-chèn-tách-nút-và-quét-khoảng)
5. [Demo: tự dựng B+tree](#5-demo-tự-dựng-btree)
6. [Bản đồ khoá database](#6-bản-đồ-khoá-database)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Vì sao cần index

> [!quote] Silberschatz (tr. 623)
> "Many queries reference only a small proportion of the records in a file."
>
> *Nhiều truy vấn chỉ đụng tới **một phần nhỏ** số bản ghi trong file.*

`SELECT * FROM instructor WHERE ID = '22222'` chỉ cần *một* dòng. Không có index, engine phải **quét tuần tự** (full scan): đọc *mọi* block của bảng để tìm một dòng — với bảng triệu dòng là hàng chục nghìn block I/O (Bài 4: chi phí đo bằng *số block*). Index là **cấu trúc phụ** cho phép nhảy thẳng tới dòng cần, giống **mục lục sách**: thay vì đọc cả cuốn, tra mục lục rồi mở đúng trang.

Mỗi index gắn với một **search key** (khoá tìm kiếm) — thuộc tính (hoặc bộ thuộc tính) ta muốn tra nhanh theo nó. Một bảng có thể có *nhiều* index, trên các search key khác nhau (tra theo `ID`, tra theo `dept_name`...). Chi phí: index tốn chỗ và phải *cập nhật mỗi lần ghi* — nên index là **đánh đổi đọc-nhanh vs ghi-chậm + tốn chỗ** (Bài 6 sẽ thấy thái cực khác của đánh đổi này).

## 2. Index có thứ tự: dense và sparse

Loại index cổ điển nhất là **ordered index** (index có thứ tự):

> [!quote] Silberschatz (tr. 625)
> "an ordered index stores the values of the search keys in sorted order and associates with each search key the records that contain it."
>
> *index có thứ tự lưu các giá trị search key **theo thứ tự đã sắp** và gắn mỗi search key với các bản ghi chứa nó.*

Có hai kiểu, khác nhau ở *mật độ*:

- **Dense index** (dày): có một mục index cho **mọi** giá trị search key. Tra là ra thẳng con trỏ tới bản ghi.
- **Sparse index** (thưa): chỉ có mục cho **một số** giá trị (ví dụ mỗi block một mục). Tra thì tìm mục lớn nhất ≤ khoá cần, rồi **quét tuần tự trong block** từ đó. Thưa → nhỏ hơn, ít tốn chỗ, nhưng tra chậm hơn chút. (Sparse chỉ dùng được khi dữ liệu *đã sắp* theo search key.)

Vấn đề của index tuần tự kiểu này: khi bảng *lớn dần* và bị chèn/xoá liên tục, hiệu năng **thoái hoá** (phải dồn file, tạo block tràn...). Cần một cấu trúc **tự cân bằng** khi dữ liệu đổi — đó là B+tree.

## 3. B+tree: cây cân bằng, béo và lùn

> [!quote] Silberschatz (tr. 634)
> "A B+-tree index takes the form of a balanced tree in which every path from the root of the tree to a leaf of the tree is of the same length. Each nonleaf node in the tree (other than the root) has between ⌈n/2⌉ and n children, where n is fixed for a particular tree; the root has between 2 and n children."
>
> *B+-tree là một **cây cân bằng** trong đó **mọi đường từ gốc tới lá dài bằng nhau**. Mỗi nút trong (trừ gốc) có từ ⌈n/2⌉ tới n con; gốc có từ 2 tới n con.*

Mỗi nút trông như sau:

> [!quote] Silberschatz (tr. 634)
> "It contains up to n−1 search-key values K1, K2, …, Kn−1, and n pointers P1, P2, …, Pn. The search-key values within a node are kept in sorted order"

```
   nút B+tree bậc n:   [ P1 | K1 | P2 | K2 | ... | Kn-1 | Pn ]
                          ↓         ↓                      ↓
                       khoá < K1   K1 ≤ khoá < K2      khoá ≥ Kn-1
   • tối đa n con / n-1 khoá, sắp tăng dần
   • nút TRONG: con trỏ chỉ tới nút con (chỉ định hướng)
   • nút LÁ: chứa (khoá → bản ghi), và nối nhau thành danh sách → quét khoảng
```

Chữ **"B" nghĩa là balanced** — và đó là tính chất *bắt buộc*:

> [!quote] Silberschatz (tr. 637)
> "the length of every path from the root to a leaf node is the same. This property is a requirement for a B+-tree. Indeed, the "B" in B+-tree stands for "balanced.""

Điểm thiên tài nằm ở chỗ **mỗi nút = một block đĩa** (Bài 4). Vì block to (4–16KB), một nút chứa *rất nhiều* con (**fanout** — số nhánh mỗi nút — lên tới hàng trăm) → cây **béo và lùn**:

> [!quote] Silberschatz (tr. 640)
> "B+-trees tend to be fat and short, unlike thin and tall binary trees."
>
> *B+-tree có xu hướng **béo và lùn**, khác với cây nhị phân **gầy và cao**.*

Vì sao điều này sống còn? Mỗi lần xuống một tầng là **một block đọc từ đĩa**. Cây nhị phân cho triệu bản ghi cao ~20 tầng → ~20 block I/O. B+tree với fanout trăm chỉ ~3 tầng → ~3 block I/O. *Chiều cao thấp = ít đụng đĩa* — đó là toàn bộ lý do B+tree thống trị. Demo mục 5 cho thấy con số này.

## 4. Tìm, chèn (tách nút), và quét khoảng

**Tìm** (search): từ gốc, ở mỗi nút so khoá cần với các `Ki` để chọn con trỏ đi xuống, lặp tới lá. Vì cây cao `h` tầng → đúng `h` block đọc.

**Chèn** (insert): tìm lá đúng, chèn khoá vào đúng vị trí (giữ thứ tự). Nếu lá **tràn** (quá n−1 khoá) → **tách nút** (split): chia đôi, và đẩy một khoá phân cách **lên nút cha**. Nếu cha cũng tràn → tách tiếp, lan lên trên. Nếu *gốc* tràn → tạo gốc mới → **cây cao thêm một tầng**. Chính cơ chế tách-lan-lên này giữ cây **luôn cân bằng** mà không cần dồn file.

- Tách **lá**: khoá phân cách được **copy** lên cha (lá vẫn giữ khoá đó, vì lá chứa dữ liệu thật).
- Tách **nút trong**: khoá giữa được **đẩy** lên cha (nút trong không giữ lại, nó chỉ định hướng).

**Quét khoảng** (range scan) `WHERE x BETWEEN a AND b`: xuống lá chứa `a`, rồi **đi ngang** theo danh sách lá nối nhau tới khi vượt `b`. Không phải quay lại gốc — đây là lý do lá được nối thành danh sách.

Demo mục 5 cài đủ cả bốn: dựng cây bằng chèn (có tách nút lan lên), in cấu trúc theo tầng, tìm (in đường đi), và quét khoảng.

## 5. Demo: tự dựng B+tree

B+tree bậc `n=4` (lá tối đa 3 khoá) thật sự chạy — chèn 1..10, xem cây tách nút và cao dần; tra cứu in cả đường gốc→lá; quét khoảng dùng lá nối nhau; và tính "béo & lùn":

```typescript
import { strict as assert } from "node:assert";

// B+tree bậc n: mỗi nút tối đa n con / n-1 khoá. Nút lá chứa (khoá→giá trị) và
// nối nhau thành danh sách (để quét khoảng). Nút trong chỉ định hướng. Cây LUÔN
// cân bằng: mọi đường gốc→lá dài bằng nhau. Nút = 1 block (Bài 4) → cây "béo & lùn".
const N = 4;                 // bậc: lá/nút trong tối đa N-1 = 3 khoá
type Leaf = { leaf: true; keys: number[]; vals: string[]; next: Leaf | null };
type Internal = { leaf: false; keys: number[]; kids: Node[] };
type Node = Leaf | Internal;
type Split = { sep: number; right: Node };

let root: Node = { leaf: true, keys: [], vals: [], next: null };

function insertRec(node: Node, key: number, val: string): Split | null {
  if (node.leaf) {
    let i = 0; while (i < node.keys.length && node.keys[i] < key) i++;
    node.keys.splice(i, 0, key); node.vals.splice(i, 0, val);
    if (node.keys.length < N) return null;                  // chưa tràn
    const at = Math.ceil(N / 2);                            // tràn → tách lá làm đôi
    const right: Leaf = { leaf: true, keys: node.keys.splice(at), vals: node.vals.splice(at), next: node.next };
    node.next = right;
    return { sep: right.keys[0], right };                   // COPY khoá đầu lá phải lên trên
  } else {
    let i = 0; while (i < node.keys.length && key >= node.keys[i]) i++;
    const res = insertRec(node.kids[i], key, val);
    if (!res) return null;
    node.keys.splice(i, 0, res.sep); node.kids.splice(i + 1, 0, res.right);
    if (node.keys.length < N) return null;                  // chưa tràn
    const mid = Math.floor(N / 2);                          // tràn → ĐẨY khoá giữa lên
    const sep = node.keys[mid];
    const right: Internal = { leaf: false, keys: node.keys.splice(mid + 1), kids: node.kids.splice(mid + 1) };
    node.keys.splice(mid);                                  // bỏ khoá giữa khỏi nút trái (đã đẩy lên)
    return { sep, right };
  }
}
function insert(key: number, val: string) {
  const res = insertRec(root, key, val);
  if (res) root = { leaf: false, keys: [res.sep], kids: [root, res.right] };  // cây cao thêm 1
}
function search(key: number): string | null {
  let node = root, path: string[] = [];
  while (!node.leaf) {
    let i = 0; while (i < node.keys.length && key >= node.keys[i]) i++;
    path.push(`[${node.keys.join(" ")}]→con${i}`); node = node.kids[i];
  }
  const j = node.keys.indexOf(key);
  console.log(`  tìm ${key}: ${path.join("  ")}  → lá[${node.keys.join(" ")}]  ${j >= 0 ? "THẤY=" + node.vals[j] : "KHÔNG có"}`);
  return j >= 0 ? node.vals[j] : null;
}
function rangeScan(lo: number, hi: number): number[] {   // tận dụng lá nối nhau
  let node: Node = root;
  while (!node.leaf) { let i = 0; while (i < node.keys.length && lo >= node.keys[i]) i++; node = node.kids[i]; }
  const out: number[] = [];
  for (let L: Leaf | null = node; L; L = L.next)
    for (const k of L.keys) if (k >= lo && k <= hi) out.push(k);
  return out;
}
function height(): number { let h = 1, n: Node = root; while (!n.leaf) { h++; n = n.kids[0]; } return h; }
function printTree() {
  let level: Node[] = [root], depth = 0;
  while (level.length) {
    console.log(`  tầng ${depth}: ` + level.map(n => `[${n.keys.join(" ")}]`).join("  "));
    const next: Node[] = [];
    for (const n of level) if (!n.leaf) next.push(...n.kids);
    level = next; depth++;
  }
}

// Chèn 1..10 theo thứ tự → quan sát cây tách nút & cao dần.
for (let k = 1; k <= 10; k++) insert(k, `v${k}`);
console.log("B+tree sau khi chèn 1..10 (bậc n=4, lá tối đa 3 khoá):");
printTree();
console.log(`\nChiều cao cây = ${height()} tầng (cân bằng: mọi đường gốc→lá bằng nhau).`);

console.log("\nTra cứu (in cả đường đi gốc→lá):");
search(7); search(10); search(99);

console.log("\nQuét khoảng [4..8] (nhờ các lá nối nhau):", rangeScan(4, 8).join(", "));

// Kiểm: mọi khoá đã chèn đều tìm thấy; quét khoảng đúng & có thứ tự.
for (let k = 1; k <= 10; k++) assert.equal(search2(k), `v${k}`);
function search2(key: number): string | null { let n: Node = root; while (!n.leaf) { let i = 0; while (i < n.keys.length && key >= n.keys[i]) i++; n = n.kids[i]; } const j = n.keys.indexOf(key); return j >= 0 ? n.vals[j] : null; }
assert.deepEqual(rangeScan(4, 8), [4, 5, 6, 7, 8]);

// "Béo & lùn": vì sao B+tree thắng cây nhị phân trên đĩa.
console.log("\nBéo & lùn (fanout lớn → ít tầng → ít block I/O):");
for (const recs of [1_000, 1_000_000]) {
  const fanout = 100;                                     // nút ~1 block chứa ~100 con
  const bptree = Math.ceil(Math.log(recs) / Math.log(fanout));
  const binary = Math.ceil(Math.log2(recs));
  console.log(`  ${recs.toLocaleString("en")} bản ghi: B+tree ~${bptree} tầng  vs  cây nhị phân ~${binary} tầng`);
}
console.log("Mỗi tầng = 1 block đọc từ đĩa → B+tree ít tầng nghĩa là ít lần đụng đĩa.");
```

Kết quả chạy thật *(tất định)*:

```
B+tree sau khi chèn 1..10 (bậc n=4, lá tối đa 3 khoá):
  tầng 0: [7]
  tầng 1: [3 5]  [9]
  tầng 2: [1 2]  [3 4]  [5 6]  [7 8]  [9 10]

Chiều cao cây = 3 tầng (cân bằng: mọi đường gốc→lá bằng nhau).

Tra cứu (in cả đường đi gốc→lá):
  tìm 7: [7]→con1  [9]→con0  → lá[7 8]  THẤY=v7
  tìm 10: [7]→con1  [9]→con1  → lá[9 10]  THẤY=v10
  tìm 99: [7]→con1  [9]→con1  → lá[9 10]  KHÔNG có

Quét khoảng [4..8] (nhờ các lá nối nhau): 4, 5, 6, 7, 8

Béo & lùn (fanout lớn → ít tầng → ít block I/O):
  1,000 bản ghi: B+tree ~2 tầng  vs  cây nhị phân ~10 tầng
  1,000,000 bản ghi: B+tree ~3 tầng  vs  cây nhị phân ~20 tầng
Mỗi tầng = 1 block đọc từ đĩa → B+tree ít tầng nghĩa là ít lần đụng đĩa.
```

Bốn điều đáng thấm. **(1)** Cây *cân bằng*: mọi lá ở cùng tầng 2 — tra khoá nào cũng đúng 3 block đọc, không có đường "xui" dài hơn. **(2)** Tra cứu in rõ đường `[7]→con1 [9]→con0 → lá[7 8]`: ở mỗi nút chỉ *so khoá rồi rẽ*, nên chi phí = chiều cao. **(3)** Quét `[4..8]` ra `4,5,6,7,8` *có thứ tự* nhờ đi ngang các lá nối nhau — không quay lại gốc. **(4)** "Béo & lùn" thành số: triệu bản ghi chỉ **3 tầng** B+tree so với **20 tầng** cây nhị phân — tức ~3 block đọc thay vì ~20. Trên đĩa (mỗi seek ~10ms) khác biệt này là *sống hay chết*.

> [!note] Tự thử
> 1. Đổi `N` từ 4 lên 6 (lá tối đa 5 khoá) rồi chèn 1..10: cây cao mấy tầng? Vì sao fanout lớn hơn làm cây *lùn* hơn?
> 2. Chèn theo thứ tự **ngược** (10..1) thay vì 1..10: cây kết quả có khác không? Nó *vẫn* cân bằng chứ? (Đây là điểm mạnh so với cây tìm kiếm nhị phân thường — chèn ngược làm BST suy biến thành danh sách.)
> 3. Thêm hàm `delete(key)` đơn giản (chỉ xoá khỏi lá, chưa cần gộp nút). Vì sao xoá *đúng* trong B+tree khó hơn chèn (gợi ý: nút có thể tụt dưới ⌈(n−1)/2⌉ → phải mượn/gộp)?
> 4. Ở phần "béo & lùn", đổi `fanout` từ 100 xuống 10: B+tree cho triệu bản ghi giờ mấy tầng? Fanout nhỏ dần thì B+tree tiến về cây gì?

## 6. Bản đồ khoá database

| # | Bài | Mảng | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | DBMS là gì & vì sao cần | động lực, trừu tượng hoá | Silberschatz Ch1 |
| 1 | Mô hình quan hệ & đại số quan hệ | nền toán của bảng/SQL | Ch2 |
| 2 | SQL từ nền tới sâu | truy vấn, join, view | Ch3–5 |
| 3 | Thiết kế & chuẩn hoá (E-R, FD, BCNF) | thiết kế đúng | Ch6–7 |
| 4 | Lưu trữ vật lý & buffer manager | dữ liệu trên đĩa/RAM | Ch12–13 |
| 5 | **Index: B+tree** ← *đang ở đây* | tra cứu nhanh | Ch14 |
| 6 | Index nâng cao: LSM & bitmap | tối ưu ghi/phân tích | Ch24 |
| 7 | Xử lý truy vấn: join algorithms | thực thi truy vấn | Ch15 |
| 8 | Tối ưu truy vấn (cost-based) | chọn kế hoạch rẻ nhất | Ch16 |
| 9 | Transaction & ACID, isolation | đúng khi có lỗi | Ch17 |
| 10 | Đồng thời: 2PL / MVCC | đúng khi song song | Ch18 |
| 11 | Phục hồi: WAL / ARIES | sống sót sau sập | Ch19 |
| 12 | Song song & phân tán (góc DB) | mở rộng ra nhiều máy | Ch20–23 + Red Book |

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 5.1 — Index giải quyết vấn đề gì? Đánh đổi là gì?
> **Đáp:** tránh **quét tuần tự** cả bảng cho truy vấn chỉ cần vài dòng → nhảy thẳng tới dòng cần. Đánh đổi: tốn chỗ + phải **cập nhật index mỗi lần ghi** (đọc nhanh hơn, ghi chậm hơn).

> [!question] Thẻ 5.2 — Dense index khác sparse index thế nào?
> **Đáp:** dense = mục cho **mọi** search key (tra ra thẳng); sparse = mục cho **một số** (vd mỗi block một mục), tra tới mục ≤ khoá rồi quét trong block. Sparse nhỏ hơn nhưng chỉ dùng khi dữ liệu đã sắp.

> [!question] Thẻ 5.3 — Nêu ba tính chất cấu trúc của B+tree.
> **Đáp:** (1) **cân bằng** — mọi đường gốc→lá bằng nhau; (2) mỗi nút ≤ n con / n−1 khoá sắp tăng, nút trong (trừ gốc) ≥ ⌈n/2⌉ con; (3) **lá nối nhau** thành danh sách (để quét khoảng).

> [!question] Thẻ 5.4 — Vì sao B+tree "béo và lùn" lại thắng cây nhị phân trên đĩa?
> **Đáp:** mỗi nút = 1 block → fanout lớn (trăm) → cây rất thấp (triệu bản ghi ~3 tầng vs ~20 của nhị phân). Mỗi tầng = 1 block I/O → ít tầng = ít đụng đĩa.

> [!question] Thẻ 5.5 — Cơ chế nào giữ B+tree cân bằng khi chèn?
> **Đáp:** **tách nút (split)**: lá/nút tràn thì chia đôi, đẩy khoá phân cách lên cha; lan lên tới gốc, gốc tràn thì cây cao thêm 1 tầng *đồng đều* → luôn cân bằng (không cần dồn file).

## 8. Câu hỏi tự kiểm tra

1. Không có index, tìm một dòng trong bảng triệu dòng tốn bao nhiêu block I/O? Index đổi con số đó ra sao? *(mục 1)*
2. Khi nào nên dùng sparse thay vì dense index? Điều kiện bắt buộc của sparse là gì? *(mục 2)*
3. Phát biểu ba tính chất của B+tree. Vì sao "B" nghĩa là balanced lại quan trọng? *(mục 3)*
4. Mô tả chèn gây tách nút lan lên gốc. Vì sao cơ chế này giữ cây cân bằng? *(mục 4, 5)*
5. Chạy demo mục 5, làm Tự thử 2 (chèn ngược 10..1). Vì sao BST thường suy biến khi chèn ngược mà B+tree thì không? *(mục 5)*

## Tóm tắt một trang

```
BÀI 5 — INDEX: B+TREE
─────────────────────────────────────────────────────────
VÌ SAO INDEX  truy vấn chỉ cần vài dòng (tr.623) nhưng full scan đọc MỌI block.
   Index = mục lục → nhảy thẳng tới dòng. Đánh đổi: tốn chỗ + ghi chậm hơn.

ORDERED INDEX  lưu search key đã sắp (tr.625). DENSE = mục cho mọi khoá; SPARSE =
   mục cho một số (nhỏ hơn, cần dữ liệu đã sắp). Index tuần tự THOÁI HOÁ khi lớn dần.

B+TREE  cây CÂN BẰNG, mọi đường gốc→lá bằng nhau ("B"=balanced, tr.637). Nút ≤ n
   con / n-1 khoá sắp tăng (tr.634); nút = 1 BLOCK → fanout lớn → BÉO & LÙN (tr.640).
   Lá nối nhau thành danh sách.

THAO TÁC  tìm = rẽ theo khoá, chi phí = chiều cao. Chèn = chèn lá, TRÀN→TÁCH NÚT,
   đẩy khoá lên cha, lan tới gốc (gốc tràn→cao thêm 1) ⇒ luôn cân bằng. Quét khoảng
   = xuống lá rồi ĐI NGANG theo link.

DEMO  B+tree n=4 chèn 1..10 → 3 tầng cân bằng; range [4..8]=4..8; BÉO&LÙN: triệu bản
   ghi ~3 tầng (B+tree) vs ~20 (nhị phân) → ~3 block I/O vs ~20. Nền cho Bài 6 (LSM).
```

## Nguồn

- **Silberschatz, Korth, Sudarshan — *Database System Concepts*, 7th ed.** — **Ch14 Indexing**: động lực index & search key (tr. 623), ordered index dense/sparse (tr. 625), cấu trúc B+tree cân bằng & nút n−1 khoá/n con (tr. 634), "B" = balanced (tr. 637), béo & lùn vs cây nhị phân (tr. 640). `tai_lieu/Database System Concepts 7th Edition...pdf` (offset **PDF = tr. + 29**).
- Liên hệ: [cloud-base Bài 10 — storage engine](../../cloud-base/bai_hoc/bai_10_du-lieu-storage.md) (B-tree vs LSM ở góc data-intensive); [Bài 4 — block & buffer](bai_04_luu-tru-buffer.md) (vì sao nút = 1 block).

---

**Bản đồ khoá học:** [Bài 0 — DBMS là gì](bai_00_dbms-la-gi.md) · [Bài 1 — Mô hình quan hệ & đại số quan hệ](bai_01_mo-hinh-quan-he.md) · [Bài 2 — SQL từ nền tới sâu](bai_02_sql.md) · [Bài 3 — Thiết kế & chuẩn hoá](bai_03_thiet-ke-chuan-hoa.md) · [Bài 4 — Lưu trữ & buffer manager](bai_04_luu-tru-buffer.md) · **[Bài 5 — Index: B+tree] ← bạn đang ở đây** · [Bài 6 — Index nâng cao: LSM & bitmap](bai_06_index-lsm-bitmap.md) · [Bài 7 — Join algorithms](bai_07_query-join.md) · [Bài 8 — Tối ưu truy vấn](bai_08_query-optimization.md) · [Bài 9 — Transaction & ACID](bai_09_transaction-acid.md) · [Bài 10 — Đồng thời: 2PL/MVCC](bai_10_concurrency.md) · [Bài 11 — Phục hồi: WAL/ARIES](bai_11_recovery.md) · [Bài 12 — Song song & phân tán](bai_12_phan-tan.md)

Xem thêm [README khoá học](../README.md).
