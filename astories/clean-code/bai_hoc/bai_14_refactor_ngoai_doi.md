# Bài 14 — Refactor ngoài đời: đọc code người khác, gột cho sạch

> [!info] Về bài này
> Chưng cất từ **Chương 15 — "JUnit Internals"** (`tr. 251–265`) và **Chương 16 — "Refactoring SerialDate"** (`tr. 267–284`) của *Clean Code* (Robert C. Martin, 2008 — `tai_lieu/`).
> Hai chương này mổ *code Java có thật của người khác* (ruột JUnit, lớp `SerialDate` của thư viện JCommon). Khoá này **không port Java nguyên văn** — mà rút lấy *bài học refactor ngoài đời*: đọc code người, phê bình chuyên nghiệp, bọc test rồi gột dần.
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 31`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: hai chương mổ code của người khác](#1-mở-đầu-hai-chương-mổ-code-của-người-khác)
2. [Phê bình là việc chuyên nghiệp, không phải công kích](#2-phê-bình-là-việc-chuyên-nghiệp-không-phải-công-kích)
3. [First, make it work: bọc test trước đã](#3-first-make-it-work-bọc-test-trước-đã)
4. [Code minh hoạ: ghim hành vi rồi refactor an toàn](#4-code-minh-hoạ-ghim-hành-vi-rồi-refactor-an-toàn)
5. [Refactor là thử-và-sai, và luôn để lại sạch hơn](#5-refactor-là-thử-và-sai-và-luôn-để-lại-sạch-hơn)
6. [Đối chiếu 2026](#6-đối-chiếu-2026)
7. [Áp dụng vào codebase của bạn](#7-áp-dụng-vào-codebase-của-bạn)
8. [Từ điển thuật ngữ](#8-từ-điển-thuật-ngữ)
9. [Câu hỏi tự kiểm tra](#9-câu-hỏi-tự-kiểm-tra)
10. [Tóm tắt một trang](#tóm-tắt-một-trang)
11. [Nguồn](#nguồn)

---

## 1. Mở đầu: hai chương mổ code của người khác

Hai chương 15 và 16 khác mọi chương trước: chúng không dạy nguyên tắc, mà **thực hành** phê bình và refactor trên *code thật của người khác*. Chương 15 mổ `ComparisonCompactor` — đoạn code trong JUnit giúp chỉ ra khác biệt giữa hai chuỗi.

> [!quote] Ch. 15 — JUnit Internals (tr. 251)
> "In this chapter we'll critique an example drawn from the JUnit framework."
>
> *Trong chương này, ta sẽ phê bình một ví dụ lấy từ framework JUnit.*

Chương 16 mổ lớp `SerialDate` của David Gilbert trong thư viện JCommon. Cả hai là bài học *refactor ngoài đời* — khác hẳn [Bài 13](bai_13_xem_code_nay_sinh.md) (nơi Uncle Bob refactor code *của chính mình*).

## 2. Phê bình là việc chuyên nghiệp, không phải công kích

Uncle Bob mở Chương 16 bằng một tuyên bố gai góc — rồi lập tức làm rõ tinh thần:

> [!quote] Ch. 16 — Refactoring SerialDate (tr. 267)
> "For all intents and purposes, this is 'good code.' And I am going to rip it to pieces."
>
> *Xét mọi mặt, đây là "code tốt". Và tôi sắp **xé nó ra từng mảnh**.*

Nghe như công kích, nhưng không:

> [!quote] Ch. 16 — Refactoring SerialDate (tr. 268)
> "What I am about to do is nothing more and nothing less than a professional review. It is something that we should all be comfortable doing. And it is something we should welcome when it is done for us."
>
> *Điều tôi sắp làm chẳng gì hơn và chẳng gì kém một **cuộc review chuyên nghiệp**. Đó là việc tất cả chúng ta nên thấy thoải mái khi làm. Và là việc ta nên **hoan nghênh** khi người khác làm cho mình.*

Bác sĩ phê bình nhau, phi công, luật sư cũng vậy — lập trình viên cũng cần học cách ấy. Gilbert còn đáng trọng vì đã *can đảm* mở code cho cộng đồng soi xét. (Chủ đề này nối thẳng với khoá *Clean Coder* — [Bài 12 (Cộng tác)](../../clean-coder/bai_hoc/bai_12_cong_tac.md) nếu bạn học cả hai.)

## 3. First, make it work: bọc test trước đã

Trước khi refactor một lớp mình chưa hiểu hết, Uncle Bob làm điều đầu tiên: **đo và bổ sung test**. Với `SerialDate`, công cụ Clover cho thấy test cũ chỉ phủ ~50% (91/185 câu lệnh) — một "tấm chăn vá". Ông *viết hẳn một bộ test độc lập* phủ kín hơn **trước khi** đụng vào cấu trúc. Đây chính là bài học cốt lõi của refactor ngoài đời: bạn không thể refactor an toàn cái mà bạn không có lưới test đỡ bên dưới. (Nối [Bài 8 (Unit test)](bai_08_unit_test.md) và quy tắc 1 ở [Bài 11](bai_11_thiet_ke_noi_len.md).)

## 4. Code minh hoạ: ghim hành vi rồi refactor an toàn

Khi code cũ *không* có đủ test, kỹ thuật thực dụng là **characterization test** (test đặc tả hành vi, còn gọi "golden master"): chụp lại cái mà code *đang* làm — chưa cần biết nó "đúng" hay "sai" — rồi refactor sao cho hành vi không đổi.

```typescript
import { strict as assert } from "node:assert";

