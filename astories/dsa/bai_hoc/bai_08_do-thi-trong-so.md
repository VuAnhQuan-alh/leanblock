# Bài 8 — Đồ thị trọng số: cây khung nhỏ nhất và đường đi ngắn nhất

> [!info] Về bài này
> Bài 7 duyệt đồ thị *không trọng số*. Thực tế, cạnh thường mang **số**: độ dài đường, chi phí cáp, thời gian truyền. Bài này giải hai bài toán kinh điển trên đồ thị có trọng số — **cây khung nhỏ nhất (MST)** (nối mọi đỉnh với tổng chi phí rẻ nhất, bằng **Prim** và **Kruskal**) và **đường đi ngắn nhất** từ một nguồn (bằng **Dijkstra**). Cả ba là thuật toán **tham lam** *(greedy)*; bài cũng giới thiệu **union-find**, cấu trúc nền của Kruskal. Dijkstra hoá ra chỉ là Prim đổi tiêu chí chọn — nối thẳng về BFS-lan-theo-tầng của Bài 7.
> Nguồn (Luật số 1): **Skiena** *The Algorithm Design Manual 3e* — **Chapter 8: Weighted Graph Algorithms** (§8.1 MST, §8.3 Shortest Paths) (`tai_lieu/`, trích `> [!quote] Skiena (tr. N)`, **PDF = tr. + 14** ở Ch8).
> **Chạy demo:** `node bai_08.ts` — Node 22+, không cài gói. Code tất định.
> Cần đọc trước: [Bài 7 — Đồ thị: duyệt](bai_07_do-thi-duyet.md), [Bài 4 — heap](bai_04_heap-cay-tim-kiem.md) (hàng đợi ưu tiên tăng tốc Prim/Dijkstra).

## Mục lục

