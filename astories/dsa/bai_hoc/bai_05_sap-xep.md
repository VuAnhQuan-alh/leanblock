# Bài 5 — Sắp xếp: mergesort, quicksort, heapsort

> [!info] Về bài này
> Sắp xếp là bài toán được nghiên cứu kỹ nhất trong khoa học máy tính, và là *viên gạch nền* mà vô số thuật toán khác dựng lên trên. Bài này mổ ba thuật toán `O(n log n)` kinh điển — **mergesort** (chia để trị), **quicksort** (phân hoạch ngẫu nhiên), **heapsort** (dùng heap Bài 4) — cho thấy chúng *cùng* ra một kết quả nhưng *khác* nhau về chi phí và điểm mạnh/yếu, và vì sao `O(n log n)` là **cận dưới** không vượt qua được của mọi thuật toán sắp xếp bằng so sánh.
> Nguồn (Luật số 1): **Skiena** *The Algorithm Design Manual 3e* — **Chapter 4: Sorting** (§4.1, §4.3 Heapsort, §4.5 Mergesort, §4.6 Quicksort) (`tai_lieu/`, trích `> [!quote] Skiena (tr. N)`, **PDF = tr. + 16** ở Ch4).
> **Chạy demo:** `node bai_05.ts` — Node 22+, không cài gói. Code tất định.
> Cần đọc trước: [Bài 1 — Big-O](bai_01_big-o.md), [Bài 4 — Heap & cây tìm kiếm](bai_04_heap-cay-tim-kiem.md) (heapsort dùng heap).

## Mục lục