// ===== Code "ngoài đời": khó hiểu, không ai dám đụng =====
// (phí ship theo cân nặng w + vùng z, viết rối)
function legacyShipping(w: number, z: string): number {
  let r = 0;
  if (z == "A") { r = w <= 1 ? 5 : 5 + (w - 1) * 2; }
  else { if (w <= 1) r = 8; else r = 8 + Math.ceil(w - 1) * 3; }
  return r;
}

// ===== Bước 1: GHIM hành vi hiện tại bằng characterization test =====
// (chưa chắc nó "đúng", chỉ chụp lại nó ĐANG làm gì)
const cases: Array<[number, string]> = [
  [0.5, "A"], [1, "A"], [2.5, "A"], [0.5, "B"], [1, "B"], [2.5, "B"],
];
const golden = cases.map(([w, z]) => legacyShipping(w, z));

// ===== Bước 2: refactor sang bản sạch, GIỮ hành vi =====
const BASE: Record<string, number> = { A: 5, B: 8 };
const PER_KG: Record<string, number> = { A: 2, B: 3 };
function shippingFee(weightKg: number, zone: string): number {
  const base = BASE[zone] ?? 8;
  const perKg = PER_KG[zone] ?? 3;
  if (weightKg <= 1) return base;
  const extraKg = zone === "A" ? weightKg - 1 : Math.ceil(weightKg - 1);
  return base + extraKg * perKg;
}

