# Bài 9 — Quy hoạch động: đệ quy có nhớ, giải bài toán tối ưu

> [!info] Về bài này
> Bài 6 (chia để trị) bẻ bài toán thành các mảnh **độc lập**. Nhưng nhiều bài toán bẻ ra thì các mảnh **chồng lấn** — cùng một bài con bị tính đi tính lại hàng triệu lần, làm đệ quy ngây thơ chậm theo cấp số mũ. **Quy hoạch động (QHĐ)** là cách chữa: *đệ quy + nhớ lại kết quả*. Bài này đi từ ví dụ kinh điển (Fibonacci) tới hai bài toán tối ưu mẫu — **edit distance** (khoảng cách sửa chuỗi, nền của gợi ý chính tả & tin sinh học) và **knapsack** (cái túi) — cùng điều kiện để một bài toán *dùng được* QHĐ.
> Nguồn (Luật số 1): **Skiena** *The Algorithm Design Manual 3e* — **Chapter 10: Dynamic Programming** (§10.1 Caching vs. Computation, §10.2 Approximate String Matching) (`tai_lieu/`, trích `> [!quote] Skiena (tr. N)`, **PDF = tr. + 14** ở Ch10).
> **Chạy demo:** `node bai_09.ts` — Node 22+, không cài gói. Code tất định.
> Cần đọc trước: [Bài 6 — Chia để trị](bai_06_chia-de-tri.md) (QHĐ là anh em của nó), [Bài 1 — Big-O](bai_01_big-o.md).

## Mục lục

