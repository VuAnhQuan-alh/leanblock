# Bài 4 — Heap và cây tìm kiếm: tra nhanh có thứ tự, lấy min/max tức thì

> [!info] Về bài này
> Bài 3 cho bảng băm — tra theo khoá O(1), nhưng *phá thứ tự* nên bó tay với "khoá nhỏ nhất", "khoá kế sau", "liệt kê có thứ tự". Bài này xây hai cấu trúc *giữ thứ tự*: **cây tìm kiếm nhị phân (BST)** cho tra-cứu-và-cập-nhật đều O(log n) *có thứ tự*, và **heap** cho lấy phần tử nhỏ nhất/lớn nhất lặp đi lặp lại cực nhanh (hàng đợi ưu tiên). Cả hai là nền của những bài sau: heap đẻ ra heapsort (Bài 5) và Dijkstra (Bài 8); BST cân bằng chính là ý tưởng B+tree của [khoá database](../../database/README.md).
> Nguồn (Luật số 1): **Skiena** *The Algorithm Design Manual 3e* — **Ch3 §3.4 Binary Search Trees, §3.5 Priority Queues** và **Ch4 §4.3 Heapsort** (`tai_lieu/`, trích `> [!quote] Skiena (tr. N)`, **PDF = tr. + 16** ở Ch3–4).
> **Chạy demo:** `node bai_04.ts` — Node 22+, không cài gói. Code tất định.
> Cần đọc trước: [Bài 2 — CTDL tuyến tính](bai_02_ctdl-tuyen-tinh.md), [Bài 3 — Từ điển & bảng băm](bai_03_bang-bam.md).

## Mục lục

