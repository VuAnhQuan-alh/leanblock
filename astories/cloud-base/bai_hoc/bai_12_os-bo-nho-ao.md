# Bài 12 — OS nâng cao: Bộ nhớ ảo, paging và OOM

> [!info] Về bài này
> **Chuyên đề mở rộng của trụ 1 (OS).** [Bài 1](bai_01_os-ao-hoa.md) nói mỗi process có *address space ảo riêng*; bài này mở nắp xem OS *hiện thực* ảo giác đó ra sao — **paging** (chia bộ nhớ thành trang), **swap** (mượn đĩa giả vờ có nhiều RAM hơn thực), **page fault** (cái giá khi trang không nằm ở RAM). Đây là nền để hiểu **Lambda memory sizing, container OOM-kill, và vì sao "hết RAM" làm hệ chậm sấp mặt** thay vì chỉ "đầy".
> Nguồn: **OSTEP** — ch. 18 (Paging), ch. 21 (Beyond Physical Memory).
> **Trích:** `OSTEP (tr. X)` = trang **in**; **offset PDF = tr. + 25**. Câu chốt nguyên văn trong `[!quote]`.
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`).
> Nên đọc trước: [Bài 1 — ảo hoá](bai_01_os-ao-hoa.md), [Bài 0 — bậc thang độ trễ](bai_00_vi-sao-nen-tang.md).

## Mục lục

1. [Địa chỉ phẳng là ảo giác: chia thành page](#1-địa-chỉ-phẳng-là-ảo-giác-chia-thành-page)
2. [Swap: giả vờ có nhiều RAM hơn thực](#2-swap-giả-vờ-có-nhiều-ram-hơn-thực)
3. [Page fault: cái giá khi page không ở RAM](#3-page-fault-cái-giá-khi-page-không-ở-ram)
4. [Demo: locality quyết định tốc độ](#4-demo-locality-quyết-định-tốc-độ)
5. [Bảng so sánh: cache, RAM, swap](#5-bảng-so-sánh-cache-ram-swap)
6. [Nối về AWS](#6-nối-về-aws)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Địa chỉ phẳng là ảo giác: chia thành page

Ở Bài 1, mỗi process tưởng mình sở hữu một address space liền mạch từ địa chỉ 0. OS dựng ảo giác đó bằng cách chia nhỏ:

> [!quote] OSTEP (tr. 186)
> "In virtual memory, we call this idea paging, and it goes back to an early and important system, the Atlas [KE+62, L78]. Instead of splitting up a process's address space into some number of variable-sized logical segments (e.g., code, heap, stack), we divide it into fixed-sized units, each of which we call a page. Correspondingly, we view physical memory as an array of fixed-sized slots called page frames; each of these frames can contain a single virtual-memory page."
>
> *Trong bộ nhớ ảo, ý tưởng này gọi là **paging**. Thay vì chia address space thành các đoạn (segment) kích thước thay đổi, ta chia nó thành **các đơn vị kích thước cố định, mỗi cái gọi là một page (trang)**. Tương ứng, ta coi bộ nhớ vật lý là **một mảng các ô cố định gọi là page frame**; mỗi frame chứa được đúng một page ảo.*

Mấu chốt: địa chỉ ảo liền mạch của process được **ánh xạ** (qua page table) tới các frame vật lý *rải rác* — hai page kề nhau trong address space ảo có thể nằm ở hai nơi hoàn toàn khác trong RAM thật. Đây chính là cơ chế đằng sau "tường cách ly" ở Bài 1: mỗi process có bảng ánh xạ riêng, nên không với tới RAM của process khác. Và vì ánh xạ ở cấp *trang*, OS có một chiêu mạnh: một page *không cần phải ở trong RAM* lúc nào cũng được.

## 2. Swap: giả vờ có nhiều RAM hơn thực

Nếu page không nhất thiết ở RAM, nó ở đâu khi vắng mặt? Trên đĩa:

> [!quote] OSTEP (tr. 233)
> "The first thing we will need to do is to reserve some space on the disk for moving pages back and forth. In operating systems, we generally refer to such space as swap space, because we swap pages out of memory to it and swap pages into memory from it."
>
> *Việc đầu tiên cần làm là **dành một khoảng trên đĩa** để chuyển page ra-vào. Ta thường gọi đó là **swap space**, vì ta **swap (hoán đổi)** page ra khỏi bộ nhớ xuống đó và swap page từ đó vào bộ nhớ.*

Và đây là mục đích — một ảo giác thứ hai chồng lên ảo giác address space:

> [!quote] OSTEP (tr. 233)
> "Beyond just a single process, the addition of swap space allows the OS to support the illusion of a large virtual memory for multiple concurrently-running processes."
>
> *Vượt ra ngoài một process, swap space cho OS dựng **ảo giác một bộ nhớ ảo lớn** cho **nhiều process chạy đồng thời** — kể cả khi tổng bộ nhớ chúng cần vượt quá RAM vật lý.*

Nghĩa là: tổng address space của mọi process **có thể lớn hơn RAM thật**. OS giữ các page "nóng" (đang dùng) trong RAM, đẩy page "nguội" xuống swap. Tuyệt vời — cho tới khi mọi thứ đều nóng cùng lúc. Lúc đó cái giá hiện ra, và nó có tên: page fault.

## 3. Page fault: cái giá khi page không ở RAM

> [!quote] OSTEP (tr. 239)
> "the operating system page-fault handler runs to service the page fault, and thus arranges for the transfer of the desired page from disk to memory, perhaps first replacing some pages in memory to make room for those soon to be swapped in."
>
> *bộ xử lý **page fault** của OS chạy để phục vụ lỗi trang, dàn xếp **chuyển page cần thiết từ đĩa vào bộ nhớ**, có thể phải **thay (replace) vài page đang ở bộ nhớ trước** để lấy chỗ cho page sắp swap vào.*

Chuỗi sự kiện khi truy cập một page đang ở swap: CPU phát hiện page vắng (không có trong RAM) → **page fault** → OS *đọc page từ đĩa* (một I/O đĩa — chậm hơn RAM hàng nghìn tới triệu lần, Bài 0!) → có thể phải *đẩy một page khác ra* để lấy chỗ. Một truy cập bộ nhớ lẽ ra ~nanosecond bỗng tốn ~mili-giây. Nếu chương trình liên tục chạm page không có trong RAM (**thrashing** — working set lớn hơn RAM), gần *mọi* truy cập thành I/O đĩa, và hệ không "đầy" một cách lịch sự — nó **chậm đi hàng nghìn lần**. Demo mục 4 cho thấy ngay cả khi chưa chạm swap, chỉ cần *kém locality* thôi đã đắt.

## 4. Demo: locality quyết định tốc độ

Không cần ép máy swap (nguy hiểm): ta đo *cùng một khối lượng tính* trên cùng một mảng lớn, chỉ khác **thứ tự duyệt**. Tuần tự = chạm các ô gần nhau (cùng page/cache line). Bước nhảy lớn = mỗi lần nhảy sang page khác → dễ trượt cache/TLB.

```typescript
// Bộ nhớ ảo/paging: địa chỉ "phẳng" là ảo giác; thật ra chia thành PAGE, ánh
// xạ xuống frame vật lý (OSTEP tr.186), phần dư đẩy ra swap trên ĐĨA (tr.233).
// Truy cập đúng locality (gần nhau) thì nhanh; nhảy lung tung thì mỗi bước dễ
// "trượt" cache/TLB/page → chậm. Đây là lý do working-set vượt RAM = thảm hoạ.
const N = 16_000_000;            // ~128MB Float64 — đủ lớn để vượt cache CPU
const arr = new Float64Array(N);
for (let i = 0; i < N; i++) arr[i] = i % 7;

