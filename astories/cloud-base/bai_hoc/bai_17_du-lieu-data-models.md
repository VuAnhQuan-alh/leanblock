# Bài 17 — Dữ liệu nâng cao: Data models (quan hệ, document, graph)

> [!info] Về bài này
> **Chuyên đề mở rộng của trụ 4 (Dữ liệu).** [Bài 10](bai_10_du-lieu-storage.md) hỏi database *lưu* dữ liệu trên đĩa ra sao (B-tree/LSM); bài này hỏi tầng trên: *tổ chức* dữ liệu theo **mô hình** nào — quan hệ (bảng), document (lồng nhau), hay graph (đồ thị). Chọn mô hình = chọn kiểu *quan hệ* mình tối ưu, và nó quyết định **RDS vs DynamoDB vs Neptune**, cùng với "single-table design" của DynamoDB ở `aws-fund`.
> Nguồn: **DDIA** — ch. 2 (Data Models and Query Languages).
> **Trích:** `DDIA (tr. X)` = trang **in**; **offset PDF = tr. + 22**. Câu chốt nguyên văn trong `[!quote]`.
> **Chạy demo:** cần **Node 22.6+** (chạy thẳng `.ts`).
> Nên đọc trước: [Bài 10 — storage engine](bai_10_du-lieu-storage.md).

## Mục lục