1. [Tình huống: cần tra nhanh VÀ cập nhật linh hoạt](#1-tình-huống-cần-tra-nhanh-và-cập-nhật-linh-hoạt)
2. [Cây tìm kiếm nhị phân: trái nhỏ, phải lớn](#2-cây-tìm-kiếm-nhị-phân-trái-nhỏ-phải-lớn)
3. [Cân bằng hay suy biến: vì sao chiều cao quyết định tất cả](#3-cân-bằng-hay-suy-biến-vì-sao-chiều-cao-quyết-định-tất-cả)
4. [Hàng đợi ưu tiên và heap](#4-hàng-đợi-ưu-tiên-và-heap)
5. [Demo: BST và min-heap](#5-demo-bst-và-min-heap)
6. [Bản đồ khoá DSA](#6-bản-đồ-khoá-dsa)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Tình huống: cần tra nhanh VÀ cập nhật linh hoạt

> [!example] Không cấu trúc nào ở Bài 2–3 làm tốt cả hai
> Bạn cần một cấu trúc vừa *tra nhanh* vừa *thêm/xoá linh hoạt* vừa *trả về theo thứ tự*. Nhìn lại kho đã có: danh sách liên kết chưa sắp thêm/xoá O(1) nhưng tra O(n). Mảng đã sắp tra O(log n) (nhị phân) nhưng chèn O(n) (phải dịch đuôi). Bảng băm tra O(1) nhưng mất hết thứ tự. Mỗi cái giỏi một nửa.

Skiena đặt vấn đề y hệt khi mở phần cây tìm kiếm:

> [!quote] Skiena (tr. 81)
> "We have seen data structures that allow fast search or flexible update, but not fast search and flexible update."
>
> *Ta đã thấy những cấu trúc cho phép **tra nhanh** hoặc **cập nhật linh hoạt**, nhưng không có cái nào cho cả **tra nhanh lẫn cập nhật linh hoạt**.*

**Cây tìm kiếm nhị phân** là câu trả lời cho nhu cầu "cả hai *và* có thứ tự". **Heap** là câu trả lời cho một nhu cầu hẹp hơn nhưng cực phổ biến: *liên tục lấy ra phần tử nhỏ nhất (hoặc lớn nhất)*.

## 2. Cây tìm kiếm nhị phân: trái nhỏ, phải lớn

**Cây tìm kiếm nhị phân (BST)** là cây nhị phân có một bất biến đơn giản mà mạnh:

> [!quote] Skiena (tr. 81)
> "All nodes in the left (resp. right) subtree of node x have keys < x (resp. > x)."
>
> *Mọi nút trong cây con **trái** (tương ứng **phải**) của nút x đều có khoá **nhỏ hơn x** (tương ứng **lớn hơn x**).*

```
             5
           /   \
         3       8          BST: mọi khoá bên TRÁI một nút < nút đó
        / \     / \              mọi khoá bên PHẢI > nút đó
       2   4   7   9
      /       /
     1       6    ← chèn 6: 6>5 rẽ phải (→8), 6<8 rẽ trái (→7), 6<7 rẽ trái → ô này
```

Bất biến này biến **tìm kiếm** thành đúng trò đoán số của Bài 0: ở mỗi nút, so khoá cần tìm với khoá nút — nhỏ hơn thì rẽ **trái**, lớn hơn rẽ **phải**, bằng thì xong. Mỗi bước *cắt bỏ một cây con*, nên số bước = **chiều cao cây**. Thêm/xoá cũng đi theo đúng đường đó rồi gắn/gỡ nút — nên *cập nhật* cũng tốn bằng chiều cao.

Một tính chất đẹp miễn phí: **duyệt in-order** (trái → nút → phải) cho ra khoá theo **thứ tự tăng dần**. Đây chính là thao tác "thứ tự" mà bảng băm không làm được (Bài 3) — và là lý do index cơ sở dữ liệu dùng cây chứ không dùng băm khi cần quét dải.

## 3. Cân bằng hay suy biến: vì sao chiều cao quyết định tất cả

Mọi chi phí BST đều là **O(chiều cao)**. Vậy chiều cao là bao nhiêu? Tuỳ **thứ tự chèn**, và đây là chỗ BST có thể sập bẫy:

- Chèn khéo (khoá tới xen kẽ): cây *tròn*, chiều cao ~`log₂ n`. Tra O(log n).
- Chèn xui (khoá tới **đã sắp sẵn** 1,2,3,...): mỗi nút mới luôn rẽ phải → cây thành một **xâu chuỗi thẳng đứng**, chiều cao `n`. Tra O(n) — tức BST suy biến đúng về danh sách liên kết của Bài 2!

```
chèn 5,3,8,2,4,...        chèn 1,2,3,4,5 (đã sắp)
      5                     1
    /   \                     \
   3     8     cao ~log n      2        cao = n
  / \   / \                     \       (suy biến thành
 2  4  7  9                       3       danh sách!)
                                   \
                                    4
```

Giải pháp là **cây cân bằng** (AVL, đỏ-đen, splay): sau mỗi lần chèn/xoá thì *xoay* lại một chút để giữ chiều cao luôn logarit.

> [!quote] Skiena (tr. 86)
> "Sophisticated balanced binary search tree data structures have been developed that guarantee the height of the tree always to be O(log n). Therefore, all dictionary operations (insert, delete, query) take O(log n) time each."
>
> *Những cấu trúc **cây tìm kiếm nhị phân cân bằng** tinh vi đã được phát triển, **bảo đảm chiều cao cây luôn là O(log n)**. Do đó mọi thao tác từ điển (chèn, xoá, truy vấn) tốn **O(log n)** mỗi thao tác.*

Điểm thực dụng: bạn hiếm khi phải *tự cài* cây đỏ-đen; coi nó như hộp đen cho từ điển có-thứ-tự O(log n). Nhưng chọn *sai* cấu trúc thì trả giá đắt:

> [!quote] Skiena (tr. 86)
> "Picking the wrong data structure for the job can be disastrous in terms of performance."
>
> *Chọn **sai** cấu trúc dữ liệu cho công việc có thể là **thảm hoạ** về hiệu năng.*

> [!note] Nối về khoá database
> BST cân bằng là ý tưởng gốc, nhưng trên **đĩa** mỗi lần "rẽ trái/phải" là một lần đọc đĩa đắt đỏ (Bài 1 — mô hình RAM nói dối). Để chiều cao thấp hơn nữa, [database dùng **B+tree**](../../database/README.md): mỗi nút chứa *hàng trăm* khoá thay vì một, nên cây chỉ cao 3–4 tầng cho hàng triệu khoá. Cùng tư tưởng "giữ cây thấp = ít bước", áp cho phần cứng thật.

## 4. Hàng đợi ưu tiên và heap

Nhiều thuật toán cần *liên tục lấy ra phần tử "cấp bách nhất"* — nhỏ nhất hay lớn nhất theo một khoá ưu tiên. Đó là **hàng đợi ưu tiên** *(priority queue)*, với ba thao tác:

> [!quote] Skiena (tr. 88)
> "the three basic priority queue operations (insert, find-minimum, and delete-minimum)"
>
> *ba thao tác hàng đợi ưu tiên cơ bản (**chèn**, **tìm nhỏ nhất**, **xoá nhỏ nhất**)*

Cài bằng mảng chưa sắp thì find-min O(n); bằng mảng đã sắp thì insert O(n). Cấu trúc làm *cả ba* trong O(log n) là **heap**:

> [!quote] Skiena (tr. 116)
> "Heaps are a simple and elegant data structure for efficiently supporting the priority queue operations insert and extract-min."
>
> *Heap là một cấu trúc dữ liệu **đơn giản và thanh lịch** hỗ trợ hiệu quả các thao tác hàng đợi ưu tiên **chèn** và **lấy-nhỏ-nhất**.*

Heap dựa trên một trật tự *yếu hơn* sắp xếp hoàn toàn (nên rẻ để duy trì) nhưng *đủ* để tìm min tức thì:

> [!quote] Skiena (tr. 116)
> "a heap-labeled tree is defined to be a binary tree such that the key of each node dominates the keys of its children. In a min-heap, a node dominates its children by having a smaller key than they do"
>
> *một **cây gán-nhãn-heap** là cây nhị phân sao cho khoá mỗi nút **trội** khoá các con của nó. Trong **min-heap**, một nút trội các con bằng cách có **khoá nhỏ hơn** chúng.*

Hai điểm tinh tế làm heap nhanh:

1. **Cây nhị phân đầy đủ** (mọi tầng kín, trừ tầng cuối dồn trái) → lưu *ngầm* trong một **mảng**, không cần con trỏ: con của nút `i` nằm ở `2i+1` và `2i+2`, cha ở `(i−1)/2`. Chiều cao luôn `log₂ n`.
2. **Chỉ cần trật tự cha–con**, không cần anh em có thứ tự. `insert`: thêm cuối mảng rồi *nổi lên* (bubble-up) tới khi cha nhỏ hơn. `extract-min`: lấy gốc (min), đưa phần tử cuối lên gốc rồi *chìm xuống* (sift-down) đổi với con nhỏ hơn. Cả hai đi dọc một đường gốc–lá → **O(log n)**.

Lấy min lặp lại cho tới hết = sắp xếp tăng dần. Skiena chỉ ra heapsort *"chỉ là selection sort cài bằng đúng cấu trúc dữ liệu"* (tr. 116) — ta gặp lại ở [Bài 5](bai_05_sap-xep.md).

## 5. Demo: BST và min-heap

Demo hai phần. **(1) BST:** dựng cùng 9 khoá theo hai thứ tự chèn — khéo (cây tròn) vs đã-sắp (suy biến), so chiều cao và số bước tìm; in-order luôn ra thứ tự tăng. **(2) Min-heap:** chèn 7 số, in mảng ngầm (gốc là min), rồi extract-min liên tục — ra đúng dãy tăng (heapsort).

```typescript
import { strict as assert } from "node:assert";

// ─── CÂY TÌM KIẾM NHỊ PHÂN (BST): trái < nút < phải ───
type TreeNode = { key: number; left: TreeNode | null; right: TreeNode | null };
class BST {
  root: TreeNode | null = null;

  insert(key: number): void {
    const node: TreeNode = { key, left: null, right: null };
    if (this.root === null) { this.root = node; return; }
    let cur = this.root;
    while (true) {
      if (key < cur.key) {
        if (cur.left === null) { cur.left = node; return; }
        cur = cur.left;
      } else {
        if (cur.right === null) { cur.right = node; return; }
        cur = cur.right;
      }
    }
  }

  // Tìm key, trả số nút phải so sánh (= độ sâu đã đi).
  search(key: number): number {
    let cur = this.root, steps = 0;
    while (cur !== null) {
      steps++;
      if (key === cur.key) return steps;
      cur = key < cur.key ? cur.left : cur.right;
    }
    return steps;
  }

  height(node: TreeNode | null = this.root): number {
    if (node === null) return 0;
    return 1 + Math.max(this.height(node.left), this.height(node.right));
  }

  inorder(node: TreeNode | null = this.root, out: number[] = []): number[] {
    if (node === null) return out;
    this.inorder(node.left, out);
    out.push(node.key);
    this.inorder(node.right, out);
    return out;
  }
}

// Cây CÂN BẰNG (thứ tự chèn khéo) vs cây SUY BIẾN (chèn theo thứ tự tăng dần).
const keys = [5, 3, 8, 2, 4, 7, 9, 1, 6];
const balanced = new BST();
for (const k of keys) balanced.insert(k);
const degenerate = new BST();
for (const k of [1, 2, 3, 4, 5, 6, 7, 8, 9]) degenerate.insert(k);  // chèn đã sắp → xâu chuỗi

console.log("CÂY TÌM KIẾM NHỊ PHÂN (BST) — 9 khoá:");
console.log(`  chèn khéo   → chiều cao = ${balanced.height()}, duyệt in-order = ${balanced.inorder().join(" ")}`);
console.log(`  chèn đã sắp → chiều cao = ${degenerate.height()}  (suy biến thành danh sách liên kết!)`);
console.log(`  tìm khoá 9: cây cân bằng ${balanced.search(9)} bước vs cây suy biến ${degenerate.search(9)} bước`);
assert.deepEqual(balanced.inorder(), [1, 2, 3, 4, 5, 6, 7, 8, 9]); // in-order luôn ra thứ tự tăng
assert.equal(balanced.height(), 4);
assert.equal(degenerate.height(), 9);

// ─── HÀNG ĐỢI ƯU TIÊN bằng MIN-HEAP (mảng ngầm: con của i ở 2i+1, 2i+2) ───
// Heap order: mỗi nút cha "trội" (nhỏ hơn) các con → gốc luôn là min.
class MinHeap {
  private a: number[] = [];
  size(): number { return this.a.length; }
  toArray(): number[] { return [...this.a]; }

  insert(x: number): void {                     // thêm cuối rồi "nổi lên" (bubble-up)
    this.a.push(x);
    let i = this.a.length - 1;
    while (i > 0) {
      const parent = (i - 1) >> 1;
      if (this.a[parent] <= this.a[i]) break;    // cha đã nhỏ hơn → đúng thứ tự
      [this.a[parent], this.a[i]] = [this.a[i], this.a[parent]];
      i = parent;
    }
  }

  extractMin(): number {                         // lấy gốc, đưa cuối lên rồi "chìm xuống" (sift-down)
    const min = this.a[0];
    const last = this.a.pop() as number;
    if (this.a.length > 0) {
      this.a[0] = last;
      let i = 0;
      const n = this.a.length;
      while (true) {
        const l = 2 * i + 1, r = 2 * i + 2;
        let smallest = i;
        if (l < n && this.a[l] < this.a[smallest]) smallest = l;
        if (r < n && this.a[r] < this.a[smallest]) smallest = r;
        if (smallest === i) break;
        [this.a[i], this.a[smallest]] = [this.a[smallest], this.a[i]];
        i = smallest;
      }
    }
    return min;
  }
}

const heap = new MinHeap();
for (const x of [5, 3, 8, 1, 9, 2, 7]) heap.insert(x);
console.log("\nMIN-HEAP (hàng đợi ưu tiên) — chèn 5 3 8 1 9 2 7:");
console.log(`  mảng ngầm sau khi chèn = [${heap.toArray().join(", ")}]  (gốc a[0]=${heap.toArray()[0]} là min)`);

const extracted: number[] = [];
while (heap.size() > 0) extracted.push(heap.extractMin());
console.log(`  extract-min liên tục    = ${extracted.join(" ")}  ← ra đúng thứ tự tăng = heapsort!`);
assert.deepEqual(extracted, [1, 2, 3, 5, 7, 8, 9]);  // lấy min lặp lại = sắp xếp

console.log("\nBST: tra + cập nhật đều O(log n) NẾU cân bằng (Skiena tr.86). Heap: insert/extract-min");
console.log("O(log n), gốc = min tức thì — nền của heapsort (Bài 5) và Dijkstra (Bài 8).");
```

Kết quả chạy thật *(tất định)*:

```
CÂY TÌM KIẾM NHỊ PHÂN (BST) — 9 khoá:
  chèn khéo   → chiều cao = 4, duyệt in-order = 1 2 3 4 5 6 7 8 9
  chèn đã sắp → chiều cao = 9  (suy biến thành danh sách liên kết!)
  tìm khoá 9: cây cân bằng 3 bước vs cây suy biến 9 bước

MIN-HEAP (hàng đợi ưu tiên) — chèn 5 3 8 1 9 2 7:
  mảng ngầm sau khi chèn = [1, 3, 2, 5, 9, 8, 7]  (gốc a[0]=1 là min)
  extract-min liên tục    = 1 2 3 5 7 8 9  ← ra đúng thứ tự tăng = heapsort!

BST: tra + cập nhật đều O(log n) NẾU cân bằng (Skiena tr.86). Heap: insert/extract-min
O(log n), gốc = min tức thì — nền của heapsort (Bài 5) và Dijkstra (Bài 8).
```

Ba điều đáng thấm. **(1) Chiều cao là tất cả:** cùng 9 khoá, cây khéo cao 4 (tìm 9 chỉ 3 bước) còn cây chèn-đã-sắp cao 9 (tìm 9 mất đủ 9 bước) — một BST không cân bằng *tệ ngang danh sách liên kết*, đúng cảnh báo "chọn sai cấu trúc là thảm hoạ". **(2) In-order = sắp xếp miễn phí:** duyệt trái–nút–phải luôn ra `1 2 … 9`, thao tác thứ tự mà bảng băm (Bài 3) chịu thua. **(3) Heap không cần sắp hết:** mảng ngầm `[1,3,2,5,9,8,7]` *không* phải dãy đã sắp — chỉ cần cha nhỏ hơn con là đủ để gốc luôn là min; vậy mà extract-min liên tục lại nhả ra đúng dãy tăng — đó chính là heapsort.

> [!note] Tự thử
> 1. Thêm `delete(key)` cho BST. Trường hợp khó nhất là xoá nút có *hai con* — xử lý bằng cách thay bằng *successor* (khoá nhỏ nhất của cây con phải). Vì sao chọn successor?
> 2. Đổi `MinHeap` thành `MaxHeap` (gốc là lớn nhất): cần đổi đúng những dấu so sánh nào? extract liên tục giờ ra thứ tự gì?
> 3. BST chèn `[1..9]` cho cây cao 9. Thứ tự chèn nào của chính 9 khoá đó cho cây *thấp nhất*? Chiều cao tối thiểu là bao nhiêu?
> 4. Trong `MinHeap.insert`, vì sao so `a[parent] <= a[i]` thì dừng được ngay (không cần đi tiếp lên gốc)?

## 6. Bản đồ khoá DSA

| # | Bài | Chủ đề | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | Thuật toán & tính đúng | nền: đúng vs hiệu quả | Skiena Ch1 + Grokking |
| 1 | Phân tích Big-O | đo chi phí khi `n` lớn | Skiena Ch2 |
| 2 | CTDL tuyến tính | mảng / list / stack / queue | Skiena Ch3 |
| 3 | Từ điển & bảng băm | tra cứu O(1) trung bình | Skiena Ch3 |
| 4 | **Heap & cây tìm kiếm** ← *đang ở đây* | lấy min/max, tra có thứ tự | Skiena Ch3–4 |
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

Heap quay lại ở [Bài 5](bai_05_sap-xep.md) (heapsort) và [Bài 8](bai_08_do-thi-trong-so.md) (Dijkstra/Prim); BST cân bằng là nền index của [database](../../database/README.md).

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 4.1 — Bất biến của cây tìm kiếm nhị phân (BST) là gì? Nó cho ta làm gì nhanh?
> **Đáp:** mọi khoá cây con **trái** < nút < mọi khoá cây con **phải** (Skiena tr. 81). Cho tìm/chèn/xoá trong O(chiều cao) (trò đoán số), và **duyệt in-order ra thứ tự tăng**.

> [!question] Thẻ 4.2 — Vì sao chiều cao BST quyết định hiệu năng? Khi nào nó tệ nhất?
> **Đáp:** mọi chi phí là O(chiều cao). Chèn khoá **đã sắp sẵn** → cây suy biến thành xâu chuỗi cao `n` → tra O(n), tệ như danh sách liên kết.

> [!question] Thẻ 4.3 — Cây cân bằng (AVL, đỏ-đen) giải quyết gì, và bảo đảm gì?
> **Đáp:** xoay lại cây sau mỗi chèn/xoá để **chiều cao luôn O(log n)** → mọi thao tác từ điển O(log n). Coi như hộp đen cho từ điển có-thứ-tự (Skiena tr. 86).

> [!question] Thẻ 4.4 — Hàng đợi ưu tiên có ba thao tác gì? Heap cài chúng nhanh thế nào?
> **Đáp:** **insert, find-minimum, delete-minimum** (Skiena tr. 88). Heap: cây nhị phân đầy đủ lưu ngầm trong mảng, chỉ cần cha trội con; insert nổi-lên, extract-min chìm-xuống — đều O(log n), find-min O(1) (gốc).

> [!question] Thẻ 4.5 — "Heap order" (trật tự heap) khác "sorted order" (sắp hoàn toàn) ở đâu?
> **Đáp:** heap chỉ đòi **cha trội con** (min-heap: cha nhỏ hơn con), không đòi anh em có thứ tự — trật tự *yếu hơn* nên rẻ duy trì, nhưng đủ để min luôn ở gốc (Skiena tr. 116).

## 8. Câu hỏi tự kiểm tra

1. Vẽ BST khi chèn lần lượt 4, 2, 6, 1, 3, 5, 7. Chiều cao bằng bao nhiêu? In-order ra gì? *(mục 2)*
2. Vì sao chèn dãy đã sắp vào BST lại cho cây tệ nhất? Cây cân bằng cứu bằng cách nào? *(mục 3)*
3. So sánh bảng băm (Bài 3) và BST cân bằng trên: search, và thao tác "liệt kê theo thứ tự". Khi nào chọn cái nào? *(mục 2 & 4)*
4. Giải thích bubble-up (insert) và sift-down (extract-min) của heap. Vì sao mỗi cái O(log n)? *(mục 4)*
5. Chạy demo mục 5. Vì sao mảng heap `[1,3,2,5,9,8,7]` *không* đã sắp mà extract-min vẫn ra dãy tăng? *(mục 4 & 5)*

## Tóm tắt một trang

```
BÀI 4 — HEAP & CÂY TÌM KIẾM
─────────────────────────────────────────────────────────
VẤN ĐỀ  cần tra nhanh VÀ cập nhật linh hoạt VÀ có thứ tự — Bài 2–3 mỗi cái
   chỉ giỏi một nửa (Skiena tr.81).

BST (cây tìm kiếm nhị phân)  bất biến: trái < nút < phải (Skiena tr.81). Tìm/
   chèn/xoá = O(chiều cao) (trò đoán số). In-order → THỨ TỰ TĂNG (băm thua).

CHIỀU CAO LÀ TẤT CẢ  chèn khéo → cao log n; chèn ĐÃ SẮP → suy biến xâu chuỗi
   cao n (= danh sách liên kết). CÂY CÂN BẰNG (AVL, đỏ-đen) xoay giữ cao
   O(log n) → mọi thao tác O(log n) (Skiena tr.86). Chọn sai DS = thảm hoạ.
   → database dùng B+TREE: nút chứa trăm khoá, cây 3-4 tầng cho triệu khoá.

HÀNG ĐỢI ƯU TIÊN  3 thao tác: insert / find-min / delete-min (Skiena tr.88).

HEAP  cây nhị phân ĐẦY ĐỦ lưu NGẦM trong mảng (con của i ở 2i+1,2i+2). Chỉ cần
   CHA TRỘI CON (min-heap: cha nhỏ hơn) — trật tự yếu hơn sắp hẳn (Skiena tr.116).
   insert nổi-lên, extract-min chìm-xuống: O(log n); find-min O(1) (gốc).
   Lấy min liên tục = HEAPSORT (Bài 5).

DEMO  BST 9 khoá: chèn khéo cao 4 (tìm 9 = 3 bước), chèn đã-sắp cao 9 (9 bước).
   heap [1,3,2,5,9,8,7] (ko sắp) → extract-min = 1 2 3 5 7 8 9.
```

## Nguồn

- **Skiena, Steven S. — *The Algorithm Design Manual*, 3rd ed.** (Springer, 2020) — **Ch3 §3.4 Binary Search Trees, §3.5 Priority Queues; Ch4 §4.3 Heapsort**: bất biến BST, chiều cao & cây cân bằng O(log n), ADT hàng đợi ưu tiên (insert/find-min/delete-min), heap (cây nhị phân đầy đủ, mảng ngầm, heap order, bubble-up/sift-down). `tai_lieu/The Algorithm Design Manual 3rd Edition...pdf` (offset **PDF = tr. + 16** ở Ch3–4).
- Liên hệ: [database — B+tree & index](../../database/README.md) (BST cân bằng áp cho đĩa); heap sẽ dùng ở [Bài 5 — Sắp xếp](bai_05_sap-xep.md) (heapsort) và [Bài 8 — Đồ thị trọng số](bai_08_do-thi-trong-so.md) (Dijkstra/Prim).

---

**Bản đồ khoá học:** [Bài 0 — Thuật toán & tính đúng](bai_00_thuat-toan-la-gi.md) · [Bài 1 — Phân tích Big-O](bai_01_big-o.md) · [Bài 2 — CTDL tuyến tính](bai_02_ctdl-tuyen-tinh.md) · [Bài 3 — Từ điển & bảng băm](bai_03_bang-bam.md) · **[Bài 4 — Heap & cây tìm kiếm] ← bạn đang ở đây** · [Bài 5 — Sắp xếp](bai_05_sap-xep.md) · [Bài 6 — Chia để trị & đệ quy](bai_06_chia-de-tri.md) · [Bài 7 — Đồ thị: duyệt](bai_07_do-thi-duyet.md) · [Bài 8 — Đồ thị trọng số](bai_08_do-thi-trong-so.md) · [Bài 9 — Quy hoạch động](bai_09_quy-hoach-dong.md) · [Bài 10 — Backtracking](bai_10_backtracking.md) · [Bài 11 — NP-đầy đủ](bai_11_np-day-du.md) · [Bài 12 — Khớp chuỗi](bai_12_khop-chuoi.md) · [Bài 13 — Luồng mạng](bai_13_luong-mang.md) · [Bài 14 — Thuật toán ngẫu nhiên](bai_14_ngau-nhien.md)

Xem thêm [README khoá học](../README.md).