function timeAccess(stride: number, label: string): number {
  const t = performance.now();
  let sum = 0;
  // đi hết mảng, nhưng theo bước 'stride' (stride lớn = nhảy xa = kém locality)
  for (let start = 0; start < stride; start++)
    for (let i = start; i < N; i += stride) sum += arr[i];
  const ms = performance.now() - t;
  if (sum < 0) console.log(sum);   // chặn tối ưu
  console.log(`  ${label.padEnd(34)} ${ms.toFixed(0).padStart(5)} ms`);
  return ms;
}

console.log(`Đi hết ${N.toLocaleString("en")} phần tử (~${(N*8/1e6)|0}MB), cùng số phép cộng, khác THỨ TỰ:`);
const seq = timeAccess(1, "tuần tự (locality tốt)");
const rnd = timeAccess(4096, "bước 4096 (nhảy xa trang khác)");
console.log(`\nCùng khối lượng tính, chỉ khác cách DUYỆT → chậm ~${(rnd/seq).toFixed(1)}x.`);
console.log(`Khác biệt là do TRƯỢT cache/TLB/page. Nếu working-set vượt RAM, mỗi`);
console.log(`trượt thành I/O đĩa (swap) — chậm thêm ngàn lần, hoặc bị OOM-kill.`);
```

Kết quả chạy thật *(số ms tuỳ máy; điều cần nhìn là **tỉ lệ** — cùng khối lượng tính, chỉ khác thứ tự duyệt)*:

```
Đi hết 16,000,000 phần tử (~128MB), cùng số phép cộng, khác THỨ TỰ:
  tuần tự (locality tốt)                15 ms
  bước 4096 (nhảy xa trang khác)        72 ms

