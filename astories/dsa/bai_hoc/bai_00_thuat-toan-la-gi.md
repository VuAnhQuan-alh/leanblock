# Bài 0 — Thuật toán là gì, và vì sao "trông hợp lý" là chưa đủ

> [!info] Về khoá này
> Khoá **`dsa`** học **cấu trúc dữ liệu & giải thuật** tới mức **"đủ dùng"** cho kỹ sư backend/hệ thống — không phải luyện thi competitive programming. Mục tiêu: nhìn một bài toán là *gọi tên* được cấu trúc dữ liệu và chiến lược thuật toán phù hợp, ước lượng được chi phí, và biết khi nào một cách làm là **sai** hay **quá chậm**. Đi từ nền (thuật toán & Big-O) → cấu trúc dữ liệu → sắp xếp & chia để trị → đồ thị → quy hoạch động → bài toán khó, rồi một tầng nâng cao (khớp chuỗi, luồng mạng, thuật toán ngẫu nhiên).
> Nguồn (Luật số 1): **Skiena** — *The Algorithm Design Manual, 3rd ed.* (nguồn **chính**, PDF `tai_lieu/`, trích `> [!quote] Skiena (tr. N)`, **PDF = tr. + 17**) · **CLRS** — *Introduction to Algorithms, 4th ed.* (tra cứu khi cần chặt chẽ, trích `> [!quote] CLRS (tr. N)`) · **Grokking** — *Grokking Algorithms* (Bhargava, khởi động trực giác, trích `> [!quote] Grokking (tr. N)`, **PDF = tr. + 19**).
> **Chạy demo:** cần **Node 22+** (chạy thẳng `.ts`, tự bỏ phần kiểu). Lưu file rồi gõ `node <tên>.ts` — không cài gói gì. Code tất định: chạy hai lần ra một kết quả.
> Liên hệ: mạch cloud ([`cloud-base`](../../cloud-base/README.md)) dùng các cấu trúc này ở quy mô hệ thống; khoá [`database`](../../database/README.md) chính là một kho giải thuật (B+tree, hash join, query optimizer) chạy thật.

## Mục lục