1. [Mô hình quan hệ: bảng và hàng](#1-mô-hình-quan-hệ-bảng-và-hàng)
2. [Impedance mismatch và mô hình document](#2-impedance-mismatch-và-mô-hình-document)
3. [Graph: khi nhiều-nhiều trở nên phức tạp](#3-graph-khi-nhiều-nhiều-trở-nên-phức-tạp)
4. [Demo: cùng dữ liệu, ba mô hình](#4-demo-cùng-dữ-liệu-ba-mô-hình)
5. [Bảng so sánh: relational vs document vs graph](#5-bảng-so-sánh-relational-vs-document-vs-graph)
6. [Nối về AWS](#6-nối-về-aws)
7. [Thẻ ôn (active recall)](#7-thẻ-ôn-active-recall)
8. [Câu hỏi tự kiểm tra](#8-câu-hỏi-tự-kiểm-tra)
9. [Tóm tắt một trang](#tóm-tắt-một-trang)
10. [Nguồn](#nguồn)

---

## 1. Mô hình quan hệ: bảng và hàng

Mô hình thống trị suốt 50 năm, và vẫn là mặc định đúng cho hầu hết ứng dụng:

> [!quote] DDIA (tr. 28)
> "The best-known data model today is probably that of SQL, based on the relational model proposed by Edgar Codd in 1970 [...] data is organized into relations (called tables in SQL), where each relation is an unordered collection of tuples (rows in SQL)."
>
> *Mô hình dữ liệu nổi tiếng nhất hiện nay có lẽ là của SQL, dựa trên **mô hình quan hệ** do Edgar Codd đề xuất năm 1970: **dữ liệu được tổ chức thành các relation (gọi là bảng trong SQL), mỗi relation là một tập hợp không thứ tự các tuple (hàng)**.*

Sức mạnh của mô hình quan hệ nằm ở **join** và các quan hệ *nhiều-về-một* / *nhiều-nhiều*: dữ liệu được *chuẩn hoá* (normalize) — mỗi sự thật lưu một chỗ, tham chiếu bằng khoá — rồi *ghép lại* khi truy vấn. Nhưng chính việc "xé nhỏ ra nhiều bảng" lại gây một khó chịu khi code ứng dụng muốn một *đối tượng* trọn vẹn.

## 2. Impedance mismatch và mô hình document

Code hướng đối tượng làm việc với các đối tượng lồng nhau; database quan hệ làm việc với bảng phẳng. Hai thế giới lệch pha nhau:

> [!quote] DDIA (tr. 29)
> "The disconnect between the models is sometimes called an impedance mismatch."
>
> *Sự lệch pha giữa hai mô hình (đối tượng trong code vs bảng/hàng/cột trong DB) đôi khi gọi là **impedance mismatch** (lệch trở kháng).*

Mô hình **document** (JSON lồng nhau — như MongoDB, hay item của DynamoDB) xoá đi sự lệch pha đó cho dữ liệu *dạng cây*. DDIA tóm gọn đánh đổi giữa hai mô hình trong một câu vàng:

> [!quote] DDIA (tr. 38)
> "The main arguments in favor of the document data model are schema flexibility, better performance due to locality, and that for some applications it is closer to the data structures used by the application. The relational model counters by providing better support for joins, and many-to-one and many-to-many relationships."
>
> *Các lập luận chính ủng hộ mô hình **document** là **schema linh hoạt, hiệu năng tốt hơn nhờ locality, và gần với cấu trúc dữ liệu của ứng dụng** hơn. Mô hình **quan hệ** đáp trả bằng việc **hỗ trợ join tốt hơn, và các quan hệ nhiều-về-một và nhiều-nhiều**.*

Chữ "locality" nối thẳng Bài 10/12: một document là một khối liền — đọc *một phát* lấy cả cây (hồ sơ + mọi vị trí việc làm), không phải join nhiều bảng. Đó là lợi thế của document cho dữ liệu *một-nhiều* (tree). Cái giá: khi dữ liệu có nhiều *nhiều-nhiều* hoặc cần join phức tạp, document đuối — và nếu còn phức tạp hơn nữa, cả hai mô hình đều đuối.

## 3. Graph: khi nhiều-nhiều trở nên phức tạp

> [!quote] DDIA (tr. 49)
> "But what if many-to-many relationships are very common in your data? The relational model can handle simple cases of many-to-many relationships, but as the connections within your data become more complex, it becomes more natural to start modeling your data as a graph."
>
> *Nhưng nếu quan hệ **nhiều-nhiều rất phổ biến** trong dữ liệu thì sao? Mô hình quan hệ xử lý được các ca nhiều-nhiều đơn giản, nhưng khi **các kết nối trong dữ liệu càng phức tạp**, việc **mô hình hoá dữ liệu thành một graph** càng trở nên tự nhiên hơn.*

Graph gồm **vertex** (đỉnh — người, địa điểm) và **edge** (cạnh — quan hệ). Nó toả sáng ở các truy vấn "đi theo quan hệ nhiều bước": bạn bè của bạn bè, đường đi, "ai từng làm chung công ty". Thử làm những truy vấn này trong SQL thì phải *join đệ quy* dài dòng; trong graph chúng là *duyệt cạnh* tự nhiên. Ba mô hình không xếp hạng hơn-kém — chúng tối ưu cho ba *hình dạng quan hệ* khác nhau. Demo mục 4 cho thấy cùng một dữ liệu hành xử ra sao trong cả ba.

## 4. Demo: cùng dữ liệu, ba mô hình

Hồ sơ Alice với nhiều vị trí việc làm. (1) Document: đọc một phát (locality). (2) Relational: join nhiều bảng (đếm số truy cập). (3) Graph: tìm "đồng nghiệp" (nhiều-nhiều qua công ty chung) bằng duyệt cạnh.

```typescript
// Data models: cùng một dữ liệu, ba cách mô hình — mỗi cách mạnh ở một kiểu
// quan hệ. Document: cây 1-nhiều, đọc 1 phát (locality). Relational: nhiều-về-
// một + join. Graph: nhiều-nhiều phức tạp, duyệt cạnh.
type Pos = { org: string; title: string };

// ---- (1) DOCUMENT: hồ sơ lồng nhau → MỘT lần đọc lấy hết (locality, tr.38) ----
const doc = { name: "Alice", positions: [{ org: "AWS", title: "SWE" }, { org: "Google", title: "SRE" }] };
let docReads = 0;
function getResumeDoc(): typeof doc { docReads++; return doc; }     // 1 truy cập
const r = getResumeDoc();
console.log(`(1) DOCUMENT: đọc ${docReads} lần → ${r.name}: ${r.positions.map(p => p.org).join(", ")}`);

// ---- (2) RELATIONAL: bảng rời, phải JOIN → nhiều truy cập ----
const users = [{ id: 1, name: "Alice" }, { id: 2, name: "Bob" }];
const positions = [{ uid: 1, org: "AWS", title: "SWE" }, { uid: 1, org: "Google", title: "SRE" },
                   { uid: 2, org: "AWS", title: "PM" }];
let relReads = 0;
function getResumeRel(uid: number): string {
  relReads++; const u = users.find(x => x.id === uid)!;            // quét bảng users
  const ps: Pos[] = [];
  for (const p of positions) { relReads++; if (p.uid === uid) ps.push(p); }  // quét positions
  return `${u.name}: ${ps.map(p => p.org).join(", ")}`;
}
console.log(`(2) RELATIONAL: ${getResumeRel(1)} — tốn ${relReads} truy cập (join)`);

// ---- (3) GRAPH: nhiều-nhiều "ai từng làm chung công ty" → duyệt cạnh (tr.49) ----
// cạnh người—(làm tại)—công ty; tìm đồng nghiệp của Alice = người nối cùng org
const worksAt: Array<[string, string]> = [["Alice","AWS"],["Alice","Google"],["Bob","AWS"],["Carol","Google"]];
function colleaguesOf(person: string): string[] {
  const orgs = new Set(worksAt.filter(([p]) => p === person).map(([, o]) => o));
  return [...new Set(worksAt.filter(([p, o]) => p !== person && orgs.has(o)).map(([p]) => p))];
}
console.log(`(3) GRAPH: đồng nghiệp của Alice = ${colleaguesOf("Alice").join(", ")} (qua org chung)`);
console.log("\nChọn model theo QUAN HỆ: 1-nhiều→document; nhiều-về-một→relational;");
console.log("nhiều-nhiều phức tạp→graph. Dùng sai model = join/duyệt đắt.");
```

Kết quả chạy thật *(tất định)*:

```
(1) DOCUMENT: đọc 1 lần → Alice: AWS, Google
(2) RELATIONAL: Alice: AWS, Google — tốn 4 truy cập (join)
(3) GRAPH: đồng nghiệp của Alice = Bob, Carol (qua org chung)

Chọn model theo QUAN HỆ: 1-nhiều→document; nhiều-về-một→relational;
nhiều-nhiều phức tạp→graph. Dùng sai model = join/duyệt đắt.
```

Cùng một "Alice: AWS, Google", nhưng: document lấy *một* lần đọc (cả cây nằm liền — locality); relational tốn *4* truy cập để quét và ghép hai bảng (join). Với dữ liệu cây một-nhiều, document thắng rõ. Nhưng câu hỏi (3) — "ai từng làm chung công ty" — là *nhiều-nhiều*: document phải nhân đôi dữ liệu hoặc quét toàn bộ; relational cần join bắc cầu; graph trả lời *tự nhiên* bằng duyệt cạnh. Bài học: **không có mô hình "tốt nhất", chỉ có mô hình hợp với *hình dạng quan hệ* và *mẫu truy vấn* của bạn** — đúng tinh thần "chọn index theo mẫu truy vấn" của Bài 10, nâng lên mức mô hình.

> [!note] Tự thử
> - Thêm 100.000 user vào mảng `positions` rồi đo `relReads`: join quét tuyến tính phình to (vì sao relational cần *index* trên `uid` — Bài 10). Document không tốn vì đã lồng sẵn.
> - Thử truy vấn "tất cả người từng làm ở AWS" trên document: bạn phải quét *mọi* document (dữ liệu bị khoá theo người, không theo công ty) — minh hoạ "document khoá bạn vào một mẫu truy vấn".
> - Mở rộng graph: "đồng nghiệp của đồng nghiệp" (hai bước) — tầm thường với duyệt cạnh, nhưng là join đệ quy khổ sở trong SQL.

## 5. Bảng so sánh: relational vs document vs graph

| Tiêu chí              | Relational (SQL)            | Document (JSON lồng)            | Graph                            |
| :-------------------- | :-------------------------- | :----------------------------- | :------------------------------- |
| Mạnh ở quan hệ        | nhiều-về-một, nhiều-nhiều (join) | **một-nhiều** (cây), locality | **nhiều-nhiều phức tạp** (duyệt) |
| Schema                | chặt (schema-on-write)      | linh hoạt (schema-on-read)     | linh hoạt                        |
| Đọc một thực thể      | join nhiều bảng             | **một lần đọc** (cả cây)       | duyệt từ đỉnh                    |
| Điểm yếu              | impedance mismatch; cứng    | nhiều-nhiều & join phức tạp đuối | ít phổ biến, học khó hơn         |
| Nền / AWS             | **RDS / Aurora**            | **DynamoDB** (item), DocumentDB | **Neptune**                     |

Quy luật chọn: **hỏi "dữ liệu của tôi chủ yếu là quan hệ hình dạng nào, và tôi sẽ truy vấn ra sao?"** Cây một-nhiều, đọc theo một thực thể → document (DynamoDB). Nhiều quan hệ chéo, truy vấn linh hoạt ad-hoc → relational (RDS). Mạng lưới kết nối nhiều bước → graph (Neptune). Chọn sai không phải "không chạy" mà là *mọi truy vấn đều đắt* — join/duyệt/nhân bản dữ liệu mãi mãi.

## 6. Nối về AWS

> [!note] Nối về AWS
> Chọn database trên AWS *là* chọn data model — xem [`aws-fund` Bài 3 — Database & Storage](../../aws-fund/bai_hoc/bai_03_database-storage.md):
> - **RDS/Aurora = relational.** Mặc định đúng khi dữ liệu có nhiều quan hệ chéo và bạn cần truy vấn *ad-hoc* (chưa biết trước sẽ hỏi gì) — join + SQL linh hoạt là thế mạnh của mục 1.
> - **DynamoDB = document/key-value.** Mỗi item là một document lồng được → locality (mục 2): đọc một phát lấy cả cây. Nhưng điều này ép **"single-table design" và "thiết kế từ access pattern trước"**: vì DynamoDB *không join tốt*, bạn phải biết trước sẽ truy vấn thế nào rồi mô hình dữ liệu *theo câu hỏi*, không theo chuẩn hoá. Đây là lý do thiết kế DynamoDB "ngược" với RDS.
> - **Neptune = graph.** Cho mạng xã hội, đồ thị tri thức, phát hiện gian lận ("tài khoản nào nối với tài khoản xấu qua mấy bước") — đúng "nhiều-nhiều phức tạp" của mục 3.
> - **Hệ quả chi phí:** dùng DynamoDB cho dữ liệu nhiều-nhiều (bắt chước join bằng nhiều lần query) hay dùng RDS cho cây đọc-một-thực-thể (join thừa) đều là *dùng sai hình dạng* — đắt và phức tạp không cần thiết. Mô hình nên theo quan hệ, không theo thói quen.

## 7. Thẻ ôn (active recall)

> [!question] Thẻ 17.1 — Mô hình quan hệ tổ chức dữ liệu thế nào? Mạnh ở đâu?
> **Đáp:** dữ liệu thành **relation (bảng)**, mỗi relation là tập không thứ tự các **tuple (hàng)**. Mạnh ở **join** và quan hệ nhiều-về-một / nhiều-nhiều.

> [!question] Thẻ 17.2 — "Impedance mismatch" là gì? Document giải nó cho dữ liệu nào?
> **Đáp:** lệch pha giữa đối tượng lồng nhau trong code và bảng phẳng trong DB. Document (JSON lồng) xoá nó cho dữ liệu **dạng cây (một-nhiều)**.

> [!question] Thẻ 17.3 — Ba lợi thế của document? Relational đáp trả bằng gì?
> **Đáp:** document: schema linh hoạt, hiệu năng nhờ **locality**, gần cấu trúc ứng dụng. Relational: join tốt hơn + quan hệ nhiều-về-một và nhiều-nhiều.

> [!question] Thẻ 17.4 — Khi nào graph tự nhiên hơn relational?
> **Đáp:** khi quan hệ **nhiều-nhiều rất phổ biến và phức tạp** (kết nối nhiều bước). SQL phải join đệ quy; graph là duyệt cạnh.

> [!question] Thẻ 17.5 — Trong demo, vì sao document đọc 1 lần mà relational tốn 4?
> **Đáp:** document lồng sẵn cả cây (locality) → một read. Relational tách bảng users/positions → phải quét + join để ghép lại.

> [!question] Thẻ 17.6 — Vì sao DynamoDB ép "single-table / access-pattern-first"?
> **Đáp:** DynamoDB là document/key-value, **không join tốt** → phải biết trước mẫu truy vấn và mô hình dữ liệu *theo câu hỏi*, không theo chuẩn hoá như RDS.

## 8. Câu hỏi tự kiểm tra

1. Mô hình quan hệ tổ chức dữ liệu ra sao? Thế mạnh cốt lõi? *(mục 1, tr. 28)*
2. Impedance mismatch là gì? Document giải quyết cho loại dữ liệu nào? *(mục 2, tr. 29)*
3. Nêu ba lợi thế document và phản biện của relational. "Locality" nối về bài nào? *(mục 2, tr. 38)*
4. Khi nào nên dùng graph? Cho một truy vấn graph làm tốt mà SQL vất vả. *(mục 3, tr. 49)*
5. Chạy demo mục 4. Giải thích chênh lệch số truy cập document vs relational, và vì sao graph hợp câu (3). *(mục 4)*
6. Ánh xạ RDS / DynamoDB / Neptune vào ba mô hình. Vì sao thiết kế DynamoDB "ngược" RDS? *(mục 5–6)*

## Tóm tắt một trang

```
BÀI 17 — DỮ LIỆU NÂNG CAO: DATA MODELS (quan hệ · document · graph)
─────────────────────────────────────────────────────────
QUAN HỆ (SQL)  dữ liệu thành bảng, mỗi bảng = tập không thứ tự các hàng
   (DDIA tr.28). Mạnh: JOIN + nhiều-về-một/nhiều-nhiều. Chuẩn hoá + ghép.

IMPEDANCE MISMATCH  lệch pha đối-tượng(code) vs bảng(DB) (tr.29). DOCUMENT
   (JSON lồng) xoá nó cho dữ liệu CÂY. Lợi thế: schema linh hoạt + LOCALITY
   + gần cấu trúc app (tr.38). Relational đáp: join + nhiều-nhiều.

GRAPH  khi nhiều-nhiều RẤT phổ biến & phức tạp → mô hình graph tự nhiên
   hơn (tr.49). Vertex+edge; truy vấn nhiều-bước = duyệt cạnh (SQL phải join
   đệ quy).

DEMO  cùng "Alice: AWS,Google": document 1 read (locality) vs relational 4
   truy cập (join). "Đồng nghiệp qua org chung" = nhiều-nhiều → graph tự nhiên.

QUY LUẬT  chọn theo HÌNH DẠNG quan hệ + mẫu truy vấn, không có "tốt nhất".
   Dùng sai = mọi truy vấn đắt (như chọn index sai, Bài 10).

NỐI VỀ AWS  RDS/Aurora=relational (ad-hoc, join); DynamoDB=document (locality
   → single-table, access-pattern-first, KHÔNG join); Neptune=graph.
```

## Nguồn

- **Martin Kleppmann**, *Designing Data-Intensive Applications* (O'Reilly, 2017) — **ch. 2 (Data Models and Query Languages)**: mô hình quan hệ (tr. 28), impedance mismatch (tr. 29), document vs relational (tr. 38), graph khi nhiều-nhiều phức tạp (tr. 49). Offset **PDF = tr. + 22**.
- Nối về AWS: [`aws-fund` Bài 3 — Database & Storage](../../aws-fund/bai_hoc/bai_03_database-storage.md) (RDS, DynamoDB, Neptune).
- Mở rộng của [Bài 10 — storage engine](bai_10_du-lieu-storage.md) (mô hình ở tầng trên engine lưu trữ).

---

**Bản đồ khoá học — lõi:** [Bài 0 — Vì sao cần nền](bai_00_vi-sao-nen-tang.md) · [Bài 1 — OS: ảo hoá](bai_01_os-ao-hoa.md) · [Bài 2 — OS: concurrency](bai_02_os-concurrency.md) · [Bài 3 — OS: lưu trữ](bai_03_os-luu-tru.md) · [Bài 4 — Mạng: phân tầng, HTTP, DNS](bai_04_mang-http-dns.md) · [Bài 5 — Mạng: TCP, TLS](bai_05_mang-tcp-tls.md) · [Bài 6 — Mạng: hiệu năng, CDN](bai_06_mang-hieu-nang.md) · [Bài 7 — Distributed: giao tiếp & thất bại](bai_07_dist-giao-tiep.md) · [Bài 8 — Distributed: nhân bản & nhất quán](bai_08_dist-nhat-quan.md) · [Bài 9 — Distributed: phân mảnh & consensus](bai_09_dist-phan-manh.md) · [Bài 10 — Dữ liệu: storage engine](bai_10_du-lieu-storage.md) · [Bài 11 — Dữ liệu: batch & stream](bai_11_du-lieu-batch-stream.md)

**Chuyên đề nâng cao:** [Bài 12 — OS nâng cao: bộ nhớ ảo](bai_12_os-bo-nho-ao.md) · [Bài 13 — OS nâng cao: scheduling & locks](bai_13_os-scheduling-locks.md) · [Bài 14 — Mạng nâng cao: bảo mật & mật mã](bai_14_mang-bao-mat.md) · [Bài 15 — Distributed nâng cao: đồng hồ](bai_15_dist-dong-ho.md) · [Bài 16 — Distributed nâng cao: transaction & saga](bai_16_dist-transaction-saga.md) · **[Bài 17 — Dữ liệu nâng cao: data models] ← bạn đang ở đây** · [Bài 18 — Dữ liệu nâng cao: encoding & schema](bai_18_du-lieu-encoding.md)

Xem thêm [README khoá học](../README.md).
