# Bài 10 — Tìm kiếm tổ hợp và backtracking: duyệt không gian lời giải

> [!info] Về bài này
> Có lớp bài toán không né được việc **thử nhiều khả năng** — xếp lịch, giải Sudoku, tìm mọi đường đi, đặt quân cờ. **Backtracking** là khuôn dựng *có hệ thống* mọi lời giải: xây dần từng phần, và **quay lui** khi bí. Bản thân nó vẫn là vét cạn (mũ), nhưng **pruning** — cắt sớm những nhánh không thể dẫn tới lời giải — biến nhiều bài "bất khả thi" thành giải được trong thực tế. Đây cũng là cửa ngõ sang Bài 11 (NP-đầy đủ): khi không gian lời giải *bắt buộc* mũ.
> Nguồn (Luật số 1): **Skiena** *The Algorithm Design Manual 3e* — **Chapter 9: Combinatorial Search** (§9.1 Backtracking, §9.3 Search Pruning) (`tai_lieu/`, trích `> [!quote] Skiena (tr. N)`, **PDF = tr. + 14** ở Ch9).
> **Chạy demo:** `node bai_10.ts` — Node 22+, không cài gói. Code tất định.
> Cần đọc trước: [Bài 7 — DFS](bai_07_do-thi-duyet.md) (backtracking là DFS trên cây lời giải), [Bài 9 — QHĐ](bai_09_quy-hoach-dong.md).

## Mục lục

