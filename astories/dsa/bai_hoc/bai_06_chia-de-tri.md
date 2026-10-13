# Bài 6 — Chia để trị và đệ quy: bẻ nhỏ bài toán, giải truy hồi

> [!info] Về bài này
> Mergesort (Bài 5) chia mảng làm đôi, sắp mỗi nửa, rồi trộn — đó là một *khuôn mẫu thiết kế* lớn: **chia để trị** *(divide and conquer)*. Bài này tách khuôn mẫu ấy ra khỏi mergesort để dùng cho bài toán khác (đếm nghịch thế, nhân nhanh, cặp gần nhất...), và quan trọng hơn: học cách **phân tích chi phí** một thuật toán đệ quy bằng **quan hệ truy hồi** và **định lý thợ (master theorem)** — công cụ cho ra ngay bậc Big-O chỉ từ cấu trúc đệ quy.
> Nguồn (Luật số 1): **Skiena** *The Algorithm Design Manual 3e* — **Chapter 5: Divide and Conquer** (§5.3 Recurrence Relations, §5.4 Master Theorem) (`tai_lieu/`, trích `> [!quote] Skiena (tr. N)`, **PDF = tr. + 16** ở Ch5).
> **Chạy demo:** `node bai_06.ts` — Node 22+, không cài gói. Code tất định.
> Cần đọc trước: [Bài 1 — Big-O](bai_01_big-o.md), [Bài 5 — Sắp xếp](bai_05_sap-xep.md) (mergesort là ca mẫu).

## Mục lục

