# Bài 14 — Thuật toán ngẫu nhiên: tung xúc xắc để thắng kẻ thù *(nâng cao)*

> [!info] Về bài này
> Bài cuối khoá. Suốt 13 bài, ta lo *worst case* — kẻ thù có thể chọn đầu vào tệ nhất ép thuật toán (quicksort gặp mảng đã sắp, bảng băm gặp khoá dồn một ô). **Thuật toán ngẫu nhiên** *(randomized algorithms)* lật thế cờ: để *chính thuật toán* tung xúc xắc, kẻ thù không còn biết trước ta làm gì nên không ép được ca xấu. Bài này phân biệt hai giống — **Las Vegas** (luôn đúng, thường nhanh) và **Monte Carlo** (luôn nhanh, thường đúng) — và gom lại mọi chỗ khoá này đã *lặng lẽ* dùng ngẫu nhiên: pivot quicksort (Bài 5), bảng băm (Bài 3), Rabin–Karp (Bài 12), min-cut (Bài 13).
> Nguồn (Luật số 1): **Skiena** *The Algorithm Design Manual 3e* — **Chapter 6: Hashing and Randomized Algorithms** (+ §4.6 Quicksort) (`tai_lieu/`, trích `> [!quote] Skiena (tr. N)`, **PDF = tr. + 15** ở Ch6, **+16** ở Ch4).
> **Chạy demo:** `node bai_14.ts` — Node 22+, không cài gói. Demo dùng PRNG **có seed cố định** để output tất định (xem hộp lưu ý).
> Cần đọc trước: [Bài 5 — quicksort](bai_05_sap-xep.md), [Bài 3 — bảng băm](bai_03_bang-bam.md), [Bài 12 — Rabin–Karp](bai_12_khop-chuoi.md).

> [!warning] Ngẫu nhiên thật vs seed cố định
> Thuật toán ngẫu nhiên *thật* lấy số từ nguồn ngẫu nhiên, nên mỗi lần chạy có thể khác. Nhưng khoá này đòi **output tất định** (Luật *"dán output thật"*). Nên demo dùng một **PRNG có seed cố định**: hành vi vẫn *như* ngẫu nhiên (pivot rải đều, điểm gieo đều) mà chạy hai lần ra một kết quả — kiểm chứng được. Trong sản phẩm thật, bạn thay seed cố định bằng nguồn ngẫu nhiên thực.

## Mục lục