1. [Tình huống: khi phải thử mọi khả năng](#1-tình-huống-khi-phải-thử-mọi-khả-năng)
2. [Backtracking: cây các lời giải bộ phận](#2-backtracking-cây-các-lời-giải-bộ-phận)
3. [Pruning: cắt nhánh chết sớm](#3-pruning-cắt-nhánh-chết-sớm)
4. [N-Queens: backtracking và pruning trong thực tế](#4-n-queens-backtracking-và-pruning-trong-thực-tế)
5. [Demo: tập con và N-Queens](#5-demo-tập-con-và-n-queens)
6. [Bản đồ khoá DSA](#6-bản-đồ-khoá-dsa)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Tình huống: khi phải thử mọi khả năng

> [!example] Không có công thức, chỉ còn thử
> Xếp 8 quân hậu lên bàn cờ sao cho không quân nào ăn nhau. Không có công thức đóng; phải *thử* các cách đặt. Nhưng "thử hết" nhanh chóng khổng lồ: bàn 8×8 có `C(64,8) ≈ 4,4 tỷ` cách đặt 8 quân. Cần cách duyệt *có hệ thống* (không sót, không lặp) và *khôn* (bỏ sớm cách vô vọng).

Vét cạn nghe đáng sợ, nhưng Skiena nhắc ta một triệu là con số nhỏ đến bất ngờ — và đó là lý do phải *cắt tỉa*:

> [!quote] Skiena (tr. 281)
> "One million permutations means all arrangements of roughly 10 objects, but not more. One million subsets means all combinations of roughly 20 items, but not more."
>
> *Một triệu **hoán vị** là mọi cách sắp của khoảng **10 vật**, không hơn. Một triệu **tập con** là mọi tổ hợp của khoảng **20 món**, không hơn.*

> [!quote] Skiena (tr. 281)
> "Solving significantly larger problems requires carefully pruning the search space to ensure we look at only the elements that really matter."
>
> *Giải những bài lớn hơn hẳn đòi **cắt tỉa cẩn thận không gian tìm kiếm** để ta chỉ nhìn vào **những phần thực sự quan trọng**.*

## 2. Backtracking: cây các lời giải bộ phận

**Backtracking** xây lời giải như một **vector** `a = (a₁, a₂, ..., aₙ)`, mỗi `aᵢ` chọn từ một tập hữu hạn. Ở mỗi bước, *thử nối thêm* một phần tử vào lời giải bộ phận; nếu đủ thì ghi nhận, nếu chưa thì đệ quy đi tiếp; khi hết lựa chọn thì **quay lui** (undo) để thử nhánh khác.

> [!quote] Skiena (tr. 282)
> "Backtracking constructs a tree of partial solutions, where each node represents a partial solution."
>
> *Backtracking dựng một **cây các lời giải bộ phận**, mỗi nút là một **lời giải bộ phận**.*

Nhìn kỹ, đây chính là **DFS** (Bài 7) trên một *cây lời giải ngầm* — không có sẵn trong bộ nhớ mà sinh ra khi đi:

```
Liệt kê tập con {1,2,3} — cây nhị phân "lấy / không lấy" mỗi phần tử:

                        ( )
             không 1 ╱       ╲ lấy 1
                  ( )           (1)
          kh2 ╱     ╲l2    kh2 ╱   ╲ l2
            ()       (2)    (1)     (1,2)
          ╱   ╲     ╱  ╲   ╱  ╲     ╱   ╲
         {} {3} {2}{2,3}{1}{1,3}{1,2}{1,2,3}   ← 2^3 = 8 lá = 8 tập con
```

Khuôn backtracking tổng quát (tựa Skiena §9.1):

```
backtrack(a, k):
    nếu a là lời giải hoàn chỉnh → xử lý (in/đếm)
    ngược lại:
        với mỗi ứng viên hợp lệ c cho vị trí k+1:
            a[k+1] = c
            backtrack(a, k+1)      ← đi sâu
            (gỡ a[k+1])            ← QUAY LUI, thử ứng viên khác
```

Dùng DFS (không BFS) vì bộ nhớ chỉ cần giữ *đường đi hiện tại* — tỉ lệ với **chiều sâu** cây, không phải bề rộng (có thể mũ).

## 3. Pruning: cắt nhánh chết sớm

Backtracking trần vẫn duyệt cả cây mũ. Vũ khí làm nó *thực sự dùng được* là **pruning** — không đi vào nhánh mà ta đã biết chắc là ngõ cụt:

> [!quote] Skiena (tr. 290)
> "Pruning is the technique of abandoning a search direction the instant we can establish that a given partial solution cannot be extended into a full solution."
>
> *Pruning là kỹ thuật **từ bỏ một hướng tìm kiếm ngay khoảnh khắc** ta xác định được rằng một lời giải bộ phận **không thể mở rộng thành lời giải đầy đủ**.*

Mấu chốt: kiểm *tại mỗi nút*, nếu phần đã xây đã vi phạm ràng buộc (hoặc chắc chắn dưới tối ưu), **chặt luôn cả cây con** bên dưới — tiết kiệm bằng mũ số nút khỏi duyệt. Đặt một quân hậu bị chiếu? Bỏ ngay, không thử đặt các hàng sau. Đó là lý do N-Queens cho `n=8` chỉ duyệt vài nghìn nút thay vì hàng tỷ.

> [!quote] Skiena (tr. 290)
> "Combinatorial search, when augmented with tree-pruning techniques, can be used to find the optimal solution for small optimization problems."
>
> *Tìm kiếm tổ hợp, khi được **tăng cường bằng kỹ thuật cắt cây**, có thể dùng để tìm **lời giải tối ưu** cho các bài tối ưu **cỡ nhỏ**.*

> [!note] Backtracking so với QHĐ (Bài 9)
> Cả hai duyệt "mọi khả năng", nhưng khác bản chất bài toán. **QHĐ** dùng khi bài con *chồng lấn* và có *cấu trúc con tối ưu* → nhớ lại để tránh mũ. **Backtracking** dùng khi không gian lời giải *không* gộp lại được (mỗi lời giải là một cấu hình riêng, như cách xếp hậu) → chỉ còn cách duyệt, và pruning là thứ duy nhất cứu. Khi *ngay cả* pruning cũng không đủ (bài NP-khó cỡ lớn), ta chuyển sang heuristic/xấp xỉ — [Bài 11](bai_11_np-day-du.md).

## 4. N-Queens: backtracking và pruning trong thực tế

**N-Queens**: đặt `n` quân hậu lên bàn `n×n` sao cho không hai quân nào cùng hàng, cùng cột, hoặc cùng đường chéo. Khuôn backtracking: đặt **mỗi hàng một quân**, thử từng cột; trước khi đệ quy xuống hàng sau, *kiểm an toàn* (pruning) — nếu cột `c` bị một quân đã đặt chiếu (cùng cột hay cùng chéo) thì bỏ qua `c` luôn.

```
Pruning ở N-Queens (n=4): đặt theo hàng, hàm "safe" chặt nhánh bị chiếu
  hàng 0: thử cột 0 →  hàng 1: cột 0 KO(cùng cột) cột 1 KO(chéo) cột 2 OK → ...
                                                              ↑ nhánh cột 0,1 bị CHẶT
  → chỉ 17 nút được duyệt cho n=4 thay vì 4^4 = 256
```

Số nút duyệt với pruning nhỏ hơn vét cạn thô theo cấp số mũ — demo mục 5 đếm chính xác: `n=8` chỉ `2057` nút so với `n^n = 16.777.216`. Đó là *"the power of search pruning"*.

## 5. Demo: tập con và N-Queens

Demo hai phần. **(1)** backtracking liệt kê mọi tập con của `{1,2,3}` — thấy cây "lấy/không lấy" sinh đúng `2ⁿ` lá. **(2)** N-Queens: đếm số lời giải *và* số nút cây đã duyệt cho `n=4..8`, so với `nⁿ` để thấy pruning cắt khủng khiếp.

```typescript
import { strict as assert } from "node:assert";

// ─── BACKTRACKING cơ bản: liệt kê MỌI tập con của {1..n} (2^n tập) ───
// Mỗi phần tử: CHỌN hoặc KHÔNG → cây nhị phân các lời giải bộ phận.
function subsets(n: number): number[][] {
  const result: number[][] = [];
  const current: number[] = [];
  function backtrack(i: number): void {
    if (i > n) { result.push([...current]); return; }  // lời giải hoàn chỉnh
    backtrack(i + 1);                 // nhánh: KHÔNG lấy i
    current.push(i);
    backtrack(i + 1);                 // nhánh: LẤY i
    current.pop();                    // quay lui (undo) — cốt lõi backtracking
  }
  backtrack(1);
  return result;
}

const subs = subsets(3);
console.log("BACKTRACKING — liệt kê mọi tập con của {1,2,3}:");
console.log(`  số tập con = ${subs.length} (= 2^3)`);
console.log(`  ${subs.map((s) => `{${s.join(",")}}`).join("  ")}`);
assert.equal(subs.length, 8);
assert.equal(subsets(10).length, 1024);   // 2^10

// ─── N-QUEENS: đặt n hậu trên bàn n×n sao cho không hậu nào ăn nhau ───
// Backtracking + PRUNING: bỏ ngay nhánh vừa đặt một hậu bị chiếu.
function nQueens(n: number): { solutions: number; nodes: number } {
  let solutions = 0, nodes = 0;
  const col = new Array<number>(n);        // col[r] = cột đặt hậu ở hàng r
  function safe(r: number, c: number): boolean {
    for (let i = 0; i < r; i++) {
      if (col[i] === c) return false;                      // cùng cột
      if (Math.abs(col[i] - c) === Math.abs(i - r)) return false; // cùng đường chéo
    }
    return true;
  }
  function place(r: number): void {
    nodes++;                               // mỗi lần vào = một nút cây tìm kiếm
    if (r === n) { solutions++; return; }  // đặt xong n hàng → một lời giải
    for (let c = 0; c < n; c++) {
      if (safe(r, c)) {                    // PRUNING: chỉ đi tiếp nếu c an toàn
        col[r] = c;
        place(r + 1);
      }
    }
  }
  place(0);
  return { solutions, nodes };
}

console.log("\nN-QUEENS — số cách đặt n hậu không ăn nhau, và số nút cây đã duyệt:");
console.log("  n   số lời giải   nút đã duyệt   n^n (vét cạn thô)");
for (const n of [4, 5, 6, 7, 8]) {
  const r = nQueens(n);
  console.log(`  ${n}   ${String(r.solutions).padStart(9)}   ${String(r.nodes).padStart(10)}   ${String(n ** n).padStart(12)}`);
}
assert.equal(nQueens(4).solutions, 2);
assert.equal(nQueens(8).solutions, 92);    // kết quả kinh điển
// Pruning cắt khủng khiếp: nút duyệt « n^n (và « n! hoán vị).
assert.ok(nQueens(8).nodes < 8 ** 8 / 100);

console.log("\nBacktracking = dựng cây lời giải bộ phận + PRUNING: bỏ nhánh ngay khi biết");
console.log("không dẫn tới lời giải đầy đủ (Skiena tr.290). Nhờ đó giải được bài vét cạn nhỏ.");
```

Kết quả chạy thật *(tất định)*:

```
BACKTRACKING — liệt kê mọi tập con của {1,2,3}:
  số tập con = 8 (= 2^3)
  {}  {3}  {2}  {2,3}  {1}  {1,3}  {1,2}  {1,2,3}

N-QUEENS — số cách đặt n hậu không ăn nhau, và số nút cây đã duyệt:
  n   số lời giải   nút đã duyệt   n^n (vét cạn thô)
  4           2           17            256
  5          10           54           3125
  6           4          153          46656
  7          40          552         823543
  8          92         2057       16777216

Backtracking = dựng cây lời giải bộ phận + PRUNING: bỏ nhánh ngay khi biết
không dẫn tới lời giải đầy đủ (Skiena tr.290). Nhờ đó giải được bài vét cạn nhỏ.
```

Ba điều đáng thấm. **(1) Backtracking = DFS trên cây sinh-khi-đi:** liệt kê tập con là cây nhị phân "lấy/không lấy", 3 phần tử cho đúng `2³ = 8` lá; `current.pop()` chính là bước **quay lui** đưa trạng thái về để thử nhánh kia. **(2) Pruning cắt theo cấp mũ:** N-Queens `n=8` chỉ duyệt `2057` nút trong khi vét cạn thô `nⁿ = 16,7 triệu` — nhỏ hơn ~8000 lần, vì mỗi lần đặt hậu bị chiếu là chặt luôn cả cây con bên dưới. **(3) Vẫn là mũ, chỉ hoãn được:** số nút `17 → 54 → 153 → 552 → 2057` vẫn tăng nhanh theo `n`; pruning dời được giới hạn khả thi lên (giải tới `n` vài chục), nhưng *không* đổi bản chất mũ — đó đúng là ranh giới dẫn tới Bài 11.

> [!note] Tự thử
> 1. In *một* lời giải N-Queens cho `n=8` dưới dạng bàn cờ (dấu `Q` và `.`), không chỉ đếm.
> 2. Thêm pruning mạnh hơn: dùng ba mảng Boolean đánh dấu cột/chéo-chính/chéo-phụ đã bị chiếm để `safe` chạy `O(1)` thay vì `O(r)`. Số *nút* duyệt có đổi không? Còn *thời gian*?
> 3. Giải Sudoku bằng backtracking: ô trống là "vị trí", ứng viên là 1–9 hợp lệ. Pruning nào làm nó nhanh? (Skiena §9.4.)
> 4. Vì sao backtracking dùng DFS (ngăn xếp/đệ quy) chứ không BFS (hàng đợi)? Liên hệ bộ nhớ chiều sâu vs bề rộng (Bài 7).

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
| 10 | **Tìm kiếm tổ hợp & backtracking** ← *đang ở đây* | duyệt không gian lời giải | Skiena Ch9 |
| 11 | NP-đầy đủ & bài toán khó | khi không có lời giải nhanh | Skiena Ch11–12 |
| 12 | *(nâng cao)* Khớp chuỗi | KMP / Rabin–Karp | Skiena §6.7 + CLRS Ch32 |
| 13 | *(nâng cao)* Luồng mạng | max-flow / min-cut | Skiena §8.5 + CLRS Ch24 |
| 14 | *(nâng cao)* Thuật toán ngẫu nhiên | randomized quicksort, Monte Carlo | Skiena Ch6 |

Backtracking là DFS ([Bài 7](bai_07_do-thi-duyet.md)) trên cây lời giải; khi không gian *bắt buộc* mũ, [Bài 11](bai_11_np-day-du.md) giải thích vì sao và làm gì.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 10.1 — Backtracking làm gì? Nó xây lời giải ra sao?
> **Đáp:** liệt kê có hệ thống mọi lời giải, xây dần như vector `a = (a₁...aₙ)`: thử nối thêm phần tử, đệ quy đi sâu, **quay lui (undo)** khi hết ứng viên. Dựng một **cây lời giải bộ phận** (Skiena tr. 282).

> [!question] Thẻ 10.2 — Backtracking liên hệ với DFS thế nào? Vì sao dùng DFS chứ không BFS?
> **Đáp:** là **DFS** trên cây lời giải *sinh khi đi* (không có sẵn). Dùng DFS vì bộ nhớ chỉ cần giữ đường đi hiện tại (chiều sâu), còn bề rộng cây có thể mũ.

> [!question] Thẻ 10.3 — Pruning là gì? Vì sao nó quan trọng đến vậy?
> **Đáp:** **từ bỏ một hướng ngay khi** biết chắc lời giải bộ phận không thể thành lời giải đầy đủ (Skiena tr. 290). Chặt cả cây con bên dưới → tiết kiệm mũ số nút; là thứ biến vét cạn thành khả thi.

> [!question] Thẻ 10.4 — Backtracking khác quy hoạch động (Bài 9) ở đâu?
> **Đáp:** QHĐ dùng khi bài con **chồng lấn** + có cấu trúc con tối ưu → nhớ lại. Backtracking dùng khi lời giải **không gộp được** (mỗi cấu hình riêng) → chỉ còn duyệt, pruning là cứu cánh.

> [!question] Thẻ 10.5 — Pruning có đổi được bản chất mũ của bài toán không?
> **Đáp:** **không** — chỉ dời giới hạn khả thi lên (giải được cỡ lớn hơn), số nút vẫn tăng mũ theo `n`. Khi cả pruning không đủ → heuristic/xấp xỉ (Bài 11).

## 8. Câu hỏi tự kiểm tra

1. Viết khuôn backtracking tổng quát và chỉ rõ đâu là bước "quay lui". *(mục 2)*
2. Vì sao backtracking là DFS? Nó tiết kiệm bộ nhớ so với BFS thế nào? *(mục 2)*
3. Pruning là gì? Cho ví dụ pruning trong N-Queens và trong knapsack/TSP. *(mục 3)*
4. Backtracking và QHĐ đều "duyệt mọi khả năng" — khi nào chọn cái nào? *(mục 3)*
5. Chạy demo mục 5. Vì sao `n=8` chỉ duyệt 2057 nút trong khi `n^n` là 16,7 triệu? *(mục 3 & 4)*

## Tóm tắt một trang

```
BÀI 10 — TÌM KIẾM TỔ HỢP & BACKTRACKING
─────────────────────────────────────────────────────────
KHI NÀO  bài phải THỬ nhiều cấu hình (xếp lịch, Sudoku, N-Queens, mọi đường).
   1 triệu = hoán vị ~10 vật / tập con ~20 món (Skiena tr.281) → phải cắt tỉa.

BACKTRACKING  xây lời giải như vector a=(a1..an): thử nối phần tử → đệ quy →
   QUAY LUI (undo) khi hết ứng viên. Dựng CÂY lời giải bộ phận (Skiena tr.282).
   = DFS (Bài 7) trên cây sinh-khi-đi. DFS vì bộ nhớ ~ chiều sâu, ko bề rộng.

PRUNING  từ bỏ một hướng NGAY khi biết lời giải bộ phận ko thể thành đầy đủ
   (Skiena tr.290). Chặt cả cây con → tiết kiệm MŨ số nút. Biến vét cạn thành
   khả thi cho bài cỡ NHỎ (tr.290).

vs QHĐ (Bài 9)  QHĐ: bài con CHỒNG LẤN + cấu trúc con tối ưu → nhớ lại.
   Backtracking: lời giải KHÔNG gộp được → duyệt + prune.

GIỚI HẠN  pruning KHÔNG đổi bản chất mũ, chỉ dời giới hạn khả thi lên → Bài 11.

DEMO  tập con {1,2,3} = 2^3=8 lá (quay lui = pop). N-Queens n=8: 92 lời giải,
   chỉ 2057 nút duyệt vs n^n=16,7 triệu (pruning cắt ~8000 lần).
```

## Nguồn

- **Skiena, Steven S. — *The Algorithm Design Manual*, 3rd ed.** (Springer, 2020) — **Chapter 9: Combinatorial Search** (§9.1 Backtracking, §9.2 Examples, §9.3 Search Pruning): vét cạn & cỡ "một triệu", khuôn backtracking, cây lời giải bộ phận, pruning cắt nhánh chết. `tai_lieu/The Algorithm Design Manual 3rd Edition...pdf` (offset **PDF = tr. + 14** ở Ch9).
- Liên hệ: [Bài 7 — DFS](bai_07_do-thi-duyet.md) (backtracking là DFS trên cây lời giải); [Bài 9 — QHĐ](bai_09_quy-hoach-dong.md) (khi bài con gộp được); [Bài 11 — NP-đầy đủ](bai_11_np-day-du.md) (khi không gian bắt buộc mũ).

---

**Bản đồ khoá học:** [Bài 0 — Thuật toán & tính đúng](bai_00_thuat-toan-la-gi.md) · [Bài 1 — Phân tích Big-O](bai_01_big-o.md) · [Bài 2 — CTDL tuyến tính](bai_02_ctdl-tuyen-tinh.md) · [Bài 3 — Từ điển & bảng băm](bai_03_bang-bam.md) · [Bài 4 — Heap & cây tìm kiếm](bai_04_heap-cay-tim-kiem.md) · [Bài 5 — Sắp xếp](bai_05_sap-xep.md) · [Bài 6 — Chia để trị & đệ quy](bai_06_chia-de-tri.md) · [Bài 7 — Đồ thị: duyệt](bai_07_do-thi-duyet.md) · [Bài 8 — Đồ thị trọng số](bai_08_do-thi-trong-so.md) · [Bài 9 — Quy hoạch động](bai_09_quy-hoach-dong.md) · **[Bài 10 — Backtracking] ← bạn đang ở đây** · [Bài 11 — NP-đầy đủ](bai_11_np-day-du.md) · [Bài 12 — Khớp chuỗi](bai_12_khop-chuoi.md) · [Bài 13 — Luồng mạng](bai_13_luong-mang.md) · [Bài 14 — Thuật toán ngẫu nhiên](bai_14_ngau-nhien.md)

Xem thêm [README khoá học](../README.md).