Cùng khối lượng tính, chỉ khác cách DUYỆT → chậm ~4.8x.
Khác biệt là do TRƯỢT cache/TLB/page. Nếu working-set vượt RAM, mỗi
trượt thành I/O đĩa (swap) — chậm thêm ngàn lần, hoặc bị OOM-kill.
```

Chú ý: ở đây dữ liệu *vẫn nằm trọn trong RAM* — khác biệt 4,8x hoàn toàn do trượt cache/TLB (tầng nhanh hơn RAM). Giờ hình dung nếu working set vượt RAM: mỗi lần "trượt" không phải lấy từ cache nữa mà là **page fault → đọc đĩa** (mục 3), cái 4,8x biến thành *hàng nghìn lần*. Đó là lý do một dịch vụ "gần hết RAM" không chậm tuyến tính mà rơi xuống vực — và vì sao cloud thà **OOM-kill** (giết tiến trình) còn hơn để nó thrash kéo cả máy xuống.

> [!note] Tự thử
> - Tăng `stride` lên `16384`, `65536`: thường chậm thêm nữa rồi bão hoà — bạn đang dò kích thước cache/trang của máy.
> - Giảm `N` xuống `1_000_000` (~8MB, lọt cache L2/L3): khác biệt tuần tự/nhảy teo lại — vì mọi thứ đã gần CPU. Locality chỉ "đắt" khi dữ liệu lớn.
> - Thử `process.memoryUsage().rss` trước/sau khi cấp mảng: thấy RSS (resident set — phần thực nằm trong RAM) tăng ~128MB. Đây chính là con số mà giới hạn bộ nhớ của Lambda/container soi vào.

## 5. Bảng so sánh: cache, RAM, swap

Bộ nhớ không phải một tầng mà là một *bậc thang*, mỗi bậc chậm hơn bậc trên hàng chục–nghìn lần (nối thẳng bậc thang độ trễ Bài 0):

| Tầng            | Độ trễ bậc độ lớn | Ai quản      | Khi "trượt" xuống tầng dưới         |
| :-------------- | :---------------- | :----------- | :---------------------------------- |
| Thanh ghi/cache | ~1 ns             | CPU          | cache miss → đọc RAM (~chục ns)      |
| RAM (page frame) | ~100 ns          | OS (paging)  | page fault → đọc swap (~ms)          |
| Swap (đĩa/SSD)  | ~ms (chậm ~10⁴×)  | OS + đĩa     | hết swap → **OOM** (giết tiến trình) |

Quy luật: **mỗi lần "trượt" xuống bậc dưới là một bước nhảy độ trễ, không phải trượt dốc đều.** Vì thế hiệu năng bộ nhớ không suy giảm mượt mà — nó rơi theo bậc thang. "Working set vừa RAM" nhanh; "vượt RAM một chút" đã có thể chậm hàng chục lần vì bắt đầu swap. Đây là cùng tinh thần bậc thang của Bài 0, lần này *bên trong một máy*.

## 6. Nối về AWS

> [!note] Nối về AWS
> Giới hạn bộ nhớ là tham số then chốt của mọi compute không-máy-chủ — xem [`aws-fund` Bài 2 — Compute](../../aws-fund/bai_hoc/bai_02_compute.md):
> - **Lambda memory = cả CPU lẫn RAM.** Chọn RAM cho Lambda không chỉ là "đủ chỗ cho dữ liệu" mà còn *cấp CPU tỉ lệ thuận*. Nếu hàm xử lý dữ liệu lớn hơn RAM cấp → không có swap trong Lambda → **lỗi/kill ngay**, không chậm dần. Hiểu working set (mục 3) = chọn đúng mức RAM, tránh cả OOM lẫn trả tiền thừa.
> - **Container OOM-kill (ECS/Fargate/EKS):** khi tiến trình vượt `memory limit`, kernel **OOM-killer** giết nó (không swap trong container mặc định) — đúng bậc cuối của bảng mục 5. "Pod restart liên tục" thường là OOM, không phải bug logic.
> - **Vì sao "thêm RAM" đôi khi cứu hiệu năng kỳ diệu:** nếu dịch vụ đang *thrash* (working set > RAM → page fault liên tục), nâng RAM để working set lọt vào là xoá được hàng loạt I/O đĩa — nhảy từ bậc "swap ~ms" lên "RAM ~100ns".
> - **Instance nén bộ nhớ / `rss`:** chỉ số theo dõi là *resident set size* — phần thực nằm trong RAM (demo mục 4). CloudWatch `MemoryUtilization` soi đúng con số này.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 12.1 — "Paging" là gì? Page và page frame khác nhau thế nào?
> **Đáp:** chia address space ảo thành **page** (đơn vị cố định); RAM vật lý là mảng **page frame** (ô cố định). OS ánh xạ page ảo → frame vật lý rải rác qua page table.

> [!question] Thẻ 12.2 — Swap space để làm gì? Nó tạo ảo giác gì?
> **Đáp:** khoảng trên đĩa để đẩy page ra/vào. Cho OS dựng ảo giác **bộ nhớ ảo lớn hơn RAM thật**, cho nhiều process chạy đồng thời dù tổng vượt RAM.

> [!question] Thẻ 12.3 — Page fault là gì? Vì sao đắt?
> **Đáp:** truy cập một page không có trong RAM → OS đọc page đó **từ đĩa** (một I/O đĩa, ~ms), có thể phải đẩy page khác ra. Đắt vì đĩa chậm hơn RAM ngàn–triệu lần (Bài 0).

> [!question] Thẻ 12.4 — "Thrashing" là gì? Vì sao hiệu năng rơi theo bậc, không mượt?
> **Đáp:** working set > RAM → gần mọi truy cập thành page fault (I/O đĩa). Rơi theo bậc vì mỗi lần trượt xuống tầng dưới (cache→RAM→swap) là một bước nhảy độ trễ hàng chục–ngàn lần.

> [!question] Thẻ 12.5 — Vì sao demo chậm 4,8x dù dữ liệu vẫn trong RAM?
> **Đáp:** khác biệt do trượt **cache/TLB** (tầng nhanh hơn RAM), chỉ khác thứ tự duyệt (locality). Nếu vượt RAM, trượt thành page fault → chậm thêm ngàn lần.

> [!question] Thẻ 12.6 — Vì sao Lambda/container "hết RAM" bị kill chứ không chậm dần?
> **Đáp:** không có swap (mặc định) → không "chậm dần qua đĩa", mà vượt giới hạn là **OOM-kill** ngay. Chọn RAM = hiểu working set để tránh cả kill lẫn trả thừa.

## 8. Câu hỏi tự kiểm tra

1. Giải thích paging. Vì sao hai page kề nhau trong address space ảo có thể ở hai nơi xa nhau trong RAM? *(mục 1, tr. 186)*
2. Swap space là gì? Nó cho phép ảo giác gì? *(mục 2, tr. 233)*
3. Mô tả chuỗi sự kiện của một page fault. Vì sao nó đắt? *(mục 3, tr. 239)*
4. Chạy demo mục 4. Vì sao chậm 4,8x dù chưa chạm swap? Nếu vượt RAM thì sao? *(mục 4)*
5. Vẽ bậc thang cache/RAM/swap. Vì sao hiệu năng bộ nhớ rơi theo bậc? *(mục 5)*
6. Vì sao Lambda/container "hết RAM" bị kill? "Thêm RAM" cứu hiệu năng khi nào? *(mục 6)*

## Tóm tắt một trang

```
BÀI 12 — OS NÂNG CAO: BỘ NHỚ ẢO · PAGING · OOM
─────────────────────────────────────────────────────────
PAGING  chia address space ảo thành PAGE (cố định); RAM = mảng PAGE FRAME;
   OS ánh xạ page→frame rải rác (OSTEP tr.186). Cơ chế của cách ly (Bài 1).