1. [Tình huống: kẻ thù ép thuật toán của bạn vào ca xấu nhất](#1-tình-huống-kẻ-thù-ép-thuật-toán-của-bạn-vào-ca-xấu-nhất)
2. [Ngẫu nhiên hoá: lấy đi sức mạnh của kẻ thù](#2-ngẫu-nhiên-hoá-lấy-đi-sức-mạnh-của-kẻ-thù)
3. [Las Vegas và Monte Carlo](#3-las-vegas-và-monte-carlo)
4. [Ứng dụng ngẫu nhiên hoá trong khoá này](#4-ứng-dụng-ngẫu-nhiên-hoá-trong-khoá-này)
5. [Demo: quicksort ngẫu nhiên và ước lượng Monte Carlo](#5-demo-quicksort-ngẫu-nhiên-và-ước-lượng-monte-carlo)
6. [Bản đồ khoá DSA](#6-bản-đồ-khoá-dsa)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Tình huống: kẻ thù ép thuật toán của bạn vào ca xấu nhất

> [!example] Mảng đã sắp — ác mộng của quicksort pivot cố định
> Bài 5 thấy: quicksort chọn pivot là *phần tử cuối* gặp mảng **đã sắp sẵn** thì suy biến `O(n²)`. Tệ hơn, nếu kẻ tấn công *biết* bạn luôn chọn pivot cuối, họ cố tình gửi đúng loại đầu vào đó để làm chậm hệ thống (một kiểu DoS thuật toán). Bảng băm cũng vậy: biết hàm băm, kẻ thù dồn mọi khoá vào một ô (Bài 3). Worst case không còn là xui rủi — nó bị *ép*.

Vấn đề gốc: thuật toán **tất định** luôn xử lý cùng đầu vào theo cùng một cách, nên tồn tại một đầu vào "khắc tinh" cố định. Cách thoát bất ngờ: để thuật toán *tự* tung xúc xắc.

## 2. Ngẫu nhiên hoá: lấy đi sức mạnh của kẻ thù

Nếu quicksort chọn pivot **ngẫu nhiên** (không phải luôn phần tử cuối), thì *không* đầu vào cố định nào ép được ca xấu — vì kẻ thù không biết trước ta sẽ bốc pivot nào. Ca `O(n²)` vẫn *có thể* xảy ra, nhưng chỉ khi xúc xắc xui liên tục, xác suất bé tí; **kỳ vọng** vẫn `O(n log n)` trên *mọi* đầu vào:

> [!quote] Skiena (tr. 134)
> "Randomized quicksort runs in Θ(n log n) time on any input, with high probability."
>
> *Quicksort **ngẫu nhiên hoá** chạy trong **Θ(n log n)** trên **mọi** đầu vào, với **xác suất cao**.*

Khác biệt tinh tế mà quan trọng: quicksort tất định "nhanh *trung bình* trên các đầu vào ngẫu nhiên" — nhưng đầu vào thực *không* ngẫu nhiên, kẻ thù chọn được. Quicksort ngẫu nhiên "nhanh với xác suất cao trên *mỗi* đầu vào cố định" — **ngẫu nhiên nằm ở thuật toán, không ở đầu vào**, nên kẻ thù hết bài. Demo mục 5 đo tận mắt: cùng mảng đã sắp, pivot cố định `2016` so sánh, pivot ngẫu nhiên tụt xuống vài trăm.

## 3. Las Vegas và Monte Carlo

Thuật toán ngẫu nhiên chia hai giống, theo chỗ chúng "hy sinh" sự ngẫu nhiên vào đâu — *thời gian* hay *tính đúng*:

> [!quote] Skiena (tr. 172)
> "Monte Carlo algorithms are always fast and usually correct, while Las Vegas algorithms are always correct and usually fast."
>
> *Thuật toán **Monte Carlo** thì **luôn nhanh** và **thường đúng**, còn thuật toán **Las Vegas** thì **luôn đúng** và **thường nhanh**.*

- **Las Vegas** — kết quả *luôn đúng*, chỉ *thời gian* dao động. Quicksort ngẫu nhiên là ca mẫu:

> [!quote] Skiena (tr. 172)
> "Randomized quicksort always produces a sorted permutation, so we know it is always correct."
>
> *Quicksort ngẫu nhiên **luôn tạo ra một hoán vị đã sắp**, nên ta biết nó **luôn đúng**.*

- **Monte Carlo** — *luôn nhanh* (chạy trong thời gian định trước), nhưng kết quả có *xác suất nhỏ sai* (hoặc chỉ *xấp xỉ*). Ước lượng π bằng gieo điểm, kiểm tra tính nguyên tố Miller–Rabin, đếm phần tử phân biệt bằng minhash — đều Monte Carlo. Đổi lại sự "có thể sai tí", ta được tốc độ và bộ nhớ hằng số cho bài vốn đắt.

```
                   LUÔN ĐÚNG          THƯỜNG ĐÚNG (sai xác suất nhỏ / xấp xỉ)
  LUÔN NHANH         —                 MONTE CARLO (ước π, Miller–Rabin)
  THƯỜNG NHANH   LAS VEGAS             —
                 (quicksort ngẫu nhiên)
```

Chọn giống nào tuỳ: cần đáp án *chắc đúng* mà chịu được thời gian co giãn → Las Vegas; cần *luôn kịp* mà chịu được sai số nhỏ → Monte Carlo (thường kèm "chạy nhiều lần để giảm xác suất sai").

## 4. Ứng dụng ngẫu nhiên hoá trong khoá này

Ngẫu nhiên hoá không phải chủ đề lạ ở cuối khoá — nó đã *chạy ngầm* suốt:

| Bài | Dùng ngẫu nhiên ở đâu | Giống |
| :-- | :-- | :-- |
| [Bài 3](bai_03_bang-bam.md) — bảng băm | hàm băm rải khoá "như ngẫu nhiên" để tránh va chạm | (nền của randomized) |
| [Bài 5](bai_05_sap-xep.md) — quicksort | chọn pivot ngẫu nhiên né worst case mảng-đã-sắp | Las Vegas |
| [Bài 12](bai_12_khop-chuoi.md) — Rabin–Karp | băm cửa sổ, `M` ngẫu nhiên → va chạm giả hiếm | Monte Carlo (có xác minh) |

Skiena xếp cả hashing lẫn randomized vào *cùng một chương* (Ch6) chính vì thế: bảng băm tốt *là* một thuật toán ngẫu nhiên hoá trá hình — nó cược rằng khoá sẽ rải đều, và cược đó gần như luôn thắng. Đây là một trong những ý tưởng thực dụng nhất của cả ngành: **đổi "bảo đảm worst-case" lấy "gần như luôn tốt, và kẻ thù bó tay"**.

> [!note] Khép khoá DSA
> Bạn vừa đi hết 15 bài: từ *đúng vs hiệu quả* (Bài 0) và *Big-O* (Bài 1), qua kho cấu trúc dữ liệu (2–4), sắp xếp & chia để trị (5–6), đồ thị (7–8), các kỹ thuật thiết kế lớn — QHĐ, backtracking (9–10) — ranh giới khả thi NP (11), tới tầng nâng cao: khớp chuỗi, luồng mạng, ngẫu nhiên (12–14). Năm trục xuyên suốt: **đúng** (chứng minh/phản ví dụ), **hiệu quả** (Big-O), **chọn đúng cấu trúc dữ liệu**, **chọn đúng khuôn thiết kế** (chia để trị / tham lam / QHĐ / backtracking / rút gọn), và **biết khi nào một bài là khó**. Xem [README khoá học](../README.md) để ôn toàn cảnh. Bước tiếp theo tự nhiên: luyện tập trên bài thật, và đào sâu CLRS cho phần lý thuyết chặt chẽ.

## 5. Demo: quicksort ngẫu nhiên và ước lượng Monte Carlo

Demo hai phần. **(1) Las Vegas:** quicksort pivot-cuối vs pivot-ngẫu-nhiên trên mảng *đã sắp* (ca xấu nhất của pivot cố định) — cùng ra kết quả đúng, nhưng ngẫu nhiên cắt số so sánh mạnh. **(2) Monte Carlo:** ước lượng π bằng gieo điểm — càng nhiều mẫu càng sát. Cả hai dùng PRNG seed cố định nên tất định.

```typescript
import { strict as assert } from "node:assert";

// ─── PRNG CÓ SEED (LCG): "ngẫu nhiên" nhưng TẤT ĐỊNH để output tái lập được ───
// (Thuật toán ngẫu nhiên thật dùng nguồn ngẫu nhiên; ở đây seed cố định để kiểm chứng.)
class Rng {
  private state: number;
  constructor(seed: number) { this.state = seed >>> 0; }
  next(): number {                       // trả số thực trong [0, 1)
    this.state = (Math.imul(this.state, 1103515245) + 12345) >>> 0;
    return this.state / 0x100000000;
  }
  int(n: number): number { return Math.floor(this.next() * n); }
}

// ─── QUICKSORT: pivot CUỐI (tất định) vs pivot NGẪU NHIÊN (Las Vegas) ───
function quicksort(input: number[], rng: Rng | null): { sorted: number[]; cmp: number } {
  const a = [...input];
  let cmp = 0;
  function partition(lo: number, hi: number): number {
    if (rng) {                           // ngẫu nhiên hoá: đổi pivot ra vị trí cuối
      const r = lo + rng.int(hi - lo + 1);
      [a[r], a[hi]] = [a[hi], a[r]];
    }
    const pivot = a[hi];
    let fh = lo;
    for (let i = lo; i < hi; i++) { cmp++; if (a[i] < pivot) { [a[i], a[fh]] = [a[fh], a[i]]; fh++; } }
    [a[hi], a[fh]] = [a[fh], a[hi]];
    return fh;
  }
  function sort(lo: number, hi: number): void {
    if (lo >= hi) return;
    const p = partition(lo, hi);
    sort(lo, p - 1); sort(p + 1, hi);
  }
  sort(0, a.length - 1);
  return { sorted: a, cmp };
}

const sorted = Array.from({ length: 64 }, (_, i) => i + 1);   // ĐÃ SẮP → worst case của pivot-cuối
const want = [...sorted];
const det = quicksort(sorted, null);
const rnd = quicksort(sorted, new Rng(42));
console.log("RANDOMIZED QUICKSORT trên mảng ĐÃ SẮP 64 phần tử (ca xấu nhất của pivot cố định):");
console.log(`  pivot cuối (tất định): ${det.cmp} so sánh  ← n(n-1)/2 = ${64 * 63 / 2}, suy biến O(n^2)`);
console.log(`  pivot ngẫu nhiên (seed 42): ${rnd.cmp} so sánh  ← quanh O(n log n), ca xấu gần như ko xảy ra`);
assert.deepEqual(det.sorted, want);      // Las Vegas: LUÔN đúng
assert.deepEqual(rnd.sorted, want);      // dù ngẫu nhiên, kết quả vẫn sắp đúng
assert.equal(det.cmp, 64 * 63 / 2);
assert.ok(rnd.cmp < det.cmp / 3);        // ngẫu nhiên hoá cắt mạnh số so sánh

// ─── MONTE CARLO: ước lượng π bằng gieo điểm ngẫu nhiên vào hình vuông đơn vị ───
// Tỉ lệ điểm rơi trong 1/4 đường tròn ≈ (π/4). Always fast, usually ~correct.
function estimatePi(samples: number, rng: Rng): number {
  let inside = 0;
  for (let i = 0; i < samples; i++) {
    const x = rng.next(), y = rng.next();
    if (x * x + y * y <= 1) inside++;
  }
  return (4 * inside) / samples;
}
const rng2 = new Rng(12345);
console.log("\nMONTE CARLO — ước lượng π bằng gieo điểm (seed 12345):");
for (const n of [100, 10_000, 1_000_000]) {
  const est = estimatePi(n, rng2);
  console.log(`  ${String(n).padStart(9)} điểm → π ≈ ${est.toFixed(5)}  (lệch ${Math.abs(est - Math.PI).toFixed(5)})`);
}
// Càng nhiều mẫu, ước lượng càng sát π (sai số co ~ 1/sqrt(n)).
const big = estimatePi(1_000_000, new Rng(999));
assert.ok(Math.abs(big - Math.PI) < 0.01);

console.log("\nLas Vegas (quicksort ngẫu nhiên): LUÔN đúng, THƯỜNG nhanh. Monte Carlo (ước π): LUÔN");
console.log("nhanh, THƯỜNG đúng xấp xỉ. Ngẫu nhiên hoá né được ca xấu nhất mà ko kẻ thù nào ép được (Skiena tr.172).");
```

Kết quả chạy thật *(tất định)*:

```
RANDOMIZED QUICKSORT trên mảng ĐÃ SẮP 64 phần tử (ca xấu nhất của pivot cố định):
  pivot cuối (tất định): 2016 so sánh  ← n(n-1)/2 = 2016, suy biến O(n^2)
  pivot ngẫu nhiên (seed 42): 341 so sánh  ← quanh O(n log n), ca xấu gần như ko xảy ra

MONTE CARLO — ước lượng π bằng gieo điểm (seed 12345):
        100 điểm → π ≈ 3.08000  (lệch 0.06159)
      10000 điểm → π ≈ 3.14480  (lệch 0.00321)
    1000000 điểm → π ≈ 3.14294  (lệch 0.00135)

Las Vegas (quicksort ngẫu nhiên): LUÔN đúng, THƯỜNG nhanh. Monte Carlo (ước π): LUÔN
nhanh, THƯỜNG đúng xấp xỉ. Ngẫu nhiên hoá né được ca xấu nhất mà ko kẻ thù nào ép được (Skiena tr.172).
```

Ba điều đáng thấm. **(1) Ngẫu nhiên hoá né ca xấu nhất:** cùng mảng *đã sắp*, pivot cố định nổ `2016` so sánh (bậc hai), pivot ngẫu nhiên chỉ `341` (quanh `n log n`) — và quan trọng hơn con số: *không* đầu vào cố định nào ép được ngẫu nhiên vào ca xấu. **(2) Las Vegas không đánh đổi tính đúng:** cả hai quicksort đều ra dãy `1..64` đúng — ngẫu nhiên chỉ ảnh hưởng *thời gian*, không bao giờ cho kết quả sai. **(3) Monte Carlo đổi độ chính xác lấy tốc độ, và hội tụ:** ước π từ `3.08` (100 điểm) tới `3.143` (1 triệu điểm) — sai số co dần `~1/√n`; không bao giờ *đúng tuyệt đối*, nhưng đủ gần và luôn kịp, cho những bài mà lời giải chính xác quá đắt.

> [!note] Tự thử
> 1. Đổi seed quicksort (42 → số khác): số so sánh đổi, nhưng kết quả sắp xếp có đổi không? Vì sao đó là đặc trưng Las Vegas?
> 2. Chạy `estimatePi` với cùng seed hai lần — có ra cùng số không? Bỏ seed (dùng `Math.random`) thì sao? Liên hệ Luật "output tất định".
> 3. Monte Carlo: cần bao nhiêu mẫu để sai số π thường `< 0.001`? Thử vài giá trị, quan sát quy luật `1/√n`.
> 4. Một kẻ tấn công biết bạn dùng quicksort pivot-cuối. Mô tả đầu vào họ gửi để ép `O(n²)`. Vì sao pivot ngẫu nhiên vô hiệu hoá họ? *(mục 1, 2)*

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
| 13 | *(nâng cao)* Luồng mạng | max-flow / min-cut | Skiena §8.5 + CLRS Ch24 |
| 14 | **Thuật toán ngẫu nhiên** *(nâng cao)* ← *đang ở đây* | randomized quicksort, Monte Carlo | Skiena Ch6 |

**Hết khoá.** Toàn bộ 15 bài đã xong — xem [README](../README.md) để ôn toàn cảnh và cách chạy verifier.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 14.1 — Ngẫu nhiên hoá chống "kẻ thù" ép ca xấu nhất bằng cách nào?
> **Đáp:** đưa ngẫu nhiên vào **thuật toán** (vd pivot ngẫu nhiên) thay vì phụ thuộc đầu vào. Kẻ thù không biết trước ta bốc gì nên không ép được ca xấu; worst case vẫn *có thể* xảy ra nhưng xác suất bé tí.

> [!question] Thẻ 14.2 — "Nhanh trung bình trên đầu vào ngẫu nhiên" khác "nhanh xác suất cao trên mọi đầu vào" ra sao?
> **Đáp:** cái đầu (quicksort tất định) giả định *đầu vào* ngẫu nhiên — sai, kẻ thù chọn được. Cái sau (quicksort ngẫu nhiên) đặt ngẫu nhiên ở *thuật toán* → `Θ(n log n)` xác suất cao trên *mỗi* đầu vào cố định (Skiena tr. 134).

> [!question] Thẻ 14.3 — Las Vegas và Monte Carlo khác nhau thế nào?
> **Đáp:** **Las Vegas**: luôn đúng, thường nhanh (thời gian dao động) — vd quicksort ngẫu nhiên. **Monte Carlo**: luôn nhanh, thường đúng / xấp xỉ (có xác suất sai nhỏ) — vd ước π, Miller–Rabin (Skiena tr. 172).

> [!question] Thẻ 14.4 — Vì sao bảng băm (Bài 3) được xem là thuật toán ngẫu nhiên hoá?
> **Đáp:** nó *cược* rằng hàm băm rải khoá đều "như ngẫu nhiên" để tránh va chạm — cược gần như luôn thắng. Vì vậy Skiena để hashing và randomized cùng Chương 6.

> [!question] Thẻ 14.5 — Monte Carlo đổi gì lấy gì? Cải thiện độ tin cậy bằng cách nào?
> **Đáp:** đổi *độ chính xác tuyệt đối* lấy *tốc độ / bộ nhớ*. Tăng độ tin: nhiều mẫu hơn (sai số co `~1/√n`), hoặc chạy lại nhiều lần giảm xác suất sai.

## 8. Câu hỏi tự kiểm tra

1. Vì sao thuật toán tất định luôn có một đầu vào "khắc tinh", còn ngẫu nhiên thì không? *(mục 1, 2)*
2. Giải thích vì sao quicksort pivot-ngẫu-nhiên là `Θ(n log n)` xác suất cao trên *mọi* đầu vào. *(mục 2)*
3. Phân loại các ví dụ sau là Las Vegas hay Monte Carlo: quicksort ngẫu nhiên, ước π, Miller–Rabin, quickselect. *(mục 3)*
4. Kể ba chỗ trong khoá đã dùng ngẫu nhiên hoá và nói mỗi cái thuộc giống nào. *(mục 4)*
5. Chạy demo mục 5. Vì sao pivot ngẫu nhiên cắt số so sánh từ 2016 xuống vài trăm trên mảng đã sắp? *(mục 2 & 5)*

## Tóm tắt một trang

```
BÀI 14 — THUẬT TOÁN NGẪU NHIÊN (nâng cao, khép khoá)
─────────────────────────────────────────────────────────
VẤN ĐỀ  thuật toán TẤT ĐỊNH luôn có đầu vào "khắc tinh" mà KẺ THÙ ép được
   (quicksort pivot-cuối + mảng đã sắp = O(n²)).

NGẪU NHIÊN HOÁ  đưa ngẫu nhiên vào THUẬT TOÁN (pivot ngẫu nhiên), không phụ
   thuộc đầu vào. Kẻ thù hết ép được. Quicksort ngẫu nhiên = Θ(n log n) xác
   suất cao trên MỌI đầu vào (Skiena tr.134). Ngẫu nhiên ở THUẬT TOÁN, ko ở
   đầu vào.

HAI GIỐNG (Skiena tr.172)
   LAS VEGAS   — LUÔN đúng, THƯỜNG nhanh (thời gian dao động). VD: quicksort NN.
   MONTE CARLO — LUÔN nhanh, THƯỜNG đúng/xấp xỉ (sai xác suất nhỏ). VD: ước π,
      Miller–Rabin. Tăng tin cậy: nhiều mẫu (sai số ~1/√n) hoặc chạy lại.

ĐÃ DÙNG SUỐT KHOÁ  bảng băm (Bài 3, cược rải đều) · pivot quicksort (Bài 5,
   Las Vegas) · Rabin–Karp (Bài 12, Monte Carlo + xác minh). Hashing =
   randomized trá hình → cùng Ch6.

DEMO  mảng đã sắp 64: pivot cuối 2016 so sánh vs ngẫu nhiên 341. Ước π: 100→
   3.08, 1 triệu→3.143 (sai số co ~1/√n). Cả hai dùng PRNG SEED cố định (tất
   định để kiểm chứng).
```

## Nguồn

- **Skiena, Steven S. — *The Algorithm Design Manual*, 3rd ed.** (Springer, 2020) — **Chapter 6: Hashing and Randomized Algorithms** (Monte Carlo vs Las Vegas, hashing như randomized, minwise/Bloom filter) và **§4.6 Quicksort** (randomized quicksort Θ(n log n) với xác suất cao). `tai_lieu/The Algorithm Design Manual 3rd Edition...pdf` (offset **PDF = tr. + 15** ở Ch6, **+16** ở Ch4).
- Liên hệ: [Bài 5 — quicksort](bai_05_sap-xep.md) (pivot ngẫu nhiên), [Bài 3 — bảng băm](bai_03_bang-bam.md), [Bài 12 — Rabin–Karp](bai_12_khop-chuoi.md), [Bài 13 — min-cut](bai_13_luong-mang.md). Toàn cảnh: [README khoá học](../README.md).

---

**Bản đồ khoá học:** [Bài 0 — Thuật toán & tính đúng](bai_00_thuat-toan-la-gi.md) · [Bài 1 — Phân tích Big-O](bai_01_big-o.md) · [Bài 2 — CTDL tuyến tính](bai_02_ctdl-tuyen-tinh.md) · [Bài 3 — Từ điển & bảng băm](bai_03_bang-bam.md) · [Bài 4 — Heap & cây tìm kiếm](bai_04_heap-cay-tim-kiem.md) · [Bài 5 — Sắp xếp](bai_05_sap-xep.md) · [Bài 6 — Chia để trị & đệ quy](bai_06_chia-de-tri.md) · [Bài 7 — Đồ thị: duyệt](bai_07_do-thi-duyet.md) · [Bài 8 — Đồ thị trọng số](bai_08_do-thi-trong-so.md) · [Bài 9 — Quy hoạch động](bai_09_quy-hoach-dong.md) · [Bài 10 — Backtracking](bai_10_backtracking.md) · [Bài 11 — NP-đầy đủ](bai_11_np-day-du.md) · [Bài 12 — Khớp chuỗi](bai_12_khop-chuoi.md) · [Bài 13 — Luồng mạng](bai_13_luong-mang.md) · **[Bài 14 — Thuật toán ngẫu nhiên] ← bạn đang ở đây**

Xem thêm [README khoá học](../README.md).
