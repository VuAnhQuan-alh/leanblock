# Bài 3 — OS trụ 1c: Lưu trữ bền (file system, crash consistency, journaling)

> [!info] Về bài này
> **Trụ 1 (OS), mảnh 3/3: persistence (lưu trữ bền).** Khép lại ba mảnh của OSTEP. [Bài 1](bai_01_os-ao-hoa.md) ảo hoá CPU/bộ nhớ (mất khi tắt máy); bài này lo phần *sống sót qua mất điện và crash*. Ý tưởng trung tâm — **write-ahead logging / journaling** — chính là thứ OSTEP nói thẳng là "ăn cắp từ thế giới cơ sở dữ liệu", nên nó là cây cầu đẹp nhất sang trụ Dữ liệu và sang **độ bền (durability) của S3/EBS/Aurora** ở `aws-fund`.
> Nguồn: **OSTEP** — chương 2 §2.4 (Persistence) và chương 42 (Crash Consistency: FSCK and Journaling).
> **Trích:** `OSTEP (tr. X)` = trang **in**; **offset PDF = tr. + 25**. Câu chốt nguyên văn trong `[!quote]`.
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`).
> Nên đọc trước: [Bài 2 — concurrency](bai_02_os-concurrency.md) (ý "all or nothing" sẽ quay lại).

## Mục lục

1. [Persistence: vì sao lưu trữ bền lại khó](#1-persistence-vì-sao-lưu-trữ-bền-lại-khó)
2. [File system: trừu tượng file, và điều OS KHÔNG ảo hoá](#2-file-system-trừu-tượng-file-và-điều-os-không-ảo-hoá)
3. [Crash consistency và write-ahead logging (journaling)](#3-crash-consistency-và-write-ahead-logging-journaling)
4. [Demo: ghi đè tại chỗ vs tmp rồi rename](#4-demo-ghi-đè-tại-chỗ-vs-tmp-rồi-rename)
5. [Bảng so sánh: ba tầng bảo đảm durability](#5-bảng-so-sánh-ba-tầng-bảo-đảm-durability)
6. [Nối về AWS](#6-nối-về-aws)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Persistence: vì sao lưu trữ bền lại khó

Mọi thứ Bài 1–2 xây đều sống trong **RAM**, và RAM có một tật chết người:

> [!quote] OSTEP (tr. 7)
> "In system memory, data can be easily lost, as devices such as DRAM store values in a volatile manner; when power goes away or the system crashes, any data in memory is lost. Thus, we need hardware and software to be able to store data persistently; such storage is thus critical to any system as users care a great deal about their data."
>
> *Trong bộ nhớ hệ thống, dữ liệu **dễ mất**: DRAM lưu giá trị **bay hơi (volatile)**; mất điện hay crash là **mất sạch** dữ liệu trong bộ nhớ. Vì vậy ta cần phần cứng + phần mềm để lưu **bền (persistently)** — kho lưu đó tối quan trọng vì người dùng rất quý dữ liệu của họ.*

Lưu bền khó vì hai lý do, và cả hai sẽ vang vọng suốt khoá: (1) thiết bị lưu trữ **chậm hơn RAM hàng nghìn tới triệu lần** (bậc thang độ trễ Bài 0), nên mọi thiết kế file system/DB là một cuộc chiến giấu độ chậm đó; (2) **crash có thể rơi vào bất kỳ thời điểm nào** — kể cả giữa lúc đang ghi.

## 2. File system: trừu tượng file, và điều OS KHÔNG ảo hoá

Phần mềm lo việc lưu bền có tên quen thuộc:

> [!quote] OSTEP (tr. 7)
> "The software in the operating system that usually manages the disk is called the file system; it is thus responsible for storing any files the user creates in a reliable and efficient manner on the disks of the system."
>
> *Phần mềm trong OS thường quản lý đĩa gọi là **file system**; nó chịu trách nhiệm lưu mọi file người dùng tạo ra một cách **tin cậy và hiệu quả** trên các đĩa của hệ thống.*

Có một điểm khác biệt sâu sắc với Bài 1 mà OSTEP nhấn mạnh ngay sau đó: với CPU và bộ nhớ, OS tạo *ảo giác riêng tư* cho mỗi process (mỗi process tưởng có CPU riêng, address space riêng). Nhưng với đĩa thì **không** — OS *không* dựng một "đĩa ảo riêng" cho từng ứng dụng. Lý do: file sinh ra để **chia sẻ**. Bạn muốn `cc` đọc file `.c` mà editor vừa ghi; muốn gửi file cho người khác. Hệ quả kiến trúc: file system là **không gian chung** — và chia sẻ cộng với ghi đồng thời lại dẫn về đúng bài toán concurrency của Bài 2, lần này trên dữ liệu *bền*.

## 3. Crash consistency và write-ahead logging (journaling)

Đây là vấn đề nan giải trung tâm của lưu trữ bền:

> [!quote] OSTEP (tr. 533)
> "One major challenge faced by a file system is how to update persistent data structures despite the presence of a power loss or system crash. Specifically, what happens if, right in the middle of updating on-disk structures, someone trips over the power cord and the machine loses power?"
>
> *Thách thức lớn của file system: **cập nhật cấu trúc dữ liệu bền ra sao khi mất điện hay crash có thể ập tới**? Cụ thể: điều gì xảy ra nếu **ngay giữa lúc đang cập nhật** cấu trúc trên đĩa, ai đó vấp dây nguồn và máy mất điện?*

Một thao tác "cập nhật" thường gồm nhiều lần ghi đĩa. Crash giữa chừng để lại trạng thái **nửa cũ nửa mới** — file hỏng. Lời giải kinh điển mượn thẳng từ cơ sở dữ liệu:

> [!quote] OSTEP (tr. 539)
> "known as write-ahead logging, was invented to address exactly this type of problem. In file systems, we usually call write-ahead logging journaling for historical reasons."
>
> *kỹ thuật **write-ahead logging** được phát minh để giải đúng loại vấn đề này. Trong file system, ta thường gọi write-ahead logging là **journaling** vì lý do lịch sử.*

Cơ chế, diễn đạt mộc mạc:

> [!quote] OSTEP (tr. 539)
> "When updating the disk, before overwriting the structures in place, first write down a little note (somewhere else on the disk, in a well-known location) describing what you are about to do. Writing this note is the "write ahead" part, and we write it to a structure that we organize as a "log"; hence, write-ahead logging."
>
> *Khi cập nhật đĩa, **trước khi** ghi đè tại chỗ, hãy **ghi một mẩu ghi chú** (ở nơi khác trên đĩa, vị trí đã biết) mô tả việc mình **sắp** làm. Ghi mẩu đó là phần "**write ahead**" (ghi trước), và ta ghi vào một cấu trúc tổ chức dạng "**log**" — nên gọi là write-ahead logging.*

Vì sao nó cứu được: nếu crash xảy ra giữa chừng, lúc khởi động lại ta **đọc lại ghi chú trong log** và biết chính xác phải hoàn tất (hoặc huỷ) việc gì — khôi phục về trạng thái nhất quán. Đây lại chính là "**all or nothing**" của Bài 2, nhưng chống lại *mất điện* thay vì *context switch*. Một ý tưởng, hai kẻ thù khác nhau.

## 4. Demo: ghi đè tại chỗ vs tmp rồi rename

Không cần giật dây nguồn thật: ta *mô phỏng* crash bằng cách ném lỗi giữa chừng. Kiểu 1 ghi đè **tại chỗ** rồi "crash" → file dở dang, JSON hỏng. Kiểu 2 dùng mẫu userland của journaling: **ghi ra file tạm → `fsync` (ép xuống đĩa) → `rename`** (rename trên POSIX là *atomic*). Crash trước rename thì bản cũ còn nguyên; sau rename thì có bản mới trọn vẹn — không bao giờ có "giữa".

```typescript
// Persistence: ghi đè TẠI CHỖ có thể để lại file dở dang nếu "crash" giữa chừng.
// Cách chữa của userland = họ hàng của journaling (write-ahead): ghi ra file
// tạm → fsync → rename (rename là ATOMIC trên POSIX) → reader thấy "all or
// nothing" (Bài 2): hoặc bản cũ nguyên vẹn, hoặc bản mới trọn vẹn.
import { writeFileSync, readFileSync, renameSync, openSync, fsyncSync, closeSync, mkdtempSync } from "node:fs";
import { join } from "node:path";
import { tmpdir } from "node:os";