1. [Tình huống: bẻ nhỏ để chinh phục](#1-tình-huống-bẻ-nhỏ-để-chinh-phục)
2. [Chia để trị: chia, trị, gộp](#2-chia-để-trị-chia-trị-gộp)
3. [Quan hệ truy hồi và cây đệ quy](#3-quan-hệ-truy-hồi-và-cây-đệ-quy)
4. [Định lý thợ (master theorem): ba trường hợp](#4-định-lý-thợ-master-theorem-ba-trường-hợp)
5. [Demo: đếm nghịch thế và master theorem](#5-demo-đếm-nghịch-thế-và-master-theorem)
6. [Bản đồ khoá DSA](#6-bản-đồ-khoá-dsa)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Tình huống: bẻ nhỏ để chinh phục

> [!example] Bài toán lớn làm ta choáng
> Cho một mảng `n` phần tử, đếm số **nghịch thế** — số cặp `(i, j)` với `i < j` nhưng `a[i] > a[j]` (thước đo "mảng lộn xộn tới đâu", dùng trong hệ thống gợi ý để so hai bảng xếp hạng). Cách hiển nhiên: xét *mọi* cặp — `O(n²)`. Với mảng 1 triệu phần tử là `5 × 10¹¹` phép so sánh, vô vọng. Có cách nào `O(n log n)` không?

Có — và chìa khoá là một ý tưởng cổ xưa: bài to thì *bẻ nhỏ*.

> [!quote] Skiena (tr. 147)
> "One of the most powerful techniques for solving problems is to break them down into smaller, more easily solved pieces."
>
> *Một trong những kỹ thuật **mạnh nhất** để giải bài toán là **bẻ chúng thành những mảnh nhỏ hơn, dễ giải hơn**.*

Khi các mảnh nhỏ *cùng kiểu* với bài gốc, một thuật toán **đệ quy** lộ diện:

> [!quote] Skiena (tr. 147)
> "A recursive algorithm starts to become apparent whenever we can break the problem into smaller instances of the same type of problem."
>
> *Một thuật toán **đệ quy** bắt đầu lộ diện bất cứ khi nào ta có thể bẻ bài toán thành những **thực thể nhỏ hơn của cùng loại bài toán**.*

## 2. Chia để trị: chia, trị, gộp

**Chia để trị** là một khuôn đệ quy ba nhịp:

> [!quote] Skiena (tr. 147)
> "to use divide and conquer as an algorithm design technique, we must divide the problem into two smaller subproblems, solve each of them recursively, and then meld the two partial solutions into one solution to the full problem."
>
> *để dùng chia-để-trị như một kỹ thuật thiết kế, ta phải **chia** bài toán thành hai bài con nhỏ hơn, **giải** mỗi bài con bằng đệ quy, rồi **hoà** hai lời giải bộ phận thành một lời giải cho bài toán đầy đủ.*

```
          CHIA            TRỊ (đệ quy)          GỘP
   bài cỡ n  ──►  hai bài cỡ n/2  ──►  hai lời giải  ──►  một lời giải cỡ n
                  (tự giải tiếp)                          (meld/merge)
```

Điều kiện để khuôn này *hiệu quả* nằm ở nhịp **gộp**:

> [!quote] Skiena (tr. 147)
> "Whenever the merging takes less time than solving the two subproblems, we get an efficient algorithm."
>
> *Bất cứ khi nào việc **gộp tốn ít thời gian hơn** việc giải hai bài con, ta có một thuật toán hiệu quả.*

Mergesort (Bài 5) là ca mẫu: chia đôi (O(1)), giải hai nửa (đệ quy), **trộn** hai nửa đã sắp chỉ tốn O(n) — gộp rẻ hơn hẳn hai bài con, nên tổng thể `O(n log n)`. Mục 5 cho thấy *cùng* khuôn trộn đó, chỉnh một dòng, còn **đếm được nghịch thế** — chia để trị làm nhiều hơn là sắp xếp.

## 3. Quan hệ truy hồi và cây đệ quy

Làm sao biết một thuật toán đệ quy tốn bao nhiêu? Viết **quan hệ truy hồi** *(recurrence)* — chi phí của bài cỡ `n` theo chi phí các bài con. Khuôn chia-để-trị điển hình cho:

```
T(n) = a · T(n/b) + f(n)
        │     │        └── f(n): công CHIA + GỘP ở tầng này (không kể đệ quy)
        │     └── n/b : mỗi bài con nhỏ đi b lần
        └── a : số bài con sinh ra
```

Mergesort: chia thành `a = 2` bài con, mỗi bài cỡ `n/2` (`b = 2`), công trộn `f(n) = O(n)` → `T(n) = 2T(n/2) + O(n)`.

Cách trực quan để giải: vẽ **cây đệ quy** và cộng công theo *từng tầng*. Mergesort có `log₂ n` tầng, mỗi tầng tổng công trộn là `O(n)` (mỗi phần tử xuất hiện ở đúng một bài con mỗi tầng) → tổng `O(n log n)`. Đây đúng là lập luận "đi `lg n` tầng × công tuyến tính mỗi tầng" của Bài 5 (Skiena tr. 128). Demo mục 5 in công từng tầng để thấy tận mắt.

## 4. Định lý thợ (master theorem): ba trường hợp

Vẽ cây mỗi lần thì mệt. **Định lý thợ** *(master theorem)* cho đáp số ngay, chỉ từ `a`, `b`, `f(n)`:

> [!quote] Skiena (tr. 154)
> "Divide-and-conquer recurrences of the form [...] are generally easy to solve, because the solutions typically fall into one of three distinct cases"
>
> *Các truy hồi chia-để-trị dạng `T(n) = aT(n/b)+f(n)` nhìn chung **dễ giải**, vì nghiệm thường rơi vào **một trong ba trường hợp** phân biệt.*

Chìa khoá là so `f(n)` (công chia+gộp) với một mốc gọi là **`n^c` với `c = log_b a`** (phản ánh tổng công ở tầng lá — số lá là `a^(log_b n) = n^c`):

```
Đặt mốc n^c, c = log_b(a).  So công GỘP f(n) với mốc này:

  CA 1   f(n) nhỏ hơn n^c         → T(n) = Θ(n^c)          LÁ chi phối (việc ở đáy nhiều nhất)
  CA 2   f(n) ≈ n^c               → T(n) = Θ(n^c · log n)  CÂN BẰNG mọi tầng
  CA 3   f(n) lớn hơn n^c         → T(n) = Θ(f(n))         GỐC chi phối (gộp đắt nhất)
```

Mergesort: `a = 2, b = 2` → `c = log₂ 2 = 1`, mốc `n^1 = n`. Công gộp `f(n) = n ≈ n^c` → **Ca 2** → `Θ(n log n)`. Khớp điều Skiena nói:

> [!quote] Skiena (tr. 154)
> "Case 1 holds for heap construction and matrix multiplication, while Case 2 holds for mergesort."
>
> *Trường hợp 1 đúng cho **dựng heap** và **nhân ma trận**, còn trường hợp 2 đúng cho **mergesort**.*

Vài ví dụ đọc nhanh bằng master theorem:

| Truy hồi | `a` | `b` | `c=log_b a` | `f(n)` | Ca | `T(n)` | Thuật toán |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| `T(n)=2T(n/2)+n` | 2 | 2 | 1 | `n` | 2 | `Θ(n log n)` | mergesort, đếm nghịch thế |
| `T(n)=T(n/2)+1` | 1 | 2 | 0 | `1` | 2 | `Θ(log n)` | tìm nhị phân (Bài 0) |
| `T(n)=2T(n/2)+1` | 2 | 2 | 1 | `1` | 1 | `Θ(n)` | duyệt cây nhị phân |
| `T(n)=7T(n/2)+n²` | 7 | 2 | ~2.81 | `n²` | 1 | `Θ(n^2.81)` | Strassen nhân ma trận |

> [!note] Master theorem là hộp đen — nhưng biết vì sao nó đúng thì hơn
> Skiena gọi nó là *"a black-box piece of machinery"*: cứ nhét `a, b, f(n)` vào là ra đáp số, không cần hiểu bên trong. Nhưng trực giác rất đơn giản — cây đệ quy có `log_b n` tầng; tầng gốc tốn `f(n)`, tầng lá tốn `n^c`; **ba ca chỉ là trả lời "đáy nặng, cân bằng, hay ngọn nặng?"**. Đây đúng tinh thần "giữ cây thấp = ít bước" đã gặp ở BST/heap (Bài 4).

## 5. Demo: đếm nghịch thế và master theorem

Demo hai phần. **(1) Đếm nghịch thế:** cùng đáp số bằng hai cách — ngây thơ `O(n²)` (mọi cặp) và chia-để-trị `O(n log n)` (sửa đúng một dòng trong mergesort); bảng số thao tác khi `n` lớn dần cho thấy khoảng cách bung ra. **(2) Master theorem cụ thể:** in công trộn từng tầng của mergesort `n=16` → thấy mỗi tầng ~`n`, có `log₂ n` tầng = Ca 2.

```typescript
import { strict as assert } from "node:assert";

// ─── ĐẾM NGHỊCH THẾ (inversions): số cặp i<j mà a[i] > a[j] ───
// Thước "mảng lộn xộn tới đâu". Chia-để-trị giải trong O(n log n), không chỉ sắp xếp.

// Cách ngây thơ: xét MỌI cặp → O(n^2).
function countNaive(a: number[]): { inv: number; ops: number } {
  let inv = 0, ops = 0;
  for (let i = 0; i < a.length; i++)
    for (let j = i + 1; j < a.length; j++) { ops++; if (a[i] > a[j]) inv++; }
  return { inv, ops };
}

// Chia-để-trị: sửa mergesort — khi trộn, nếu lấy phần tử từ nửa PHẢI trước
// một loạt phần tử nửa TRÁI còn lại, thì mỗi phần tử trái đó tạo 1 nghịch thế.
function countDC(input: number[]): { inv: number; ops: number } {
  let inv = 0, ops = 0;
  function sort(a: number[]): number[] {
    if (a.length <= 1) return a;
    const mid = a.length >> 1;
    const left = sort(a.slice(0, mid));
    const right = sort(a.slice(mid));
    const out: number[] = [];
    let i = 0, j = 0;
    while (i < left.length && j < right.length) {
      ops++;
      if (left[i] <= right[j]) out.push(left[i++]);
      else { inv += left.length - i; out.push(right[j++]); } // right[j] nhỏ hơn mọi left còn lại
    }
    while (i < left.length) out.push(left[i++]);
    while (j < right.length) out.push(right[j++]);
    return out;
  }
  sort(input);
  return { inv, ops };
}

const sample = [2, 4, 1, 3, 5];  // nghịch thế: (2,1),(4,1),(4,3) = 3
console.log("ĐẾM NGHỊCH THẾ trên [2, 4, 1, 3, 5]:");
console.log(`  ngây thơ O(n^2): ${countNaive(sample).inv} nghịch thế`);
console.log(`  chia-để-trị    : ${countDC(sample).inv} nghịch thế  (cùng đáp số, dựa trên mergesort)`);
assert.equal(countNaive(sample).inv, 3);
assert.equal(countDC(sample).inv, countNaive(sample).inv);

// So số thao tác khi n lớn dần: mảng ĐẢO NGƯỢC [n..1] (nhiều nghịch thế nhất).
console.log("\nSỐ THAO TÁC trên mảng đảo ngược [n..1] (nghịch thế = n(n-1)/2):");
console.log("  n     ngây thơ O(n^2)   chia-để-trị O(n log n)");
for (const n of [8, 16, 32, 64]) {
  const arr = Array.from({ length: n }, (_, i) => n - i);
  const naive = countNaive(arr), dc = countDC(arr);
  assert.equal(naive.inv, dc.inv);              // cùng đáp số
  assert.equal(naive.inv, n * (n - 1) / 2);     // mảng đảo = tối đa nghịch thế
  console.log(`  ${String(n).padStart(3)}   ${String(naive.ops).padStart(10)}       ${String(dc.ops).padStart(10)}`);
}

// ─── MASTER THEOREM cụ thể: mergesort T(n)=2T(n/2)+O(n) → ca 2 → n log n ───
// Đo công TRỘN ở từng tầng đệ quy: mỗi tầng ~n, có log2(n) tầng.
function workPerLevel(n: number): number[] {
  const levels: number[] = [];
  function rec(size: number, depth: number): void {
    if (size <= 1) return;
    const mid = size >> 1, right = size - mid;
    levels[depth] = (levels[depth] ?? 0) + (size - 1);  // trộn size phần tử ≤ size-1 so sánh
    rec(mid, depth + 1);
    rec(right, depth + 1);
  }
  rec(n, 0);
  return levels;
}
const n = 16;
const levels = workPerLevel(n);
console.log(`\nMASTER THEOREM — mergesort n=${n}, T(n)=2T(n/2)+O(n):`);
levels.forEach((w, d) => console.log(`  tầng ${d}: tối đa ${w} so sánh trộn`));
const total = levels.reduce((a, b) => a + b, 0);
console.log(`  tổng ${total} so sánh ≈ n·log2(n) = ${n} × ${Math.log2(n)} = ${n * Math.log2(n)}  → CA 2: Θ(n log n)`);
assert.equal(levels.length, Math.log2(n));      // đúng log2(n) tầng có công

console.log("\nChia-để-trị: bẻ đôi → giải mỗi nửa → gộp. Nếu gộp rẻ hơn hai nửa cộng lại → hiệu quả.");
console.log("Master theorem T(n)=aT(n/b)+f(n): 3 ca; mergesort là ca 2 (Skiena tr.154).");
```

Kết quả chạy thật *(tất định)*:

```
ĐẾM NGHỊCH THẾ trên [2, 4, 1, 3, 5]:
  ngây thơ O(n^2): 3 nghịch thế
  chia-để-trị    : 3 nghịch thế  (cùng đáp số, dựa trên mergesort)

SỐ THAO TÁC trên mảng đảo ngược [n..1] (nghịch thế = n(n-1)/2):
  n     ngây thơ O(n^2)   chia-để-trị O(n log n)
    8           28               12
   16          120               32
   32          496               80
   64         2016              192

MASTER THEOREM — mergesort n=16, T(n)=2T(n/2)+O(n):
  tầng 0: tối đa 15 so sánh trộn
  tầng 1: tối đa 14 so sánh trộn
  tầng 2: tối đa 12 so sánh trộn
  tầng 3: tối đa 8 so sánh trộn
  tổng 49 so sánh ≈ n·log2(n) = 16 × 4 = 64  → CA 2: Θ(n log n)

Chia-để-trị: bẻ đôi → giải mỗi nửa → gộp. Nếu gộp rẻ hơn hai nửa cộng lại → hiệu quả.
Master theorem T(n)=aT(n/b)+f(n): 3 ca; mergesort là ca 2 (Skiena tr.154).
```

Ba điều đáng thấm. **(1) Chia-để-trị làm nhiều hơn sắp:** sửa đúng *một dòng* trong mergesort (`inv += left.length - i`) là đếm được nghịch thế trong `O(n log n)` — vì khi một phần tử nửa phải "vượt mặt" cả loạt phần tử nửa trái còn lại, đó là bằng ấy nghịch thế đếm gộp một lần. **(2) Khoảng cách O(n²) vs O(n log n) bung theo `n`:** ở `n=64`, ngây thơ tốn 2016 thao tác còn chia-để-trị chỉ 192 — gấp hơn 10 lần, và tỉ lệ này còn phình nữa khi `n` lớn. **(3) Master theorem hiện ra từ cây:** công trộn mỗi tầng xấp xỉ `n` (15, 14, 12, 8 — hao hụt vì bài con lẻ), có đúng `log₂16 = 4` tầng → tổng ~`n log n`; đây chính là Ca 2 (`f(n) = n ≈ n^c`), không cần giải tay.

> [!note] Tự thử
> 1. Đổi mảng trong demo nghịch thế sang **đã sắp** `[1..n]`: cả hai cách ra bao nhiêu nghịch thế? Số thao tác chia-để-trị có đổi không? (Gợi ý: trộn vẫn chạy đủ.)
> 2. Áp master theorem cho `T(n) = 3T(n/2) + n`: `c = log₂3 ≈ 1.58`, `f(n)=n` — rơi vào ca nào? `T(n) = ?`
> 3. Tìm **cặp gần nhất** trên mặt phẳng (closest pair) có thuật toán chia-để-trị `O(n log n)` (Skiena §5.6). Nhịp "gộp" của nó làm gì?
> 4. Vì sao binary search `T(n)=T(n/2)+1` cho `Θ(log n)` chứ không `Θ(n)`? Áp master theorem: `a=1, b=2, c=0`, `f(n)=1=n^0` — ca mấy?

## 6. Bản đồ khoá DSA

| # | Bài | Chủ đề | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | Thuật toán & tính đúng | nền: đúng vs hiệu quả | Skiena Ch1 + Grokking |
| 1 | Phân tích Big-O | đo chi phí khi `n` lớn | Skiena Ch2 |
| 2 | CTDL tuyến tính | mảng / list / stack / queue | Skiena Ch3 |
| 3 | Từ điển & bảng băm | tra cứu O(1) trung bình | Skiena Ch3 |
| 4 | Heap & cây tìm kiếm | lấy min/max, tra có thứ tự | Skiena Ch3–4 |
| 5 | Sắp xếp | quicksort / mergesort / heapsort | Skiena Ch4 |
| 6 | **Chia để trị & đệ quy** ← *đang ở đây* | bẻ nhỏ bài toán, master theorem | Skiena Ch5 |
| 7 | Đồ thị: biểu diễn & duyệt | BFS / DFS | Skiena Ch7 |
| 8 | Đồ thị trọng số: MST & đường ngắn nhất | Dijkstra / Prim / Kruskal | Skiena Ch8 |
| 9 | Quy hoạch động | tối ưu bằng bảng con | Skiena Ch10 |
| 10 | Tìm kiếm tổ hợp & backtracking | duyệt không gian lời giải | Skiena Ch9 |
| 11 | NP-đầy đủ & bài toán khó | khi không có lời giải nhanh | Skiena Ch11–12 |
| 12 | *(nâng cao)* Khớp chuỗi | KMP / Rabin–Karp | Skiena §6.7 + CLRS Ch32 |
| 13 | *(nâng cao)* Luồng mạng | max-flow / min-cut | Skiena §8.5 + CLRS Ch24 |
| 14 | *(nâng cao)* Thuật toán ngẫu nhiên | randomized quicksort, Monte Carlo | Skiena Ch6 |

Chia để trị "bẻ đôi độc lập"; [Bài 9 — quy hoạch động](bai_09_quy-hoach-dong.md) "bẻ nhưng các mảnh chồng lấn" — hai mặt của cùng tư tưởng (Skiena nói thẳng ở tr. 147).

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 6.1 — Chia để trị gồm ba nhịp gì? Khi nào thì hiệu quả?
> **Đáp:** **chia** bài thành bài con nhỏ hơn, **trị** mỗi bài con bằng đệ quy, **gộp** các lời giải bộ phận. Hiệu quả khi **gộp tốn ít hơn** giải các bài con (Skiena tr. 147). Mergesort là ca mẫu.

> [!question] Thẻ 6.2 — Quan hệ truy hồi `T(n) = a·T(n/b) + f(n)`: mỗi ký hiệu nghĩa là gì?
> **Đáp:** `a` = số bài con; `n/b` = kích thước mỗi bài con (nhỏ đi `b` lần); `f(n)` = công chia + gộp ở tầng này (không kể đệ quy). Mergesort: `2T(n/2)+O(n)`.

> [!question] Thẻ 6.3 — Master theorem so `f(n)` với mốc nào? Ba trường hợp cho gì?
> **Đáp:** so với `n^c`, `c = log_b a`. Ca 1 (`f` nhỏ hơn): `Θ(n^c)` — lá chi phối. Ca 2 (`f ≈ n^c`): `Θ(n^c log n)` — cân bằng. Ca 3 (`f` lớn hơn): `Θ(f(n))` — gốc chi phối (Skiena tr. 154).

> [!question] Thẻ 6.4 — Vì sao mergesort là Ca 2 của master theorem?
> **Đáp:** `a=2, b=2` → `c = log₂2 = 1`, mốc `n`. Công gộp `f(n)=n ≈ n^1` → Ca 2 → `Θ(n log n)`. Skiena xác nhận "Case 2 holds for mergesort" (tr. 154).

> [!question] Thẻ 6.5 — Chia để trị khác quy hoạch động (Bài 9) ở đâu?
> **Đáp:** chia-để-trị bẻ thành bài con **độc lập** (hai nửa không chồng lấn); quy hoạch động bẻ thành bài con **chồng lấn** nên phải nhớ lại (memo) kẻo tính lại. Cùng tư tưởng "bẻ nhỏ" (Skiena tr. 147).

## 8. Câu hỏi tự kiểm tra

1. Viết ba nhịp chia-để-trị cho mergesort, chỉ rõ nhịp nào tốn O(n). *(mục 2)*
2. Viết quan hệ truy hồi cho: tìm nhị phân, mergesort, duyệt cây nhị phân. *(mục 3)*
3. Áp master theorem giải `T(n)=4T(n/2)+n`: `c`? ca nào? `T(n)=?` *(mục 4)*
4. Giải thích vì sao đếm nghịch thế bằng mergesort chỉ cần sửa một dòng, và vì sao dòng đó đúng. *(mục 2 & 5)*
5. Chạy demo mục 5. Vì sao công trộn mỗi tầng không đúng bằng `n` (15, 14, 12, 8 thay vì 16, 16, 16, 16)? *(mục 3 & 5)*

## Tóm tắt một trang

```
BÀI 6 — CHIA ĐỂ TRỊ & ĐỆ QUY
─────────────────────────────────────────────────────────
Ý LỚN  bài to → BẺ NHỎ thành bài con CÙNG LOẠI → đệ quy (Skiena tr.147).

CHIA ĐỂ TRỊ (3 nhịp)  CHIA bài thành bài con → TRỊ mỗi bài con (đệ quy) → GỘP
   lời giải. Hiệu quả KHI gộp rẻ hơn giải các bài con (Skiena tr.147).
   Mergesort = ca mẫu (trộn O(n) < giải 2 nửa).

TRUY HỒI  T(n) = a·T(n/b) + f(n).  a = số bài con; n/b = cỡ bài con;
   f(n) = công chia+gộp. Giải bằng vẽ CÂY ĐỆ QUY, cộng công theo tầng.

MASTER THEOREM  so f(n) với mốc n^c, c = log_b(a):
   CA 1  f < n^c   → Θ(n^c)        (lá chi phối)
   CA 2  f ≈ n^c   → Θ(n^c log n)  (cân bằng) ← mergesort: a=b=2,c=1,f=n
   CA 3  f > n^c   → Θ(f(n))       (gốc chi phối)
   (Skiena tr.154: Ca 1 = dựng heap/nhân ma trận; Ca 2 = mergesort.)

DEMO  đếm nghịch thế: sửa 1 dòng mergesort → O(n log n). n=64: ngây thơ 2016
   thao tác vs chia-để-trị 192. Master theorem n=16: 4 tầng ~n công = Ca 2.

vs QUY HOẠCH ĐỘNG (Bài 9)  chia-để-trị = bài con ĐỘC LẬP; QHĐ = bài con CHỒNG
   LẤP (phải nhớ lại). Cùng tư tưởng bẻ nhỏ.
```

## Nguồn

- **Skiena, Steven S. — *The Algorithm Design Manual*, 3rd ed.** (Springer, 2020) — **Chapter 5: Divide and Conquer** (§5.1 Binary Search, §5.3 Recurrence Relations, §5.4 Solving Divide-and-Conquer Recurrences / master theorem): khuôn chia-trị-gộp, quan hệ truy hồi, cây đệ quy, ba trường hợp master theorem. `tai_lieu/The Algorithm Design Manual 3rd Edition...pdf` (offset **PDF = tr. + 16** ở Ch5).
- Liên hệ: [Bài 5 — mergesort](bai_05_sap-xep.md) (ca mẫu); [Bài 9 — quy hoạch động](bai_09_quy-hoach-dong.md) (bài con chồng lấn); [Bài 12 — Rabin–Karp](bai_12_khop-chuoi.md) & [Bài 14 — ngẫu nhiên](bai_14_ngau-nhien.md) (quicksort cũng chia để trị).

---

**Bản đồ khoá học:** [Bài 0 — Thuật toán & tính đúng](bai_00_thuat-toan-la-gi.md) · [Bài 1 — Phân tích Big-O](bai_01_big-o.md) · [Bài 2 — CTDL tuyến tính](bai_02_ctdl-tuyen-tinh.md) · [Bài 3 — Từ điển & bảng băm](bai_03_bang-bam.md) · [Bài 4 — Heap & cây tìm kiếm](bai_04_heap-cay-tim-kiem.md) · [Bài 5 — Sắp xếp](bai_05_sap-xep.md) · **[Bài 6 — Chia để trị & đệ quy] ← bạn đang ở đây** · [Bài 7 — Đồ thị: duyệt](bai_07_do-thi-duyet.md) · [Bài 8 — Đồ thị trọng số](bai_08_do-thi-trong-so.md) · [Bài 9 — Quy hoạch động](bai_09_quy-hoach-dong.md) · [Bài 10 — Backtracking](bai_10_backtracking.md) · [Bài 11 — NP-đầy đủ](bai_11_np-day-du.md) · [Bài 12 — Khớp chuỗi](bai_12_khop-chuoi.md) · [Bài 13 — Luồng mạng](bai_13_luong-mang.md) · [Bài 14 — Thuật toán ngẫu nhiên](bai_14_ngau-nhien.md)

Xem thêm [README khoá học](../README.md).
