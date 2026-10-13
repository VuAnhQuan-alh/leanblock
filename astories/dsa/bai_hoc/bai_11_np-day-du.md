# Bài 11 — NP-đầy đủ và bài toán khó: khi không có lời giải nhanh

> [!info] Về bài này
> Bài 10 cho thấy có những bài phải duyệt không gian mũ. Bài này trả lời câu hỏi lớn: *vì sao* một số bài toán dường như không thể giải nhanh — và ta làm gì khi gặp chúng. Đây là **lý thuyết NP-đầy đủ**: khái niệm **rút gọn** (reduction) chứng minh hai bài "khó như nhau", bài toán **SAT** làm nguyên mẫu, câu hỏi triệu đô **P vs NP** (tìm khó nhưng kiểm dễ), và ba lối thoát thực dụng khi bài là NP-khó. Bài này **khép tầng lõi** (0–11); tầng nâng cao (12–14) là các chủ đề chuyên sâu.
> Nguồn (Luật số 1): **Skiena** *The Algorithm Design Manual 3e* — **Chapter 11: NP-Completeness, Chapter 12: Dealing with Hard Problems** (`tai_lieu/`, trích `> [!quote] Skiena (tr. N)`, **PDF = tr. + 13** ở Ch11–12).
> **Chạy demo:** `node bai_11.ts` — Node 22+, không cài gói. Code tất định.
> Cần đọc trước: [Bài 1 — Big-O](bai_01_big-o.md), [Bài 10 — backtracking](bai_10_backtracking.md) (không gian mũ).

## Mục lục