const dir = mkdtempSync(join(tmpdir(), "cb_b3_"));
const file = join(dir, "config.json");
const GOOD = JSON.stringify({ version: 1, tier: "basic" });
const NEW = JSON.stringify({ version: 2, tier: "premium" });

function readOrNull(): string | null {
  try { JSON.parse(readFileSync(file, "utf8")); return readFileSync(file, "utf8"); }
  catch { return null; }
}

// --- (1) GHI ĐÈ TẠI CHỖ, "crash" giữa chừng ---
writeFileSync(file, GOOD);                       // trạng thái ban đầu hợp lệ
try {
  // mô phỏng ghi 2 mảnh: cắt file, ghi nửa đầu, rồi "mất điện"
  const fd = openSync(file, "w");                // truncate -> file rỗng ngay
  writeFileSync(fd, NEW.slice(0, 15));           // mới ghi được nửa
  throw new Error("CRASH (mất điện giữa lúc ghi)");
  // closeSync(fd);  // không bao giờ tới đây
} catch (e) {
  // fd rò rỉ như sau một crash thật
}
const after1 = readOrNull();
console.log("(1) Ghi đè TẠI CHỖ rồi crash:");
console.log(`    đọc lại JSON hợp lệ? ${after1 !== null ? "CÓ" : "KHÔNG → file HỎNG"}`);
console.log(`    nội dung thô: ${readFileSync(file, "utf8")!}`);

