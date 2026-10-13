# Bài 12 — Khớp chuỗi: Rabin–Karp và KMP *(nâng cao)*

> [!info] Về bài này
> Mở đầu **tầng nâng cao**. Tìm một *pattern* trong một *text* lớn là thao tác nền của trình soạn thảo, `grep`, công cụ tìm kiếm, và so khớp DNA. Cách ngây thơ tốn `O(nm)`. Bài này hai thuật toán nhanh hơn, mỗi cái một ý tưởng đẹp: **Rabin–Karp** (băm cửa sổ trượt — dùng lại bảng băm Bài 3) và **KMP** (dùng "hàm thất bại" để con trỏ text *không bao giờ lùi*). Đây là nơi băm (Bài 3) và tư duy ngẫu nhiên (sắp tới ở Bài 14) gặp lại nhau trong ứng dụng thật.
> Nguồn (Luật số 1): **Skiena** *The Algorithm Design Manual 3e* — **§6.7 Efficient String Matching** (Rabin–Karp) (`tai_lieu/`, trích `> [!quote] Skiena (tr. N)`, **PDF = tr. + 15** ở Ch6). **KMP** tham khảo **CLRS 4e Ch32** (xem hộp lưu ý nguồn).
> **Chạy demo:** `node bai_12.ts` — Node 22+, không cài gói. Code tất định.
> Cần đọc trước: [Bài 3 — bảng băm](bai_03_bang-bam.md) (Rabin–Karp là băm), [Bài 1 — Big-O](bai_01_big-o.md).

> [!warning] Về nguồn KMP
> Bản PDF CLRS trong `tai_lieu/` bị lỗi phông khi trích văn bản (chữ *fi/ffi* ra ký tự lạ), nên **không trích nguyên văn CLRS** ở đây để khỏi vi phạm Luật số 1. Mọi trích dẫn nguyên văn trong bài lấy từ **Skiena §6.7** (sạch); KMP được mô tả theo ý và dẫn CLRS §32.4 làm nguồn tra cứu chuẩn.

## Mục lục