// ===== Bước 3: bản sạch phải khớp MỌI golden =====
cases.forEach(([w, z], i) => {
  assert.equal(shippingFee(w, z), golden[i]);
  console.log(`w=${w} zone=${z}: legacy=${golden[i]}  clean=${shippingFee(w, z)}`);
});
console.log("bản sạch khớp mọi hành vi đã ghim — refactor an toàn vì có test bọc.");
```

Kết quả chạy thật:

```
w=0.5 zone=A: legacy=5  clean=5
w=1 zone=A: legacy=5  clean=5
w=2.5 zone=A: legacy=8  clean=8
w=0.5 zone=B: legacy=8  clean=8
w=1 zone=B: legacy=8  clean=8
w=2.5 zone=B: legacy=14  clean=14
bản sạch khớp mọi hành vi đã ghim — refactor an toàn vì có test bọc.
```

`legacyShipping` dùng `==` lỏng, biến một chữ, logic lồng — khó đọc. Nhưng ta **không sửa mò**: trước hết ghim 6 hành vi của nó vào `golden`, rồi viết `shippingFee` sạch (bảng `BASE`/`PER_KG`, điều kiện rõ), rồi chứng minh bản sạch khớp *mọi* hành vi đã ghim. Nếu bản sạch lệch một ca, `assert` đỏ ngay — đó là cái lưới cho phép bạn gột code lạ mà không sợ phá ngầm.

> [!note] Tự thử
> 1. Sửa `shippingFee` cho zone A cũng dùng `Math.ceil(weightKg - 1)`. Characterization test có đỏ không? Vì sao? (Đây là lúc bạn phát hiện bản sạch *vô tình đổi* hành vi.)
> 2. Thêm ca `[3, "C"]` vào `cases`. Hai bản có khớp nhau cho vùng lạ "C" không? Golden ghim cái gì?
> 3. Giả sử bạn *muốn* sửa một hành vi (vùng A cũng làm tròn lên). Characterization test cũ cản bạn — bạn nên làm gì với test đó, và theo thứ tự nào?

## 5. Refactor là thử-và-sai, và luôn để lại sạch hơn

Một điều trung thực mà chương thừa nhận: refactor không đi thẳng.

> [!quote] Ch. 15 — Conclusion (tr. 265)
> "Refactoring is an iterative process full of trial and error, inevitably converging on something that we feel is worthy of a professional."
>
> *Refactor là một quá trình lặp đầy thử-và-sai, rốt cuộc hội tụ về một thứ mà ta thấy xứng đáng với một người chuyên nghiệp.*

Uncle Bob kể ông đã *đảo ngược* vài quyết định refactor trước đó — inline lại những method vừa tách — "thường một lần refactor dẫn tới lần sau, rồi lần sau lại hoàn tác lần đầu". Và cả hai chương đều khép lại bằng cùng một quy tắc — **Boy Scout Rule** ([Bài 0](bai_00_clean_code_la_gi.md)):

> [!quote] Ch. 16 — Conclusion (tr. 284)
> "So once again we've followed the Boy Scout Rule. We've checked the code in a bit cleaner than when we checked it out."
>
> *Vậy một lần nữa ta theo Quy tắc Hướng đạo sinh. Ta check-in code sạch hơn một chút so với lúc check-out.*

Không module nào miễn nhiễm với việc cải thiện; mỗi người có trách nhiệm để code lại sạch hơn lúc mình chạm vào.

## 6. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Phương pháp của hai chương này **bất tử**, nhưng chúng cũng là nơi lời phê bình nổi tiếng nhất về chính *Clean Code* bắt nguồn.
> - **Chính "clean code" có thể bị đẩy quá đà — và ví dụ của sách là bằng chứng.** Đoạn `SetupTeardownIncluder` (kết quả refactor `testableHtml` ở [Bài 2](bai_02_ham.md)) thường bị cộng đồng 2026 lấy làm *ví dụ ngược*: tách thành quá nhiều method tí hon khiến phải nhảy qua chục hàm mới hiểu một việc — "shallow modules" theo **John Ousterhout**. Bài học kép: refactor để *giảm* tải nhận thức, không phải để đạt chỉ tiêu "hàm nhỏ"; nếu bản "sạch" khó theo hơn bản gốc, bạn đã đi quá xa.
> - **Characterization test — chuẩn vàng 2026 cho legacy**, chính là kỹ thuật trung tâm của Michael Feathers (*Working Effectively with Legacy Code*). Năm 2026 có thêm **approval/snapshot testing** (thư viện như `approvals`, Jest snapshot) tự động hoá đúng ý "golden master", và **mutation testing** (Stryker) để kiểm xem lưới test có thật sự chặt.
> - **"First, make it work (bọc test) rồi refactor"** càng đúng trong kỷ nguyên AI: bảo Copilot/Cursor "refactor cái này" mà *không* có characterization test là mời gọi thảm hoạ — AI dễ đổi hành vi một cách tinh vi. Test là hợp đồng giữ AI trung thực.
> - **Review chuyên nghiệp**: năm 2026 là **pull request review** thường nhật + review có AI hỗ trợ. Tinh thần Uncle Bob — "phê bình là việc nên làm và nên *hoan nghênh* khi người khác làm cho mình" — vẫn là văn hoá đội lành mạnh (nối khoá *Clean Coder*).
> - **Vẫn vàng**: đo coverage trước khi đụng, ghim hành vi, refactor thử-và-sai, và Boy Scout Rule.

## 7. Áp dụng vào codebase của bạn

> [!question] Áp dụng vào codebase của bạn
> 1. **Ghim một hàm legacy.** Tìm một hàm cũ không ai dám đụng, không có test. Viết 5–6 characterization test chụp hành vi hiện tại của nó (dù bạn nghi nó có bug). Giờ bạn đã có lưới.
> 2. **Đo coverage trước.** Chạy công cụ coverage trên một module bạn sắp sửa. Nó phủ bao nhiêu %? Những dòng *không* phủ chính là nơi refactor dễ phá ngầm nhất.
> 3. **Tập review chuyên nghiệp.** Lần review PR tới, phê bình *code* (không phải người), nêu lý do, và khi bị người khác phê bình code mình — tập *hoan nghênh* thay vì thủ thế.
> 4. **Boy Scout một lần.** Trong file bạn đang mở, chọn một cải thiện nhỏ (đổi tên, tách một khối, bỏ `==` lỏng). Làm, chạy test, commit. Để lại sạch hơn lúc đến.

## 8. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Professional review** | Phê bình *code* (không phải người) để cùng học; nên làm và nên hoan nghênh (tr. 268). |
| **First, make it work** | Đo & bổ sung test cho đủ phủ *trước khi* refactor code lạ (tr. 267). |
| **Characterization test** | "Golden master": ghim hành vi hiện tại của code để refactor không làm đổi nó. |
| **Refactoring = trial and error** | Quá trình lặp, có khi hoàn tác chính mình, hội tụ dần (tr. 265). |
| **Boy Scout Rule** | Để lại code sạch hơn lúc bạn chạm vào — kết của cả hai chương (tr. 284). |
| **Shallow module** | (2026, Ousterhout) Tách quá nhỏ làm tăng tải nhận thức — rủi ro của "clean code quá đà". |

## 9. Câu hỏi tự kiểm tra

1. Vì sao Uncle Bob gọi việc mổ code của Gilbert là "professional review" chứ không phải công kích? *(tr. 268)*
2. "First, make it work" nghĩa là làm gì *trước* khi refactor? Clover cho thấy gì về `SerialDate`? *(tr. 267)*
3. Characterization test (golden master) giúp refactor code lạ an toàn thế nào? *(mục 4)*
4. "Refactoring là thử-và-sai" — cho một ví dụ về việc hoàn tác chính mình. *(tr. 265)*
5. Vì sao `SetupTeardownIncluder` lại thành ví dụ *ngược* về "clean code quá đà" năm 2026? *(Đối chiếu 2026)*

## Tóm tắt một trang

```
BÀI 14 — REFACTOR NGOÀI ĐỜI: ĐỌC CODE NGƯỜI, GỘT CHO SẠCH
─────────────────────────────────────────────────────────
Ch.15 mổ ComparisonCompactor (JUnit); Ch.16 mổ SerialDate (JCommon)
— code THẬT của người khác.

