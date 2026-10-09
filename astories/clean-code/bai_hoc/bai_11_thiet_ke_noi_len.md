# Bài 11 — Thiết kế nổi lên: bốn quy tắc thiết kế đơn giản

> [!info] Về bài này
> Dựng từ **Chương 12 — "Emergence"** (tác giả Jeff Langr) của *Clean Code* (Robert C. Martin, 2008 — `tai_lieu/`, `tr. 171–176`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 31`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Mạch bài: *bốn quy tắc → code trùng lặp → bản sạch (TypeScript, chạy được) → nguyên tắc → đối chiếu 2026 → áp dụng*.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`.

## Mục lục

1. [Mở đầu: bốn quy tắc của thiết kế đơn giản](#1-mở-đầu-bốn-quy-tắc-của-thiết-kế-đơn-giản)
2. [Quy tắc 1: chạy qua mọi test](#2-quy-tắc-1-chạy-qua-mọi-test)
3. [Quy tắc 2: không trùng lặp](#3-quy-tắc-2-không-trùng-lặp)
4. [Code minh hoạ: diệt trùng lặp bằng Template Method](#4-code-minh-hoạ-diệt-trùng-lặp-bằng-template-method)
5. [Quy tắc 3: diễn đạt ý định](#5-quy-tắc-3-diễn-đạt-ý-định)
6. [Quy tắc 4: tối thiểu lớp và method](#6-quy-tắc-4-tối-thiểu-lớp-và-method)
7. [Đối chiếu 2026](#7-đối-chiếu-2026)
8. [Áp dụng vào codebase của bạn](#8-áp-dụng-vào-codebase-của-bạn)
9. [Từ điển thuật ngữ](#9-từ-điển-thuật-ngữ)
10. [Câu hỏi tự kiểm tra](#10-câu-hỏi-tự-kiểm-tra)
11. [Tóm tắt một trang](#tóm-tắt-một-trang)
12. [Nguồn](#nguồn)

---

## 1. Mở đầu: bốn quy tắc của thiết kế đơn giản

Nếu có bốn quy tắc đơn giản mà cứ theo là thiết kế tốt *tự nổi lên* (emergent) thì sao? Jeff Langr giới thiệu **bốn quy tắc Thiết kế Đơn giản** của Kent Beck. Một thiết kế là "đơn giản" nếu nó:

> [!quote] Ch. 12 — Getting Clean via Emergent Design (tr. 172)
> "Runs all the tests • Contains no duplication • Expresses the intent of the programmer • Minimizes the number of classes and methods"
>
> *• Chạy qua mọi test • Không trùng lặp • Diễn đạt ý định của lập trình viên • Tối thiểu số lớp và method*

Bốn quy tắc được liệt kê **theo thứ tự quan trọng**. Bạn sẽ nhận ra đây chính là bốn quy tắc mà Ron Jeffries đã nhắc ở [Bài 0](bai_00_clean_code_la_gi.md).

## 2. Quy tắc 1: chạy qua mọi test

Thiết kế hoàn hảo trên giấy mà không có cách đơn giản để *kiểm chứng* hệ thống chạy đúng thì mọi công sức trên giấy đều đáng ngờ. Hệ không kiểm chứng được thì không nên triển khai. Điều bất ngờ là: chính việc ép hệ thống *test được* lại đẩy thiết kế về phía tốt hơn — lớp nhỏ, đơn-trách-nhiệm (SRP), ít ràng buộc (dùng DIP, interface, dependency injection để giảm coupling).

> [!quote] Ch. 12 — Simple Design Rule 1: Runs All the Tests (tr. 172)
> "Writing tests leads to better designs."
>
> *Viết test dẫn tới thiết kế tốt hơn.*

Có test rồi (quy tắc 1), ta mới dám áp ba quy tắc còn lại — vì chúng đều là **refactor**, mà refactor không test bọc thì đáng sợ. (Nối với [Bài 8](bai_08_unit_test.md).)

## 3. Quy tắc 2: không trùng lặp

> [!quote] Ch. 12 — No Duplication (tr. 173)
> "Duplication is the primary enemy of a well-designed system."
>
> *Trùng lặp là kẻ thù số một của một hệ thống được thiết kế tốt.*

Trùng lặp hiện ra nhiều dạng: dòng giống hệt, dòng *na ná* (có thể nắn cho giống hẳn rồi gộp), và trùng lặp *cài đặt* — ví dụ `isEmpty()` nên định nghĩa bằng `return 0 == size()` thay vì tự đếm riêng. Diệt trùng lặp "ở mức nhỏ" (reuse in the small) có thể làm độ phức tạp hệ thống co lại đáng kể.

## 4. Code minh hoạ: diệt trùng lặp bằng Template Method

Khi hai method gần như giống hệt, chỉ khác một khúc, dùng **Template Method**: đặt thuật toán chung ở lớp cha, để lớp con điền vào "lỗ hổng" khác biệt. Ví dụ chính sách nghỉ phép US/EU:

```typescript
import { strict as assert } from "node:assert";

// Template Method: thuật toán chung ở lớp cha, chỉ "lỗ hổng" khác nhau ở con
abstract class VacationPolicy {
  accrue(hoursWorked: number): number {
    const base = this.calculateBase(hoursWorked);
    const adjusted = this.alterForLegalMinimums(base);
    return this.applyToPayroll(adjusted);
  }
  private calculateBase(hoursWorked: number): number {
    return Math.floor(hoursWorked / 40); // 1 ngày phép / 40 giờ làm
  }
  protected abstract alterForLegalMinimums(days: number): number;
  private applyToPayroll(days: number): number {
    return days; // ghi vào bảng lương (ở đây chỉ trả về)
  }
}
class USVacationPolicy extends VacationPolicy {
  protected alterForLegalMinimums(days: number): number {
    return Math.max(days, 10); // Mỹ: tối thiểu 10 ngày
  }
}
class EUVacationPolicy extends VacationPolicy {
  protected alterForLegalMinimums(days: number): number {
    return Math.max(days, 20); // EU: tối thiểu 20 ngày
  }
}

const worked = 200; // 200 / 40 = 5 ngày cơ sở
const us = new USVacationPolicy().accrue(worked);
const eu = new EUVacationPolicy().accrue(worked);
assert.equal(us, 10);
assert.equal(eu, 20);
console.log("200 giờ -> phép US:", us, " phép EU:", eu);
console.log("thuật toán chung dùng chung; chỉ 'lỗ hổng' tối thiểu pháp lý khác nhau (DRY).");
```

Kết quả chạy thật:

```
200 giờ -> phép US: 10  phép EU: 20
thuật toán chung dùng chung; chỉ 'lỗ hổng' tối thiểu pháp lý khác nhau (DRY).
```

`accrue` — ba bước *tính cơ sở → chỉnh theo tối thiểu pháp lý → ghi lương* — viết **một lần** ở lớp cha. US và EU chỉ điền phần khác biệt duy nhất (`alterForLegalMinimums`). Nếu không dùng Template Method, hai method `accrueUS`/`accrueEU` sẽ lặp lại toàn bộ ba bước, và sửa thuật toán chung là sửa hai chỗ.

> [!note] Tự thử
> 1. Thêm `JapanVacationPolicy` (tối thiểu 15 ngày). Bạn phải viết thêm bao nhiêu dòng? Có phải động vào `accrue` không?
> 2. Đổi `calculateBase` thành `/ 20` (1 ngày / 20 giờ). Bao nhiêu lớp phải sửa? (Gợi ý: 1 — đó là DRY.)
> 3. Thử viết lại *không* Template Method: `accrueUS` và `accrueEU` tự làm cả ba bước. Giờ sửa bước `applyToPayroll` phải đụng mấy chỗ?

## 5. Quy tắc 3: diễn đạt ý định

Phần lớn chi phí của một dự án phần mềm nằm ở **bảo trì dài hạn**. Người bảo trì sau không hiểu sâu bài toán như bạn lúc viết. Vậy nên:

> [!quote] Ch. 12 — Expressive (tr. 175)
> "code should clearly express the intent of its author. The clearer the author can make the code, the less time others will have to spend understanding it."
>
> *code nên diễn đạt rõ ý định của tác giả. Tác giả làm code càng rõ, người khác càng tốn ít thời gian để hiểu.*

Cách diễn đạt: tên tốt ([Bài 1](bai_01_dat_ten.md)), hàm/lớp nhỏ ([Bài 2](bai_02_ham.md), [Bài 9](bai_09_class.md)), dùng tên mẫu thiết kế chuẩn (`COMMAND`, `VISITOR`), và test viết khéo (test là "tài liệu bằng ví dụ"). Nhưng điều quan trọng nhất:

> [!quote] Ch. 12 — Expressive (tr. 176)
> "the most important way to be expressive is to try."
>
> *cách quan trọng nhất để diễn đạt rõ là **chịu cố gắng**.*

Vì người đọc code của bạn tiếp theo, nhiều khả năng nhất, chính là bạn.

## 6. Quy tắc 4: tối thiểu lớp và method

Ngay cả diệt-trùng-lặp, diễn-đạt, SRP cũng có thể bị đẩy *quá đà* — tạo ra quá nhiều lớp và method tí hon. Quy tắc 4 kéo lại: giữ số lớp/hàm thấp. Số lớp/method cao đôi khi là hậu quả của **giáo điều vô nghĩa** (ví dụ "mọi lớp đều phải có interface", hay "luôn tách dữ liệu và hành vi thành hai lớp"). Hãy chống giáo điều ấy bằng lối thực dụng. Nhưng nhớ: đây là quy tắc **ưu tiên thấp nhất** trong bốn — quan trọng hơn cả vẫn là có test, diệt trùng lặp, và diễn đạt rõ.

## 7. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Chương này **già đi rất tốt** — bốn quy tắc gần như không ai cãi, và chính quy tắc 4 là liều vắc-xin chống đúng những lời phê bình "clean code đẻ quá nhiều mảnh vụn".
> - **Bốn quy tắc = cốt lõi còn sống của XP.** Năm 2026, "simple design" vẫn là nền của refactoring và TDD. Thứ tự ưu tiên (test > DRY > diễn đạt > tối thiểu số lượng) vẫn là cách phân xử tốt khi các nguyên tắc xung đột.
> - **Quy tắc 4 trả lời sẵn Ousterhout/"classitis".** Chính Jeff Langr viết "diệt trùng lặp và SRP có thể bị đẩy quá đà" — đây là chỗ sách *tự phản biện* cái mà [Bài 2](bai_02_ham.md) và [Bài 9](bai_09_class.md) bị chê (hàm/lớp quá nhỏ). Năm 2026, nhớ rằng "tối thiểu số lớp/method" cũng là một quy tắc, cân lại với "nhỏ là tốt".
> - **DRY — đừng cực đoan (2026).** Cộng đồng nhận ra **"nhầm trừu tượng còn đắt hơn trùng lặp"** (Sandi Metz: *"duplication is far cheaper than the wrong abstraction"*). Gộp hai đoạn *trông* giống nhau nhưng thay đổi vì *lý do khác nhau* là sai lầm — nối với **Rule of Three** (chờ thấy ba lần mới trừu tượng hoá). Template Method của mục 4 chỉ đúng khi hai policy *thật sự* chung một thuật toán.
> - **Template Method qua kế thừa** là mẫu 2008; năm 2026 thường ưu tiên **hợp thành / truyền hàm** (strategy qua tham số hàm) hơn cây kế thừa — cùng mục tiêu "điền lỗ hổng" nhưng linh hoạt hơn.
> - **Vẫn vàng**: test trước đã, diệt trùng lặp *thật*, diễn đạt ý định, và đừng để số lượng mảnh vụn phình to.

## 8. Áp dụng vào codebase của bạn

> [!question] Áp dụng vào codebase của bạn
> 1. **Chấm một module theo bốn quy tắc.** Có test không? Có trùng lặp *thật* không? Có diễn đạt ý định không? Số lớp/method có bị phình vì giáo điều không? Quy tắc nào rớt?
> 2. **Phân biệt trùng lặp thật vs trùng lặp giả.** Tìm hai đoạn code giống nhau. Chúng giống nhau vì *cùng một lý do*, hay chỉ *tình cờ giống* lúc này? (Sandi Metz: đừng gộp trùng lặp giả.)
> 3. **Tìm một Template Method tiềm năng.** Có hai hàm chung thuật toán, chỉ khác một khúc không? Thử rút khung chung ra (bằng kế thừa *hoặc* truyền hàm).
> 4. **Soi giáo điều.** Dự án có luật "mọi lớp phải có interface" hay tách lớp máy móc không? Nó có đang vi phạm quy tắc 4 không?

## 9. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Emergent design** | Thiết kế tốt *nổi lên* khi theo bốn quy tắc đơn giản, thay vì vẽ hết trước (tr. 171). |
| **Four Rules of Simple Design** | Chạy test > không trùng lặp > diễn đạt ý định > tối thiểu lớp/method (tr. 172). |
| **Reuse in the small** | Diệt trùng lặp ở mức nhỏ làm độ phức tạp hệ thống co lại (tr. 173–174). |
| **Template Method** | Thuật toán chung ở lớp cha, con điền "lỗ hổng" khác biệt (tr. 174–175). |
| **Wrong abstraction** | (2026, Sandi Metz) Gộp trùng lặp *giả* còn đắt hơn chính trùng lặp đó. |
| **Rule of Three** | (2026) Chờ thấy một mẫu lặp lại ba lần rồi hẵng trừu tượng hoá. |

## 10. Câu hỏi tự kiểm tra

1. Kể bốn quy tắc thiết kế đơn giản theo đúng thứ tự ưu tiên. *(tr. 172)*
2. Vì sao "viết test dẫn tới thiết kế tốt hơn"? *(tr. 172)*
3. Template Method diệt trùng lặp kiểu gì? Lớp con điền cái gì? *(tr. 174–175)*
4. Quy tắc 4 (tối thiểu lớp/method) cân lại điều gì? Vì sao nó ưu tiên thấp nhất? *(tr. 176)*
5. Sandi Metz phản biện gì về DRY, và "Rule of Three" nói gì? *(Đối chiếu 2026)*

## Tóm tắt một trang

```
BÀI 11 — THIẾT KẾ NỔI LÊN: BỐN QUY TẮC ĐƠN GIẢN
─────────────────────────────────────────────────────────
BỐN QUY TẮC (theo thứ tự ưu tiên, tr.172):
   1. Chạy qua MỌI TEST   → "viết test dẫn tới thiết kế tốt hơn"
   2. KHÔNG TRÙNG LẶP     → "kẻ thù số một" (tr.173)
   3. DIỄN ĐẠT ý định     → "cách quan trọng nhất là CHỊU cố gắng"(tr.176)
   4. TỐI THIỂU lớp/method→ chống giáo điều; ưu tiên THẤP nhất

TEMPLATE METHOD  thuật toán chung ở cha, con điền "lỗ hổng":
   VacationPolicy.accrue() dùng chung; US max(.,10) EU max(.,20)
   200 giờ → US 10, EU 20. Đổi thuật toán = sửa 1 chỗ.

2026  bốn quy tắc = cốt lõi XP còn sống. Quy tắc 4 trả lời sẵn
      "classitis". DRY đừng cực đoan: "nhầm trừu tượng đắt hơn
      trùng lặp" (Metz) + Rule of Three. Ưu tiên hợp thành hơn
      kế thừa cho Template Method.
```

## Nguồn

- **Robert C. Martin**, *Clean Code* (Prentice Hall, 2008) — **Chương 12, "Emergence"** (Jeff Langr) (`tr. 171–176`): bốn quy tắc thiết kế đơn giản của Kent Beck (tr. 171–172); quy tắc 1 — chạy mọi test, "viết test dẫn tới thiết kế tốt hơn" (tr. 172); quy tắc 2–4 là refactoring (tr. 172); không trùng lặp, `isEmpty`/`size`, `replaceImage`, Template Method `VacationPolicy` (tr. 173–175); diễn đạt, "cách quan trọng nhất là chịu cố gắng" (tr. 175–176); tối thiểu lớp/method, chống giáo điều (tr. 176); kết luận (tr. 176). `tai_lieu/Clean.Code.2008.8.pdf`
- Bổ sung 2026 dẫn từ ngoài sách: Sandi Metz, *"The Wrong Abstraction"* (2016); Rule of Three; composition over inheritance.
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 31`.

---

**Bản đồ khoá học:** [Bài 0 — Clean Code là gì](bai_00_clean_code_la_gi.md) · [Bài 1 — Đặt tên](bai_01_dat_ten.md) · [Bài 2 — Hàm](bai_02_ham.md) · [Bài 3 — Comment](bai_03_comment.md) · [Bài 4 — Định dạng](bai_04_dinh_dang.md) · [Bài 5 — Object & dữ liệu](bai_05_object_va_du_lieu.md) · [Bài 6 — Xử lý lỗi](bai_06_xu_ly_loi.md) · [Bài 7 — Ranh giới](bai_07_ranh_gioi.md) · [Bài 8 — Unit test](bai_08_unit_test.md) · [Bài 9 — Class](bai_09_class.md) · [Bài 10 — Hệ thống](bai_10_he_thong.md) · [Bài 11 ← bạn đang ở đây] · [Bài 12 — Concurrency](bai_12_concurrency.md) · [Bài 13 — Xem code sạch nảy sinh](bai_13_xem_code_nay_sinh.md) · [Bài 14 — Refactor ngoài đời](bai_14_refactor_ngoai_doi.md) · [Bài 15 — Danh mục mùi code](bai_15_danh_muc_mui_code.md)

Xem thêm [README khoá học](../README.md).
