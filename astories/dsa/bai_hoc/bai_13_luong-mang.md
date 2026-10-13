# Bài 13 — Luồng mạng: max-flow, min-cut, và quy về luồng *(nâng cao)*

> [!info] Về bài này
> **Luồng mạng** *(network flow)* hỏi: qua một mạng ống có sức chứa giới hạn, gửi được tối đa bao nhiêu "hàng" từ nguồn `s` tới đích `t`? Tự thân đã hữu dụng (giao thông, băng thông, cấp thoát nước), nhưng sức mạnh thật nằm ở chỗ **rất nhiều bài toán khác quy về nó** — ghép cặp, kết nối, phân công. Bài này ba trụ: thuật toán **Ford–Fulkerson** (đường tăng luồng), định lý đẹp **max-flow = min-cut**, và kỹ thuật **rút gọn** (Bài 11) một bài lạ về luồng mạng — minh hoạ bằng *bipartite matching*.
> Nguồn (Luật số 1): **Skiena** *The Algorithm Design Manual 3e* — **§8.5 Network Flows and Bipartite Matching** (`tai_lieu/`, trích `> [!quote] Skiena (tr. N)`, **PDF = tr. + 14** ở Ch8). Tham khảo chuẩn: **CLRS 4e Ch24** (bản PDF lỗi phông — không trích nguyên văn, như [Bài 12](bai_12_khop-chuoi.md)).
> **Chạy demo:** `node bai_13.ts` — Node 22+, không cài gói. Code tất định.
> Cần đọc trước: [Bài 8 — đồ thị trọng số](bai_08_do-thi-trong-so.md), [Bài 7 — BFS](bai_07_do-thi-duyet.md) (tìm đường tăng), [Bài 11 — rút gọn](bai_11_np-day-du.md).

## Mục lục

