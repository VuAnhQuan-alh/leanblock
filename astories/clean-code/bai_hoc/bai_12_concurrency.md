# Bài 12 — Concurrency: tách "cái gì" khỏi "khi nào"

> [!info] Về bài này
> Dựng từ **Chương 13 — "Concurrency"** (tác giả Brett L. Schuchert) của *Clean Code* (Robert C. Martin, 2008 — `tai_lieu/`, `tr. 177–190`), có gập tinh tuý **Phụ lục A — "Concurrency II"** (`tr. 317+`) vào mục Mở rộng.
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 31`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Mạch bài: *race condition → gọi tên vấn đề → bản sạch (TypeScript, chạy được) → nguyên tắc → đối chiếu 2026 → áp dụng*.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: vì sao concurrency khó](#1-mở-đầu-vì-sao-concurrency-khó)
2. [Vì sao vẫn cần: tách cái gì khỏi khi nào](#2-vì-sao-vẫn-cần-tách-cái-gì-khỏi-khi-nào)
3. [Những lầm tưởng, và một dòng code 12.870 lối chạy](#3-những-lầm-tưởng-và-một-dòng-code-12870-lối-chạy)
4. [Code minh hoạ: một race condition và cách tránh](#4-code-minh-hoạ-một-race-condition-và-cách-tránh)
5. [Nguyên tắc phòng thủ concurrency](#5-nguyên-tắc-phòng-thủ-concurrency)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào codebase của bạn](#7-áp-dụng-vào-codebase-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mở đầu: vì sao concurrency khó

> [!quote] Ch. 13 — Concurrency (tr. 177)
> "Objects are abstractions of processing. Threads are abstractions of schedule."
>
> *Object là trừu tượng của **xử lý**. Thread là trừu tượng của **lịch trình**. (James O. Coplien)*

> [!quote] Ch. 13 — Concurrency (tr. 178)
> "Writing clean concurrent programs is hard—very hard."
>
> *Viết chương trình đồng thời cho sạch thì khó — rất khó.*

Code đa luồng dễ *trông* ổn trên bề mặt mà hỏng ở tầng sâu, chỉ lộ ra khi hệ thống chịu tải. Chương này là bản tổng quan; chi tiết nằm ở Phụ lục A.

## 2. Vì sao vẫn cần: tách cái gì khỏi khi nào

> [!quote] Ch. 13 — Why Concurrency? (tr. 178)
> "Concurrency is a decoupling strategy. It helps us decouple what gets done from when it gets done."
>
> *Concurrency là một chiến lược **tháo ghép**. Nó giúp ta tách **cái gì** được làm khỏi **khi nào** nó được làm.*

Trong ứng dụng đơn luồng, "cái gì" và "khi nào" dính chặt tới mức nhìn stack là biết trạng thái. Tách chúng ra giúp tăng cả thông lượng (throughput) lẫn cấu trúc: hệ thống trông như nhiều máy nhỏ cộng tác thay vì một vòng lặp lớn. Ví dụ thực tế: thu thập dữ liệu từ nhiều web — bản đơn luồng hứng I/O tuần tự, càng nhiều site càng chậm; bản đa luồng hứng nhiều site cùng lúc.

## 3. Những lầm tưởng, và một dòng code 12.870 lối chạy

Vài lầm tưởng chương bác bỏ: "concurrency luôn tăng hiệu năng" (chỉ khi có nhiều *thời gian chờ* để chia), "thiết kế không đổi khi viết đa luồng", "dùng container (Web/EJB) thì khỏi cần hiểu concurrency". Và minh hoạ kinh điển — một dòng `return ++lastIdUsed` tưởng vô hại:

> [!quote] Ch. 13 — Challenges (tr. 180)
> "there are 12,870 different possible execution paths […] If the type of lastIdUsed is changed from int to long, the number of possible paths increases to 2,704,156."
>
> *có **12.870** lối chạy khả dĩ khác nhau [cho hai thread cùng chạy trong `getNextId`]. Nếu đổi kiểu `lastIdUsed` từ `int` sang `long`, số lối chạy tăng lên **2.704.156**.*

Hai thread cùng gọi `getNextId()` có thể cho kết quả đúng (43/44) hoặc **sai** (cả hai cùng 43) — vì chúng "giẫm lên nhau" ở một dòng duy nhất.

## 4. Code minh hoạ: một race condition và cách tránh

JavaScript/Node chạy **đơn luồng** trên event loop, nên không có race kiểu `++` của Java. Nhưng race *logic* vẫn xảy ra khi có điểm **nhường** (`await`) nằm giữa lúc *đọc* và lúc *ghi* một state chia sẻ — hai tác vụ async chen vào nhau:

```typescript
import { strict as assert } from "node:assert";

