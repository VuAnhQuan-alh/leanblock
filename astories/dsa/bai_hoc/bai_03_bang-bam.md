# Bài 3 — Từ điển và bảng băm: tra cứu theo khoá trong O(1)

> [!info] Về bài này
> Bài 2 lo chuyện *cất và lấy theo thứ tự* (container). Bài này lo chuyện khác hẳn: **tra theo nội dung** — cho một *khoá* (tên, mã, URL), trả về *giá trị* gắn với nó. Đó là **từ điển** *(dictionary)*, cấu trúc dữ liệu được dùng nhiều nhất trong lập trình thực tế (`Map`, `dict`, `HashMap`, object của JS đều là nó). Câu hỏi trung tâm: làm sao tra cứu trong **O(1)** thay vì quét cả `n` phần tử? Câu trả lời là **băm** *(hashing)* — biến khoá thành chỉ số mảng.
> Nguồn (Luật số 1): **Skiena** *The Algorithm Design Manual 3e* — **Chapter 3 §3.3 Dictionaries, §3.7 Hashing** (`tai_lieu/`, trích `> [!quote] Skiena (tr. N)`, **PDF = tr. + 16** ở Ch3).
> **Chạy demo:** `node bai_03.ts` — Node 22+, không cài gói. Code tất định.
> Cần đọc trước: [Bài 2 — CTDL tuyến tính](bai_02_ctdl-tuyen-tinh.md) (bảng băm dùng mảng + danh sách liên kết).

## Mục lục

