# Bài 7 — Đồ thị: biểu diễn và duyệt (BFS, DFS)

> [!info] Về bài này
> **Đồ thị** là cấu trúc mô hình hoá *quan hệ* — mạng xã hội, bản đồ đường đi, phụ thuộc giữa các task, liên kết trang web. Rất nhiều bài toán thực tế quy về "đi trên đồ thị". Bài này xây hai thứ: cách **biểu diễn** đồ thị trong bộ nhớ (danh sách kề vs ma trận kề), và hai thuật toán **duyệt** nền tảng — **BFS** (bề rộng) và **DFS** (bề sâu) — mà khác biệt *duy nhất* giữa chúng hoá ra chỉ là dùng **hàng đợi** hay **ngăn xếp** (Bài 2). Đây là nền cho Bài 8 (đồ thị trọng số: Dijkstra/MST).
> Nguồn (Luật số 1): **Skiena** *The Algorithm Design Manual 3e* — **Chapter 7: Graph Traversal** (`tai_lieu/`, trích `> [!quote] Skiena (tr. N)`, **PDF = tr. + 14** ở Ch7 — offset trôi tiếp, xem hộp lưu ý).
> **Chạy demo:** `node bai_07.ts` — Node 22+, không cài gói. Code tất định.
> Cần đọc trước: [Bài 2 — CTDL tuyến tính](bai_02_ctdl-tuyen-tinh.md) (stack/queue), [Bài 1 — Big-O](bai_01_big-o.md).

> [!warning] Offset trang Skiena tiếp tục trôi
> Ch1–2 dùng **+17**, Ch3–6 dùng **+16**, sang **Ch7** là **+14** (trang in 197 = PDF 211). Mỗi quote vẫn được dò lại đúng trang PDF chứa chữ; verifier quét cửa sổ ±3 trang quanh mốc nên bắt được cả drift này.

## Mục lục

