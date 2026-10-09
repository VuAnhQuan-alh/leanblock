# Bài 4 — Lưu trữ vật lý và buffer manager

> [!info] Về bài này
> Hết tầng nền (Bài 0–3). Giờ **mở nắp ca-pô**: dữ liệu *thực sự* nằm ở đâu, và vì sao mỗi truy vấn lại tốn thời gian như nó tốn. Bài này đi từ **phân cấp lưu trữ** (đĩa chậm, RAM nhanh, RAM nhỏ), tới **block** (đơn vị truyền dữ liệu), tới **buffer manager** — lớp giữ bản sao block nóng trong RAM, tim đập của mọi database engine.
> Nguồn (Luật số 1): **Silberschatz** *Database System Concepts 7e* — **Ch12 (Physical Storage Systems)**, **Ch13 (Data Storage Structures)** (offset PDF = tr. + 29).
> **Chạy demo:** **Node 22+**, `node <tên>.ts` — không cài gói.
> Nên đọc trước: [Bài 0 — DBMS là gì](bai_00_dbms-la-gi.md). Liên hệ: [cloud-base Bài 10 — storage engine](../../cloud-base/bai_hoc/bai_10_du-lieu-storage.md).

## Mục lục

1. [Dữ liệu sống trên đĩa, chạy trên RAM](#1-dữ-liệu-sống-trên-đĩa-chạy-trên-ram)
2. [Phân cấp lưu trữ và đơn vị block](#2-phân-cấp-lưu-trữ-và-đơn-vị-block)
3. [Tổ chức bản ghi trong block (slotted page)](#3-tổ-chức-bản-ghi-trong-block-slotted-page)
4. [Buffer manager: RAM nhỏ hơn cơ sở dữ liệu](#4-buffer-manager-ram-nhỏ-hơn-cơ-sở-dữ-liệu)
5. [Demo: LRU buffer pool, dirty page, pin](#5-demo-lru-buffer-pool-dirty-page-pin)
6. [Bản đồ khoá database](#6-bản-đồ-khoá-database)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Dữ liệu sống trên đĩa, chạy trên RAM

Ở Bài 0–3, "bảng" là một khái niệm *logic*. Nhưng CPU không tính được trên đĩa — nó chỉ tính trên **RAM**. Còn RAM thì **bay hơi** (mất khi cúp điện) nên dữ liệu *thật* phải nằm trên **bộ nhớ không bay hơi** (SSD/đĩa từ). Mọi database engine vì thế sống trong một nghịch lý:

- Dữ liệu **bền** nằm trên đĩa — nhưng đĩa **chậm** (cả nghìn lần so với RAM).
- Tính toán xảy ra trên RAM — nhưng RAM **bay hơi** và **nhỏ hơn** cơ sở dữ liệu.

Toàn bộ Bài 4 là câu trả lời cho câu hỏi: *làm sao chạy nhanh trên RAM mà vẫn bền trên đĩa, khi RAM không chứa nổi cả CSDL (cơ sở dữ liệu)?* Câu trả lời có tên: **buffer manager** (mục 4). Trước hết phải hiểu hai bên của khe nứt: phân cấp lưu trữ và block.

## 2. Phân cấp lưu trữ và đơn vị block

Bộ nhớ xếp thành **tháp**: càng lên cao càng nhanh, càng đắt, càng nhỏ — và ranh giới *bay hơi* nằm giữa tháp:

```
   NHANH, đắt, nhỏ                              BAY HƠI (mất khi cúp điện)
   ┌─ cache        (CPU quản, ~ns)                    ↑
   ├─ main memory  (RAM — CPU tính ở đây, ~100ns)     │ volatile
   ├───────────────────────────────────────────────  ┼ ───────────────
   ├─ flash / SSD  (~10–100µs)                        │ non-volatile
   └─ magnetic disk (HDD, ~ms — chậm nhất)            ↓  (dữ liệu THẬT ở đây)
   CHẬM, rẻ, lớn
```

> [!quote] Silberschatz (tr. 562)
> "[storage systems] from main memory up are volatile, whereas the storage systems from flash memory down are non-volatile. Data must be written to non-volatile storage for safekeeping."
>
> *[các hệ lưu trữ] **từ main memory trở lên là bay hơi**, còn **từ flash trở xuống là không bay hơi**. Dữ liệu phải được ghi xuống bộ nhớ không bay hơi để **an toàn**.*

Vì đĩa chậm, engine **không** đọc/ghi từng byte hay từng bản ghi — nó đọc/ghi theo **khối (block)**, đơn vị cố định (thường 4–16 KB):

> [!quote] Silberschatz (tr. 578)
> "Data are transferred between disk and main memory in units of blocks."
>
> *Dữ liệu được truyền giữa đĩa và RAM theo **đơn vị block**.*

Đây là hằng số nền của mọi thứ phía sau: một bản ghi 200 byte vẫn tốn *nguyên một lần đọc block*. Nên đo chi phí truy vấn, ta đếm **số block I/O**, không đếm số byte. Và nó định hình cả cách tổ chức dữ liệu (mục 3) lẫn index (Bài 5 — B+tree có nút *vừa đúng một block*).

## 3. Tổ chức bản ghi trong block (slotted page)

Một block chứa nhiều bản ghi. Với bản ghi **dài cố định** thì dễ (xếp liền nhau). Khó là bản ghi **dài thay đổi** (có cột `VARCHAR`): chèn/xoá làm dịch chuyển lung tung. Giải pháp kinh điển:

> [!quote] Silberschatz (tr. 593)
> "The slotted-page structure is commonly used for organizing records within a block"
>
> *Cấu trúc **slotted-page** thường được dùng để tổ chức các bản ghi trong một block.*

```
   ┌───────────────────────────────────────────────────┐  slotted page
   │ header: [#entries][free-end]→ [slot0][slot1]...   │  slot = (offset, length)
   │ ░░░░░░░ free space ░░░░░░░                        │
   │ ... [ rec2 ][ rec1 ][ rec0 ]                      │ bản ghi mọc từ CUỐI
   └───────────────────────────────────────────────────┘
```

Ý tưởng: **header** đầu block chứa mảng *slot* trỏ tới từng bản ghi (offset + độ dài); bản ghi mọc từ *cuối* block vào. Nhờ đó:
- Con trỏ ngoài chỉ cần tham chiếu `(block, số-slot)` — di dời bản ghi *trong* block chỉ cần sửa slot, **không** đổi con trỏ ngoài.
- Xoá = đánh dấu slot rỗng; chèn = tìm chỗ trống. Nén lại được khi cần.

Chi tiết không quan trọng bằng *nguyên tắc*: block là một **vùng tự quản** có header mô tả nội dung — ta sẽ gặp lại y hệt tư tưởng này ở nút B+tree (Bài 5) và ở log (Bài 11).

## 4. Buffer manager: RAM nhỏ hơn cơ sở dữ liệu

Đây là trái tim bài học. Vì RAM không chứa nổi cả CSDL, engine giữ một **vùng đệm (buffer)** chứa *bản sao* của một số block nóng:

> [!quote] Silberschatz (tr. 604)
> "The buffer is that part of main memory available for storage of copies of disk blocks. [...] The subsystem responsible for the allocation of buffer space is called the buffer manager."
>
> ***Buffer** là phần RAM dành để chứa **bản sao của các block đĩa**. [...] Bộ phận phụ trách cấp phát vùng buffer gọi là **buffer manager**.*

Mọi phần khác của engine *không đụng đĩa trực tiếp* — chúng **xin block từ buffer manager**. Quy trình:

> [!quote] Silberschatz (tr. 604)
> "If the block is not in the buffer, the buffer manager first allocates space in the buffer for the block, throwing out some other block, if necessary, to make space for the new block. The thrown-out block is written back to disk only if it has been modified since the most recent time that it was written to the disk."
>
> *Nếu block **chưa** trong buffer, buffer manager cấp chỗ, **đá một block khác ra** nếu cần. Block bị đá chỉ **được ghi lại đĩa nếu đã bị sửa** kể từ lần ghi gần nhất.*

Ba cơ chế cốt lõi:

1. **HIT / MISS.** Block đã trong buffer → **hit** (nhanh, khỏi đụng đĩa). Chưa có → **miss** (phải đọc đĩa). Tỉ lệ hit cao = engine nhanh. Đây chính là *locality* (tính cục bộ — dữ liệu vừa dùng dễ được dùng lại) — nền của hiệu năng CSDL.
2. **Thay thế LRU.** Hết chỗ thì đá block nào?

   > [!quote] Silberschatz (tr. 605)
   > "Most operating systems use a least recently used (LRU) scheme, in which the block that was referenced least recently is written back to disk and is removed from the buffer."
   >
   > *Hầu hết dùng cơ chế **LRU** (least recently used): block **lâu không được dùng nhất** bị ghi lại đĩa và loại khỏi buffer.*

   Và **dirty page**: chỉ block *đã sửa* (bẩn) mới phải ghi lại đĩa khi bị đá; block *sạch* (chưa sửa) chỉ việc bỏ — vì bản trên đĩa vẫn đúng.
3. **Pin.** Đang đọc dở một block mà nó bị đá ra thì đọc nhầm dữ liệu rác. Nên:

   > [!quote] Silberschatz (tr. 605)
   > "the process executes a pin operation on the block; the buffer manager never evicts a pinned block."
   >
   > *tiến trình thực hiện thao tác **pin** lên block; buffer manager **không bao giờ đá một block đang bị pin**.*

Demo mục 5 cài cả ba: đếm hit/miss, đá LRU (ghi lại đĩa chỉ khi bẩn), và pin chặn eviction.

## 5. Demo: LRU buffer pool, dirty page, pin

Một buffer pool thật thu nhỏ: "đĩa" 6 page, RAM chứa 3. Quan sát thứ tự LRU đổi sau mỗi lần dùng, page bẩn phải ghi-lại-đĩa khi bị đá, và page bị pin thì bất khả xâm phạm:

```typescript
import { strict as assert } from "node:assert";

// Buffer pool: giữ BẢN SAO một số block của "đĩa" trong RAM. RAM < CSDL nên
// phải thay thế block cũ khi hết chỗ — chiến lược LRU (least recently used).
type Frame = { dirty: boolean; pinned: boolean };

class BufferPool {
  capacity: number;
  disk: Map<string, number>;        // "đĩa": pageId → giá trị (luôn bền)
  frames: Map<string, Frame>;       // các page đang nằm trong RAM
  order: string[];                  // thứ tự dùng: đầu = cũ nhất (LRU), cuối = mới nhất
  hits: number; misses: number; evictions: number; writebacks: number;

  constructor(capacity: number, disk: Map<string, number>) {
    this.capacity = capacity; this.disk = disk;
    this.frames = new Map(); this.order = [];
    this.hits = 0; this.misses = 0; this.evictions = 0; this.writebacks = 0;
  }

  private touch(id: string) {                 // đánh dấu vừa dùng → đẩy xuống cuối
    this.order = this.order.filter(x => x !== id);
    this.order.push(id);
  }

  private evict() {                           // bỏ page LRU (bỏ qua page đang pin)
    const victimIdx = this.order.findIndex(id => !this.frames.get(id)!.pinned);
    if (victimIdx < 0) throw new Error("mọi page đều bị pin — không evict được!");
    const victim = this.order[victimIdx];
    const f = this.frames.get(victim)!;
    if (f.dirty) { this.writebacks++; }        // CHỈ ghi lại đĩa nếu đã sửa (bẩn)
    this.order.splice(victimIdx, 1);
    this.frames.delete(victim);
    this.evictions++;
    return `evict ${victim}${f.dirty ? " (bẩn→ghi lại đĩa)" : " (sạch→bỏ)"}`;
  }

  access(id: string, write = false): string {
    let note = "";
    if (this.frames.has(id)) {                 // HIT: đã trong RAM
      this.hits++; note = "HIT ";
    } else {                                    // MISS: đọc từ đĩa
      this.misses++; note = "MISS";
      if (this.frames.size >= this.capacity) note += " [" + this.evict() + "]";
      this.frames.set(id, { dirty: false, pinned: false });
    }
    if (write) this.frames.get(id)!.dirty = true;
    this.touch(id);
    return `${write ? "write" : "read "} ${id}: ${note}  RAM=[${this.order.join(",")}]`;
  }

  pin(id: string)   { this.frames.get(id)!.pinned = true; }
  unpin(id: string) { this.frames.get(id)!.pinned = false; }
}

// Đĩa có 6 page; RAM chỉ chứa 3 → buộc phải thay thế.
const disk = new Map([["P1",10],["P2",20],["P3",30],["P4",40],["P5",50],["P6",60]]);
const bp = new BufferPool(3, disk);

console.log("RAM chứa 3 page / đĩa 6 page. Dãy truy cập:");
for (const [id, w] of [["P1",0],["P2",0],["P3",0],["P1",0],["P4",1],["P2",0],["P4",0],["P5",0],["P6",0],["P2",0]] as [string,number][])
  console.log("  " + bp.access(id, w === 1));

console.log(`\nTổng: ${bp.hits} hit, ${bp.misses} miss, ${bp.evictions} evict, ${bp.writebacks} ghi-lại-đĩa`);
console.log("→ P4 (đã write→bẩn) khi bị evict phải GHI LẠI đĩa; các page sạch chỉ việc bỏ.");

// Pin: page đang xử lý KHÔNG được evict dù là LRU.
console.log("\nDemo pin — P2 bị pin thì không bao giờ bị đá ra:");
const bp2 = new BufferPool(2, disk);
bp2.access("P2"); bp2.pin("P2");          // P2 vào RAM rồi pin
bp2.access("P3");                          // RAM đầy: [P2(pin), P3]
console.log("  " + bp2.access("P4"));      // cần chỗ: LRU là P2 nhưng bị pin → phải đá P3
assert.ok(bp2.frames.has("P2"), "P2 bị pin phải còn trong RAM");
console.log("  P2 (pinned) còn trong RAM?", bp2.frames.has("P2"), "— đúng, pin chặn evict.");
```

Kết quả chạy thật *(tất định)*:

```
RAM chứa 3 page / đĩa 6 page. Dãy truy cập:
  read  P1: MISS  RAM=[P1]
  read  P2: MISS  RAM=[P1,P2]
  read  P3: MISS  RAM=[P1,P2,P3]
  read  P1: HIT   RAM=[P2,P3,P1]
  write P4: MISS [evict P2 (sạch→bỏ)]  RAM=[P3,P1,P4]
  read  P2: MISS [evict P3 (sạch→bỏ)]  RAM=[P1,P4,P2]
  read  P4: HIT   RAM=[P1,P2,P4]
  read  P5: MISS [evict P1 (sạch→bỏ)]  RAM=[P2,P4,P5]
  read  P6: MISS [evict P2 (sạch→bỏ)]  RAM=[P4,P5,P6]
  read  P2: MISS [evict P4 (bẩn→ghi lại đĩa)]  RAM=[P5,P6,P2]

Tổng: 2 hit, 8 miss, 5 evict, 1 ghi-lại-đĩa
→ P4 (đã write→bẩn) khi bị evict phải GHI LẠI đĩa; các page sạch chỉ việc bỏ.

Demo pin — P2 bị pin thì không bao giờ bị đá ra:
  read  P4: MISS [evict P3 (sạch→bỏ)]  RAM=[P2,P4]
  P2 (pinned) còn trong RAM? true — đúng, pin chặn evict.
```

Bốn điều đáng thấm. **(1)** Mỗi lần dùng, page nhảy xuống *cuối* hàng LRU (`read P1` khi P1 đang trong RAM đẩy nó thành mới nhất) — đó là cách LRU "nhớ" cái gì nóng. **(2)** `hit` khỏi đụng đĩa, `miss` phải đọc đĩa: 2 hit / 8 miss ở đây vì buffer nhỏ so với working set (tập trang đang dùng tích cực) — tăng `capacity` thì hit tăng (Tự thử 1). **(3)** Chỉ **P4** (đã `write` → bẩn) mới tốn *ghi lại đĩa* khi bị đá; năm page sạch kia chỉ việc bỏ vì bản trên đĩa vẫn đúng — đây là lý do engine phân biệt dirty/clean. **(4)** Ở demo pin, LRU đáng lẽ đá `P2` nhưng P2 *bị pin* nên buffer manager bỏ qua, đá `P3` — pin là cái chốt an toàn khi ai đó đang đọc dở.

> [!note] Tự thử
> 1. Tăng `capacity` từ 3 lên 5 rồi chạy lại dãy đầu: hit/miss đổi thế nào? Vì sao buffer lớn hơn (gần bằng working set) làm hit tăng vọt?
> 2. Thêm `bp.access("P4", true)` *trước* khi P4 bị evict lần nữa: số `ghi-lại-đĩa` đổi không? (gợi ý: bẩn vẫn là bẩn, ghi một lần khi evict.)
> 3. Ở demo pin, thử `bp2.pin("P2")` *cả* `bp2.pin("P4")` rồi `access("P5")` — chuyện gì xảy ra? Vì sao "pin quá nhiều" là nguy hiểm (sách tr. 605)?
> 4. Đổi chính sách: thay LRU bằng **FIFO** (đá theo thứ tự *nạp vào*, không cập nhật khi hit). Với dãy có `read P1` lặp lại, FIFO cho hit ít hơn hay nhiều hơn LRU? Vì sao?

## 6. Bản đồ khoá database

| # | Bài | Mảng | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | DBMS là gì & vì sao cần | động lực, trừu tượng hoá | Silberschatz Ch1 |
| 1 | Mô hình quan hệ & đại số quan hệ | nền toán của bảng/SQL | Ch2 |
| 2 | SQL từ nền tới sâu | truy vấn, join, view | Ch3–5 |
| 3 | Thiết kế & chuẩn hoá (E-R, FD, BCNF) | thiết kế đúng | Ch6–7 |
| 4 | **Lưu trữ vật lý & buffer manager** ← *đang ở đây* | dữ liệu trên đĩa/RAM | Ch12–13 |
| 5 | Index: B+tree | tra cứu nhanh | Ch14 |
| 6 | Index nâng cao: LSM & bitmap | tối ưu ghi/phân tích | Ch24 |
| 7 | Xử lý truy vấn: join algorithms | thực thi truy vấn | Ch15 |
| 8 | Tối ưu truy vấn (cost-based) | chọn kế hoạch rẻ nhất | Ch16 |
| 9 | Transaction & ACID, isolation | đúng khi có lỗi | Ch17 |
| 10 | Đồng thời: 2PL / MVCC | đúng khi song song | Ch18 |
| 11 | Phục hồi: WAL / ARIES | sống sót sau sập | Ch19 |
| 12 | Song song & phân tán (góc DB) | mở rộng ra nhiều máy | Ch20–23 + Red Book |

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 4.1 — Vì sao database cần cả đĩa lẫn RAM, không dùng một cái?
> **Đáp:** đĩa **bền** nhưng **chậm**; RAM **nhanh** nhưng **bay hơi** và **nhỏ hơn** CSDL. Dữ liệu thật phải ở đĩa (non-volatile); tính toán phải ở RAM. Buffer manager bắc cầu.

> [!question] Thẻ 4.2 — Đơn vị truyền dữ liệu giữa đĩa và RAM là gì? Hệ quả khi đo chi phí?
> **Đáp:** **block** (4–16KB). Một bản ghi nhỏ vẫn tốn nguyên một block I/O → đo chi phí truy vấn bằng **số block I/O**, không bằng số byte.

> [!question] Thẻ 4.3 — Buffer và buffer manager là gì?
> **Đáp:** **buffer** = phần RAM chứa *bản sao* các block đĩa; **buffer manager** = bộ phận cấp phát/thay thế buffer. Mọi truy cập dữ liệu đi qua nó (hit = khỏi đụng đĩa).

> [!question] Thẻ 4.4 — LRU là gì? Dirty page ảnh hưởng eviction thế nào?
> **Đáp:** LRU đá block **lâu không dùng nhất**. Block **bẩn** (đã sửa) phải **ghi lại đĩa** khi bị đá; block **sạch** chỉ việc bỏ (bản đĩa còn đúng).

> [!question] Thẻ 4.5 — Pin dùng để làm gì? Nguy cơ khi pin quá nhiều?
> **Đáp:** pin chặn eviction khi tiến trình đang đọc/sửa block (tránh đọc rác). Pin hết buffer → không đá được block nào → **không nạp được block mới → kẹt cứng**.

## 8. Câu hỏi tự kiểm tra

1. Giải thích nghịch lý "bền nhưng chậm vs nhanh nhưng bay hơi". Buffer manager giải nó ra sao? *(mục 1, 4)*
2. Vì sao đọc một bản ghi 200 byte lại tốn chi phí như đọc cả 4KB? *(mục 2)*
3. Slotted page giải quyết vấn đề gì với bản ghi dài thay đổi? Vì sao con trỏ ngoài không cần đổi khi di dời bản ghi trong block? *(mục 3)*
4. Khi buffer đầy và cần nạp block mới: mô tả các bước buffer manager làm. Khi nào phải ghi lại đĩa? *(mục 4, Silberschatz tr. 604)*
5. Chạy demo mục 5, làm Tự thử 1 (tăng capacity). Giải thích quan hệ giữa kích thước buffer và hit rate. *(mục 5)*

## Tóm tắt một trang

```
BÀI 4 — LƯU TRỮ VẬT LÝ & BUFFER MANAGER
─────────────────────────────────────────────────────────
NGHỊCH LÝ  đĩa BỀN nhưng CHẬM; RAM NHANH nhưng BAY HƠI + NHỎ hơn CSDL. Dữ liệu
   thật ở đĩa (non-volatile), tính ở RAM. Ranh giới volatile giữa RAM↔flash (tr.562).

BLOCK  đơn vị truyền đĩa↔RAM (4–16KB, tr.578). Bản ghi nhỏ vẫn tốn nguyên 1 block
   → đo chi phí bằng SỐ BLOCK I/O. Slotted page (tr.593): header+slot trỏ bản ghi,
   bản ghi mọc từ cuối → di dời trong block không đổi con trỏ ngoài.

BUFFER MANAGER  buffer = phần RAM chứa BẢN SAO block đĩa; manager cấp phát/thay thế
   (tr.604). Mọi truy cập qua nó. HIT (có sẵn, nhanh) vs MISS (đọc đĩa).

THAY THẾ  LRU: đá block lâu không dùng nhất (tr.605). DIRTY page (đã sửa) → phải
   GHI LẠI đĩa khi evict; CLEAN → chỉ bỏ. PIN: không bao giờ đá block đang pin
   (tránh đọc rác); pin quá nhiều → kẹt cứng.

DEMO  pool 3 frame/6 page: thấy LRU đổi thứ tự, P4 bẩn evict→ghi lại, pin chặn đá P2.
   Buffer lớn hơn → hit rate cao hơn. (nền cho B+tree Bài 5: nút = 1 block)
```

## Nguồn

- **Silberschatz, Korth, Sudarshan — *Database System Concepts*, 7th ed.** — **Ch12 Physical Storage Systems**: phân cấp lưu trữ, volatile vs non-volatile (tr. 562); **Ch13 Data Storage Structures**: block là đơn vị truyền (tr. 578), slotted-page (tr. 593), buffer & buffer manager (tr. 604), LRU & dirty write-back, pin (tr. 605). `tai_lieu/Database System Concepts 7th Edition...pdf` (offset **PDF = tr. + 29**).
- Liên hệ: [cloud-base Bài 10 — storage engine](../../cloud-base/bai_hoc/bai_10_du-lieu-storage.md) (append-log, B-tree vs LSM ở góc data-intensive); [cloud-base Bài 13 — OS scheduling](../../cloud-base/bai_hoc/bai_13_os-scheduling-locks.md).

---

**Bản đồ khoá học:** [Bài 0 — DBMS là gì](bai_00_dbms-la-gi.md) · [Bài 1 — Mô hình quan hệ & đại số quan hệ](bai_01_mo-hinh-quan-he.md) · [Bài 2 — SQL từ nền tới sâu](bai_02_sql.md) · [Bài 3 — Thiết kế & chuẩn hoá](bai_03_thiet-ke-chuan-hoa.md) · **[Bài 4 — Lưu trữ & buffer manager] ← bạn đang ở đây** · [Bài 5 — Index: B+tree](bai_05_index-btree.md) · [Bài 6 — Index nâng cao: LSM & bitmap](bai_06_index-lsm-bitmap.md) · [Bài 7 — Join algorithms](bai_07_query-join.md) · [Bài 8 — Tối ưu truy vấn](bai_08_query-optimization.md) · [Bài 9 — Transaction & ACID](bai_09_transaction-acid.md) · [Bài 10 — Đồng thời: 2PL/MVCC](bai_10_concurrency.md) · [Bài 11 — Phục hồi: WAL/ARIES](bai_11_recovery.md) · [Bài 12 — Song song & phân tán](bai_12_phan-tan.md)

Xem thêm [README khoá học](../README.md).
