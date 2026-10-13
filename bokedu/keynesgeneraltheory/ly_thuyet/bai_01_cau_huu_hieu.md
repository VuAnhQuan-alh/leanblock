# Bài 1 — Cầu hữu hiệu: cú lật đổ "cung tự tạo cầu"

> [!info] Về bài này
> Dựng từ **Quyển I — Dẫn nhập** (*Chương 1–3*) của *The General Theory* (Keynes, 1936). Đây
> là **trái tim** của cả cuốn sách: Keynes tháo một định đề cột trụ của kinh tế học cổ điển và
> **Định luật Say**, rồi đặt vào chỗ đó một ý tưởng mới — **nguyên lý cầu hữu hiệu**.
>
> Bài này thuộc **Vòng 1 (học kỹ)**. Nếu chỉ đọc một bài của khoá, hãy đọc bài này. Mọi câu trích
> in nguyên văn tiếng Anh kèm **bản dịch của người soạn**; ví dụ *(số giả định)* là số tự dựng để
> tập tính, đã tính lại bằng Python.
>
> **Cần đọc trước:** [Bài 0 — Nhập môn](bai_00_nhap_mon.md) (bối cảnh 1936, "kinh tế học cổ điển"
> là gì, ba giả định của nó).

---

## Mục lục

<!-- MUC-LUC -->