SWAP  dành chỗ trên ĐĨA để đẩy page ra/vào (tr.233) → ảo giác "RAM lớn hơn
   thật", tổng address space mọi process CÓ THỂ vượt RAM vật lý.

PAGE FAULT  chạm page không ở RAM → đọc từ đĩa (~ms, chậm hơn RAM ngàn
   lần — Bài 0), có thể đẩy page khác ra (tr.239). THRASHING = working set
   > RAM → gần mọi truy cập thành I/O đĩa → chậm NGÀN lần.

DEMO  128MB, cùng phép tính, khác thứ tự: tuần tự 15ms vs nhảy 72ms (~4.8x)
   — chỉ do trượt cache/TLB, DỮ LIỆU VẪN TRONG RAM. Vượt RAM → ×1000.

BẬC THANG  cache ~1ns → RAM ~100ns → swap ~ms → OOM. Rơi theo BẬC, không
   mượt: mỗi lần trượt tầng dưới là một bước nhảy độ trễ.

NỐI VỀ AWS  Lambda memory = CPU+RAM, vượt → kill ngay (không swap);
   container OOM-kill (pod restart = OOM, không phải bug); "thêm RAM" cứu
   khi đang thrash; CloudWatch MemoryUtilization = rss (demo).
```

## Nguồn

- **Remzi H. & Andrea C. Arpaci-Dusseau**, *Operating Systems: Three Easy Pieces* — **ch. 18 (Paging: Introduction)**: định nghĩa paging & page frame (tr. 186); **ch. 21 (Beyond Physical Memory: Mechanisms)**: swap space & ảo giác bộ nhớ lớn (tr. 233), page-fault handler (tr. 239). `tai_lieu/Operating systems three easy pieces.pdf` — **offset PDF = tr. + 25**.
- Nối về AWS: [`aws-fund` Bài 2 — Compute](../../aws-fund/bai_hoc/bai_02_compute.md) (Lambda memory, OOM).
- Mở rộng của [Bài 1 — ảo hoá](bai_01_os-ao-hoa.md); cùng bậc thang độ trễ [Bài 0](bai_00_vi-sao-nen-tang.md).

---

**Bản đồ khoá học — lõi:** [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md) · [Bài 1 — OS: ảo hoá](bai_01_os-ao-hoa.md) · [Bài 2 — OS: concurrency](bai_02_os-concurrency.md) · [Bài 3 — OS: lưu trữ](bai_03_os-luu-tru.md) · [Bài 4 — Mạng: phân tầng, HTTP, DNS](bai_04_mang-http-dns.md) · [Bài 5 — Mạng: TCP, TLS](bai_05_mang-tcp-tls.md) · [Bài 6 — Mạng: hiệu năng, CDN](bai_06_mang-hieu-nang.md) · [Bài 7 — Distributed: giao tiếp & thất bại](bai_07_dist-giao-tiep.md) · [Bài 8 — Distributed: nhân bản & nhất quán](bai_08_dist-nhat-quan.md) · [Bài 9 — Distributed: phân mảnh & consensus](bai_09_dist-phan-manh.md) · [Bài 10 — Dữ liệu: storage engine](bai_10_du-lieu-storage.md) · [Bài 11 — Dữ liệu: batch & stream](bai_11_du-lieu-batch-stream.md)

**Chuyên đề nâng cao:** **[Bài 12 — OS nâng cao: bộ nhớ ảo] ← bạn đang ở đây** · [Bài 13 — OS nâng cao: scheduling & locks](bai_13_os-scheduling-locks.md) · [Bài 14 — Mạng nâng cao: bảo mật & mật mã](bai_14_mang-bao-mat.md) · [Bài 15 — Distributed nâng cao: đồng hồ](bai_15_dist-dong-ho.md) · [Bài 16 — Distributed nâng cao: transaction & saga](bai_16_dist-transaction-saga.md) · [Bài 17 — Dữ liệu nâng cao: data models](bai_17_du-lieu-data-models.md) · [Bài 18 — Dữ liệu nâng cao: encoding & schema](bai_18_du-lieu-encoding.md)

Xem thêm [README khoá học](../README.md).