1. [Tình huống: tra cứu trong danh bạ phình to](#1-tình-huống-tra-cứu-trong-danh-bạ-phình-to)
2. [Từ điển: ADT tra theo khoá](#2-từ-điển-adt-tra-theo-khoá)
3. [Bảng băm: biến khoá thành chỉ số](#3-bảng-băm-biến-khoá-thành-chỉ-số)
4. [Va chạm là tất yếu: chaining và open addressing](#4-va-chạm-là-tất-yếu-chaining-và-open-addressing)
5. [Demo: bảng băm chaining từ đầu](#5-demo-bảng-băm-chaining-từ-đầu)
6. [Bản đồ khoá DSA](#6-bản-đồ-khoá-dsa)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Tình huống: tra cứu trong danh bạ phình to

> [!example] Danh bạ 1 triệu số
> Bạn có danh bạ: tên → số điện thoại. Lưu vào một mảng chưa sắp, tra một tên là **quét tuyến tính** — worst case `n` bước (Bài 1). Với 1 triệu mục, mỗi lần tra có thể duyệt cả triệu.
>
> Sắp xếp mảng theo tên rồi tìm nhị phân? Tra còn `log n` (~20 bước) — tốt hơn nhiều, nhưng mỗi lần *thêm* một tên mới phải chèn đúng chỗ, dịch cả đuôi mảng O(n). Có cách nào tra **và** thêm đều gần như tức thì không?

Có — nếu biến khoá "An" thành thẳng một **chỉ số mảng** rồi nhảy tới đó. Đó là ý tưởng bảng băm (mục 3). Trước hết, định nghĩa cho rõ cái ta đang cần: **từ điển**.

## 2. Từ điển: ADT tra theo khoá

Ở Bài 2, container (stack/queue) lấy dữ liệu ra *không cần biết nội dung*. **Từ điển** thì ngược lại — truy xuất **dựa trên khoá**. Skiena liệt kê bảy thao tác nền của một từ điển:

> [!quote] Skiena (tr. 77)
> "What are the asymptotic worst-case running times for all seven fundamental dictionary operations (search, insert, delete, successor, predecessor, minimum, and maximum)[?]"
>
> *Thời gian chạy worst-case tiệm cận của cả **bảy thao tác từ điển nền tảng** (tìm, chèn, xoá, kế sau, kế trước, nhỏ nhất, lớn nhất) là bao nhiêu[?]*

Ba thao tác đầu — **search / insert / delete** — là cốt lõi và là thứ bài này tối ưu. Bốn thao tác sau (successor, predecessor, min, max) cần *thứ tự* giữa các khoá; bảng băm **không** hỗ trợ tốt chúng (sẽ thấy vì sao ở mục 4), và đó là lý do ta vẫn cần cây tìm kiếm ở [Bài 4](bai_04_heap-cay-tim-kiem.md). Mỗi cách cài từ điển là một bộ đánh đổi khác nhau trên bảng bảy thao tác này:

| Cài đặt từ điển | search | insert | thao tác thứ tự (min/successor…) |
| :-- | :-- | :-- | :-- |
| mảng chưa sắp | O(n) | O(1) | O(n) |
| mảng đã sắp | O(log n) | O(n) | O(1)–O(log n) |
| **bảng băm** | **O(1)** kỳ vọng | **O(1)** kỳ vọng | O(n) — *không hợp* |
| cây tìm kiếm cân bằng (Bài 4) | O(log n) | O(log n) | O(log n) |

## 3. Bảng băm: biến khoá thành chỉ số

Nhận xét chốt: tra một phần tử trong mảng khi **đã biết chỉ số** là O(1) (Bài 2). Nếu có cách *tính* chỉ số thẳng từ khoá, ta tra tức thì. Cái máy tính đó là **hàm băm**.

> [!quote] Skiena (tr. 93)
> "Hash tables are a very practical way to maintain a dictionary. They exploit the fact that looking an item up in an array takes constant time once you have its index. A hash function is a mathematical function that maps keys to integers."
>
> *Bảng băm là cách rất thực dụng để duy trì một từ điển. Chúng khai thác sự thật rằng **tra một phần tử trong mảng tốn thời gian hằng số một khi đã có chỉ số**. Một **hàm băm** là hàm toán học **ánh xạ khoá thành số nguyên**.*

Hai bước:

1. **Khoá → số nguyên lớn.** Coi chuỗi như một số trong hệ cơ số `α` (`α` = cỡ bảng chữ cái): mỗi ký tự là một "chữ số". Chuỗi khác nhau ra số khác nhau (gần như luôn).
2. **Số lớn → chỉ số 0..m−1.** Lấy phần dư: `H'(S) = H(S) mod m`, với `m` = số ô của bảng. Skiena ví như bánh xe roulette — viên bi lăn một quãng dài rồi dừng ở một ô "ngẫu nhiên".

```
khoá "An"  ──H──►  số nguyên lớn  ──mod m──►  chỉ số ô (vd 5)  ──►  mảng[5]
            cơ số α                 m = số ô                        tra O(1)
```

Chọn `m` khéo thì các chỉ số trải đều. Skiena khuyên lý tưởng `m` là **số nguyên tố lớn**, không quá gần `2^i − 1` (tr. 93) — demo mục 5 cho thấy `m` là luỹ thừa 2 trải *lệch* hơn hẳn `m` nguyên tố.

## 4. Va chạm là tất yếu: chaining và open addressing

Hai khoá khác nhau vẫn có thể ra cùng một chỉ số — gọi là **va chạm** *(collision)*. Không hàm băm nào tránh được: ánh xạ vô hạn khoá có thể vào `m` ô hữu hạn thì kiểu gì cũng đụng (nguyên lý chuồng bồ câu).

> [!quote] Skiena (tr. 93)
> "No matter how good our hash function is, we had better be prepared for collisions, because two distinct keys will at least occasionally hash to the same value."
>
> *Dù hàm băm tốt đến đâu, ta vẫn nên **chuẩn bị cho va chạm**, vì hai khoá phân biệt **chí ít thỉnh thoảng** sẽ băm ra cùng một giá trị.*

Có hai cách xử lý va chạm:

- **Chaining (móc xích):** mỗi ô là một **danh sách liên kết** (Bài 2) chứa mọi khoá băm vào ô đó. Tra/chèn/xoá quy về thao tác trên danh sách của đúng ô.

> [!quote] Skiena (tr. 93)
> "Chaining represents a hash table as an array of m linked lists [...] If the n keys are distributed uniformly in a table, each list will contain roughly n/m elements"
>
> *Chaining biểu diễn bảng băm như một **mảng `m` danh sách liên kết** (mỗi danh sách là một "bucket") [...] Nếu `n` khoá trải đều trong bảng, mỗi danh sách chứa **khoảng `n/m` phần tử**.*

- **Open addressing (địa chỉ mở):** không dùng danh sách; khi ô đã kẹt thì **dò sang ô kế** theo một quy tắc tới khi gặp ô trống. Tốn ít bộ nhớ hơn (không có con trỏ), locality/cache tốt hơn — Skiena nói *"the highest-performing hash tables generally rely on ... open addressing"* (tr. 93).

Tỉ số **`α = n/m`** gọi là **hệ số tải** *(load factor)* — số khoá trung bình mỗi ô. Với chaining, tìm kiếm *kỳ vọng* là **O(n/m) = O(α)**; giữ `m ≈ n` (α hằng số) thì tra cứu kỳ vọng **O(1)**. Đây là lý do `Map`/`HashMap` tự **phóng to bảng** (rehash) khi α vượt ngưỡng — đúng trò gấp đôi mảng động ở Bài 2.

> [!quote] Skiena (tr. 95)
> "Pragmatically, a hash table often is the best data structure to maintain a dictionary."
>
> *Trên thực tế, bảng băm **thường là cấu trúc dữ liệu tốt nhất** để duy trì một từ điển.*

> [!note] Vì sao bảng băm chịu thua ở thao tác "thứ tự"
> Băm *cố tình* phá thứ tự khoá — rải chúng ngẫu nhiên khắp bảng để tránh va chạm. Nên "khoá nhỏ nhất", "khoá kế sau khoá x", hay "liệt kê theo thứ tự" đều phải quét cả bảng O(n + m). Khi cần *cả* tra nhanh *lẫn* duyệt có thứ tự (vd: index của [database](../../database/README.md) phải trả về dải khoá đã sắp), người ta dùng **B+tree** thay vì bảng băm — mạch này nối thẳng sang [Bài 4](bai_04_heap-cay-tim-kiem.md) và khoá database.

## 5. Demo: bảng băm chaining từ đầu

Demo dựng một bảng băm chaining (hàm băm đa thức cơ số 31), nhét 12 khoá vào 8 ô để **thấy va chạm**, in phân bố + hệ số tải, đo số bước tra cứu (chỉ quét *một* ô) so với quét tuyến tính cả mảng, và so `m=8` (luỹ thừa 2) với `m=11` (nguyên tố).

```typescript
import { strict as assert } from "node:assert";

// ─── BẢNG BĂM với CHAINING (mỗi ô là một danh sách "bucket") ───
// Khoá là chuỗi → băm ra số nguyên → mod m để ra chỉ số ô.
class HashTable {
  private buckets: Array<Array<[string, string]>>;
  private m: number;
  public size: number;

  constructor(m: number) {
    this.m = m;
    this.buckets = Array.from({ length: m }, () => []);
    this.size = 0;
  }

  // Hàm băm đa thức cơ số 31 (coi ký tự như "chữ số"), rồi mod m.
  hash(key: string): number {
    let h = 0;
    for (const ch of key) h = (h * 31 + ch.charCodeAt(0)) % this.m;
    return h;
  }

  set(key: string, value: string): void {
    const b = this.buckets[this.hash(key)];
    const found = b.find((pair) => pair[0] === key);
    if (found) found[1] = value;
    else { b.push([key, value]); this.size++; }
  }

  // Trả giá trị + số lần so sánh (độ dài quãng phải đi trong bucket).
  get(key: string): { value: string | null; steps: number } {
    const b = this.buckets[this.hash(key)];
    let steps = 0;
    for (const [k, v] of b) { steps++; if (k === key) return { value: v, steps }; }
    return { value: null, steps };
  }

  distribution(): number[] {
    return this.buckets.map((b) => b.length);
  }
}

// Danh bạ: tên → số máy lẻ. 12 mục, bảng 8 ô → chắc chắn có va chạm.
const entries: Array<[string, string]> = [
  ["An", "101"], ["Binh", "102"], ["Cuong", "103"], ["Dung", "104"],
  ["Hoa", "105"], ["Khanh", "106"], ["Lan", "107"], ["Minh", "108"],
  ["Nam", "109"], ["Oanh", "110"], ["Phuc", "111"], ["Quang", "112"],
];
const m = 8;
const ht = new HashTable(m);
for (const [k, v] of entries) ht.set(k, v);

console.log(`BẢNG BĂM CHAINING — ${entries.length} khoá vào ${m} ô:`);
const dist = ht.distribution();
for (let i = 0; i < m; i++) {
  const keys = entries.filter(([k]) => ht.hash(k) === i).map(([k]) => k);
  console.log(`  ô ${i}: ${dist[i]} khoá  [${keys.join(", ")}]`);
}

const alpha = ht.size / m;
const collisions = dist.filter((len) => len > 1).reduce((s, len) => s + (len - 1), 0);
console.log(`\n  hệ số tải α = n/m = ${ht.size}/${m} = ${alpha.toFixed(2)}`);
console.log(`  số va chạm (khoá phải xếp sau khoá khác cùng ô) = ${collisions}`);

// ─── TRA CỨU: bảng băm chỉ đi trong MỘT bucket, không quét cả 12 khoá ───
console.log("\nTRA CỨU (số lần so sánh):");
for (const name of ["An", "Quang", "Minh"]) {
  const r = ht.get(name);
  console.log(`  get("${name}") = ${r.value}  trong ${r.steps} bước (chỉ quét ô ${ht.hash(name)})`);
}

// So với "từ điển" bằng mảng chưa sắp: tra = quét tuyến tính, worst case = n.
function arrayLookup(arr: Array<[string, string]>, key: string): number {
  let steps = 0;
  for (const [k] of arr) { steps++; if (k === key) break; }
  return steps;
}
const worstArray = arrayLookup(entries, "Quang"); // phần tử cuối
const worstHash = ht.get("Quang").steps;
console.log(`\n  tra "Quang" (khoá cuối):  mảng chưa sắp = ${worstArray} bước,  bảng băm = ${worstHash} bước`);

// ─── KÍCH THƯỚC BẢNG: luỹ thừa 2 trải lệch, số nguyên tố trải đều hơn ───
// Skiena: "ideally m is a large prime not too close to 2^i − 1" (tr.93).
function maxChain(tableSize: number): number {
  const t = new HashTable(tableSize);
  for (const [k, v] of entries) t.set(k, v);
  return Math.max(...t.distribution());
}
console.log("\nKÍCH THƯỚC BẢNG ảnh hưởng độ dài ô dài nhất (12 khoá):");
console.log(`  m = 8  (luỹ thừa 2):   ô dài nhất = ${maxChain(8)} khoá`);
console.log(`  m = 11 (số nguyên tố): ô dài nhất = ${maxChain(11)} khoá  ← trải đều hơn`);

// Kiểm: tổng độ dài các bucket = số khoá; tra bảng băm rẻ hơn hẳn quét mảng.
assert.equal(dist.reduce((a, b) => a + b, 0), entries.length);
assert.equal(ht.get("An").value, "101");
assert.equal(ht.get("Zzz").value, null);
assert.ok(worstHash < worstArray);
assert.ok(maxChain(11) < maxChain(8));       // nguyên tố trải đều hơn luỹ thừa 2

console.log("\nBăm tốt + m nguyên tố → mỗi ô ~α khoá → tra kỳ vọng O(n/m) ~ O(1) khi m ≈ n (Skiena tr.95).");
```

Kết quả chạy thật *(tất định)*:

```
BẢNG BĂM CHAINING — 12 khoá vào 8 ô:
  ô 0: 0 khoá  []
  ô 1: 2 khoá  [Binh, Lan]
  ô 2: 3 khoá  [Dung, Hoa, Nam]
  ô 3: 0 khoá  []
  ô 4: 1 khoá  [Oanh]
  ô 5: 1 khoá  [An]
  ô 6: 5 khoá  [Cuong, Khanh, Minh, Phuc, Quang]
  ô 7: 0 khoá  []

  hệ số tải α = n/m = 12/8 = 1.50
  số va chạm (khoá phải xếp sau khoá khác cùng ô) = 7

TRA CỨU (số lần so sánh):
  get("An") = 101  trong 1 bước (chỉ quét ô 5)
  get("Quang") = 112  trong 5 bước (chỉ quét ô 6)
  get("Minh") = 108  trong 3 bước (chỉ quét ô 6)

  tra "Quang" (khoá cuối):  mảng chưa sắp = 12 bước,  bảng băm = 5 bước

KÍCH THƯỚC BẢNG ảnh hưởng độ dài ô dài nhất (12 khoá):
  m = 8  (luỹ thừa 2):   ô dài nhất = 5 khoá
  m = 11 (số nguyên tố): ô dài nhất = 3 khoá  ← trải đều hơn

Băm tốt + m nguyên tố → mỗi ô ~α khoá → tra kỳ vọng O(n/m) ~ O(1) khi m ≈ n (Skiena tr.95).
```

Bốn điều đáng thấm. **(1) Va chạm có thật và không đều:** 12 khoá vào 8 ô sinh 7 va chạm; ô 6 dồn tới 5 khoá trong khi ba ô trống trơn — băm *không* đảm bảo đều tuyệt đối, chỉ đều *kỳ vọng*. **(2) Tra cứu chỉ chạm một ô:** `get("An")` 1 bước, `get("Quang")` 5 bước (vì rơi vào ô đông) — luôn ≤ độ dài ô đó, *không* phải cả 12 khoá; so quét mảng chưa sắp tới `Quang` tốn trọn 12 bước. **(3) Kích thước bảng là tham số quan trọng:** đúng 12 khoá đó, `m=8` (luỹ thừa 2) cho ô dài nhất 5, còn `m=11` (nguyên tố) chỉ 3 — khớp lời khuyên "m là số nguyên tố" của Skiena. **(4) Giữ α nhỏ là chìa khoá O(1):** ô càng ngắn tra càng nhanh; muốn vậy phải tăng `m` khi `n` tăng (rehash) — chính là mảng động của Bài 2 áp vào bảng băm.

> [!note] Tự thử
> 1. Tăng bảng lên `m = 16` rồi `m = 13`: hệ số tải và ô dài nhất đổi thế nào? Số nguyên tố có còn trải đều hơn không?
> 2. Hàm băm "ngu": đổi `hash` thành `return 0` (mọi khoá vào ô 0). Giờ `get` tốn bao nhiêu? Bảng băm suy biến thành cấu trúc gì của Bài 2?
> 3. Thêm thao tác `delete(key)` cho `HashTable`. Vì sao với chaining nó dễ, còn với open addressing lại rắc rối (gợi ý: xoá tạo "lỗ hổng" làm đứt chuỗi dò)?
> 4. Vì sao không thể dùng bảng băm để trả lời "liệt kê 3 tên theo thứ tự abc"? Thao tác nào của bảng bảy-thao-tác bị hỏng? *(mục 2 & 4)*

## 6. Bản đồ khoá DSA

| # | Bài | Chủ đề | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | Thuật toán & tính đúng | nền: đúng vs hiệu quả | Skiena Ch1 + Grokking |
| 1 | Phân tích Big-O | đo chi phí khi `n` lớn | Skiena Ch2 |
| 2 | CTDL tuyến tính | mảng / list / stack / queue | Skiena Ch3 |
| 3 | **Từ điển & bảng băm** ← *đang ở đây* | tra cứu O(1) trung bình | Skiena Ch3 |
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

Bảng băm và khớp chuỗi gặp lại nhau ở [Bài 12](bai_12_khop-chuoi.md) (Rabin–Karp băm cửa sổ trượt).

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 3.1 — Từ điển (dictionary) khác container (stack/queue) ở đâu?
> **Đáp:** container lấy ra *không cần biết nội dung* (theo thứ tự chèn); từ điển truy xuất **theo khoá/nội dung**. Bảy thao tác nền: search, insert, delete, successor, predecessor, min, max (Skiena tr. 77).

> [!question] Thẻ 3.2 — Hàm băm làm gì, và vì sao cho tra cứu O(1)?
> **Đáp:** **ánh xạ khoá thành số nguyên**, rồi `mod m` thành chỉ số ô; tra mảng khi đã có chỉ số là O(1), nên tra từ điển thành O(1) kỳ vọng (Skiena tr. 93).

> [!question] Thẻ 3.3 — Va chạm (collision) là gì? Vì sao không tránh được?
> **Đáp:** hai khoá khác nhau băm ra cùng chỉ số. Vô hạn khoá vào `m` ô hữu hạn → chuồng bồ câu → kiểu gì cũng đụng; phải *chuẩn bị* cho nó (Skiena tr. 93).

> [!question] Thẻ 3.4 — Chaining và open addressing khác nhau ra sao? Hệ số tải α là gì?
> **Đáp:** **chaining** = mỗi ô một danh sách liên kết chứa mọi khoá vào ô đó; **open addressing** = dò sang ô kế khi kẹt (ít bộ nhớ, cache tốt). **α = n/m** = số khoá TB mỗi ô; search chaining kỳ vọng O(α), giữ α hằng số thì O(1) (Skiena tr. 93–95).

> [!question] Thẻ 3.5 — Vì sao bảng băm kém ở thao tác "thứ tự" (min, successor)? Dùng gì thay?
> **Đáp:** băm rải khoá ngẫu nhiên, phá thứ tự → min/successor phải quét cả bảng O(n+m). Cần tra nhanh *và* duyệt có thứ tự thì dùng **cây tìm kiếm cân bằng / B+tree** (Bài 4, khoá database).

## 8. Câu hỏi tự kiểm tra

1. So ba cách cài từ điển (mảng chưa sắp, mảng đã sắp, bảng băm) trên search và insert. Cái nào thắng ở đâu? *(mục 2)*
2. Mô tả hai bước của một hàm băm chuỗi: khoá → số lớn → chỉ số. Vì sao bước `mod m` cần thiết? *(mục 3)*
3. Va chạm là gì? Giải thích vì sao dù hàm băm hoàn hảo vẫn phải xử lý va chạm. *(mục 4)*
4. Hệ số tải α ảnh hưởng thời gian tra cứu thế nào? Vì sao `Map`/`HashMap` phải rehash khi α lớn? *(mục 4)*
5. Chạy demo mục 5. Vì sao `m=11` cho ô dài nhất ngắn hơn `m=8` với cùng 12 khoá? *(mục 3 & 5)*

## Tóm tắt một trang

```
BÀI 3 — TỪ ĐIỂN & BẢNG BĂM
─────────────────────────────────────────────────────────
TỪ ĐIỂN (dictionary)  tra theo KHOÁ (khác container tra theo thứ tự chèn). 7
   thao tác: search/insert/delete + successor/predecessor/min/max (Skiena tr.77).

BẢNG BĂM  hàm băm ánh xạ KHOÁ → SỐ NGUYÊN → mod m → CHỈ SỐ ô; tra mảng theo
   chỉ số là O(1) → tra từ điển O(1) kỳ vọng (Skiena tr.93). m nên là SỐ
   NGUYÊN TỐ lớn để trải đều.

VA CHẠM  hai khoá → cùng ô; KHÔNG tránh được (chuồng bồ câu). Hai cách xử lý:
   CHAINING = mỗi ô một danh sách liên kết; OPEN ADDRESSING = dò ô kế (ít RAM,
   cache tốt, bảng nhanh nhất hay dùng).

HỆ SỐ TẢI α = n/m  số khoá TB mỗi ô. Search chaining kỳ vọng O(α); giữ m ≈ n
   (α hằng) → O(1). Tăng n thì REHASH phóng to bảng (= mảng động Bài 2).

ĐIỂM YẾU  băm phá thứ tự → min/successor/duyệt-có-thứ-tự = O(n+m). Cần cả tra
   nhanh LẪN thứ tự → dùng cây/B+tree (Bài 4, database). "Pragmatically, a hash
   table often is the best" cho từ điển thuần (Skiena tr.95).

DEMO  12 khoá / 8 ô → 7 va chạm, ô 6 dồn 5 khoá. get chỉ quét MỘT ô (1–5 bước)
   vs quét mảng 12. m=8 → ô dài nhất 5; m=11 → 3.
```

## Nguồn

- **Skiena, Steven S. — *The Algorithm Design Manual*, 3rd ed.** (Springer, 2020) — **Chapter 3 §3.3 Dictionaries, §3.7 Hashing**: ADT từ điển & bảy thao tác, bảng chi phí theo cài đặt, hàm băm (khoá → số → mod m), va chạm, chaining vs open addressing, hệ số tải & thời gian kỳ vọng O(n/m). `tai_lieu/The Algorithm Design Manual 3rd Edition...pdf` (offset **PDF = tr. + 16** ở Ch3).
- Liên hệ: [database — B+tree & index](../../database/README.md) cho thấy khi nào chọn cây thay vì băm (cần dải khoá có thứ tự); [Bài 12 — Khớp chuỗi](bai_12_khop-chuoi.md) dùng băm cho Rabin–Karp.

---

**Bản đồ khoá học:** [Bài 0 — Thuật toán & tính đúng](bai_00_thuat-toan-la-gi.md) · [Bài 1 — Phân tích Big-O](bai_01_big-o.md) · [Bài 2 — CTDL tuyến tính](bai_02_ctdl-tuyen-tinh.md) · **[Bài 3 — Từ điển & bảng băm] ← bạn đang ở đây** · [Bài 4 — Heap & cây tìm kiếm](bai_04_heap-cay-tim-kiem.md) · [Bài 5 — Sắp xếp](bai_05_sap-xep.md) · [Bài 6 — Chia để trị & đệ quy](bai_06_chia-de-tri.md) · [Bài 7 — Đồ thị: duyệt](bai_07_do-thi-duyet.md) · [Bài 8 — Đồ thị trọng số](bai_08_do-thi-trong-so.md) · [Bài 9 — Quy hoạch động](bai_09_quy-hoach-dong.md) · [Bài 10 — Backtracking](bai_10_backtracking.md) · [Bài 11 — NP-đầy đủ](bai_11_np-day-du.md) · [Bài 12 — Khớp chuỗi](bai_12_khop-chuoi.md) · [Bài 13 — Luồng mạng](bai_13_luong-mang.md) · [Bài 14 — Thuật toán ngẫu nhiên](bai_14_ngau-nhien.md)

Xem thêm [README khoá học](../README.md).