1. [Tình huống: bao nhiêu hàng chảy qua được mạng ống](#1-tình-huống-bao-nhiêu-hàng-chảy-qua-được-mạng-ống)
2. [Luồng mạng: đồ thị như mạng ống](#2-luồng-mạng-đồ-thị-như-mạng-ống)
3. [Ford-Fulkerson: đường tăng luồng](#3-ford-fulkerson-đường-tăng-luồng)
4. [Max-flow = min-cut, và sức mạnh của quy về luồng](#4-max-flow--min-cut-và-sức-mạnh-của-quy-về-luồng)
5. [Demo: max-flow, min-cut, bipartite matching](#5-demo-max-flow-min-cut-bipartite-matching)
6. [Bản đồ khoá DSA](#6-bản-đồ-khoá-dsa)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Tình huống: bao nhiêu hàng chảy qua được mạng ống

> [!example] Mạng lưới có nút cổ chai
> Một mạng ống nước: nguồn `s`, bể chứa `t`, giữa là các ống với sức chứa khác nhau (ống to tải nhiều, ống nhỏ tải ít). Bơm nước từ `s`, hỏi: **tối đa** bao nhiêu đơn vị nước tới được `t` mỗi giây? Không phải cứ cộng sức chứa các ống ra `s` — vì xuống dưới có thể gặp *nút cổ chai* chặn lại. Cùng bài toán cho: băng thông mạng, lưu lượng giao thông, số chuyến hàng qua kho trung chuyển.

> [!quote] Skiena (tr. 267)
> "An edge-weighted graph can be interpreted as a network of pipes, where the weight of an edge determines the capacity of the pipe."
>
> *Một đồ thị có trọng số cạnh có thể được hiểu như một **mạng ống**, ở đó **trọng số cạnh quy định sức chứa của ống**.*

## 2. Luồng mạng: đồ thị như mạng ống

Bài toán phát biểu gọn:

> [!quote] Skiena (tr. 267)
> "The network flow problem asks for the maximum amount of flow that can be sent from vertices s to t in a given weighted graph G while respecting the maximum capacities of each pipe."
>
> *Bài toán **luồng mạng** hỏi **lượng luồng lớn nhất** có thể gửi từ đỉnh `s` tới `t` trong đồ thị trọng số `G`, trong khi **tôn trọng sức chứa tối đa** của mỗi ống.*

Một *luồng* hợp lệ phải thoả hai ràng buộc: **sức chứa** (luồng qua mỗi cạnh ≤ sức chứa cạnh đó) và **bảo toàn** (tại mọi đỉnh trừ `s`, `t`: luồng vào = luồng ra — không tạo cũng không mất hàng). Mục tiêu: cực đại luồng ra khỏi `s` (= luồng vào `t`).

```
Mạng 6 đỉnh (s=0, t=5) — cạnh "u→v: sức chứa", khớp đúng mảng edges ở demo:
   s→1: 16     1→3: 12     2→4: 14     3→t: 20
   s→2: 13     2→1: 4      4→3: 7      4→t: 4
               3→2: 9

Hai nhánh chính: s→1→3→t và s→2→4→t; các cạnh chéo (2→1, 3→2, 4→3) nối hai nhánh.
Mục tiêu: luồng lớn nhất từ s tới t  (max-flow = 23).
```

## 3. Ford-Fulkerson: đường tăng luồng

Ý tưởng **Ford–Fulkerson**: bắt đầu luồng 0, rồi lặp — tìm một **đường tăng luồng** *(augmenting path)* từ `s` tới `t` còn chỗ trống, đẩy thêm luồng dọc đường đó bằng **nút cổ chai** (sức chứa còn lại nhỏ nhất trên đường); lặp tới khi không còn đường nào.

Mấu chốt là **đồ thị thặng dư** *(residual graph)*: với mỗi cạnh ta theo dõi sức chứa *còn lại*; khi đẩy `f` đơn vị qua cạnh `(u,v)`, ta *giảm* chỗ trống chiều thuận `u→v` đi `f` *và tăng* chiều nghịch `v→u` đi `f`. Cạnh nghịch cho phép thuật toán *"rút lại"* quyết định cũ nếu sau này thấy sai — đó là lý do Ford–Fulkerson *đúng* (hội tụ về tối ưu), không kẹt ở lời giải dở như tham lam thuần (Bài 8).

Tìm đường tăng luồng bằng **BFS** (Bài 7) trên residual chính là biến thể **Edmonds–Karp**, bảo đảm số lần tăng là đa thức. Demo mục 5 cài đúng cách đó.

```
Một vòng Ford–Fulkerson:
  1. BFS trên đồ thị thặng dư tìm đường s → t còn chỗ trống
  2. không còn đường?  → DỪNG, luồng hiện tại là tối ưu
  3. có đường?  → bottleneck = min(chỗ trống trên đường)
                   đẩy bottleneck: thuận −bottleneck, nghịch +bottleneck
                   cộng vào tổng luồng; lặp lại
```

## 4. Max-flow = min-cut, và sức mạnh của quy về luồng

Khi nào biết luồng đã cực đại? Câu trả lời là một trong những định lý đẹp nhất của lý thuyết đồ thị, nối **luồng** với **lát cắt**. Một **lát cắt s–t** là tập cạnh mà xoá đi thì `s` và `t` đứt liên lạc:

> [!quote] Skiena (tr. 269)
> "A set of edges whose deletion separates s from t [...] is called an s–t cut."
>
> *Một tập cạnh mà **xoá đi sẽ tách `s` khỏi `t`** [...] được gọi là một **lát cắt s–t**.*

Mọi luồng từ `s` tới `t` đều phải *đi qua* lát cắt, nên không luồng nào vượt được sức chứa của lát cắt *nhỏ nhất*. Điều đẹp là chặn trên đó **luôn đạt được**:

> [!quote] Skiena (tr. 269)
> "The maximum flow from s to t always equals the weight of the minimum s–t cut."
>
> *Luồng **lớn nhất** từ `s` tới `t` **luôn bằng** trọng số của **lát cắt s–t nhỏ nhất**.*

Định lý **max-flow min-cut** vừa cho *chứng chỉ tối ưu* (luồng = một lát cắt nào đó ⟹ cả hai đều tối ưu), vừa biến bài "tìm điểm nghẽn yếu nhất của mạng" (min-cut) thành bài luồng. Nhưng giá trị lớn nhất của luồng mạng là làm **đích đến của phép rút gọn** (Bài 11):

> [!quote] Skiena (tr. 267)
> "its primary importance lies in solving other important graph problems. A classic example is bipartite matching."
>
> *tầm quan trọng **chính yếu** của nó nằm ở việc **giải các bài toán đồ thị khác**. Một ví dụ kinh điển là **bipartite matching** (ghép cặp đồ thị hai phía).*

**Bipartite matching**: có hai nhóm (vd *việc* và *người*), cạnh `(j, p)` nghĩa "người `p` làm được việc `j`"; tìm cách ghép tối đa số cặp, mỗi người/việc thuộc tối đa một cặp. Rút gọn về luồng: thêm nguồn `s` nối mọi *việc* (sức chứa 1), đích `t` nối từ mọi *người* (sức chứa 1), mỗi cạnh "làm được" sức chứa 1 — **max-flow = số cặp ghép tối đa**. Phân công ca trực, gán request tới server, khớp người hiến–nhận tạng... đều là matching = luồng.

## 5. Demo: max-flow, min-cut, bipartite matching

Demo: **(1)** Edmonds–Karp tính max-flow trên mạng 6 đỉnh (kết quả kinh điển 23); **(2)** từ đồ thị thặng dư, trích **min-cut** và kiểm nó *bằng* max-flow (định lý); **(3)** rút gọn **bipartite matching** (3 việc ↔ 3 người) về max-flow.

```typescript
import { strict as assert } from "node:assert";

// ─── MAX-FLOW bằng Edmonds–Karp (Ford–Fulkerson + BFS tìm đường tăng luồng) ───
// Đồ thị dưới dạng ma trận SỨC CHỨA cap[u][v]. Luồng = tìm đường tăng tới khi hết.
function maxFlow(cap: number[][], s: number, t: number): { flow: number; residual: number[][] } {
  const n = cap.length;
  const res = cap.map((row) => row.slice());   // sức chứa còn lại (residual)
  let flow = 0;
  while (true) {
    // BFS tìm một đường tăng luồng từ s tới t trong đồ thị residual.
    const parent = new Array<number>(n).fill(-1);
    parent[s] = s;
    const queue = [s];
    let head = 0;
    while (head < queue.length) {
      const u = queue[head++];
      for (let v = 0; v < n; v++) {
        if (parent[v] === -1 && res[u][v] > 0) { parent[v] = u; queue.push(v); }
      }
    }
    if (parent[t] === -1) break;                // không còn đường tăng → tối ưu

    // Nút cổ chai (bottleneck) = sức chứa nhỏ nhất dọc đường.
    let bottleneck = Infinity;
    for (let v = t; v !== s; v = parent[v]) bottleneck = Math.min(bottleneck, res[parent[v]][v]);
    for (let v = t; v !== s; v = parent[v]) {   // đẩy luồng: trừ chiều thuận, cộng chiều nghịch
      res[parent[v]][v] -= bottleneck;
      res[v][parent[v]] += bottleneck;
    }
    flow += bottleneck;
  }
  return { flow, residual: res };
}

// Mạng ví dụ 6 đỉnh (s=0 ... t=5) — bài kinh điển, max-flow = 23.
const N = 6, S = 0, T = 5;
const cap: number[][] = Array.from({ length: N }, () => new Array(N).fill(0));
const edges: Array<[number, number, number]> = [
  [0, 1, 16], [0, 2, 13], [1, 3, 12], [2, 1, 4],
  [3, 2, 9], [2, 4, 14], [4, 3, 7], [3, 5, 20], [4, 5, 4],
];
for (const [u, v, c] of edges) cap[u][v] = c;

const mf = maxFlow(cap, S, T);
console.log(`MAX-FLOW từ s=${S} tới t=${T} (mạng 6 đỉnh):`);
console.log(`  luồng lớn nhất = ${mf.flow}`);
assert.equal(mf.flow, 23);

// ─── MIN-CUT: đỉnh nào s còn với tới trong residual = phía S; cạnh S→(không S) là lát cắt ───
const reachable = new Array<boolean>(N).fill(false);
{
  const q = [S]; reachable[S] = true; let h = 0;
  while (h < q.length) { const u = q[h++]; for (let v = 0; v < N; v++) if (!reachable[v] && mf.residual[u][v] > 0) { reachable[v] = true; q.push(v); } }
}
const cutEdges: Array<[number, number, number]> = [];
let cutCapacity = 0;
for (const [u, v, c] of edges)
  if (reachable[u] && !reachable[v]) { cutEdges.push([u, v, c]); cutCapacity += c; }
console.log(`  lát cắt nhỏ nhất (min-cut): ${cutEdges.map(([u, v, c]) => `${u}→${v}(${c})`).join(", ")}`);
console.log(`  tổng sức chứa lát cắt = ${cutCapacity}  → BẰNG max-flow (định lý max-flow min-cut)`);
assert.equal(cutCapacity, mf.flow);     // ĐỊNH LÝ: max-flow = min-cut

// ─── BIPARTITE MATCHING quy về MAX-FLOW: ghép việc ↔ người ───
// 3 việc (J1,J2,J3) ↔ 3 người (P1,P2,P3). Nguồn→việc→người→đích, mọi cạnh sức chứa 1.
// đỉnh: 0=nguồn, 1..3=việc, 4..6=người, 7=đích.
const BN = 8, BS = 0, BT = 7;
const bcap: number[][] = Array.from({ length: BN }, () => new Array(BN).fill(0));
for (let j = 1; j <= 3; j++) bcap[BS][j] = 1;        // nguồn → mỗi việc
for (let p = 4; p <= 6; p++) bcap[p][BT] = 1;        // mỗi người → đích
// ai làm được việc nào (việc j → người p):
const canDo: Array<[number, number]> = [[1, 4], [1, 5], [2, 5], [3, 5], [3, 6]];
for (const [j, p] of canDo) bcap[j][p] = 1;
const bm = maxFlow(bcap, BS, BT);
console.log(`\nBIPARTITE MATCHING (3 việc ↔ 3 người) quy về max-flow:`);
console.log(`  số cặp ghép tối đa = ${bm.flow}  (J1-P4, J2-P5, J3-P6)`);
assert.equal(bm.flow, 3);               // ghép được cả 3 việc

console.log("\nLuồng mạng: đồ thị = mạng ống, trọng số = sức chứa (Skiena tr.267). Max-flow = min-cut");
console.log("(tr.269). Nhiều bài (ghép cặp, kết nối) quy về luồng — đó là sức mạnh thật của nó.");
```

Kết quả chạy thật *(tất định)*:

```
MAX-FLOW từ s=0 tới t=5 (mạng 6 đỉnh):
  luồng lớn nhất = 23
  lát cắt nhỏ nhất (min-cut): 1→3(12), 4→3(7), 4→5(4)
  tổng sức chứa lát cắt = 23  → BẰNG max-flow (định lý max-flow min-cut)

BIPARTITE MATCHING (3 việc ↔ 3 người) quy về max-flow:
  số cặp ghép tối đa = 3  (J1-P4, J2-P5, J3-P6)

Luồng mạng: đồ thị = mạng ống, trọng số = sức chứa (Skiena tr.267). Max-flow = min-cut
(tr.269). Nhiều bài (ghép cặp, kết nối) quy về luồng — đó là sức mạnh thật của nó.
```

Ba điều đáng thấm. **(1) Đường tăng luồng hội tụ về tối ưu:** Edmonds–Karp cứ tìm đường còn chỗ, đẩy nút cổ chai, lặp — tới khi BFS không còn chạm `t` thì luồng `23` là *chắc chắn tối ưu* (nhờ cạnh nghịch cho rút lại quyết định, khác tham lam). **(2) Min-cut = chứng chỉ tối ưu:** từ residual, tập đỉnh `s` còn với tới là phía `S`; ba cạnh vượt ra — `1→3(12), 4→3(7), 4→5(4)` — cộng đúng `23 = max-flow`, phơi bày *đúng* những ống nghẽn giới hạn cả mạng. **(3) Matching là luồng trá hình:** bài ghép 3 việc–3 người, *không* viết thuật toán matching riêng — chỉ dựng mạng (nguồn→việc→người→đích, sức chứa 1) rồi gọi *đúng* hàm max-flow, ra `3` cặp; đó là sức mạnh của **rút gọn** (Bài 11).

> [!note] Tự thử
> 1. Giảm sức chứa cạnh `3→5` từ 20 xuống 5. Max-flow mới là bao nhiêu? Min-cut đổi sang tập cạnh nào?
> 2. Bỏ cạnh "làm được" `[3,6]` trong bipartite: giờ ghép tối đa mấy cặp? Việc/người nào bị lẻ?
> 3. Vì sao Ford–Fulkerson cần **cạnh nghịch** trong residual? Dựng ví dụ nhỏ mà không có cạnh nghịch thì kẹt ở luồng dưới tối ưu.
> 4. Min-cut tìm "điểm yếu nhất" của mạng. Nêu một ứng dụng vận hành: nếu mạng là hạ tầng, min-cut cho biết điều gì về độ bền? *(liên hệ sre)*

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
| 8 | Đồ thị trọng số: MST & đường ngắn nhất | Dijkstra / Prim / Kruskal | Skiena Ch8 |
| 9 | Quy hoạch động | tối ưu bằng bảng con | Skiena Ch10 |
| 10 | Tìm kiếm tổ hợp & backtracking | duyệt không gian lời giải | Skiena Ch9 |
| 11 | NP-đầy đủ & bài toán khó | khi không có lời giải nhanh | Skiena Ch11–12 |
| 12 | *(nâng cao)* Khớp chuỗi | KMP / Rabin–Karp | Skiena §6.7 + CLRS Ch32 |
| 13 | **Luồng mạng** *(nâng cao)* ← *đang ở đây* | max-flow / min-cut | Skiena §8.5 + CLRS Ch24 |
| 14 | *(nâng cao)* Thuật toán ngẫu nhiên | randomized quicksort, Monte Carlo | Skiena Ch6 |

Luồng mạng tiếp mạch đồ thị trọng số ([Bài 8](bai_08_do-thi-trong-so.md)) và dùng BFS ([Bài 7](bai_07_do-thi-duyet.md)); matching là ca mẫu của rút gọn ([Bài 11](bai_11_np-day-du.md)).

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 13.1 — Bài toán luồng mạng hỏi gì? Ẩn dụ nào giúp hiểu?
> **Đáp:** luồng lớn nhất gửi được từ `s` tới `t` khi tôn trọng sức chứa mỗi cạnh (Skiena tr. 267). Ẩn dụ: đồ thị = **mạng ống**, trọng số cạnh = **sức chứa ống**.

> [!question] Thẻ 13.2 — Hai ràng buộc của một luồng hợp lệ?
> **Đáp:** **sức chứa** (luồng qua cạnh ≤ sức chứa cạnh) và **bảo toàn** (mọi đỉnh trừ s,t: luồng vào = luồng ra).

> [!question] Thẻ 13.3 — Ford–Fulkerson hoạt động ra sao? Cạnh nghịch để làm gì?
> **Đáp:** lặp tìm **đường tăng luồng** (s→t còn chỗ) trên **đồ thị thặng dư**, đẩy **nút cổ chai**, tới khi hết đường. **Cạnh nghịch** cho phép *rút lại* luồng cũ → đảm bảo hội tụ tối ưu (không kẹt như tham lam). BFS tìm đường = Edmonds–Karp.

> [!question] Thẻ 13.4 — Định lý max-flow min-cut nói gì? Dùng để làm gì?
> **Đáp:** **luồng lớn nhất từ s tới t = trọng số lát cắt s–t nhỏ nhất** (Skiena tr. 269). Cho chứng chỉ tối ưu, và biến bài "tìm điểm nghẽn yếu nhất" thành bài luồng.

> [!question] Thẻ 13.5 — Bipartite matching quy về max-flow thế nào? Vì sao đáng làm?
> **Đáp:** thêm nguồn→nhóm-trái (sc 1), nhóm-phải→đích (sc 1), cạnh "ghép được" sc 1; **max-flow = số cặp tối đa**. Đáng làm vì tái dùng thuật toán luồng cho vô số bài (phân công, gán tài nguyên) — sức mạnh của **rút gọn** (Skiena tr. 267, Bài 11).

## 8. Câu hỏi tự kiểm tra

1. Giải thích ẩn dụ "mạng ống" và hai ràng buộc của luồng hợp lệ. *(mục 1, 2)*
2. Mô tả một vòng Ford–Fulkerson. Đồ thị thặng dư và cạnh nghịch đóng vai trò gì? *(mục 3)*
3. Phát biểu định lý max-flow min-cut. Làm sao từ luồng tối ưu trích được min-cut? *(mục 4)*
4. Rút gọn bipartite matching về luồng: dựng mạng ra sao, sức chứa bao nhiêu? *(mục 4)*
5. Chạy demo mục 5. Vì sao tổng sức chứa min-cut đúng bằng max-flow 23? *(mục 4 & 5)*

## Tóm tắt một trang

```
BÀI 13 — LUỒNG MẠNG (nâng cao)
─────────────────────────────────────────────────────────
LUỒNG MẠNG  đồ thị = mạng ỐNG, trọng số = SỨC CHỨA (Skiena tr.267). Hỏi: luồng
   lớn nhất từ s tới t, tôn trọng sức chứa mỗi ống. Luồng hợp lệ: (1) ≤ sức
   chứa; (2) BẢO TOÀN (vào = ra tại mọi đỉnh ≠ s,t).

FORD–FULKERSON  lặp: tìm ĐƯỜNG TĂNG LUỒNG (s→t còn chỗ) trên ĐỒ THỊ THẶNG DƯ,
   đẩy NÚT CỔ CHAI, tới khi hết đường. CẠNH NGHỊCH cho rút lại luồng → hội tụ
   tối ưu. BFS tìm đường = EDMONDS–KARP (đa thức).

MAX-FLOW = MIN-CUT  luồng lớn nhất = trọng số lát cắt s–t nhỏ nhất (Skiena
   tr.269). Lát cắt s–t = tập cạnh xoá đi thì tách s khỏi t. Cho chứng chỉ
   tối ưu + tìm điểm nghẽn yếu nhất.

QUY VỀ LUỒNG (sức mạnh thật)  BIPARTITE MATCHING: nguồn→trái(sc1), phải→đích
   (sc1), cạnh ghép-được(sc1) → max-flow = số cặp tối đa (Skiena tr.267). Phân
   công, gán tài nguyên... đều là matching = luồng (rút gọn, Bài 11).

DEMO  mạng 6 đỉnh: max-flow = 23 = min-cut {1→3(12),4→3(7),4→5(4)}. Bipartite
   3 việc–3 người → 3 cặp, chỉ gọi lại hàm max-flow.
```

## Nguồn

- **Skiena, Steven S. — *The Algorithm Design Manual*, 3rd ed.** (Springer, 2020) — **§8.5 Network Flows and Bipartite Matching** (trong Chapter 8: Weighted Graph Algorithms): ẩn dụ mạng ống, bài toán luồng, đường tăng luồng & residual, định lý max-flow min-cut, rút gọn bipartite matching về luồng. `tai_lieu/The Algorithm Design Manual 3rd Edition...pdf` (offset **PDF = tr. + 14** ở Ch8).
- **Cormen, Leiserson, Rivest, Stein — *Introduction to Algorithms*, 4th ed. (CLRS), Chapter 24: Maximum Flow** — nguồn tra cứu chuẩn (Ford–Fulkerson, Edmonds–Karp, max-flow min-cut). *(Bản PDF trong `tai_lieu/` lỗi phông khi trích text nên không trích nguyên văn.)*
- Liên hệ: [Bài 8 — đồ thị trọng số](bai_08_do-thi-trong-so.md) (nền); [Bài 7 — BFS](bai_07_do-thi-duyet.md) (tìm đường tăng); [Bài 11 — rút gọn](bai_11_np-day-du.md) (matching = luồng).

---

**Bản đồ khoá học:** [Bài 0 — Thuật toán & tính đúng](bai_00_thuat-toan-la-gi.md) · [Bài 1 — Phân tích Big-O](bai_01_big-o.md) · [Bài 2 — CTDL tuyến tính](bai_02_ctdl-tuyen-tinh.md) · [Bài 3 — Từ điển & bảng băm](bai_03_bang-bam.md) · [Bài 4 — Heap & cây tìm kiếm](bai_04_heap-cay-tim-kiem.md) · [Bài 5 — Sắp xếp](bai_05_sap-xep.md) · [Bài 6 — Chia để trị & đệ quy](bai_06_chia-de-tri.md) · [Bài 7 — Đồ thị: duyệt](bai_07_do-thi-duyet.md) · [Bài 8 — Đồ thị trọng số](bai_08_do-thi-trong-so.md) · [Bài 9 — Quy hoạch động](bai_09_quy-hoach-dong.md) · [Bài 10 — Backtracking](bai_10_backtracking.md) · [Bài 11 — NP-đầy đủ](bai_11_np-day-du.md) · [Bài 12 — Khớp chuỗi](bai_12_khop-chuoi.md) · **[Bài 13 — Luồng mạng] ← bạn đang ở đây** · [Bài 14 — Thuật toán ngẫu nhiên](bai_14_ngau-nhien.md)

Xem thêm [README khoá học](../README.md).