1. [Tình huống: vì sao sắp xếp đáng học ba lần](#1-tình-huống-vì-sao-sắp-xếp-đáng-học-ba-lần)
2. [Mergesort: chia đôi rồi trộn](#2-mergesort-chia-đôi-rồi-trộn)
3. [Quicksort: phân hoạch quanh pivot](#3-quicksort-phân-hoạch-quanh-pivot)
4. [Heapsort và cận dưới n log n](#4-heapsort-và-cận-dưới-n-log-n)
5. [Demo: ba thuật toán, một kết quả, chi phí khác nhau](#5-demo-ba-thuật-toán-một-kết-quả-chi-phí-khác-nhau)
6. [Bản đồ khoá DSA](#6-bản-đồ-khoá-dsa)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Tình huống: vì sao sắp xếp đáng học ba lần

> [!example] Sắp xong là nửa bài toán xong
> Rất nhiều bài toán *tự nhiên dễ* khi dữ liệu đã sắp: tìm phần tử (nhị phân, Bài 0), tìm trùng lặp (phần tử bằng nhau nằm cạnh nhau), tìm trung vị, gộp hai danh sách... Mẹo chung của dân thuật toán: gặp bài khó, thử **sắp xếp trước** rồi xem bài có sập thành dễ không.

Skiena dành cả một chương cho sắp xếp vì nó vừa là công cụ vừa là nơi hội tụ mọi ý tưởng thiết kế thuật toán:

> [!quote] Skiena (tr. 109)
> "Sorting is the basic building block that many other algorithms are built around. By understanding sorting, we obtain an amazing amount of power to solve other problems."
>
> *Sắp xếp là **viên gạch nền** mà nhiều thuật toán khác dựng quanh. Hiểu sắp xếp, ta có được **sức mạnh đáng kinh ngạc** để giải những bài toán khác.*

Và điểm chốt của cả chương là một con số:

> [!quote] Skiena (tr. 109)
> "clever sorting algorithms exist that run in O(n log n)."
>
> *tồn tại những thuật toán sắp xếp **khéo** chạy trong **O(n log n)**.*

So với sắp xếp ngây thơ `O(n²)` (insertion/selection sort — Bài 1), `O(n log n)` là khác biệt một trời một vực khi `n` lớn (Bài 1 đã thấy: `n` ×10 thì bậc hai ×100 còn `n log n` chỉ ×~15). Ba thuật toán dưới đây đều đạt mốc `O(n log n)` đó, bằng ba ý tưởng khác nhau.

## 2. Mergesort: chia đôi rồi trộn

**Mergesort** là ví dụ sạch nhất của **chia để trị** (Bài 6 đào sâu): chia mảng làm đôi, **sắp mỗi nửa** (đệ quy), rồi **trộn** hai nửa đã sắp thành một.

Phép trộn là trái tim: hai danh sách đã sắp, phần tử nhỏ nhất toàn cục luôn nằm ở *đầu một trong hai*; lấy nó ra, lặp lại → trộn `n` phần tử tốn `n − 1` so sánh, tức `O(n)`.

```
          [9 3 14 1 | 7 12 5 16]        chia đôi tới khi còn 1 phần tử
         /                     \
    [9 3 | 14 1]           [7 12 | 5 16]
      ↓ sắp mỗi nửa rồi TRỘN ngược lên
    [1 3 9 14]            [5 7 12 16]
         \                     /
          [1 3 5 7 9 12 14 16]           mỗi tầng trộn tốn O(n); có log n tầng
```

Cây đệ quy sâu `log₂ n` tầng, mỗi tầng làm `O(n)` công trộn:

> [!quote] Skiena (tr. 128)
> "goes lg n levels deep, and a linear amount of work is done per level, mergesort takes O(n log n) time in the worst case."
>
> *[cây đệ quy] đi sâu `lg n` tầng, và mỗi tầng làm một lượng công tuyến tính, nên mergesort tốn **O(n log n)** ở trường hợp xấu nhất.*

Điểm mạnh riêng: mergesort là `O(n log n)` **worst case bất kể đầu vào** (không có ca xui), và **ổn định** (giữ thứ tự tương đối các khoá bằng nhau). Nó cũng hợp sắp **danh sách liên kết** (Bài 2) và dữ liệu lớn hơn RAM (external sort — chính là [sort-merge join của database](../../database/README.md)). Giá phải trả: cần `O(n)` bộ nhớ phụ cho mảng trộn.

## 3. Quicksort: phân hoạch quanh pivot

**Quicksort** cũng chia để trị nhưng theo chiều ngược: làm việc khó (**phân hoạch**) *trước*, rồi đệ quy mà không cần trộn. Chọn một **pivot**, dồn mọi phần tử nhỏ hơn pivot sang trái, lớn hơn sang phải — giờ pivot đã *đúng chỗ cuối cùng*; đệ quy sắp hai bên.

Phân hoạch tốn `O(n)` mỗi tầng (như mergesort), nên tổng chi phí phụ thuộc **chiều cao cây đệ quy**:

> [!quote] Skiena (tr. 131)
> "As with mergesort, quicksort runs in O(n · h) time, where h is the height of the recursion tree."
>
> *Như mergesort, quicksort chạy trong **O(n · h)**, với `h` là **chiều cao cây đệ quy**.*

Và `h` tuỳ pivot chia khéo hay lệch — đúng câu chuyện chiều cao của BST ở Bài 4:

- Pivot chia **đôi đều** mỗi lần → `h = log n` → `O(n log n)`. Đây là ca may và cũng là ca *trung bình*.
- Pivot luôn **lệch tối đa** (luôn là max hoặc min) → `h = n` → **O(n²)**. Ca xui kinh điển: mảng **đã sắp sẵn** mà lại chọn pivot là phần tử cuối (demo mục 5).

> [!quote] Skiena (tr. 132)
> "the worst case for quicksort is worse than heapsort or mergesort. To justify its name, quicksort had better be good in the average case."
>
> *worst case của quicksort **tệ hơn** heapsort hay mergesort. Để xứng cái tên, quicksort **tốt nhất là nên** chạy tốt ở trường hợp trung bình.*

Và nó đúng là tốt — mẹo cứu là **chọn pivot ngẫu nhiên** (hoặc xáo mảng trước), biến "ca xui" thành gần như không thể xảy ra:

> [!quote] Skiena (tr. 134)
> "Randomized quicksort runs in Θ(n log n) time on any input, with high probability."
>
> *Quicksort **ngẫu nhiên hoá** chạy trong **Θ(n log n)** trên *mọi* đầu vào, với **xác suất cao**.*

Dù worst case `O(n²)`, quicksort thường **nhanh nhất thực tế** vì phân hoạch tại chỗ, hằng số nhỏ, thân thiện với cache (Bài 2 — locality). Đây là lý do thư viện chuẩn của nhiều ngôn ngữ dùng biến thể quicksort. Ta gặp lại tư tưởng ngẫu nhiên hoá ở [Bài 14](bai_14_ngau-nhien.md).

## 4. Heapsort và cận dưới n log n

**Heapsort** đã gặp ở [Bài 4](bai_04_heap-cay-tim-kiem.md): nhét hết `n` phần tử vào heap rồi rút phần tử trội (min/max) ra liên tục. Dựng heap + `n` lần rút, mỗi lần `O(log n)` → `O(n log n)` **worst case bất kể đầu vào** (như mergesort), và sắp **tại chỗ** không cần `O(n)` bộ nhớ phụ (hơn mergesort). Giá phải trả: nhảy khắp mảng theo chỉ số `2i+1`/`2i+2` nên cache kém hơn quicksort, thường chậm hơn thực tế dù cùng bậc.

Cả ba đạt `O(n log n)`. Có cách nào nhanh hơn không? **Không** — với sắp xếp dựa trên **so sánh** khoá:

> [!note] Cận dưới Ω(n log n) cho sắp xếp bằng so sánh
> Mỗi phép so sánh "a < b?" cho 1 bit thông tin. Có `n!` hoán vị khả dĩ của đầu vào, nên để phân biệt được hết ta cần ít nhất `log₂(n!) ≈ n log₂ n` phép so sánh (công thức Stirling). Vì vậy **không** thuật toán sắp-xếp-bằng-so-sánh nào thắng được `Ω(n log n)` ở worst case — mergesort/heapsort đã *chạm đáy* lý thuyết. (Muốn nhanh hơn phải *không* so sánh, như distribution/radix sort dùng giá trị khoá trực tiếp — Skiena §4.7.)

Bảng tổng kết ba thuật toán:

| Thuật toán | Worst case | Trung bình | Bộ nhớ phụ | Ổn định | Điểm mạnh riêng |
| :-- | :-- | :-- | :-- | :-- | :-- |
| **mergesort** | O(n log n) | O(n log n) | O(n) | có | worst-case vững, hợp list & external sort |
| **quicksort** | O(n²) | O(n log n) | O(log n) | không | nhanh nhất thực tế (tại chỗ, cache tốt) |
| **heapsort** | O(n log n) | O(n log n) | O(1) | không | worst-case vững + tại chỗ |

## 5. Demo: ba thuật toán, một kết quả, chi phí khác nhau

Demo cài cả ba (đếm **số lần so sánh** — thước tất định độc lập máy, Bài 1), sắp cùng một mảng 16 phần tử → cùng kết quả, khác chi phí. Rồi dựng **bẫy worst-case**: quicksort pivot-cuối trên mảng *đã sắp* nổ lên `O(n²)`, còn mergesort đứng yên `O(n log n)`.

```typescript
import { strict as assert } from "node:assert";

// Mỗi sort trả về mảng đã sắp + SỐ LẦN SO SÁNH khoá (thước đo tất định, độc máy).

// ─── MERGESORT: chia đôi, sắp mỗi nửa, rồi TRỘN. Worst case O(n log n) ───
function mergeSort(arr: number[]): { sorted: number[]; cmp: number } {
  let cmp = 0;
  function sort(a: number[]): number[] {
    if (a.length <= 1) return a;
    const mid = a.length >> 1;
    const left = sort(a.slice(0, mid));
    const right = sort(a.slice(mid));
    const out: number[] = [];
    let i = 0, j = 0;
    while (i < left.length && j < right.length) {
      cmp++;
      if (left[i] <= right[j]) out.push(left[i++]);
      else out.push(right[j++]);
    }
    while (i < left.length) out.push(left[i++]);
    while (j < right.length) out.push(right[j++]);
    return out;
  }
  return { sorted: sort(arr), cmp };
}

// ─── QUICKSORT: chọn PIVOT (phần tử cuối), phân hoạch quanh nó rồi đệ quy ───
// Worst case O(n^2) khi pivot luôn lệch (vd mảng đã sắp + pivot cuối).
function quickSort(input: number[]): { sorted: number[]; cmp: number } {
  const a = [...input];
  let cmp = 0;
  function partition(lo: number, hi: number): number {
    const pivot = a[hi];              // chọn phần tử cuối làm pivot
    let firstHigh = lo;
    for (let i = lo; i < hi; i++) {
      cmp++;
      if (a[i] < pivot) { [a[i], a[firstHigh]] = [a[firstHigh], a[i]]; firstHigh++; }
    }
    [a[hi], a[firstHigh]] = [a[firstHigh], a[hi]];
    return firstHigh;
  }
  function sort(lo: number, hi: number): void {
    if (lo >= hi) return;
    const p = partition(lo, hi);
    sort(lo, p - 1);
    sort(p + 1, hi);
  }
  sort(0, a.length - 1);
  return { sorted: a, cmp };
}

// ─── HEAPSORT: dựng MAX-HEAP tại chỗ rồi rút gốc về cuối dần. Worst case O(n log n) ───
function heapSort(input: number[]): { sorted: number[]; cmp: number } {
  const a = [...input];
  let cmp = 0;
  const n = a.length;
  function siftDown(root: number, size: number): void {
    while (true) {
      const l = 2 * root + 1, r = 2 * root + 2;
      let largest = root;
      if (l < size) { cmp++; if (a[l] > a[largest]) largest = l; }
      if (r < size) { cmp++; if (a[r] > a[largest]) largest = r; }
      if (largest === root) break;
      [a[root], a[largest]] = [a[largest], a[root]];
      root = largest;
    }
  }
  for (let i = (n >> 1) - 1; i >= 0; i--) siftDown(i, n);      // dựng heap
  for (let end = n - 1; end > 0; end--) {                      // rút max về cuối
    [a[0], a[end]] = [a[end], a[0]];
    siftDown(0, end);
  }
  return { sorted: a, cmp };
}

// Mảng "ngẫu nhiên" cố định (hoán vị 1..16) — tất định giữa các lần chạy.
const data = [9, 3, 14, 1, 7, 12, 5, 16, 2, 11, 8, 6, 15, 4, 13, 10];
const want = [...data].sort((x, y) => x - y);

const results = {
  mergesort: mergeSort(data),
  quicksort: quickSort(data),
  heapsort: heapSort(data),
};
console.log(`SẮP XẾP cùng mảng ${data.length} phần tử — đếm số lần so sánh:`);
for (const [name, r] of Object.entries(results)) {
  console.log(`  ${name.padEnd(10)} ${String(r.cmp).padStart(3)} so sánh   kết quả đúng: ${JSON.stringify(r.sorted) === JSON.stringify(want)}`);
  assert.deepEqual(r.sorted, want);        // cả ba PHẢI ra cùng kết quả đúng
}

// ─── BẪY worst-case: quicksort (pivot cuối) trên mảng ĐÃ SẮP → O(n^2) ───
const sortedInput = Array.from({ length: 16 }, (_, i) => i + 1);  // 1..16, đã sắp
const qsWorst = quickSort(sortedInput);
const msWorst = mergeSort(sortedInput);
console.log("\nBẪY worst-case trên mảng ĐÃ SẮP (16 phần tử):");
console.log(`  quicksort (pivot cuối) = ${qsWorst.cmp} so sánh  ← n(n-1)/2 = ${16 * 15 / 2}, suy biến O(n^2)`);
console.log(`  mergesort              = ${msWorst.cmp} so sánh  ← vẫn O(n log n), bất kể đầu vào`);
assert.equal(qsWorst.cmp, 16 * 15 / 2);    // 120: mỗi phân hoạch lệch tối đa
assert.ok(qsWorst.cmp > 3 * msWorst.cmp);

console.log("\nBa sort đều O(n log n) worst-case TRỪ quicksort O(n^2) worst — nhưng quicksort");
console.log("thường nhanh nhất thực tế; cận dưới mọi sort-so-sánh là Ω(n log n).");
```

Kết quả chạy thật *(tất định)*:

```
SẮP XẾP cùng mảng 16 phần tử — đếm số lần so sánh:
  mergesort   48 so sánh   kết quả đúng: true
  quicksort   42 so sánh   kết quả đúng: true
  heapsort    80 so sánh   kết quả đúng: true

BẪY worst-case trên mảng ĐÃ SẮP (16 phần tử):
  quicksort (pivot cuối) = 120 so sánh  ← n(n-1)/2 = 120, suy biến O(n^2)
  mergesort              = 32 so sánh  ← vẫn O(n log n), bất kể đầu vào

Ba sort đều O(n log n) worst-case TRỪ quicksort O(n^2) worst — nhưng quicksort
thường nhanh nhất thực tế; cận dưới mọi sort-so-sánh là Ω(n log n).
```

Bốn điều đáng thấm. **(1) Cùng kết quả, khác chi phí:** cả ba nhả ra `1..16` y hệt (tính đúng, Bài 0) nhưng tốn 48 / 42 / 80 so sánh — chọn thuật toán là chọn *hằng số và điểm mạnh*, không chỉ bậc. **(2) Quicksort thắng ở ca thường:** 42 so sánh, ít hơn cả mergesort — đúng lý do thực tế hay chọn nó, dù lý thuyết worst-case tệ hơn. **(3) Bẫy worst-case là thật và nguy hiểm:** đúng mảng *đã sắp* (tình huống rất hay gặp!) mà pivot-cuối làm quicksort nổ lên 120 so sánh (`n(n−1)/2`, bậc hai) trong khi mergesort đứng yên 32 — đây là lý do phải **ngẫu nhiên hoá pivot**. **(4) Mergesort không có ca xui:** 48 so sánh ở input ngẫu nhiên, 32 ở input đã sắp — luôn `O(n log n)`.

> [!note] Tự thử
> 1. Sửa `quickSort` chọn pivot **ngẫu nhiên** (hoán đổi `a[hi]` với một chỉ số ngẫu nhiên trong `[lo, hi]` trước khi phân hoạch). Chạy lại bẫy worst-case — số so sánh trên mảng đã sắp giờ ra sao? (Lưu ý: output hết tất định vì có ngẫu nhiên — chỉ quan sát, đừng đưa vào fence kết quả.)
> 2. Vì sao mergesort `≤` (dùng `<=` khi trộn) giữ được **tính ổn định** còn nếu đổi thành `<` thì mất? Ổn định quan trọng khi nào?
> 3. Heapsort tốn 80 so sánh — nhiều nhất trong ba. Vì sao nó vẫn được dùng (gợi ý: bộ nhớ phụ `O(1)` + worst-case vững)?
> 4. Cận dưới `Ω(n log n)` chỉ áp cho sắp-xếp-bằng-so-sánh. Radix sort sắp số nguyên trong `O(n)` — nó "lách" bằng cách nào? *(mục 4)*

## 6. Bản đồ khoá DSA

| # | Bài | Chủ đề | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | Thuật toán & tính đúng | nền: đúng vs hiệu quả | Skiena Ch1 + Grokking |
| 1 | Phân tích Big-O | đo chi phí khi `n` lớn | Skiena Ch2 |
| 2 | CTDL tuyến tính | mảng / list / stack / queue | Skiena Ch3 |
| 3 | Từ điển & bảng băm | tra cứu O(1) trung bình | Skiena Ch3 |
| 4 | Heap & cây tìm kiếm | lấy min/max, tra có thứ tự | Skiena Ch3–4 |
| 5 | **Sắp xếp** ← *đang ở đây* | quicksort / mergesort / heapsort | Skiena Ch4 |
| 6 | Chia để trị & đệ quy | bẻ nhỏ bài toán, master theorem | Skiena Ch5 |
| 7 | Đồ thị: biểu diễn & duyệt | BFS / DFS | Skiena Ch7 |
| 8 | Đồ thị trọng số: MST & đường ngắn nhất | Dijkstra / Prim / Kruskal | Skiena Ch8 |
| 9 | Quy hoạch động | tối ưu bằng bảng con | Skiena Ch10 |
| 10 | Tìm kiếm tổ hợp & backtracking | duyệt không gian lời giải | Skiena Ch9 |
| 11 | NP-đầy đủ & bài toán khó | khi không có lời giải nhanh | Skiena Ch11–12 |
| 12 | *(nâng cao)* Khớp chuỗi | KMP / Rabin–Karp | Skiena §6.7 + CLRS Ch32 |
| 13 | *(nâng cao)* Luồng mạng | max-flow / min-cut | Skiena §8.5 + CLRS Ch24 |
| 14 | *(nâng cao)* Thuật toán ngẫu nhiên | randomized quicksort, Monte Carlo | Skiena Ch6 |

Mergesort là ca mẫu của [Bài 6 — chia để trị](bai_06_chia-de-tri.md); pivot ngẫu nhiên nối sang [Bài 14](bai_14_ngau-nhien.md).

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 5.1 — Vì sao sắp xếp đáng học kỹ đến vậy?
> **Đáp:** là **viên gạch nền** nhiều thuật toán dựng quanh; nhiều bài khó thành dễ sau khi sắp; và là nơi hội tụ các ý tưởng thiết kế (chia để trị, cấu trúc dữ liệu, ngẫu nhiên hoá) (Skiena tr. 109).

> [!question] Thẻ 5.2 — Mergesort hoạt động thế nào? Vì sao O(n log n)?
> **Đáp:** chia đôi → sắp mỗi nửa (đệ quy) → **trộn** hai nửa đã sắp (O(n)). Cây đệ quy sâu `log n` tầng × `O(n)` công/tầng = **O(n log n)** worst case bất kể đầu vào (Skiena tr. 128). Ổn định; cần O(n) bộ nhớ phụ.

> [!question] Thẻ 5.3 — Quicksort chạy O(n·h). h phụ thuộc gì? Khi nào thành O(n²)?
> **Đáp:** `h` = chiều cao cây đệ quy, tuỳ **pivot** chia khéo hay lệch (Skiena tr. 131). Pivot luôn lệch tối đa (vd mảng **đã sắp** + pivot cuối) → `h = n` → **O(n²)** (Skiena tr. 132).

> [!question] Thẻ 5.4 — Quicksort worst case tệ hơn, sao vẫn hay được dùng? Cứu ca xui bằng gì?
> **Đáp:** trung bình O(n log n), hằng số nhỏ, tại chỗ + cache tốt → **thường nhanh nhất thực tế**. Cứu bằng **chọn pivot ngẫu nhiên** → Θ(n log n) trên mọi đầu vào với xác suất cao (Skiena tr. 134).

> [!question] Thẻ 5.5 — Vì sao không sort-bằng-so-sánh nào nhanh hơn Ω(n log n)?
> **Đáp:** cần phân biệt `n!` hoán vị, mỗi so sánh cho 1 bit → cần ≥ `log₂(n!) ≈ n log n` so sánh. Mergesort/heapsort chạm đáy đó. Muốn nhanh hơn phải *không* so sánh (radix/distribution sort).

## 8. Câu hỏi tự kiểm tra

1. Mô tả bước "trộn" của mergesort. Vì sao trộn hai danh sách `n` phần tử chỉ tốn O(n)? *(mục 2)*
2. Giải thích vì sao quicksort trên mảng đã sắp (pivot cuối) lại là O(n²). Ngẫu nhiên hoá cứu thế nào? *(mục 3)*
3. So mergesort / quicksort / heapsort trên: worst case, bộ nhớ phụ, tốc độ thực tế. Khi nào chọn cái nào? *(mục 2–4)*
4. Giải thích cận dưới Ω(n log n) cho sắp-xếp-bằng-so-sánh bằng lập luận `n!` hoán vị. *(mục 4)*
5. Chạy demo mục 5. Vì sao cả ba ra cùng kết quả nhưng số so sánh khác nhau (48/42/80)? *(mục 5)*

## Tóm tắt một trang

```
BÀI 5 — SẮP XẾP
─────────────────────────────────────────────────────────
VÌ SAO  sắp là VIÊN GẠCH NỀN; nhiều bài khó thành dễ sau khi sắp (Skiena tr.109).
   Tồn tại sort O(n log n) — hơn hẳn O(n²) ngây thơ khi n lớn.

MERGESORT  chia đôi → sắp mỗi nửa → TRỘN (O(n)). log n tầng × O(n) = O(n log n)
   worst case BẤT KỂ đầu vào (Skiena tr.128). Ổn định; cần O(n) bộ nhớ phụ. Hợp
   list & external sort (= sort-merge join database).

QUICKSORT  chọn PIVOT, phân hoạch, đệ quy. O(n·h), h = chiều cao cây (Skiena
   tr.131). Pivot đều → log n → O(n log n); pivot lệch (mảng ĐÃ SẮP + pivot
   cuối) → h=n → O(n²) (tr.132). CỨU: pivot NGẪU NHIÊN → Θ(n log n) mọi input
   (tr.134). Thường NHANH NHẤT thực tế (tại chỗ, cache tốt).

HEAPSORT  nhét heap + rút min/max n lần → O(n log n) worst case, TẠI CHỖ O(1)
   bộ nhớ. Cache kém hơn quicksort.

CẬN DƯỚI  mọi sort-BẰNG-SO-SÁNH ≥ Ω(n log n) (phân biệt n! hoán vị, mỗi so
   sánh 1 bit). Nhanh hơn phải KHÔNG so sánh (radix/distribution).

DEMO  16 phần tử: merge 48 / quick 42 / heap 80 so sánh, CÙNG kết quả. Mảng đã
   sắp: quicksort nổ 120 (n(n-1)/2) vs mergesort 32.
```

## Nguồn

- **Skiena, Steven S. — *The Algorithm Design Manual*, 3rd ed.** (Springer, 2020) — **Chapter 4: Sorting** (§4.1 Applications, §4.3 Heapsort, §4.5 Mergesort, §4.6 Quicksort): vì sao sắp xếp quan trọng, mergesort (chia để trị, trộn O(n)), quicksort (phân hoạch, O(n·h), ngẫu nhiên hoá), heapsort, cận dưới so sánh. `tai_lieu/The Algorithm Design Manual 3rd Edition...pdf` (offset **PDF = tr. + 16** ở Ch4).
- Liên hệ: [Bài 4 — heap](bai_04_heap-cay-tim-kiem.md) (nền heapsort); [Bài 6 — chia để trị](bai_06_chia-de-tri.md) (mergesort là ca mẫu); [Bài 14 — ngẫu nhiên](bai_14_ngau-nhien.md) (pivot ngẫu nhiên); [database — sort-merge join](../../database/README.md) (external mergesort).

---

**Bản đồ khoá học:** [Bài 0 — Thuật toán & tính đúng](bai_00_thuat-toan-la-gi.md) · [Bài 1 — Phân tích Big-O](bai_01_big-o.md) · [Bài 2 — CTDL tuyến tính](bai_02_ctdl-tuyen-tinh.md) · [Bài 3 — Từ điển & bảng băm](bai_03_bang-bam.md) · [Bài 4 — Heap & cây tìm kiếm](bai_04_heap-cay-tim-kiem.md) · **[Bài 5 — Sắp xếp] ← bạn đang ở đây** · [Bài 6 — Chia để trị & đệ quy](bai_06_chia-de-tri.md) · [Bài 7 — Đồ thị: duyệt](bai_07_do-thi-duyet.md) · [Bài 8 — Đồ thị trọng số](bai_08_do-thi-trong-so.md) · [Bài 9 — Quy hoạch động](bai_09_quy-hoach-dong.md) · [Bài 10 — Backtracking](bai_10_backtracking.md) · [Bài 11 — NP-đầy đủ](bai_11_np-day-du.md) · [Bài 12 — Khớp chuỗi](bai_12_khop-chuoi.md) · [Bài 13 — Luồng mạng](bai_13_luong-mang.md) · [Bài 14 — Thuật toán ngẫu nhiên](bai_14_ngau-nhien.md)

Xem thêm [README khoá học](../README.md).
