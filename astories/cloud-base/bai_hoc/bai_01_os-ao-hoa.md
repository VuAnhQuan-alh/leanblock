# Bài 1 — OS trụ 1a: Ảo hoá (process, CPU, bộ nhớ)

> [!info] Về bài này
> **Trụ 1 (OS), mảnh 1/3: ảo hoá (virtualization).** OSTEP tổ chức quanh ba mảnh — *virtualization, concurrency, persistence* (Bài 0). Bài này là mảnh đầu: OS biến **một** CPU + **một** vùng RAM vật lý thành **ảo giác** mỗi chương trình có CPU riêng, bộ nhớ riêng. Hiểu nó rồi, **EC2 / Lambda / Fargate** của `aws-fund` lộ ra bản chất: tất cả đều là *ảo hoá đẩy lên một tầng nữa*.
> Nguồn: **OSTEP** — *Operating Systems: Three Easy Pieces*, chương 2 (Introduction) và chương 4 (The Abstraction: The Process).
> **Trích:** `OSTEP tr. X` = trang **in trong sách**; offset PDF: **PDF = tr. + 25** (PDF 48 = tr. 23). Câu chốt để nguyên văn trong `[!quote]`.
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.
> Nên đọc trước: [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md).

## Mục lục

1. [Process: trừu tượng của chương trình đang chạy](#1-process-trừu-tượng-của-chương-trình-đang-chạy)
2. [Ảo hoá CPU: ảo giác chạy đồng thời](#2-ảo-hoá-cpu-ảo-giác-chạy-đồng-thời)
3. [Ảo hoá bộ nhớ: address space riêng cho mỗi process](#3-ảo-hoá-bộ-nhớ-address-space-riêng-cho-mỗi-process)
4. [Demo: đo time-sharing bằng thời gian thật](#4-demo-đo-time-sharing-bằng-thời-gian-thật)
5. [Bảng so sánh: ảo hoá ba tài nguyên](#5-bảng-so-sánh-ảo-hoá-ba-tài-nguyên)
6. [Nối về AWS](#6-nối-về-aws)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Process: trừu tượng của chương trình đang chạy

Khái niệm nền số một của OS là **process**. Đừng lẫn với "chương trình": *chương trình* là file nằm im trên đĩa; *process* là chương trình **đang chạy** — có trạng thái, có tài nguyên.

> [!quote] OSTEP (tr. 23)
> "The abstraction provided by the OS of a running program is something we will call a process. As we said above, a process is simply a running program; at any instant in time, we can summarize a process by taking an inventory of the different pieces of the system it accesses or affects during the course of its execution."
>
> *Trừu tượng mà OS cung cấp cho **một chương trình đang chạy** gọi là **process**. Như đã nói, process đơn giản là một chương trình đang chạy; tại mỗi thời điểm, ta tóm tắt một process bằng cách kiểm kê những phần của hệ thống mà nó truy cập hoặc tác động trong quá trình thực thi.*

"Kiểm kê" đó gồm những gì? Chủ yếu là **machine state** — thứ chương trình đọc/ghi khi chạy: bộ nhớ nó địa chỉ hoá được (address space), các thanh ghi (registers), trong đó có **program counter** (lệnh kế tiếp sẽ chạy) và **stack pointer**. Toàn bộ "ảnh chụp" này là cái OS phải *lưu lại rồi khôi phục* mỗi khi nó chuyển sang chạy process khác — đó là **context switch**, hạt nhân của ảo hoá CPU ở mục 2.

Một process không ở mãi một trạng thái. Ba trạng thái cơ bản:

```
             được xếp lịch (sched)
   ┌───────────┐ ──────────────────▶ ┌───────────┐
   │   READY   │                     │  RUNNING  │
   │(sẵn sàng) │ ◀────────────────── │(đang chạy)│
   └───────────┘   bị tước CPU       └───────────┘
         ▲                                 │
         │ I/O xong          phát lệnh I/O │
         │                                 ▼
         │                            ┌───────────┐
         └─────────────────────────── │  BLOCKED  │
                                      │  (chờ)    │
                                      └───────────┘
```

- **RUNNING**: đang thực sự chiếm một CPU.
- **READY**: sẵn sàng chạy nhưng OS chưa cho (đang xếp hàng). Mỗi lần OS chuyển một process từ RUNNING về READY để chạy process khác, chính là time-sharing.
- **BLOCKED**: chờ một sự kiện (đọc đĩa, gói mạng về). Nó *không* tiêu CPU khi chờ — đây là lý do một server có 4 lõi vẫn phục vụ hàng nghìn kết nối: phần lớn đang BLOCKED chờ mạng (nối tới Bài 2 concurrency và Bài 5 TCP).

## 2. Ảo hoá CPU: ảo giác chạy đồng thời

Máy của bạn mở hàng chục process cùng lúc, nhưng số lõi CPU chỉ đếm trên đầu ngón tay. Làm sao? OS **dối** — một cách có kỷ luật:

> [!quote] OSTEP (tr. 2)
> "Turning a single CPU (or small set of them) into a seemingly infinite number of CPUs and thus allowing many programs to seemingly run at once is what we call virtualizing the CPU."
>
> *Biến **một** CPU (hoặc một nhúm nhỏ) thành **dường như vô số** CPU, nhờ đó cho phép nhiều chương trình **dường như chạy cùng lúc** — đó là cái ta gọi là **ảo hoá CPU**.*

Hai chữ "seemingly" (dường như) là linh hồn của ảo hoá: không có vô số CPU nào cả, chỉ là OS **luân phiên** cực nhanh nên mắt người (và bản thân mỗi process) tưởng mình độc chiếm. Cơ chế đó có tên:

> [!quote] OSTEP (tr. 23)
> "Time sharing is a basic technique used by an OS to share a resource. By allowing the resource to be used for a little while by one entity, and then a little while by another, and so forth, the resource in question (e.g., the CPU, or a network link) can be shared by many."
>
> *Chia-thời-gian (time sharing) là kỹ thuật cơ bản để OS **chia sẻ một tài nguyên**: cho một thực thể dùng một chút, rồi thực thể khác một chút, cứ thế — nhờ đó tài nguyên (vd. CPU, hay một đường mạng) được **nhiều bên dùng chung**.*

Hình dung trên **một** CPU vật lý, trục thời gian chạy ngang:

```
1 CPU vật lý │ A | B | A | C | B | A | C | A | ...   (OS luân phiên từng lát)
             └───────────────────────────────────▶ thời gian
Ảo giác      │ A, B, C đều tưởng "mình đang chạy liên tục, một mình một CPU"
```

Mỗi lần đổi từ A sang B, OS làm **context switch**: lưu machine state của A, nạp của B. Đổi đủ nhanh (hàng nghìn lần/giây) thì ba process *trông như* song song. Điểm mấu chốt — và là thứ demo mục 4 đo được: **ảo giác không miễn phí**. Nếu việc cần làm nhiều hơn số lõi, tổng thời gian thật *phải* giãn ra, vì chỉ có bấy nhiêu lõi để chia.

> [!warning] "Song song" (parallel) ≠ "đồng thời" (concurrent)
> *Song song thật* = nhiều lõi cùng làm cùng lúc (tăng tốc thật). *Đồng thời nhờ time-sharing* = một lõi luân phiên (không tăng tốc, chỉ tạo cảm giác phản hồi). Lẫn hai cái này là nguồn gốc của kỳ vọng sai về hiệu năng — và là lằn ranh giữa Bài 1 (ảo hoá) với Bài 2 (concurrency).

## 3. Ảo hoá bộ nhớ: address space riêng cho mỗi process

OS không chỉ ảo hoá CPU — nó ảo hoá cả **bộ nhớ**. Mỗi process được phát cho một ảo giác thứ hai: *nó sở hữu trọn bộ nhớ của máy*, bắt đầu từ địa chỉ 0.

> [!quote] OSTEP (tr. 23)
> "Thus the memory that the process can address (called its address space) is part of the process."
>
> *Vậy phần bộ nhớ mà process địa chỉ hoá được (gọi là **address space** — không gian địa chỉ) là một phần của process.*

> [!quote] OSTEP (tr. 4)
> "Each process accesses its own private virtual address space (sometimes just called its address space), which the OS somehow maps onto the physical memory of the machine."
>
> *Mỗi process truy cập **address space ảo riêng tư của chính nó** (đôi khi gọi tắt là address space), rồi OS bằng cách nào đó **ánh xạ** nó xuống bộ nhớ vật lý của máy.*

Hệ quả thực tế: hai process cùng ghi vào "địa chỉ 0x1000" **không** đạp lên nhau — OS ánh xạ mỗi address space ảo xuống một vùng vật lý khác nhau. Đây là **tường cách ly**: một process sập không kéo process khác sập, một bug con trỏ không đọc trộm được RAM của tiến trình kề bên. Chính sự cách ly này là thứ ta mua lại ở tầng cloud dưới cái tên **isolation** — mỗi lời gọi Lambda, mỗi container, mỗi VM đều dựng trên ý tưởng "address space riêng" phóng to lên.

## 4. Demo: đo time-sharing bằng thời gian thật

Lý thuyết nói "ảo giác không miễn phí". Hãy **đo** nó. Ta phóng ra nhiều "công việc" nặng CPU (mỗi việc là một worker thread quay vòng tính toán) và đo thời gian thật ở ba mức: 1 việc, số-việc-bằng-số-lõi, và gấp 4 lần số lõi. Nếu CPU thực sự "vô số" như ảo giác, thời gian phải không đổi. Nó **không** không đổi — đó là bằng chứng của time-sharing.

> [!quote] OSTEP (tr. 2)
> "Turning a single CPU (or small set of them) into a seemingly infinite number of CPUs ..."
>
> *... "dường như vô số CPU" — demo dưới cho thấy chữ "dường như" tốn đúng bao nhiêu.*

```typescript
// Ảo hoá CPU: "chạy đồng thời" chỉ là ảo giác do OS luân phiên (time-sharing).
// Chứng minh bằng cách đo thời gian thật: 1 CPU vật lý không nhân bản khi ta
// phóng thêm "process" — nó chỉ bị chia nhỏ ra.
import { Worker, isMainThread, parentPort } from "node:worker_threads";
import { availableParallelism } from "node:os";

const ITERATIONS = 60_000_000; // khối lượng CPU cố định cho MỘT "công việc"

function burn(): void {
  let x = 0;
  for (let i = 0; i < ITERATIONS; i++) x += Math.sqrt(i) % 7;
  if (x < 0) console.log(x); // chặn tối ưu hoá xoá vòng lặp
}

if (!isMainThread) {
  burn();
  parentPort!.postMessage("done");
} else {
  const cores = availableParallelism();

  function runJobs(n: number): Promise<number> {
    const start = performance.now();
    return new Promise((resolve) => {
      let left = n;
      for (let i = 0; i < n; i++) {
        const w = new Worker(new URL(import.meta.url), {});
        w.on("message", () => {
          w.terminate();
          if (--left === 0) resolve(performance.now() - start);
        });
      }
    });
  }

  const main = async (): Promise<void> => {
    console.log(`Máy này có ${cores} CPU lõi dùng được.\n`);
    const t1 = await runJobs(1);
    const tC = await runJobs(cores);
    const tX = await runJobs(cores * 4);
    const ms = (t: number) => `${t.toFixed(0)} ms`;
    console.log(`1 việc               : ${ms(t1)}  (mốc chuẩn, 1 lõi làm)`);
    console.log(`${cores} việc (= số lõi)     : ${ms(tC)}  (mọi lõi làm song song THẬT)`);
    console.log(`${cores * 4} việc (gấp 4 số lõi): ${ms(tX)}  (lõi đã bão hoà → phải luân phiên)`);
    console.log(`\nTừ "đủ lõi" sang "gấp 4 số lõi": ${ms(tC)} → ${ms(tX)} ≈ ${(tX / tC).toFixed(1)}x`);
    console.log("Gấp 4 lần việc trên vùng bão hoà ⇒ gấp ~4 lần thời gian.");
    console.log("CPU KHÔNG nhân thêm. 'Chạy đồng thời' là ảo giác — OS juggling.");
    console.log("(Thời gian tuỳ máy; TỈ LỆ ~4x ở dòng cuối mới là điều cần nhìn.)");
  };
  main();
}
```

Kết quả chạy thật *(số ms tuỳ máy và tuỳ lần chạy — điều cần nhìn là **tỉ lệ ~4x** ở dòng cuối, không phải con số tuyệt đối)*:

```
Máy này có 11 CPU lõi dùng được.

1 việc               : 570 ms  (mốc chuẩn, 1 lõi làm)
11 việc (= số lõi)     : 1108 ms  (mọi lõi làm song song THẬT)
44 việc (gấp 4 số lõi): 4086 ms  (lõi đã bão hoà → phải luân phiên)

Từ "đủ lõi" sang "gấp 4 số lõi": 1108 ms → 4086 ms ≈ 3.7x
Gấp 4 lần việc trên vùng bão hoà ⇒ gấp ~4 lần thời gian.
CPU KHÔNG nhân thêm. 'Chạy đồng thời' là ảo giác — OS juggling.
(Thời gian tuỳ máy; TỈ LỆ ~4x ở dòng cuối mới là điều cần nhìn.)
```

Đọc kết quả: lên tới số lõi, thêm việc gần như *miễn phí* (song song thật). Vượt qua, mỗi lần nhân đôi khối lượng là nhân đôi thời gian — **lõi đã bão hoà, OS chỉ còn cách luân phiên**. Ảo giác "vô số CPU" vỡ ngay khi bạn ép nó làm nhiều hơn phần cứng cho phép. Đây chính xác là *vì sao* đặt quá nhiều việc nặng-CPU lên một máy/một hàm không "nhanh hơn" — và là nền của mọi quyết định về số vCPU ở mục 6.

> [!note] Tự thử
> - Đổi `ITERATIONS` còn `6_000_000`: baseline nhỏ lại, chi phí dựng worker (cố định) chiếm tỉ trọng lớn hơn → tỉ lệ méo đi. Nhận ra: *đo cái gì cũng dính overhead của phép đo*.
> - Thêm mức `runJobs(cores * 8)`: xác nhận đường thẳng tuyến tính vẫn tiếp tục (≈8x so với mức "đủ lõi").
> - In thêm `process.pid` trong worker (`import process`): mọi worker *cùng* một pid — vì `worker_threads` là **luồng trong cùng một process**, không phải process OS riêng. Process thật tách rời cần `child_process`.

## 5. Bảng so sánh: ảo hoá ba tài nguyên

Ảo hoá là **một ý tưởng** áp lên nhiều tài nguyên. Nhìn chúng cạnh nhau để thấy khuôn chung — và để sau này nhận ra mỗi dịch vụ AWS đang ảo hoá cái gì:

| Tài nguyên vật lý | Ảo giác OS bán cho process | Cơ chế                     | Khi nào ảo giác vỡ                         |
| :---------------- | :------------------------- | :------------------------- | :----------------------------------------- |
| CPU (ít lõi)      | "CPU riêng, chạy liên tục" | time-sharing + context switch | việc > lõi → thời gian giãn tuyến tính   |
| RAM vật lý        | "toàn bộ bộ nhớ, từ 0"     | address space ảo + ánh xạ  | hết RAM → swap xuống đĩa, chậm hàng nghìn lần |
| 1 process         | "máy của riêng tôi"        | cách ly address space      | bug/exploit phá rào cách ly                |

Khuôn chung: **nhiều khách tin mình độc chiếm một tài nguyên vật lý khan hiếm; một lớp trung gian (OS) luân phiên + ánh xạ để duy trì ảo giác; ảo giác vỡ khi cầu vượt cung.** Giữ đúng khuôn này — cả cloud là nó, phóng to.

## 6. Nối về AWS

> [!note] Nối về AWS
> Mọi dịch vụ **compute** của AWS chỉ là ảo hoá đẩy lên các tầng khác nhau — xem [`aws-fund` Bài 2 — Compute](../../aws-fund/bai_hoc/bai_02_compute.md):
> - **EC2** = ảo hoá **nguyên cái máy** (một VM: CPU ảo + RAM ảo + đĩa ảo, nhiều VM chia một máy chủ vật lý). "**vCPU**" trong bảng giá chính là *lát time-share* của mục 2 — không phải một lõi vật lý trọn vẹn.
> - **Lambda** = ảo hoá ở mức **process phù du**: mỗi lời gọi chạy trong một môi trường cô lập rồi biến mất. **Cold start** = cái giá dựng address space + nạp code *mới toanh* cho một "process" chưa tồn tại — đúng chi phí context mà mục 1 mô tả, cộng độ trễ mạng của [Bài 0](bai_00_vi-sao-nen-tang.md).
> - **Fargate** = ảo hoá mức **container**: cách ly kiểu address space (mục 3) nhưng cho cả một cây tiến trình, không cần bạn quản VM.
> - Vì sao Lambda tính tiền theo **GB-giây** chứ không theo "số lần"? Vì tài nguyên thật bị *time-share + ánh xạ*: bạn trả cho **lát CPU × RAM × thời gian** mình thực sự chiếm của máy vật lý dùng chung — y hệt mô hình "chia sẻ tài nguyên khan hiếm" của mục 5.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 1.1 — Phân biệt *chương trình* và *process*.
> **Đáp:** chương trình = file tĩnh trên đĩa; process = chương trình **đang chạy**, có machine state (bộ nhớ/address space + thanh ghi + PC + stack pointer) mà OS kiểm kê.

> [!question] Thẻ 1.2 — "Ảo hoá CPU" theo OSTEP là gì? Chữ nào là linh hồn?
> **Đáp:** biến một (nhúm) CPU thành *dường như vô số* CPU, cho nhiều chương trình *dường như* chạy cùng lúc. Linh hồn = "**seemingly/dường như**": không có CPU thật nào thêm, chỉ là time-sharing luân phiên.

> [!question] Thẻ 1.3 — Ba trạng thái process và trạng thái nào *không* tốn CPU?
> **Đáp:** RUNNING (đang chạy), READY (chờ được xếp lịch), BLOCKED (chờ I/O). BLOCKED không tốn CPU → một server ít lõi vẫn ôm nhiều kết nối đang chờ mạng.

> [!question] Thẻ 1.4 — Address space ảo giải quyết vấn đề gì?
> **Đáp:** mỗi process tưởng mình sở hữu trọn bộ nhớ từ địa chỉ 0; OS ánh xạ mỗi address space ảo xuống vùng vật lý khác nhau → **cách ly**: hai process không đạp bộ nhớ nhau, một process sập không kéo process khác.

> [!question] Thẻ 1.5 — Demo cho thấy ảo giác "vô số CPU" vỡ khi nào, và đo bằng gì?
> **Đáp:** vỡ khi số việc nặng-CPU > số lõi; đo bằng **thời gian thật** — vượt số lõi thì thời gian giãn tuyến tính (gấp 4 việc ⇒ ~4x thời gian).

> [!question] Thẻ 1.6 — "vCPU" của EC2 và "cold start" của Lambda nối về khái niệm nền nào?
> **Đáp:** vCPU = một *lát time-share* (không phải lõi vật lý trọn vẹn); cold start = chi phí dựng address space + nạp code cho một process phù du mới toanh.

## 8. Câu hỏi tự kiểm tra

1. Định nghĩa process theo OSTEP. "Machine state" của một process gồm những gì? *(mục 1, tr. 23)*
2. Giải thích vì sao 10 process chạy được trên 1 CPU. Vai trò của context switch? *(mục 2)*
3. Phân biệt "song song thật" và "đồng thời nhờ time-sharing". Cái nào tăng tốc thật? *(mục 2)*
4. Address space ảo mang lại tính chất gì, và vì sao nó quan trọng cho bảo mật/độ tin cậy? *(mục 3, tr. 4 & 23)*
5. Chạy demo mục 4. Vì sao mức "= số lõi" rẻ mà mức "gấp 4 lõi" lại đắt ~4x? *(mục 4)*
6. Ánh xạ: EC2 / Lambda / Fargate mỗi cái ảo hoá ở mức nào? vCPU và GB-giây phản ánh điều gì về tài nguyên dùng chung? *(mục 6)*

## Tóm tắt một trang

```
BÀI 1 — OS TRỤ 1a: ẢO HOÁ (process · CPU · bộ nhớ)
─────────────────────────────────────────────────────────
PROCESS  = chương trình ĐANG CHẠY (khác file tĩnh trên đĩa).
   Machine state: address space + thanh ghi + PC + stack pointer.
   3 trạng thái: RUNNING / READY / BLOCKED (BLOCKED không tốn CPU).

ẢO HOÁ CPU  "biến 1 CPU thành DƯỜNG NHƯ vô số" (OSTEP tr.2).
   Cơ chế: TIME-SHARING + context switch (lưu/nạp machine state).
   Linh hồn = "seemingly": không có CPU thật nào thêm.
   Song song THẬT (nhiều lõi) ≠ đồng thời nhờ luân phiên (1 lõi).

ẢO HOÁ BỘ NHỚ  mỗi process có ADDRESS SPACE ảo riêng, từ địa chỉ 0;
   OS ánh xạ xuống RAM vật lý khác nhau → CÁCH LY.

DEMO  việc ≤ lõi: gần miễn phí (song song thật).
   việc = 4× lõi: ~4x thời gian → ảo giác "vô số CPU" VỠ khi cầu>cung.

KHUÔN CHUNG  nhiều khách tưởng độc chiếm tài nguyên khan hiếm;
   OS luân phiên + ánh xạ giữ ảo giác; vỡ khi cầu vượt cung.

NỐI VỀ AWS  EC2 = ảo hoá nguyên máy (vCPU = lát time-share);
   Lambda = process phù du (cold start = dựng address space+nạp code);
   Fargate = ảo hoá container; GB-giây = trả theo lát-tài-nguyên × giờ.
```

## Nguồn

- **Remzi H. & Andrea C. Arpaci-Dusseau**, *Operating Systems: Three Easy Pieces* — **chương 2 (Introduction)**: "virtualizing the CPU" (tr. 2), "virtual address space" (tr. 4); **chương 4 (The Abstraction: The Process)**: định nghĩa process, time-sharing, address space (tr. 23). `tai_lieu/Operating systems three easy pieces.pdf` — **offset PDF = tr. + 25** (PDF 48 = tr. 23).
- Nối về AWS: [`aws-fund` Bài 2 — Compute](../../aws-fund/bai_hoc/bai_02_compute.md) (EC2/Lambda/Fargate, cold start, GB-giây).
- Hai mảnh còn lại của OS: [Bài 2 — concurrency](bai_02_os-concurrency.md), [Bài 3 — lưu trữ](bai_03_os-luu-tru.md).

---

**Bản đồ khoá học — lõi:** [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md) · **[Bài 1 — OS: ảo hoá] ← bạn đang ở đây** · [Bài 2 — OS: concurrency](bai_02_os-concurrency.md) · [Bài 3 — OS: lưu trữ](bai_03_os-luu-tru.md) · [Bài 4 — Mạng: phân tầng, HTTP, DNS](bai_04_mang-http-dns.md) · [Bài 5 — Mạng: TCP, TLS](bai_05_mang-tcp-tls.md) · [Bài 6 — Mạng: hiệu năng, CDN](bai_06_mang-hieu-nang.md) · [Bài 7 — Distributed: giao tiếp & thất bại](bai_07_dist-giao-tiep.md) · [Bài 8 — Distributed: nhân bản & nhất quán](bai_08_dist-nhat-quan.md) · [Bài 9 — Distributed: phân mảnh & consensus](bai_09_dist-phan-manh.md) · [Bài 10 — Dữ liệu: storage engine](bai_10_du-lieu-storage.md) · [Bài 11 — Dữ liệu: batch & stream](bai_11_du-lieu-batch-stream.md)

**Chuyên đề nâng cao:** [Bài 12 — OS nâng cao: bộ nhớ ảo](bai_12_os-bo-nho-ao.md) · [Bài 13 — OS nâng cao: scheduling & locks](bai_13_os-scheduling-locks.md) · [Bài 14 — Mạng nâng cao: bảo mật & mật mã](bai_14_mang-bao-mat.md) · [Bài 15 — Distributed nâng cao: đồng hồ](bai_15_dist-dong-ho.md) · [Bài 16 — Distributed nâng cao: transaction & saga](bai_16_dist-transaction-saga.md) · [Bài 17 — Dữ liệu nâng cao: data models](bai_17_du-lieu-data-models.md) · [Bài 18 — Dữ liệu nâng cao: encoding & schema](bai_18_du-lieu-encoding.md)

Xem thêm [README khoá học](../README.md).