1. [Tình huống: mọi thứ đều là đồ thị](#1-tình-huống-mọi-thứ-đều-là-đồ-thị)
2. [Biểu diễn đồ thị: danh sách kề hay ma trận kề](#2-biểu-diễn-đồ-thị-danh-sách-kề-hay-ma-trận-kề)
3. [Duyệt đồ thị: đánh dấu để không đi lại](#3-duyệt-đồ-thị-đánh-dấu-để-không-đi-lại)
4. [BFS và DFS: khác nhau chỉ ở queue hay stack](#4-bfs-và-dfs-khác-nhau-chỉ-ở-queue-hay-stack)
5. [Demo: adjacency list, BFS, DFS](#5-demo-adjacency-list-bfs-dfs)
6. [Bản đồ khoá DSA](#6-bản-đồ-khoá-dsa)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Tình huống: mọi thứ đều là đồ thị

> [!example] Ba câu hỏi, một cấu trúc
> "Hai người này có quen chung ai không?" (mạng xã hội) · "Đường ngắn nhất từ nhà tới công ty?" (bản đồ) · "Thứ tự biên dịch các module phụ thuộc nhau?" (build system). Ba bài khác hẳn nhau về bề ngoài, nhưng cùng một *hình*: một tập **đỉnh** (vertex) nối nhau bởi các **cạnh** (edge). Giải được "đi trên đồ thị" là giải được cả ba.

> [!quote] Skiena (tr. 197)
> "Graphs are one of the unifying themes of computer science"
>
> *Đồ thị là một trong những **chủ đề thống nhất** của khoa học máy tính.*

Đồ thị `G = (V, E)` gồm tập đỉnh `V` và tập cạnh `E` (các cặp đỉnh). Cạnh có thể **vô hướng** (tình bạn: quen nhau là hai chiều) hay **có hướng** (theo dõi trên mạng xã hội: một chiều), có **trọng số** (độ dài đường — Bài 8) hay không. Một quan sát quyết định cách lưu:

> [!quote] Skiena (tr. 202)
> "Most of the graphs that one encounters in real life are sparse."
>
> *Phần lớn đồ thị gặp trong đời thực đều **thưa** (sparse).*

Thưa = số cạnh `m` nhỏ hơn nhiều so với tối đa `n²` (người đông nhất thế giới cũng chỉ quen một phần tí xíu nhân loại). Điều này định hướng chọn cách biểu diễn ở mục 2.

## 2. Biểu diễn đồ thị: danh sách kề hay ma trận kề

Hai cách lưu một đồ thị `n` đỉnh, `m` cạnh:

- **Ma trận kề** *(adjacency matrix)*: bảng `n × n`, ô `[u][v] = 1` nếu có cạnh `u–v`. Kiểm "có cạnh u–v?" tức thì `O(1)`, nhưng tốn `O(n²)` bộ nhớ *dù đồ thị thưa* và duyệt hàng xóm của một đỉnh luôn mất `O(n)`.
- **Danh sách kề** *(adjacency list)*: mỗi đỉnh giữ một *danh sách* các đỉnh kề nó. Tốn `O(n + m)` bộ nhớ, duyệt hàng xóm của `u` mất đúng bằng *bậc* (degree) của `u`; kiểm "có cạnh u–v?" mất `O(bậc u)`.

```
Đồ thị:  1—2   1—3   2—4            MA TRẬN KỀ (n×n)      DANH SÁCH KỀ (n + m)
                                       1 2 3 4              1: [2, 3]
            1                       1 [0 1 1 0]             2: [1, 4]
          /   \                     2 [1 0 0 1]             3: [1]
         2     3                    3 [1 0 0 0]             4: [2]
         |                          4 [0 1 0 0]
         4                          O(n^2) dù thưa          O(n+m): tiết kiệm khi thưa
```

Vì đồ thị thực tế hầu hết **thưa**, **danh sách kề** gần như luôn là lựa chọn mặc định (Skiena tr. 204): tiết kiệm bộ nhớ `O(n + m)` thay vì `O(n²)`, và cho phép duyệt mọi cạnh trong `O(n + m)` — đúng độ phức tạp của BFS/DFS. (Ma trận kề chỉ thắng khi đồ thị *dày* hoặc cần kiểm tra cạnh liên tục.) Khoá này dùng danh sách kề.

## 3. Duyệt đồ thị: đánh dấu để không đi lại

**Duyệt** *(traversal)* = thăm có hệ thống mọi đỉnh và cạnh. Khác mảng/cây, đồ thị có **chu trình** — đi lung tung dễ quay lại chỗ cũ và lặp vô hạn. Chìa khoá tránh điều đó:

> [!quote] Skiena (tr. 213)
> "The key idea behind graph traversal is to mark each vertex when we first visit it and keep track of what we have not yet completely explored."
>
> *Ý tưởng cốt lõi của duyệt đồ thị là **đánh dấu mỗi đỉnh khi lần đầu thăm nó**, và **theo dõi những gì chưa khám phá xong**.*

Mỗi đỉnh đi qua ba trạng thái: **chưa khám phá** *(undiscovered)* → **đã khám phá** *(discovered — đã thấy, chưa xét hết cạnh)* → **đã xử lý** *(processed — xét hết cạnh)*. Nhờ đánh dấu, mỗi đỉnh vào hàng chờ đúng *một* lần, mỗi cạnh được xét đúng *một* lần (hai lần với vô hướng) → cả BFS lẫn DFS đều chạy `O(n + m)` — tuyến tính theo cỡ đồ thị.

## 4. BFS và DFS: khác nhau chỉ ở queue hay stack

Có hai thuật toán duyệt nền tảng. Điều bất ngờ đẹp đẽ: chúng *giống hệt nhau*, chỉ khác **cấu trúc chứa các đỉnh đã-khám-phá-chưa-xử-lý**:

> [!quote] Skiena (tr. 221)
> "The difference between BFS and DFS lies in the order in which they explore vertices. This order depends completely upon the container data structure used to store the discovered but not processed vertices."
>
> *Khác biệt giữa BFS và DFS nằm ở **thứ tự** chúng khám phá đỉnh. Thứ tự này **phụ thuộc hoàn toàn** vào **cấu trúc chứa** các đỉnh đã-khám-phá-nhưng-chưa-xử-lý.*

- **Queue (FIFO)** → **BFS (bề rộng)**: lấy đỉnh *cũ nhất* trước → thăm lan toả theo **tầng** từ điểm xuất phát. Vì lan theo tầng, BFS cho **đường ngắn nhất (số cạnh)** trên đồ thị *không trọng số*.
- **Stack (LIFO)** → **DFS (bề sâu)**: lấy đỉnh *mới nhất* trước → lao sâu theo một nhánh tới khi cụt rồi *quay lui* (backtrack). DFS cài gọn bằng **đệ quy** (dùng luôn call stack). DFS là nền cho phát hiện chu trình, sắp xếp tô-pô, thành phần liên thông mạnh.

```
Cùng đồ thị, xuất phát từ 1:

BFS (queue):  1 → {2,3} → {4,5} → {6}     lan theo tầng, gần trước xa sau
              tầng0  tầng1   tầng2  tầng3

DFS (stack):  1 → 2 → 4 → 3 → 5 → 6       lao sâu một nhánh rồi quay lui
```

Đây chính là lý do Bài 2 dạy *cả* stack *lẫn* queue: đổi một cái là đổi cả hành vi duyệt. Demo mục 5 chạy cả hai trên cùng đồ thị để thấy khác biệt, và dùng BFS tính khoảng cách ngắn nhất.

## 5. Demo: adjacency list, BFS, DFS

Demo dựng đồ thị 6 đỉnh bằng danh sách kề, chạy BFS (queue) và DFS (đệ quy) từ đỉnh 1 — *cùng* đồ thị, *khác* thứ tự thăm; dùng BFS lấy khoảng cách ngắn nhất (số cạnh); rồi đếm **thành phần liên thông** của một đồ thị có "đảo" rời.

```typescript
import { strict as assert } from "node:assert";

// ─── ĐỒ THỊ bằng DANH SÁCH KỀ (adjacency list): đỉnh → mảng các đỉnh kề ───
// Vô hướng: thêm cạnh (u,v) thì cả u→v lẫn v→u. Hàng xóm sắp tăng → tất định.
class Graph {
  private adj = new Map<number, number[]>();
  addEdge(u: number, v: number): void {
    if (!this.adj.has(u)) this.adj.set(u, []);
    if (!this.adj.has(v)) this.adj.set(v, []);
    this.adj.get(u)!.push(v);
    this.adj.get(v)!.push(u);
  }
  neighbors(u: number): number[] { return (this.adj.get(u) ?? []).slice().sort((a, b) => a - b); }
  vertices(): number[] { return [...this.adj.keys()].sort((a, b) => a - b); }
}

// Đồ thị mẫu 6 đỉnh (số cạnh m=7 « n^2=36 → thưa → danh sách kề hợp lý).
const g = new Graph();
for (const [u, v] of [[1, 2], [1, 3], [2, 4], [3, 4], [3, 5], [4, 6], [5, 6]]) g.addEdge(u, v);

// ─── BFS: dùng HÀNG ĐỢI (FIFO) → lan TOẢ theo tầng → cho khoảng cách ngắn nhất (số cạnh) ───
function bfs(start: number): { order: number[]; dist: Map<number, number> } {
  const order: number[] = [];
  const dist = new Map<number, number>([[start, 0]]);
  const seen = new Set<number>([start]);
  const queue: number[] = [start];
  let head = 0;
  while (head < queue.length) {
    const u = queue[head++];            // lấy từ ĐẦU hàng đợi
    order.push(u);
    for (const v of g.neighbors(u)) {
      if (!seen.has(v)) { seen.add(v); dist.set(v, dist.get(u)! + 1); queue.push(v); }
    }
  }
  return { order, dist };
}

// ─── DFS: dùng NGĂN XẾP (đệ quy = call stack, LIFO) → lao sâu theo một nhánh ───
function dfs(start: number): number[] {
  const order: number[] = [];
  const seen = new Set<number>();
  function visit(u: number): void {
    seen.add(u);
    order.push(u);
    for (const v of g.neighbors(u)) if (!seen.has(v)) visit(v);  // lao sâu trước
  }
  visit(start);
  return order;
}

const b = bfs(1);
const d = dfs(1);
console.log("ĐỒ THỊ (6 đỉnh, 7 cạnh) — danh sách kề:");
for (const u of g.vertices()) console.log(`  ${u}: [${g.neighbors(u).join(", ")}]`);

console.log("\nDUYỆT từ đỉnh 1:");
console.log(`  BFS (hàng đợi FIFO): ${b.order.join(" ")}   ← lan theo tầng`);
console.log(`  DFS (ngăn xếp LIFO): ${d.join(" ")}   ← lao sâu một nhánh`);
console.log(`  cùng đồ thị, khác thứ tự — khác biệt DUY NHẤT là queue (BFS) vs stack (DFS).`);

// BFS cho khoảng cách ngắn nhất (số cạnh) từ đỉnh 1 — DFS thì KHÔNG.
console.log("\nKHOẢNG CÁCH NGẮN NHẤT (số cạnh) từ 1, nhờ BFS lan theo tầng:");
for (const u of g.vertices()) console.log(`  1 → ${u}: ${b.dist.get(u)} cạnh`);
assert.equal(b.dist.get(6), 3);           // 1-3-5-6 hoặc 1-2-4-6: 3 cạnh
assert.equal(b.dist.get(1), 0);

// Cả hai thăm ĐỦ mọi đỉnh của thành phần liên thông chứa 1.
assert.deepEqual([...b.order].sort((a, c) => a - c), [1, 2, 3, 4, 5, 6]);
assert.deepEqual([...d].sort((a, c) => a - c), [1, 2, 3, 4, 5, 6]);
assert.equal(b.order.length, 6);

// ─── ĐẾM THÀNH PHẦN LIÊN THÔNG: chạy BFS từ mỗi đỉnh chưa thăm ───
function countComponents(gr: Graph): number {
  const seen = new Set<number>();
  let comps = 0;
  for (const s of gr.vertices()) {
    if (seen.has(s)) continue;
    comps++;
    const q = [s]; seen.add(s); let h = 0;
    while (h < q.length) { const u = q[h++]; for (const v of gr.neighbors(u)) if (!seen.has(v)) { seen.add(v); q.push(v); } }
  }
  return comps;
}
const g2 = new Graph();            // thêm một "đảo" rời: 7-8
for (const [u, v] of [[1, 2], [1, 3], [2, 4], [7, 8]]) g2.addEdge(u, v);
console.log(`\nTHÀNH PHẦN LIÊN THÔNG của đồ thị {1-2,1-3,2-4, 7-8} = ${countComponents(g2)}  (cụm {1,2,3,4} và {7,8})`);
assert.equal(countComponents(g2), 2);

console.log("\nBFS/DFS đều O(n + m) (mỗi đỉnh, mỗi cạnh xét một lần). Chọn queue→BFS, stack→DFS (Skiena tr.221).");
```

Kết quả chạy thật *(tất định)*:

```
ĐỒ THỊ (6 đỉnh, 7 cạnh) — danh sách kề:
  1: [2, 3]
  2: [1, 4]
  3: [1, 4, 5]
  4: [2, 3, 6]
  5: [3, 6]
  6: [4, 5]

DUYỆT từ đỉnh 1:
  BFS (hàng đợi FIFO): 1 2 3 4 5 6   ← lan theo tầng
  DFS (ngăn xếp LIFO): 1 2 4 3 5 6   ← lao sâu một nhánh
  cùng đồ thị, khác thứ tự — khác biệt DUY NHẤT là queue (BFS) vs stack (DFS).

KHOẢNG CÁCH NGẮN NHẤT (số cạnh) từ 1, nhờ BFS lan theo tầng:
  1 → 1: 0 cạnh
  1 → 2: 1 cạnh
  1 → 3: 1 cạnh
  1 → 4: 2 cạnh
  1 → 5: 2 cạnh
  1 → 6: 3 cạnh

THÀNH PHẦN LIÊN THÔNG của đồ thị {1-2,1-3,2-4, 7-8} = 2  (cụm {1,2,3,4} và {7,8})

BFS/DFS đều O(n + m) (mỗi đỉnh, mỗi cạnh xét một lần). Chọn queue→BFS, stack→DFS (Skiena tr.221).
```

Ba điều đáng thấm. **(1) Cùng đồ thị, khác thứ tự — chỉ vì queue vs stack:** BFS ra `1 2 3 4 5 6` (hết tầng này mới sang tầng khác), DFS ra `1 2 4 3 5 6` (lao xuống `1→2→4` trước khi lùi lại xét `3`); đổi hàng đợi thành ngăn xếp là đổi toàn bộ hành vi. **(2) BFS tặng kèm đường ngắn nhất:** vì lan theo tầng, lần đầu BFS chạm đỉnh `6` là đã đi đúng `3` cạnh — số cạnh ít nhất; DFS *không* có tính chất này (có thể tới `6` qua đường dài hơn). **(3) Duyệt = công cụ đa năng:** thêm một vòng ngoài chạy duyệt từ mỗi đỉnh chưa thăm là **đếm thành phần liên thông** (ở đây 2 cụm) — cùng bộ khung giải được hàng loạt bài.

> [!note] Tự thử
> 1. Viết DFS **lặp** (iterative) dùng ngăn xếp tường minh thay cho đệ quy. Thứ tự thăm có giống hệt DFS đệ quy không? Vì sao có thể khác? (Gợi ý: thứ tự đẩy hàng xóm vào stack.)
> 2. Vì sao BFS cho đường ngắn nhất (số cạnh) còn DFS thì không? Dựng một ví dụ nhỏ DFS tới đích bằng đường dài hơn.
> 3. Đồ thị **có hướng**: sửa `addEdge` chỉ thêm `u→v` (bỏ `v→u`). BFS từ 1 giờ thăm được những đỉnh nào? Thành phần liên thông còn đúng không?
> 4. Phát hiện **chu trình** bằng DFS: nếu gặp một đỉnh *đã khám phá nhưng chưa xử lý xong* (không phải cha vừa đến), đó là chu trình. Cài thử trên đồ thị demo.

## 6. Bản đồ khoá DSA

| # | Bài | Chủ đề | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | Thuật toán & tính đúng | nền: đúng vs hiệu quả | Skiena Ch1 + Grokking |
| 1 | Phân tích Big-O | đo chi phí khi `n` lớn | Skiena Ch2 |
| 2 | CTDL tuyến tính | mảng / list / stack / queue | Skiena Ch3 |
| 3 | Từ điển & bảng băm | tra cứu O(1) trung bình | Skiena Ch3 |
| 4 | Heap & cây tìm kiếm | lấy min/max, tra có thứ tự | Skiena Ch3–4 |
| 5 | Sắp xếp | quicksort / mergesort / heapsort | Skiena Ch4 |
| 6 | Chia để trị & đệ quy | bẻ nhỏ bài toán, master theorem | Skiena Ch5 |
| 7 | **Đồ thị: biểu diễn & duyệt** ← *đang ở đây* | BFS / DFS | Skiena Ch7 |
| 8 | Đồ thị trọng số: MST & đường ngắn nhất | Dijkstra / Prim / Kruskal | Skiena Ch8 |
| 9 | Quy hoạch động | tối ưu bằng bảng con | Skiena Ch10 |
| 10 | Tìm kiếm tổ hợp & backtracking | duyệt không gian lời giải | Skiena Ch9 |
| 11 | NP-đầy đủ & bài toán khó | khi không có lời giải nhanh | Skiena Ch11–12 |
| 12 | *(nâng cao)* Khớp chuỗi | KMP / Rabin–Karp | Skiena §6.7 + CLRS Ch32 |
| 13 | *(nâng cao)* Luồng mạng | max-flow / min-cut | Skiena §8.5 + CLRS Ch24 |
| 14 | *(nâng cao)* Thuật toán ngẫu nhiên | randomized quicksort, Monte Carlo | Skiena Ch6 |

[Bài 8](bai_08_do-thi-trong-so.md) thêm **trọng số** lên cạnh: BFS-lan-theo-tầng tiến hoá thành Dijkstra; DFS là nền backtracking ([Bài 10](bai_10_backtracking.md)).

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 7.1 — Đồ thị G = (V, E) là gì? Vì sao nói "mọi thứ đều là đồ thị"?
> **Đáp:** tập **đỉnh** V nối bởi tập **cạnh** E (cặp đỉnh). Mô hình hoá mọi *quan hệ*: mạng xã hội, bản đồ, phụ thuộc task, web — "chủ đề thống nhất của CS" (Skiena tr. 197).

> [!question] Thẻ 7.2 — Danh sách kề vs ma trận kề: bộ nhớ và chi phí? Thường chọn cái nào?
> **Đáp:** ma trận O(n²) bộ nhớ, kiểm cạnh O(1); danh sách O(n+m) bộ nhớ, duyệt hàng xóm theo bậc. Đồ thị thực tế hầu hết **thưa** → mặc định **danh sách kề** (Skiena tr. 202, 204).

> [!question] Thẻ 7.3 — Ý tưởng cốt lõi để duyệt đồ thị mà không lặp vô hạn?
> **Đáp:** **đánh dấu** mỗi đỉnh khi lần đầu thăm, theo dõi phần chưa khám phá xong (3 trạng thái: chưa khám phá → đã khám phá → đã xử lý). Nhờ vậy mỗi đỉnh/cạnh xét một lần → O(n+m) (Skiena tr. 213).

> [!question] Thẻ 7.4 — BFS và DFS khác nhau ở đâu? Hệ quả?
> **Đáp:** khác **cấu trúc chứa** đỉnh đã-khám-phá-chưa-xử-lý: **queue (FIFO) → BFS** (lan theo tầng, cho đường ngắn nhất số cạnh); **stack (LIFO) → DFS** (lao sâu, quay lui; cài bằng đệ quy) (Skiena tr. 221).

> [!question] Thẻ 7.5 — Vì sao BFS cho đường ngắn nhất (số cạnh) còn DFS thì không?
> **Đáp:** BFS lan đều theo tầng nên lần đầu chạm một đỉnh là qua số cạnh ít nhất. DFS lao sâu một nhánh, có thể tới đỉnh qua đường vòng dài hơn trước.

## 8. Câu hỏi tự kiểm tra

1. Cho ba bài toán thực tế và chỉ ra đỉnh/cạnh của đồ thị tương ứng mỗi bài. *(mục 1)*
2. Đồ thị mạng xã hội 1 tỷ người, mỗi người ~300 bạn. Ma trận kề tốn bao nhiêu ô? Vì sao phải dùng danh sách kề? *(mục 2)*
3. Giải thích ba trạng thái của một đỉnh khi duyệt, và vì sao đánh dấu cho ra O(n+m). *(mục 3)*
4. BFS và DFS cùng khung, khác cái gì? Mỗi cái mạnh ở bài toán nào? *(mục 4)*
5. Chạy demo mục 5. Vì sao BFS ra `1 2 3 4 5 6` còn DFS ra `1 2 4 3 5 6`? *(mục 4 & 5)*

## Tóm tắt một trang

```
BÀI 7 — ĐỒ THỊ: BIỂU DIỄN & DUYỆT
─────────────────────────────────────────────────────────
ĐỒ THỊ G=(V,E)  tập ĐỈNH nối bởi CẠNH. Mô hình mọi QUAN HỆ (mạng XH, bản đồ,
   phụ thuộc, web) — "chủ đề thống nhất của CS" (Skiena tr.197). Vô/có hướng,
   có/không trọng số.

BIỂU DIỄN  ma trận kề: O(n²) bộ nhớ, kiểm cạnh O(1). Danh sách kề: O(n+m) bộ
   nhớ, duyệt hàng xóm theo bậc. Đồ thị thực tế hầu hết THƯA (Skiena tr.202)
   → mặc định DANH SÁCH KỀ.

DUYỆT  ĐÁNH DẤU mỗi đỉnh khi lần đầu thăm (Skiena tr.213). 3 trạng thái: chưa
   khám phá → đã khám phá → đã xử lý. Mỗi đỉnh/cạnh xét 1 lần → O(n+m).

BFS vs DFS  khác DUY NHẤT: cấu trúc chứa đỉnh chờ (Skiena tr.221).
   QUEUE (FIFO) → BFS: lan theo TẦNG → đường ngắn nhất (số cạnh).
   STACK (LIFO) → DFS: lao SÂU rồi quay lui; cài bằng đệ quy → chu trình,
      sắp tô-pô, thành phần liên thông mạnh.

DEMO  6 đỉnh: BFS 1 2 3 4 5 6 (tầng), DFS 1 2 4 3 5 6 (sâu). BFS cho 1→6 = 3
   cạnh. Đếm thành phần liên thông {1,2,3,4}+{7,8} = 2.
```

## Nguồn

- **Skiena, Steven S. — *The Algorithm Design Manual*, 3rd ed.** (Springer, 2020) — **Chapter 7: Graph Traversal** (§7.1 Flavors of Graphs, §7.2 Data Structures for Graphs, §7.6 BFS, §7.8 DFS): định nghĩa đồ thị, đồ thị thưa, danh sách kề vs ma trận kề, đánh dấu khi duyệt, BFS (queue) vs DFS (stack). `tai_lieu/The Algorithm Design Manual 3rd Edition...pdf` (offset **PDF = tr. + 14** ở Ch7).
- Liên hệ: [Bài 2 — stack/queue](bai_02_ctdl-tuyen-tinh.md) (BFS/DFS khác nhau đúng ở đây); [Bài 8 — đồ thị trọng số](bai_08_do-thi-trong-so.md) (Dijkstra/MST); [cloud-base](../../cloud-base/README.md) (mạng & hệ phân tán cũng là đồ thị).

---

**Bản đồ khoá học:** [Bài 0 — Thuật toán & tính đúng](bai_00_thuat-toan-la-gi.md) · [Bài 1 — Phân tích Big-O](bai_01_big-o.md) · [Bài 2 — CTDL tuyến tính](bai_02_ctdl-tuyen-tinh.md) · [Bài 3 — Từ điển & bảng băm](bai_03_bang-bam.md) · [Bài 4 — Heap & cây tìm kiếm](bai_04_heap-cay-tim-kiem.md) · [Bài 5 — Sắp xếp](bai_05_sap-xep.md) · [Bài 6 — Chia để trị & đệ quy](bai_06_chia-de-tri.md) · **[Bài 7 — Đồ thị: duyệt] ← bạn đang ở đây** · [Bài 8 — Đồ thị trọng số](bai_08_do-thi-trong-so.md) · [Bài 9 — Quy hoạch động](bai_09_quy-hoach-dong.md) · [Bài 10 — Backtracking](bai_10_backtracking.md) · [Bài 11 — NP-đầy đủ](bai_11_np-day-du.md) · [Bài 12 — Khớp chuỗi](bai_12_khop-chuoi.md) · [Bài 13 — Luồng mạng](bai_13_luong-mang.md) · [Bài 14 — Thuật toán ngẫu nhiên](bai_14_ngau-nhien.md)

Xem thêm [README khoá học](../README.md).