REVIEW   "đây là code tốt. Và tôi sắp xé nó ra" (tr.267) nhưng là
         "professional review... nên HOAN NGHÊNH" (tr.268). Không công kích.

FIRST MAKE IT WORK  đo coverage (Clover: ~50%), VIẾT TEST đủ phủ
         TRƯỚC khi refactor (tr.267).

CHARACTERIZATION TEST  ghim hành vi legacy (golden) → refactor →
         bản sạch phải khớp mọi golden. legacyShipping == shippingFee.

THẬT THÀ  "refactor là thử-và-sai, có khi hoàn tác chính mình" (tr.265).
         Kết cả hai chương: BOY SCOUT RULE — để lại sạch hơn (tr.284).

2026   SetupTeardownIncluder = ví dụ NGƯỢC "clean code quá đà"
       (Ousterhout, shallow module). Characterization = Feathers +
       snapshot/mutation test. Bọc test trước khi nhờ AI refactor.
```

## Nguồn

- **Robert C. Martin**, *Clean Code* (Prentice Hall, 2008) — **Chương 15, "JUnit Internals"** (`tr. 251–265`): phê bình `ComparisonCompactor` của JUnit (tr. 251); chuỗi refactor (tr. 252–264); "refactoring là thử-và-sai", Boy Scout Rule (tr. 265). **Chương 16, "Refactoring SerialDate"** (`tr. 267–284`): "good code, và tôi sắp xé nó ra" (tr. 267); "professional review" (tr. 268); "First, Make It Work" — coverage ~50%, viết test độc lập (tr. 267); chuỗi refactor `SerialDate`→`DayDate` (tr. 268–284); kết Boy Scout Rule (tr. 284). `tai_lieu/Clean.Code.2008.8.pdf`
- Bổ sung 2026 dẫn từ ngoài sách: Michael Feathers, *Working Effectively with Legacy Code*; John Ousterhout (shallow modules); approval/snapshot testing; mutation testing (Stryker); PR review.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 31`.

---

**Bản đồ khoá học:** [Bài 0 — Clean Code là gì](bai_00_clean_code_la_gi.md) · [Bài 1 — Đặt tên](bai_01_dat_ten.md) · [Bài 2 — Hàm](bai_02_ham.md) · [Bài 3 — Comment](bai_03_comment.md) · [Bài 4 — Định dạng](bai_04_dinh_dang.md) · [Bài 5 — Object & dữ liệu](bai_05_object_va_du_lieu.md) · [Bài 6 — Xử lý lỗi](bai_06_xu_ly_loi.md) · [Bài 7 — Ranh giới](bai_07_ranh_gioi.md) · [Bài 8 — Unit test](bai_08_unit_test.md) · [Bài 9 — Class](bai_09_class.md) · [Bài 10 — Hệ thống](bai_10_he_thong.md) · [Bài 11 — Thiết kế nổi lên](bai_11_thiet_ke_noi_len.md) · [Bài 12 — Concurrency](bai_12_concurrency.md) · [Bài 13 — Xem code sạch nảy sinh](bai_13_xem_code_nay_sinh.md) · [Bài 14 ← bạn đang ở đây] · [Bài 15 — Danh mục mùi code](bai_15_danh_muc_mui_code.md)

Xem thêm [README khoá học](../README.md).