function delay(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

// ===== Bản DỄ DÍNH RACE: đọc balance, nhường (await), rồi ghi =====
let sharedBalance = 100;
async function withdrawRacy(amount: number): Promise<void> {
  const current = sharedBalance; // đọc
  await delay(10); // điểm NHƯỜNG: task khác chen vào giữa đọc và ghi
  sharedBalance = current - amount; // ghi dựa trên giá trị đã CŨ
}

// ===== Bản AN TOÀN: đọc-ghi liền mạch, không await xen giữa =====
let safeBalance = 100;
function withdrawSafe(amount: number): void {
  safeBalance = safeBalance - amount;
}

async function main(): Promise<void> {
  await Promise.all([withdrawRacy(30), withdrawRacy(30)]); // hai lần rút 30 "song song"
  withdrawSafe(30);
  withdrawSafe(30);

  console.log("số dư bản RACY:", sharedBalance, "(mong đợi 40)");
  console.log("số dư bản SAFE:", safeBalance, "(mong đợi 40)");
  assert.equal(safeBalance, 40);
  console.log("bản racy MẤT một lần rút vì đọc-await-ghi trên state chia sẻ.");
}

main();
```

Kết quả chạy thật:

```
số dư bản RACY: 70 (mong đợi 40)
số dư bản SAFE: 40 (mong đợi 40)
bản racy MẤT một lần rút vì đọc-await-ghi trên state chia sẻ.
```

Cả hai `withdrawRacy` đọc `sharedBalance = 100`, cùng `await`, rồi cùng ghi `100 - 30 = 70` — **một lần rút biến mất**. Đây đúng "kết quả bất ngờ thứ ba" của sách, dịch sang thế giới async đơn luồng. Bản `withdrawSafe` đọc-ghi liền mạch (không `await` xen giữa) nên đúng. Bài học: *giữ phần đọc-sửa-ghi trên state chia sẻ càng gọn và càng tách biệt càng tốt* — đúng tinh thần các nguyên tắc dưới đây.

> [!note] Tự thử
> 1. Trong `withdrawRacy`, chuyển dòng `await delay(10)` xuống *sau* dòng ghi. Chạy lại: còn mất tiền không? Vì sao?
> 2. Đổi `Promise.all` thành chạy *tuần tự* (`await withdrawRacy(30); await withdrawRacy(30);`). Kết quả là bao nhiêu? Tuần tự hoá có phải một cách "sửa" không — và nó đánh đổi cái gì?
> 3. Thêm một `withdrawRacy(30)` thứ ba vào `Promise.all`. Số dư racy giờ là bao nhiêu? (Gợi ý: vẫn 70 — vì sao?)

## 5. Nguyên tắc phòng thủ concurrency

Chương đưa một loạt nguyên tắc; cốt lõi:

> [!quote] Ch. 13 — Single Responsibility Principle (tr. 181)
> "Keep your concurrency-related code separate from other code."
>
> *Hãy giữ code liên quan đến concurrency **tách biệt** khỏi code khác.*

Vì code concurrency có vòng đời, thách thức và cách hỏng riêng. Các hệ quả kèm theo:

- **Giới hạn phạm vi dữ liệu** (*limit scope of data*): càng nhiều nơi state chia sẻ bị sửa, càng dễ quên bảo vệ một chỗ → "nhận lấy việc đóng gói dữ liệu vào tim; hạn chế gắt gao mọi truy cập tới dữ liệu có thể bị chia sẻ".
- **Dùng bản sao dữ liệu** (*use copies of data*): tránh chia sẻ ngay từ đầu — copy, xử lý read-only, rồi gộp kết quả ở một luồng.
- **Thread càng độc lập càng tốt**: mỗi luồng sống trong thế giới riêng, dữ liệu từ nguồn không chia sẻ, lưu trong biến cục bộ.
- **Hiểu thư viện của bạn**: dùng collection thread-safe, executor framework, giải pháp non-blocking.

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Đây là **chương lỗi thời về công nghệ nhiều nhất** của phần "code sạch" — nó viết cho mô hình *shared-memory threading* của Java 2008 (`synchronized`, `java.util.concurrent`). Nguyên tắc tư duy thì còn, nhưng thế giới đã đổi mô hình.
> - **Mô hình đã dịch chuyển khỏi shared-memory threading.** Năm 2026, nhiều hệ dùng: **async/await + event loop** (JS/Node, Python asyncio — đơn luồng, không race kiểu `++` nhưng *có* race logic như mục 4); **message passing / actor** (Erlang/Elixir, Akka — "đừng chia sẻ bộ nhớ, hãy truyền thông điệp"); **CSP channel** (Go goroutine + channel); **ownership** (Rust — trình biên dịch *chặn* data race ngay khi biên dịch, điều Java 2008 không mơ tới). Lời khuyên "đừng chia sẻ, dùng bản sao, giữ luồng độc lập" của sách chính là *tiên đoán* các mô hình này.
> - **"Giữ concurrency tách biệt" + "giới hạn chia sẻ"**: còn nguyên giá trị, và là triết lý nền của Go ("share memory by communicating") và Rust (ownership). Đây là phần *bất tử* của chương.
> - **"12.870 lối chạy"**: minh hoạ vẫn đắt về mặt trực giác — số tổ hợp interleaving bùng nổ — dù con số cụ thể là của bytecode Java.
> - **Mới sau 2008**: structured concurrency (nursery/scope, Java 21 `StructuredTaskScope`, Kotlin coroutine scope), và với Node — **worker_threads** + `SharedArrayBuffer`/`Atomics` cho đa luồng thật khi cần CPU-bound.
> - **Test code đồng thời**: sách khuyến nghị chạy lặp nhiều lần, "shake" bằng cách chèn delay ngẫu nhiên. Năm 2026 còn có công cụ chuyên dụng (`tsan`, deterministic simulation testing như của FoundationDB) — nhưng tinh thần "bug concurrency không lặp lại nên đừng bỏ qua như one-off" vẫn vàng.

## 7. Áp dụng vào codebase của bạn

> [!question] Áp dụng vào codebase của bạn
> 1. **Săn một điểm nhường nguy hiểm.** Trong code async của bạn, tìm một chỗ *đọc* state chia sẻ → `await` → *ghi* lại dựa trên giá trị đã đọc. Đó là một race logic chờ sẵn (như mục 4).
> 2. **Đo phạm vi chia sẻ.** Liệt kê các biến/state được nhiều tác vụ đồng thời đụng tới. Mỗi cái là một nguồn rủi ro — có thể thu hẹp, copy, hay làm bất biến không?
> 3. **Xác định mô hình của bạn.** Dự án dùng mô hình nào: event-loop async, worker/actor, goroutine, hay thread chia sẻ bộ nhớ? Lời khuyên "giữ luồng độc lập" áp vào mô hình đó ra sao?
> 4. **Làm bất biến.** Chọn một object bị chia sẻ-và-sửa. Thử làm nó *read-only* (copy khi cần đổi). Rủi ro race có giảm không?

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Concurrency = decoupling** | Tách *cái gì* được làm khỏi *khi nào* được làm (tr. 178). |
| **Race condition** | Nhiều luồng/tác vụ "giẫm lên nhau" khi đọc-ghi state chia sẻ, cho kết quả sai (tr. 180). |
| **Limit scope of data** | Hạn chế gắt gao nơi state chia sẻ bị sửa; đóng gói dữ liệu (tr. 181). |
| **Use copies of data** | Tránh chia sẻ bằng cách copy, xử lý read-only rồi gộp (tr. 182). |
| **Threads independent** | Mỗi luồng tự chứa, dữ liệu cục bộ, không chia sẻ (tr. 182). |
| **Deadlock / Starvation** | Hai luồng chờ nhau mãi / một luồng bị cấm tiến mãi (tr. 183). |
| **Actor / CSP / ownership** | (2026) Các mô hình thay cho shared-memory threading: message passing, channel, Rust ownership. |

## 9. Câu hỏi tự kiểm tra

1. "Concurrency là chiến lược tháo ghép" nghĩa là gì? Tách cái gì khỏi cái gì? *(tr. 178)*
2. Nêu hai lầm tưởng về concurrency mà chương bác bỏ. *(tr. 179–180)*
3. Vì sao một dòng `return ++lastIdUsed` lại có hàng nghìn lối chạy? *(tr. 180)*
4. Ba hệ quả của việc "giới hạn phạm vi dữ liệu" và "dùng bản sao" là gì? *(tr. 181–182)*
5. Năm 2026, những mô hình nào đã thay cho shared-memory threading, và chúng hiện thực lời khuyên nào của chương? *(Đối chiếu 2026)*

## Tóm tắt một trang

```
BÀI 12 — CONCURRENCY: TÁCH "CÁI GÌ" KHỎI "KHI NÀO"
─────────────────────────────────────────────────────────
"viết concurrency sạch thì KHÓ — rất khó" (tr.178).
Concurrency = tháo ghép: tách CÁI GÌ khỏi KHI NÀO (tr.178).

LẦM TƯỞNG  "luôn tăng hiệu năng" · "thiết kế không đổi" ·
           "dùng container thì khỏi hiểu" — đều SAI.
1 DÒNG     return ++lastIdUsed → 12.870 lối chạy (tr.180).

RACE (demo async): đọc balance → await → ghi giá trị cũ →
     hai lần rút 30 từ 100 còn 70 (mất 1 lần). Fix: đọc-ghi liền.

PHÒNG THỦ  giữ code concurrency TÁCH BIỆT (tr.181); giới hạn
           phạm vi chia sẻ; dùng bản sao; luồng độc lập; hiểu thư viện.

2026  mô hình đổi: async/event-loop, actor/message-passing (Elixir),
      CSP channel (Go), ownership chặn-lúc-biên-dịch (Rust),
      structured concurrency. "Đừng chia sẻ bộ nhớ" = phần bất tử.
```

## Nguồn

- **Robert C. Martin**, *Clean Code* (Prentice Hall, 2008) — **Chương 13, "Concurrency"** (Brett L. Schuchert) (`tr. 177–190`): epigraph Coplien (tr. 177); "rất khó", tổng quan (tr. 178); vì sao concurrency, tách cái-gì/khi-nào (tr. 178–179); lầm tưởng (tr. 179–180); thách thức, lớp `X`, 12.870 lối chạy (tr. 180); nguyên tắc phòng thủ — SRP, giới hạn phạm vi, bản sao, luồng độc lập (tr. 181–182); hiểu thư viện, mô hình thực thi, deadlock/starvation (tr. 182–190). Gập tinh tuý **Phụ lục A — "Concurrency II"** (`tr. 317+`): possible paths of execution, producer-consumer, readers-writers, dining philosophers.`tai_lieu/Clean.Code.2008.8.pdf`
- Bổ sung 2026 dẫn từ ngoài sách: actor model (Erlang/Elixir/Akka); CSP (Go channel); Rust ownership & borrow checker; structured concurrency (Java 21 `StructuredTaskScope`, Kotlin); Node `worker_threads`/`Atomics`.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 31`.

---

**Bản đồ khoá học:** [Bài 0 — Clean Code là gì](bai_00_clean_code_la_gi.md) · [Bài 1 — Đặt tên](bai_01_dat_ten.md) · [Bài 2 — Hàm](bai_02_ham.md) · [Bài 3 — Comment](bai_03_comment.md) · [Bài 4 — Định dạng](bai_04_dinh_dang.md) · [Bài 5 — Object & dữ liệu](bai_05_object_va_du_lieu.md) · [Bài 6 — Xử lý lỗi](bai_06_xu_ly_loi.md) · [Bài 7 — Ranh giới](bai_07_ranh_gioi.md) · [Bài 8 — Unit test](bai_08_unit_test.md) · [Bài 9 — Class](bai_09_class.md) · [Bài 10 — Hệ thống](bai_10_he_thong.md) · [Bài 11 — Thiết kế nổi lên](bai_11_thiet_ke_noi_len.md) · [Bài 12 ← bạn đang ở đây] · [Bài 13 — Xem code sạch nảy sinh](bai_13_xem_code_nay_sinh.md) · [Bài 14 — Refactor ngoài đời](bai_14_refactor_ngoai_doi.md) · [Bài 15 — Danh mục mùi code](bai_15_danh_muc_mui_code.md)

Xem thêm [README khoá học](../README.md).
