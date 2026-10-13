# Bài 2 — Cấu trúc dữ liệu tuyến tính: mảng, danh sách liên kết, stack, queue

> [!info] Về bài này
> Bài 0–1 cho công cụ *đo* (đúng, Big-O). Từ bài này ta xây **kho cấu trúc dữ liệu** — vật liệu để ráp thuật toán. Bắt đầu bằng nhóm *tuyến tính*: dữ liệu xếp thành một dãy. Câu hỏi xuyên suốt: cùng lưu một đống phần tử, vì sao có lúc chọn **mảng**, có lúc chọn **danh sách liên kết**, và khi nào cần **stack**/**queue**? Mỗi lựa chọn là một bộ đánh đổi chi phí thao tác — đổi cấu trúc dữ liệu có thể làm chương trình nhanh gấp bội mà không đổi một dòng logic.
> Nguồn (Luật số 1): **Skiena** *The Algorithm Design Manual 3e* — **Chapter 3: Data Structures** (`tai_lieu/`, trích `> [!quote] Skiena (tr. N)`, **PDF = tr. + 16** ở chương này — xem hộp lưu ý offset).
> **Chạy demo:** `node bai_02.ts` — Node 22+, không cài gói. Code tất định.
> Cần đọc trước: [Bài 1 — Phân tích Big-O](bai_01_big-o.md).

> [!warning] Offset trang Skiena trôi theo chương
> Bài 0–1 dùng **PDF = tr. + 17** (Ch1–2). Sang **Ch3**, offset là **+16** (trang in 69 = PDF 85). Sách có trang phân cách phần không đánh số nên offset *không cố định tuyệt đối* — giống hệt bẫy ở [khoá database](../../database/README.md) (Silberschatz). Mỗi quote trong khoá đều được dò lại đúng trang PDF chứa chữ trước khi ghi; verifier quét cửa sổ ±3 trang để bắt lệch.

## Mục lục

1. [Tình huống: đổi cấu trúc dữ liệu, chương trình nhanh gấp bội](#1-tình-huống-đổi-cấu-trúc-dữ-liệu-chương-trình-nhanh-gấp-bội)
2. [Liền kề hay liên kết: mảng so với danh sách liên kết](#2-liền-kề-hay-liên-kết-mảng-so-với-danh-sách-liên-kết)
3. [Mảng động: vì sao thêm cuối trung bình O(1)](#3-mảng-động-vì-sao-thêm-cuối-trung-bình-o1)
4. [Container: stack (LIFO) và queue (FIFO)](#4-container-stack-lifo-và-queue-fifo)
5. [Demo: mảng động, danh sách liên kết, stack, queue](#5-demo-mảng-động-danh-sách-liên-kết-stack-queue)
6. [Bản đồ khoá DSA](#6-bản-đồ-khoá-dsa)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Tình huống: đổi cấu trúc dữ liệu, chương trình nhanh gấp bội

> [!example] Chương trình chậm, không đổi logic mà vẫn tăng tốc
> Bạn có một chương trình chạy ì ạch. Hồ sơ cho thấy nó dành phần lớn thời gian *tra cứu* trong một danh sách. Bạn không đổi thuật toán, chỉ đổi **cách lưu** danh sách đó — từ mảng chưa sắp thành một cấu trúc tra cứu tốt hơn — và chương trình nhanh lên gấp bội. Vì sao được phép, và vì sao lại hiệu quả đến thế?

Skiena mở chương cấu trúc dữ liệu bằng đúng hình ảnh đó:

> [!quote] Skiena (tr. 68)
> "Putting the right data structure into a slow program can work the same wonders as transplanting fresh parts into a sick patient."
>
> *Đặt đúng cấu trúc dữ liệu vào một chương trình chậm có thể tạo kỳ tích chẳng kém **ghép tạng tươi** vào một bệnh nhân đang ốm.*

Mấu chốt: đổi cấu trúc dữ liệu **không** đụng tới tính đúng (Bài 0) — bạn thay một cài đặt đúng bằng một cài đặt đúng khác. Cái đổi là **chi phí thao tác**:

> [!quote] Skiena (tr. 68)
> "Changing the data structure does not affect the correctness of the program [...] However, the new implementation may realize different trade-offs in the time to execute various operations, so the total performance can improve dramatically."
>
> *Đổi cấu trúc dữ liệu **không ảnh hưởng tính đúng** của chương trình [...] Tuy nhiên, cài đặt mới có thể mang **bộ đánh đổi khác** về thời gian thực thi các thao tác, nên tổng hiệu năng có thể **cải thiện ngoạn mục**.*

Vậy học cấu trúc dữ liệu = học *bảng giá thao tác* của từng loại, để chọn loại rẻ đúng chỗ chương trình hay làm nhất.

## 2. Liền kề hay liên kết: mảng so với danh sách liên kết

Mọi cấu trúc tuyến tính chia làm hai phe theo cách cấp phát bộ nhớ:

> [!quote] Skiena (tr. 69)
> "Data structures can be neatly classified as either contiguous or linked, depending upon whether they are based on arrays or pointers."
>
> *Cấu trúc dữ liệu có thể phân loại gọn thành **liền kề (contiguous)** hay **liên kết (linked)**, tuỳ vào chúng dựa trên **mảng** hay **con trỏ**.*

- **Mảng (contiguous):** các phần tử nằm sát nhau trong một khối bộ nhớ liền mạch. Biết chỉ số `i` là tính ngay địa chỉ `base + i·kích_thước` → **truy cập ngẫu nhiên O(1)**. Nhưng chèn vào giữa phải dịch chuyển phần đuôi.
- **Danh sách liên kết (linked):** mỗi **nút** chứa dữ liệu + **con trỏ** tới nút kế. Các nút rải rác khắp bộ nhớ, nối nhau bằng con trỏ.

```
MẢNG (liền kề):  [ A | B | C | D | E ]     địa chỉ liền nhau → nhảy tới arr[3] tức thì
                   0   1   2   3   4

LIÊN KẾT:   head → [A|•]→[B|•]→[C|•]→[D|•]→[E|⌀]   rải rác, phải đi từng nút tới D
```

Skiena liệt kê **ưu thế từng phe** (tr. 74) — đây là bảng đánh đổi cần thuộc:

| Danh sách liên kết hơn ở | Mảng hơn ở |
| :-- | :-- |
| không tràn tới khi bộ nhớ thật sự đầy | **truy cập ngẫu nhiên** hiệu quả (biết chỉ số là tới ngay) |
| chèn/xoá đơn giản hơn | tiết kiệm bộ nhớ (không tốn ô cho con trỏ) |
| bản ghi lớn: dời con trỏ rẻ hơn dời cả phần tử | **locality** và **cache** tốt hơn nhảy con trỏ lung tung |

> [!quote] Skiena (tr. 74)
> "Better memory locality and cache performance than random pointer jumping."
>
> *Tính **cục bộ bộ nhớ (locality)** và hiệu năng **cache** tốt hơn so với việc nhảy con trỏ ngẫu nhiên.*

> [!note] Vì sao thực tế mảng thường thắng dù lý thuyết hoà
> Dòng cuối bảng là thủ phạm hay bị quên. Mô hình RAM (Bài 1) coi mọi truy cập bộ nhớ như nhau, nhưng CPU thật đọc theo **dòng cache**: phần tử mảng cạnh nhau được nạp cùng lúc, còn nút liên kết nằm rải rác mỗi lần truy cập là một lần "cache miss" đắt đỏ. Vì vậy với dữ liệu nhỏ–vừa, duyệt một mảng thường nhanh hơn duyệt danh sách liên kết *cùng độ phức tạp O(n)*. Đây đúng chỗ mô hình RAM "nói dối" đã cảnh báo ở Bài 1, và là lý do [cloud-base](../../cloud-base/README.md) nhấn mạnh locality.

## 3. Mảng động: vì sao thêm cuối trung bình O(1)

Mảng cố định có một tật: phải biết kích thước trước. **Mảng động** *(dynamic array — `Array` của JS, `vector` C++, `ArrayList` Java)* gỡ tật đó: khi đầy thì **cấp mảng mới gấp đôi**, chép toàn bộ sang, rồi tiếp tục. Nghe có vẻ đắt — mỗi lần đầy phải chép tất cả — nhưng tính gộp lại thì rẻ bất ngờ.

Vì sao? Việc gấp đôi càng lúc càng thưa: chép sau phần tử thứ 1, 2, 4, 8, ..., `n`. Tổng số lần chép là `1 + 2 + 4 + ... + n < 2n`. Chia cho `n` phần tử → trung bình **mỗi phần tử chỉ bị chép ~2 lần**.

> [!quote] Skiena (tr. 71)
> "each of the n elements move only two times on average, and the total work of managing the dynamic array is the same O(n) as it would have been if a single array of sufficient size had been allocated in advance!"
>
> *mỗi trong số `n` phần tử chỉ bị dời **trung bình hai lần**, và tổng công quản lý mảng động vẫn là **O(n)** y như khi ta cấp sẵn một mảng đủ lớn ngay từ đầu!*

Đây là **phân tích khấu hao** *(amortized analysis)*: một thao tác `push` lẻ *có thể* tốn O(n) (đúng lúc phải gấp đôi), nhưng **trung bình trên cả dãy** thì O(1). Cái mất là *lời hứa worst-case từng thao tác* — thỉnh thoảng có một nhịp khựng. Demo mục 5 đếm tận tay: thêm 1000 phần tử tốn tổng cộng bao nhiêu lần chép.

## 4. Container: stack (LIFO) và queue (FIFO)

Khi chỉ cần *cất vào — lấy ra* mà không quan tâm nội dung, Skiena gọi đó là **container** (khác *dictionary* tra theo khoá — Bài 3). Container phân biệt nhau ở **thứ tự lấy ra**:

> [!quote] Skiena (tr. 75)
> "Stacks support retrieval by last-in, first-out (LIFO) order. [...] Queues support retrieval in first-in, first-out (FIFO) order. This is surely the fairest way to control waiting times for services."
>
> *Stack hỗ trợ lấy ra theo thứ tự **vào-sau-ra-trước (LIFO)**. [...] Queue hỗ trợ lấy ra theo thứ tự **vào-trước-ra-trước (FIFO)**. Đây chắc chắn là cách **công bằng nhất** để điều phối thời gian chờ dịch vụ.*

- **Stack (ngăn xếp, LIFO):** `push` thêm lên đỉnh, `pop` lấy từ đỉnh. Như chồng đĩa: cái đặt cuối lấy ra đầu. Thuật toán **đệ quy** chạy trên stack (call stack); duyệt DFS (Bài 7) dùng stack.
- **Queue (hàng đợi, FIFO):** `enqueue` thêm vào cuối, `dequeue` lấy từ đầu. Như xếp hàng mua vé: ai tới trước phục vụ trước. Duyệt BFS (Bài 7), lập lịch công việc dùng queue.

```
STACK (LIFO)                      QUEUE (FIFO)
  push 1,2,3                        enqueue 1,2,3
      ┌───┐ ← đỉnh (pop ra trước)   đầu → ┌───┬───┬───┐ ← cuối
      │ 3 │                               │ 1 │ 2 │ 3 │
      │ 2 │                               └───┴───┴───┘
      │ 1 │                          dequeue → 1, 2, 3
      └───┘                          (đúng thứ tự vào)
  pop → 3, 2, 1
  (ngược thứ tự vào)
```

## 5. Demo: mảng động, danh sách liên kết, stack, queue

Demo bốn phần: **(1)** mảng động đếm tổng số lần chép khi thêm 1000 phần tử — kiểm `< 2n` (khấu hao O(1)); **(2)** danh sách liên kết thêm-đầu O(1) nhưng tra cứu O(n); **(3)** stack vs queue cho thấy LIFO/FIFO khác nhau ở thứ tự ra; **(4)** bảng chi phí worst-case tổng kết.

```typescript
import { strict as assert } from "node:assert";

// ─── MẢNG ĐỘNG: vì sao thêm cuối trung bình O(1) dù thỉnh thoảng phải sao chép ───
// Mỗi lần đầy thì GẤP ĐÔI sức chứa và sao chép toàn bộ. Đếm tổng số lần sao chép.
class DynamicArray {
  private data: number[];
  private size: number;
  private capacity: number;
  public copies: number;   // tổng phần tử đã phải chép khi mở rộng
  public resizes: number;  // số lần gấp đôi

  constructor() {
    this.capacity = 1;
    this.data = new Array(this.capacity);
    this.size = 0;
    this.copies = 0;
    this.resizes = 0;
  }

  push(x: number): void {
    if (this.size === this.capacity) {       // đầy → gấp đôi
      this.capacity *= 2;
      const bigger = new Array(this.capacity);
      for (let i = 0; i < this.size; i++) {  // chép từng phần tử sang mảng mới
        bigger[i] = this.data[i];
        this.copies++;
      }
      this.data = bigger;
      this.resizes++;
    }
    this.data[this.size++] = x;              // ghi O(1)
  }

  get length(): number { return this.size; }
}

const n = 1000;
const arr = new DynamicArray();
for (let i = 0; i < n; i++) arr.push(i);
console.log("MẢNG ĐỘNG — thêm 1000 phần tử (sức chứa khởi đầu 1, gấp đôi khi đầy):");
console.log(`  số lần gấp đôi      = ${arr.resizes}`);
console.log(`  tổng phần tử đã chép = ${arr.copies}  (cận trên lý thuyết 2n = ${2 * n})`);
console.log(`  trung bình mỗi push  = ${(arr.copies / n).toFixed(2)} lần chép  → thêm cuối ~O(1) khấu hao`);
assert.ok(arr.copies < 2 * n);               // tổng công sao chép vẫn O(n)
assert.equal(arr.resizes, 10);               // 2^10 = 1024 >= 1000

// ─── DANH SÁCH LIÊN KẾT: thêm đầu O(1), nhưng tra cứu phải đi từng nút O(n) ───
type Node = { item: number; next: Node | null };
class LinkedList {
  private head: Node | null = null;
  insertFront(x: number): void {             // O(1): không cần duyệt
    this.head = { item: x, next: this.head };
  }
  search(x: number): number {                // O(n): đi từng nút, trả số bước
    let steps = 0, cur = this.head;
    while (cur !== null) { steps++; if (cur.item === x) return steps; cur = cur.next; }
    return steps;
  }
}
const list = new LinkedList();
for (let i = 0; i < n; i++) list.insertFront(i);   // 0..999, đầu danh sách là 999
console.log("\nDANH SÁCH LIÊN KẾT — thêm đầu 1000 phần tử:");
console.log(`  tìm 999 (ở đầu)  = ${list.search(999)} bước`);
console.log(`  tìm 0   (ở cuối) = ${list.search(0)} bước  ← không random access, phải đi hết`);
assert.equal(list.search(999), 1);
assert.equal(list.search(0), 1000);

// ─── CONTAINER: STACK (LIFO) vs QUEUE (FIFO) — khác nhau ở THỨ TỰ LẤY RA ───
class Stack { private s: number[] = [];
  push(x: number) { this.s.push(x); }
  pop(): number | undefined { return this.s.pop(); } }      // lấy từ CUỐI
class Queue { private q: number[] = []; private head = 0;
  enqueue(x: number) { this.q.push(x); }
  dequeue(): number | undefined { return this.q[this.head++]; } }  // lấy từ ĐẦU

const st = new Stack(), qu = new Queue();
for (const x of [1, 2, 3]) { st.push(x); qu.enqueue(x); }
const stackOut = [st.pop(), st.pop(), st.pop()];
const queueOut = [qu.dequeue(), qu.dequeue(), qu.dequeue()];
console.log("\nCONTAINER — nạp vào 1, 2, 3 rồi lấy hết ra:");
console.log(`  Stack (LIFO, last-in first-out):  ${stackOut.join(", ")}`);
console.log(`  Queue (FIFO, first-in first-out): ${queueOut.join(", ")}`);
assert.deepEqual(stackOut, [3, 2, 1]);
assert.deepEqual(queueOut, [1, 2, 3]);

// ─── BẢNG CHI PHÍ worst-case: mỗi cấu trúc mạnh/yếu ở chỗ khác nhau ───
console.log("\nCHI PHÍ worst-case (chọn cấu trúc = chọn thao tác nào cần nhanh):");
console.log("  thao tác              mảng động    danh sách liên kết");
console.log("  truy cập theo chỉ số   O(1)         O(n)");
console.log("  thêm vào đầu           O(n)         O(1)");
console.log("  thêm vào cuối          O(1)*        O(1) nếu giữ đuôi");
console.log("  tìm (chưa sắp)         O(n)         O(n)");
console.log("  * khấu hao: thỉnh thoảng O(n) khi gấp đôi, trung bình O(1).");
```

Kết quả chạy thật *(tất định)*:

```
MẢNG ĐỘNG — thêm 1000 phần tử (sức chứa khởi đầu 1, gấp đôi khi đầy):
  số lần gấp đôi      = 10
  tổng phần tử đã chép = 1023  (cận trên lý thuyết 2n = 2000)
  trung bình mỗi push  = 1.02 lần chép  → thêm cuối ~O(1) khấu hao

DANH SÁCH LIÊN KẾT — thêm đầu 1000 phần tử:
  tìm 999 (ở đầu)  = 1 bước
  tìm 0   (ở cuối) = 1000 bước  ← không random access, phải đi hết

CONTAINER — nạp vào 1, 2, 3 rồi lấy hết ra:
  Stack (LIFO, last-in first-out):  3, 2, 1
  Queue (FIFO, first-in first-out): 1, 2, 3

CHI PHÍ worst-case (chọn cấu trúc = chọn thao tác nào cần nhanh):
  thao tác              mảng động    danh sách liên kết
  truy cập theo chỉ số   O(1)         O(n)
  thêm vào đầu           O(n)         O(1)
  thêm vào cuối          O(1)*        O(1) nếu giữ đuôi
  tìm (chưa sắp)         O(n)         O(n)
  * khấu hao: thỉnh thoảng O(n) khi gấp đôi, trung bình O(1).
```

Bốn điều đáng thấm. **(1) Khấu hao là thật:** thêm 1000 phần tử chỉ tốn 1023 lần chép — trung bình 1,02 lần mỗi phần tử, đúng "move only two times on average" của Skiena; `push` *trung bình* O(1) dù có 10 nhịp gấp đôi. **(2) Không có cấu trúc "tốt nhất":** danh sách liên kết tra phần tử đầu 1 bước nhưng phần tử cuối 1000 bước — nó *không có truy cập ngẫu nhiên*, bù lại thêm-đầu luôn O(1). **(3) Stack vs queue chỉ khác một chỗ:** cùng nạp 1,2,3 mà stack nhả `3,2,1` còn queue nhả `1,2,3` — khác nhau *lấy từ đầu hay cuối*, thế là đủ sinh ra hai công cụ cho hai loại bài toán. **(4) Bảng chi phí là la bàn chọn cấu trúc:** nhìn chương trình hay làm thao tác nào nhất rồi chọn cấu trúc rẻ ở đúng ô đó.

> [!note] Tự thử
> 1. Đổi hệ số mở rộng từ gấp đôi (`*= 2`) sang `+= 1` (mỗi lần chỉ nới thêm 1 ô). Tổng số lần chép khi thêm 1000 phần tử giờ là bao nhiêu? Vì sao thành O(n²)?
> 2. Thêm con trỏ `tail` vào `LinkedList` để `insertEnd` thành O(1). Nếu muốn `deleteEnd` cũng O(1) thì cần gì? (Gợi ý: danh sách liên kết đôi.)
> 3. Cài một queue *chỉ* bằng hai stack. `enqueue`/`dequeue` khi đó tốn bao nhiêu (khấu hao)? (Kinh điển phỏng vấn.)
> 4. Trong demo stack, `this.s.pop()` của JS `Array` chạy bao lâu? Vì sao `pop` cuối mảng là O(1) còn `shift` đầu mảng là O(n)?

## 6. Bản đồ khoá DSA

| # | Bài | Chủ đề | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | Thuật toán & tính đúng | nền: đúng vs hiệu quả | Skiena Ch1 + Grokking |
| 1 | Phân tích Big-O | đo chi phí khi `n` lớn | Skiena Ch2 |
| 2 | **CTDL tuyến tính** ← *đang ở đây* | mảng / list / stack / queue | Skiena Ch3 |
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

> [!question] Thẻ 2.1 — Đổi cấu trúc dữ liệu có làm chương trình sai không? Nó đổi cái gì?
> **Đáp:** **không** đổi tính đúng (thay một cài đặt đúng bằng cài đặt đúng khác); nó đổi **bộ đánh đổi chi phí thao tác**, nên tổng hiệu năng có thể cải thiện ngoạn mục (Skiena tr. 68).

> [!question] Thẻ 2.2 — Liền kề (contiguous) khác liên kết (linked) ở đâu? Mỗi loại mạnh ở gì?
> **Đáp:** liền kề = mảng (phần tử sát nhau) → **truy cập ngẫu nhiên O(1)**, locality/cache tốt. Liên kết = con trỏ (nút rải rác) → chèn/xoá đơn giản, không tràn tới khi hết bộ nhớ, dời bản ghi lớn rẻ (Skiena tr. 74).

> [!question] Thẻ 2.3 — Vì sao thêm cuối vào mảng động trung bình O(1) dù có lúc phải chép cả mảng?
> **Đáp:** gấp đôi khi đầy → tổng số lần chép `1+2+4+...+n < 2n`, mỗi phần tử bị dời trung bình 2 lần → tổng công O(n), trung bình O(1) mỗi `push` (**khấu hao**). Mất: lời hứa worst-case từng thao tác (Skiena tr. 71).

> [!question] Thẻ 2.4 — Stack và queue khác nhau ở đâu? Cho một ứng dụng mỗi loại.
> **Đáp:** **stack** = LIFO (vào sau ra trước) — call stack, DFS. **queue** = FIFO (vào trước ra trước) — xếp hàng, BFS, lập lịch (Skiena tr. 75).

> [!question] Thẻ 2.5 — Danh sách liên kết tra cứu phần tử ở cuối tốn bao nhiêu? Vì sao?
> **Đáp:** **O(n)** — không có truy cập ngẫu nhiên, phải đi theo con trỏ từng nút từ đầu tới cuối. (Mảng thì O(1) vì tính địa chỉ trực tiếp từ chỉ số.)

## 8. Câu hỏi tự kiểm tra

1. Chương trình chậm vì tra cứu nhiều. Giải thích vì sao đổi cấu trúc dữ liệu tăng tốc được mà không phá tính đúng. *(mục 1)*
2. Khi nào bạn chọn mảng thay vì danh sách liên kết, và ngược lại? Nêu hai lý do mỗi chiều. *(mục 2)*
3. Giải thích "khấu hao O(1)" của `push` mảng động. Cái gì bị đánh đổi so với mảng cấp sẵn đủ lớn? *(mục 3)*
4. Nạp A, B, C, D vào một stack và một queue rồi lấy hết ra — viết thứ tự ra của mỗi loại. *(mục 4)*
5. Chạy demo mục 5. Vì sao tìm `0` trong danh sách tốn 1000 bước còn tìm `999` chỉ 1 bước? *(mục 5)*

## Tóm tắt một trang

```
BÀI 2 — CẤU TRÚC DỮ LIỆU TUYẾN TÍNH
─────────────────────────────────────────────────────────
Ý LỚN  đổi cấu trúc dữ liệu = đổi BẢNG GIÁ thao tác, KHÔNG đổi tính đúng; có
   thể nhanh gấp bội như "ghép tạng" (Skiena tr.68). Học DS = học bảng giá đó.

LIỀN KỀ vs LIÊN KẾT (Skiena tr.69,74)
   MẢNG (contiguous): phần tử sát nhau → truy cập chỉ số O(1), locality/cache
      tốt; nhưng chèn giữa phải dịch đuôi.
   LIÊN KẾT (linked): nút + con trỏ, rải rác → chèn/xoá dễ, không tràn tới khi
      hết RAM; nhưng KHÔNG random access (tra = O(n)), tốn ô con trỏ.

MẢNG ĐỘNG  đầy thì GẤP ĐÔI + chép. Tổng chép 1+2+...+n < 2n → mỗi phần tử dời
   ~2 lần → push KHẤU HAO O(1) (Skiena tr.71). Mất: worst-case từng thao tác.

CONTAINER (Skiena tr.75)  STACK = LIFO (push/pop đỉnh) — call stack, DFS.
   QUEUE = FIFO (enqueue cuối/dequeue đầu) — xếp hàng, BFS. Khác nhau MỖI
   chỗ lấy đầu hay cuối.

DEMO  mảng động 1000 phần tử = 1023 lần chép (1,02/phần tử). Liên kết: tìm
   đầu 1 bước, cuối 1000. Stack nhả 3,2,1; queue nhả 1,2,3.
```

## Nguồn

- **Skiena, Steven S. — *The Algorithm Design Manual*, 3rd ed.** (Springer, 2020) — **Chapter 3: Data Structures** (§3.1 Contiguous vs. Linked, §3.2 Containers: Stacks and Queues): phân loại liền kề/liên kết, ưu thế từng loại, mảng động & phân tích khấu hao, stack LIFO / queue FIFO. `tai_lieu/The Algorithm Design Manual 3rd Edition...pdf` (offset **PDF = tr. + 16** ở Ch3).
- Liên hệ: [cloud-base](../../cloud-base/README.md) về locality/cache; [database — buffer & slotted page](../../database/README.md) dùng chính mảng/con trỏ ở tầng lưu trữ; stack/queue sẽ quay lại ở [Bài 7 — duyệt đồ thị](bai_07_do-thi-duyet.md) (DFS dùng stack, BFS dùng queue).

---

**Bản đồ khoá học:** [Bài 0 — Thuật toán & tính đúng](bai_00_thuat-toan-la-gi.md) · [Bài 1 — Phân tích Big-O](bai_01_big-o.md) · **[Bài 2 — CTDL tuyến tính] ← bạn đang ở đây** · [Bài 3 — Từ điển & bảng băm](bai_03_bang-bam.md) · [Bài 4 — Heap & cây tìm kiếm](bai_04_heap-cay-tim-kiem.md) · [Bài 5 — Sắp xếp](bai_05_sap-xep.md) · [Bài 6 — Chia để trị & đệ quy](bai_06_chia-de-tri.md) · [Bài 7 — Đồ thị: duyệt](bai_07_do-thi-duyet.md) · [Bài 8 — Đồ thị trọng số](bai_08_do-thi-trong-so.md) · [Bài 9 — Quy hoạch động](bai_09_quy-hoach-dong.md) · [Bài 10 — Backtracking](bai_10_backtracking.md) · [Bài 11 — NP-đầy đủ](bai_11_np-day-du.md) · [Bài 12 — Khớp chuỗi](bai_12_khop-chuoi.md) · [Bài 13 — Luồng mạng](bai_13_luong-mang.md) · [Bài 14 — Thuật toán ngẫu nhiên](bai_14_ngau-nhien.md)

Xem thêm [README khoá học](../README.md).