1. [Tình huống: đoán số từ 1 đến 100](#1-tình-huống-đoán-số-từ-1-đến-100)
2. [Thuật toán là gì: bài toán và thực thể](#2-thuật-toán-là-gì-bài-toán-và-thực-thể)
3. [Ba tính chất của một thuật toán tốt](#3-ba-tính-chất-của-một-thuật-toán-tốt)
4. [Tính đúng phải được chứng minh, không phải "trông hợp lý"](#4-tính-đúng-phải-được-chứng-minh-không-phải-trông-hợp-lý)
5. [Demo: nhị phân so với tuyến tính, và một bản sai](#5-demo-nhị-phân-so-với-tuyến-tính-và-một-bản-sai)
6. [Bản đồ khoá DSA](#6-bản-đồ-khoá-dsa)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Tình huống: đoán số từ 1 đến 100

> [!example] Trò đoán số
> Tôi nghĩ ra một số từ 1 đến 100. Bạn đoán, mỗi lần tôi chỉ nói *"cao hơn"*, *"thấp hơn"* hay *"đúng rồi"*. Bạn cần ít lần đoán nhất.
>
> Cách ngây thơ: đoán 1, rồi 2, rồi 3... Nếu số là 99 thì mất 99 lần. Grokking gọi vui đây là *"simple search (maybe stupid search would be a better term)"*.
>
> Cách khôn: luôn đoán **giữa** khoảng còn lại. Đoán 50 — *"thấp hơn"* → vứt luôn nửa trên. Đoán 75, rồi 63... Mỗi lần **cắt đôi** không gian còn lại, nên dù số nào cũng tìm ra trong **tối đa 7 lần**.

> [!quote] Grokking (tr. 6)
> "This is binary search. You just learned your first algorithm!"
>
> *Đây chính là **tìm kiếm nhị phân**. Bạn vừa học thuật toán đầu tiên của mình!*

Khác biệt 99 với 7 không phải chuyện "code nhanh hơn chút". Nó là khác biệt về **bậc độ lớn**: tuyến tính cần `n` bước, nhị phân cần `log₂ n` bước. Với `n = 100` thì 100 so 7; với `n = 1 tỷ` thì một tỷ so **30**. Cả khoá này xoay quanh đúng loại khác biệt đó — chọn cấu trúc và chiến lược sao cho số bước tăng chậm nhất có thể khi dữ liệu phình to.

> [!quote] Grokking (tr. 7)
> "So binary search will take 18 steps—a big difference! In general, for any list of n, binary search will take log2 n steps to run in the worst case, whereas simple search will take n steps."
>
> *Vậy tìm nhị phân chỉ mất 18 bước — khác biệt lớn! Tổng quát, với danh sách `n` phần tử, tìm nhị phân mất `log₂ n` bước ở trường hợp xấu nhất, còn tìm tuyến tính mất `n` bước.*

## 2. Thuật toán là gì: bài toán và thực thể

Trước khi đo nhanh/chậm, phải định nghĩa *thuật toán* cho chặt. Skiena mở đầu cả cuốn sách bằng đúng câu hỏi này:

> [!quote] Skiena (tr. 3)
> "What is an algorithm? An algorithm is a procedure to accomplish a specific task. An algorithm is the idea behind any reasonable computer program. To be interesting, an algorithm must solve a general, well-specified problem."
>
> *Thuật toán là gì? Một **thuật toán** là một **thủ tục để hoàn thành một nhiệm vụ cụ thể**. Thuật toán là *ý tưởng* đứng sau mọi chương trình máy tính hợp lý. Để đáng quan tâm, một thuật toán phải giải một **bài toán tổng quát, được đặc tả rõ ràng**.*

Mấu chốt là phân biệt **bài toán** *(problem)* với **thực thể** *(instance)* của nó. Bài toán mô tả *toàn bộ tập đầu vào có thể* và đầu ra mong muốn; thực thể là *một* đầu vào cụ thể. Skiena đặc tả bài toán sắp xếp như sau:

```
Bài toán: Sắp xếp (Sorting)
Đầu vào:  một dãy n khoá a₁, ..., aₙ.
Đầu ra:   hoán vị (sắp lại) của dãy sao cho a₁ ≤ a₂ ≤ ... ≤ aₙ.
```

Dãy `{154, 245, 568, 324, 654, 324}` chỉ là *một thực thể*. Một thuật toán sắp xếp phải đúng trên **mọi** thực thể hợp lệ, không chỉ cái bạn thử.

> [!quote] Skiena (tr. 3)
> "This distinction, between a problem and an instance of a problem, is fundamental."
>
> *Sự phân biệt này — giữa một bài toán và một thực thể của bài toán — là **nền tảng**.*

> [!note] Vì sao phân biệt này quan trọng
> Bug kinh điển: code "chạy đúng với mọi test tôi thử" nhưng sai trên thực thể chưa thử. Thuật toán được phán xét trên *cả không gian đầu vào*, nên lý lẽ "tôi chạy thử thấy ổn" không bao giờ là bằng chứng đúng — nó chỉ là *chưa thấy* sai. Mục 4 sẽ cho thấy một bản tìm nhị phân "chạy thử thấy ổn" mà vẫn sai.

## 3. Ba tính chất của một thuật toán tốt

> [!quote] Skiena (tr. 4)
> "There are three desirable properties for a good algorithm. We seek algorithms that are correct and efficient, while being easy to implement."
>
> *Có ba tính chất đáng mong muốn ở một thuật toán tốt. Ta tìm những thuật toán **đúng** và **hiệu quả**, đồng thời **dễ cài đặt**.*

Ba tính chất này căng nhau, hiếm khi đạt cả ba cùng lúc:

| Tính chất | Nghĩa là | Đo bằng | Dạy ở bài |
| :-- | :-- | :-- | :-- |
| **Đúng** *(correct)* | ra kết quả đúng trên **mọi** đầu vào hợp lệ | chứng minh / phản ví dụ | Bài 0 (và suốt khoá) |
| **Hiệu quả** *(efficient)* | số bước / bộ nhớ tăng chậm khi `n` lớn | Big-O (Bài 1) | Bài 1 trở đi |
| **Dễ cài** *(easy to implement)* | ít dòng, ít chỗ sai, dễ đọc | kinh nghiệm | xuyên suốt |

Skiena nhấn: trong công nghiệp, "đủ nhanh và đủ đúng" thường được chấp nhận ngay, và người ta chỉ đi tìm thuật toán tối ưu khi *đã* gặp rắc rối hiệu năng. Nhưng *đúng* thì không có vùng xám — một thuật toán sai thì nhanh cỡ nào cũng vô dụng. Vì vậy bài này tập trung vào trục **đúng**; trục **hiệu quả** là trọng tâm Bài 1.

## 4. Tính đúng phải được chứng minh, không phải "trông hợp lý"

Đây là bài học đắt nhất của chương mở đầu Skiena, và là lý do ta không bao giờ tin một thuật toán chỉ vì nó *nghe* có lý:

> [!quote] Skiena (tr. 11)
> "Take-Home Lesson: Reasonable-looking algorithms can easily be incorrect. Algorithm correctness is a property that must be carefully demonstrated."
>
> *Bài học rút ra: Những thuật toán **trông hợp lý** rất dễ **sai**. Tính đúng của thuật toán là một tính chất phải được **chứng minh cẩn thận**.*

Vậy làm sao *bác bỏ* một thuật toán sai? Không cần chứng minh dài dòng — chỉ cần **một thực thể** mà nó cho đáp án sai. Thực thể đó gọi là **phản ví dụ** *(counterexample)*:

> [!quote] Skiena (tr. 13)
> "The best way to prove that an algorithm is incorrect is to produce an instance on which it yields an incorrect answer. Such instances are called counterexamples."
>
> *Cách tốt nhất để chứng minh một thuật toán **sai** là đưa ra một thực thể mà nó cho **đáp án sai**. Những thực thể như vậy gọi là **phản ví dụ**.*

Skiena nói một phản ví dụ tốt cần hai tính chất: **kiểm chứng được** *(verifiability)* — tính được đáp án sai của thuật toán *và* chỉ ra đáp án đúng hơn; và **đơn giản** *(simplicity)* — lược bỏ mọi chi tiết thừa để thấy rõ *vì sao* nó hỏng. Chứng minh một thuật toán **đúng** thì khó (cần bất biến vòng lặp, quy nạp — sẽ gặp dần); nhưng chứng minh nó **sai** thì rẻ: tìm được một phản ví dụ là xong.

Mục 5 làm đúng quy trình đó bằng code: lấy một bản tìm nhị phân *trông hoàn toàn hợp lý*, rồi để máy **dò ra phản ví dụ nhỏ nhất** bác bỏ nó.

## 5. Demo: nhị phân so với tuyến tính, và một bản sai

Demo làm hai việc. **(a)** Đếm số lần so sánh của tìm tuyến tính vs tìm nhị phân trên `[1..100]` — thấy tận mắt `n` so với `log₂ n`. **(b)** Dựng một `buggyBinarySearch` *trông hợp lý* (chỉ lệch biên trên một đơn vị) rồi quét tìm phản ví dụ nhỏ nhất — minh hoạ sống "trông hợp lý ≠ đúng".

```typescript
import { strict as assert } from "node:assert";

// ─── Hai thuật toán tìm kiếm, đếm số lần so sánh để thấy "hiệu quả" khác nhau ───

// Tìm tuyến tính (simple search): quét từ đầu. Worst case n bước.
function linearSearch(arr: number[], target: number): { index: number; steps: number } {
  let steps = 0;
  for (let i = 0; i < arr.length; i++) {
    steps++;
    if (arr[i] === target) return { index: i, steps };
  }
  return { index: -1, steps };
}

// Tìm nhị phân (binary search): đòi mảng ĐÃ SẮP XẾP. Worst case log2(n) bước.
function binarySearch(arr: number[], target: number): { index: number; steps: number } {
  let lo = 0;
  let hi = arr.length - 1;
  let steps = 0;
  while (lo <= hi) {
    steps++;
    const mid = (lo + hi) >> 1; // chia đôi, làm tròn xuống
    if (arr[mid] === target) return { index: mid, steps };
    if (arr[mid] < target) lo = mid + 1;
    else hi = mid - 1;
  }
  return { index: -1, steps };
}

// ─── Một binary search TRÔNG HỢP LÝ nhưng SAI: biên trên lệch một đơn vị ───
// (khởi tạo hi = length - 2 → không bao giờ xét phần tử CUỐI mảng)
function buggyBinarySearch(arr: number[], target: number): number {
  let lo = 0;
  let hi = arr.length - 2;          // SAI: phải là length - 1
  while (lo <= hi) {
    const mid = (lo + hi) >> 1;
    if (arr[mid] === target) return mid;
    if (arr[mid] < target) lo = mid + 1;
    else hi = mid - 1;
  }
  return -1;
}

const sorted = Array.from({ length: 100 }, (_, i) => i + 1); // [1, 2, ..., 100]

console.log("TÌM KIẾM TRONG MẢNG [1..100] — đếm số lần so sánh:");
for (const target of [1, 50, 100, 99]) {
  const lin = linearSearch(sorted, target);
  const bin = binarySearch(sorted, target);
  console.log(
    `  tìm ${String(target).padStart(3)}  |  tuyến tính: ${String(lin.steps).padStart(3)} bước` +
    `   nhị phân: ${String(bin.steps).padStart(2)} bước`,
  );
  // cả hai phải tìm ra cùng vị trí
  assert.equal(lin.index, bin.index);
}

// log2(100) ≈ 6.64 → worst case nhị phân = 7 bước (Grokking tr.7)
const worst = binarySearch(sorted, 100);
console.log(`\nWorst case (tìm 100): tuyến tính 100 bước vs nhị phân ${worst.steps} bước` +
  `  (log2(100) ≈ 6.64 → 7).`);
assert.equal(worst.steps, 7);

// ─── Tính ĐÚNG phải được CHỨNG MINH, không chỉ "trông hợp lý" (Skiena tr.11) ───
// Tìm một COUNTEREXAMPLE (Skiena tr.13) khiến bản "sai" trả kết quả sai.
console.log("\nTÍNH ĐÚNG — bản binary search TRÔNG hợp lý nhưng SAI:");
let counterexample = -1;
for (let t = 1; t <= 100; t++) {
  if (buggyBinarySearch(sorted, t) !== binarySearch(sorted, t).index) {
    counterexample = t;
    break;
  }
}
console.log(`  counterexample nhỏ nhất: tìm ${counterexample}` +
  `  → bản sai trả ${buggyBinarySearch(sorted, counterexample)}` +
  `, bản đúng trả ${binarySearch(sorted, counterexample).index}`);
assert.notEqual(counterexample, -1);         // CÓ phản ví dụ → bản kia SAI
assert.equal(buggyBinarySearch(sorted, counterexample), -1);
assert.equal(binarySearch(sorted, counterexample).index, counterexample - 1);

console.log("\nMột phản ví dụ đủ để bác bản 'trông hợp lý'. Tính đúng phải chứng minh,");
console.log("còn tính hiệu quả thì đo bằng số bước — hai trục xuyên suốt cả khoá.");
```

Kết quả chạy thật *(tất định)*:

```
TÌM KIẾM TRONG MẢNG [1..100] — đếm số lần so sánh:
  tìm   1  |  tuyến tính:   1 bước   nhị phân:  6 bước
  tìm  50  |  tuyến tính:  50 bước   nhị phân:  1 bước
  tìm 100  |  tuyến tính: 100 bước   nhị phân:  7 bước
  tìm  99  |  tuyến tính:  99 bước   nhị phân:  6 bước

Worst case (tìm 100): tuyến tính 100 bước vs nhị phân 7 bước  (log2(100) ≈ 6.64 → 7).

TÍNH ĐÚNG — bản binary search TRÔNG hợp lý nhưng SAI:
  counterexample nhỏ nhất: tìm 100  → bản sai trả -1, bản đúng trả 99

Một phản ví dụ đủ để bác bản 'trông hợp lý'. Tính đúng phải chứng minh,
còn tính hiệu quả thì đo bằng số bước — hai trục xuyên suốt cả khoá.
```

Ba điều đáng thấm. **(1) `log n` cắt bước khủng khiếp:** tìm 50 chỉ mất *1* bước nhị phân (trúng giữa ngay) so với 50 bước tuyến tính; tìm 100 mất 7 so với 100. **(2) Nhị phân đòi điều kiện:** mảng *phải sắp xếp* — đó là một ví dụ "trả tiền trước" (sắp xếp một lần) để "rẻ mãi về sau" (tra nhanh nhiều lần), đúng tinh thần của index trong [khoá database](../../database/README.md). **(3) Lệch một đơn vị ở biên là đủ sai:** `hi = length - 2` khiến phần tử cuối không bao giờ bị xét; nó *đúng với 99/100 đầu vào* nên dễ lọt qua test hời hợt — máy dò ra phản ví dụ `100` phơi bày điều đó. Đây chính là *"reasonable-looking algorithms can easily be incorrect"*.

> [!note] Tự thử
> 1. Đổi `buggyBinarySearch` thành `hi = arr.length - 1` (sửa bug): quét lại — còn phản ví dụ nào không? Vì sao vòng dò giờ chạy hết 1..100 mà không tìm thấy?
> 2. Thêm một bug *khác*: để `mid = (lo + hi + 1) >> 1` (làm tròn lên). Phản ví dụ nhỏ nhất bây giờ là bao nhiêu? (Gợi ý: nghĩ về lúc `lo` và `hi` sát nhau.)
> 3. Với mảng `n = 1000`, worst case nhị phân là mấy bước? Kiểm bằng cách đổi `length: 100` thành `1000` rồi tìm phần tử cuối. So với `log2(1000) ≈ 9.97`.
> 4. Vì sao tìm tuyến tính **không** đòi mảng sắp xếp còn nhị phân thì có? Nếu dữ liệu đến theo luồng không sắp xếp và chỉ tra một lần, thuật toán nào hợp lý hơn?

## 6. Bản đồ khoá DSA

Khoá chia **hai tầng**: lõi (Bài 0–11) đủ cho phần lớn công việc thực tế; nâng cao (Bài 12–14) cho các bài toán chuyên biệt hay gặp trong hệ thống lớn.

| # | Bài | Chủ đề | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | **Thuật toán & tính đúng** ← *đang ở đây* | nền: đúng vs hiệu quả | Skiena Ch1 + Grokking |
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
| 14 | *(nâng cao)* Thuật toán ngẫu nhiên | randomized quicksort, Monte Carlo | Skiena Ch6 |

Hai trục xuyên suốt: mỗi bài hỏi *thuật toán này có **đúng** không* (Bài 0) và *nó tốn bao nhiêu khi `n` lớn* (Bài 1).

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 0.1 — Thuật toán là gì?
> **Đáp:** một **thủ tục để hoàn thành một nhiệm vụ cụ thể**; là *ý tưởng* sau một chương trình. Để đáng quan tâm, nó phải giải một **bài toán tổng quát, đặc tả rõ ràng** (Skiena tr. 3).

> [!question] Thẻ 0.2 — Phân biệt "bài toán" (problem) và "thực thể" (instance).
> **Đáp:** **bài toán** mô tả *toàn bộ* tập đầu vào có thể + đầu ra mong muốn; **thực thể** là *một* đầu vào cụ thể. Thuật toán phải đúng trên **mọi** thực thể, không chỉ cái đã thử.

> [!question] Thẻ 0.3 — Ba tính chất của một thuật toán tốt?
> **Đáp:** **đúng** (correct), **hiệu quả** (efficient), **dễ cài** (easy to implement). Hiếm khi đạt cả ba; nhưng *đúng* không có vùng xám (Skiena tr. 4).

> [!question] Thẻ 0.4 — Cách tốt nhất để chứng minh một thuật toán SAI?
> **Đáp:** đưa ra một **phản ví dụ** (counterexample) — một thực thể mà nó cho đáp án sai. Phản ví dụ tốt: **kiểm chứng được** và **đơn giản** (Skiena tr. 13).

> [!question] Thẻ 0.5 — Tìm nhị phân nhanh hơn tìm tuyến tính bao nhiêu, và với điều kiện gì?
> **Đáp:** `log₂ n` bước so với `n` bước ở worst case (n=100 → 7 so 100; n=1 tỷ → 30 so 1 tỷ). Điều kiện: mảng phải **đã sắp xếp** (Grokking tr. 7).

## 8. Câu hỏi tự kiểm tra

1. Trò đoán số 1–100: vì sao đoán giữa khoảng luôn tốt nhất? Mỗi lần đoán cắt bỏ bao nhiêu phần không gian còn lại? *(mục 1)*
2. Viết đặc tả **bài toán** (problem) cho "tìm phần tử lớn nhất trong một dãy số" theo dạng Đầu vào / Đầu ra của Skiena. *(mục 2)*
3. Ba tính chất của thuật toán tốt là gì? Vì sao *đúng* khác hẳn hai cái kia về bản chất? *(mục 3)*
4. "Code chạy đúng với mọi test tôi thử" — vì sao đây *không* phải bằng chứng thuật toán đúng? *(mục 2 & 4)*
5. Chạy demo mục 5. Với bản `buggyBinarySearch`, giải thích vì sao phản ví dụ nhỏ nhất là `100` chứ không phải số nào khác. *(mục 5)*

## Tóm tắt một trang

```
BÀI 0 — THUẬT TOÁN LÀ GÌ + VÌ SAO "TRÔNG HỢP LÝ" CHƯA ĐỦ
─────────────────────────────────────────────────────────
THUẬT TOÁN  = thủ tục hoàn thành một nhiệm vụ cụ thể; ý tưởng sau một chương
   trình. Phải giải BÀI TOÁN tổng quát, đặc tả rõ (Skiena tr.3).

BÀI TOÁN vs THỰC THỂ  problem = toàn bộ tập đầu vào + đầu ra; instance = MỘT
   đầu vào. Thuật toán phải đúng trên MỌI thực thể → "chạy thử thấy ổn" ≠ đúng.

BA TÍNH CHẤT TỐT  (1) ĐÚNG  (2) HIỆU QUẢ  (3) DỄ CÀI (Skiena tr.4). Hiếm khi
   đủ cả ba; "đúng" không có vùng xám — sai thì nhanh cỡ nào cũng vô dụng.

TÍNH ĐÚNG  phải CHỨNG MINH (Skiena tr.11). Bác một thuật toán sai = đưa một
   PHẢN VÍ DỤ (counterexample): instance cho đáp án sai (Skiena tr.13).

HAI TRỤC CẢ KHOÁ  ĐÚNG (bài 0) + HIỆU QUẢ = log n vs n (Grokking tr.7, Big-O
   bài 1). Tìm nhị phân: log₂ n bước, cần mảng ĐÃ SẮP XẾP.

DEMO  n vs log n: tìm 100 → 100 bước vs 7. Bug hi=length-2 đúng 99/100 ca →
   phản ví dụ nhỏ nhất = 100. 15 bài: lõi 0–11 + nâng cao 12–14.
```

## Nguồn

- **Skiena, Steven S. — *The Algorithm Design Manual*, 3rd ed.** (Springer, 2020) — **Chapter 1: Introduction to Algorithm Design**: định nghĩa thuật toán, phân biệt problem/instance, ba tính chất (đúng/hiệu quả/dễ cài), reasoning about correctness, phản ví dụ. `tai_lieu/The Algorithm Design Manual 3rd Edition...pdf` (offset **PDF = tr. + 17**).
- **Bhargava, Aditya Y. — *Grokking Algorithms*** (Manning) — **Chapter 1**: tìm nhị phân, trực giác `log n` qua trò đoán số. `tai_lieu/Grokking Algorithms...pdf` (offset **PDF = tr. + 19**).
- **Cormen, Leiserson, Rivest, Stein — *Introduction to Algorithms*, 4th ed.** (CLRS, MIT Press) — dùng tra cứu chặt chẽ ở các bài sau. `tai_lieu/Introduction to Algorithms 4th edition...pdf`.
- Liên hệ: [database — Index: B+tree](../../database/README.md) là "tìm nhị phân trên đĩa" ở quy mô thật; [cloud-base](../../cloud-base/README.md) dùng các cấu trúc này ở quy mô hệ thống.

---

**Bản đồ khoá học:** **[Bài 0 — Thuật toán & tính đúng] ← bạn đang ở đây** · [Bài 1 — Phân tích Big-O](bai_01_big-o.md) · [Bài 2 — CTDL tuyến tính](bai_02_ctdl-tuyen-tinh.md) · [Bài 3 — Từ điển & bảng băm](bai_03_bang-bam.md) · [Bài 4 — Heap & cây tìm kiếm](bai_04_heap-cay-tim-kiem.md) · [Bài 5 — Sắp xếp](bai_05_sap-xep.md) · [Bài 6 — Chia để trị & đệ quy](bai_06_chia-de-tri.md) · [Bài 7 — Đồ thị: duyệt](bai_07_do-thi-duyet.md) · [Bài 8 — Đồ thị trọng số](bai_08_do-thi-trong-so.md) · [Bài 9 — Quy hoạch động](bai_09_quy-hoach-dong.md) · [Bài 10 — Backtracking](bai_10_backtracking.md) · [Bài 11 — NP-đầy đủ](bai_11_np-day-du.md) · [Bài 12 — Khớp chuỗi](bai_12_khop-chuoi.md) · [Bài 13 — Luồng mạng](bai_13_luong-mang.md) · [Bài 14 — Thuật toán ngẫu nhiên](bai_14_ngau-nhien.md)

Xem thêm [README khoá học](../README.md).