- [Mở đầu: nhà máy đóng cửa, mà người vẫn thèm hàng](#mở-đầu-nhà-máy-đóng-cửa-mà-người-vẫn-thèm-hàng)
- [1. Hai định đề của kinh tế học cổ điển](#1-hai-định-đề-của-kinh-tế-học-cổ-điển)
- [2. Ba loại thất nghiệp — và loại thứ ba bị chối bỏ](#2-ba-loại-thất-nghiệp--và-loại-thứ-ba-bị-chối-bỏ)
- [3. Cú đánh thứ nhất: giảm lương không phải liều thuốc](#3-cú-đánh-thứ-nhất-giảm-lương-không-phải-liều-thuốc)
- [4. Cú đánh thứ hai: "cung tự tạo cầu" là một ảo giác](#4-cú-đánh-thứ-hai-cung-tự-tạo-cầu-là-một-ảo-giác)
- [5. Lời giải: nguyên lý cầu hữu hiệu (D và Z)](#5-lời-giải-nguyên-lý-cầu-hữu-hiệu-d-và-z)
- [6. Nghịch lý nghèo giữa cảnh thừa mứa](#6-nghịch-lý-nghèo-giữa-cảnh-thừa-mứa)
- [7. Vì sao một ý tưởng sai lại thắng: Ricardo và Malthus](#7-vì-sao-một-ý-tưởng-sai-lại-thắng-ricardo-và-malthus)
- [8. Phản biện & hậu Keynes](#8-phản-biện--hậu-keynes)
- [9. Đối chiếu 2026](#9-đối-chiếu-2026)
- [10. Nối môn đang học](#10-nối-môn-đang-học)
- [11. Từ điển thuật ngữ](#11-từ-điển-thuật-ngữ)
- [12. Câu hỏi tự kiểm tra](#12-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## Mở đầu: nhà máy đóng cửa, mà người vẫn thèm hàng

Năm 1932, giữa Đại khủng hoảng, nhà máy dệt Mỹ **đóng cửa**, công nhân dệt **thất nghiệp** — trong
khi chính họ **thiếu quần áo**. Có người muốn làm, có người muốn mua, máy vẫn nằm im. Cái gì chặn
giữa hai bên?

Kinh tế học cổ điển có sẵn câu trả lời: *tại người lao động đòi lương cao quá* — cứ hạ lương, chủ
sẽ thuê lại. Keynes bảo câu trả lời này **không khớp với kinh nghiệm**.

> [!quote] Thực tế 1932 không ăn khớp lý thuyết cổ điển — QI, Ch 2
> *"It is not very plausible to assert that unemployment in the United States in 1932 was due
> either to labour obstinately refusing to accept a reduction of money-wages or to its obstinately
> demanding a real wage beyond what the productivity of the economic machine was capable of
> furnishing."*
>
> "Thật khó tin nổi khi khẳng định rằng nạn thất nghiệp ở Mỹ năm 1932 là do người lao động
> **ngoan cố không chịu giảm lương danh nghĩa**, hoặc ngoan cố đòi một mức **lương thực** cao hơn
> cái mà cỗ máy kinh tế có thể trả nổi." (QI, Ch 2)

Người lao động *"is not more truculent in the depression than in the boom"* — không hung hăng hơn
trong suy thoái so với lúc bùng nổ (QI, Ch 2). Chương 1 dài đúng một đoạn, đặt luận đề cho cả cuốn:
các định đề cổ điển *"are applicable to a special case only and not to the general case"* (QI, Ch 1)
— chữ *General* trong tên sách nghĩa là thế. Mạch bài: phái cổ điển **tựa vào cái gì** (§1–§2), hai
cú đánh (§3–§4), lời giải (§5), và vì sao lời giải cho ra thất nghiệp (§6).

---

## 1. Hai định đề của kinh tế học cổ điển

> [!example] Góc đời sống — quán bún thuê người thứ năm
> Quán bún của cô Hoa có một nồi nước dùng, sáu cái bàn. Người phụ thứ nhất giúp bán gấp đôi; tới
> người thứ năm thì cả bọn **chen nhau** trong bếp chật — thêm người chỉ thêm chút ít bát bún. Cô
> chỉ thuê thêm khi phần bát bún người mới làm ra **còn đáng** đồng lương: **định đề thứ nhất**.
> Còn người được mời thì cân nhắc tiền công có **bõ** cái nóng của bếp không: **định đề thứ hai**.

**Keynes nói gì.** Lý thuyết việc làm cổ điển, *"supposedly simple and obvious"*, đứng trên hai định
đề hầu như không ai bàn (QI, Ch 2):

- **Định đề I:** *"The wage is equal to the marginal product of labour"* — tiền công bằng **sản
  phẩm biên**, giá trị *"which would be lost if employment were to be reduced by one unit"* (QI, Ch 2).
- **Định đề II:** *"The utility of the wage when a given volume of labour is employed is equal to the
  marginal disutility of that amount of employment"* — **độ thoả dụng** của tiền công bằng **nỗi
  khổ nhọc biên**: lương thực vừa đủ để lượng lao động đang dùng chịu ra làm (QI, Ch 2).

Định đề I cho **đường cầu** lao động, định đề II cho **đường cung**; việc làm chốt ở chỗ hai đường
gặp nhau. Từ đó chỉ có **bốn cách** tăng việc làm: bớt cọ xát; chịu lương thực thấp hơn; tăng năng
suất trong ngành làm ra **hàng tiền công** (*wage-goods* — chữ của Pigou: hàng mà giá của nó quyết
định sức mua của tiền lương, như gạo, vải); hoặc dịch chi tiêu sang hàng khác. Đó là *Theory of
Unemployment* (1933) của **Arthur Pigou** — *"the only detailed account of the classical theory of
employment which exists"* (QI, Ch 2). Không cách nào là "tăng tổng cầu".

Keynes tuyên bố *"we shall maintain the first postulate as heretofore"* (QI, Ch 2), rồi nói rõ điều đó
kéo theo gì:

> [!quote] Keynes giữ định đề thứ nhất — QI, Ch 2
> *"Thus I am not disputing this vital fact which the classical economists have (rightly) asserted
> as indefeasible. In a given state of organisation, equipment and technique, the real wage earned
> by a unit of labour has a unique (inverse) correlation with the volume of employment. Thus if
> employment increases, then, in the short period, the reward per unit of labour in terms of
> wage-goods must, in general, decline and profits increase."*
>
> "Vậy tôi **không** bác bỏ sự thật hệ trọng mà các nhà kinh tế cổ điển đã (đúng đắn) khẳng định là
> không thể chối. Với tổ chức, thiết bị và kỹ thuật cho trước, lương thực của một đơn vị lao động có
> **tương quan duy nhất (nghịch)** với khối lượng việc làm. Việc làm tăng thì, trong ngắn hạn, phần
> trả tính bằng hàng tiền công nói chung phải **giảm**, còn lợi nhuận **tăng**." (QI, Ch 2)

**Định nghĩa.** **Nỗi khổ nhọc biên** (*marginal disutility*) hiểu rộng: *"every kind of reason which
might lead a man, or a body of men, to withhold their labour"* (QI, Ch 2). **Lương danh nghĩa**
(*money-wage*) là số tiền trên phiếu lương; **lương thực** (*real wage*) là số hàng tiền công nó mua
được. Định đề I (phía **cầu**) Keynes **giữ**; định đề II (phía **cung**) ông **bỏ**.

**Chuỗi lập luận.**

1. **Ngắn hạn, máy móc cố định**: thêm người thì sản phẩm biên giảm — *"decreasing returns in the
   short period"* (QI, Ch 2).
2. **Định đề I**: chủ thuê tới khi lương thực = sản phẩm biên, nên việc làm cao **đi kèm** lương
   thực thấp (QI, Ch 2).
3. **Định đề II** thêm vế cung; nếu cả hai đúng, ai không có việc là vì không chịu mức trả ấy.
4. **Keynes giữ bước 1–2, bỏ bước 3.** Việc làm thấp vẫn **đi kèm** lương thực cao, nhưng *"is not
   necessarily due to labour's demanding a larger quantity of wage-goods"* (QI, Ch 2). Cái gì quyết
   định việc làm thì §5 trả lời.

**Ví dụ số** *(số giả định)*. 100 nghìn người muốn làm ở mức lương hiện hành; đo bằng "giỏ hàng
tiền công"/người/ngày:

| Việc làm N (nghìn người) | 70 | 80 | 90 | 100 |
| --- | ---: | ---: | ---: | ---: |
| Sản phẩm biên (định đề I) | 11 | 10 | 9 | 8 |
| Nỗi khổ nhọc biên (định đề II) | 5 | 6 | 7 | 8 |
| Chênh lệch | 6 | 4 | 2 | **0** |

Phái cổ điển: hai hàng gặp nhau ở **N = 100**, lương thực 8 giỏ — toàn dụng. Keynes giữ hàng đầu:
nếu vì lý do nào đó việc làm chỉ ở **80**, lương thực là **10** giỏ — **cao hơn** nỗi khổ nhọc biên 6
giỏ; lương thực cao là **hệ quả** của việc làm thấp. "Lý do nào đó" là §5–§6.

> [!warning] Keynes GIỮ định đề I, BỎ định đề II
> Ông nhận "sự thật hệ trọng" việc làm tăng thì lương thực giảm (QI, Ch 2). Thứ ông bỏ là ý rằng lương thực
> **luôn** khớp nỗi khổ nhọc biên. (Sau 1936, chính "việc làm tăng thì lương thực giảm" bị số liệu
> thách thức — §8.)

---

## 2. Ba loại thất nghiệp — và loại thứ ba bị chối bỏ

> [!example] Góc đời sống — phép thử "giá chợ nhích lên một chút"
> Anh Sơn thợ hồ nghỉ việc ba tháng nay — tự nguyện, hay muốn làm mà không có việc? Hỏi thẳng thì
> ai cũng bảo "muốn làm". Keynes đề nghị một **phép thử tưởng tượng**: giữ công **300 nghìn/ngày**,
> cho giá chợ **nhích lên một chút**. Nếu anh **vẫn** nhận làm ở 300 nghìn, và chủ thầu **lại muốn**
> thuê thêm (lương thực họ trả rẻ đi), thì cái thiếu không ở lương — anh là **thất nghiệp không tự
> nguyện**.

**Keynes nói gì.** Định đề II dung được hai loại thất nghiệp: **cọ xát** (*frictional* — tính sai,
độ trễ, người *"between jobs"*) và **tự nguyện** (*voluntary* — không nhận mức trả tương ứng năng
suất biên do luật lệ, tập quán, thương lượng tập thể, chậm thích nghi hay *"mere human obstinacy"*).
*"But these two categories … are comprehensive"*: loại thứ ba **không có chỗ** (QI, Ch 2). Keynes loại
trước cái **không** tính: sức làm còn thừa (*"An eight-hour day does not constitute unemployment
because it is not beyond human capacity to work ten hours"*), và nhóm người tự rút lao động vì không
chịu dưới một mức trả thực nào đó (QI, Ch 2). Rồi:

> [!quote] Định nghĩa thất nghiệp không tự nguyện — QI, Ch 2
> *"Men are involuntarily unemployed if, in the event of a small rise in the price of wage-goods
> relatively to the money-wage, both the aggregate supply of labour willing to work for the
> current money-wage and the aggregate demand for it at that wage would be greater than the
> existing volume of employment."*
>
> "Người ta **thất nghiệp không tự nguyện** nếu, khi giá hàng tiền công nhích lên một chút so với
> lương danh nghĩa, thì **cả** tổng cung lao động sẵn lòng làm ở mức lương danh nghĩa hiện hành
> **lẫn** tổng cầu lao động ở mức lương đó đều sẽ **lớn hơn** khối lượng việc làm hiện có." (QI,
> Ch 2)

**Định nghĩa.** Có thất nghiệp không tự nguyện khi một **cú giảm nhẹ lương thực qua giá** (lương
danh nghĩa giữ nguyên) làm **cả** người muốn làm **lẫn** chỗ chủ muốn thuê đều **vượt** số việc làm
hiện tại. **Toàn dụng** (*full employment*) là khi **không** có loại này; cọ xát và tự nguyện vẫn có
thể tồn tại: *"both 'frictional' and 'voluntary' unemployment being consistent with 'full' employment
thus defined"* (QI, Ch 2). Dễ lẫn: thất nghiệp **tự nguyện** là không chịu mức trả hiện hành; **không
tự nguyện** là chịu mà không có chỗ.

**Chuỗi lập luận.**

1. **Định đề II**: lương thực luôn bằng nỗi khổ nhọc biên, nên ai không làm là tự nguyện (QI, Ch 2).
2. **Phép thử**: hạ nhẹ lương thực **bằng giá**, giữ lương danh nghĩa. Nếu định đề II đúng, người
   muốn làm phải **ít đi**.
3. **Nếu không ít đi** — và chủ muốn thuê **thêm** (định đề I) — thì có người muốn làm mà **tiền
   công** không phải vật cản.
4. **Hệ quả:** định đề II đúng ⇔ không có thất nghiệp không tự nguyện ⇔ toàn dụng. Lý thuyết cổ điển
   *"is best regarded as a theory of distribution in conditions of full employment"* (QI, Ch 2); áp
   nó vào thất nghiệp là sai chỗ.

**Ví dụ số** *(số giả định)*. Đang có **80** nghìn người làm, lương **200 nghìn/ngày**. Giá hàng tiền
công tăng **2%**, lương tiền giữ nguyên: lương thực = 200 ÷ 1,02 = **196,08** nghìn, giảm ≈ **1,96%**.

| Kịch bản | Cung LĐ ở 200 nghìn | Cầu LĐ ở 200 nghìn | Kết luận |
| --- | ---: | ---: | --- |
| A — người lao động mặc cả theo **lương danh nghĩa** (Keynes: trường hợp thường gặp) | 100 | 85 | cả hai > 80 → **có** thất nghiệp không tự nguyện |
| B — cung lao động chỉ phụ thuộc **lương thực** (định đề II) | 79 | 85 | cung < 80 → **không** có |

Ở A, 80 không phải giới hạn do lương; ở B, giá tăng 2% đã có người bỏ làm. Thế giới giống A hay B? §3.

> [!warning] Phép thử là thí nghiệm tư duy, không phải số liệu
> Định nghĩa là một phép thử **giả định** ("nếu giá nhích lên thì…"), không phải phát hiện thống kê
> về Đại khủng hoảng; bằng chứng Keynes đưa là **kinh nghiệm thông thường** (§3) và cảnh 1932. "Không
> tự nguyện" cũng không phải "không có gì để làm" mà là "muốn làm **ở mức lương hiện hành** mà không
> có chỗ".

Keynes ví cả trường phái bằng một hình ảnh sắc như dao:

> [!quote] Nhà hình học Euclid trong thế giới cong — QI, Ch 2
> *"The classical theorists resemble Euclidean geometers in a non-Euclidean world who, discovering
> that in experience straight lines apparently parallel often meet, rebuke the lines for not
> keeping straight… Yet, in truth, there is no remedy except to throw over the axiom of parallels
> and to work out a non-Euclidean geometry."*
>
> "Các nhà lý thuyết cổ điển giống những nhà hình học Euclid lạc vào một thế giới phi Euclid: thấy
> trong thực tế hai đường thẳng tưởng song song lại cứ cắt nhau, họ bèn **mắng những đường thẳng sao
> không chịu thẳng**… Nhưng thật ra không có cách chữa nào khác ngoài **vứt bỏ tiên đề đường song
> song** và dựng một nền hình học phi Euclid." (QI, Ch 2)

"Mắng đường thẳng" là trách người lao động bướng; tiên đề phải vứt: *"the second postulate of the
classical doctrine"* (QI, Ch 2).

---

## 3. Cú đánh thứ nhất: giảm lương không phải liều thuốc

> [!example] Góc đời sống — hai tổ may, hai kiểu "mất lương"
> Tổ cắt và tổ may đều nhận 200 nghìn/ngày. Chủ đề nghị **riêng tổ cắt** nhận 180 nghìn: tổ cắt phản
> đối kịch liệt — vì từ nay họ **thua** tổ may. Năm sau giá tăng 10%, lương mọi người vẫn 200 nghìn,
> sức mua ai cũng còn khoảng 182 nghìn, nhưng **không tổ nào** đình công. Cái người lao động canh giữ
> là **vị trí tương đối**, không phải lương thực tuyệt đối.

**Keynes nói gì.** Phái cổ điển chữa thế bí: số người dư ra là do thoả thuận ngầm *"not to work for
less"*, nên thất nghiệp ấy *"though apparently involuntary, is not strictly so"* (QI, Ch 2). Keynes
đáp bằng **hai phản bác**; cái thứ nhất *"is not theoretically fundamental"*, cái thứ hai mới là nền
tảng (QI, Ch 2).

**Định nghĩa.** **Lương danh nghĩa** do mặc cả chủ–thợ quyết định; **lương thực chung** do *"certain
other forces"* của hệ thống quyết định (QI, Ch 2).

**Phản bác thứ nhất — người lao động thật sự cư xử thế nào.** Không chịu **giảm lương danh nghĩa**
không có nghĩa là sẽ rút lao động khi **giá tăng** làm lương thực giảm: *"the demand of labour is for
a minimum money-wage and not for a minimum real wage"* (QI, Ch 2).

Nếu cung lao động không phải hàm **chỉ** của lương thực, đường cung cổ điển *"will shift bodily with
every movement of prices"* và lý thuyết *"breaks down entirely"*; mà *"experience shows that this is
how labour in fact behaves"* (QI, Ch 2). Vì sao hành vi ấy không phi lý:

> [!quote] Đấu tranh lương danh nghĩa là để giữ lương tương đối — QI, Ch 2
> *"Since there is imperfect mobility of labour, and wages do not tend to an exact equality of net
> advantage in different occupations, any individual or group of individuals, who consent to a
> reduction of money-wages relatively to others, will suffer a relative reduction in real wages,
> which is a sufficient justification for them to resist it. On the other hand it would be
> impracticable to resist every reduction of real wages, due to a change in the purchasing-power of
> money which affects all workers alike; and in fact reductions of real wages arising in this way
> are not, as a rule, resisted unless they proceed to an extreme degree."*
>
> "Vì lao động không di chuyển hoàn hảo, ai hay nhóm nào **chịu giảm lương danh nghĩa so với người
> khác** sẽ bị giảm **lương thực tương đối** — lý do đủ để chống lại. Ngược lại, chống mọi lần giảm
> lương thực do **sức mua của đồng tiền** đổi — đụng tới **mọi** người như nhau — là bất khả thi; và
> thực tế những lần ấy thường **không bị chống**, trừ khi tới mức cực đoan." (QI, Ch 2)

Giằng co về lương tiền vì thế chủ yếu quyết định **cách chia** tổng lương thực giữa các nhóm, không
phải **mức trung bình**.

Người lao động *"are instinctively more reasonable economists than the classical school"*, vì *"no
trade union would dream of striking on every occasion of a rise in the cost of living"* (QI, Ch 2).

**Phản bác thứ hai — nền tảng: người lao động không quyết định được lương thực.**

> [!quote] Giả định lén lút — QI, Ch 2
> *"In assuming that the wage bargain determines the real wage the classical school have slipt in
> an illicit assumption. For there may be no method available to labour as a whole whereby it can
> bring the wage-goods equivalent of the general level of money wages into conformity with the
> marginal disutility of the current volume of employment. There may exist no expedient by which
> labour as a whole can reduce its real wage to a given figure by making revised money bargains
> with the entrepreneurs."*
>
> "Khi giả định **giao kèo tiền công quyết định lương thực**, phái cổ điển đã **lén cài một giả định
> không chính đáng**. Vì có thể **không có cách nào** để giới lao động, xét như tổng thể, đưa sức mua
> của mức lương chung về khớp nỗi khổ nhọc biên; không có phương kế nào để **cả giới lao động** hạ
> lương thực xuống một con số cho trước bằng cách mặc cả lại lương **tiền**." (QI, Ch 2)

Nó còn trái với chính lý thuyết cổ điển: giá theo chi phí biên, chủ yếu là tiền công, nên lương tiền
giảm kéo giá giảm theo, *"leaving the real wage and the level of unemployment practically the same as
before"* (QI, Ch 2).

**Chuỗi lập luận.**

1. **Định đề II cần** người lao động **tự đặt** được lương thực qua mặc cả lương tiền (QI, Ch 2).
2. **Phản bác 1 (hành vi):** họ đòi lương **danh nghĩa** tối thiểu — hợp lý, để giữ lương **tương
   đối** — nên lương thực hiện hành **không** đo đúng nỗi khổ nhọc biên (QI, Ch 2).
3. **Phản bác 2 (nền tảng):** mặc cả lương tiền có thể **không** điều khiển được lương thực chung, vì
   giá cả chạy theo (QI, Ch 2).
4. **Kết luận:** sẵn lòng nhận lương tiền thấp hơn *"is not necessarily a remedy for unemployment"*;
   phân tích đầy đủ hẹn tới *"chapter 19 and its Appendix"* (QI, Ch 2).

**Ví dụ số** *(số giả định, tình huống ở Góc đời sống)*.

| Tình huống | Lương tổ cắt (lương thực) | Lương tổ may (lương thực) | Tổ cắt so với tổ may | Có chống không |
| --- | ---: | ---: | ---: | --- |
| Chỉ tổ cắt giảm 10% lương tiền | 180,0 | 200,0 | **−10%** | **có** |
| Giá tăng 10%, lương tiền giữ nguyên | 200 ÷ 1,1 = 181,8 | 181,8 | 0% | thường không |

Lương thực tổ cắt mất ở hai dòng gần như nhau (180,0 với 181,8), nhưng chỉ dòng đầu làm họ tụt hạng.

**Còn "hạ lương 20% làm teo sức mua"?** Lập luận ấy **không nằm ở Chương 2**: Keynes chủ ý gác các
tác động gián tiếp, *"effects which we shall examine in detail in chapter 19"* (QI, Ch 2) — xem
[Bài 7, §1](bai_07_tien_cong_gia_ca.md#1-vì-sao-giảm-lương-không-trực-tiếp-chữa-thất-nghiệp).

**Một phỏng đoán, không phải số liệu.** Keynes đề nghị *"a statistical enquiry"* về quan hệ lương
tiền – lương thực, rồi **đoán**: với mức lương **chung**, *"it will be found, I think, that the change in real wages associated with a change in
money-wages, so far from being usually in the same direction, is almost always in the opposite
direction"* (QI, Ch 2). Vì việc làm **giảm** kéo theo hai điều độc lập: người lao động dễ chịu cắt
lương tiền hơn, còn lương thực **tăng** vì sản phẩm biên tăng (định đề I). Vậy lương thực cao lúc suy
thoái là **hệ quả** của việc làm giảm, không phải bằng chứng người lao động đòi nhiều hơn. Đây là **phỏng đoán** ("I think"); số liệu sau đó **không ủng hộ** nó (§8).

> [!warning] Keynes không nói "cứ tăng lương là hết thất nghiệp"
> Luận điểm là: (1) người lao động **không** cư xử như định đề II giả định; (2) mặc cả lương tiền
> **không** chắc điều khiển được lương thực; nên (3) giảm lương danh nghĩa **không phải công cụ đáng
> tin**. Cái gì quyết định việc làm thì phải chờ §5.

---

## 4. Cú đánh thứ hai: "cung tự tạo cầu" là một ảo giác

> [!example] Góc đời sống — nhịn ăn phở KHÔNG tự động thành cái nhà máy
> Chị Tư sợ khủng hoảng, bỏ bữa phở sáng, gửi 30 nghìn vào tài khoản. Định luật Say ngầm bảo: 30
> nghìn đó **tự khắc** thành **đầu tư** đâu đó; cầu chỉ **đổi dạng** từ "cầu phở" sang "cầu nhà
> xưởng". Keynes: người *nhịn tiêu* (chị Tư) và người *xây xưởng* (một doanh nhân) là **hai người,
> hai động cơ**. Doanh nhân chỉ xây khi **kỳ vọng bán được hàng** — mà khi ai cũng nhịn, hàng đang ế.
> Quán phở mất khách, không xưởng nào mọc lên: **cầu tụt thật**.

**Keynes nói gì.** *"From the time of Say and Ricardo the classical economists have taught that
supply creates its own demand"* — theo nghĩa toàn bộ chi phí sản xuất rốt cuộc phải được chi ra,
trực tiếp hay gián tiếp, để mua sản phẩm (QI, Ch 2). Keynes trích thẳng J.S. Mill:

> [!quote] J.S. Mill, được Keynes dẫn lại — QI, Ch 2
> *"All sellers are inevitably, and by the meaning of the word, buyers. Could we suddenly double
> the productive powers of the country, we should double the supply of commodities in every
> market; but we should, by the same stroke, double the purchasing power."*
>
> "Mọi người bán, tất yếu và theo đúng nghĩa của từ, đều là người mua. Nếu bỗng nhiên ta nhân đôi
> năng lực sản xuất của cả nước, ta sẽ nhân đôi lượng hàng trong mọi thị trường; nhưng bằng chính cú
> đó, ta cũng nhân đôi **sức mua**." (Mill, *Principles of Political Economy*, dẫn trong QI, Ch 2)

Hệ quả kéo theo — Keynes dẫn **Marshall**: người ta mua lao động và hàng hoá *"with that portion of
his income which he saves just as much as he does with that he is said to spend"* (QI, Ch 2): **mỗi
hành vi nhịn tiêu tự thành đầu tư**. Không ai còn viết thô như thế, nhưng nó *"still underlies the
whole classical theory, which would collapse without it"* (QI, Ch 2).

**Vì sao nghe xuôi tai?** Vì nó đứng sát hai mệnh đề **đúng** (QI, Ch 2):

- tổng thu nhập **bằng** giá trị sản lượng — nhưng không suy ra chi phí **luôn** được bù bằng tiền bán
  hàng;
- tổng phần giàu thêm của cá nhân bằng của cộng đồng — nhưng không suy ra mỗi hành vi tiết kiệm **tất
  dẫn tới** đầu tư song song.

> [!quote] Ảo giác quang học — QI, Ch 2
> *"Those who think in this way are deceived, nevertheless, by an optical illusion, which makes two
> essentially different activities appear to be the same. They are fallaciously supposing that
> there is a nexus which unites decisions to abstain from present consumption with decisions to
> provide for future consumption; whereas the motives which determine the latter are not linked in
> any simple way with the motives which determine the former."*
>
> "Tuy vậy, những ai nghĩ như thế đã bị đánh lừa bởi một **ảo giác quang học**, khiến hai hoạt động
> về bản chất khác hẳn nhau trông như là một. Họ lầm tưởng có một **sợi dây** nối **quyết định nhịn
> tiêu hôm nay** với **quyết định chuẩn bị cho tiêu dùng tương lai**; trong khi động cơ quyết định
> cái sau không gắn một cách đơn giản nào với động cơ quyết định cái trước." (QI, Ch 2)

**Định nghĩa.** **Định luật Say**, Keynes viết lại cho chính xác: *"the aggregate demand price of
output as a whole is equal to its aggregate supply price for all volumes of output"* (QI, Ch 3) —
"tiền thu về từ bán hàng" luôn bằng "tiền cần thu để bõ công sản xuất", ở **mọi** mức sản lượng (§5).

**Chuỗi lập luận.**

1. **Sản xuất tạo ra thu nhập bằng đúng giá trị sản lượng** — đúng (QI, Ch 2).
2. **Thu nhập chia thành tiêu dùng và tiết kiệm**; phần tiêu dùng quay lại mua hàng.
3. **Say cần thêm**: phần tiết kiệm **cũng** quay lại thành đầu tư. Đây là mắt xích ảo giác — hai
   quyết định, hai người, hai động cơ (QI, Ch 2).
4. **Mắt xích đứt** thì tiền bán hàng có thể **thấp hơn** mức bõ công; doanh nghiệp cắt sản lượng.
5. **Đây là "tiên đề song song" của phái cổ điển:** *"Granted this, all the rest follows"* (QI, Ch 2).
   Ba giả định — lương thực bằng nỗi khổ nhọc biên, không có thất nghiệp không tự nguyện, cung tự tạo
   cầu — *"all stand and fall together, any one of them logically involving the other two"* (QI, Ch 2).

**Ví dụ số** *(số giả định)*. Sản lượng giá trị **1.000** tỷ, trả ra đúng 1.000 tỷ thu nhập. Hộ gia
đình tiêu **800**, để dành **200**.

| | Theo Say | Theo Keynes |
| --- | ---: | ---: |
| Tiêu dùng | 800 | 800 |
| Đầu tư (doanh nghiệp **quyết định** mua máy, xây xưởng) | 200 — "tự khớp" tiết kiệm | **120** — tuỳ kỳ vọng lợi nhuận |
| Tổng chi mua hàng | 1.000 | **920** |
| Hàng không bán được như dự tính | 0 | **80** |

Ở cột Keynes, **80 tỷ hàng tồn ngoài ý muốn** khiến kỳ sau doanh nghiệp **cắt sản xuất**.

> [!warning] "Tiết kiệm ≡ đầu tư" của Bài 2 không cứu được Say
> [Bài 2](bai_02_dinh_nghia_cong_cu.md#4-tiết-kiệm--đầu-tư-một-đẳng-thức-không-phải-một-quy-luật)
> cho thấy tiết kiệm **luôn bằng** đầu tư **sau khi đã xảy ra**: 80 tỷ hàng tồn cũng tính là đầu tư
> vào kho, nên 200 = 120 + 80. Đó là **kế toán**; Say nói về **kế hoạch**. Phần 80 tỷ "đầu tư" bất
> đắc dĩ chính là tín hiệu buộc doanh nghiệp thu hẹp sản xuất.

---

## 5. Lời giải: nguyên lý cầu hữu hiệu (D và Z)

> [!example] Góc đời sống — xưởng may chốt số công nhân tháng sau
> Cuối tháng, chủ xưởng may không hỏi "thị trường có tự cân bằng không" mà hỏi: **tháng sau bán được
> bao nhiêu tiền?** Ước bán 1,2 tỷ trong khi thuê 120 thợ cần ít nhất 1,1 tỷ mới bõ — bà thuê thêm;
> ước chỉ 0,9 tỷ — bà cho bớt thợ nghỉ. Nhân lên cả nền kinh tế, đó là nguyên lý cầu hữu hiệu.

**Keynes nói gì.** Thuê một lượng lao động, doanh nhân chịu **chi phí yếu tố** (*factor cost*: trả
cho các yếu tố sản xuất — chính là thu nhập của họ) và **chi phí sử dụng** (*user cost*: mua của
doanh nghiệp khác cộng hao mòn thiết bị). Giá trị sản lượng trừ hai thứ ấy là **lợi nhuận**, thứ
doanh nhân tìm cách tối đa; chi phí yếu tố cộng lợi nhuận là **tiền thu** (*proceeds*) của lượng việc
làm ấy (QI, Ch 3). Rồi:

- **Giá cung tổng hợp Z** là *"the expectation of proceeds which will just make it worth the while of
  the entrepreneurs to give that employment"* — tiền thu kỳ vọng **vừa đủ** để tạo ngần ấy việc làm;
  **hàm cung tổng hợp** Z = φ(N) (QI, Ch 3).
- **Giá cầu tổng hợp D** là *"the proceeds which entrepreneurs expect to receive from the employment
  of N men"* — tiền thu **thực sự kỳ vọng**; **hàm cầu tổng hợp** D = f(N) (QI, Ch 3).

> [!quote] Định nghĩa cầu hữu hiệu — QI, Ch 3
> *"Thus the volume of employment is given by the point of intersection between the aggregate
> demand function and the aggregate supply function; for it is at this point that the
> entrepreneurs' expectation of profits will be maximised. The value of D at the point of the
> aggregate demand function, where it is intersected by the aggregate supply function, will be
> called the effective demand."*
>
> "Như vậy, khối lượng việc làm được cho bởi **giao điểm giữa hàm cầu tổng hợp và hàm cung tổng
> hợp**; vì chính tại điểm này kỳ vọng lợi nhuận của doanh nhân được tối đa. Giá trị của D tại điểm
> trên hàm cầu tổng hợp nơi nó bị hàm cung tổng hợp cắt qua sẽ được gọi là **cầu hữu hiệu**." (QI,
> Ch 3)

**Định nghĩa.**

| Ký hiệu | Trả lời câu hỏi | Phụ thuộc |
| --- | --- | --- |
| **Z = φ(N)** | thuê N người thì **cần** kỳ vọng thu bao nhiêu mới bõ? | kỹ thuật, tài nguyên, chi phí |
| **D = f(N)** | thuê N người thì **kỳ vọng** thu được bao nhiêu? | tiêu dùng D₁ + đầu tư D₂ |
| **Cầu hữu hiệu** | giá trị của D tại D = Z — **một con số**, không phải "nhu cầu có khả năng thanh toán" chung chung | cả hai hàm |

> [!note] [sửa lỗi in] Gutenberg mất chữ φ, χ
> Bản Gutenberg in cả hai hàm là "f(N)" (*"f(N) and f(N) are equal"* vô nghĩa) và χ thành "c(N)";
> nguyên bản: Z = φ(N), D = f(N), D₁ = χ(N) — hai hàm khác nhau phải mang hai chữ khác nhau.

**Chuỗi lập luận.**

1. **Doanh nhân thuê người theo kỳ vọng tiền thu** (QI, Ch 3).
2. **D > Z**: có động cơ thuê thêm — kể cả cạnh tranh nhau đẩy chi phí lên — tới chỗ Z bằng D (QI,
   Ch 3). **D < Z**: thuê bớt.
3. **Cân bằng ở D = Z**, nơi lợi nhuận kỳ vọng tối đa; giá trị D ở đó là cầu hữu hiệu (QI, Ch 3).
4. **Định luật Say** ở đây: f(N) và φ(N) **bằng nhau với mọi N**, nên việc làm *"is indeterminate
   except in so far as the marginal disutility of labour sets an upper limit"* — **giới hạn trên do nỗi
   khổ nhọc biên đặt ra**, không phải "hết người để thuê" (QI, Ch 3); cạnh tranh đẩy việc làm tới đó.
5. **Kết luận:** Say ⇔ *"there is no obstacle to full employment"* (QI, Ch 3). Đây cũng là định nghĩa
   toàn dụng thứ hai đã hứa: *"a situation in which aggregate employment is inelastic in response to an
   increase in the effective demand for its output"* (QI, Ch 3).

**Ví dụ số** *(số giả định)*. N tính bằng nghìn người, Z và D bằng tỷ đồng/tháng; toàn dụng **N = 100**.
Giả định ẩn: (i) lương danh nghĩa mỗi lao động **không đổi** — giản lược Keynes tự dùng trong bản tóm
tắt Ch 3; (ii) **Z = φ(N) = 10·N** (Z thật cong lên vì lợi suất giảm dần, ở đây làm thẳng); (iii) thu
nhập ứng với N lấy bằng Z; (iv) **D₁ = 80 + 0,8·Z** — **khuynh hướng tiêu dùng biên** 0,8 (thêm 1
đồng thu nhập tiêu thêm 0,8; [Bài 3](bai_03_tieu_dung_so_nhan.md)); (v) **D₂ = 80** cố định.

| N | Z = 10N | D₁ = 80 + 0,8Z | D₂ | D = D₁ + D₂ | D − Z | Doanh nghiệp |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 60 | 600 | 560 | 80 | 640 | **+40** | thuê thêm |
| 70 | 700 | 640 | 80 | 720 | +20 | thuê thêm |
| **80** | **800** | **720** | **80** | **800** | **0** | **đứng yên** |
| 90 | 900 | 800 | 80 | 880 | −20 | thuê bớt |
| 100 | 1.000 | 880 | 80 | 960 | **−40** | thuê bớt |

Dòng N = 80: Z = 10 × 80 = 800; D₁ = 80 + 0,8 × 800 = 720; D = 720 + 80 = 800 = Z. Đại số: 10N = 80 +
8N + 80 ⇒ N = 80. Cầu hữu hiệu **800 tỷ**, việc làm **80** nghìn — **20** nghìn dưới toàn dụng. Dưới
80 thì D > Z, trên 80 thì D < Z: điểm 80 **ổn định**, không lực nào tự kéo nó lên 100. Đây chính là N
= 80 ở §1: lương thực 10 giỏ > nỗi khổ nhọc biên 6 giỏ.

Theo **Say**, cột D − Z bằng **0 ở mọi dòng**: mệnh đề (7) gọi đó là *"neutral equilibrium for all
values of N less than its maximum value"* — cân bằng **trung tính**, cạnh tranh đẩy dần tới 100 (QI,
Ch 3).

> [!warning] Hai lỗi đọc hay gặp
> 1. **D = Z với mọi N là Say, không phải Keynes.** Ở Keynes, D = Z là **điều kiện cân bằng** chỉ
>    thoả tại **một** N. Say biến nó thành **đồng nhất thức** đúng ở mọi N.
> 2. **D không phải doanh thu đã thu được**, mà là doanh thu **kỳ vọng** khi quyết định thuê người.
>    Kỳ vọng ngắn hạn ấy hình thành ra sao, Keynes bàn ở Ch 5
>    ([Bài 2](bai_02_dinh_nghia_cong_cu.md)).

Bộ khung của cả cuốn sách nằm trong tách đôi D:

```
        D   =   D₁   +   D₂
                │        │
    cầu hữu     │        └── ĐẦU TƯ  (doanh nghiệp mua máy, xây xưởng…)
    hiệu        │              → hiệu suất biên của vốn & LÃI SUẤT        [Bài 4–5]
                │
                └─────────── TIÊU DÙNG (hộ gia đình)  D₁ = χ(N)
                               → khuynh hướng tiêu dùng                   [Bài 3]
```

Mệnh đề (4)–(5), ký hiệu nguyên bản *[sửa lỗi in]*: D₁ + D₂ = D = φ(N) và D₁ = χ(N), nên **φ(N) −
χ(N) = D₂** — việc làm cân bằng phụ thuộc hàm cung φ, khuynh hướng tiêu dùng χ và đầu tư D₂: *"This
is the essence of the General Theory of Employment"* (QI, Ch 3). Kiểm: ở N = 80, 800 − 720 = 80 = D₂.

---

## 6. Nghịch lý nghèo giữa cảnh thừa mứa

> [!example] Góc đời sống — hai vòi nước và cái bể rò
> Coi "việc làm" là mực nước trong bể. Vòi **tiêu dùng** (D₁) tự to lên khi nước dâng, nhưng chỉ bù
> 8 phần trong 10 — 2 phần **rò** ra (phần để dành). Nước càng cao, chỗ rò càng lớn. Vòi **đầu tư**
> (D₂) do **người khác** vặn, theo lý do khác (Bài 4–5); nó chảy bao nhiêu thì mực nước dừng ở chỗ
> rò bằng chừng ấy — có thể là **lưng chừng bể**.

**Keynes nói gì.** Vì sao giao điểm không tự nằm ở toàn dụng? Vì một "quy luật tâm lý": *"when
aggregate real income is increased aggregate consumption is increased, but not by so much as
income"*, nên phải có đủ đầu tư *"to absorb the excess of total output over what the community
chooses to consume"* (QI, Ch 3). Mệnh đề (8) nói gọn nhất:

> [!quote] Khoảng hở giữa Z và D₁ — QI, Ch 3
> *"When employment increases, D1 will increase, but not by so much as D; since when our income
> increases our consumption increases also, but not by so much. The key to our practical problem is
> to be found in this psychological law. For it follows from this that the greater the volume of
> employment the greater will be the gap between the aggregate supply price (Z) of the corresponding
> output and the sum (D1) which the entrepreneurs can expect to get back out of the expenditure of
> consumers. Hence, if there is no change in the propensity to consume, employment cannot increase,
> unless at the same time D2 is increasing so as to fill the increasing gap between Z and D1."*
>
> "Khi việc làm tăng, **D₁ tăng nhưng không nhiều bằng D**; vì thu nhập tăng thì tiêu dùng cũng tăng,
> nhưng không nhiều bằng. **Chìa khoá** cho vấn đề thực tiễn nằm ở **quy luật tâm lý** này. Từ đó:
> việc làm càng lớn thì **khoảng hở** giữa giá cung tổng hợp (Z) và khoản (D₁) doanh nhân mong thu
> lại từ người tiêu dùng **càng rộng**. Vậy nếu khuynh hướng tiêu dùng không đổi, việc làm **không thể
> tăng** trừ khi **D₂ đồng thời tăng** để lấp khoảng hở ấy." (QI, Ch 3)

Trừ phi có (như phái cổ điển giả định) một lực luôn làm D₂ tăng đủ, *"the economic system may find
itself in stable equilibrium with N at a level below full employment"* (QI, Ch 3).

**Định nghĩa.** **Khoảng hở** (*gap*) ở mức việc làm N là **Z − D₁**: phần tiền thu cần có mà người
tiêu dùng không trả. Cân bằng ở chỗ **D₂ = Z − D₁**; vì khoảng hở **rộng dần** theo N, một mức đầu tư
cho trước chỉ lấp được tới **một** N. **Nghịch lý nghèo giữa cảnh thừa mứa** (*"the paradox of poverty
in the midst of plenty"*): sản xuất bị chặn dù *"the marginal product of labour still exceeds in value
the marginal disutility of employment"* — làm thêm vẫn đáng, mà không ai thuê (QI, Ch 3).

**Chuỗi lập luận.**

1. **Tiêu dùng tăng ít hơn thu nhập** khi việc làm tăng (QI, Ch 3).
2. **Vậy Z − D₁ rộng dần** theo N (QI, Ch 3).
3. **Chỉ D₂ lấp được khoảng hở**, mà D₂ do *"the inducement to invest"* quyết định — hiệu suất biên
   của vốn so với lãi suất (QI, Ch 3) — **không** do khoảng hở cần bao nhiêu.
4. **Cân bằng ở N mà D₂ = Z − D₁.** Nó *"cannot be greater than full employment"*, *"But there is no
   reason in general for expecting it to be equal to full employment"*; toàn dụng chỉ đạt *"by
   accident or design"* (QI, Ch 3).
5. **Hệ quả về lương:** việc làm quyết định lương thực, *"not the other way round"*; khi cầu hữu hiệu
   thiếu, lương thực cân bằng **lớn hơn** nỗi khổ nhọc biên (QI, Ch 3) — cặp 10 > 6 ở §1.

**Ví dụ số 1 — khoảng hở rộng dần** *(số giả định, tiếp bảng §5)*.

| N | Z | D₁ | Khoảng hở Z − D₁ | D₂ có | Đủ lấp? |
| ---: | ---: | ---: | ---: | ---: | --- |
| 60 | 600 | 560 | 40 | 80 | thừa 40 → thuê thêm |
| 80 | 800 | 720 | **80** | 80 | **vừa đủ** → cân bằng |
| 100 | 1.000 | 880 | **120** | 80 | thiếu 40 → không giữ được |

N tăng 20 nghìn thì Z tăng 200 tỷ, D₁ chỉ tăng 0,8 × 200 = 160: khoảng hở tăng **40 tỷ**. Toàn dụng
cần D₂ = **120**, thêm **40**; thu nhập tăng 1.000 − 800 = **200** = 40 × 5, đúng **số nhân** k = 1 ÷
(1 − 0,8) = 5 của [Bài 3](bai_03_tieu_dung_so_nhan.md).

**Ví dụ số 2 — nước càng giàu, khoảng hở càng rộng** *(số giả định)*. Keynes: *"the richer the
community, the wider will tend to be the gap between its actual and its potential production"* (QI,
Ch 3). Hai nước cùng sản lượng toàn dụng **1.000**; tiêu dùng tỷ lệ với thu nhập, nên Y = D₂ ÷ (1 − c):

| Nước | Tỷ lệ tiêu dùng c | Đầu tư cần cho toàn dụng (1 − c) × 1.000 | Đầu tư thực có | Sản lượng cân bằng |
| --- | ---: | ---: | ---: | ---: |
| Nghèo | 0,95 | 50 | 50 | **1.000** |
| Giàu | 0,75 | 250 | 150 | 150 ÷ 0,25 = **600** |

Thiếu cơ hội đầu tư, nước giàu co sản lượng xuống 600 — *"until … it has become
so poor that its surplus over its consumption is sufficiently diminished to correspond to the
weakness of the inducement to invest"* (QI, Ch 3): phần thừa 0,25 × 600 = 150 vừa khớp đầu tư. Tệ
hơn, vốn tích luỹ nhiều làm cơ hội mới kém hấp dẫn trừ khi lãi suất giảm đủ nhanh — dẫn sang
[Bài 5](bai_05_lai_suat_thanh_khoan.md).

> [!warning] Keynes không nói "nền kinh tế luôn nằm dưới toàn dụng"
> Câu chính xác: cân bằng **không thể vượt** toàn dụng, và **không có lý do chung** để nó **bằng**
> toàn dụng (QI, Ch 3). Ch 3 chưa nói gì về **tốc độ** hay **chu kỳ** — chỉ nói cân bằng **có thể ổn
> định** ở mức thấp. Cảnh 1932 ở đầu bài (ghi chú người soạn: nông dân Mỹ đổ sữa, đốt ngô vì giá
> không bõ chở đi bán, trong khi người thành phố xếp hàng nhận súp) là một trạng thái như thế.

---

## 7. Vì sao một ý tưởng sai lại thắng: Ricardo và Malthus

Nếu Định luật Say sai, **vì sao hơn trăm năm người ta tin nó?** Đầu thế kỷ 19, **Malthus** phản đối
chủ thuyết của **Ricardo** rằng cầu hữu hiệu không thể thiếu — nhưng thua, vì *"Malthus was unable to
explain clearly (apart from an appeal to the facts of common observation) how and why effective
demand could be deficient or excessive"* (QI, Ch 3). Bài học: muốn lật một lý thuyết, phải có lý
thuyết khác — việc §5–§6 làm.

> [!quote] "Ricardo chinh phục nước Anh" — QI, Ch 3
> *"Ricardo conquered England as completely as the Holy Inquisition conquered Spain. Not only was his
> theory accepted by the city, by statesmen and by the academic world. But controversy ceased; the
> other point of view completely disappeared; it ceased to be discussed. The great puzzle of effective
> demand with which Malthus had wrestled vanished from economic literature."*
>
> "Ricardo chinh phục nước Anh trọn vẹn như **Toà án Dị giáo** chinh phục Tây Ban Nha. Giới tài chính,
> chính khách, học giới đều chấp nhận; tranh luận chấm dứt, quan điểm kia biến mất. **Câu đố lớn về
> cầu hữu hiệu** mà Malthus vật lộn đã biến khỏi văn liệu kinh tế." (QI, Ch 3)

Không thấy nó *"even once"* trong Marshall, Edgeworth, Pigou; nó chỉ sống *"furtively, below the
surface, in the underworlds of Karl Marx, Silvio Gesell or Major Douglas"* (QI, Ch 3) — Gesell là nhà
cải cách tiền tệ Đức, Douglas đề xướng "tín dụng xã hội" ở Anh (ghi chú người soạn).

**Vì sao thắng — xã hội học của tư tưởng** (QI, Ch 3): kết luận **ngược trực giác** (thêm uy tín);
thực hành **khắc khổ** — *"That its teaching, translated into practice, was austere and often
unpalatable, lent it virtue"*; dựng được **lâu đài logic** (có vẻ đẹp); coi bất công là **cái giá tất
yếu** của tiến bộ (giới cầm quyền ưa); biện minh cho tự do của nhà tư bản (được giới có tiền ủng hộ).
Lạc quan ấy khiến các nhà kinh tế bị coi như những chàng **Candide** của Voltaire (QI, Ch 3).

Câu khép Quyển I: lý thuyết cổ điển có thể là cách ta **muốn** nền kinh tế vận hành, *"But to assume
that it actually does so is to assume our difficulties away"* (QI, Ch 3).

---

## 8. Phản biện & hậu Keynes

> [!note] Phần này **không có trong sách**
> Người soạn bổ sung, theo thứ tự thời gian; mỗi bước trả lời một lỗ hổng của bước trước.

**Bước 1 — số liệu bác phỏng đoán về lương (1938–1939).** Phỏng đoán ở §3 (lương thực tăng khi suy
thoái) bị kiểm ngay: **John Dunlop** (*Economic Journal*, 1938, số liệu Anh) và **Lorie Tarshis**
(*Economic Journal*, 1939, số liệu Mỹ) thấy lương thực **không** đi ngược chiều lương tiền như Keynes
đoán. Keynes đáp trong bài *Relative Movements of Real Wages and Output* (*Economic Journal*, 3/1939):
**nhận** số liệu không ủng hộ phỏng đoán, và cho rằng bỏ giả định ấy không làm đổ — thậm chí làm gọn —
lý thuyết cầu hữu hiệu. Cái §1 "giữ" từ phái cổ điển hoá ra là chỗ yếu; §5–§6 không bị đụng.

**Bước 2 — đóng gói thành mô hình (1937–1953).** **John Hicks** (*Econometrica*, 1937) nén lý thuyết
vào hai đường **IS–LL**; **Alvin Hansen** phổ biến dạng **IS–LM** (1953). **Paul Samuelson** đưa vào
giáo trình *Economics* (1948) **chữ thập Keynes**: chi tiêu dự kiến cắt đường 45° — bảng §5 vẽ thành
hình. Cái giá: Z = φ(N) và **kỳ vọng** của doanh nhân gần như biến khỏi sách giáo khoa.

**Bước 3 — phản công: hiệu ứng số dư thực (1943–1956).** Nếu lương và giá **giảm đủ**, tiền nắm giữ
mua được nhiều hơn, người ta tiêu thêm — D₁ dịch lên tới khi lấp khoảng hở. **Arthur Pigou**
(*Economic Journal*, 1943) nêu ý này; **Don Patinkin** (1948; *Money, Interest, and Prices*, 1956)
khái quát thành **hiệu ứng số dư thực**: với giá linh hoạt hoàn toàn, cân bằng dưới toàn dụng không
vĩnh viễn. Phản đáp: **Michał Kalecki** (1944) — giảm phát làm **nợ nặng thêm**, gần lý thuyết **giảm
phát nợ** của Irving Fisher (1933, **trước** Keynes). Hiệu ứng có thật nhưng **yếu và chậm**.

**Bước 4 — đọc lại và phản bác (1965–1978).** **Robert Clower** (1965) và **Axel Leijonhufvud** (1968)
cho rằng cốt lõi của Keynes là **trục trặc phối hợp**: người thất nghiệp muốn mua nhưng không có thu
nhập để biến mong muốn thành cầu. **Milton Friedman** (1968) đưa ra **tỷ lệ thất nghiệp tự nhiên**:
dài hạn, cầu chỉ đổi lạm phát. **Robert Lucas** (1978) cho rằng thất nghiệp không tự nguyện của §2
không phải sự kiện quan sát được, nên không phải thứ lý thuyết cần giải thích.

**Bước 5 — Neo-Keynes giải thích *vì sao* lương cứng (1977–1999).** **Stanley Fischer** (1977) và
**John Taylor** (1980) dựng hợp đồng lương **so le**; **Shapiro và Stiglitz** (1984) đưa **lương hiệu
quả** — chủ trả cao để thợ không lười, nên thất nghiệp không tự nguyện tồn tại ở cân bằng. **Akerlof,
Dickens và Perry** (1996) đo được độ **cứng khi giảm** của lương danh nghĩa. **Truman Bewley** (*Why
Wages Don't Fall During a Recession*, 1999) phỏng vấn hơn 300 người (chủ yếu nhà quản lý): họ né cắt lương vì sợ
hỏng **tinh thần** và cảm giác **bất công so với người khác** — rất gần phản bác thứ nhất của Keynes
về lương **tương đối** (§3).

**Bước 6 — sau 2008.** Lãi suất chạm 0, thiếu hụt tổng cầu trở lại trung tâm (Summers hồi sinh cụm
"trì trệ trường kỳ" của Hansen, 2013). Câu hỏi nay là lực tự điều chỉnh **mạnh và nhanh** tới đâu.

---

## 9. Đối chiếu 2026

> [!note] Phần này **không có trong sách**; số liệu kèm nguồn và ngày, có thể đã đổi — kiểm lại
> trước khi dùng. Diễn giải "đọc bằng Keynes" là của người soạn.

**Mỹ.** Tháng 9/2026 thất nghiệp **4,2%** (≈ **7,1 triệu** người), trong khoảng 4,1–4,3% từ tháng 3
(BLS, 2026-10-09); việc làm phi nông nghiệp chỉ tăng **29.000**, dưới dự báo (Fed St. Louis,
2026-10-02). Giữa tháng 9 (2026-09-16) Fed **tăng** lãi suất 0,25 điểm lên 3,75–4% — lần đầu sau hơn
ba năm — vì lạm phát vẫn cao (Fed, 2026-09-16; Indeed Hiring Lab, 2026-10-02). Đọc bằng Keynes: tăng lãi suất **nén D₂** (Bài 4–5) giữa lúc tuyển
dụng chậm; Keynes 1936 không có lời giải cho cảnh **vừa** lạm phát **vừa** cầu yếu (§8, Friedman).

**Việt Nam — thất nghiệp thấp chưa chắc cầu đủ.**

| Dữ kiện quý III/2026 (Cục Thống kê, 2026-10-03) | Đọc bằng Keynes |
| --- | --- |
| Thất nghiệp trong độ tuổi **2,22%** (≈ 1,071 triệu người); thành thị 2,72% | thấp hơn Mỹ nhiều — nhưng xem các dòng dưới |
| Thiếu việc làm **1,31%** (≈ 617,3 nghìn); **không sử dụng hết tiềm năng 3,63%** (≈ 1,9 triệu) | người **muốn làm thêm** ở mức trả hiện hành mà không có — gần ý "không tự nguyện" hơn con số 2,22% |
| Lao động **phi chính thức 60,6%** | không có trợ cấp đủ sống, thiếu cầu ít hiện thành thất nghiệp **mở**, mà thành việc làm ít giờ, thu nhập thấp |
| Thất nghiệp thanh niên 15–24 tuổi **9,07%**; ≈ 1,6 triệu thanh niên không việc, không học (11,2%) | nhóm chịu "khoảng hở" trước tiên |
| Thu nhập bình quân **9,2 triệu đồng/tháng**, +9,9% so với cùng kỳ | khác Mỹ: nền của D₁ đang mạnh |

Bài học: Keynes định nghĩa thất nghiệp không tự nguyện bằng **phép thử hành vi**, không bằng một tỷ
lệ; ở nền kinh tế nhiều lao động phi chính thức, **thiếu việc làm** gần câu hỏi của ông hơn.

---

## 10. Nối môn đang học

| Môn trong kho | Giao ở đâu | Học kết hợp thế nào |
| --- | --- | --- |
| [Của cải của các dân tộc (Adam Smith)](../../adamsmitccccdt/ly_thuyet/bai_05_von.md) | §4 | Smith coi mỗi đồng để dành đều vào sản xuất; Keynes tấn công đúng mắt xích ấy (ảo giác quang học). Bài 3 đẩy tới **nghịch lý tiết kiệm**. |
| [Ba người khổng lồ (Skousen)](../../bigthreeeconomic/README.md) | cả bài | Bản tóm của Skousen có giữ Z = φ(N), khoảng hở Z − D₁, hay rút gọn thành "Keynes = nhà nước tiêu tiền"? |
| [EG43 — Kinh tế Chính trị Mác–Lênin](../../../houedu/eg43-kinhtechinhtri/README.md) | §7 | Keynes xếp **Marx** vào số ít người giữ sống "câu đố cầu hữu hiệu". Cả hai bác Say; Marx để kết tội hệ thống, Keynes để **sửa** nó. |

---

## 11. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa gọn | Dễ lẫn với |
| --- | --- | --- |
| **Định đề I / II** | lương = sản phẩm biên [Keynes giữ] / thoả dụng của lương = nỗi khổ nhọc biên [Keynes bỏ] (QI, Ch 2) | nhau |
| **Lương danh nghĩa / lương thực** | số tiền trên giao kèo / số hàng tiền công nó mua được | "lương thực" = gạo |
| **Thất nghiệp không tự nguyện** | giá tăng nhẹ thì cả cung lẫn cầu lao động ở lương tiền hiện hành đều vượt việc làm hiện có (QI, Ch 2) | "không có gì để làm"; cọ xát; tự nguyện |
| **Toàn dụng** | không có thất nghiệp không tự nguyện; tương đương: việc làm không tăng khi cầu hữu hiệu tăng | thất nghiệp bằng 0 |
| **Định luật Say** | giá cầu tổng hợp = giá cung tổng hợp ở **mọi** mức sản lượng (QI, Ch 3) | thu nhập = giá trị sản lượng (đúng) |
| **Z = φ(N)** | tiền thu kỳ vọng **vừa đủ** để tạo N việc làm (QI, Ch 3) | chi phí đã chi |
| **D = f(N)** | tiền thu **kỳ vọng** khi thuê N người; D = D₁ + D₂ | doanh thu đã thu |
| **Cầu hữu hiệu** | giá trị của D tại giao điểm D = Z (QI, Ch 3) | "nhu cầu có khả năng thanh toán" |
| **Khoảng hở Z − D₁** | phần tiền thu cần có mà tiêu dùng không trả; rộng dần theo N; D₂ phải lấp | output gap hiện đại |
| **Nghèo giữa thừa mứa** | thiếu cầu hữu hiệu chặn sản xuất dù làm thêm vẫn đáng (QI, Ch 3) | nghèo do thiếu năng lực sản xuất |

---

## 12. Câu hỏi tự kiểm tra

Tự trả lời trước khi xem lại bài.

1. Phát biểu **hai định đề** cổ điển. Keynes giữ cái nào, bỏ cái nào? Giữ định đề I buộc ông nhận
   điều gì về lương thực? (QI, Ch 2)
2. Định nghĩa **thất nghiệp không tự nguyện** theo chữ của Keynes. Vì sao phép thử dùng **giá tăng**
   chứ không dùng **lương tiền giảm**? (QI, Ch 2)
3. Nêu **hai phản bác** với định đề II. Cái nào là nền tảng? Vì sao người lao động "theo bản năng hợp
   lý hơn phái cổ điển"? (QI, Ch 2)
4. Lập luận "giảm lương đồng loạt làm teo tổng cầu" nằm ở chương nào, và vì sao không thuộc Ch 2?
5. Định luật Say nói gì trong ngôn ngữ D và Z? Vì sao phải viết Z = φ(N) và D = f(N) bằng **hai chữ
   khác nhau**? Theo phái cổ điển, cái gì đặt giới hạn trên cho việc làm? (QI, Ch 2–3)
6. Dùng mệnh đề (8) giải thích vì sao cân bằng **có thể** ổn định dưới toàn dụng. Vì sao "nước càng
   giàu, khoảng hở càng rộng"? (QI, Ch 3)
7. **Tự tính — cầu hữu hiệu.** Giữ Z = 10N, D₁ = 80 + 0,8Z *(số giả định)*. (a) Với D₂ = 60, tìm N
   cân bằng và cầu hữu hiệu. (b) Lập bảng D − Z ở N = 60, 70, 80. (c) Cần D₂ bao nhiêu cho N = 100?
   (d) Khuynh hướng tiêu dùng biên lên 0,85 (giữ hệ số 80), D₂ = 60: N là bao nhiêu?
8. **Tự tính — phép thử.** Đang có 90 nghìn người làm, lương 250 nghìn/ngày *(số giả định)*. Giá hàng
   tiền công tăng 4%. (a) Lương thực giảm bao nhiêu phần trăm? (b) Sau cú giá, cung lao động ở 250
   nghìn là 97 nghìn, cầu là 93 nghìn: có thất nghiệp không tự nguyện không, tối thiểu bao nhiêu? (c)
   Nếu cung là 88 nghìn thì sao — ứng với định đề nào?

---

## Tóm tắt một trang

```
BÀI 1 — CẦU HỮU HIỆU: CÚ LẬT ĐỔ "CUNG TỰ TẠO CẦU"                  (Quyển I, Ch 1–3)
═══════════════════════════════════════════════════════════════════════════════
HAI ĐỊNH ĐỀ:  I. lương = sản phẩm biên (cầu LĐ)    [GIỮ → việc làm ↑ thì lương thực ↓]
              II. lương = nỗi khổ nhọc biên (cung LĐ) [BỎ]
THẤT NGHIỆP: cọ xát · tự nguyện · KHÔNG tự nguyện (cổ điển chối bỏ)
   phép thử: giá tăng nhẹ, lương tiền giữ nguyên → cung LĐ & cầu LĐ đều > việc làm hiện có?

CÚ ĐÁNH 1 (Ch 2) — hai phản bác định đề II:
   (1) hành vi: chống giảm lương TIỀN (giữ lương TƯƠNG ĐỐI), không đình công khi giá tăng
   (2) nền tảng: mặc cả lương tiền KHÔNG quyết định lương THỰC chung → "giả định lén lút"
   "giảm lương làm teo tổng cầu" = Ch 19 (Bài 7). Phỏng đoán "ngược chiều": Dunlop/Tarshis bác.

CÚ ĐÁNH 2 — SAY: D = Z với MỌI N. Ảo giác: NHỊN TIÊU ≠ ĐẦU TƯ (hai người, hai động cơ).

LỜI GIẢI (Ch 3):  Z = φ(N) cung tổng hợp | D = f(N) cầu tổng hợp = D1 + D2
   D>Z thuê thêm · D<Z thuê bớt · D=Z → giá trị D = CẦU HỮU HIỆU;  φ(N) − χ(N) = D2
   Z=10N, D1=80+0,8Z, D2=80 → N = 80 < 100 toàn dụng.

VÌ SAO DƯỚI TOÀN DỤNG: tiêu dùng tăng ÍT HƠN thu nhập → Z − D1 RỘNG DẦN (40/80/120)
   chỉ D2 lấp → cân bằng ổn định ở N thấp; không vượt toàn dụng, không có lý do để bằng nó.
   NGHÈO GIỮA THỪA MỨA; nước càng giàu khoảng hở càng rộng.
RICARDO thắng Malthus "như Toà Dị giáo". SAU 1936: Hicks · Samuelson · Patinkin · Bewley.
═══════════════════════════════════════════════════════════════════════════════
```

---

## Nguồn

- **John Maynard Keynes**, ***The General Theory of Employment, Interest and Money*** (1936) —
  **Book I: Introduction**, gồm **Chapter 1** (The General Theory), **Chapter 2** (The Postulates of
  the Classical Economics), **Chapter 3** (The Principle of Effective Demand).
- Bản dùng: Project Gutenberg Australia, eBook #0300071h. Tệp trong kho:
  `tai_lieu/The General Theory - Keynes (Gutenberg AU).txt`. Lỗi in có ghi chú: bản Gutenberg mất ký
  hiệu φ (in "f(N)" cho cả hai hàm) và χ (in "c(N)").
- Câu trích nguyên văn kèm **bản dịch của người soạn**; ví dụ *(số giả định)* của người soạn, tính lại
  bằng Python.
- **§8 (không có trong sách):** tác giả, tạp chí và năm ghi ngay trong từng bước.
- **§9 (không có trong sách):**
  [BLS, 2026-10-09](https://www.bls.gov/opub/ted/2026/unemployment-rate-little-changed-at-4-2-percent-in-september-2026.htm);
  [Fed St. Louis, 2026-10-02](https://www.stlouisfed.org/on-the-economy/2026/oct/flash-report-unemployment-rises-slightly-job-growth-slows-september);
  [Fed, 2026-09-16](https://www.federalreserve.gov/monetarypolicy/files/monetary20260916a1.pdf);
  [Indeed Hiring Lab, 2026-10-02](https://hiringlab.indeed.com/2026/10/02/september-2026-jobs-report-steadiness-without-a-spark/);
  [Cục Thống kê, 2026-10-03](https://www.nso.gov.vn/tin-tuc-thong-ke/2026/10/thong-cao-bao-chi-ve-tinh-hinh-lao-dong-viec-lam-quy-iii-va-9-thang-nam-2026/).
- **Góc đời sống**, §8, §9, §10 là phần biên soạn thêm, **không có trong sách**.

<!-- BAN-DO -->

**Bản đồ khoá học**


| #     | Bài                                                                                      | Nội dung sách  | Vòng |
| -----: | ---------------------------------------------------------------------------------------- | -------------- | :----: |
| 0     | [Nhập môn — năm 1936 và cuộc cách mạng Keynes](bai_00_nhap_mon.md)                       | Lời tựa + Ch 1 | 1    |
| **1** | **Cầu hữu hiệu — cú lật đổ "cung tự tạo cầu"** ← *bạn đang ở đây*                        | QI, Ch 1–3     | 1    |
| 2     | [Bộ công cụ: đơn vị đo, kỳ vọng, tiết kiệm ≡ đầu tư](bai_02_dinh_nghia_cong_cu.md)       | QII, Ch 4–7    | 2    |
| 3     | [Khuynh hướng tiêu dùng và Số nhân chi tiêu](bai_03_tieu_dung_so_nhan.md)                | QIII, Ch 8–10  | 1    |
| 4     | [Đầu tư — hiệu suất biên của vốn và "animal spirits"](bai_04_dau_tu_animal_spirits.md)   | QIV, Ch 11–12  | 1    |
| 5     | [Lãi suất và ưa thích thanh khoản — bẫy thanh khoản](bai_05_lai_suat_thanh_khoan.md)     | QIV, Ch 13–15  | 1    |
| 6     | [Bản chất vốn, tính chất riêng của tiền và mô hình việc làm](bai_06_von_tien_mo_hinh.md) | QIV, Ch 16–18  | 2    |
| 7     | [Tiền công, giá cả và lạm phát](bai_07_tien_cong_gia_ca.md)                              | QV, Ch 19–21   | 2    |
| 8     | [Chu kỳ, trọng thương và triết lý xã hội](bai_08_chu_ky_triet_ly.md)                     | QVI, Ch 22–24  | 1    |


Chỉ mục khoá học: [README.md](../README.md)

<!-- /BAN-DO -->

