# Bài 1 — Phân tích Big-O: đo chi phí khi dữ liệu phình to

> [!info] Về bài này
> Bài 0 nói thuật toán tốt phải vừa **đúng** vừa **hiệu quả**. Bài này dựng công cụ đo trục *hiệu quả*: **Big-O**. Ý tưởng cốt lõi — đừng đo *giây* (phụ thuộc máy, ngôn ngữ, lúc chạy), mà **đếm số bước** và xem nó tăng *nhanh cỡ nào* khi dữ liệu `n` phình to. Đây là ngôn ngữ chung để nói "thuật toán A tốt hơn B" mà không cần cầm máy bấm giờ.
> Nguồn (Luật số 1): **Skiena** *The Algorithm Design Manual 3e* — **Chapter 2: Algorithm Analysis** (`tai_lieu/`, trích `> [!quote] Skiena (tr. N)`, **PDF = tr. + 17**).
> **Chạy demo:** `node bai_01.ts` — Node 22+, không cài gói. Code tất định.
> Cần đọc trước: [Bài 0 — Thuật toán & tính đúng](bai_00_thuat-toan-la-gi.md).

## Mục lục

1. [Tình huống: thuật toán nào nhanh hơn?](#1-tình-huống-thuật-toán-nào-nhanh-hơn)
2. [Mô hình RAM: đếm bước, không đo giây](#2-mô-hình-ram-đếm-bước-không-đo-giây)
3. [Worst, best, average: vì sao luôn nhìn worst case](#3-worst-best-average-vì-sao-luôn-nhìn-worst-case)
4. [Big-O: bỏ hằng số, giữ bậc trội](#4-big-o-bỏ-hằng-số-giữ-bậc-trội)
5. [Demo: đếm thao tác thật theo từng bậc](#5-demo-đếm-thao-tác-thật-theo-từng-bậc)
6. [Bản đồ khoá DSA](#6-bản-đồ-khoá-dsa)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Tình huống: thuật toán nào nhanh hơn?

> [!example] Cách ngây thơ để so hai thuật toán
> Bạn viết hai thuật toán sắp xếp, chạy thử, bấm giờ: cái A xong trong 0,8 giây, cái B trong 1,2 giây. Kết luận A nhanh hơn?
>
> **Sai lầm.** Con số 0,8 giây đó phụ thuộc: máy của bạn (CPU, RAM, cache), ngôn ngữ, trình biên dịch, kích thước dữ liệu bạn chọn, thậm chí lúc đó máy có đang chạy việc khác không. Đổi máy, đổi `n`, có khi B lại thắng. "Đo giây một lần" không trả lời được câu hỏi thật: **khi dữ liệu lớn gấp nghìn lần thì sao?**

Ta cần cách so sánh *độc lập máy và ngôn ngữ*. Skiena mở chương phân tích bằng đúng tinh thần đó:

> [!quote] Skiena (tr. 31)
> "Algorithms are the most important and durable part of computer science because they can be studied in a language- and machine-independent way. [...] Our two most important tools are (1) the RAM model of computation and (2) the asymptotic analysis of computational complexity."
>
> *Thuật toán là phần quan trọng và bền vững nhất của khoa học máy tính vì chúng có thể được nghiên cứu **độc lập với ngôn ngữ và máy móc**. [...] Hai công cụ quan trọng nhất của ta là (1) **mô hình RAM** và (2) **phân tích tiệm cận** độ phức tạp tính toán.*

Hai công cụ đó là nội dung mục 2 và 4.

## 2. Mô hình RAM: đếm bước, không đo giây

Thay vì đo thời gian thật, ta tưởng tượng một máy lý tưởng — **Random Access Machine (RAM)** — và **đếm số thao tác cơ bản**:

> [!quote] Skiena (tr. 31)
> "Each simple operation (+, *, –, =, if, call) takes exactly one time step. [...] Each memory access takes exactly one time step. Furthermore, we have as much memory as we need. The RAM model takes no notice of whether an item is in cache or on the disk."
>
> *Mỗi thao tác đơn giản (+, *, –, =, if, call) tốn **đúng một bước**. [...] Mỗi lần truy cập bộ nhớ tốn đúng một bước. Hơn nữa, ta có bao nhiêu bộ nhớ tuỳ ý. Mô hình RAM **không quan tâm** phần tử nằm ở cache hay trên đĩa.*

Vòng lặp và hàm con **không** phải thao tác đơn — chúng là *tổng* của nhiều bước đơn, tuỳ số vòng lặp. Sắp xếp một triệu phần tử chắc chắn lâu hơn sắp xếp mười phần tử, nên `sort` không thể tính là "một bước".

> [!note] Mô hình RAM "sai" một cách hữu ích
> Thực tế, cộng hai số và truy cập đĩa *không* cùng chi phí — đọc đĩa chậm hơn RAM hàng vạn lần (xem [cloud-base — phân cấp lưu trữ](../../cloud-base/README.md), và [database — buffer manager](../../database/README.md)). Mô hình RAM cố tình bỏ qua điều đó. Nó là một *phép xấp xỉ*: đủ thô để dễ tính, đủ đúng để dự đoán **xu hướng** khi `n` lớn. "Tất cả mô hình đều sai, nhưng vài cái hữu ích."

Dưới mô hình RAM, ta đo run time bằng cách **đếm số bước** một thuật toán chạy trên một đầu vào. Nhưng với cùng kích thước `n`, các đầu vào khác nhau tốn số bước khác nhau — nên "số bước theo `n`" chưa phải một hàm xác định. Mục 3 giải quyết chuyện đó.

## 3. Worst, best, average: vì sao luôn nhìn worst case

Với mỗi kích thước `n`, gom mọi đầu vào cỡ `n` lại, ta định nghĩa ba hàm chi phí (Skiena tr. 33):

```
số bước
   ↑                              ● worst case  — nhiều bước nhất trong mọi đầu vào cỡ n
   │                         ●  ○  average case — trung bình trên mọi đầu vào cỡ n
   │                    ●  ○  ×   best case   — ít bước nhất trong mọi đầu vào cỡ n
   │               ●  ○  ×
   │          ●  ○  ×
   └──────────────────────────→ n (kích thước đầu vào)
```

- **Worst case** — số bước *tối đa* trên mọi đầu vào cỡ `n`.
- **Best case** — số bước *tối thiểu*.
- **Average case** — *trung bình* trên mọi đầu vào cỡ `n`.

Ta gần như luôn dùng **worst case**. Nhiều người thấy phản trực giác (sao không dùng trung bình?), nhưng worst case cho một **lời hứa chắc chắn**: "không bao giờ chậm hơn thế này". Average case thì phải giả định *phân bố* đầu vào — thường không biết và dễ sai.

> [!quote] Skiena (tr. 33)
> "The worst-case complexity generally proves to be most useful of these three measures in practice."
>
> *Độ phức tạp **worst case** nhìn chung tỏ ra **hữu dụng nhất** trong ba thước đo này trên thực tế.*

Nhớ lại Bài 0: tìm tuyến tính best case 1 bước (trúng ngay phần tử đầu), worst case `n` bước (phần tử không có, quét hết). Khi nói "tìm tuyến tính là O(n)", ta đang nói về *worst case* — mục 5 đo tận mắt.

## 4. Big-O: bỏ hằng số, giữ bậc trội

Đếm bước chính xác (kiểu "`2n² + 3n + 7`") vẫn còn rườm. Khi `n` lớn, số hạng `n²` **nuốt** mọi thứ còn lại, và hằng số `2` phụ thuộc chi tiết cài đặt. **Big-O** gạt bỏ cả hai: chỉ giữ **bậc trội**, bỏ hằng số và số hạng bậc thấp. `2n² + 3n + 7` thành **O(n²)**.

> [!quote] Skiena (tr. 36)
> "Take-Home Lesson: The Big Oh notation and worst-case analysis are tools that greatly simplify our ability to compare the efficiency of algorithms."
>
> *Bài học rút ra: Ký hiệu **Big Oh** và phân tích **worst case** là những công cụ **đơn giản hoá rất nhiều** khả năng so sánh hiệu quả của các thuật toán.*

Vì sao được phép bỏ hằng số? Vì câu hỏi thật không phải "A hay B nhanh hơn khi sắp 10 phần tử" mà là "cái nào thắng khi sắp 1 triệu phần tử". Ở quy mô đó, bậc trội quyết định tất cả — Big-O *"cho phép ta bỏ qua chi tiết và tập trung vào bức tranh lớn"* (tr. 36).

Skiena liệt kê các **bậc hàm** hay gặp (tr. 39), từ chậm tăng tới nhanh tăng:

| Big-O | Tên | Xuất hiện ở | Ví dụ bài |
| :-- | :-- | :-- | :-- |
| `O(1)` | hằng | đọc một phần tử mảng | truy cập mảng (Bài 2) |
| `O(log n)` | logarit | tìm nhị phân | B+tree, heap (Bài 4–5) |
| `O(n)` | tuyến tính | quét từng phần tử một lần | duyệt, tìm tuyến tính |
| `O(n log n)` | siêu tuyến *(superlinear)* | quicksort, mergesort | sắp xếp (Bài 5) |
| `O(n²)` | bậc hai | nhìn mọi **cặp** phần tử | insertion/selection sort |
| `O(n³)` | bậc ba | mọi **bộ ba** | vài quy hoạch động (Bài 9) |
| `O(2ⁿ)` | mũ | liệt kê mọi **tập con** | backtracking (Bài 10) |
| `O(n!)` | giai thừa | liệt kê mọi **hoán vị** | bài toán khó (Bài 11) |

Điều quan trọng nhất cần thuộc là **thứ tự trội** giữa chúng (Skiena tr. 39):

```
n!  »  2ⁿ  »  n³  »  n²  »  n log n  »  n  »  log n  »  1
   chậm đi tù                                      nhanh như chớp
```

Dấu `»` nghĩa "trội hơn hẳn khi `n` đủ lớn". Một thuật toán `O(n log n)` **luôn** thắng một `O(n²)` nếu `n` đủ lớn, bất kể hằng số. Demo mục 5 cho thấy khoảng cách đó bằng số thật.

## 5. Demo: đếm thao tác thật theo từng bậc

Demo cài **năm** hàm thuộc năm bậc, **đếm thao tác thật** (không dùng công thức), rồi cho `n` chạy 10 → 100 → 1000 để thấy số bước bung ra theo bậc. Cuối cùng đo worst vs best case của tìm tuyến tính.

```typescript
import { strict as assert } from "node:assert";

// Đếm thao tác THẬT (không dùng công thức) của 5 bậc độ lớn, khi n tăng ×10.
// Mỗi hàm trả về số "thao tác cơ bản" theo mô hình RAM (mỗi phép = 1 bước).

// O(1): nhìn một phần tử, bất kể n.
function constant(arr: number[]): number {
  return 1; // đọc arr[0] — một thao tác
}

// O(log n): tìm nhị phân worst-case (phần tử không có) — đếm số lần lặp.
function logarithmic(arr: number[]): number {
  let lo = 0, hi = arr.length - 1, steps = 0;
  const target = Infinity; // không bao giờ thấy → đi hết chiều sâu
  while (lo <= hi) {
    steps++;
    const mid = (lo + hi) >> 1;
    if (arr[mid] < target) lo = mid + 1;
    else hi = mid - 1;
  }
  return steps;
}

// O(n): quét từng phần tử một lần (tính tổng).
function linear(arr: number[]): number {
  let ops = 0, sum = 0;
  for (const x of arr) { sum += x; ops++; }
  return ops;
}

// O(n log n): mergesort, đếm số lần SO SÁNH khi trộn.
function linearithmic(arr: number[]): number {
  let cmp = 0;
  function sort(a: number[]): number[] {
    if (a.length <= 1) return a;
    const mid = a.length >> 1;
    const left = sort(a.slice(0, mid));
    const right = sort(a.slice(mid));
    const merged: number[] = [];
    let i = 0, j = 0;
    while (i < left.length && j < right.length) {
      cmp++;                              // một so sánh
      if (left[i] <= right[j]) merged.push(left[i++]);
      else merged.push(right[j++]);
    }
    while (i < left.length) merged.push(left[i++]);
    while (j < right.length) merged.push(right[j++]);
    return merged;
  }
  sort(arr);
  return cmp;
}

// O(n^2): nhìn MỌI cặp phần tử (đếm số cặp so sánh).
function quadratic(arr: number[]): number {
  let ops = 0;
  for (let i = 0; i < arr.length; i++)
    for (let j = i + 1; j < arr.length; j++) ops++;
  return ops;
}

const classes: Array<[string, (a: number[]) => number]> = [
  ["O(1)      hằng", constant],
  ["O(log n)  log ", logarithmic],
  ["O(n)      tuyến tính", linear],
  ["O(n log n) siêu tuyến", linearithmic],
  ["O(n^2)    bậc hai", quadratic],
];
const sizes = [10, 100, 1000];

console.log("SỐ THAO TÁC THEO BẬC ĐỘ LỚN (mô hình RAM: mỗi phép = 1 bước):");
console.log("bậc".padEnd(22) + sizes.map((n) => `n=${n}`.padStart(10)).join(""));
const table: Record<string, number[]> = {};
for (const [name, fn] of classes) {
  const row = sizes.map((n) => fn(Array.from({ length: n }, (_, i) => i)));
  table[name] = row;
  console.log(name.padEnd(22) + row.map((v) => String(v).padStart(10)).join(""));
}

console.log("\nKHI n TĂNG ×10 (từ 100 lên 1000), số thao tác nhân lên bao nhiêu lần:");
for (const [name] of classes) {
  const [, a, b] = table[name];
  const factor = a === 0 ? 1 : b / a;
  console.log(`  ${name.padEnd(22)} ×${factor.toFixed(2).padStart(8)}`);
}

// Kiểm: bậc hai nhân ~100 lần, tuyến tính ~10 lần khi n ×10 — đúng lý thuyết.
assert.ok(table["O(n^2)    bậc hai"][2] / table["O(n^2)    bậc hai"][1] > 95);
assert.equal(table["O(n)      tuyến tính"][2] / table["O(n)      tuyến tính"][1], 10);
// log n chỉ tăng thêm vài bước; hằng số đứng yên.
assert.equal(table["O(1)      hằng"][0], table["O(1)      hằng"][2]);

// ─── WORST vs BEST vs AVERAGE: tìm tuyến tính trên n=1000 ───
function linearSearchSteps(arr: number[], target: number): number {
  let steps = 0;
  for (const x of arr) { steps++; if (x === target) break; }
  return steps;
}
const big = Array.from({ length: 1000 }, (_, i) => i);
const best = linearSearchSteps(big, 0);        // ngay phần tử đầu
const worst = linearSearchSteps(big, -1);      // không có → quét hết
console.log("\nWORST vs BEST (tìm tuyến tính, n=1000):");
console.log(`  best case  (phần tử đầu) = ${best} bước`);
console.log(`  worst case (không có)    = ${worst} bước  ← Big-O lấy mốc này`);
assert.equal(best, 1);
assert.equal(worst, 1000);

console.log("\nBig-O bỏ qua hằng số, chỉ giữ bậc trội: n! » 2^n » n^3 » n^2 » n log n » n » log n » 1.");
```

Kết quả chạy thật *(tất định)*:

```
SỐ THAO TÁC THEO BẬC ĐỘ LỚN (mô hình RAM: mỗi phép = 1 bước):
bậc                         n=10     n=100    n=1000
O(1)      hằng                 1         1         1
O(log n)  log                  4         7        10
O(n)      tuyến tính          10       100      1000
O(n log n) siêu tuyến         15       316      4932
O(n^2)    bậc hai             45      4950    499500

KHI n TĂNG ×10 (từ 100 lên 1000), số thao tác nhân lên bao nhiêu lần:
  O(1)      hằng         ×    1.00
  O(log n)  log          ×    1.43
  O(n)      tuyến tính   ×   10.00
  O(n log n) siêu tuyến  ×   15.61
  O(n^2)    bậc hai      ×  100.91

WORST vs BEST (tìm tuyến tính, n=1000):
  best case  (phần tử đầu) = 1 bước
  worst case (không có)    = 1000 bước  ← Big-O lấy mốc này

Big-O bỏ qua hằng số, chỉ giữ bậc trội: n! » 2^n » n^3 » n^2 » n log n » n » log n » 1.
```

Đọc bảng là thấy toàn bộ tinh thần Big-O — bốn điều đáng thấm. **(1) Bậc quyết định tất cả khi `n` lớn:** `O(1)` đứng yên ở 1; `O(log n)` bò từ 4 lên 10; còn `O(n²)` bay từ 45 lên gần **nửa triệu**. **(2) Hệ số nhân phơi bày bậc:** `n` ×10 thì tuyến tính ×10 (đúng 10,00), bậc hai ×~100 (100,91), log chỉ ×1,43 — con số nhân *chính là* bậc độ lớn hiện hình. **(3) `n log n` ở giữa:** nhân ~15,6 lần — nhỉnh hơn tuyến tính một chút nhưng cách bậc hai cả vực; đây là lý do mergesort/quicksort được coi là "đủ nhanh" còn insertion sort O(n²) thì không, cho dữ liệu lớn (Bài 5). **(4) Worst case là lời hứa:** tìm tuyến tính may thì 1 bước, xui thì 1000 — Big-O lấy mốc 1000 để hứa "không bao giờ tệ hơn".

> [!note] Tự thử
> 1. Thêm bậc `O(n³)` (ba vòng lặp lồng): với `n` ×10, hệ số nhân sẽ là bao nhiêu? Đoán trước rồi kiểm.
> 2. `linearithmic` đếm so sánh mergesort ra 4932 ở `n=1000`. So với `n·log₂n = 1000 × 9,97 ≈ 9966` — vì sao số thật *nhỏ hơn* ước lượng trên? (Gợi ý: mỗi lần trộn thường dừng sớm khi một nửa hết trước.)
> 3. Đổi best case của tìm tuyến tính: nếu phần tử cần tìm luôn nằm *giữa* mảng, số bước worst/best/average liên hệ ra sao?
> 4. Vì sao `O(2ⁿ)` với `n=60` đã là con số lớn hơn số giây từ khi vũ trụ ra đời? Tính `2⁶⁰` và so.

## 6. Bản đồ khoá DSA

| # | Bài | Chủ đề | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | Thuật toán & tính đúng | nền: đúng vs hiệu quả | Skiena Ch1 + Grokking |
| 1 | **Phân tích Big-O** ← *đang ở đây* | đo chi phí khi `n` lớn | Skiena Ch2 |
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
| 13 | *(nâng cao)* Luồng mạng | max-flow / min-cut | Skiena §8.5 + CLRS Ch24 |
| 14 | *(nâng cao)* Thuật toán ngẫu nhiên | randomized quicksort, Monte Carlo | Skiena Ch6 |

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 1.1 — Vì sao không đo hiệu quả thuật toán bằng cách bấm giây?
> **Đáp:** giây phụ thuộc máy, ngôn ngữ, `n` cụ thể, tải lúc chạy — không độc lập và không trả lời được "khi `n` lớn gấp nghìn thì sao". Ta đếm bước độc lập máy (mô hình RAM) thay vì đo giây.

> [!question] Thẻ 1.2 — Mô hình RAM giả định gì?
> **Đáp:** mỗi thao tác đơn (+, *, =, if, call) và mỗi lần truy cập bộ nhớ tốn **đúng 1 bước**; bộ nhớ vô hạn; không phân biệt cache/đĩa. Vòng lặp/hàm con là tổng nhiều bước (Skiena tr. 31).

> [!question] Thẻ 1.3 — Worst / best / average case là gì? Thường dùng cái nào, vì sao?
> **Đáp:** số bước tối đa / tối thiểu / trung bình trên mọi đầu vào cỡ `n`. Dùng **worst case** vì nó cho lời hứa chắc chắn "không bao giờ chậm hơn", không cần giả định phân bố đầu vào (Skiena tr. 33).

> [!question] Thẻ 1.4 — Big-O làm gì với `2n² + 3n + 7`? Vì sao được phép?
> **Đáp:** rút thành **O(n²)** — bỏ hằng số và số hạng bậc thấp, giữ bậc trội. Được phép vì khi `n` lớn, bậc trội nuốt mọi thứ còn lại và quyết định ai thắng (Skiena tr. 36).

> [!question] Thẻ 1.5 — Sắp các bậc từ nhanh-tăng tới chậm-tăng.
> **Đáp:** `n! » 2ⁿ » n³ » n² » n log n » n » log n » 1`. `O(n log n)` luôn thắng `O(n²)` khi `n` đủ lớn, bất kể hằng số (Skiena tr. 39).

## 8. Câu hỏi tự kiểm tra

1. Một đồng nghiệp nói "thuật toán tôi chạy 0,3 giây, nhanh hơn của bạn". Bạn phản biện thế nào bằng ngôn ngữ Big-O? *(mục 1)*
2. Trong mô hình RAM, vì sao `sort(arr)` *không* được tính là một bước, còn `arr[i]` thì có? *(mục 2)*
3. Giải thích vì sao worst case hữu dụng hơn average case trong thực tế, dù nghe phản trực giác. *(mục 3)*
4. Rút gọn các biểu thức sau về Big-O: `100n + 5`; `n²/2 + n`; `3·2ⁿ + n¹⁰⁰`. *(mục 4)*
5. Chạy demo mục 5. Khi `n` ×10, vì sao hệ số nhân của bậc hai xấp xỉ 100 còn tuyến tính đúng 10? *(mục 4 & 5)*

## Tóm tắt một trang

```
BÀI 1 — PHÂN TÍCH BIG-O
─────────────────────────────────────────────────────────
VẤN ĐỀ  bấm giây để so thuật toán là SAI: phụ thuộc máy/ngôn ngữ/n/tải. Cần
   thước độc lập máy, trả lời "khi n lớn gấp nghìn thì sao".

MÔ HÌNH RAM  mỗi thao tác đơn + mỗi truy cập bộ nhớ = 1 bước; bộ nhớ vô hạn;
   kệ cache/đĩa (Skiena tr.31). Đếm BƯỚC thay vì đo GIÂY. Vòng lặp = tổng bước.

WORST/BEST/AVERAGE  số bước tối đa/tối thiểu/trung bình trên mọi đầu vào cỡ n.
   Dùng WORST CASE — lời hứa "không bao giờ chậm hơn", khỏi giả định phân bố
   (Skiena tr.33).

BIG-O  bỏ hằng số + số hạng bậc thấp, giữ BẬC TRỘI. 2n²+3n+7 → O(n²). Vì khi
   n lớn bậc trội nuốt tất cả (Skiena tr.36).

THỨ TỰ TRỘI  n! » 2ⁿ » n³ » n² » n log n » n » log n » 1 (Skiena tr.39).
   O(n log n) luôn thắng O(n²) khi n đủ lớn, bất kể hằng số.

DEMO  n ×10 → tuyến tính ×10, bậc hai ×~100, log ×1,4. Hệ số nhân CHÍNH LÀ
   bậc hiện hình. Tìm tuyến tính: best 1 bước, worst 1000 — Big-O lấy worst.
```

## Nguồn

- **Skiena, Steven S. — *The Algorithm Design Manual*, 3rd ed.** (Springer, 2020) — **Chapter 2: Algorithm Analysis**: mô hình RAM (§2.1), worst/best/average case, ký hiệu Big Oh (§2.2–2.4), các bậc hàm thường gặp & quan hệ trội (§2.3, tr. 39). `tai_lieu/The Algorithm Design Manual 3rd Edition...pdf` (offset **PDF = tr. + 17**).
- Liên hệ: [cloud-base — phân cấp lưu trữ](../../cloud-base/README.md) và [database — buffer manager](../../database/README.md) cho thấy chỗ mô hình RAM "nói dối" (cache/đĩa *không* cùng chi phí) nhưng vẫn hữu ích để ước lượng xu hướng.

---

**Bản đồ khoá học:** [Bài 0 — Thuật toán & tính đúng](bai_00_thuat-toan-la-gi.md) · **[Bài 1 — Phân tích Big-O] ← bạn đang ở đây** · [Bài 2 — CTDL tuyến tính](bai_02_ctdl-tuyen-tinh.md) · [Bài 3 — Từ điển & bảng băm](bai_03_bang-bam.md) · [Bài 4 — Heap & cây tìm kiếm](bai_04_heap-cay-tim-kiem.md) · [Bài 5 — Sắp xếp](bai_05_sap-xep.md) · [Bài 6 — Chia để trị & đệ quy](bai_06_chia-de-tri.md) · [Bài 7 — Đồ thị: duyệt](bai_07_do-thi-duyet.md) · [Bài 8 — Đồ thị trọng số](bai_08_do-thi-trong-so.md) · [Bài 9 — Quy hoạch động](bai_09_quy-hoach-dong.md) · [Bài 10 — Backtracking](bai_10_backtracking.md) · [Bài 11 — NP-đầy đủ](bai_11_np-day-du.md) · [Bài 12 — Khớp chuỗi](bai_12_khop-chuoi.md) · [Bài 13 — Luồng mạng](bai_13_luong-mang.md) · [Bài 14 — Thuật toán ngẫu nhiên](bai_14_ngau-nhien.md)

Xem thêm [README khoá học](../README.md).