// --- (2) WRITE-TMP + RENAME (atomic), "crash" trước khi rename ---
writeFileSync(file, GOOD);                       // reset về bản cũ hợp lệ
const tmp = file + ".tmp";
try {
  const fd = openSync(tmp, "w");
  writeFileSync(fd, NEW);                         // ghi TRỌN vào file tạm
  fsyncSync(fd);                                  // ép xuống đĩa (durable)
  closeSync(fd);
  throw new Error("CRASH (mất điện TRƯỚC khi rename)");
  // renameSync(tmp, file);  // bước atomic — chưa kịp chạy
} catch (e) { /* crash */ }
const after2 = readOrNull();
console.log("\n(2) Write-tmp + fsync, crash TRƯỚC rename:");
console.log(`    đọc lại JSON hợp lệ? ${after2 !== null ? "CÓ" : "KHÔNG"}`);
console.log(`    nội dung: ${readFileSync(file, "utf8")}  ← bản CŨ còn nguyên`);

// --- (3) chạy trọn: rename thành công ---
const fd = openSync(tmp, "w");
writeFileSync(fd, NEW); fsyncSync(fd); closeSync(fd);
renameSync(tmp, file);                            // atomic: cũ -> mới, không có giữa
console.log("\n(3) Hoàn tất rename:");
console.log(`    nội dung: ${readFileSync(file, "utf8")}  ← bản MỚI, trọn vẹn`);
console.log("\nGhi đè tại chỗ: có trạng thái DỞ DANG. Tmp+rename: chỉ cũ HOẶC mới.");
```

Kết quả chạy thật *(tất định — chạy lại cho y hệt)*:

```
(1) Ghi đè TẠI CHỖ rồi crash:
    đọc lại JSON hợp lệ? KHÔNG → file HỎNG
    nội dung thô: {"version":2,"t

(2) Write-tmp + fsync, crash TRƯỚC rename:
    đọc lại JSON hợp lệ? CÓ
    nội dung: {"version":1,"tier":"basic"}  ← bản CŨ còn nguyên

(3) Hoàn tất rename:
    nội dung: {"version":2,"tier":"premium"}  ← bản MỚI, trọn vẹn

Ghi đè tại chỗ: có trạng thái DỞ DANG. Tmp+rename: chỉ cũ HOẶC mới.
```

Kiểu (1) để lại `{"version":2,"t` — không phải JSON, không phải bản cũ: **dở dang**, đúng cơn ác mộng crash-consistency ở mục 3. Kiểu (2)/(3) biến một thao tác nhiều-bước thành *một chuyển trạng thái atomic* nhờ `rename`: `fsync` đảm bảo dữ liệu thực sự nằm trên đĩa trước, `rename` chuyển con trỏ tên file trong một nhịp không chia cắt. Đây là journaling thu nhỏ: ghi an toàn ở chỗ khác trước, rồi "chốt" trong một bước không thể vỡ.

> [!note] Tự thử
> - Bỏ dòng `fsync`: trên máy thật, rename có thể "chốt" tên mới trong khi dữ liệu còn kẹt ở cache RAM → crash vẫn mất. `fsync` là mảnh ghép *durability* mà rename *một mình* không cho.
> - In `fs.readdirSync(dir)` sau bước (2): thấy cả `config.json` lẫn `config.json.tmp` — file tạm "mồ côi" sau crash chính là thứ quá trình khôi phục (recovery) phải dọn.
> - Thử ghi đè tại chỗ nhưng nội dung mới **ngắn hơn** cũ rồi crash: bạn được phần đầu mới + phần đuôi cũ dính lại — kiểu hỏng âm thầm còn khó phát hiện hơn.

## 5. Bảng so sánh: ba tầng bảo đảm durability

"Lưu bền" không phải một công tắc mà là nhiều tầng, mỗi tầng chống một kiểu mất mát khác nhau:

| Tầng                     | Chống được gì                             | Cơ chế                                   | Nền / AWS tương ứng                       |
| :----------------------- | :---------------------------------------- | :--------------------------------------- | :---------------------------------------- |
| **fsync (ép xuống đĩa)** | mất dữ liệu còn kẹt ở cache RAM khi crash | buộc ghi từ page cache xuống thiết bị    | `fsync`; EBS flush; commit của DB         |
| **Atomic (tmp+rename / journaling)** | trạng thái DỞ DANG sau crash giữa chừng | ghi an toàn chỗ khác trước, rồi chốt 1 nhịp | journaling FS; **S3 PUT** atomic; WAL của DB |
| **Nhân bản (replication)** | hỏng **cả ổ đĩa / cả máy / cả AZ**       | giữ nhiều bản trên nhiều thiết bị/vùng   | RAID; **S3 11 nines**; Multi-AZ (Bài 8)   |

Thang leo dần: `fsync` cứu khi *mất điện*, atomic cứu khi *crash giữa chừng*, nhưng cả hai **bó tay** khi chính cái ổ đĩa chết. Muốn chống mất phần cứng phải lên tầng **nhân bản** — và đó chính là cánh cửa dẫn sang trụ Distributed (Bài 7–8): một khi dữ liệu nằm trên *nhiều máy*, mọi bài toán cũ (atomicity, nhất quán) tái sinh ở quy mô mạng.

## 6. Nối về AWS

> [!note] Nối về AWS
> Độ bền (durability) là lời hứa trung tâm của mọi dịch vụ **lưu trữ** AWS — xem [`aws-fund` Bài 3 — Database & Storage](../../aws-fund/bai_hoc/bai_03_database-storage.md):
> - **S3 "11 nines" (99.999999999%)** không phải phép màu — nó là **tầng 3 (nhân bản)** của bảng mục 5 đẩy tới cực hạn: mỗi object được sao thành nhiều bản trên nhiều thiết bị/nhiều AZ. S3 chịu nổi mất cả một trung tâm dữ liệu đúng vì lý do "fsync + atomic bó tay khi ổ đĩa chết".
> - **S3 PUT là atomic**: người đọc hoặc thấy object cũ, hoặc thấy object mới trọn vẹn — *không bao giờ* thấy nửa file. Đây đúng là "tmp + rename / all or nothing" của mục 4–5, nâng lên mức dịch vụ.
> - **Write-ahead log** mà OSTEP bảo "ăn cắp từ database" (tr. 539) hôm nay chạy *ngược về* database: **Aurora** đẩy chính cái WAL qua mạng tới tầng lưu trữ chia sẻ; **DynamoDB** ghi vào log trước khi áp dụng. Khi bạn thấy "commit" trả về, nghĩa là WAL đã durable — y hệt `fsync` ở mục 5.
> - Vì sao **EBS** khác **instance store**: instance store là đĩa cục bộ (mất khi instance dừng — như RAM volatile ở mức máy); EBS là volume *nhân bản*, sống sót qua vòng đời instance. Chọn sai = mất dữ liệu đúng kiểu "DRAM volatile" mục 1, chỉ to hơn.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 3.1 — Vì sao RAM không đủ để "lưu dữ liệu"? Một từ khoá.
> **Đáp:** **volatile (bay hơi)** — DRAM mất sạch khi mất điện/crash. Cần thiết bị lưu bền (đĩa/SSD) + file system quản lý.

> [!question] Thẻ 3.2 — OS ảo hoá CPU/bộ nhớ "riêng tư" cho mỗi process; với đĩa thì sao? Vì sao?
> **Đáp:** **không** dựng đĩa ảo riêng — file sinh ra để **chia sẻ** (editor ghi, trình biên dịch đọc). File system là không gian chung.

> [!question] Thẻ 3.3 — "Crash consistency problem" là gì?
> **Đáp:** làm sao cập nhật cấu trúc dữ liệu bền khi crash/mất điện có thể rơi **giữa chừng** một thao tác nhiều-bước, để lại trạng thái nửa cũ nửa mới (hỏng).

> [!question] Thẻ 3.4 — Write-ahead logging (journaling) hoạt động ra sao? Nối với khái niệm Bài 2 nào?
> **Đáp:** trước khi ghi đè tại chỗ, **ghi một ghi chú vào log** mô tả việc sắp làm; crash thì đọc log để hoàn tất/huỷ → nhất quán. Chính là "**all or nothing**" (atomicity, Bài 2) chống *mất điện*.

> [!question] Thẻ 3.5 — Mẫu "tmp + fsync + rename" cho gì mà ghi đè tại chỗ không có?
> **Đáp:** `fsync` = durability (ép xuống đĩa thật); `rename` atomic = reader chỉ thấy cũ HOẶC mới, không có dở dang.

> [!question] Thẻ 3.6 — "S3 11 nines" tương ứng tầng durability nào? Vì sao fsync/atomic không đủ?
> **Đáp:** tầng **nhân bản (replication)** — nhiều bản trên nhiều AZ. fsync/atomic chỉ cứu crash/mất điện trên *một* ổ; ổ/máy/AZ chết thì phải có bản khác.

## 8. Câu hỏi tự kiểm tra

1. Vì sao lưu trữ bền *khó*? Nêu hai lý do gốc. *(mục 1, tr. 7)*
2. Điều gì OS **không** ảo hoá riêng tư, khác với CPU/bộ nhớ? Vì sao? *(mục 2)*
3. Phát biểu crash-consistency problem. Cho một ví dụ thao tác nhiều-bước. *(mục 3, tr. 533)*
4. Giải thích write-ahead logging. Vì sao nó cứu được crash giữa chừng? Nối với "all or nothing" ra sao? *(mục 3, tr. 539)*
5. Chạy demo mục 4. Vì sao kiểu (1) ra JSON hỏng còn (2) giữ được bản cũ? Vai trò của `fsync` và `rename`? *(mục 4)*
6. Ba tầng durability chống ba loại mất mát nào? "S3 11 nines" và "S3 PUT atomic" ứng tầng nào? *(mục 5–6)*

## Tóm tắt một trang

```
BÀI 3 — OS TRỤ 1c: LƯU TRỮ BỀN (file system · crash · journaling)
─────────────────────────────────────────────────────────
VÌ SAO KHÓ  RAM VOLATILE (mất điện = mất sạch); đĩa CHẬM hơn RAM ngàn-
   triệu lần; CRASH rơi bất kỳ lúc nào, kể cả giữa lúc ghi.

FILE SYSTEM  phần mềm quản đĩa, lưu file tin cậy+hiệu quả.
   Khác CPU/bộ nhớ: KHÔNG ảo hoá đĩa riêng — file sinh ra để CHIA SẺ.

CRASH CONSISTENCY  cập nhật nhiều-bước + crash giữa chừng = nửa cũ nửa
   mới = HỎNG (tr.533).
JOURNALING = WRITE-AHEAD LOGGING (tr.539, "ăn cắp từ database"):
   ghi NOTE vào log TRƯỚC khi ghi đè → crash thì đọc log khôi phục.
   = "all or nothing" (Bài 2) chống MẤT ĐIỆN.

DEMO  ghi đè tại chỗ + crash → {"version":2,"t  (JSON hỏng).
   tmp+fsync+rename + crash → bản cũ nguyên; rename xong → bản mới trọn.

3 TẦNG DURABILITY  fsync (cache→đĩa) · atomic/journaling (chống dở dang)
   · replication (chống chết ổ/máy/AZ).

NỐI VỀ AWS  S3 11 nines = replication cực hạn; S3 PUT atomic = tmp+rename;
   Aurora/DynamoDB = WAL durable khi "commit"; EBS nhân bản vs instance
   store volatile.
```

## Nguồn

- **Remzi H. & Andrea C. Arpaci-Dusseau**, *Operating Systems: Three Easy Pieces* — **chương 2 §2.4 (Persistence)**: DRAM volatile, định nghĩa file system (tr. 7); **chương 42 (Crash Consistency: FSCK and Journaling)**: crash-consistency problem (tr. 533), write-ahead logging = journaling (tr. 539). `tai_lieu/Operating systems three easy pieces.pdf` — **offset PDF = tr. + 25**.
- Nối về AWS: [`aws-fund` Bài 3 — Database & Storage](../../aws-fund/bai_hoc/bai_03_database-storage.md) (S3 durability, EBS, WAL của Aurora/DynamoDB).
- Khép lại trụ 1 (OS). Tiếp trụ 2 (Mạng): [Bài 4 — phân tầng, HTTP, DNS](bai_04_mang-http-dns.md). "Nhân bản" (tầng 3 durability) sẽ trở lại ở [Bài 8 — nhất quán](bai_08_dist-nhat-quan.md).

---

**Bản đồ khoá học — lõi:** [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md) · [Bài 1 — OS: ảo hoá](bai_01_os-ao-hoa.md) · [Bài 2 — OS: concurrency](bai_02_os-concurrency.md) · **[Bài 3 — OS: lưu trữ] ← bạn đang ở đây** · [Bài 4 — Mạng: phân tầng, HTTP, DNS](bai_04_mang-http-dns.md) · [Bài 5 — Mạng: TCP, TLS](bai_05_mang-tcp-tls.md) · [Bài 6 — Mạng: hiệu năng, CDN](bai_06_mang-hieu-nang.md) · [Bài 7 — Distributed: giao tiếp & thất bại](bai_07_dist-giao-tiep.md) · [Bài 8 — Distributed: nhân bản & nhất quán](bai_08_dist-nhat-quan.md) · [Bài 9 — Distributed: phân mảnh & consensus](bai_09_dist-phan-manh.md) · [Bài 10 — Dữ liệu: storage engine](bai_10_du-lieu-storage.md) · [Bài 11 — Dữ liệu: batch & stream](bai_11_du-lieu-batch-stream.md)

**Chuyên đề nâng cao:** [Bài 12 — OS nâng cao: bộ nhớ ảo](bai_12_os-bo-nho-ao.md) · [Bài 13 — OS nâng cao: scheduling & locks](bai_13_os-scheduling-locks.md) · [Bài 14 — Mạng nâng cao: bảo mật & mật mã](bai_14_mang-bao-mat.md) · [Bài 15 — Distributed nâng cao: đồng hồ](bai_15_dist-dong-ho.md) · [Bài 16 — Distributed nâng cao: transaction & saga](bai_16_dist-transaction-saga.md) · [Bài 17 — Dữ liệu nâng cao: data models](bai_17_du-lieu-data-models.md) · [Bài 18 — Dữ liệu nâng cao: encoding & schema](bai_18_du-lieu-encoding.md)

Xem thêm [README khoá học](../README.md).