1. [Tình huống: những bài toán không ai biết giải nhanh](#1-tình-huống-những-bài-toán-không-ai-biết-giải-nhanh)
2. [NP-đầy đủ và phép rút gọn](#2-np-đầy-đủ-và-phép-rút-gọn)
3. [P vs NP: tìm khó, kiểm dễ](#3-p-vs-np-tìm-khó-kiểm-dễ)
4. [Gặp bài NP-khó thì làm gì](#4-gặp-bài-np-khó-thì-làm-gì)
5. [Demo: SAT và vertex cover xấp xỉ](#5-demo-sat-và-vertex-cover-xấp-xỉ)
6. [Bản đồ khoá DSA](#6-bản-đồ-khoá-dsa)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Tình huống: những bài toán không ai biết giải nhanh

> [!example] Sếp giao một bài, bạn loay hoay mãi không ra thuật toán nhanh
> Lịch trình tối ưu cho đội xe, xếp 200 sinh viên vào phòng thi tránh trùng môn, tìm tour rẻ nhất thăm 50 thành phố (TSP). Bạn thử đủ cách — tham lam sai, QHĐ thì trạng thái mũ — và bắt đầu nghi ngờ *không có* thuật toán nhanh. Nhưng làm sao *chứng minh* điều đó, thay vì cứ nghĩ tại mình kém?

Đó chính là món quà của lý thuyết NP-đầy đủ: một công cụ để *biết chắc* khi nào nên ngừng tìm lời giải nhanh.

> [!quote] Skiena (tr. 355)
> "The truth is that the theory of NP-completeness is an immensely useful tool for the algorithm designer, even though all it provides are negative results."
>
> *Sự thật là lý thuyết **NP-đầy đủ** là một công cụ **cực kỳ hữu ích** cho người thiết kế thuật toán, dù tất cả những gì nó cho chỉ là **kết quả phủ định**.*

> [!quote] Skiena (tr. 355)
> "The theory of NP-completeness enables us to focus our efforts more productively, by revealing when the search for an efficient algorithm is doomed to failure."
>
> *Lý thuyết NP-đầy đủ giúp ta **tập trung sức lực hiệu quả hơn**, bằng cách cho biết khi nào việc tìm một thuật toán hiệu quả là **vô vọng**.*

Biết một bài là NP-khó không phải để bỏ cuộc — mà để *ngừng tìm lời giải tối ưu nhanh* và chuyển sang giải pháp thực dụng (mục 4).

## 2. NP-đầy đủ và phép rút gọn

Công cụ trung tâm là **rút gọn** *(reduction)* — biến bài toán A thành bài toán B để nói "A khó không quá B":

> [!quote] Skiena (tr. 355)
> "The fundamental concept we will use here is reduction, showing that two problems are really equivalent."
>
> *Khái niệm nền tảng ta dùng ở đây là **rút gọn**, cho thấy hai bài toán thực ra **tương đương**.*

Ý tưởng: nếu ta *biến* mọi thực thể của A thành thực thể của B (nhanh, đa thức) sao cho lời giải B cho ra lời giải A, thì "B giải được nhanh ⟹ A cũng vậy". Đảo lại: nếu A đã biết là khó, thì B cũng khó.

Vài lớp khái niệm (nói gọn):

- **P** — lớp bài **giải** được trong thời gian đa thức (sắp xếp, đường ngắn nhất, MST... mọi thứ Bài 0–9).
- **NP** — lớp bài mà một lời giải đề xuất **kiểm** được trong thời gian đa thức (dù *tìm* nó có thể khó).
- **NP-đầy đủ** *(NP-complete)* — những bài **khó nhất trong NP**: mọi bài NP đều rút gọn được về chúng. Giải nhanh *một* bài NP-đầy đủ ⟹ giải nhanh *mọi* bài NP. **SAT** (thoả được công thức logic) là bài NP-đầy đủ đầu tiên được chứng minh (định lý Cook–Levin); TSP, vertex cover, tô màu đồ thị, ba-lô... đều NP-đầy đủ.

```
            ┌─────────────── NP (kiểm dễ) ───────────────┐
            │   ┌──── P (giải dễ) ────┐                   │
            │   │ sort, BFS, Dijkstra │   NP-đầy đủ:       │
            │   │ MST, QHĐ...         │   SAT, TSP,        │
            │   └─────────────────────┘   vertex cover... │
            └─────────────────────────────────────────────┘
            P = NP ?  (chưa ai biết — câu hỏi mở lớn nhất CS)
```

## 3. P vs NP: tìm khó, kiểm dễ

Câu hỏi mở nổi tiếng nhất khoa học máy tính nằm ở khoảng cách giữa *tìm* và *kiểm*:

> [!quote] Skiena (tr. 380)
> "The primary issue in P vs. NP is whether verification is really an easier task than initial discovery."
>
> *Vấn đề cốt lõi của **P vs. NP** là liệu **kiểm chứng** có thực sự là việc **dễ hơn** việc **khám phá** lời giải ban đầu hay không.*

Trực giác: cho một tour TSP, *kiểm* "tổng ≤ k?" rất nhanh (cộng các cạnh); nhưng *tìm* tour rẻ nhất thì phải lục trong không gian mũ. Cho một lời gán biến, *kiểm* công thức SAT có thoả không là duyệt tuyến tính; nhưng *tìm* lời gán thoả thì (ta tin) phải thử `2ⁿ`. **P = NP?** hỏi: liệu mọi bài kiểm-dễ có thực ra cũng giải-dễ? Hầu hết tin **P ≠ NP** (tìm *thực sự* khó hơn kiểm), nhưng chưa ai chứng minh — giải được là một triệu đô giải Clay. Demo mục 5 cho thấy tận mắt khe hở "tìm `2ⁿ` vs kiểm tuyến tính".

## 4. Gặp bài NP-khó thì làm gì

NP-khó *không* phải dấu chấm hết — ứng dụng vẫn cần giải:

> [!quote] Skiena (tr. 389)
> "For the practical person, demonstrating that a problem is NP-complete is never the end of the line."
>
> *Với người thực dụng, chứng minh một bài là **NP-đầy đủ không bao giờ là điểm dừng**.*

Điều ta mất chỉ là *lời giải tối ưu, nhanh, ở worst case* — không phải mọi hy vọng:

> [!quote] Skiena (tr. 389)
> "All you know is that you won't find one that quickly solves the problem to optimality in the worst case."
>
> *Tất cả những gì bạn biết là bạn **sẽ không tìm được** thuật toán giải bài toán tới **tối ưu một cách nhanh chóng ở trường hợp xấu nhất**.*

Ba lối thoát (Skiena Ch12), đánh đổi giữa *tối ưu*, *tốc độ*, và *bảo đảm*:

| Lối thoát | Bỏ cái gì | Giữ cái gì | Ví dụ |
| :-- | :-- | :-- | :-- |
| **Nhanh ở ca trung bình** | bảo đảm worst case | lời giải *tối ưu* | backtracking + pruning mạnh (Bài 10) |
| **Heuristic** | bảo đảm *tối ưu* | *tốc độ* | tham lam, luyện kim mô phỏng (simulated annealing) |
| **Thuật toán xấp xỉ** | tối ưu *tuyệt đối* | *bảo đảm gần tối ưu* (vd ≤ 2× tối ưu) | 2-approximation vertex cover |

Thuật toán xấp xỉ là đẹp nhất về lý thuyết: chạy đa thức *và* hứa *chứng minh được* kết quả không tệ quá một hệ số so với tối ưu — demo mục 5 làm vertex cover 2-approximation.

> [!note] Khép tầng lõi — và vì sao NP-khó quan trọng với kỹ sư hệ thống
> Rất nhiều bài vận hành thực tế là NP-khó trá hình: xếp pod lên node (bin packing), định tuyến, lập lịch job, phân mảnh dữ liệu tối ưu. Biết chúng NP-khó giúp bạn *không* phí thời gian tìm lời giải hoàn hảo, mà dùng heuristic "đủ tốt" ngay — đúng tinh thần đã gặp ở [sre](../../sre/README.md) và [cloud-base](../../cloud-base/README.md). Tầng lõi DSA (Bài 0–11) khép lại ở đây; tầng nâng cao kế tiếp (khớp chuỗi, luồng mạng, thuật toán ngẫu nhiên) là các chủ đề chuyên sâu đứng trên nền này.

## 5. Demo: SAT và vertex cover xấp xỉ

Demo hai phần. **(1) SAT:** giải công thức CNF 3 biến bằng vét `2ⁿ` lời gán, rồi cho thấy *kiểm* một lời gán chỉ tốn số-mệnh-đề (tìm khó, kiểm dễ — ruột P vs NP). **(2) Vertex cover:** so lời giải *chính xác* (vét `2ⁿ` tập con, NP-khó) với **2-approximation** (đa thức, bảo đảm ≤ 2× tối ưu).

```typescript
import { strict as assert } from "node:assert";

// ─── SAT (thoả được): bài toán NP-đầy đủ "nguyên mẫu" ───
// Công thức CNF: VÀ của các mệnh đề; mỗi mệnh đề là HOẶC của các literal.
// literal > 0: biến xi phải TRUE; literal < 0: biến x|i| phải FALSE.
type Clause = number[];
const formula: Clause[] = [
  [1, -2],    // x1 OR (NOT x2)
  [2, 3],     // x2 OR x3
  [-1, -3],   // (NOT x1) OR (NOT x3)
];
const numVars = 3;

// KIỂM TRA một lời gán (dễ, đa thức): duyệt mọi mệnh đề.
function verify(assign: boolean[]): boolean {
  return formula.every((clause) =>
    clause.some((lit) => (lit > 0 ? assign[lit] : !assign[-lit])));
}

// TÌM lời giải (khó, mũ): thử cả 2^n lời gán.
function solveSAT(n: number): { found: boolean[] | null; tried: number } {
  let tried = 0;
  for (let mask = 0; mask < (1 << n); mask++) {
    tried++;
    const assign: boolean[] = [false];           // index 1..n
    for (let i = 1; i <= n; i++) assign[i] = (mask & (1 << (i - 1))) !== 0;
    if (verify(assign)) return { found: assign, tried };
  }
  return { found: null, tried };
}

const sat = solveSAT(numVars);
console.log("SAT — tìm lời gán thoả công thức CNF 3 biến:");
console.log(`  số lời gán phải thử (worst case) = 2^${numVars} = ${1 << numVars}`);
console.log(`  đã thử ${sat.tried} lời gán, tìm thấy: x1=${sat.found![1]}, x2=${sat.found![2]}, x3=${sat.found![3]}`);
console.log(`  KIỂM TRA lời gán đó: chỉ cần duyệt ${formula.length} mệnh đề (đa thức) → ${verify(sat.found!)}`);
assert.ok(sat.found !== null);
assert.ok(verify(sat.found!));
// Khó ≠ dễ: TÌM phải quét tới 2^n, KIỂM chỉ tốn số-mệnh-đề. Đây là ruột P vs NP.

// ─── VERTEX COVER: tập đỉnh phủ MỌI cạnh. Tìm nhỏ nhất = NP-khó ───
const edges: Array<[number, number]> = [[1, 2], [1, 3], [2, 3], [3, 4], [4, 5]];
const verts = [1, 2, 3, 4, 5];

// CHÍNH XÁC (mũ): thử mọi tập con đỉnh, lấy tập nhỏ nhất phủ hết cạnh.
function exactVC(): number {
  let best = verts.length;
  for (let mask = 0; mask < (1 << verts.length); mask++) {
    const cover = new Set<number>();
    for (let i = 0; i < verts.length; i++) if (mask & (1 << i)) cover.add(verts[i]);
    if (edges.every(([u, v]) => cover.has(u) || cover.has(v))) best = Math.min(best, cover.size);
  }
  return best;
}

// XẤP XỈ 2 lần (đa thức): nhặt một cạnh chưa phủ, thêm CẢ HAI đầu, lặp.
function approxVC(): number {
  const cover = new Set<number>();
  for (const [u, v] of edges) {
    if (!cover.has(u) && !cover.has(v)) { cover.add(u); cover.add(v); }
  }
  return cover.size;
}

const opt = exactVC();
const approx = approxVC();
console.log("\nVERTEX COVER — phủ mọi cạnh bằng ít đỉnh nhất:");
console.log(`  chính xác (thử 2^${verts.length} tập con) = ${opt} đỉnh  ← NP-khó, mũ`);
console.log(`  xấp xỉ 2 lần (đa thức, nhanh)        = ${approx} đỉnh  ← đảm bảo ≤ 2 × tối ưu`);
assert.ok(approx <= 2 * opt);     // bảo đảm của thuật toán xấp xỉ 2-approximation
assert.equal(opt, 3);

console.log("\nNP-khó: TÌM lời giải tối ưu phải vét mũ; nhưng KIỂM nhanh (P vs NP, Skiena tr.380).");
console.log("Khi gặp bài NP-khó: chấp nhận chậm (backtracking+prune), heuristic, hay XẤP XỈ (tr.389).");
```

Kết quả chạy thật *(tất định)*:

```
SAT — tìm lời gán thoả công thức CNF 3 biến:
  số lời gán phải thử (worst case) = 2^3 = 8
  đã thử 4 lời gán, tìm thấy: x1=true, x2=true, x3=false
  KIỂM TRA lời gán đó: chỉ cần duyệt 3 mệnh đề (đa thức) → true

VERTEX COVER — phủ mọi cạnh bằng ít đỉnh nhất:
  chính xác (thử 2^5 tập con) = 3 đỉnh  ← NP-khó, mũ
  xấp xỉ 2 lần (đa thức, nhanh)        = 4 đỉnh  ← đảm bảo ≤ 2 × tối ưu

NP-khó: TÌM lời giải tối ưu phải vét mũ; nhưng KIỂM nhanh (P vs NP, Skiena tr.380).
Khi gặp bài NP-khó: chấp nhận chậm (backtracking+prune), heuristic, hay XẤP XỈ (tr.389).
```

Ba điều đáng thấm. **(1) Tìm khó, kiểm dễ — tận mắt:** SAT phải *quét* tới `2ⁿ` lời gán để tìm (ở đây may, trúng sau 4 lần), nhưng *kiểm* một lời gán chỉ duyệt 3 mệnh đề — đúng khe hở trung tâm của P vs NP. **(2) Xấp xỉ đổi tối ưu lấy tốc độ + bảo đảm:** 2-approximation cho `4` đỉnh (không phải `3` tối ưu) nhưng chạy đa thức *và* chắc chắn không quá `2 × 3 = 6`; với đồ thị triệu đỉnh, "gần đúng mà nhanh" thắng "tối ưu mà treo máy". **(3) NP-khó là ranh giới, không phải vực thẳm:** cả hai bài vẫn giải *được* — chỉ là cái giá worst-case là mũ; biết điều đó để chọn đúng lối thoát thay vì húc đầu tìm thuật toán đa thức không tồn tại.

> [!note] Tự thử
> 1. Đổi công thức SAT thành *không thoả được* (vd thêm mệnh đề mâu thuẫn): `solveSAT` thử hết bao nhiêu lời gán rồi trả `null`? (Gợi ý: đúng `2ⁿ`.)
> 2. Thêm biến vào SAT (n=4, 5, ...): số lời gán phải thử tăng thế nào? Vẽ `2ⁿ` cho `n = 10, 20, 50`.
> 3. Dựng một đồ thị mà 2-approximation vertex cover cho kết quả *đúng gấp đôi* tối ưu (chạm cận bảo đảm). (Gợi ý: nhiều cạnh rời.)
> 4. TSP là NP-khó. Nêu một heuristic (vd "luôn tới thành phố gần nhất chưa thăm") và một lý do nó có thể cho tour tệ. *(mục 4)*

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
| 11 | **NP-đầy đủ & bài toán khó** ← *đang ở đây* | khi không có lời giải nhanh | Skiena Ch11–12 |
| 12 | *(nâng cao)* Khớp chuỗi | KMP / Rabin–Karp | Skiena §6.7 + CLRS Ch32 |
| 13 | *(nâng cao)* Luồng mạng | max-flow / min-cut | Skiena §8.5 + CLRS Ch24 |
| 14 | *(nâng cao)* Thuật toán ngẫu nhiên | randomized quicksort, Monte Carlo | Skiena Ch6 |

**Hết tầng lõi (0–11).** Tầng nâng cao: khớp chuỗi dùng lại băm (Bài 3); luồng mạng tiếp đồ thị trọng số (Bài 8); thuật toán ngẫu nhiên nối pivot ngẫu nhiên (Bài 5).

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 11.1 — Lý thuyết NP-đầy đủ cho ta điều gì, dù chỉ là "kết quả phủ định"?
> **Đáp:** cho biết **khi nào ngừng tìm** thuật toán nhanh — việc tìm là *vô vọng* (Skiena tr. 355). Giúp tập trung sức lực, và chuyển sang giải pháp thực dụng thay vì húc đầu tìm cái không tồn tại.

> [!question] Thẻ 11.2 — Rút gọn (reduction) là gì? Dùng để làm gì?
> **Đáp:** biến bài A thành bài B (đa thức) sao cho lời giải B cho ra lời giải A → "A không khó hơn B". Nếu A đã biết khó thì B cũng khó. Cho thấy hai bài **tương đương** về độ khó (Skiena tr. 355).

> [!question] Thẻ 11.3 — Phân biệt P, NP, NP-đầy đủ.
> **Đáp:** **P** = giải được đa thức. **NP** = *kiểm* được đa thức (tìm có thể khó). **NP-đầy đủ** = khó nhất trong NP; mọi bài NP rút gọn về chúng (SAT, TSP, vertex cover). Giải nhanh một cái ⟹ giải nhanh mọi bài NP.

> [!question] Thẻ 11.4 — Câu hỏi P vs NP hỏi gì? Ta tin điều gì?
> **Đáp:** liệu **kiểm chứng** có thực sự dễ hơn **khám phá** (Skiena tr. 380). P = NP nghĩa mọi bài kiểm-dễ cũng giải-dễ. Hầu hết tin **P ≠ NP** nhưng chưa ai chứng minh.

> [!question] Thẻ 11.5 — Ba lối thoát khi gặp bài NP-khó?
> **Đáp:** (1) **nhanh ca trung bình** (backtracking + pruning — giữ tối ưu, bỏ bảo đảm worst case); (2) **heuristic** (nhanh, không bảo đảm tối ưu); (3) **xấp xỉ** (đa thức + bảo đảm gần tối ưu, vd ≤ 2×) (Skiena tr. 389).

## 8. Câu hỏi tự kiểm tra

1. Vì sao biết một bài là NP-khó lại *hữu ích* dù chỉ là kết quả phủ định? *(mục 1)*
2. Giải thích rút gọn A→B. Nếu B giải nhanh thì sao? Nếu A đã biết khó thì sao? *(mục 2)*
3. Phân biệt P, NP, NP-đầy đủ bằng lời của bạn. SAT thuộc lớp nào? *(mục 2)*
4. "Tìm khó, kiểm dễ" nghĩa là gì? Minh hoạ bằng TSP và SAT. *(mục 3)*
5. Chạy demo mục 5. Vì sao 2-approximation vertex cover cho 4 chứ không 3, và vì sao vẫn chấp nhận được? *(mục 4 & 5)*

## Tóm tắt một trang

```
BÀI 11 — NP-ĐẦY ĐỦ & BÀI TOÁN KHÓ (khép tầng lõi)
─────────────────────────────────────────────────────────
VẤN ĐỀ  có bài (TSP, xếp lịch, SAT) ko ai biết giải NHANH. NP-đầy đủ = công cụ
   CHỨNG MINH khi nào nên NGỪNG tìm (kết quả phủ định nhưng cực hữu ích, tr.355).

RÚT GỌN (reduction)  biến A→B đa thức: B nhanh ⟹ A nhanh; A khó ⟹ B khó.
   Hai bài TƯƠNG ĐƯƠNG độ khó (Skiena tr.355).

LỚP  P = giải đa thức (sort/BFS/Dijkstra/QHĐ). NP = KIỂM đa thức. NP-ĐẦY ĐỦ =
   khó nhất NP, mọi bài NP rút về chúng (SAT, TSP, vertex cover). Giải nhanh
   1 cái ⟹ giải nhanh TẤT CẢ.

P vs NP  kiểm có dễ hơn tìm không? (Skiena tr.380). Tin P≠NP, chưa ai chứng
   minh (giải Clay triệu đô).

GẶP NP-KHÓ (ko phải điểm dừng, tr.389)  3 lối: (1) nhanh-ca-TB backtrack+prune
   (giữ tối ưu); (2) HEURISTIC (nhanh, ko bảo đảm); (3) XẤP XỈ (đa thức +
   bảo đảm ≤ hệ số × tối ưu).

DEMO  SAT: tìm quét tới 2^n, KIỂM chỉ duyệt mệnh đề (ruột P vs NP). Vertex
   cover: chính xác 3 (mũ) vs 2-approx 4 (đa thức, ≤ 2×tối ưu).
```

## Nguồn

- **Skiena, Steven S. — *The Algorithm Design Manual*, 3rd ed.** (Springer, 2020) — **Chapter 11: NP-Completeness** (rút gọn, SAT, P vs NP) **và Chapter 12: Dealing with Hard Problems** (nhanh-ca-trung-bình, heuristic, thuật toán xấp xỉ): lý thuyết độ khó và ba lối thoát thực dụng. `tai_lieu/The Algorithm Design Manual 3rd Edition...pdf` (offset **PDF = tr. + 13** ở Ch11–12).
- Liên hệ: [Bài 10 — backtracking](bai_10_backtracking.md) (vét mũ + pruning); [Bài 8 — greedy](bai_08_do-thi-trong-so.md) (heuristic tham lam); [sre](../../sre/README.md) & [cloud-base](../../cloud-base/README.md) (bài vận hành NP-khó trá hình: bin packing, lập lịch).

---

**Bản đồ khoá học:** [Bài 0 — Thuật toán & tính đúng](bai_00_thuat-toan-la-gi.md) · [Bài 1 — Phân tích Big-O](bai_01_big-o.md) · [Bài 2 — CTDL tuyến tính](bai_02_ctdl-tuyen-tinh.md) · [Bài 3 — Từ điển & bảng băm](bai_03_bang-bam.md) · [Bài 4 — Heap & cây tìm kiếm](bai_04_heap-cay-tim-kiem.md) · [Bài 5 — Sắp xếp](bai_05_sap-xep.md) · [Bài 6 — Chia để trị & đệ quy](bai_06_chia-de-tri.md) · [Bài 7 — Đồ thị: duyệt](bai_07_do-thi-duyet.md) · [Bài 8 — Đồ thị trọng số](bai_08_do-thi-trong-so.md) · [Bài 9 — Quy hoạch động](bai_09_quy-hoach-dong.md) · [Bài 10 — Backtracking](bai_10_backtracking.md) · **[Bài 11 — NP-đầy đủ] ← bạn đang ở đây** · [Bài 12 — Khớp chuỗi](bai_12_khop-chuoi.md) · [Bài 13 — Luồng mạng](bai_13_luong-mang.md) · [Bài 14 — Thuật toán ngẫu nhiên](bai_14_ngau-nhien.md)

Xem thêm [README khoá học](../README.md).