1. [Tình huống: tìm một chuỗi trong một chuỗi lớn](#1-tình-huống-tìm-một-chuỗi-trong-một-chuỗi-lớn)
2. [Khớp ngây thơ và vì sao nó chậm](#2-khớp-ngây-thơ-và-vì-sao-nó-chậm)
3. [Rabin-Karp: băm cửa sổ trượt](#3-rabin-karp-băm-cửa-sổ-trượt)
4. [KMP: con trỏ text không bao giờ lùi](#4-kmp-con-trỏ-text-không-bao-giờ-lùi)
5. [Demo: naive, Rabin-Karp, KMP](#5-demo-naive-rabin-karp-kmp)
6. [Bản đồ khoá DSA](#6-bản-đồ-khoá-dsa)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Tình huống: tìm một chuỗi trong một chuỗi lớn

> [!example] Ctrl-F trên một văn bản khổng lồ
> Bạn gõ một từ vào ô tìm kiếm của trình soạn thảo, nó phải chỉ ra *mọi* chỗ từ đó xuất hiện trong tài liệu triệu ký tự — ngay lập tức. `grep` quét cả cây mã nguồn, công cụ tìm kiếm dò pattern trong hàng tỷ trang. Chung một bài toán.

> [!quote] Skiena (tr. 189)
> "The most fundamental operation on text strings is substring search"
>
> *Thao tác **nền tảng nhất** trên chuỗi văn bản là **tìm chuỗi con (substring search)**.*

Bài toán, đặc tả rõ (kiểu Skiena, Bài 0):

```
Bài toán: Substring Pattern Matching
Đầu vào: một text string t và một pattern string p.
Đầu ra:  t có chứa p như một chuỗi con không, nếu có thì ở đâu?
```

Gọi `n = |t|`, `m = |p|` (thường `m ≪ n`). Mục tiêu: nhanh hơn cách ngây thơ.

## 2. Khớp ngây thơ và vì sao nó chậm

Cách hiển nhiên: đặt pattern ở *mọi* vị trí trong text, so từng ký tự.

> [!quote] Skiena (tr. 189)
> "The simplest algorithm to search for the presence of pattern string p in text t overlays the pattern string at every position in the text, and checks whether every pattern character matches the corresponding text character."
>
> *Thuật toán **đơn giản nhất** để tìm sự có mặt của pattern `p` trong text `t` là **đặt chồng pattern lên mọi vị trí** trong text, rồi **kiểm từng ký tự pattern có khớp ký tự text tương ứng** không.*

Có `n − m + 1` vị trí, mỗi vị trí so tới `m` ký tự → **O(nm)** worst case. Tệ nhất khi pattern và text trùng nhau phần lớn rồi lệch ở ký tự cuối (vd text `"AAAA...AAB"`, pattern `"AAAB"`): mỗi vị trí so gần hết `m` ký tự mới phát hiện lệch. Hai thuật toán dưới đây tránh lãng phí đó bằng hai cách khác nhau.

## 3. Rabin-Karp: băm cửa sổ trượt

Ý tưởng Rabin–Karp: thay vì so *chuỗi*, so *số* — **băm** pattern và mỗi cửa sổ `m` ký tự của text, chỉ khi hai **hash bằng nhau** mới bỏ công so chuỗi thật.

> [!quote] Skiena (tr. 189)
> "It is based on hashing. Suppose we compute a given hash function on both the pattern string p and the m-character substring starting from the ith position of t. If these two strings are identical, clearly the resulting hash values must be the same."
>
> *Nó **dựa trên băm**. Giả sử ta tính một hàm băm trên **cả** pattern `p` lẫn chuỗi con `m` ký tự bắt đầu ở vị trí `i` của `t`. Nếu hai chuỗi **giống hệt**, rõ ràng **hai giá trị băm phải bằng nhau**.*

Nhưng tính hash mỗi cửa sổ từ đầu lại tốn `O(m)`, `n` cửa sổ thành `O(nm)` — chẳng lợi gì. Mẹo cốt tử là **băm lăn (rolling hash)**: biết hash cửa sổ ở vị trí `j`, tính hash cửa sổ `j+1` trong **O(1)** — vì hai cửa sổ chỉ khác một ký tự đầu bỏ đi và một ký tự cuối thêm vào (dùng lại hàm băm đa thức cơ số `α` của [Bài 3](bai_03_bang-bam.md)):

```
cửa sổ j:    [ s_j  s_{j+1} ... s_{j+m-1} ]            hash = H(S, j)
cửa sổ j+1:       [ s_{j+1} ... s_{j+m-1}  s_{j+m} ]    hash = H(S, j+1)
                  ↑ bỏ s_j (trừ đi)        ↑ thêm s_{j+m} (cộng vào)
H(S, j+1) = α·(H(S, j) − α^(m-1)·char(s_j)) + char(s_{j+m})   ← O(1)!
```

Vì hash có thể trùng cho hai chuỗi *khác* nhau (**false positive**, va chạm — Bài 3), khi hash khớp ta vẫn **xác minh** bằng so chuỗi thật `O(m)`. Nếu hàm băm tốt (`mod M`, `M` nguyên tố lớn), va chạm giả cực hiếm (xác suất `~1/M`), nên hầu như mọi cửa sổ chỉ tốn `O(1)` → **O(n + m) kỳ vọng**.

> [!quote] Skiena (tr. 190)
> "Rabin–Karp is a good example of a randomized algorithm"
>
> *Rabin–Karp là một **ví dụ hay về thuật toán ngẫu nhiên hoá**.*

Đây đúng là cầu nối sang [Bài 14](bai_14_ngau-nhien.md): chọn `M` ngẫu nhiên thì *không* bảo đảm `O(n+m)` worst case (xui thì va chạm liên tục), nhưng xác suất nghiêng hẳn về phía ta — kiểu "đúng gần như chắc chắn, nhanh gần như luôn".

## 4. KMP: con trỏ text không bao giờ lùi

Rabin–Karp *kỳ vọng* nhanh nhưng worst-case vẫn có thể tệ. **KMP** (Knuth–Morris–Pratt) cho worst-case `O(n + m)` *bảo đảm*, bằng một ý tưởng khác hẳn: khi khớp lệch, đừng vứt công đã làm.

Khi ngây thơ lệch ở vị trí `j` của pattern, nó lùi con trỏ text lại và thử lại từ vị trí kế — *quên* rằng `j` ký tự vừa rồi *đã khớp*. KMP tính trước một **hàm thất bại** *(failure/prefix function)* `fail[i]` = độ dài tiền tố của pattern cũng đồng thời là hậu tố của `p[0..i]`. Khi lệch, nó *nhảy* pattern về `fail[j-1]` thay vì về 0 — nhờ đó **con trỏ text không bao giờ lùi**, mỗi ký tự text được xét đúng một lần → `O(n)` (cộng `O(m)` dựng hàm thất bại).

```
text:    A A B A A C ...        pattern: A A B A
ngây thơ: lệch ở C → lùi text, thử lại từ vị trí +1 (phí)
KMP:      lệch ở C → biết "AA" vừa khớp vẫn là tiền tố hợp lệ,
          nhảy pattern theo fail[], text ĐỨNG YÊN ở C
fail cho "AABA" = [0, 1, 0, 1]
```

So ba cách: **ngây thơ** `O(nm)` (lùi và lặp lại); **Rabin–Karp** `O(n+m)` *kỳ vọng* (băm + xác minh khi trùng); **KMP** `O(n+m)` *bảo đảm* (không lùi text). Demo mục 5 đếm số lần so ký tự của cả ba.

## 5. Demo: naive, Rabin-Karp, KMP

Demo tìm `"AABA"` trong `"AABAACAADAABAABA"` bằng ba thuật toán — cùng ra các vị trí `[0, 9, 12]`, nhưng đếm công khác hẳn: ngây thơ so ký tự nhiều, Rabin–Karp chỉ xác minh khi hash khớp, KMP xét mỗi ký tự text đúng một lần.

```typescript
import { strict as assert } from "node:assert";

const text = "AABAACAADAABAABA";   // n = 16
const pattern = "AABA";             // m = 4, xuất hiện ở vị trí 0, 9, 12

// ─── NGÂY THƠ: đặt pattern ở MỌI vị trí, so từng ký tự. O(nm) ───
function naive(t: string, p: string): { hits: number[]; comparisons: number } {
  const hits: number[] = [];
  let comparisons = 0;
  for (let s = 0; s + p.length <= t.length; s++) {
    let j = 0;
    while (j < p.length) { comparisons++; if (t[s + j] !== p[j]) break; j++; }
    if (j === p.length) hits.push(s);
  }
  return { hits, comparisons };
}

// ─── RABIN–KARP: băm cửa sổ trượt, chỉ so chuỗi khi HASH khớp. O(n+m) kỳ vọng ───
// Băm lăn (rolling hash): tính hash cửa sổ kế từ cửa sổ trước trong O(1).
function rabinKarp(t: string, p: string): { hits: number[]; hashHits: number; verifications: number } {
  const m = p.length, n = t.length;
  const base = 256, mod = 1_000_003;             // M là số nguyên tố (Bài 3)
  const hits: number[] = [];
  let hashHits = 0, verifications = 0;
  let hp = 0, ht = 0, high = 1;                  // high = base^(m-1) mod M
  for (let i = 0; i < m; i++) {
    hp = (hp * base + p.charCodeAt(i)) % mod;
    ht = (ht * base + t.charCodeAt(i)) % mod;
    if (i < m - 1) high = (high * base) % mod;
  }
  for (let s = 0; s + m <= n; s++) {
    if (hp === ht) {                             // hash khớp → có THỂ trùng
      hashHits++;
      verifications++;                           // mới xác minh từng ký tự (tránh false positive)
      if (t.substr(s, m) === p) hits.push(s);
    }
    if (s + m < n) {                             // lăn sang cửa sổ kế trong O(1)
      ht = ((ht - t.charCodeAt(s) * high) * base + t.charCodeAt(s + m)) % mod;
      ht = ((ht % mod) + mod) % mod;             // giữ không âm
    }
  }
  return { hits, hashHits, verifications };
}

// ─── KMP: khi lệch, KHÔNG lùi con trỏ text — dùng "hàm thất bại" nhảy thông minh ───
function kmp(t: string, p: string): { hits: number[]; comparisons: number } {
  const m = p.length;
  const fail = new Array(m).fill(0);             // fail[i] = độ dài tiền tố-cũng-là-hậu tố dài nhất
  for (let i = 1, k = 0; i < m; i++) {
    while (k > 0 && p[i] !== p[k]) k = fail[k - 1];
    if (p[i] === p[k]) k++;
    fail[i] = k;
  }
  const hits: number[] = [];
  let comparisons = 0, k = 0;
  for (let i = 0; i < t.length; i++) {
    comparisons++;
    while (k > 0 && t[i] !== p[k]) k = fail[k - 1];  // nhảy theo fail, text KHÔNG lùi
    if (t[i] === p[k]) k++;
    if (k === m) { hits.push(i - m + 1); k = fail[k - 1]; }
  }
  return { hits, comparisons };
}

const nv = naive(text, pattern);
const rk = rabinKarp(text, pattern);
const km = kmp(text, pattern);

console.log(`KHỚP CHUỖI — tìm "${pattern}" trong "${text}" (n=${text.length}, m=${pattern.length}):`);
console.log(`  ngây thơ    : vị trí ${JSON.stringify(nv.hits)}, ${nv.comparisons} lần so ký tự`);
console.log(`  Rabin–Karp  : vị trí ${JSON.stringify(rk.hits)}, ${rk.hashHits} lần hash khớp → ${rk.verifications} lần xác minh`);
console.log(`  KMP         : vị trí ${JSON.stringify(km.hits)}, ${km.comparisons} lần so ký tự (text không lùi)`);

// Cả ba PHẢI tìm ra cùng các vị trí.
assert.deepEqual(nv.hits, [0, 9, 12]);
assert.deepEqual(rk.hits, nv.hits);
assert.deepEqual(km.hits, nv.hits);
// KMP so ký tự đúng n lần (mỗi ký tự text xét một lần, không lùi).
assert.equal(km.comparisons, text.length);
// Rabin–Karp chỉ xác minh khi hash khớp — ít hơn nhiều so quét ngây thơ.
assert.ok(rk.verifications <= nv.comparisons);

console.log("\nNgây thơ O(nm): vị trí nào cũng so lại từ đầu. Rabin–Karp băm cửa sổ trượt (Bài 3),");
console.log("chỉ so chuỗi khi hash khớp (Skiena tr.189). KMP dùng hàm thất bại để KHÔNG lùi text.");
```

Kết quả chạy thật *(tất định)*:

```
KHỚP CHUỖI — tìm "AABA" trong "AABAACAADAABAABA" (n=16, m=4):
  ngây thơ    : vị trí [0,9,12], 30 lần so ký tự
  Rabin–Karp  : vị trí [0,9,12], 3 lần hash khớp → 3 lần xác minh
  KMP         : vị trí [0,9,12], 16 lần so ký tự (text không lùi)

Ngây thơ O(nm): vị trí nào cũng so lại từ đầu. Rabin–Karp băm cửa sổ trượt (Bài 3),
chỉ so chuỗi khi hash khớp (Skiena tr.189). KMP dùng hàm thất bại để KHÔNG lùi text.
```

Ba điều đáng thấm. **(1) Băm biến so-chuỗi thành so-số:** Rabin–Karp chỉ bỏ công so ký tự ở `3` cửa sổ (đúng 3 chỗ hash khớp, không false positive ở đây) thay vì rà `30` lần như ngây thơ — nhờ băm lăn cập nhật hash mỗi cửa sổ trong `O(1)`. **(2) KMP không bao giờ lùi text:** đúng `16` lần so = `n`, mỗi ký tự text xét một lần; đó là lý do nó `O(n+m)` worst-case *bảo đảm*, không như Rabin–Karp (kỳ vọng). **(3) Cùng kết quả, khác tư tưởng:** cả ba ra `[0, 9, 12]` (tính đúng, Bài 0); chọn cái nào là chọn đánh đổi — Rabin–Karp đơn giản và tổng quát hoá dễ (tìm nhiều pattern, băm 2D), KMP bảo đảm worst-case, ngây thơ đủ cho chuỗi ngắn.

> [!note] Tự thử
> 1. Dựng text/pattern *worst case* cho ngây thơ: `text = "A".repeat(20) + "B"`, `pattern = "A".repeat(4) + "B"`. Đếm số lần so của ba thuật toán — khoảng cách giờ ra sao?
> 2. Ép Rabin–Karp gặp **false positive**: đổi `mod` thành số rất nhỏ (vd `7`) để nhiều cửa sổ trùng hash. `hashHits` và `verifications` tăng thế nào, kết quả `hits` có còn đúng không (nhờ bước xác minh)?
> 3. In mảng `fail` của KMP cho pattern `"ABABAC"`. Giải thích vì sao `fail[3] = 2`.
> 4. Vì sao Rabin–Karp dễ mở rộng để tìm *nhiều* pattern cùng lúc (băm tất cả pattern vào một tập), còn KMP thì không tự nhiên bằng? *(mục 3, 4)*

## 6. Bản đồ khoá DSA

| # | Bài | Chủ đề | Nguồn chính |
| :-- | :-- | :-- | :-- |
| 0 | Thuật toán & tính đúng | nền: đúng vs hiệu quả | Skiena Ch1 + Grokking |
| 1 | Phân tích Big-O | đo chi phí khi `n` lớn | Skiena Ch2 |
| 2 | CTDL tuyến tính | mảng / list / stack / queue | Skiena Ch3 |
| 3 | Từ điển & bảng băm | tra cứu O(1) trung bình | Skiena Ch3 |
| 4 | Heap & cây tìm kiếm | lấy min/max, tra có thứ tự | Skiena Ch3–4 |
| 5 | Sắp xếp | quicksort / mergesort / heapsort | Skiena Ch4 |
| 6 | Chia để trị & đệ quy | bẻ nhỏ bài toán, master theorem | Skiena Ch5 |
| 7 | Đồ thị: biểu diễn & duyệt | BFS / DFS | Skiena Ch7 |
| 8 | Đồ thị trọng số: MST & đường ngắn nhất | Dijkstra / Prim / Kruskal | Skiena Ch8 |
| 9 | Quy hoạch động | tối ưu bằng bảng con | Skiena Ch10 |
| 10 | Tìm kiếm tổ hợp & backtracking | duyệt không gian lời giải | Skiena Ch9 |
| 11 | NP-đầy đủ & bài toán khó | khi không có lời giải nhanh | Skiena Ch11–12 |
| 12 | **Khớp chuỗi** *(nâng cao)* ← *đang ở đây* | KMP / Rabin–Karp | Skiena §6.7 + CLRS Ch32 |
| 13 | *(nâng cao)* Luồng mạng | max-flow / min-cut | Skiena §8.5 + CLRS Ch24 |
| 14 | *(nâng cao)* Thuật toán ngẫu nhiên | randomized quicksort, Monte Carlo | Skiena Ch6 |

Rabin–Karp là băm ([Bài 3](bai_03_bang-bam.md)) + ngẫu nhiên hoá ([Bài 14](bai_14_ngau-nhien.md)); nối tiếp tầng nâng cao.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 12.1 — Bài toán khớp chuỗi là gì? Khớp ngây thơ tốn bao nhiêu?
> **Đáp:** tìm mọi vị trí pattern `p` (độ dài `m`) xuất hiện trong text `t` (độ dài `n`). Ngây thơ đặt `p` ở mọi vị trí, so từng ký tự → **O(nm)** worst case (Skiena tr. 189).

> [!question] Thẻ 12.2 — Ý tưởng cốt lõi của Rabin–Karp?
> **Đáp:** **băm** pattern và mỗi cửa sổ `m` ký tự; chỉ so chuỗi thật khi **hash khớp**. Hash giống thì chuỗi *có thể* giống; khác thì chắc chắn khác (Skiena tr. 189).

> [!question] Thẻ 12.3 — "Băm lăn" (rolling hash) làm gì, và vì sao quan trọng?
> **Đáp:** tính hash cửa sổ kế từ hash cửa sổ trước trong **O(1)** (bỏ ký tự đầu, thêm ký tự cuối). Không có nó, băm lại mỗi cửa sổ tốn `O(m)` → quay về `O(nm)`.

> [!question] Thẻ 12.4 — Vì sao Rabin–Karp cần bước "xác minh", và nó là thuật toán loại gì?
> **Đáp:** hash có thể trùng cho hai chuỗi khác (false positive, va chạm Bài 3) → phải so chuỗi thật khi hash khớp. Là **thuật toán ngẫu nhiên hoá**: `O(n+m)` *kỳ vọng*, không bảo đảm (Skiena tr. 190).

> [!question] Thẻ 12.5 — KMP khác Rabin–Karp ra sao? Chìa khoá của KMP là gì?
> **Đáp:** KMP cho `O(n+m)` worst-case *bảo đảm* (Rabin–Karp chỉ kỳ vọng). Chìa khoá: **hàm thất bại** cho phép nhảy pattern thông minh khi lệch, nên **con trỏ text không bao giờ lùi** — mỗi ký tự text xét một lần.

## 8. Câu hỏi tự kiểm tra

1. Viết đặc tả bài toán khớp chuỗi (Đầu vào/Đầu ra). Vì sao ngây thơ là O(nm)? *(mục 1, 2)*
2. Giải thích băm lăn: tính hash cửa sổ `j+1` từ cửa sổ `j` thế nào, vì sao O(1)? *(mục 3)*
3. False positive trong Rabin–Karp là gì? Bước xác minh xử lý nó ra sao? *(mục 3)*
4. KMP đảm bảo con trỏ text không lùi bằng cách nào? Hàm thất bại lưu gì? *(mục 4)*
5. Chạy demo mục 5. Vì sao KMP so đúng 16 lần (= n) còn ngây thơ tới 30? *(mục 4 & 5)*

## Tóm tắt một trang

```
BÀI 12 — KHỚP CHUỖI (nâng cao)
─────────────────────────────────────────────────────────
BÀI TOÁN  tìm mọi vị trí pattern p (|p|=m) trong text t (|t|=n). Thao tác nền
   tảng nhất trên chuỗi (Skiena tr.189).

NGÂY THƠ  đặt p ở mọi vị trí, so từng ký tự → O(nm). Phí khi trùng dài rồi lệch.

RABIN–KARP  so SỐ thay vì chuỗi: băm p và mỗi cửa sổ m ký tự, chỉ so chuỗi khi
   HASH khớp (Skiena tr.189). BĂM LĂN: hash cửa sổ kế tính từ cửa sổ trước
   trong O(1) (bỏ đầu, thêm cuối). Cần XÁC MINH (false positive = va chạm Bài
   3). Thuật toán NGẪU NHIÊN → O(n+m) KỲ VỌNG (Skiena tr.190).

KMP  O(n+m) BẢO ĐẢM. HÀM THẤT BẠI (prefix function) cho nhảy pattern thông
   minh khi lệch → con trỏ TEXT KHÔNG BAO GIỜ LÙI, mỗi ký tự text xét 1 lần.

DEMO  "AABA" trong "AABAACAADAABAABA" → [0,9,12]. Ngây thơ 30 so ký tự; Rabin–
   Karp 3 xác minh (hash khớp đúng 3 chỗ); KMP 16 (= n, không lùi).

CHỌN  Rabin–Karp: đơn giản, dễ mở rộng (nhiều pattern). KMP: bảo đảm worst-case.
```

## Nguồn

- **Skiena, Steven S. — *The Algorithm Design Manual*, 3rd ed.** (Springer, 2020) — **§6.7 Efficient String Matching** (trong Chapter 6: Hashing and Randomized Algorithms): bài toán substring search, khớp ngây thơ O(nm), Rabin–Karp (băm lăn, xác minh, randomized). `tai_lieu/The Algorithm Design Manual 3rd Edition...pdf` (offset **PDF = tr. + 15** ở Ch6).
- **Cormen, Leiserson, Rivest, Stein — *Introduction to Algorithms*, 4th ed. (CLRS), Chapter 32: String Matching** — nguồn tra cứu chuẩn cho **KMP** (§32.4, hàm tiền tố / prefix function) và Rabin–Karp (§32.2). *(Bản PDF trong `tai_lieu/` lỗi phông khi trích text nên không trích nguyên văn — xem hộp lưu ý đầu bài.)*
- Liên hệ: [Bài 3 — bảng băm](bai_03_bang-bam.md) (Rabin–Karp dùng băm + va chạm); [Bài 14 — thuật toán ngẫu nhiên](bai_14_ngau-nhien.md) (Rabin–Karp là ca randomized).

---

**Bản đồ khoá học:** [Bài 0 — Thuật toán & tính đúng](bai_00_thuat-toan-la-gi.md) · [Bài 1 — Phân tích Big-O](bai_01_big-o.md) · [Bài 2 — CTDL tuyến tính](bai_02_ctdl-tuyen-tinh.md) · [Bài 3 — Từ điển & bảng băm](bai_03_bang-bam.md) · [Bài 4 — Heap & cây tìm kiếm](bai_04_heap-cay-tim-kiem.md) · [Bài 5 — Sắp xếp](bai_05_sap-xep.md) · [Bài 6 — Chia để trị & đệ quy](bai_06_chia-de-tri.md) · [Bài 7 — Đồ thị: duyệt](bai_07_do-thi-duyet.md) · [Bài 8 — Đồ thị trọng số](bai_08_do-thi-trong-so.md) · [Bài 9 — Quy hoạch động](bai_09_quy-hoach-dong.md) · [Bài 10 — Backtracking](bai_10_backtracking.md) · [Bài 11 — NP-đầy đủ](bai_11_np-day-du.md) · **[Bài 12 — Khớp chuỗi] ← bạn đang ở đây** · [Bài 13 — Luồng mạng](bai_13_luong-mang.md) · [Bài 14 — Thuật toán ngẫu nhiên](bai_14_ngau-nhien.md)

Xem thêm [README khoá học](../README.md).