1. [Tình huống: cạnh có trọng số đổi luật chơi](#1-tình-huống-cạnh-có-trọng-số-đổi-luật-chơi)
2. [Cây khung nhỏ nhất: nối mọi đỉnh rẻ nhất](#2-cây-khung-nhỏ-nhất-nối-mọi-đỉnh-rẻ-nhất)
3. [Prim và Kruskal: hai lối tham lam, cùng kết quả tối ưu](#3-prim-và-kruskal-hai-lối-tham-lam-cùng-kết-quả-tối-ưu)
4. [Đường đi ngắn nhất: Dijkstra](#4-đường-đi-ngắn-nhất-dijkstra)
5. [Demo: Prim, Kruskal, Dijkstra](#5-demo-prim-kruskal-dijkstra)
6. [Bản đồ khoá DSA](#6-bản-đồ-khoá-dsa)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Tình huống: cạnh có trọng số đổi luật chơi

> [!example] "Đường ngắn nhất" không còn là "ít cạnh nhất"
> Bài 7 dùng BFS tìm đường *ít cạnh nhất* trên đồ thị không trọng số. Nhưng trên bản đồ thật, đi qua 2 con đường nhỏ (mỗi cái 1 km) *ngắn hơn* đi 1 đường vòng 10 km — dù nhiều cạnh hơn. Khi cạnh mang **trọng số**, "ngắn nhất" nghĩa là *tổng trọng số nhỏ nhất*, và BFS không còn đủ.

> [!quote] Skiena (tr. 243)
> "Identifying the shortest path in such graphs proves more complicated than breadth-first search in unweighted graphs, but opens the door to a wide range of applications."
>
> *Tìm đường ngắn nhất trong những đồ thị như vậy **phức tạp hơn** BFS trên đồ thị không trọng số, nhưng **mở ra** vô số ứng dụng.*

Hai bài toán trọng số nền tảng, trả lời hai câu hỏi khác nhau: **(MST)** "nối *mọi* đỉnh với *tổng* chi phí rẻ nhất?" và **(shortest path)** "đường rẻ nhất từ *một nguồn* tới các đỉnh?". Đừng lẫn — demo mục 5 cho thấy chúng cho cây khác nhau.

## 2. Cây khung nhỏ nhất: nối mọi đỉnh rẻ nhất

**Cây khung** *(spanning tree)* của đồ thị liên thông là tập cạnh con nối *mọi* đỉnh mà không tạo chu trình (đúng `n − 1` cạnh). **Cây khung nhỏ nhất (MST)** là cây khung có tổng trọng số bé nhất:

> [!quote] Skiena (tr. 244)
> "For edge-weighted graphs, we are particularly interested in the minimum spanning tree—the spanning tree whose sum of edge weights is as small as possible."
>
> *Với đồ thị có trọng số cạnh, ta đặc biệt quan tâm **cây khung nhỏ nhất** — cây khung có **tổng trọng số cạnh nhỏ nhất có thể**.*

MST là lời đáp bất cứ khi nào cần **nối một tập điểm** (thành phố, nhà, nút mạng) **rẻ nhất** bằng ít đường/cáp/ống nhất tính theo trọng số: kéo cáp điện tới mọi hộ, nối các trung tâm dữ liệu, gom cụm dữ liệu.

```
Đồ thị: 6 đỉnh, 9 cạnh  (u–v: trọng số)
   1–2: 7     2–3: 10    3–4: 11
   1–3: 9     2–4: 15    3–6: 2
   1–6: 14    4–5: 6     5–6: 9

MST = 5 cạnh (= n−1), tổng 33 — lấy cạnh nhẹ trước nếu không tạo chu trình:
   3–6(2)  →  4–5(6)  →  1–2(7)  →  1–3(9)  →  5–6(9)        [tổng 33]
bỏ 4 cạnh nặng/tạo chu trình:  2–3(10), 3–4(11), 1–6(14), 2–4(15)
```

## 3. Prim và Kruskal: hai lối tham lam, cùng kết quả tối ưu

Cả hai thuật toán MST đều **tham lam** — mỗi bước chọn lựa chọn tốt nhất *tại chỗ*, không nhìn toàn cục:

> [!quote] Skiena (tr. 245)
> "Greedy algorithms make the decision of what to do next by selecting the best local option from all available choices without regard to the global structure."
>
> *Thuật toán **tham lam** quyết định bước kế tiếp bằng cách chọn **phương án tốt nhất tại chỗ** trong mọi lựa chọn sẵn có, **không màng** cấu trúc toàn cục.*

Thường tham lam cho kết quả *dưới tối ưu* (Bài 11 sẽ thấy tham lam thất bại). Nhưng với MST, hai heuristic tham lam khác nhau *đều* cho ra cây tối ưu — một tính chất đẹp và hiếm:

- **Prim** — mọc cây từ *một* đỉnh:

> [!quote] Skiena (tr. 245)
> "Prim's minimum spanning tree algorithm starts from one vertex and grows the rest of the tree one edge at a time until all vertices are included."
>
> *Thuật toán MST của **Prim** bắt đầu từ **một đỉnh** và mọc phần còn lại của cây **mỗi lần một cạnh** cho tới khi gồm đủ mọi đỉnh.*

Mỗi bước Prim chọn **cạnh nhẹ nhất nối cây với một đỉnh ngoài**. (Dùng hàng đợi ưu tiên — Bài 4 — để lấy cạnh nhẹ nhất nhanh → `O(m log n)`.)

- **Kruskal** — xét cạnh *nhẹ nhất trước*: duyệt mọi cạnh theo thứ tự trọng số tăng, thêm cạnh nếu nó **không tạo chu trình**. Để kiểm "hai đầu cạnh đã cùng một cụm chưa?" nhanh, Kruskal dùng **union-find** *(disjoint set)* — cấu trúc quản lý các cụm rời, với hai thao tác `find` (cụm của một đỉnh) và `union` (gộp hai cụm), cả hai ~`O(log n)` (hoặc gần `O(1)` với nén đường). Cùng tư tưởng "cụm liên thông" của thành phần liên thông Bài 7.

Điểm thấm: *hai* lối tham lam khác hẳn nhau (mọc từ một đỉnh vs gom cạnh toàn cục) nhưng cho *cùng* tổng trọng số tối ưu — demo mục 5 kiểm điều đó.

## 4. Đường đi ngắn nhất: Dijkstra

Bài toán khác: từ *một nguồn* `s`, tìm đường tổng-trọng-số-nhỏ-nhất tới mọi đỉnh.

> [!quote] Skiena (tr. 258)
> "Dijkstra's algorithm is the method of choice for finding shortest paths"
>
> *Thuật toán **Dijkstra** là lựa chọn hàng đầu để tìm **đường đi ngắn nhất**.*

Dijkstra mọc một cây đường-ngắn-nhất từ `s`: mỗi bước lấy đỉnh **gần nguồn nhất** trong số chưa xử lý, rồi **nới lỏng** *(relax)* các cạnh của nó (nếu đi qua nó tới hàng xóm rẻ hơn thì cập nhật). Nhìn kỹ, nó *giống hệt* Prim:

> [!quote] Skiena (tr. 259)
> "the only difference between Dijkstra's and Prim's algorithms is how they rate the desirability of each outside vertex."
>
> *khác biệt **duy nhất** giữa thuật toán Dijkstra và Prim là cách chúng **chấm điểm độ hấp dẫn** của mỗi đỉnh bên ngoài.*

- **Prim** chấm điểm đỉnh ngoài bằng *trọng số cạnh* nối nó với cây (rẻ để *nối thêm*).
- **Dijkstra** chấm bằng *khoảng cách đường đi từ `s`* tới nó (gần *nguồn* nhất).

Đây cũng chính là BFS của Bài 7 tổng quát hoá: BFS lan theo tầng vì mọi cạnh "nặng 1"; Dijkstra lan theo *khoảng cách thực* vì cạnh có trọng số — thay hàng đợi FIFO bằng **hàng đợi ưu tiên** theo khoảng cách. (Lưu ý: Dijkstra đòi trọng số **không âm**; có cạnh âm phải dùng Bellman–Ford.)

> [!note] MST ≠ đường đi ngắn nhất
> Dễ lẫn hai bài. **MST** tối thiểu *tổng* cạnh để nối *mọi* đỉnh — không quan tâm khoảng cách giữa hai đỉnh cụ thể. **Đường ngắn nhất** tối thiểu khoảng cách *từ nguồn* tới từng đỉnh — có thể dùng cạnh *không* nằm trong MST. Trong demo, đường ngắn nhất `1→5` dùng cạnh mà MST cũng có, nhưng nói chung cây Dijkstra và cây Prim khác nhau.

## 5. Demo: Prim, Kruskal, Dijkstra

Demo trên đồ thị 6 đỉnh, 9 cạnh có trọng số: chạy **Prim** và **Kruskal** (union-find) → cùng tổng trọng số MST (hai tham lam, một tối ưu); rồi **Dijkstra** từ đỉnh 1 → khoảng cách ngắn nhất, khác với cây khung.

```typescript
import { strict as assert } from "node:assert";

// Đồ thị CÓ TRỌNG SỐ, vô hướng: cạnh [u, v, w].
type Edge = [number, number, number];
const edges: Edge[] = [
  [1, 2, 7], [1, 3, 9], [1, 6, 14], [2, 3, 10], [2, 4, 15],
  [3, 4, 11], [3, 6, 2], [4, 5, 6], [5, 6, 9],
];
const V = [1, 2, 3, 4, 5, 6];

// Danh sách kề có trọng số.
const adj = new Map<number, Array<[number, number]>>();
for (const v of V) adj.set(v, []);
for (const [u, v, w] of edges) { adj.get(u)!.push([v, w]); adj.get(v)!.push([u, w]); }

// ─── PRIM: mọc cây từ MỘT đỉnh, mỗi bước thêm CẠNH NHẸ NHẤT nối cây với ngoài ───
function prim(start: number): { weight: number; picked: Edge[] } {
  const inTree = new Set<number>([start]);
  const picked: Edge[] = [];
  let weight = 0;
  while (inTree.size < V.length) {
    let best: Edge | null = null;
    for (const u of inTree)                         // mọi cạnh từ cây ra ngoài
      for (const [v, w] of adj.get(u)!.slice().sort((a, b) => a[0] - b[0]))
        if (!inTree.has(v) && (best === null || w < best[2])) best = [u, v, w];
    inTree.add(best![1]); picked.push(best!); weight += best![2];
  }
  return { weight, picked };
}

// ─── KRUSKAL: sắp mọi cạnh tăng dần, thêm cạnh nếu KHÔNG tạo chu trình (union-find) ───
function kruskal(): { weight: number; picked: Edge[] } {
  const parent = new Map<number, number>(V.map((v) => [v, v]));
  function find(x: number): number { while (parent.get(x)! !== x) x = parent.get(x)!; return x; }
  function union(a: number, b: number): boolean {
    const ra = find(a), rb = find(b);
    if (ra === rb) return false;                    // cùng cây → thêm vào sẽ tạo chu trình
    parent.set(ra, rb); return true;
  }
  const picked: Edge[] = [];
  let weight = 0;
  for (const [u, v, w] of [...edges].sort((a, b) => a[2] - b[2]))  // cạnh nhẹ trước
    if (union(u, v)) { picked.push([u, v, w]); weight += w; }
  return { weight, picked };
}

// ─── DIJKSTRA: như Prim nhưng chọn đỉnh GẦN NGUỒN NHẤT (khoảng cách đường đi) ───
function dijkstra(start: number): Map<number, number> {
  const dist = new Map<number, number>(V.map((v) => [v, Infinity]));
  dist.set(start, 0);
  const done = new Set<number>();
  while (done.size < V.length) {
    let u = -1, best = Infinity;                    // đỉnh chưa xong gần nguồn nhất
    for (const v of V) if (!done.has(v) && dist.get(v)! < best) { best = dist.get(v)!; u = v; }
    if (u === -1) break;
    done.add(u);
    for (const [v, w] of adj.get(u)!)               // nới lỏng (relax) các cạnh
      if (dist.get(u)! + w < dist.get(v)!) dist.set(v, dist.get(u)! + w);
  }
  return dist;
}

const p = prim(1), k = kruskal();
console.log("CÂY KHUNG NHỎ NHẤT (MST) — đồ thị 6 đỉnh, 9 cạnh có trọng số:");
console.log(`  Prim    : tổng trọng số = ${p.weight}, chọn ${p.picked.length} cạnh`);
console.log(`  Kruskal : tổng trọng số = ${k.weight}, chọn ${k.picked.length} cạnh`);
console.log(`  cạnh Kruskal chọn (nhẹ→nặng): ${k.picked.map(([u, v, w]) => `${u}-${v}(${w})`).join(", ")}`);
assert.equal(p.weight, k.weight);          // HAI greedy khác nhau → CÙNG trọng số tối ưu
assert.equal(p.picked.length, V.length - 1);  // cây khung có đúng n-1 cạnh

// ─── ĐƯỜNG ĐI NGẮN NHẤT từ đỉnh 1 (Dijkstra) — KHÁC với cây khung nhỏ nhất ───
const dist = dijkstra(1);
console.log("\nĐƯỜNG ĐI NGẮN NHẤT (tổng trọng số) từ đỉnh 1 — Dijkstra:");
for (const v of V) console.log(`  1 → ${v}: ${dist.get(v)}`);
assert.equal(dist.get(5), 20);             // 1-3-6-5 = 9+2+9 = 20 (không phải 1-3-4-5=26)
assert.equal(dist.get(6), 11);             // 1-3-6 = 9+2 = 11 (không phải cạnh 1-6=14)

console.log("\nMST (nối MỌI đỉnh rẻ nhất) KHÁC đường ngắn nhất (từ MỘT nguồn). Prim/Kruskal tham lam");
console.log("cho cùng MST tối ưu; Dijkstra = Prim nhưng chọn đỉnh gần NGUỒN nhất (Skiena tr.259).");
```

Kết quả chạy thật *(tất định)*:

```
CÂY KHUNG NHỎ NHẤT (MST) — đồ thị 6 đỉnh, 9 cạnh có trọng số:
  Prim    : tổng trọng số = 33, chọn 5 cạnh
  Kruskal : tổng trọng số = 33, chọn 5 cạnh
  cạnh Kruskal chọn (nhẹ→nặng): 3-6(2), 4-5(6), 1-2(7), 1-3(9), 5-6(9)

ĐƯỜNG ĐI NGẮN NHẤT (tổng trọng số) từ đỉnh 1 — Dijkstra:
  1 → 1: 0
  1 → 2: 7
  1 → 3: 9
  1 → 4: 20
  1 → 5: 20
  1 → 6: 11

MST (nối MỌI đỉnh rẻ nhất) KHÁC đường ngắn nhất (từ MỘT nguồn). Prim/Kruskal tham lam
cho cùng MST tối ưu; Dijkstra = Prim nhưng chọn đỉnh gần NGUỒN nhất (Skiena tr.259).
```

Ba điều đáng thấm. **(1) Hai tham lam, một tối ưu:** Prim (mọc từ đỉnh 1) và Kruskal (gom cạnh nhẹ toàn cục) đi đường hoàn toàn khác nhau nhưng *cùng* ra tổng trọng số 33 — với MST, tham lam *chứng minh được* tối ưu (khác Bài 11). **(2) Kruskal đọc được tư duy "cạnh nhẹ trước":** nó lần lượt lấy `3-6(2), 4-5(6), 1-2(7), 1-3(9)`, rồi `5-6(9)`; bỏ qua mọi cạnh nối hai đỉnh *đã cùng cụm* (nhờ union-find) để không tạo chu trình. **(3) Đường ngắn nhất ≠ MST:** Dijkstra cho `1→6 = 11` (qua `1-3-6`, *không* dùng cạnh trực tiếp `1-6` nặng 14), `1→5 = 20` — đây là cây *khác* mục tiêu với MST, dù trên đồ thị này vài cạnh trùng.

> [!note] Tự thử
> 1. Thêm cạnh `1-6` trọng số **3** (thay vì 14). MST đổi thế nào? Dijkstra `1→6` giờ bằng bao nhiêu?
> 2. Cho Dijkstra một cạnh **âm** (vd `3-6 = −5`): kết quả còn đúng không? Vì sao Dijkstra *giả định* trọng số không âm? (Gợi ý: một khi đỉnh "xong", Dijkstra không xét lại.)
> 3. Tăng tốc Prim/Dijkstra bằng **hàng đợi ưu tiên** (Bài 4) thay vòng quét `O(V)` tìm min: độ phức tạp đổi từ `O(V²)` sang gì?
> 4. Dựng một đồ thị mà **cây Prim khác hẳn cây Dijkstra** từ cùng một đỉnh, để thấy MST và cây đường-ngắn-nhất là hai thứ khác nhau. *(mục 4)*

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
| 7 | Đồ thị: biểu diễn & duyệt | BFS / DFS | Skiena Ch7 |
| 8 | **Đồ thị trọng số: MST & đường ngắn nhất** ← *đang ở đây* | Dijkstra / Prim / Kruskal | Skiena Ch8 |
| 9 | Quy hoạch động | tối ưu bằng bảng con | Skiena Ch10 |
| 10 | Tìm kiếm tổ hợp & backtracking | duyệt không gian lời giải | Skiena Ch9 |
| 11 | NP-đầy đủ & bài toán khó | khi không có lời giải nhanh | Skiena Ch11–12 |
| 12 | *(nâng cao)* Khớp chuỗi | KMP / Rabin–Karp | Skiena §6.7 + CLRS Ch32 |
| 13 | *(nâng cao)* Luồng mạng | max-flow / min-cut | Skiena §8.5 + CLRS Ch24 |
| 14 | *(nâng cao)* Thuật toán ngẫu nhiên | randomized quicksort, Monte Carlo | Skiena Ch6 |

Greedy ở đây *chứng minh được* tối ưu; [Bài 9 — quy hoạch động](bai_09_quy-hoach-dong.md) xử lý khi greedy *không* đủ; [Bài 13 — luồng mạng](bai_13_luong-mang.md) tiếp tục trên đồ thị trọng số.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 8.1 — Vì sao BFS không đủ để tìm đường ngắn nhất trên đồ thị có trọng số?
> **Đáp:** BFS tối thiểu *số cạnh*, nhưng khi cạnh có trọng số, "ngắn nhất" là *tổng trọng số nhỏ nhất* — đi nhiều cạnh nhẹ có thể rẻ hơn ít cạnh nặng (Skiena tr. 243). Cần Dijkstra.

> [!question] Thẻ 8.2 — Cây khung nhỏ nhất (MST) là gì? Dùng khi nào?
> **Đáp:** tập `n−1` cạnh nối **mọi** đỉnh, không chu trình, **tổng trọng số nhỏ nhất** (Skiena tr. 244). Dùng để nối một tập điểm rẻ nhất: cáp điện, mạng, gom cụm.

> [!question] Thẻ 8.3 — Prim và Kruskal khác nhau ra sao? Kết quả?
> **Đáp:** Prim **mọc cây từ một đỉnh**, mỗi bước thêm cạnh nhẹ nhất nối cây với ngoài (Skiena tr. 245). Kruskal **gom cạnh nhẹ nhất toàn cục**, bỏ cạnh tạo chu trình (union-find). Hai tham lam khác nhau → **cùng** MST tối ưu.

> [!question] Thẻ 8.4 — Thuật toán tham lam (greedy) là gì? Vì sao MST đặc biệt?
> **Đáp:** chọn **tốt nhất tại chỗ**, không màng toàn cục (Skiena tr. 245). Thường dưới tối ưu, nhưng MST là ca hiếm mà greedy *chứng minh được* tối ưu.

> [!question] Thẻ 8.5 — Dijkstra khác Prim ở đâu? Quan hệ với BFS?
> **Đáp:** khác **duy nhất** ở cách chấm điểm đỉnh ngoài — Prim dùng *trọng số cạnh*, Dijkstra dùng *khoảng cách từ nguồn* (Skiena tr. 259). Dijkstra = BFS tổng quát cho đồ thị trọng số (hàng đợi ưu tiên thay FIFO); đòi trọng số không âm.

## 8. Câu hỏi tự kiểm tra

1. Phân biệt bài toán MST và bài toán đường-đi-ngắn-nhất. Mỗi bài trả lời câu hỏi gì? *(mục 1, 2, 4)*
2. Mô tả một bước của Prim và một bước của Kruskal. Kruskal cần cấu trúc gì, để làm gì? *(mục 3)*
3. "Greedy" nghĩa là gì? Cho một ví dụ greedy *thất bại* và giải thích vì sao MST thì không. *(mục 3)*
4. Dijkstra khác Prim đúng một chỗ — chỗ nào? Vì sao Dijkstra cần trọng số không âm? *(mục 4)*
5. Chạy demo mục 5. Vì sao Dijkstra cho `1→6 = 11` chứ không phải 14 (cạnh trực tiếp)? *(mục 4 & 5)*

## Tóm tắt một trang

```
BÀI 8 — ĐỒ THỊ TRỌNG SỐ: MST & ĐƯỜNG NGẮN NHẤT
─────────────────────────────────────────────────────────
TRỌNG SỐ đổi luật  "ngắn nhất" = tổng trọng số nhỏ nhất, không phải ít cạnh
   nhất → BFS không đủ (Skiena tr.243).

MST (cây khung nhỏ nhất)  n-1 cạnh nối MỌI đỉnh, không chu trình, TỔNG trọng
   số bé nhất (Skiena tr.244). Nối tập điểm rẻ nhất: cáp/mạng/ống.

GREEDY  chọn tốt nhất TẠI CHỖ, kệ toàn cục (Skiena tr.245). Thường dưới tối
   ưu — nhưng MST là ca hiếm greedy CHỨNG MINH tối ưu.
   PRIM: mọc cây từ 1 đỉnh, thêm cạnh nhẹ nhất nối cây↔ngoài (Skiena tr.245).
   KRUSKAL: gom cạnh nhẹ toàn cục, bỏ cạnh tạo chu trình (UNION-FIND).
   → hai lối khác nhau, CÙNG tổng trọng số tối ưu.

ĐƯỜNG NGẮN NHẤT  Dijkstra (Skiena tr.258): từ nguồn s, lấy đỉnh GẦN NGUỒN
   nhất rồi RELAX cạnh. = PRIM đổi tiêu chí: chấm bằng khoảng-cách-từ-s thay
   vì trọng-số-cạnh (Skiena tr.259). = BFS tổng quát (PQ thay FIFO). Đòi
   trọng số KHÔNG ÂM.

DEMO  6 đỉnh 9 cạnh: Prim = Kruskal = 33 (tối ưu). Dijkstra từ 1: 1→6=11
   (qua 1-3-6, ko dùng cạnh 1-6=14), 1→5=20. MST ≠ cây đường-ngắn-nhất.
```

## Nguồn

- **Skiena, Steven S. — *The Algorithm Design Manual*, 3rd ed.** (Springer, 2020) — **Chapter 8: Weighted Graph Algorithms** (§8.1 Minimum Spanning Trees: Prim, Kruskal, union-find; §8.3 Shortest Paths: Dijkstra): đồ thị trọng số, định nghĩa MST, thuật toán tham lam, Prim vs Kruskal, Dijkstra = Prim đổi tiêu chí. `tai_lieu/The Algorithm Design Manual 3rd Edition...pdf` (offset **PDF = tr. + 14** ở Ch8).
- Liên hệ: [Bài 7 — BFS/DFS](bai_07_do-thi-duyet.md) (Dijkstra tổng quát BFS); [Bài 4 — heap](bai_04_heap-cay-tim-kiem.md) (hàng đợi ưu tiên tăng tốc Prim/Dijkstra); [Bài 9 — quy hoạch động](bai_09_quy-hoach-dong.md) (khi greedy không đủ).

---

**Bản đồ khoá học:** [Bài 0 — Thuật toán & tính đúng](bai_00_thuat-toan-la-gi.md) · [Bài 1 — Phân tích Big-O](bai_01_big-o.md) · [Bài 2 — CTDL tuyến tính](bai_02_ctdl-tuyen-tinh.md) · [Bài 3 — Từ điển & bảng băm](bai_03_bang-bam.md) · [Bài 4 — Heap & cây tìm kiếm](bai_04_heap-cay-tim-kiem.md) · [Bài 5 — Sắp xếp](bai_05_sap-xep.md) · [Bài 6 — Chia để trị & đệ quy](bai_06_chia-de-tri.md) · [Bài 7 — Đồ thị: duyệt](bai_07_do-thi-duyet.md) · **[Bài 8 — Đồ thị trọng số] ← bạn đang ở đây** · [Bài 9 — Quy hoạch động](bai_09_quy-hoach-dong.md) · [Bài 10 — Backtracking](bai_10_backtracking.md) · [Bài 11 — NP-đầy đủ](bai_11_np-day-du.md) · [Bài 12 — Khớp chuỗi](bai_12_khop-chuoi.md) · [Bài 13 — Luồng mạng](bai_13_luong-mang.md) · [Bài 14 — Thuật toán ngẫu nhiên](bai_14_ngau-nhien.md)

Xem thêm [README khoá học](../README.md).
