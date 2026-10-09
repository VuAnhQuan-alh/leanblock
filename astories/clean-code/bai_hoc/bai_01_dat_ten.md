# Bài 1 — Đặt tên: để code tự nói ý định

> [!info] Về bài này
> Dựng từ **Chương 2 — "Meaningful Names"** (tác giả Tim Ottinger) của *Clean Code* (Robert C. Martin, 2008 — `tai_lieu/`, `tr. 17–30`).
> Trích theo `Ch. N` + `tr. X` (số trang **in trong sách**; PDF = `tr. + 31`). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, kèm bản dịch gọn.
> Mạch bài: *code không đọc được → gọi tên vấn đề → bản sạch (TypeScript, chạy được) → nguyên tắc → đối chiếu 2026 → áp dụng*.
>
> **Chạy code:** cần **Node 22.6+** (chạy thẳng `.ts`). Lưu file rồi gõ `node <tên-file>.ts`. Không cần cài gói.

## Mục lục

1. [Mở đầu: hàm getThem không ai đọc nổi](#1-mở-đầu-hàm-getthem-không-ai-đọc-nổi)
2. [Dùng tên nói rõ ý định](#2-dùng-tên-nói-rõ-ý-định)
3. [Code minh hoạ: ba bước làm sạch một cái tên](#3-code-minh-hoạ-ba-bước-làm-sạch-một-cái-tên)
4. [Tránh gây hiểu lầm, phân biệt phải có nghĩa](#4-tránh-gây-hiểu-lầm-phân-biệt-phải-có-nghĩa)
5. [Tên phát âm được, tra được](#5-tên-phát-âm-được-tra-được)
6. [Tên lớp, tên hàm, và một từ cho một khái niệm](#6-tên-lớp-tên-hàm-và-một-từ-cho-một-khái-niệm)
7. [Đối chiếu 2026](#7-đối-chiếu-2026)
8. [Áp dụng vào codebase của bạn](#8-áp-dụng-vào-codebase-của-bạn)
9. [Từ điển thuật ngữ](#9-từ-điển-thuật-ngữ)
10. [Câu hỏi tự kiểm tra](#10-câu-hỏi-tự-kiểm-tra)
11. [Tóm tắt một trang](#tóm-tắt-một-trang)
12. [Nguồn](#nguồn)

---

## 1. Mở đầu: hàm getThem không ai đọc nổi

Tên có mặt ở khắp nơi trong phần mềm: biến, hàm, tham số, lớp, file, thư mục. Vì ta đặt tên nhiều đến thế, tốt nhất là đặt cho khéo. Chương này mở bằng một hàm trông vô hại — không biểu thức phức tạp, thụt lề gọn gàng, chỉ ba biến và hai hằng — mà vẫn không ai đoán nổi nó làm gì:

```
public List<int[]> getThem() {
  List<int[]> list1 = new ArrayList<int[]>();
  for (int[] x : theList)
    if (x[0] == 4)
      list1.add(x);
  return list1;
}
```

Vấn đề không nằm ở độ phức tạp, mà ở cái Tim Ottinger gọi là *implicity* — mức độ bối cảnh **không** hiện ra trong chính code. Để hiểu, bạn buộc phải biết sẵn câu trả lời cho: `theList` chứa thứ gì? Chỉ số 0 của mỗi phần tử có ý nghĩa gì? Con số `4` nghĩa là gì? Những tri thức đó nằm trong đầu người viết, không nằm trong code.

> [!quote] Ch. 2 — Use Intention-Revealing Names (tr. 18)
> "If a name requires a comment, then the name does not reveal its intent."
>
> *Nếu một cái tên cần tới comment để giải thích, thì cái tên đó đã không nói lên ý định của nó.*

## 2. Dùng tên nói rõ ý định

Cách chữa không phải thêm comment, mà là **đặt tên cho những thứ đang ẩn**. Giả sử đây là game dò mìn: `theList` là bàn cờ (`gameBoard`), mỗi ô là một mảng, chỉ số 0 giữ trạng thái, và trạng thái `4` nghĩa là "đã cắm cờ". Chỉ cần đặt tên cho các khái niệm đó, code đổi hẳn — dù **không** bớt đi một phép toán hay một cấp lồng nào.

> [!quote] Ch. 2 — Use Intention-Revealing Names (tr. 17)
> "Choosing good names takes time but saves more than it takes."
>
> *Chọn tên tốt tốn thời gian, nhưng tiết kiệm nhiều hơn phần đã tốn.*

## 3. Code minh hoạ: ba bước làm sạch một cái tên

Cùng một phép lọc "lấy các ô đã cắm cờ", viết ba lần — mỗi lần tên nói rõ hơn một chút, và kết quả không đổi:

```typescript
import { strict as assert } from "node:assert";

// ===== Bản 1: tên vô nghĩa, số ma thuật =====
function getThem(theList: number[][]): number[][] {
  const list1: number[][] = [];
  for (const x of theList) if (x[0] === 4) list1.push(x);
  return list1;
}

// ===== Bản 2: tên nói rõ ý định, đặt tên cho số ma thuật =====
const STATUS_VALUE = 0;
const FLAGGED = 4;

function getFlaggedCells(gameBoard: number[][]): number[][] {
  const flaggedCells: number[][] = [];
  for (const cell of gameBoard)
    if (cell[STATUS_VALUE] === FLAGGED) flaggedCells.push(cell);
  return flaggedCells;
}

// ===== Bản 3: Cell thành lớp, giấu số ma thuật sau isFlagged() =====
class Cell {
  private status: number;
  constructor(status: number) {
    this.status = status;
  }
  isFlagged(): boolean {
    return this.status === FLAGGED;
  }
}

function getFlaggedCellsTyped(gameBoard: Cell[]): Cell[] {
  return gameBoard.filter((cell) => cell.isFlagged());
}

// ô đầu mỗi hàng là trạng thái; 4 = đã cắm cờ
const rawBoard = [
  [4, 10, 20],
  [0, 1, 2],
  [4, 3, 3],
  [1, 0, 0],
];
const typedBoard = rawBoard.map((row) => new Cell(row[0]));

const n1 = getThem(rawBoard).length;
const n2 = getFlaggedCells(rawBoard).length;
const n3 = getFlaggedCellsTyped(typedBoard).length;

assert.equal(n1, n2);
assert.equal(n2, n3);
console.log("số ô đã cắm cờ (bản 1 getThem)        :", n1);
console.log("số ô đã cắm cờ (bản 2 getFlaggedCells):", n2);
console.log("số ô đã cắm cờ (bản 3 Cell.isFlagged) :", n3);
console.log("ba bản cùng kết quả:", n1 === n2 && n2 === n3);
```

Kết quả chạy thật:

```
số ô đã cắm cờ (bản 1 getThem)        : 2
số ô đã cắm cờ (bản 2 getFlaggedCells): 2
số ô đã cắm cờ (bản 3 Cell.isFlagged) : 2
ba bản cùng kết quả: true
```

Từ bản 1 sang bản 3, không một phép toán nào thay đổi — chỉ có cái tên. Nhưng `gameBoard.filter(cell => cell.isFlagged())` đọc gần như một câu tiếng Anh, còn `theList` với `x[0] === 4` thì phải giải mã. Đó là toàn bộ sức mạnh của việc đặt tên.

> [!note] Tự thử
> 1. Đổi `FLAGGED = 4` thành `5`. Bản nào bạn chỉ phải sửa **một chỗ**, bản nào phải đi lùng con số `4` rải rác?
> 2. Thêm một hàng `[4, 9, 9]` vào `rawBoard` (nhớ `typedBoard` tự suy ra). Ba con số có còn khớp không?
> 3. Đổi tên `getFlaggedCellsTyped` thành `g`. Sáu tháng nữa đọc lại, bạn mất bao lâu để nhớ `g` làm gì?

## 4. Tránh gây hiểu lầm, phân biệt phải có nghĩa

Tên tồi hơn cả tên vô nghĩa là tên **gây hiểu lầm**. Đừng gọi một nhóm tài khoản là `accountList` nếu nó không thực sự là một `List` — với lập trình viên, `list` có nghĩa cụ thể. Đừng đặt hai tên khác nhau tí xíu (`XYZControllerForEfficientHandlingOfStrings` vs `...EfficientStorageOfStrings`). Và đừng bao giờ dùng chữ `l` thường hay `O` hoa làm tên biến — chúng trông y hệt số `1` và `0`.

> [!quote] Ch. 2 — Avoid Disinformation (tr. 20)
> "Spelling similar concepts similarly is information. Using inconsistent spellings is disinformation."
>
> *Viết các khái niệm giống nhau theo lối giống nhau là **thông tin**. Viết bất nhất là **thông tin sai lệch**.*

Phân biệt tên cũng phải có nghĩa. Thêm số thứ tự (`a1`, `a2`) hay "từ nhiễu" (`ProductInfo`, `ProductData`, `CustomerObject`) chỉ làm compiler hài lòng chứ không nói thêm được gì. Ba hàm `getActiveAccount()`, `getActiveAccounts()`, `getActiveAccountInfo()` đặt cạnh nhau: người sau biết gọi cái nào?

## 5. Tên phát âm được, tra được

Hai tiêu chí thực dụng nữa. **Phát âm được**, vì "lập trình là hoạt động xã hội" — bạn phải nói về code với người khác; một biến `genymdhms` khiến cả nhóm phải phát âm như người ngớ ngẩn. **Tra được**, vì tên một chữ và số ma thuật rất khó `grep`: tìm `MAX_CLASSES_PER_STUDENT` thì dễ, tìm số `7` thì ra vô vàn chỗ không liên quan.

> [!quote] Ch. 2 — Use Searchable Names (tr. 22)
> "The length of a name should correspond to the size of its scope."
>
> *Độ dài của một cái tên nên tương xứng với độ lớn phạm vi của nó.*

Nghĩa là: biến một chữ (`i`, `j`) chỉ nên dùng làm biến cục bộ trong hàm ngắn; càng được nhìn thấy ở nhiều nơi, tên càng cần dài và dễ tra. Chương này cũng khai tử **Hungarian Notation** và tiền tố `m_`: thời compiler không kiểm kiểu thì chúng là cái nạng, còn nay ngôn ngữ có hệ kiểu giàu và IDE tô màu, chúng chỉ còn là rác.

## 6. Tên lớp, tên hàm, và một từ cho một khái niệm

Vài quy ước gọn mà đắt:

- **Lớp** mang tên danh từ (`Customer`, `WikiPage`, `AddressParser`); tránh `Manager`, `Processor`, `Data`, `Info`. Tên lớp không phải động từ (tr. 25).
- **Hàm** mang tên động từ (`postPayment`, `deletePage`, `save`) (tr. 25).
- **Một từ cho một khái niệm**: đừng để `fetch`, `retrieve`, `get` cùng nghĩa rải ở các lớp khác nhau — người dùng phải nhớ "lớp này xài từ nào".
- **Đừng chơi chữ** (*don't pun*): đừng dùng `add` cho cả "cộng hai giá trị" lẫn "nhét một phần tử vào collection" — cái sau nên là `insert`/`append`.
- **Đừng cố tỏ ra dí dỏm**: `HolyHandGrenade` hay `eatMyShorts()` chỉ vui với người biết trò đùa.

> [!quote] Ch. 2 — Don't Be Cute (tr. 26)
> "Say what you mean. Mean what you say."
>
> *Nói đúng điều bạn muốn. Và làm đúng điều bạn nói.*

Sợi chỉ xuyên suốt cả chương là một câu phân biệt "thông minh" với "chuyên nghiệp":

> [!quote] Ch. 2 — Avoid Mental Mapping (tr. 25)
> "One difference between a smart programmer and a professional programmer is that the professional understands that clarity is king."
>
> *Một khác biệt giữa lập trình viên thông minh và lập trình viên chuyên nghiệp: người chuyên nghiệp hiểu rằng **rõ ràng là vua**.*

## 7. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> Đây là chương **già đi đẹp nhất** của cả cuốn — gần như toàn bộ còn đúng nguyên năm 2026. Tên nói rõ ý định, tránh gây hiểu lầm, tra được, một-từ-một-khái-niệm: vẫn là vàng. Vài chi tiết cần cập nhật:
> - **Hungarian Notation / tiền tố `m_`, `I`**: sách tuyên bố đã chết — năm 2026 đúng hẳn với kiểu Hungarian. Nhưng tiền tố `I` cho interface (`IShapeFactory`) vẫn sống dai trong hệ sinh thái C#/TypeScript; Ottinger ghét nó, nhiều team vẫn giữ. Đây là chuyện quy ước nhóm, không phải đúng/sai tuyệt đối.
> - **Quy ước `get`/`set`/`is` kiểu JavaBean** là của Java. Trong TypeScript, ta có `get` accessor của ngôn ngữ, hoặc field trần, hoặc chỉ `isFlagged()` — tinh thần (predicate đặt tên theo giá trị) giữ nguyên, cú pháp thì theo ngôn ngữ của bạn.
> - **Cái mới sau 2008**: tên hàm `async` nên ngụ ý chờ đợi (`fetchUser`, `loadConfig`); tên biến boolean nên là mệnh đề khẳng định (`isLoading`, `hasPermission`) — đều là phần mở rộng tự nhiên của "tên nói rõ ý định".
> - **Tên và AI (2026)**: trình gợi ý như Copilot/Cursor đọc *tên* của bạn để đoán ý; đặt tên rõ không chỉ giúp người, mà còn khiến máy sinh code đúng hơn. Tên tồi làm hỏng cả gợi ý của AI.

## 8. Áp dụng vào codebase của bạn

> [!question] Áp dụng vào codebase của bạn
> 1. **Săn một `getThem` thật.** Tìm trong code bạn một hàm có số ma thuật (`=== 4`, `status === 2`…). Đặt tên hằng cho con số đó. Commit riêng — đó là một lần "Boy Scout".
> 2. **Grep thử một con số.** Chọn một hằng số quan trọng trong dự án (giới hạn, timeout). `grep` giá trị thô của nó xem rải bao nhiêu chỗ. Nếu > 1, bạn vừa tìm ra một nguồn bug chờ sẵn.
> 3. **Đọc to một tên.** Tìm biến/hàm khó phát âm nhất trong module bạn đang làm. Nếu không đọc to lên được mà không thấy ngượng, đổi tên nó.
> 4. **Một từ một khái niệm.** Dự án bạn đang dùng mấy từ cho "lấy dữ liệu" — `get`, `fetch`, `load`, `retrieve`? Chọn một, ghi vào quy ước nhóm.

## 9. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Intention-revealing name** | Tên trả lời được "tồn tại để làm gì, làm gì, dùng ra sao" mà không cần comment (tr. 17–18). |
| **Magic number** (số ma thuật) | Hằng số xuất hiện trần trong code (`=== 4`) không rõ nghĩa; nên đặt tên (`FLAGGED`). |
| **Disinformation** | Tên gieo manh mối sai: `accountList` mà không phải `List`, dùng `l`/`O` làm biến (tr. 19–20). |
| **Noise word** (từ nhiễu) | `Info`, `Data`, `Object`, `variable`… thêm vào mà không tạo khác biệt có nghĩa (tr. 20–21). |
| **Hungarian Notation** | Lối mã hoá kiểu dữ liệu vào tên (`phoneString`); sách tuyên bố đã lỗi thời (tr. 23–24). |
| **Pronounceable / searchable name** | Tên đọc được để thảo luận, và dài vừa đủ để `grep` ra (tr. 21–23). |

## 10. Câu hỏi tự kiểm tra

1. Vì sao `getThem` khó hiểu dù code rất đơn giản? Khái niệm *implicity* là gì? *(tr. 18)*
2. Quy tắc "độ dài tên tương xứng phạm vi" nghĩa là gì? Khi nào `i` là tên chấp nhận được? *(tr. 22, 25)*
3. Phân biệt *disinformation* với *noninformation*, mỗi loại một ví dụ. *(tr. 19–21)*
4. "Chơi chữ" (*pun*) trong đặt tên là gì? Cho ví dụ với `add`. *(tr. 27)*
5. Nêu một lời khuyên đặt tên của chương đã được cập nhật cho TypeScript/2026 — và cập nhật đó là gì.

## Tóm tắt một trang

```
BÀI 1 — ĐẶT TÊN: ĐỂ CODE TỰ NÓI Ý ĐỊNH
─────────────────────────────────────────────────────────
LÕI       Tên tốt trả lời: tồn tại để làm gì, làm gì, dùng sao.
          "Cần comment để giải thích = tên đã thất bại" (tr.18).

getThem → getFlaggedCells → cell.isFlagged()
          Không đổi một phép toán nào — chỉ đổi tên — mà code
          từ "phải giải mã" thành "đọc như câu tiếng Anh".

TRÁNH     · disinformation: accountList không phải List; l/O
          · noise words: Info, Data, Object, ...Manager
          · magic number: đặt tên hằng (FLAGGED = 4)
          · pun: add dùng cho hai nghĩa khác nhau

NÊN       · phát âm được (lập trình là việc xã hội)
          · tra được; độ dài tên ~ độ lớn phạm vi (tr.22)
          · lớp = danh từ; hàm = động từ (tr.25)
          · một từ cho một khái niệm

CÂU CHỐT  "clarity is king" — rõ ràng là vua (tr.25).

2026      Chương già đi ĐẸP NHẤT, gần như còn nguyên. Cập nhật:
          Hungarian/m_ đã chết; get/set/is là của Java; thêm
          isLoading/hasPermission, tên async; tên rõ giúp cả
          AI gợi ý đúng.
```

## Nguồn

- **Robert C. Martin**, *Clean Code* (Prentice Hall, 2008) — **Chương 2, "Meaningful Names"** (Tim Ottinger) (`tr. 17–30`): tên ở khắp nơi, phải đặt khéo (tr. 17); `getThem` → `getFlaggedCells` và sức mạnh của tên nói rõ ý định (tr. 18–19); tránh gây hiểu lầm, `l`/`O` (tr. 19–20); phân biệt có nghĩa, từ nhiễu (tr. 20–21); tên phát âm được (tr. 21–22); tên tra được, độ dài ~ phạm vi (tr. 22–23); tránh mã hoá, Hungarian, `m_` (tr. 23–24); tránh ánh xạ trong đầu, "clarity is king" (tr. 25); tên lớp/hàm (tr. 25); đừng cute, một-từ-một-khái-niệm, đừng chơi chữ (tr. 26–27); thêm bối cảnh có nghĩa, đừng thừa bối cảnh (tr. 27–30). `tai_lieu/Clean.Code.2008.8.pdf`
- Quy ước trích: `tr. X` = số trang in; PDF = `X + 31`.

---

**Bản đồ khoá học:** [Bài 0 — Clean Code là gì](bai_00_clean_code_la_gi.md) · [Bài 1 ← bạn đang ở đây] · [Bài 2 — Hàm](bai_02_ham.md) · [Bài 3 — Comment](bai_03_comment.md) · [Bài 4 — Định dạng](bai_04_dinh_dang.md) · [Bài 5 — Object & dữ liệu](bai_05_object_va_du_lieu.md) · [Bài 6 — Xử lý lỗi](bai_06_xu_ly_loi.md) · [Bài 7 — Ranh giới](bai_07_ranh_gioi.md) · [Bài 8 — Unit test](bai_08_unit_test.md) · [Bài 9 — Class](bai_09_class.md) · [Bài 10 — Hệ thống](bai_10_he_thong.md) · [Bài 11 — Thiết kế nổi lên](bai_11_thiet_ke_noi_len.md) · [Bài 12 — Concurrency](bai_12_concurrency.md) · [Bài 13 — Xem code sạch nảy sinh](bai_13_xem_code_nay_sinh.md) · [Bài 14 — Refactor ngoài đời](bai_14_refactor_ngoai_doi.md) · [Bài 15 — Danh mục mùi code](bai_15_danh_muc_mui_code.md)

Xem thêm [README khoá học](../README.md).