1. [Tình huống: Fibonacci đệ quy chậm đến khó tin](#1-tình-huống-fibonacci-đệ-quy-chậm-đến-khó-tin)
2. [Quy hoạch động: đệ quy có nhớ](#2-quy-hoạch-động-đệ-quy-có-nhớ)
3. [Edit distance: bài toán DP kinh điển](#3-edit-distance-bài-toán-dp-kinh-điển)
4. [Knapsack và khi nào dùng được DP](#4-knapsack-và-khi-nào-dùng-được-dp)
5. [Demo: Fibonacci, edit distance, knapsack](#5-demo-fibonacci-edit-distance-knapsack)
6. [Bản đồ khoá DSA](#6-bản-đồ-khoá-dsa)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Tình huống: Fibonacci đệ quy chậm đến khó tin

> [!example] Một dòng đệ quy, một thảm hoạ hiệu năng
> `fib(n) = fib(n-1) + fib(n-2)` — định nghĩa đẹp, dịch thẳng thành đệ quy. Nhưng `fib(50)` chạy *hàng phút*. Vì sao? Vẽ cây gọi: để tính `fib(5)` ta cần `fib(4)` và `fib(3)`; nhưng `fib(4)` *lại* cần `fib(3)`... `fib(3)` bị tính hai lần, `fib(2)` nhiều lần hơn nữa. Số lần gọi phình theo **cấp số mũ** `~φⁿ` — dù chỉ có `n` giá trị Fibonacci khác nhau.

Đây là dấu hiệu kinh điển của bài toán có **bài con chồng lấn** *(overlapping subproblems)*: đệ quy tính đi tính lại cùng một thứ. Giải pháp hiện ra ngay khi ta nhận ra điều đó.

> [!quote] Skiena (tr. 307)
> "Dynamic programming is a technique for efficiently implementing a recursive algorithm by storing partial results. It requires seeing that a naive recursive algorithm computes the same subproblems over and over and over again."
>
> *Quy hoạch động là kỹ thuật cài đặt **hiệu quả** một thuật toán đệ quy bằng cách **lưu các kết quả bộ phận**. Nó đòi ta **nhận ra** rằng một thuật toán đệ quy ngây thơ tính **cùng những bài con lặp đi lặp lại**.*

## 2. Quy hoạch động: đệ quy có nhớ

QHĐ đứng giữa hai thái cực. **Tham lam** (Bài 8) quyết nhanh tại chỗ nhưng thường không tối ưu; **vét cạn** thử mọi khả năng nên luôn tối ưu nhưng quá đắt. QHĐ lấy cái hay của cả hai:

> [!quote] Skiena (tr. 307)
> "Dynamic programming combines the best of both worlds. It gives us a way to design custom algorithms that systematically search all possibilities (thus guaranteeing correctness) while storing intermediate results to avoid recomputing (thus providing efficiency)."
>
> *Quy hoạch động **kết hợp cái hay của cả hai thế giới**. Nó cho ta cách thiết kế thuật toán **duyệt có hệ thống mọi khả năng** (nên bảo đảm **đúng**) trong khi **lưu kết quả trung gian để khỏi tính lại** (nên bảo đảm **hiệu quả**).*

Hai cách cài QHĐ, cùng ý tưởng:

- **Top-down (memoization):** giữ nguyên đệ quy, nhưng trước khi tính thì tra một *bảng nhớ (cache)*; đã tính rồi thì trả lại ngay. Một dòng thêm vào biến Fibonacci mũ thành tuyến tính.
- **Bottom-up (lập bảng):** điền một *bảng* từ bài con nhỏ nhất lên, mỗi ô dùng các ô đã điền. Không đệ quy, dễ phân tích chi phí.

```
fib(5) ĐỆ QUY NGÂY THƠ (bài con chồng lấn)      CÓ NHỚ (mỗi bài con 1 lần)
            5                                      5 ← 4 ← 3 ← 2 ← 1
          /   \                                    cache: [0,1,1,2,3,5]
         4     3    ← fib(3) tính LẠI              mỗi giá trị tính ĐÚNG MỘT LẦN
        / \   / \                                  → O(n) thay vì O(φ^n)
       3  2  2  1
      ...bùng nổ mũ...
```

Mấu chốt: lời giải vẫn *đúng như* vét cạn (xét mọi khả năng), nhưng mỗi bài con chỉ tính một lần. Chi phí tụt từ mũ xuống đa thức — thường là `O(số bài con × công mỗi bài)`.

## 3. Edit distance: bài toán DP kinh điển

**Edit distance** *(khoảng cách sửa / Levenshtein)*: số thao tác ít nhất để biến chuỗi `a` thành chuỗi `b`, với ba phép — **thay** *(substitute)*, **chèn** *(insert)*, **xoá** *(delete)* một ký tự. Đây là nền của gợi ý chính tả, `diff`, và so khớp DNA.

Chìa khoá QHĐ là nhìn ra cấu trúc đệ quy ở *ký tự cuối*:

> [!quote] Skiena (tr. 315)
> "We can define a recursive algorithm using the observation that the last character in the string must either be matched, substituted, inserted, or deleted."
>
> *Ta có thể định nghĩa một thuật toán đệ quy dựa trên nhận xét rằng **ký tự cuối** của chuỗi phải **hoặc khớp, hoặc bị thay, hoặc bị chèn, hoặc bị xoá**.*

Gọi `D[i][j]` = số thao tác ít nhất biến `a[0..i)` thành `b[0..j)`. Mỗi ô là **min của ba lựa chọn** — đúng ba phép trên:

```
D[i][j] = min(
    D[i-1][j-1] + (a[i-1]==b[j-1] ? 0 : 1),   ← khớp (0) hoặc thay (1)
    D[i-1][j]   + 1,                           ← xoá a[i-1]
    D[i][j-1]   + 1,                           ← chèn b[j-1]
)
Biên: D[i][0] = i (xoá i ký tự),  D[0][j] = j (chèn j ký tự)
```

Có `(m+1)(n+1)` bài con, mỗi ô tính trong `O(1)` → **`O(mn)`** thay vì `3^n` của đệ quy ngây thơ. Demo mục 5 in cả bảng cho `"kitten" → "sitting"`.

## 4. Knapsack và khi nào dùng được DP

**Knapsack 0/1** *(cái túi)*: cho `n` món, mỗi món có *trọng lượng* và *giá trị*; chọn tập món (mỗi món 0 hoặc 1 lần) để *tối đa tổng giá trị* mà không vượt sức chứa `W`. Bài tối ưu kinh điển: phân bổ ngân sách, cắt vật liệu, chọn task.

Cấu trúc QHĐ: `K[i][w]` = giá trị lớn nhất dùng `i` món đầu với sức chứa `w`. Mỗi món có *hai* lựa chọn — lấy hoặc không:

```
K[i][w] = max(
    K[i-1][w],                              ← KHÔNG lấy món i
    K[i-1][w - weight[i]] + value[i]        ← LẤY món i (nếu weight[i] ≤ w)
)
```

Không phải bài nào cũng xài được QHĐ. Cần hai tính chất:

1. **Bài con chồng lấn** *(overlapping subproblems)* — cùng bài con xuất hiện lại (nếu không thì chia-để-trị, Bài 6, là đủ; lưu lại chẳng lợi gì).
2. **Cấu trúc con tối ưu** *(optimal substructure)* — lời giải tối ưu của bài lớn **ghép từ** lời giải tối ưu của bài con. Fibonacci, edit distance, knapsack, Dijkstra đều có; nhưng có bài *không* (demo giới hạn QHĐ: TSP cần trạng thái mũ — Skiena §10.9), nối sang [Bài 11](bai_11_np-day-du.md).

> [!note] QHĐ, chia để trị, và tham lam — ba anh em
> Cả ba đều "bẻ nhỏ bài toán", khác nhau ở *quan hệ giữa các mảnh* và *cách chọn*: **chia để trị** (Bài 6) — mảnh **độc lập**, gộp thẳng; **tham lam** (Bài 8) — chọn tốt nhất tại chỗ, *không* nhìn lại, nhanh nhưng chỉ tối ưu ở vài bài đặc biệt (MST); **QHĐ** — mảnh **chồng lấn**, xét *mọi* lựa chọn ở mỗi bước nhưng nhớ lại để khỏi tính lại, tối ưu cho lớp bài rộng hơn tham lam. Skiena gọi QHĐ là *"the easiest algorithm design technique to apply"* một khi đã hiểu.

## 5. Demo: Fibonacci, edit distance, knapsack

Ba phần. **(1) Fibonacci:** đếm số lần gọi — ngây thơ (mũ) vs có nhớ (tuyến tính). **(2) Edit distance:** dựng bảng `D[i][j]` cho `"kitten" → "sitting"`, in cả bảng, đáp số ở góc. **(3) Knapsack 0/1:** bảng `K[i][w]` cho giá trị lớn nhất.

```typescript
import { strict as assert } from "node:assert";

// ─── ĐỘNG LỰC: Fibonacci đệ quy ngây thơ tính LẠI cùng bài con vô số lần ───
let naiveCalls = 0;
function fibNaive(n: number): number {
  naiveCalls++;
  if (n < 2) return n;
  return fibNaive(n - 1) + fibNaive(n - 2);   // F(n-2) bị tính lại ở cả hai nhánh
}

let memoComputes = 0;
function fibMemo(n: number, cache = new Map<number, number>()): number {
  if (n < 2) return n;
  if (cache.has(n)) return cache.get(n)!;      // đã tính → lấy lại, KHÔNG tính nữa
  memoComputes++;
  const v = fibMemo(n - 1, cache) + fibMemo(n - 2, cache);
  cache.set(n, v);
  return v;
}

const N = 30;
const f1 = fibNaive(N);
const f2 = fibMemo(N);
console.log(`FIBONACCI F(${N}) = ${f1}:`);
console.log(`  đệ quy ngây thơ: ${naiveCalls} lần gọi hàm  (mũ ~ φ^n)`);
console.log(`  có nhớ (memo)  : ${memoComputes} lần tính    (tuyến tính ~ n)`);
assert.equal(f1, f2);                          // cùng đáp số
assert.equal(f1, 832040);
assert.ok(naiveCalls > 1000 * memoComputes);   // ngây thơ đắt gấp hàng nghìn lần

// ─── EDIT DISTANCE (Levenshtein): ít thao tác nhất biến chuỗi a → b ───
// Mỗi ký tự cuối: khớp/thay (substitute), chèn (insert), hoặc xoá (delete).
function editDistance(a: string, b: string): { dist: number; table: number[][] } {
  const m = a.length, n = b.length;
  // D[i][j] = số thao tác ít nhất biến a[0..i) → b[0..j)
  const D: number[][] = Array.from({ length: m + 1 }, () => new Array(n + 1).fill(0));
  for (let i = 0; i <= m; i++) D[i][0] = i;     // xoá i ký tự
  for (let j = 0; j <= n; j++) D[0][j] = j;     // chèn j ký tự
  for (let i = 1; i <= m; i++)
    for (let j = 1; j <= n; j++) {
      const cost = a[i - 1] === b[j - 1] ? 0 : 1;  // khớp = 0, thay = 1
      D[i][j] = Math.min(
        D[i - 1][j - 1] + cost,   // khớp/thay
        D[i - 1][j] + 1,          // xoá
        D[i][j - 1] + 1,          // chèn
      );
    }
  return { dist: D[m][n], table: D };
}

const a = "kitten", b = "sitting";
const ed = editDistance(a, b);
console.log(`\nEDIT DISTANCE "${a}" → "${b}" = ${ed.dist} thao tác:`);
console.log(`      ${["", ...b].join("  ")}`);
ed.table.forEach((row, i) => console.log(`  ${(i === 0 ? "" : a[i - 1]).padEnd(2)} ${row.map((v) => String(v).padStart(2)).join(" ")}`));
assert.equal(ed.dist, 3);   // k→s (thay), e→i (thay), chèn g: 3 thao tác

// ─── KNAPSACK 0/1: chọn tập món (mỗi món 1 lần) tối đa giá trị trong sức chứa W ───
function knapsack(weights: number[], values: number[], W: number): number {
  const n = weights.length;
  // K[i][w] = giá trị lớn nhất dùng i món đầu với sức chứa w
  const K: number[][] = Array.from({ length: n + 1 }, () => new Array(W + 1).fill(0));
  for (let i = 1; i <= n; i++)
    for (let w = 0; w <= W; w++) {
      K[i][w] = K[i - 1][w];                       // không lấy món i
      if (weights[i - 1] <= w)                      // lấy món i nếu vừa sức chứa
        K[i][w] = Math.max(K[i][w], K[i - 1][w - weights[i - 1]] + values[i - 1]);
    }
  return K[n][W];
}

const weights = [2, 3, 4, 5], values = [3, 4, 5, 6], cap = 5;
const best = knapsack(weights, values, cap);
console.log(`\nKNAPSACK 0/1 — sức chứa ${cap}, món (nặng/giá): ${weights.map((w, i) => `${w}/${values[i]}`).join(", ")}`);
console.log(`  giá trị lớn nhất = ${best}  (chọn món nặng 2 + nặng 3 = giá 3+4)`);
assert.equal(best, 7);   // 2+3 = 5 (vừa chứa), giá 3+4 = 7 > chọn 1 món nặng 5 (giá 6)

console.log("\nQHĐ = đệ quy + NHỚ LẠI bài con chồng lấn: vét cạn mọi khả năng (đúng) nhưng");
console.log("lưu kết quả trung gian để không tính lại (hiệu quả) — Skiena tr.307.");
```

Kết quả chạy thật *(tất định)*:

```
FIBONACCI F(30) = 832040:
  đệ quy ngây thơ: 2692537 lần gọi hàm  (mũ ~ φ^n)
  có nhớ (memo)  : 29 lần tính    (tuyến tính ~ n)

EDIT DISTANCE "kitten" → "sitting" = 3 thao tác:
        s  i  t  t  i  n  g
      0  1  2  3  4  5  6  7
  k   1  1  2  3  4  5  6  7
  i   2  2  1  2  3  4  5  6
  t   3  3  2  1  2  3  4  5
  t   4  4  3  2  1  2  3  4
  e   5  5  4  3  2  2  3  4
  n   6  6  5  4  3  3  2  3

KNAPSACK 0/1 — sức chứa 5, món (nặng/giá): 2/3, 3/4, 4/5, 5/6
  giá trị lớn nhất = 7  (chọn món nặng 2 + nặng 3 = giá 3+4)

QHĐ = đệ quy + NHỚ LẠI bài con chồng lấn: vét cạn mọi khả năng (đúng) nhưng
lưu kết quả trung gian để không tính lại (hiệu quả) — Skiena tr.307.
```

Ba điều đáng thấm. **(1) Nhớ lại biến mũ thành tuyến tính:** tính `F(30)` ngây thơ tốn **2.692.537** lần gọi, có nhớ chỉ **29** lần — gấp gần trăm nghìn lần, chỉ vì thêm một bảng cache; `F(50)` ngây thơ thì vô vọng còn có nhớ thì tức thì. **(2) Bảng DP kể lại lời giải:** góc dưới-phải bảng edit distance là `3` — và lần theo bảng (ô nào sinh ra ô nào) còn *dựng lại* được chuỗi thao tác: `k→s`, `e→i`, chèn `g`. **(3) Knapsack chọn khôn, không tham:** sức chứa 5, tham lam "lấy món giá cao nhất trước" sẽ lấy món nặng 5 (giá 6); QHĐ xét *mọi* tổ hợp và thấy nặng-2 + nặng-3 (giá `3+4 = 7`) tốt hơn — đúng chỗ tham lam thất bại mà QHĐ thắng.

> [!note] Tự thử
> 1. Thêm bảng `back[i][j]` lưu lựa chọn nào cho `D[i][j]`, rồi lần ngược để *in ra* dãy thao tác biến `kitten → sitting`. (Gọi là *traceback*.)
> 2. Knapsack: đổi sức chứa thành 7. Giá trị lớn nhất giờ là bao nhiêu, chọn món nào?
> 3. QHĐ edit distance tốn `O(mn)` bộ nhớ. Chứng tỏ ta chỉ cần **hai hàng** bảng (hàng trước + hàng hiện tại) để tính *giá trị* khoảng cách — khi nào cần giữ cả bảng?
> 4. Vì sao knapsack 0/1 là QHĐ được, còn "knapsack với trọng số thực/liên tục" lại có thể giải *tham lam*? (Gợi ý: fractional knapsack.)

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
| 9 | **Quy hoạch động** ← *đang ở đây* | tối ưu bằng bảng con | Skiena Ch10 |
| 10 | Tìm kiếm tổ hợp & backtracking | duyệt không gian lời giải | Skiena Ch9 |
| 11 | NP-đầy đủ & bài toán khó | khi không có lời giải nhanh | Skiena Ch11–12 |
| 12 | *(nâng cao)* Khớp chuỗi | KMP / Rabin–Karp | Skiena §6.7 + CLRS Ch32 |
| 13 | *(nâng cao)* Luồng mạng | max-flow / min-cut | Skiena §8.5 + CLRS Ch24 |
| 14 | *(nâng cao)* Thuật toán ngẫu nhiên | randomized quicksort, Monte Carlo | Skiena Ch6 |

QHĐ là anh em của [chia để trị](bai_06_chia-de-tri.md) (bài con chồng lấn thay vì độc lập); khi cả QHĐ cũng bó tay (trạng thái mũ) thì sang [backtracking](bai_10_backtracking.md) và [NP-đầy đủ](bai_11_np-day-du.md).

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 9.1 — Vì sao Fibonacci đệ quy ngây thơ chậm theo cấp số mũ?
> **Đáp:** **bài con chồng lấn** — `fib(n-2)` và các giá trị nhỏ hơn bị tính đi tính lại ở nhiều nhánh; số lần gọi `~φⁿ` dù chỉ có `n` giá trị khác nhau (Skiena tr. 307).

> [!question] Thẻ 9.2 — Quy hoạch động là gì? Nó đứng giữa hai thái cực nào?
> **Đáp:** cài đặt hiệu quả một đệ quy bằng **lưu kết quả bộ phận**. Giữa **tham lam** (nhanh, thường không tối ưu) và **vét cạn** (tối ưu, quá đắt): duyệt mọi khả năng (đúng) + nhớ lại (hiệu quả) (Skiena tr. 307).

> [!question] Thẻ 9.3 — Memoization (top-down) khác lập bảng (bottom-up) ra sao?
> **Đáp:** cùng ý tưởng. **Top-down**: giữ đệ quy + cache, tính bài con khi cần. **Bottom-up**: điền bảng từ bài con nhỏ nhất lên, không đệ quy. Cả hai mỗi bài con tính một lần.

> [!question] Thẻ 9.4 — Hai tính chất để một bài toán dùng được QHĐ?
> **Đáp:** **(1) bài con chồng lấn** (nếu không, chia-để-trị đủ); **(2) cấu trúc con tối ưu** — lời giải tối ưu ghép từ lời giải tối ưu của bài con. Thiếu (2) thì QHĐ sai.

> [!question] Thẻ 9.5 — Edit distance: `D[i][j]` là gì, và là min của ba lựa chọn nào?
> **Đáp:** số thao tác ít nhất biến `a[0..i)` → `b[0..j)`. Min của: khớp/thay (`D[i-1][j-1] + 0/1`), xoá (`D[i-1][j]+1`), chèn (`D[i][j-1]+1`) — ba phép trên ký tự cuối (Skiena tr. 315). Tổng `O(mn)`.

## 8. Câu hỏi tự kiểm tra

1. Giải thích "bài con chồng lấn" qua ví dụ Fibonacci. Nó khác chia-để-trị (Bài 6) ở đâu? *(mục 1, 4)*
2. QHĐ đứng giữa tham lam và vét cạn thế nào? Nó lấy ưu điểm gì của mỗi bên? *(mục 2)*
3. Viết công thức truy hồi `D[i][j]` của edit distance và giải thích ba số hạng. *(mục 3)*
4. Hai tính chất cần có để dùng QHĐ là gì? Cho một bài *không* có cấu trúc con tối ưu. *(mục 4)*
5. Chạy demo mục 5. Vì sao knapsack chọn (2,3) giá 7 chứ không chọn món nặng 5 giá 6? Tham lam sai ở đâu? *(mục 4 & 5)*

## Tóm tắt một trang

```
BÀI 9 — QUY HOẠCH ĐỘNG
─────────────────────────────────────────────────────────
VẤN ĐỀ  đệ quy ngây thơ tính LẠI cùng bài con (fib: ~φ^n gọi cho n giá trị) —
   BÀI CON CHỒNG LẤN (Skiena tr.307).

QHĐ  đệ quy + NHỚ LẠI kết quả bộ phận. Giữa tham lam (nhanh, ko tối ưu) và vét
   cạn (tối ưu, đắt): duyệt mọi khả năng (ĐÚNG) + lưu trung gian (HIỆU QUẢ)
   (Skiena tr.307). Top-down (memo) = đệ quy+cache; bottom-up = điền bảng.

DÙNG ĐƯỢC QHĐ khi  (1) bài con CHỒNG LẤN (ko thì chia-để-trị đủ); (2) CẤU TRÚC
   CON TỐI ƯU (lời giải lớn ghép từ lời giải tối ưu bài con).

EDIT DISTANCE  D[i][j] = min(khớp/thay D[i-1][j-1]+0/1, xoá D[i-1][j]+1, chèn
   D[i][j-1]+1) — ba phép trên ký tự cuối (Skiena tr.315). O(mn).

KNAPSACK 0/1  K[i][w] = max(bỏ K[i-1][w], lấy K[i-1][w-wt]+val). Chọn khôn, ko
   tham.

DEMO  F(30): ngây thơ 2.692.537 gọi vs memo 29. "kitten"→"sitting" = 3. Knapsack
   W=5: chọn (2,3) giá 7 > món nặng 5 giá 6 (tham lam sai, QHĐ đúng).

3 ANH EM  chia-để-trị (mảnh ĐỘC LẬP) · tham lam (chọn tại chỗ) · QHĐ (mảnh
   CHỒNG LẤN, xét mọi lựa chọn + nhớ).
```

## Nguồn

- **Skiena, Steven S. — *The Algorithm Design Manual*, 3rd ed.** (Springer, 2020) — **Chapter 10: Dynamic Programming** (§10.1 Caching vs. Computation: Fibonacci & memoization; §10.2 Approximate String Matching: edit distance): định nghĩa QHĐ, bài con chồng lấn, top-down vs bottom-up, công thức truy hồi edit distance. `tai_lieu/The Algorithm Design Manual 3rd Edition...pdf` (offset **PDF = tr. + 14** ở Ch10).
- Liên hệ: [Bài 6 — chia để trị](bai_06_chia-de-tri.md) (anh em: bài con độc lập); [Bài 8 — greedy](bai_08_do-thi-trong-so.md) (QHĐ khi greedy không đủ); [Bài 10 — backtracking](bai_10_backtracking.md) & [Bài 11 — NP](bai_11_np-day-du.md) (khi cả QHĐ bó tay).

---

**Bản đồ khoá học:** [Bài 0 — Thuật toán & tính đúng](bai_00_thuat-toan-la-gi.md) · [Bài 1 — Phân tích Big-O](bai_01_big-o.md) · [Bài 2 — CTDL tuyến tính](bai_02_ctdl-tuyen-tinh.md) · [Bài 3 — Từ điển & bảng băm](bai_03_bang-bam.md) · [Bài 4 — Heap & cây tìm kiếm](bai_04_heap-cay-tim-kiem.md) · [Bài 5 — Sắp xếp](bai_05_sap-xep.md) · [Bài 6 — Chia để trị & đệ quy](bai_06_chia-de-tri.md) · [Bài 7 — Đồ thị: duyệt](bai_07_do-thi-duyet.md) · [Bài 8 — Đồ thị trọng số](bai_08_do-thi-trong-so.md) · **[Bài 9 — Quy hoạch động] ← bạn đang ở đây** · [Bài 10 — Backtracking](bai_10_backtracking.md) · [Bài 11 — NP-đầy đủ](bai_11_np-day-du.md) · [Bài 12 — Khớp chuỗi](bai_12_khop-chuoi.md) · [Bài 13 — Luồng mạng](bai_13_luong-mang.md) · [Bài 14 — Thuật toán ngẫu nhiên](bai_14_ngau-nhien.md)

Xem thêm [README khoá học](../README.md).
