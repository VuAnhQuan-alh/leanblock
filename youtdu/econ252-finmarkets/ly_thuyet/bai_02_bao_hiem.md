# Bảo hiểm — gộp rủi ro, và ba chỗ nó gãy

> [!info] Về bài này
> Bài học gộp **hai buổi** của khoá **Yale ECON 252 *Financial Markets*** (Xuân 2011):
> **buổi 5 "Insurance, the Archetypal Risk Management Institution"** (YouTube `qfK9rCDCicE`, 73:13),
> giảng viên **Robert J. Shiller**; và **buổi 14**, khách mời **Maurice "Hank" Greenberg**, cựu CEO
> AIG (YouTube `72qUcUAtRZc`, 70:48).
> Mốc dạng `05 26:21` = **buổi 5, phút 26:21**; `14 34:54` = **buổi 14**. Mọi mốc đã đối chiếu
> ngược với phụ đề gốc **của đúng buổi đó** bằng script.
> Phần **📚 Mở rộng** và **🇻🇳 Góc Việt Nam** không có trong video.
>
> **Cách đọc các khối màu:** `[!quote]` trích nguyên văn (kèm nguồn) · `[!warning]` chỗ dễ nhầm · `[!note]` mở rộng/ghi chú · `[!example]` ví dụ áp dụng (Góc QTKD / Góc đời sống — biên soạn thêm, không có trong sách).
>
> **Đọc cùng:** [Bài 3 — Ngân hàng](bai_03_ngan_hang.md). Bài này tự dựng khái niệm **đồng bảo
> hiểm** ở §4 nên đọc độc lập được; nhưng §9 và §12 đối chiếu thẳng với bảo hiểm tiền gửi ở bài 3, và
> đọc hai bài cạnh nhau thì phần so sánh đó mới đủ sức.

## Mục lục

1. [Vì sao bảo hiểm chạy được — một dòng công thức](#1-vì-sao-bảo-hiểm-chạy-được--một-dòng-công-thức)
2. [Lá thư năm 1609 gửi Bá tước Oldenburg](#2-lá-thư-năm-1609-gửi-bá-tước-oldenburg)
3. [Bảo hiểm là một phát minh, và phát minh thì có bản vẽ](#3-bảo-hiểm-là-một-phát-minh-và-phát-minh-thì-có-bản-vẽ)
4. [Chỗ gãy thứ nhất và thứ hai — rủi ro đạo đức, lựa chọn ngược](#4-chỗ-gãy-thứ-nhất-và-thứ-hai--rủi-ro-đạo-đức-lựa-chọn-ngược)
5. [📚 Chỗ gãy thứ ba — khi độc lập không còn](#5-chỗ-gãy-thứ-ba--khi-độc-lập-không-còn)
6. [AIG — chín mươi năm dựng, ba năm sập](#6-aig--chín-mươi-năm-dựng-ba-năm-sập)
7. [Greenberg kể lại cùng câu chuyện, và không khớp](#7-greenberg-kể-lại-cùng-câu-chuyện-và-không-khớp)
8. [Hai chẩn đoán, và vì sao cần cả hai](#8-hai-chẩn-đoán-và-vì-sao-cần-cả-hai)
9. [Quỹ bảo lãnh — và mẹo chia nhỏ không dùng được](#9-quỹ-bảo-lãnh--và-mẹo-chia-nhỏ-không-dùng-được)
10. [⚠️ Bốn chỗ video nói sai](#10-bốn-chỗ-video-nói-sai)
11. [⚠️ Đối chiếu 2026](#11-đối-chiếu-2026)
12. [🇻🇳 Góc Việt Nam — quỹ đã có, rồi bị bãi bỏ](#12-góc-việt-nam--quỹ-đã-có-rồi-bị-bãi-bỏ)
13. [Chương trình](#13-chương-trình)
14. [Từ điển thuật ngữ](#14-từ-điển-thuật-ngữ)
15. [Câu hỏi tự kiểm tra](#15-câu-hỏi-tự-kiểm-tra)

---

## 1. Vì sao bảo hiểm chạy được — một dòng công thức

Shiller mở buổi bằng một lời thú nhận (`05 03:54`): *"Bảo hiểm nghe không có vẻ là chủ đề hào hứng
lắm, đúng không?"* Rồi ông tự nhận sẽ cố làm nó hào hứng hơn, và giải thích vì sao với ông nó hào
hứng (`05 04:27`): *"vì nó là chuyện làm cho đời sống chúng ta chạy được"*, và vì *"nó dính tới lý
thuyết toán học nằm dưới khái niệm ấy."*

Cái lý thuyết toán học ấy vừa vặn trong một dòng. Shiller viết nó lên bảng ở `05 09:12`:

$$\text{sd} = \sqrt{\frac{p(1-p)}{n}}$$

Có $n$ phép thử, mỗi phép xảy ra với xác suất $p$. Độ lệch chuẩn của **tỷ lệ** số lần xảy ra là biểu
thức trên. Và điểm mấu chốt, Shiller nhấn ở `05 10:12`: *"nó giảm theo $n$ — tôi phải nói là, theo
**căn bậc hai** của $n$."*

Áp vào một công ty bảo hiểm hoả hoạn với $p = 1\%$:

|   Số hợp đồng | Độ lệch chuẩn của tỷ lệ | Tỷ lệ nằm trong khoảng (±3 độ lệch) |
| ------------: | ----------------------: | ----------------------------------- |
|             1 |                9,9499 % | 0 % – 30,850 %                      |
|           100 |                0,9950 % | 0 % – 3,985 %                       |
|        10.000 |                0,0995 % | 0,702 % – 1,298 %                   |
| **1.000.000** |            **0,0099 %** | **0,970 % – 1,030 %**               |

Bán **một** hợp đồng: tỷ lệ tổn thất là 0% hoặc 100%. Không kinh doanh được.
Bán **một triệu**: gần như chắc chắn rơi vào 0,97%–1,03%.

Cùng một rủi ro. Chỉ khác số lượng.

> [!note] Cách hiểu đúng về "gộp rủi ro".
> Gộp rủi ro **không làm rủi ro biến mất** — tổng số nhà cháy
> mỗi năm vẫn thế. Cái nó làm biến mất là **vốn cần thiết**. [Mục 2 của chương trình](#13-chương-trình)
> đo bằng số: với 10 ngôi nhà, công ty phải giữ vốn dự trữ bằng **9,44 năm** tiền phí mới chịu được
> một năm xấu; với một triệu ngôi nhà, chỉ cần **0,03 năm** — tức 3% của một năm phí.

Đó là toàn bộ mô hình kinh doanh, và nó giải thích vì sao ngành này luôn hướng tới quy mô lớn.

### Aristotle biết trước hai nghìn năm

Shiller dẫn một đoạn trong ***De Caelo*** (`05 08:38`):

> [!quote]
> *"Thành công ở nhiều việc hoặc nhiều lần là khó. Chẳng hạn, ném ra cùng một mặt xúc xắc 10.000 lần
> thì bất khả thi, còn ném trúng một hai lần thì tương đối dễ."*

Shiller bình (`05 09:01`): Aristotle *"không có ngôn ngữ của xác suất, nhưng ông biết là ta không thể
gieo xúc xắc 1.000 lần và ra cùng một số mỗi lần."*

> [!note]
> Trực giác có trước công thức **hai nghìn năm**. Đó là mẫu hình lặp lại suốt cả bài này, và §2 là ví
> dụ rõ nhất.

---

## 2. Lá thư năm 1609 gửi Bá tước Oldenburg

Bảo hiểm có từ **La Mã cổ đại**, nhưng ở dạng rất hạn chế (`05 05:01`). Dạng phổ biến là **bảo hiểm
mai táng** — trả tiền tang lễ. Shiller giải thích động cơ (`05 05:29`): người thời cổ tin rằng phải
được chôn cất đúng cách, *"nếu không linh hồn sẽ lang thang mãi mãi"*. Nên các phường hội bán bảo
hiểm tang lễ.

Nhưng họ *"không có ý niệm rõ ràng về khái niệm gộp rủi ro"* (`05 05:48`). Shiller kể ông từng đọc
một hợp đồng bảo hiểm thời Phục hưng Ý dịch sang tiếng Anh, và *"nó gần như không nhận ra được là một
hợp đồng bảo hiểm"* — đầy ngôn ngữ tôn giáo (`05 06:14`).

Mô tả rõ ràng đầu tiên xuất hiện năm **1609**, và nó là **một lá thư nặc danh** gửi **Bá tước
Oldenburg** (`05 06:59`). Đề nghị của người viết: mỗi người nộp **1% giá trị nhà mỗi năm** vào một
quỹ, quỹ ấy xây lại nhà cho ai bị cháy.

Rồi câu Shiller trích nguyên văn (`05 07:41`), và nó đáng đọc kỹ:

> [!quote]
> *"không nghi ngờ gì rằng điều đó sẽ được chứng minh đầy đủ, nếu tính số nhà bị lửa thiêu trong một
> khu vực nhất định trong khoảng **30 năm**, thì tổn thất sẽ không hề lên tới số tiền thu được trong
> thời gian đó."*

Shiller bình (`05 08:09`): *"Ông ta không diễn đạt bất kỳ định luật toán học nào, nhưng đó là khái
niệm bảo hiểm."*

### Ông ta có đúng không?

[Mục 2 của chương trình](#13-chương-trình) kiểm đúng theo cách người viết đề xuất — cộng dồn 30 năm:

| Tỷ lệ nhà cháy/năm | Thu được | Phải chi ra |     Quỹ còn lại |
| -----------------: | -------: | ----------: | --------------: |
|             0,50 % |   60.000 |      30.000 |         +30.000 |
|         **1,00 %** |   60.000 |      60.000 | **0 — hoà vốn** |
|             1,20 % |   60.000 |      72.000 |         −12.000 |

Điểm hoà vốn nằm **đúng** ở tỷ lệ cháy = mức phí = 1%/năm. Người viết năm 1609 đặt cược rằng nhà
không cháy tới 1%/năm. **Ông ta đúng — nhưng không biết vì sao mình đúng.**

> [!note]
> Chỗ ông ta thiếu là §1. Không phải chỉ cần tỷ lệ **trung bình** đủ thấp, mà còn cần **đủ nhiều
> nhà** để tỷ lệ **thực tế** không lệch xa trung bình. Một quỹ 10 nhà với $p = 1\%$ vẫn có thể vỡ ngay
> năm đầu tiên.

Và đó là lý do Shiller nhấn mốc **1600** (`05 06:39`): bảo hiểm chỉ thành ngành *"cùng lúc một số
khái niệm toán học bắt đầu được phát triển. Đáng chú ý là khái niệm **xác suất** trở nên phổ biến hơn
vào những năm 1600."*

Cũng thập niên ấy, người ta bắt đầu lập **bảng tử vong** lần đầu tiên (`05 04:29` của phần sau,
`05 17:29`): *"Không có dữ liệu nào về tuổi lúc chết. Nó bắt đầu từ những năm 1600, vì người ta đang
xây dựng một ngành bảo hiểm và họ cần biết những thứ đó."*

> [!note]
> Thứ tự đáng nhớ: **trực giác (1609) → xác suất (1600s) → dữ liệu (1600s) → ngành**. Không phải
> ngược lại.

---

## 3. Bảo hiểm là một phát minh, và phát minh thì có bản vẽ

Đây là chủ đề Shiller nói rõ là ông muốn nhắc lại xuyên suốt khoá học (`05 02:12`): **các định chế
tài chính là những phát minh** — *"chúng là những cấu trúc mà ai đó phải thiết kế và làm cho chạy
đúng. Đôi khi chúng chạy không đúng."*

Ông đưa một phép so sánh gọn (`05 12:44`): *"Bạn có thể nghĩ ra ý tưởng làm một chiếc máy bay, nhưng
để nó thực sự bay được, và bay an toàn, lại là chuyện khác."*

Rồi ông liệt kê **bản vẽ** — những gì một ngành bảo hiểm cần có mới chạy được (`05 12:51`–`05 18:59`):

|    # | Thành phần                                                           | Vì sao cần                                            |
| ---: | -------------------------------------------------------------------- | ----------------------------------------------------- |
|    1 | **Thiết kế hợp đồng** xác định rủi ro, loại trừ rủi ro không phù hợp | chặn rủi ro đạo đức và lựa chọn ngược                 |
|    2 | **Định nghĩa tổn thất chính xác** và bằng chứng chứng minh tổn thất  | nếu mập mờ thì *"sẽ có tranh cãi pháp lý và bất mãn"* |
|    3 | **Mô hình toán về gộp rủi ro**                                       | công thức §1 — và nó **giả định độc lập**             |
|    4 | **Thu thập thống kê**, và đánh giá chất lượng thống kê ấy            | bảng tử vong                                          |
|    5 | **Hình thức pháp lý của công ty** — cổ phần hay tương hỗ             | ai chịu rủi ro nếu bốn khoản trên làm sai             |
|    6 | **Thiết kế quản lý nhà nước**                                        | xem dưới                                              |

Shiller giải thích khoản 6 kỹ nhất, và lập luận rất sắc (`05 18:26`):

> [!quote]
> *"Vấn đề của bảo hiểm là người ta sẽ đóng tiền vào trong rất, rất nhiều năm trước khi họ được nhận,
> đúng không? Nhất là nếu bạn mua bảo hiểm nhân thọ, bạn hy vọng **không bao giờ** phải nhận. Và thế
> thì bạn không biết được nó có chạy đúng hay không. Đó là lý do bạn cần quản lý nhà nước… **Nó không
> chạy nếu không có cơ quan quản lý, vì bạn sẽ không tin công ty bảo hiểm.**"*

> [!note]
> Đây là lập luận mạnh hơn vẻ ngoài, và nó khác lập luận quản lý ngân hàng ở [bài 3 §6](bai_03_ngan_hang.md#6-basel--tài-sản-có-rủi-ro-và-yêu-cầu-vốn).
> Ngân hàng bị quản lý vì **nhà nước bảo hiểm cho nó**, nên phải chặn rủi ro đạo đức. Bảo hiểm bị quản
> lý vì **sản phẩm của nó là một lời hứa 30 năm** mà người mua không có cách nào tự kiểm chứng. Hai lý
> do hoàn toàn khác nhau, dẫn tới hai bộ máy khác nhau — và §9 cho thấy chúng khác nhau tới mức nào.

Khoản 3 mới là chỗ đáng chú ý nhất. Shiller viết ra rồi tự đặt điều kiện lên nó (`05 17:05`): *"Cái
này giả định độc lập. Nếu bạn không giả định độc lập, bạn có thể làm những mô hình phức tạp hơn."*

Câu đó nghe như một chú thích kỹ thuật. Nó là chỗ AIG chết. Xem §5.

---

## 4. Chỗ gãy thứ nhất và thứ hai — rủi ro đạo đức, lựa chọn ngược

### Rủi ro đạo đức

Shiller cho biết cụm từ *moral hazard* xuất hiện **thế kỷ 19** để chỉ những tác động **không mong
muốn** của bảo hiểm lên hành vi con người (`05 13:25`).

Ví dụ kinh điển (`05 13:36`): mua bảo hiểm cháy nhà rồi **cố tình đốt nhà** để lấy tiền. Hoặc mua bảo
hiểm nhân thọ rồi **tự sát** để gia đình có tiền.

Shiller nói rõ mức nghiêm trọng (`05 13:54`): những kết cục ấy *"có thể **giết chết toàn bộ khái
niệm** bảo hiểm, vì nếu bạn không kiểm soát được rủi ro đạo đức thì rõ ràng cả hệ thống sẽ không chạy."*

Hai cách chặn:

1. **Loại trừ** những nguyên nhân dễ bị lợi dụng — ví dụ những nguyên nhân tử vong trông giống tự sát
   (`05 14:16`).
2. **Không bảo hiểm quá giá trị thật** (`05 14:28`). Lập luận của Shiller rất gọn: nếu bảo hiểm không
   phủ hết giá trị căn nhà thì *"chẳng có động cơ nào để đốt nó. Bán quách căn nhà đi còn hơn. Đốt
   làm gì nếu vẫn lỗ một ít."*

> [!note]
> Cách thứ hai chính là **đồng bảo hiểm** — cùng cơ chế đã làm Northern Rock sụp ở
> [bài 3 §5](bai_03_ngan_hang.md#5-bảo-hiểm-tiền-gửi-và-bốn-lần-thử). Đáng chú ý là ở đây nó là **tính
> năng**, còn ở đó nó là **lỗi**. Khác biệt: bảo hiểm nhà cần người mua **giữ phần da thịt trong cuộc
> chơi**; bảo hiểm tiền gửi cần người gửi **không có lý do gì để xếp hàng**. Cùng một công cụ, hai mục
> tiêu ngược nhau. §12 cho thấy Việt Nam từng dùng nhầm chỗ.

### Lựa chọn ngược

Shiller định nghĩa ở `05 15:07`: lựa chọn ngược xảy ra khi **người đăng ký biết mình rủi ro cao hơn**.

Ví dụ ông đưa (`05 15:31`): người biết mình mắc bệnh nan y sắp chết *"sẽ đổ xô đi ký hợp đồng bảo
hiểm nhân thọ của bạn."* Hệ quả (`05 15:41`): công ty phải **tính phí rất cao**, *"và điều đó sẽ đẩy
những người khác, những người không biết mình sắp chết, ra khỏi việc mua bảo hiểm."*

Ông gọi đây là *"vấn đề nền tảng"* (`05 15:58`).

### Vòng xoáy tử thần, đo bằng số

Câu của Shiller mô tả **một** vòng. Nhưng nó không dừng ở một vòng: người khoẻ rời đi làm phí tăng,
phí tăng lại đẩy nhóm khoẻ kế tiếp ra. [Mục 4 của chương trình](#13-chương-trình) chạy vòng lặp đó
tới khi đứng yên — 100 người, chi phí y tế kỳ vọng từ 10 tới 1.000, ai cũng sẵn sàng trả tối đa 1,2
lần chi phí kỳ vọng **của chính mình**:

| Vòng |     Phí | Người còn mua | Ai vừa rời bỏ |
| ---: | ------: | ------------: | ------------: |
|    1 |     505 |           100 |      42 người |
|    2 |     715 |            58 |      17 người |
|    3 |     800 |            41 |       7 người |
|    4 |     835 |            34 |       3 người |
|    7 | **860** |        **29** |  0 — đứng yên |

Cân bằng: **29 trên 100 người** còn bảo hiểm. **71 người không có gì.** Phí tăng từ 505 lên 860.

📌 **Không ai lừa dối ai. Không ai hành xử phi lý.** Người khoẻ rời bỏ vì phí cao hơn giá trị họ nhận
được — đúng như thế. Đây là cùng một cấu trúc với bank run ở
[bài 3 §3](bai_03_ngan_hang.md#3-diamonddybvig--vì-sao-một-ngân-hàng-lành-mạnh-vẫn-sập): **hành vi
hợp lý của từng cá nhân phá huỷ định chế mà tất cả đều cần**.

Buộc mọi người mua thì vòng xoáy biến mất: phí **505** cho cả 100 người — **rẻ hơn 41%** so với cân
bằng trên, **và phủ 100% dân số**.

Đó chính là cơ chế Shiller mô tả ở `05 62:04`: *"bằng cách buộc mọi người đăng ký, công ty bảo hiểm
không còn vấn đề chỉ người ốm mới đăng ký. Mọi người đều đăng ký, nên họ có thể hạ phí."*

> [!warning]
> Shiller nói rõ luật 2010 **không bắt buộc mua** (`05 61:39`) — nó **đánh thuế nếu không mua**,
> khoảng *"700 đô một năm"*. Về mặt kinh tế, mức phạt phải đủ lớn thì mới thay được lệnh bắt buộc; nếu
> phạt rẻ hơn phí, vòng xoáy vẫn chạy, chỉ chậm hơn.

### Rủi ro đạo đức trong y tế: bác sĩ

Shiller thêm một dạng rủi ro đạo đức khác, không nằm ở người mua mà ở **người cung cấp dịch vụ**
(`05 53:36`): với bảo hiểm y tế tư, bác sĩ *"có động cơ vắt sữa công ty bảo hiểm, đúng không? Họ có
thể chỉ định quá nhiều thủ thuật."*

Rồi ông nói một câu khá thẳng (`05 53:50`): *"Bác sĩ không quan tâm bạn — bệnh nhân — sống lâu. Họ chỉ
có động cơ làm thật nhiều thủ thuật."* Và lập tức tự sửa: *"họ sẽ làm, nếu họ có nhân cách đạo đức —
nhưng **động cơ tài chính thì sai**."*

Giải pháp là **HMO** (`05 54:46`): Đạo luật HMO **1973**, trong đó *"bác sĩ được trả lương, không
được trả theo thủ thuật"* — nên họ *"không có động cơ mổ cho bạn một ca bạn không cần, vì lương họ
không tăng."*

Shiller kể một chi tiết địa phương thú vị (`05 55:53`): **Yale Health Plan** có từ **1971**, tức
**trước** Đạo luật HMO. Provost Charles Taylor thích ý tưởng ấy, và *"Yale còn không đợi chính phủ
bắt buộc, chúng tôi làm trước."*

---

## 5. Chỗ gãy thứ ba — khi độc lập không còn

Đây là chỗ gãy nguy hiểm nhất, và cũng là chỗ Shiller **nói qua nhanh nhất**. Ông nhắc điều kiện độc
lập đúng một lần ở `05 17:05`, rồi dùng nó để chẩn đoán AIG ở `05 26:21` — nhưng không bao giờ đưa ra
con số. Mục này đưa.

Nếu các tổn thất **tương quan** với nhau ở mức $\rho$, công thức §1 thành:

$$\text{sd} = \sqrt{\frac{p(1-p)\,\bigl[1 + (n-1)\rho\bigr]}{n}}$$

Cho $n \to \infty$, số hạng $n$ triệt tiêu và còn lại một **chặn dưới**:

$$\text{sd}_{\min} = \sqrt{p(1-p)\,\rho}$$

**Độ lệch chuẩn không về 0 nữa.** Nó dừng ở một mức mà **không lượng hợp đồng nào vượt qua được**.
[Mục 3 của chương trình](#13-chương-trình) tính:

|        ρ |  n = 100 | n = 10.000 | n = 1.000.000 | Chặn dưới |
| -------: | -------: | ---------: | ------------: | --------: |
| **0,00** | 0,9950 % |   0,0995 % |  **0,0099 %** |  0,0000 % |
|     0,01 | 1,4036 % |   0,9999 % |      0,9950 % |  0,9950 % |
|     0,05 | 2,4270 % |   2,2270 % |      2,2249 % |  2,2249 % |
| **0,25** | 5,0490 % |   4,9757 % |  **4,9749 %** |  4,9749 % |
|     1,00 | 9,9499 % |   9,9499 % |      9,9499 % |  9,9499 % |

📌 Với $\rho = 0{,}25$, bán **một triệu** hợp đồng vẫn chịu độ lệch chuẩn **4,97%** — gấp **500 lần**
trường hợp độc lập. Quy mô không cứu được gì.

Và nhìn cột ρ = 0,01: chỉ **một phần trăm** tương quan cũng đủ để một triệu hợp đồng chỉ tốt ngang
**một trăm** hợp đồng độc lập.

> [!note] Đây là chỗ để nhớ.
> Ngành bảo hiểm không sợ $p$ lớn — $p$ lớn thì cứ tính phí cao lên. Nó sợ
> $\rho$ **khác không**, vì $\rho$ phá huỷ chính cơ chế mà cả ngành đứng trên.

Và điều này giải thích luôn một chi tiết Shiller nêu ở cuối buổi mà nhiều người coi là kỳ quặc
(`05 67:02`): hợp đồng bảo hiểm truyền thống **loại trừ chiến tranh và khủng bố**. Lý do ông đưa
(`05 67:12`): *"họ cảm thấy phải loại trừ nó, vì đó là những rủi ro **tương quan**, đúng không? Nếu có
chiến tranh, các xác suất thiệt hại **không độc lập**."*

Chiến tranh và khủng bố không bị loại trừ vì **lớn**. Chúng bị loại trừ vì **ρ ≈ 1**. Ở cột cuối
bảng trên, ρ = 1 nghĩa là bán một triệu hợp đồng cũng bằng bán một hợp đồng.

> [!warning]
> Nhưng Shiller nêu luôn nghịch lý (`05 67:30`): *"hoá ra đây lại chính là những rủi ro mà ta lo
> lắng nhất."* Mỹ giải bằng **TRIA — Đạo luật Bảo hiểm Rủi ro Khủng bố, 2002** (`05 67:36`): buộc công
> ty bảo hiểm **phải chào** bảo hiểm khủng bố, đổi lại **chính phủ gánh phần lớn tổn thất** nếu xảy ra
> thảm hoạ quốc gia.

Tức là: khi ρ tiến tới 1, thị trường không làm được nữa và **nhà nước trở thành người tái bảo hiểm
cuối cùng**. Cùng kết luận với [bài 3 §5](bai_03_ngan_hang.md#5-bảo-hiểm-tiền-gửi-và-bốn-lần-thử) —
*"lớp bảo đảm sau cùng thậm chí không được viết ra"* — chỉ khác là lần này nó **được** viết ra thành
luật.

### Trái phiếu thảm hoạ

Cách thứ hai để đối phó với ρ cao: đừng gộp trong một nước, **rải ra cả thế giới**. Shiller giới thiệu
**trái phiếu thảm hoạ** (`05 68:44`): một trái phiếu chỉ phải hoàn trả **nếu thảm hoạ không xảy ra**.

Ví dụ ông đưa: chính phủ Mexico phát hành trái phiếu tháng 5/2006, chỉ phải trả nếu Mexico **không**
có động đất lớn. Lý lẽ (`05 69:47`): *"Chính phủ Mexico không đủ lớn để quản lý rủi ro đó một cách
hiệu quả. Tốt hơn là rủi ro được rải ra khắp thế giới."*

> [!warning]
> Shiller đọc quy mô đợt phát hành là **160 tỷ đô**. Con số thật là **160 triệu** — xem
> [§10](#10-bốn-chỗ-video-nói-sai).

---

## 6. AIG — chín mươi năm dựng, ba năm sập

Shiller chọn AIG làm ví dụ vì hai lý do (`05 19:24`): nó từng là công ty bảo hiểm lớn nhất thế giới,
**và** vì Hank Greenberg sẽ tới lớp — nên "hãy dùng AIG."

### Lịch sử

|   Năm | Sự kiện                                                                             |
| ----: | ----------------------------------------------------------------------------------- |
|  1919 | **Cornelius Vander Starr** lập **American Asiatic Underwriters** tại **Thượng Hải** |
| ~1949 | chuyển trụ sở về New York, ngay trước khi Mao lên nắm quyền                         |
|  1968 | Starr mất; Greenberg kế nhiệm                                                       |
|  2005 | Greenberg buộc phải rời đi                                                          |

Shiller nêu một quan sát đáng chú ý (`05 21:02`): *"khá thú vị là công ty bảo hiểm lớn nhất thế giới
nổi lên từ Thượng Hải, và **một trong những ngân hàng lớn nhất thế giới cũng thế — HSBC**."* Rồi hỏi
lớp có biết HSBC nghĩa là gì không: **Hong Kong and Shanghai Banking Corporation**.

Và ông tóm cả cấu trúc quản trị trong một câu (`05 22:28`): **hai người điều hành công ty này trong
gần một thế kỷ.** Sau 2005, Greenberg được ba CEO kế nhiệm trong sáu năm — *"chuyện thường"*.

> [!warning]
> Shiller nói Starr bổ nhiệm Greenberg làm CEO **năm 1962**. Số học của chính ông ngay sau đó
> (49 năm + 37 năm) đòi mốc **1968** — xem [§10](#10-bốn-chỗ-video-nói-sai).

### Dachau

Shiller kể một chuyện ngoài lề nhưng ông rõ ràng muốn lớp nghe (`05 22:54`): Greenberg nhập ngũ Mỹ,
đánh Thế chiến II, và một trong những nhiệm vụ của ông là **giải phóng Dachau**.

Rồi (`05 23:32`): tại một cuộc họp của Council on Foreign Relations, Greenberg gặp **Mahmoud
Ahmadinejad**, tổng thống Iran. Ahmadinejad nói gì đó nghi ngờ Holocaust có thật hay không.

> [!quote] 05 23:47
> *"Greenberg đứng dậy phẫn nộ và nói: **nó đã xảy ra. Tôi đã thấy. Tôi đã ở đó.**"* (`05 23:47`)

Shiller kể tiếp về Geoffrey Hartman, giáo sư văn học ở Yale, và vợ ông là Renee — bà từng ở một trại
tập trung tại Bratislava và **bị bỏ đói tới chết**. Shiller hỏi bà vì sao họ bỏ đói bà. Bà trả lời
(`05 24:46`): *"Chúng tôi không biết. Chúng tôi nghĩ có lẽ họ giữ chúng tôi làm con tin, hay gì đó."*

> [!note]
> Đoạn này không có nội dung tài chính nào. Nhưng nó là lý do buổi 14 nặng ký: người sắp bước vào lớp
> không phải một CEO đọc slide.

### Vì sao AIG sập — theo Shiller

Chẩn đoán của Shiller rất dứt khoát (`05 26:21`):

> [!quote]
> *"Lý do họ phải được cứu, theo tôi, **gần như hoàn toàn là do một thất bại của giả định độc lập**."*

Mô hình rủi ro của AIG cho rằng (`05 26:41`): *"không sao khi ta nhận rủi ro giá nhà giảm, vì giá nhà
**không bao giờ có thể giảm ở mọi nơi**. Chúng có thể giảm ở một thành phố, nhưng chuyện đó không ảnh
hưởng tới ta. Đó chỉ là một thành phố, và mọi thứ sẽ bù trừ nhau."*

Rồi (`05 27:01`): *"giá nhà giảm ở mọi nơi, **đúng chính xác cái điều họ nghĩ là không thể xảy ra**."*

Đó là §5 nói bằng lời. AIG không sai về $p$. Họ sai về $\rho$.

### Quy mô

| Khoản                                        |                               Số |
| -------------------------------------------- | -------------------------------: |
| Tổng cam kết cứu trợ của chính phủ liên bang |       **182 tỷ đô** (`05 27:54`) |
| Cổ đông AIG mất                              | **hơn 90%** giá trị (`05 32:49`) |
| Gộp cổ phiếu ngược, tháng 7/2009             |         **1 ăn 20** (`05 32:56`) |

Shiller nói thẳng một điều trái với dư luận thời đó (`05 33:58`): *"cơn giận của công chúng về việc
cứu AIG thực ra hơi **không đúng chỗ**, vì họ đã mất gần như tất cả."* Cổ đông bị pha loãng gần sạch;
chính phủ nhận cổ phiếu ưu đãi ở giá rất thấp.

Rồi ông chỉ ra chỗ cơn giận **đúng** chỗ (`05 34:33`):

> [!quote]
> *"Cơn giận thật sự là ở chỗ **các đối tác kinh doanh của AIG không mất gì cả**, đáng chú ý là
> **Goldman Sachs**, bên đứng phía kia của các hợp đồng với AIG. Nó **không mất một xu nào**."*

Vì sao chính phủ làm thế? Shiller đưa lý do khá phũ (`05 34:58`): chính phủ *"không biết"* liệu
Goldman Sachs có sập theo không — *"vì họ không có thông tin, vì cơ quan quản lý đã **không thu thập**
loại thông tin đó."*

> [!note]
> Ghi nhớ câu này. §7 cho thấy Greenberg đến lớp và nói **cùng một điều** về Goldman — nhưng với một
> kết luận khác hẳn.

---

## 7. Greenberg kể lại cùng câu chuyện, và không khớp

Ba tuần sau, Greenberg ngồi trước lớp. Shiller giới thiệu ông bằng đúng những gì đã kể ở buổi 5, rồi
đặt yêu cầu (`14 01:13`): nói về chuyện tài chính, nhưng *"như chúng tôi vẫn nhấn mạnh trong khoá học
này, nó **không chỉ là mô hình CAPM toán học** — nó là chuyện tạo động lực cho con người, chuyện tìm
những người có **nhân cách** phù hợp."*

### Cách Greenberg mô tả việc mình đã làm

Ông kể mình nhập ngũ **năm 17 tuổi**, sửa giấy khai sinh thành 18 (`14 02:04`), đổ bộ Normandy ngày
D-Day, đi hết châu Âu, gặp quân Nga ở Linz. Rồi phải quay lại học nốt trung học — *"một trong những
quãng khó khăn nhất đời tôi"* (`14 02:52`). Học luật xong thì Chiến tranh Triều Tiên nổ ra.

Cách ông vào ngành bảo hiểm đáng kể lại nguyên văn (`14 04:21`–`14 05:31`): ông ghé Continental
Casualty hỏi việc, gặp giám đốc nhân sự *"khá khó chịu"*. Ông vừa từ Triều Tiên về, *"bốn ngày trước
đó tôi vẫn còn bùn trên giày"*. Nên ông xuống tầng trệt, đọc bảng danh mục, đi thẳng vào phòng một phó
chủ tịch và nói: **"ông có một giám đốc nhân sự không ra gì."** Kết quả: ông được nhận việc.

Nghề đầu tiên: **thẩm định viên sơ cấp** — *"bạn phân tích rủi ro và quyết định công ty có muốn nhận
rủi ro đó hay không"* (`14 05:37`).

### Bốn thứ Greenberg cho là đã tạo nên AIG

**1. Đa dạng hoá địa lý là chiến lược, không phải hệ quả** (`14 12:43`):

> [!quote]
> *"ngành bảo hiểm tài sản và thương vong là một ngành rất biến động. Bạn chịu động đất. Bạn chịu bão.
> Bạn chịu các môi trường kinh tế khác nhau… nên chúng tôi muốn đa dạng hoá không chỉ trong ngành tài
> sản — thương vong, mà **trên toàn cầu**. Đó là lý do chúng tôi vào rất nhiều nước."*

> [!note]
> Đọc câu đó cạnh §5 thì nó là **một chiến lược giảm ρ**. Greenberg không dùng chữ tương quan, nhưng
> ông đang mô tả chính xác việc đi tìm những rủi ro không cùng sập một lúc. Và điều đó làm những gì xảy
> ra sau 2005 càng đáng chú ý: AIG chuyển từ đa dạng hoá địa lý sang tập trung vào **một** rủi ro duy
> nhất — bất động sản Mỹ.

**2. Tỷ lệ chi phí** (`14 13:26`): ngành chạy ở khoảng **30%**; AIG chạy ở **19%**.

**3. Không hợp đồng lao động, và trần lương** (`14 22:16`):

- *"Không ai được hưởng quá **1 triệu đô** tiền lương. Tôi đặt ra quy tắc đó."*
- *"Thứ hai, không ai có hợp đồng. Bạn ở lại AIG vì bạn yêu nó."*

Thay vào đó là **còng tay vàng** (`14 23:56`): các công ty tư nhân sở hữu cổ phiếu AIG phân bổ cổ
phiếu cho cá nhân theo hiệu quả, hai năm một lần, **nhận khi nghỉ hưu**. Rời công ty thì bỏ lại.

Chi tiết Greenberg nhấn (`14 24:55`): *"**Nó không tốn của AIG đồng nào.** Cổ đông đại chúng của AIG
không phải gánh chi phí nào cho việc đó."*

> [!note]
> Đây là một thiết kế đãi ngộ đáng phân tích, và nó ngược hẳn thông lệ ngày nay. Chi phí do **cổ đông
> kiểm soát** gánh, không phải cổ đông đại chúng. Nhưng nó cũng có mặt tối: nó khiến ban điều hành trung
> thành với **C.V. Starr**, không phải với AIG.

**4. Mở cửa thị trường bằng chính phủ Mỹ** (`14 15:09`), và ông không hề vòng vo:

> [!quote]
> *"Chính phủ Mỹ rất ủng hộ chúng tôi, và nếu người Nhật không mở thị trường cho chúng tôi, chúng tôi
> **làm việc rất tích cực để ngăn** một số công ty của họ làm ăn ở Mỹ… **Chúng tôi không ngần ngại
> dùng chính phủ Mỹ** để hỗ trợ mong muốn mở cửa thị trường."*

Trung Quốc mất từ **1975 tới 1992** mới ra được giấy phép bảo hiểm nhân thọ đầu tiên cấp cho một công
ty nước ngoài (`14 16:41`) — và AIG sở hữu **100%**, trong khi các công ty nước ngoài sau đó chỉ được
49%.

### Và cách ông kể chuyện AIG sập

Đây là chỗ hai buổi giảng tách nhau.

**Về Spitzer**, Greenberg giận dữ (`14 29:34`–`14 31:34`): sau Enron, văn phòng Tổng chưởng lý New
York *"trở thành một văn phòng bị chính trị hoá"*, dùng làm **bàn đạp tranh cử thống đốc**. Ông liệt
kê những người Spitzer nhắm tới — con trai ông là Jeff ở Marsh & McLennan, Sandy Weill ở Citigroup,
Merrill Lynch — rồi kết: *"Ông ta **phá huỷ vài trăm tỷ đô giá trị**."*

Về việc mình bị buộc rời đi (`14 31:01`): Spitzer *"đe doạ hội đồng quản trị AIG rằng nếu tôi không rời
công ty, ông ta sẽ truy tố công ty."*

Và chi tiết cay đắng nhất (`14 31:23`): Spitzer lên truyền hình quốc gia cáo buộc ông gian lận kế
toán, rồi *"ngay trước Lễ Tạ ơn, ông ta **rút toàn bộ các cáo buộc**, vì chẳng ai đọc báo vào tối
trước Lễ Tạ ơn."*

> [!warning] Năm 2017, Greenberg thừa nhận ông đã khởi xướng hai giao dịch giả.
> Xem
> [§11](#11-đối-chiếu-2026). Cả lời kể của ông **và** lời bênh vực của Shiller ở `05 25:49` đều không
> đứng vững.

**Về nguyên nhân sập**, Greenberg đưa một chuỗi nhân quả hoàn toàn khác Shiller:

1. **Các cuộc họp bị bỏ.** Ông mô tả hai cuộc họp cố định mỗi tuần — thứ Hai về toàn bộ hoạt động,
   thứ Tư về **phòng hộ và quản trị rủi ro** (`14 33:13`–`14 33:45`). Người kế nhiệm Martin Sullivan
   *"vì lý do gì đó đã ngừng những cuộc họp ấy. Tôi không hiểu vì sao, nhưng ông ta đã làm thế."* Và
   (`14 34:02`): *"điều rất đáng lo là **uỷ ban kiểm toán của hội đồng quản trị AIG biết chuyện đó và
   không làm gì cả**."*

2. **Khối lượng bùng nổ.** AIG Financial Products *"làm nhiều hợp đồng hoán đổi rủi ro tín dụng trong
   **chín tháng** sau khi tôi rời công ty hơn là chúng tôi đã làm trong **bảy năm**"* (`14 34:18`).

3. **Điều khoản bị đổi.** Đây là luận điểm trung tâm của Greenberg (`14 34:54`):

> [!quote]
> *"Ban đầu, những công cụ đó **phải vỡ nợ** trước khi một CDS phản ứng… Đến một lúc nào đó, điều đó
> bị đổi, nên bạn không cần — công cụ đó **không cần vỡ nợ, nó chỉ cần mất giá**. Và bạn phải đặt thế
> chấp… bằng đúng phần giá trị đã mất, **kể cả khi khoản lỗ đó chưa được hiện thực hoá**."*

4. **Không có nơi định giá.** Không có sàn giao dịch cho CDO nên *"mỗi nhà môi giới có một giá khác
   nhau"* (`14 37:07`). Greenberg quy trách nhiệm cho Bộ Tài chính thời Clinton dưới thời **Bob Rubin**
   đã bác đề xuất lập sàn và quản lý CDS (`14 36:49`).

5. **Và Goldman đưa ra giá thấp nhất** (`14 37:24`): *"Goldman Sachs có mức giá thấp nhất trong số các
   CDO đang bị đòi thế chấp. Và vì AIG Financial Products làm ăn rất nhiều với Goldman Sachs, họ bị
   đòi thế chấp ngày càng nhiều. **Họ hết tiền mặt.**"*

📌 **Chỗ hai người gặp nhau.** Shiller ở `05 34:33` nói cơn giận đúng chỗ là Goldman không mất xu nào.
Greenberg ở `14 50:52` nói: *"AIG đã bị dùng để cứu nhiều bên, **bao gồm Goldman Sachs**."*

Một giáo sư Nobel và người CEO bị mất công ty, xuất phát từ hai phía đối lập, **đồng ý với nhau về
điểm này**. Đó là dữ kiện đáng tin nhất trong cả hai buổi giảng.

### Con số Greenberg đưa

| Khoản                                    | Số                                                          |
| ---------------------------------------- | ----------------------------------------------------------- |
| Vay từ Fed New York                      | **85 tỷ đô, lãi 14,5%** (`14 41:14`)                        |
| Fed lấy                                  | **79,9%** vốn chủ sở hữu (`14 41:20`)                       |
| *"Về cơ bản họ đã quốc hữu hoá công ty"* | (`14 41:29`)                                                |
| Chính phủ sở hữu, tại thời điểm giảng    | **92%** (`14 43:03`)                                        |
| Đáng lẽ thương lượng được                | **40–60 xu trên đồng**; Fed bắt trả **100 xu** (`14 41:53`) |

Và ông nói rõ ông đã bị hỏi điều này trước Quốc hội (`14 50:16`): *"chính phủ có quyền gì mà lấy về
cơ bản 92% của AIG? Với tôi, đó là một **vụ tước đoạt bất hợp pháp**."* Ông so sánh: Citigroup được
cứu và chính phủ lấy khoảng **30%** vốn — *"khác với 92%."*

Câu cuối trước phần hỏi đáp (`14 43:28`): *"Vậy tôi có cay đắng không? **Có. Tôi rất cay đắng.**"*

### Chẩn đoán chung của Greenberg về khủng hoảng

Khi được hỏi vì sao cả nước rơi vào cảnh đó, ông liệt kê (`14 45:16`–`14 49:37`):

1. Chính sách thời Clinton muốn **ai cũng sở hữu nhà**, *"không phân biệt mấy chuyện bạn có đủ khả
   năng hay không"*.
2. **Ngân hàng địa phương mất phần da thịt trong cuộc chơi** — Fannie/Freddie mua lại khoản vay, ngân
   hàng chỉ còn phục vụ hồ sơ, *"không còn dính líu tài chính nào sau khi khoản vay được bán đi"*
   (`14 46:01`).
3. **Ngân hàng đầu tư dùng đòn bẩy 30–40 lần** vốn, *"từ khoảng năm sáu lần… lên 40, 50, 30 lần"*.
   Và: *"**SEC chỉ đơn giản làm ngơ.**"* (`14 46:48`)
4. **Đa dạng hoá giả** — gom khoản vay *"từ đông sang tây sang nam"* rồi tuyên bố đa dạng hoá tốt nên
   *"nó sẽ được xếp hạng AAA"*. Các tổ chức xếp hạng *"chiều theo họ, chẳng phân tích gì mấy"*
   (`14 47:38`).
5. **Điều khoản CDS bị đổi** — như trên.
6. **Kế toán ghi nhận theo giá thị trường**, đúng lúc xấu nhất (`14 48:51`).

📌 Điểm **4** đáng dừng lại. Greenberg đang mô tả **chính xác** thất bại ρ ở §5 — nhưng ở một chỗ khác:
không phải trong sổ sách của AIG, mà trong **hồ sơ xếp hạng** của các CDO mà AIG bảo hiểm. Cùng một
sai lầm, hai nơi, cùng một lúc.

---

## 8. Hai chẩn đoán, và vì sao cần cả hai

|                  | Shiller (buổi 5)         | Greenberg (buổi 14)                            |
| ---------------- | ------------------------ | ---------------------------------------------- |
| Nguyên nhân      | giả định **độc lập** gãy | **điều khoản thế chấp** của CDS bị đổi         |
| Loại rủi ro      | thống kê                 | hợp đồng                                       |
| Khoản lỗ là      | **thật**                 | bị **phóng đại**                               |
| Hệ quả trực tiếp | vốn không đủ             | **tiền mặt** không đủ                          |
| Sửa bằng cách    | mô hình đúng ρ           | quay lại kích hoạt-khi-vỡ-nợ, lập sàn định giá |

[Mục 5 của chương trình](#13-chương-trình) chạy cả hai trên cùng một sổ sách mô hình — danh nghĩa 80
tỷ đô, thị trường định giá tài sản cơ sở mất 30%, nhưng rốt cuộc chỉ 5% thực sự vỡ nợ:

| Thiết kế hợp đồng                              |                           Tiền phải chi ra |
| ---------------------------------------------- | -----------------------------------------: |
| **A.** Kích hoạt khi **vỡ nợ** (thiết kế gốc)  |       **4 tỷ đô** — trả dần theo nhiều năm |
| **B.** Kích hoạt khi **mất giá** (sau khi đổi) | **24 tỷ đô** — ngay lập tức, bằng tiền mặt |

Cùng một sổ sách. Cùng một thế giới thực. Khác nhau **một điều khoản** — và thiết kế B đòi tiền mặt
gấp **6 lần**, đòi **ngay**.

Greenberg ở `14 36:23`: *"Tôi không quan tâm bạn to đến đâu, bạn hết tiền mặt — và họ hết thật."*

Và ông đưa một dữ kiện kiểm chứng được (`14 62:06`): *"nếu bạn nhìn lại tất cả những CDO mà các CDS
đó bảo hiểm, **phần lớn đã hồi phục giá trị**. Có một sự sụt giảm giá trị tạm thời, nhưng chúng
**không vỡ nợ**."*

📌 **Hai chẩn đoán không loại trừ nhau — chúng nhân nhau.**

- Nếu ρ đúng như mô hình AIG giả định, thị trường không sụp 30%, và điều khoản thế chấp **chẳng bao
  giờ bị kích hoạt**.
- Nếu điều khoản vẫn là "chỉ khi vỡ nợ", thì ρ sai vẫn gây lỗ 4 tỷ — đau, nhưng **không làm hết tiền
  mặt trong vài tuần**.

Cần **cả hai** mới ra được tháng 9/2008. Rủi ro thống kê và rủi ro hợp đồng nhân nhau, không cộng lại.

> [!note]
> Đây cũng là lý do hai người có thể cùng đúng mà nghe như đang cãi nhau. Shiller trả lời câu hỏi
> *"khoản lỗ đến từ đâu?"*; Greenberg trả lời câu hỏi *"vì sao nó xảy ra nhanh đến thế?"*. Trong một
> cuộc khủng hoảng thanh khoản, câu thứ hai mới là câu giết người — đúng như
> [bài 3 §3](bai_03_ngan_hang.md#3-diamonddybvig--vì-sao-một-ngân-hàng-lành-mạnh-vẫn-sập) đã cho thấy
> với một ngân hàng thừa tài sản mà vẫn sập.

---

## 9. Quỹ bảo lãnh — và mẹo chia nhỏ không dùng được

Shiller hỏi lớp một câu mà ông đoán ít người biết (`05 36:01`): ngân hàng có FDIC, còn **bảo hiểm thì
có gì tương đương không?**

Có: **quỹ bảo lãnh bảo hiểm cấp bang**. Quỹ đầu tiên là **New York, 1941**; Connecticut có từ **1972**
(`05 37:17`–`05 37:39`).

Rồi Shiller đặt câu hỏi hay (`05 38:02`): *"vậy sao quỹ bảo lãnh bảo hiểm không xử lý được AIG?"*

Câu trả lời (`05 38:12`): các quỹ này *"để bảo vệ **người nhỏ**"*. AIG **quá lớn** so với chúng.

### Ba khác biệt so với FDIC

**1. Mức trần thấp hơn nhiều.** Connecticut và New York — *"hai bang hào phóng nhất"* — trả tối đa
**500.000 đô**; một bang điển hình chỉ **300.000 đô** (`05 38:41`).

Shiller làm nó cụ thể bằng một phép tính đời thường (`05 39:04`): bạn mua bảo hiểm nhân thọ cho gia
đình, hai đứa con, định cho chúng học Yale — *"riêng tiền học đã khoảng 500.000 đô."* Nếu đó là tất cả
những gì bảo hiểm trả thì *"nó không lớn."*

Kết luận của ông (`05 39:25`): **"những quỹ này nhỏ, chúng không bảo lãnh đủ cho bạn."**

**2. Mẹo chia nhỏ không dùng được.** Đây là khác biệt kỹ thuật quan trọng nhất (`05 39:40`):

Với FDIC, *"tất cả những gì bạn làm là chia tiền ra nhiều ngân hàng. Nếu bạn có 2,5 triệu, bạn gửi vào
10 ngân hàng khác nhau. FDIC sẽ bảo hiểm từng cái một."*

Với quỹ bảo lãnh Connecticut: *"họ giới hạn bạn ở 500.000 đô, **bất kể bạn có bao nhiêu hợp đồng**."*

| Mệnh giá hợp đồng | Connecticut / NY | Bang điển hình | % được phủ |
| ----------------: | ---------------: | -------------: | ---------: |
|        300.000 đô |          300.000 |        300.000 |      100 % |
|        500.000 đô |          500.000 |        300.000 |      100 % |
|      1.000.000 đô |          500.000 |        300.000 |   **50 %** |
|      2.000.000 đô |          500.000 |        300.000 |   **25 %** |

**3. Không được quảng cáo.** Shiller nêu chi tiết này với vẻ thấy nó lạ (`05 40:22`): Connecticut
**không cho** công ty bảo hiểm quảng cáo rằng mình được bảo lãnh — *"ngược hẳn với bảo hiểm tiền gửi,
nơi FDIC **bắt buộc** họ phải treo biển rằng mình được bảo hiểm."* Rồi: *"Đó là lý do bạn không nghe
nói về nó."*

> [!note] Khác biệt thứ ba không vô tình, và nó là chỗ hay nhất của mục này.
> Bảo hiểm tiền gửi **phải
> được biết** mới chặn được bank run — công dụng của nó nằm ở chỗ nó **thay đổi kỳ vọng**, đúng như
> [bài 3 §5](bai_03_ngan_hang.md#5-bảo-hiểm-tiền-gửi-và-bốn-lần-thử). Quỹ bảo lãnh bảo hiểm thì **không
> có bank run nào để chặn**: không ai xếp hàng đòi rút hợp đồng nhân thọ. Nên nó im lặng được — và việc
> cấm quảng cáo còn giảm được rủi ro đạo đức, vì người mua buộc phải tự nhìn vào công ty bảo hiểm.

Shiller rút ra đúng bài học ấy (`05 40:42`): *"bạn phải **nhìn vào công ty bảo hiểm** mà bạn mua bảo
hiểm từ đó."*

### Cấp bang, không phải cấp liên bang

Một đặc thù Mỹ mà Shiller nhấn (`05 41:24`): bảo hiểm được quản lý **hoàn toàn** ở cấp bang, do
**Đạo luật McCarran–Ferguson 1945**. Hệ quả: *"bạn có **50 cơ quan quản lý khác nhau** ở Mỹ. Mỹ là
một nơi đặc biệt khó xử lý."*

Chất keo duy nhất là **NAIC — Hiệp hội Uỷ viên Bảo hiểm Quốc gia** (`05 42:54`), mà Shiller nói rõ
*"không phải một tổ chức nhà nước, nó là một hiệp hội không có định nghĩa hiến định hay chính quyền
nào."* Nó soạn **luật mẫu** để các bang tự áp dụng — *"nếu không, chúng ta sẽ có hỗn loạn hoàn toàn
trong quản lý bảo hiểm."*

Sau AIG, **Dodd-Frank 2010** lập **Văn phòng Bảo hiểm Liên bang**. Nhưng Shiller cảnh báo đừng hiểu
nhầm (`05 44:34`): *"nghe như chính phủ liên bang Mỹ đang bước vào ngành bảo hiểm. Nhưng thật ra
**không**."* Văn phòng này chỉ **thu thập thông tin** để phát hiện công ty nào đang tạo ra loại rủi ro
mà AIG đã tạo ra.

Và Shiller nói thẳng lý do tồn tại của nó (`05 46:01`), nối lại đúng §5:

> [!quote]
> *"họ chỉ đang nhìn vào vấn đề mà tôi đã nêu ở đầu buổi: **toàn bộ mô hình bảo hiểm giả định rủi ro
> độc lập**, một dạng độc lập nào đó, để việc gộp rủi ro xảy ra được. Nhưng nếu nó không thực sự độc
> lập thì việc gộp sẽ không thành công."*

---

## 10. Bốn chỗ video nói sai

### 10.1 Trái phiếu thảm hoạ Mexico là 160 **triệu**, không phải 160 **tỷ**

Shiller (`05 69:07`): *"Chính phủ Mexico, tháng 5/2006, phát hành trái phiếu tổng cộng **160 tỷ đô**."*

**Thật:** **160 triệu đô** — trái phiếu thảm hoạ tham số đầu tiên do một quốc gia phát hành, qua công
ty mục đích đặc biệt **CAT-Mex Ltd.**, cấu trúc bởi Swiss Re và Deutsche Bank, đóng ngày 11/5/2006.
S&P xếp hạng **BB+**.

Sai **1.000 lần**. Và nó làm hỏng chính luận điểm: 160 tỷ sẽ lớn hơn toàn bộ thị trường trái phiếu
thảm hoạ thời đó nhiều lần, khiến câu chuyện thành "đây là công cụ khổng lồ" thay vì luận điểm thật
của Shiller ở `05 68:48` — rằng đây là *"một định chế giống bảo hiểm đang phát triển **chậm chạp**."*

Con số đúng còn củng cố ý ông: 160 triệu là **nhỏ**, đúng như 8 triệu đô bảo hiểm ở Caribbean lúc
động đất Haiti mà ông nêu ở `05 64:46`.

### 10.2 Greenberg thành CEO năm 1968, không phải 1962

Shiller (`05 21:57`): *"ngay trước khi ông ấy mất, ông ấy bổ nhiệm Hank Greenberg… làm CEO **năm
1962**."*

**Thật:** Greenberg vào C.V. Starr & Co. năm **1960**, được giao American Home năm **1962**, và kế
nhiệm Starr làm CEO năm **1968**.

Chính Shiller **tự bác mình hai câu sau** (`05 22:19`): *"49 năm dưới thời Starr, rồi Greenberg tiếp
quản và điều hành tới 2005. Vậy là 37 năm dưới thời Greenberg."* 1919 + 49 = **1968**;
2005 − 37 = **1968**. Số học của ông đòi mốc 1968, chỉ có câu nói là 1962.

Greenberg ngồi trong lớp ba tuần sau cũng nói khác (`14 10:38`): *"tới **1967** tôi tạo ra AIG, đặt
một công ty mẹ lên trên ba công ty này… **Starr mất năm 1968**, nhưng ông ấy đã thấy AIG khởi đầu."*

> [!note]
> Chi tiết này quan trọng hơn vẻ ngoài: theo lời Greenberg, **AIG do chính ông tạo ra năm 1967**, chứ
> không phải do Starr sáng lập năm 1919. Cái Starr lập năm 1919 là **American Asiatic Underwriters**.
> Bảng lịch sử ở §6 đã dựng theo mốc đúng.

### 10.3 "Financial Stability Oversight **Commission**" — thật ra là **Council**

Shiller (`05 47:22`): *"một cơ quan khác gọi là **Financial Stability Oversight Commission**, được lập
ra bởi Dodd-Frank — người ta gọi nó là F-SOC."*

**Thật:** **Financial Stability Oversight *Council*** — Hội đồng Giám sát Ổn định Tài chính. Chính chữ
viết tắt **FSOC** mà ông đọc ngay sau đó đã tự sửa ông.

### 10.4 Greenberg gọi nhầm cơ quan ban hành chuẩn kế toán

Greenberg (`14 48:51`): *"**Accounting Principles Board**, đặt ngay tại Connecticut đây, đưa ra kế
toán ghi nhận theo giá thị trường."*

**Thật:** **Accounting Principles Board** tồn tại 1959–1973 và đã giải thể từ lâu. Cơ quan đóng tại
**Norwalk, Connecticut** và ban hành chuẩn giá trị hợp lý là **FASB — Financial Accounting Standards
Board**; chuẩn liên quan là **SFAS 157**, ban hành 2006.

Địa điểm ông nhớ đúng, tên cơ quan thì nhớ nhầm sang tổ chức tiền nhiệm đã chết 38 năm.

---

## 11. Đối chiếu 2026

### 11.1 Shiller nói Greenberg vô tội. Năm 2017 Greenberg thừa nhận

Đây là chỗ đối chiếu quan trọng nhất của cả bài, vì nó bác **cả hai** diễn giả cùng lúc.

Shiller (`05 25:49`): *"Hoá ra là **không điều gì Spitzer nói đứng vững được**, nên có vẻ Greenberg
vô tội trước mọi cáo buộc."*

Greenberg (`14 31:23`): Spitzer *"rút toàn bộ các cáo buộc"* trước Lễ Tạ ơn, và *"ông ta là một kẻ
xấu."*

**Ngày 10/2/2017**, Greenberg và cựu giám đốc tài chính Howard Smith **dàn xếp** với Tổng chưởng lý
New York. Điều khoản:

- Hoàn trả **9,9 triệu đô** tiền thưởng nhận trong giai đoạn **2001–2004** (Greenberg 9 triệu, Smith
  0,9 triệu).
- Greenberg **thừa nhận** rằng **chính ông khởi xướng, tham gia và phê duyệt** hai giao dịch (Gen Re
  và Capco).
- Cả hai **thừa nhận** biết rằng các giao dịch đó nhằm tăng dự phòng tổn thất và chuyển lỗ nghiệp vụ
  thành lỗ đầu tư, và rằng tác dụng của chúng là **mô tả sai kết quả tài chính thật của AIG**.

Tổng chưởng lý Schneiderman: vụ dàn xếp *"giải quyết một sự thật không thể chối cãi mà ông Greenberg
đã phủ nhận suốt mười hai năm."*

📌 Vụ kiện do **chính Spitzer** khởi xướng năm 2005. Nó đi qua **ba đời tổng chưởng lý**, ra toà tháng
9/2016, và kết thúc bằng lời thừa nhận. Đánh giá của Shiller năm 2011 — đưa ra một cách thiện chí, ba
tuần trước khi mời Greenberg tới lớp — **đã sai**.

> [!note]
> Bài học phương pháp, không phải bài học về nhân cách: **"cáo buộc chưa đứng vững" không đồng nghĩa
> với "vô tội"**, nó chỉ có nghĩa là **chưa xong**. Năm 2011 vụ việc còn 6 năm nữa mới kết thúc. Shiller
> đã chuyển một quy trình **đang chạy** thành một kết luận.

### 11.2 Khoản cứu trợ được hoàn trả — và có lãi

Shiller nói cam kết **182 tỷ đô** (`05 27:54`) và gọi đó là *"vụ cứu trợ lớn nhất ở bất cứ đâu, bất cứ
lúc nào."* Con số của ông **đúng**.

Điều ông không thể biết:

|                                        |                                                                     |
| -------------------------------------- | ------------------------------------------------------------------: |
| Tổng cam kết                           | **182 tỷ đô** (Bộ Tài chính ~70 tỷ qua TARP + Fed New York ~112 tỷ) |
| Bộ Tài chính bán hết cổ phiếu          |                   **11/12/2012**, giá 32,50 đô/cổ phiếu, thu 7,6 tỷ |
| **Lợi nhuận ròng cho người đóng thuế** |                       **+22,7 tỷ đô** (Bộ Tài chính 5,0 + Fed 17,7) |

Trong 19 tháng, Bộ Tài chính bán 1.655.037.962 cổ phiếu — ban đầu là **92% của AIG**, đúng con số
Greenberg đọc ở `14 43:03` — với giá trung bình 31,18 đô.

> [!warning]
> Hai lưu ý làm con số này bớt đẹp:

1. **22,7 tỷ là con số danh nghĩa**, không chiết khấu cho bốn năm nắm giữ hay chi phí cơ hội của vốn.
2. AIG đã chuyển **hơn 90 tỷ đô** tiền cứu trợ — quá nửa — cho các ngân hàng châu Âu và Phố Wall, gồm
   Goldman Sachs, Deutsche Bank và Barclays.

📌 Khoản 2 xác nhận điều **cả Shiller lẫn Greenberg** đã nói. Shiller ở `05 34:33`: Goldman *"không
mất một xu"*. Greenberg ở `14 50:52`: *"AIG đã bị dùng để cứu nhiều bên, bao gồm Goldman Sachs."* Cả
hai đúng.

### 11.3 Greenberg tròn 100 tuổi, và đã xây lại

Trước lớp năm 2011, Greenberg mô tả điều ông đang làm (`14 43:36`): *"Tôi đang điều hành C.V. Starr &
Co. và Starr International. Chúng tôi đang xây dựng nó trở lại thành một tổ chức lớn. Khi tôi rời AIG,
C.V. Starr có **300 người**. Bây giờ khoảng **1.000 người**."*

Ông 85 tuổi khi nói câu đó.

- Ngày **4/5/2025**, Greenberg tròn **100 tuổi**.
- Starr ngày nay là một doanh nghiệp bảo hiểm với **11,9 tỷ đô phí gốc**, xếp hạng **A** của AM Best.
- Đầu 2025 ông chuyển sang vai trò **chủ tịch danh dự**; con trai Jeff kế nhiệm làm chủ tịch kiêm
  đồng CEO C.V. Starr.
- Ông làm chủ tịch Quỹ Starr từ **1968 tới 2024**; quỹ đã tài trợ **hơn 3,8 tỷ đô**.

> [!note]
> Từ 300 người lên 11,9 tỷ đô phí — làm trong độ tuổi từ 80 tới 99. Bất kể đánh giá thế nào về Gen Re
> và Capco, việc ông nói *"chúng tôi đang xây dựng nó trở lại"* ở tuổi 85 và **làm được** là dữ kiện
> đáng ghi.

### 11.4 Bảo hiểm y tế: điều Shiller dự đoán và điều đã xảy ra

Shiller mô tả luật 2010 với giọng dè dặt (`05 61:08`): *"Nó **chưa xảy ra**, nhưng các thủ tục đã có
để dựng nó lên."*

Ông nêu ba cơ chế: sàn giao dịch bảo hiểm, phạt thuế nếu không mua (~700 đô/năm), và **cấm từ chối vì
bệnh có sẵn**.

Đến 2026, cơ chế thứ hai — mức phạt — **đã bị đưa về 0** ở cấp liên bang từ năm 2019, trong khi hai cơ
chế còn lại vẫn tồn tại. Theo mô hình vòng xoáy ở §4, bỏ ràng buộc mua mà giữ lệnh cấm từ chối bệnh có
sẵn là **giữ nguyên chỗ gãy và bỏ đi cái nạng**.

> [!warning]
> Đây là suy luận từ mô hình, không phải dữ kiện thực nghiệm. Việc thị trường không sụp như mô hình
> dự đoán là một câu hỏi mở đáng theo — và là một bài tập tốt cho mục Tự thử.

---

## 12. Góc Việt Nam — quỹ đã có, rồi bị bãi bỏ

Việt Nam từng có **đúng** cái Shiller mô tả ở §9: một quỹ bảo lãnh cho người mua bảo hiểm. Rồi bãi bỏ
nó. Câu chuyện này soi thẳng vào lập luận của Shiller từ cả hai phía.

### Quỹ bảo vệ người được bảo hiểm

**Nghị định 73/2016/NĐ-CP, Điều 107**, với hợp đồng bảo hiểm nhân thọ:

> [!note]
> trả tối đa **90% mức trách nhiệm** của doanh nghiệp bảo hiểm nhân thọ, nhưng **không quá 200 triệu
> đồng** / người được bảo hiểm / hợp đồng.

📌 **Đọc kỹ chữ "90%".** Đây là **đồng bảo hiểm** — đúng cấu trúc đã làm Northern Rock sụp năm 2007,
xem [bài 3 §5](bai_03_ngan_hang.md#5-bảo-hiểm-tiền-gửi-và-bốn-lần-thử).

[Mục 7 của chương trình](#13-chương-trình) tính:

| Trách nhiệm hợp đồng | Quỹ trả | Mất trắng |    % mất |
| -------------------: | ------: | --------: | -------: |
|            100 triệu |   90 tr |     10 tr | **10 %** |
|            200 triệu |  180 tr |     20 tr | **10 %** |
|            500 triệu |  200 tr |    300 tr |     60 % |
|          2.000 triệu |  200 tr |  1.800 tr |     90 % |

Cột "% mất" **không bao giờ bằng 0**. Kể cả hợp đồng nhỏ nhất cũng mất 10%.

> [!warning]
> Nhưng ở đây có một khác biệt so với bài 3 mà không được lẫn: **đồng bảo hiểm trong bảo hiểm tiền
> gửi là lỗi thiết kế** (nó cho người gửi lý do xếp hàng), còn **trong bảo hiểm nói chung nó là tính
> năng** (nó chặn rủi ro đạo đức — §4). Câu hỏi đúng phải là: quỹ bảo vệ người được bảo hiểm giống loại
> nào?

Nó giống loại **thứ nhất**. Người mua bảo hiểm nhân thọ không thể gây ra việc doanh nghiệp bảo hiểm
phá sản, nên không có rủi ro đạo đức nào để chặn. Cắt 10% chỉ có tác dụng **chuyển tổn thất sang người
mua** — đúng nhóm không kiểm soát được gì.

### Rồi quỹ bị bãi bỏ

**Luật Kinh doanh bảo hiểm 2022, Điều 157 khoản 4–5:** từ **01/01/2023**, doanh nghiệp bảo hiểm và chi
nhánh doanh nghiệp bảo hiểm phi nhân thọ nước ngoài **dừng trích nộp** Quỹ bảo vệ người được bảo hiểm.

Lý do được nêu khi trình Quốc hội: sau **12 năm**, số dư quỹ khoảng **1.000 tỷ đồng** và **chưa phải
sử dụng lần nào**. Việc duy trì tạo gánh nặng cho cả doanh nghiệp lẫn người mua, vì tiền trích nộp
tính theo tỷ lệ phần trăm phí bảo hiểm mà bên mua đóng.

Số dư không bị giải thể — Bộ Tài chính quản lý để dùng khi doanh nghiệp mất khả năng thanh toán hoặc
phá sản.

### 1.000 tỷ đồng là bao nhiêu?

Ở mức trần 200 triệu đồng/người, quỹ đủ trả cho **5.000 người**.

Năm nghìn người, trong một thị trường có hàng triệu hợp đồng nhân thọ.

📌 Đó **chính xác** là lời phê bình của Shiller ở `05 39:25`, áp cho Việt Nam: *"những quỹ này nhỏ,
chúng không bảo lãnh đủ cho bạn."* Quỹ này không bao giờ đủ để xử lý một doanh nghiệp bảo hiểm sập
thật — nó chỉ đủ cho một sự cố nhỏ.

### Thay bằng gì

**Luật 2022, Điều 97:** doanh nghiệp bảo hiểm phải trích **quỹ dự trữ bắt buộc** — **5% lợi nhuận sau
thuế** hằng năm, để **bổ sung vốn chủ sở hữu** và bảo đảm khả năng thanh toán.

> [!note]
> Đây là một đảo chiều logic đáng phân tích:

|                          | Quỹ bảo lãnh (cũ)                       | Quỹ dự trữ (mới)                      |
| ------------------------ | --------------------------------------- | ------------------------------------- |
| Tiền nằm ở đâu           | quỹ chung ngoài doanh nghiệp            | **trong vốn chủ sở hữu** doanh nghiệp |
| Bảo vệ ai                | **người mua**, sau khi doanh nghiệp sập | **doanh nghiệp**, để nó không sập     |
| Ai trả                   | người mua, qua phí                      | cổ đông, qua lợi nhuận giữ lại        |
| Khi doanh nghiệp vẫn sập | có lớp đệm (nhỏ)                        | **không còn lớp đệm nào**             |

Việt Nam chọn **vế thứ hai** — cùng triết lý với Basel III ở
[bài 3 §6](bai_03_ngan_hang.md#6-basel--tài-sản-có-rủi-ro-và-yêu-cầu-vốn): buộc định chế giữ đủ vốn
để **đừng sập**, thay vì dựng quỹ để dọn dẹp **sau khi** sập.

Lập luận cho lựa chọn đó khá mạnh: một quỹ 1.000 tỷ chỉ đủ cho 5.000 người thì nó không phải lớp bảo
vệ, nó là **ảo giác về lớp bảo vệ** — và theo đúng lập luận rủi ro đạo đức của Shiller ở `05 18:26`,
một lớp bảo vệ mà người mua tin là có nhưng thực ra không có còn **tệ hơn** không có gì, vì nó làm
người ta thôi nhìn kỹ công ty bảo hiểm.

Lập luận ngược lại cũng mạnh: Shiller nói ở `05 18:53` rằng bảo hiểm *"không chạy nếu không có cơ quan
quản lý, vì bạn sẽ không tin công ty bảo hiểm"*. Quỹ dự trữ bảo vệ **bảng cân đối**, không bảo vệ
**người mua**. Nếu một doanh nghiệp vẫn sập — và §5 cho thấy ρ có thể làm bất kỳ ai sập — thì người
mua giờ đứng sau **không** lớp đệm nào ngoài số dư cũ.

### Câu hỏi để mở

**Một quỹ 12 năm không dùng tới là lãng phí, hay là bảo hiểm đã làm đúng việc của nó?**

Cả khoá học này không trả lời được câu đó — vì đó chính là câu hỏi mà ngành bảo hiểm tồn tại để trả
lời. Bạn trả tiền trong nhiều năm và hy vọng **không bao giờ** phải nhận. Shiller nói đúng câu ấy ở
`05 18:26` khi giải thích vì sao bảo hiểm cần cơ quan quản lý.

Áp chính lập luận đó vào quyết định năm 2022: lý do "12 năm chưa dùng lần nào" là một lý lẽ **rất
đáng ngờ** để bãi bỏ một quỹ bảo hiểm — vì "chưa dùng lần nào" là **kết quả mong đợi**, không phải
bằng chứng vô dụng.

Nhưng lý do "1.000 tỷ chỉ đủ cho 5.000 người" thì là một lý lẽ **rất mạnh** — vì nó nói quỹ ấy **quá
nhỏ để có tác dụng khi cần**.

📌 Hai lý do đó dẫn tới hai kết luận khác nhau: lý do thứ nhất nói **bỏ đi**, lý do thứ hai nói **làm
cho nó lớn hơn**. Bản trình Quốc hội nêu lý do thứ nhất.

---

## 13. Chương trình

> [!note]
> ⚙️ **Chạy:** cần **Python 3.10+**. Lưu file rồi gõ `python3 bai-02-bao-hiem.py`. Không cần cài gói,
> không đọc file ngoài, không gọi mạng. Kết quả **tất định**.

Chương trình: [`../thuc_hanh/bai-02-bao-hiem.py`](../thuc_hanh/bai-02-bao-hiem.py) — 7 mục, mọi khoản
tiền là **số nguyên** ở đơn vị nhỏ nhất, mọi con số hai diễn giả đọc trên lớp đều có một `assert`
đứng sau.

Kết quả chạy thật:

```
BAI 2 — BAO HIEM: GOP RUI RO, VA BA CHO NO GAY
Yale ECON 252 (2011) buoi 5 va buoi 14 — Robert J. Shiller, Hank Greenberg

==============================================================================
1. Luat so lon — cong thuc Shiller viet tren bang
==============================================================================
  Xac suat mot ngoi nha chay trong nam: p = 1%
  Cong ty bao hiem ban n hop dong. Ty le nha chay THUC TE lech bao nhieu?

            n     do lech chuan cua ty le    ty le nam trong khoang
  ----------------------------------------------------------------------
            1               9.9499 %       0.000 % - 30.850 %
           10               3.1464 %       0.000 % - 10.439 %
          100               0.9950 %       0.000 % - 3.985 %
        1,000               0.3146 %       0.056 % - 1.944 %
       10,000               0.0995 %       0.702 % - 1.298 %
      100,000               0.0315 %       0.906 % - 1.094 %
    1,000,000               0.0099 %       0.970 % - 1.030 %

  Ban 1 hop dong: ty le ton that la 0 % hoac 100 %. Khong the kinh doanh.
  Ban 1 trieu hop dong: gan nhu chac chan roi vao 0,97 % - 1,03 %.
  Cung mot rui ro. Chi khac so luong.

  Shiller `05 08:38` dan Aristotle trong De Caelo, hai nghin nam truoc:
    'Nem duoc cung mot mat xuc xac 10.000 lan thi bat kha thi,
     con nem trung mot hai lan thi tuong doi de.'
  Aristotle khong co ngon ngu xac suat, nhung ong biet ket qua.

==============================================================================
2. La thu gui Ba tuoc Oldenburg nam 1609 co dung khong
==============================================================================
  De nghi: nop 1 % gia tri nha moi nam vao mot quy chung.
  Kiem chung theo dung cach nguoi viet de xuat: cong don qua 30 nam.

  Ty le nha chay/nam    Thu duoc      Phai chi ra    Quy con lai   Ket luan
  --------------------------------------------------------------------------
         0.20 %        60,000 tr       12,000 tr       48,000 tr   quy song
         0.50 %        60,000 tr       30,000 tr       30,000 tr   quy song
         0.80 %        60,000 tr       48,000 tr       12,000 tr   quy song
         1.00 %        60,000 tr       60,000 tr            0 tr   hoa von
         1.20 %        60,000 tr       72,000 tr      -12,000 tr   quy vo
         2.00 %        60,000 tr      120,000 tr      -60,000 tr   quy vo

  Diem hoa von nam dung o ty le chay = muc phi = 1 %/nam.
  Nguoi viet nam 1609 dat cuoc rang nha khong chay toi 1 %/nam.
  Ong ta dung — nhung ong ta khong biet vi sao minh dung.

  Cho ong ta THIEU la muc 1: khong phai chi can ty le trung binh du thap,
  ma con can DU NHIEU NHA de ty le thuc te khong lech xa trung binh.

  Do bang VON: mot nam xau (trung binh + 3 do lech chuan) doi bao nhieu von
  du tru tren MOI hop dong, ngoai so phi da thu?

     Phi thu duoc moi hop dong moi nam: 2 trieu

            n     von du tru / hop dong    tinh ra la bao nhieu nam phi
  ----------------------------------------------------------------------
           10                 18.88 tr                       9.44 nam
        1,000                  1.89 tr                       0.94 nam
      100,000                  0.19 tr                       0.09 nam
    1,000,000                  0.06 tr                       0.03 nam

  Voi 10 ngoi nha, phai giu von bang gan 10 NAM tien phi — khong ai lam noi.
  Voi mot trieu ngoi nha, giu von bang 3 % mot nam phi la du.
  Quy mo khong lam rui ro bien mat; no lam VON CAN THIET bien mat.

  Do la ly do bao hiem chi thanh nganh sau nam 1600, dung luc khai niem
  XAC SUAT duoc dua ra (`05 06:39`). Truc giac co truoc, dinh ly co sau.

==============================================================================
3. Khi doc lap gay — chan duoi ma gop rui ro khong vuot qua
==============================================================================
  Cung p = 1%, cung n. Chi them mot thu: cac ton that tuong quan voi nhau.

      rho          n=100        n=10.000     n=1.000.000    chan duoi
  --------------------------------------------------------------------------
    0.00        0.9950 %        0.0995 %        0.0099 %      0.0000 %  <- doc lap
    0.01        1.4036 %        0.9999 %        0.9950 %      0.9950 %
    0.05        2.4270 %        2.2270 %        2.2249 %      2.2249 %
    0.25        5.0490 %        4.9757 %        4.9749 %      4.9749 %
    1.00        9.9499 %        9.9499 %        9.9499 %      9.9499 %  <- moi nha cung so phan

  Voi rho = 0,25, ban mot TRIEU hop dong van chiu do lech chuan 4.97 %,
  tuc gap 500 lan truong hop doc lap. Quy mo khong cuu duoc gi.

  Day la dieu Shiller muon noi. Khong phai AIG danh gia sai xac suat gia
  nha giam — ho danh gia sai VIEC CAC XAC SUAT DO CO LIEN QUAN VOI NHAU.
  Mot sai lam ve rho, khong phai ve p.

  Va no giai thich luon vi sao hop dong bao hiem loai tru CHIEN TRANH va
  KHUNG BO (`05 67:02`): do khong phai rui ro lon, do la rui ro rho ~ 1.

==============================================================================
4. Vong xoay tu than cua lua chon nguoc
==============================================================================
  100 nguoi, chi phi y te ky vong tu 10 den 1000.
  Trung binh toan dan: 505.
  Moi nguoi mua neu phi <= 1.2 x chi phi ky vong cua chinh minh.

   Vong    Phi     Nguoi mua   Nguoi khoe nhat con lai   Ai vua roi bo
  --------------------------------------------------------------------------
      1     505         100                        10       42 nguoi
      2     715          58                       430       17 nguoi
      3     800          41                       600        7 nguoi
      4     835          34                       670        3 nguoi
      5     850          31                       700        1 nguoi
      6     855          30                       710        1 nguoi
      7     860          29                       720        0 nguoi

  Can bang: chi 29 tren 100 nguoi con bao hiem. 71 nguoi KHONG co gi.
  Phi tang tu 505 len 860 (+70 %).

  Khong ai lua doi ai. Khong ai hanh xu phi ly. Nguoi khoe roi bo vi phi
  cao hon gia tri ho nhan duoc — dung nhu the. Va moi lan ho roi bo, phi
  lai tang, day tiep nhom khoe ke sau ra.

  BUOC MOI NGUOI MUA thi vong xoay bien mat:
    phi = 505 cho ca 100 nguoi
    so voi 860 o can bang tren: RE HON 41 %, va phu 100 % dan so.

  Do dung la co che Shiller mo ta o `05 62:04`: 'bang cach buoc moi nguoi
  dang ky, cong ty bao hiem khong con van de chi nguoi om moi dang ky.'
  Luat 2010 khong bat buoc mua — no danh thue neu khong mua (`05 61:39`).

==============================================================================
5. AIG: hai chan doan khac nhau tu hai nguoi trong cung mot khoa hoc
==============================================================================
  Mo hinh: mot so CDS danh nghia 80 ty do.
  Thi truong dinh gia tai san co so mat 30 %.
  Nhung rot cuoc chi 5 % thuc su VO NO.

   Thiet ke hop dong                        Tien phai chi ra ngay
  --------------------------------------------------------------------------
   A. Kich hoat khi VO NO (thiet ke goc)         4 ty do   tra dan theo nhieu nam
   B. Kich hoat khi MAT GIA (sau khi doi)       24 ty do   NGAY LAP TUC, bang tien mat
  --------------------------------------------------------------------------
   Chenh lech                                   20 ty do

  Cung mot so sach. Cung mot the gioi thuc. Khac nhau MOT DIEU KHOAN.
  Thiet ke B doi tien mat gap 6 lan thiet ke A, va doi NGAY.

  Greenberg `14 36:23`: 'Toi khong quan tam ban to den dau, ban het tien mat
  — va ho het that.'

  Va ong noi them mot dieu kiem chung duoc (`14 62:06`): 'neu ban nhin lai
  tat ca nhung CDO ma cac CDS do bao hiem, phan lon da HOI PHUC gia tri.'
  Tuc la trong mo hinh nay, cot A moi la ton that that; cot B la thanh khoan.

  Con Fed thi bat tra 100 xu tren dong, trong khi Greenberg noi le ra
  thuong luong duoc 40-60 xu (`14 41:53`). Chenh lech do bang:
    thuong luong o 40 xu:  tra   9.6 ty thay vi 24.0 ty  -> tiet kiem 14.4 ty
    thuong luong o 50 xu:  tra  12.0 ty thay vi 24.0 ty  -> tiet kiem 12.0 ty
    thuong luong o 60 xu:  tra  14.4 ty thay vi 24.0 ty  -> tiet kiem  9.6 ty

  HAI CHAN DOAN, VA CHUNG KHONG LOAI TRU NHAU:
    Shiller (muc 3):    rho bi danh gia sai  -> khoan lo la THAT
    Greenberg (muc nay): dieu khoan bi doi   -> khoan lo bi PHONG DAI
  Ca hai deu can thiet. Neu rho dung nhu mo hinh AIG gia dinh thi dieu khoan
  the chap chang bao gio bi kich hoat. Neu dieu khoan van la 'chi khi vo no'
  thi rho sai van khong lam ho het tien mat trong vai tuan.
  Rui ro thong ke va rui ro hop dong nhan nhau, khong cong lai.

==============================================================================
6. Quy bao lanh: vi sao meo chia nho khong dung duoc cho bao hiem
==============================================================================
  MEO CHIA NHO voi tien gui ngan hang (`05 39:40`):
    co 2,500,000 do, chia vao 10 ngan hang, moi noi 250,000 do
    -> duoc bao hiem TOAN BO 2,500,000 do

  CUNG MEO DO voi bao hiem: khong dung duoc.
    quy bao lanh Connecticut gioi han 500,000 do, du ban mua bao nhieu hop dong

  Shiller lay vi du cu the (`05 39:04`): mua bao hiem nhan tho cho gia dinh,
  hai dua con hoc dai hoc thi rieng tien hoc da khoang 500.000 do.

     Menh gia hop dong    Connecticut/NY      Bang dien hinh My     % duoc phu
  --------------------------------------------------------------------------
            100,000 do        100,000 do            100,000 do         100 %
            300,000 do        300,000 do            300,000 do         100 %
            500,000 do        500,000 do            300,000 do         100 %
          1,000,000 do        500,000 do            300,000 do          50 %
          2,000,000 do        500,000 do            300,000 do          25 %

  Shiller ket (`05 39:25`): 'nhung quy nay nho, chung khong bao lanh du cho ban.'

  Va con mot khac biet nua ma ong nhan manh (`05 40:22`): Connecticut KHONG
  CHO cong ty bao hiem quang cao rang minh duoc bao lanh — nguoc han voi FDIC,
  von BAT BUOC ngan hang phai treo bien. 'Do la ly do ban khong nghe noi ve no.'

  Khac biet do khong vo tinh. Bao hiem tien gui phai duoc BIET moi chan duoc
  bank run (xem bai 3). Quy bao lanh bao hiem thi khong co bank run de chan —
  nguoi ta khong xep hang doi rut hop dong nhan tho. Nen no im lang duoc.

==============================================================================
7. GOC VIET NAM — Quy bao ve nguoi duoc bao hiem, va viec bai bo no
==============================================================================
  Viet Nam tung co dung cai Shiller mo ta o muc 6: mot quy bao lanh.
  Nghi dinh 73/2016/ND-CP Dieu 107, voi hop dong bao hiem nhan tho:
    tra toi da 90 % trach nhiem cua doanh nghiep,
    nhung khong qua 200 trieu dong / nguoi / hop dong.

     Trach nhiem HD    Quy tra    Mat trang   % mat   Co ly do lo lang?
  --------------------------------------------------------------------------
            100 trieu       90 tr         10 tr     10 %   CO
            200 trieu      180 tr         20 tr     10 %   CO
            222 trieu      199 tr         22 tr     10 %   CO
            500 trieu      200 tr        300 tr     60 %   CO
          1,000 trieu      200 tr        800 tr     80 %   CO
          2,000 trieu      200 tr      1,800 tr     90 %   CO

  Chu y cot '% mat' KHONG BAO GIO bang 0. Cau truc 90 % nghia la nguoi gui
  1 dong cung mat 0,1 dong. Do dung la cau truc DONG BAO HIEM da lam sup
  Northern Rock nam 2007 — xem bai 3 muc 5.

  Tran 200 trieu cham o trach nhiem 222 trieu dong.
  Tren muc do, ty le phu chi giam dan.

  QUY NAY DA BI BAI BO. Luat Kinh doanh bao hiem 2022, Dieu 157 khoan 4-5:
  tu 01/01/2023 doanh nghiep bao hiem DUNG TRICH NOP.

  Ly do: sau 12 nam, so du khoang 1.000 ty dong va CHUA DUNG LAN NAO.

  Nhung 1.000 ty dong la bao nhieu? O muc tran 200 trieu/nguoi,
  quy du tra cho 5,000 nguoi.

  Nam nghin nguoi, trong mot thi truong co hang trieu hop dong nhan tho.
  Do chinh xac la loi phe binh cua Shiller o `05 39:25`, ap cho Viet Nam:
  quy nay khong bao gio du de xu ly mot doanh nghiep bao hiem sup that.

  THAY VAO DO, Luat 2022 chuyen sang QUY DU TRU BAT BUOC (Dieu 97):
    trich 5 % loi nhuan sau thue hang nam, de bo sung von chu so huu.

  Day la mot lua chon thiet ke thu vi, va no dao nguoc logic cua Shiller:
    quy bao lanh  = tra cho nguoi mua SAU KHI doanh nghiep sup
    quy du tru    = giu cho doanh nghiep KHONG SUP ngay tu dau

  Viet Nam chon ve thu hai. Doi lai, neu mot doanh nghiep van sup, gio
  KHONG con lop dem nao cho nguoi mua — chi con so du cu do Bo Tai chinh giu.

  Cau hoi de mo: mot quy 12 nam khong dung toi la LANG PHI, hay la BAO HIEM
  DA LAM DUNG VIEC CUA NO? Ca khoa hoc nay khong tra loi duoc cau do —
  vi do dung la cau hoi ma chinh nganh bao hiem ton tai de tra loi.

==============================================================================
Het. Moi assert da qua.
```

> [!example] Tự thử
>
> 1. **Ở mục 3, tìm mức ρ nhỏ nhất khiến một triệu hợp đồng chỉ tốt ngang một nghìn hợp đồng độc lập.**
>    Con số đó nhỏ đến mức nào? Nó nói gì về việc kiểm định giả định độc lập trong thực tế?
> 2. **Ở mục 4, đổi `NGAI_RUI_RO_BP` từ 12.000 xuống 10.500** (người ta chỉ chịu trả 1,05 lần chi phí kỳ
>    vọng). Bao nhiêu người còn bảo hiểm? Rồi thử 15.000. Mức ngại rủi ro ảnh hưởng tới quy mô thị trường
>    thế nào?
> 3. **Mô hình mức phạt.** Thêm vào mục 4 một khoản phạt `F` nếu không mua: người ta mua nếu
>    `phí − F ≤ 1,2 × chi phí kỳ vọng`. Tìm mức `F` nhỏ nhất để giữ được 100% dân số. So với mức 700 đô
>    Shiller nêu ở `05 61:39` — và với mức 0 đô hiện hành (§11.4).
> 4. **Ở mục 5, tìm tỷ lệ vỡ nợ thực tế khiến hai thiết kế hợp đồng tốn ngang nhau.** Trên mức đó, thiết
>    kế nào đắt hơn? Kết quả có ủng hộ lập luận của Greenberg không?
> 5. **Ở mục 7, tính lại nếu quỹ Việt Nam trả 100% thay vì 90%.** Mức trần 200 triệu chạm ở đâu? Và với
>    1.000 tỷ đồng, quỹ đủ cho bao nhiêu người?

---

## 14. Từ điển thuật ngữ

| Tiếng Việt               | Tiếng Anh                              | Nghĩa trong bài                                                         |
| ------------------------ | -------------------------------------- | ----------------------------------------------------------------------- |
| Gộp rủi ro               | *risk pooling*                         | gom nhiều rủi ro độc lập để tỷ lệ tổn thất thực tế bám sát trung bình   |
| Luật số lớn              | *law of large numbers*                 | độ lệch chuẩn của tỷ lệ giảm theo căn bậc hai của n                     |
| Rủi ro đạo đức           | *moral hazard*                         | được che rủi ro nên hành xử liều hơn — đốt nhà, chỉ định thừa thủ thuật |
| Lựa chọn ngược           | *adverse selection*                    | người biết mình rủi ro cao đổ xô mua, đẩy người khoẻ ra                 |
| Vòng xoáy tử thần        | *death spiral*                         | lựa chọn ngược lặp lại: phí tăng đẩy người khoẻ đi, lại đẩy phí tăng    |
| Tương quan               | *correlation (ρ)*                      | mức các tổn thất cùng xảy ra — chỗ gãy chết người của gộp rủi ro        |
| Hoán đổi rủi ro tín dụng | *credit default swap (CDS)*            | hợp đồng trả tiền khi một khoản nợ hỏng                                 |
| Kích hoạt khi vỡ nợ      | *default trigger*                      | CDS chỉ trả khi tài sản cơ sở thực sự vỡ nợ — thiết kế gốc              |
| Kích hoạt khi mất giá    | *mark-to-market trigger*               | phải đặt thế chấp khi tài sản chỉ **mất giá** — thiết kế đã giết AIG    |
| Nghĩa vụ nợ có thế chấp  | *collateralized debt obligation (CDO)* | gói khoản vay đóng thành chứng khoán                                    |
| Phát hiện giá            | *price discovery*                      | có sàn giao dịch nên biết giá thật; CDO không có                        |
| Công ty tương hỗ         | *mutual company*                       | do người mua bảo hiểm sở hữu, không có cổ đông ngoài                    |
| Quỹ bảo lãnh bảo hiểm    | *insurance guaranty fund*              | quỹ cấp bang trả cho người mua khi công ty bảo hiểm sập                 |
| Đồng bảo hiểm            | *co-insurance*                         | chỉ trả một phần trăm nhất định — tính năng ở §4, lỗi ở §12             |
| Trái phiếu thảm hoạ      | *catastrophe bond*                     | trái phiếu chỉ hoàn trả nếu thảm hoạ **không** xảy ra                   |
| Rủi ro hệ thống          | *systemic risk*                        | rủi ro một tổ chức sập kéo cả hệ thống theo                             |

---

## 15. Câu hỏi tự kiểm tra

1. Vì sao bán một triệu hợp đồng an toàn hơn bán mười hợp đồng, khi tổng rủi ro trong xã hội **không
   hề đổi**? Trả lời bằng khái niệm **vốn**, không dùng chữ "phân tán".
2. Người viết thư năm 1609 đúng ở điều gì và thiếu điều gì? Nếu ông ta lập quỹ với **10 ngôi nhà**,
   chuyện gì có khả năng xảy ra?
3. Ở §5, vì sao ρ = 0,01 — chỉ **một phần trăm** tương quan — đã đủ khiến một triệu hợp đồng chỉ tốt
   ngang một trăm hợp đồng độc lập? Điều này nói gì về việc kiểm định độc lập bằng dữ liệu quá khứ?
4. Hợp đồng bảo hiểm loại trừ chiến tranh và khủng bố. Giải thích lý do **bằng ρ**, không bằng "vì
   thiệt hại quá lớn".
5. Đồng bảo hiểm là **tính năng** ở §4 và **lỗi** ở §12. Điều gì quyết định nó là cái nào?
6. Shiller nói AIG sập vì giả định độc lập gãy. Greenberg nói vì điều khoản thế chấp bị đổi. Dựng một
   kịch bản trong đó **chỉ một** trong hai xảy ra — AIG có sập không, và nhanh thế nào?
7. Vì sao FDIC **bắt buộc** ngân hàng treo biển được bảo hiểm, còn Connecticut **cấm** công ty bảo
   hiểm quảng cáo điều tương tự? Cả hai đều hợp lý — giải thích.
8. Năm 2011 Shiller nói Greenberg vô tội vì các cáo buộc "không đứng vững". Năm 2017 Greenberg thừa
   nhận. Sai lầm suy luận ở đây là gì, và nó khác gì với việc "đoán sai"?
9. Quỹ bảo vệ người được bảo hiểm chạy 12 năm, không dùng lần nào, rồi bị bãi bỏ. Nêu lập luận mạnh
   nhất **ủng hộ** và mạnh nhất **phản đối** quyết định đó.
10. Nếu bạn phải thiết kế lại quỹ ấy cho Việt Nam năm 2026, bạn giữ mức trần 200 triệu hay bỏ tỷ lệ
    90%? Chỉ được chọn **một**. Chọn cái nào và vì sao?

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  BẢO HIỂM — Yale ECON 252 buổi 5 + buổi 14 (Xuân 2011)                       ║
║  Robert Shiller  |  khách mời: Hank Greenberg, cựu CEO AIG                   ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  CẢ NGÀNH ĐỨNG TRÊN MỘT DÒNG CÔNG THỨC  (`05 09:12`)                         ║
║      sd = [ p(1-p) / n ] ^ (1/2)      giảm theo CĂN BẬC HAI của n            ║
║                                                                              ║
║      n = 1          sd = 9,95 %   -> không kinh doanh được                   ║
║      n = 1.000.000  sd = 0,01 %   -> tỷ lệ chắc chắn trong 0,97-1,03 %       ║
║                                                                              ║
║      Gộp rủi ro KHÔNG làm rủi ro biến mất.                                   ║
║      Nó làm VỐN CẦN THIẾT biến mất: 9,44 năm phí -> 0,03 năm phí.            ║
║                                                                              ║
║  BA CHỖ CÔNG THỨC ĐÓ GÃY                                                     ║
║    1. RỦI RO ĐẠO ĐỨC   đốt nhà, bác sĩ chỉ định thừa thủ thuật               ║
║       chặn bằng: loại trừ nguyên nhân + KHÔNG bảo hiểm quá giá trị thật      ║
║    2. LỰA CHỌN NGƯỢC   người ốm đổ xô mua -> phí tăng -> người khoẻ đi       ║
║       mô phỏng: 100 người -> còn 29. 71 NGƯỜI KHÔNG CÓ GÌ.                   ║
║       buộc mọi người mua: phí 505 thay vì 860, phủ 100 % dân số              ║
║    3. ĐỘC LẬP GÃY      <- chỗ chết người nhất, Shiller nói qua nhanh         ║
║       sd = [ p(1-p)(1+(n-1)ρ) / n ] ^ (1/2)                                  ║
║       khi n -> vô cùng, sd KHÔNG về 0, nó dừng ở [ p(1-p)ρ ] ^ (1/2)         ║
║       ρ = 0,25 -> một TRIỆU hợp đồng vẫn chịu sd 4,97 %, gấp 500 LẦN         ║
║       ρ = 0,01 -> một triệu hợp đồng chỉ tốt ngang MỘT TRĂM hợp đồng         ║
║                   độc lập. Chỉ một phần trăm tương quan.                     ║
║       => vì sao hợp đồng loại trừ CHIẾN TRANH và KHỦNG BỐ: ρ ~ 1.            ║
║          Không phải vì thiệt hại LỚN, mà vì chúng KHÔNG ĐỘC LẬP.             ║
║                                                                              ║
║  AIG — HAI CHẨN ĐOÁN TỪ HAI NGƯỜI TRONG CÙNG MỘT KHOÁ HỌC                    ║
║    SHILLER   (`05 26:21`)  giả định độc lập gãy                              ║
║              "giá nhà không bao giờ có thể giảm ở mọi nơi" -> nó giảm        ║
║              => khoản lỗ là THẬT, vấn đề là VỐN                              ║
║    GREENBERG (`14 34:54`)  điều khoản CDS bị đổi: từ VỠ NỢ -> MẤT GIÁ        ║
║              => khoản lỗ bị PHÓNG ĐẠI, vấn đề là TIỀN MẶT                    ║
║       cùng sổ sách: kích hoạt khi vỡ nợ    4 tỷ, trả dần nhiều năm           ║
║                     kích hoạt khi mất giá 24 tỷ, NGAY, bằng tiền mặt         ║
║       HAI CHẨN ĐOÁN NHÂN NHAU, KHÔNG CỘNG LẠI.                               ║
║       Nếu ρ đúng như mô hình AIG giả định thì điều khoản thế chấp            ║
║       chẳng bao giờ bị kích hoạt. Nếu điều khoản vẫn là "chỉ khi vỡ nợ"      ║
║       thì ρ sai vẫn không làm họ hết tiền mặt trong vài tuần.                ║
║                                                                              ║
║    CẢ HAI ĐỒNG Ý MỘT ĐIỀU: Goldman Sachs không mất một xu.                   ║
║       Shiller `05 34:33` | Greenberg `14 50:52`                              ║
║                                                                              ║
║  QUỸ BẢO LÃNH KHÁC FDIC BA CHỖ  (`05 38:41` - `05 40:22`)                    ║
║    trần thấp hơn        300.000 - 500.000 đô, so với 250.000/NGÂN HÀNG       ║
║    không chia nhỏ được  bao nhiêu hợp đồng cũng chỉ 500.000 đô               ║
║    CẤM quảng cáo        ngược hẳn FDIC, vốn BẮT BUỘC treo biển               ║
║      -> vì bảo hiểm tiền gửi phải được BIẾT mới chặn được bank run;          ║
║         quỹ bảo lãnh bảo hiểm không có bank run nào để chặn.                 ║
║                                                                              ║
║  BỐN CHỖ VIDEO NÓI SAI                                                       ║
║    cat bond Mexico 160 TỶ   -> 160 TRIỆU  (sai 1.000 lần)                    ║
║    Greenberg CEO từ 1962    -> 1968 (số học của chính Shiller đòi 1968)      ║
║    "FSOC Commission"        -> Council                                       ║
║    "Accounting Principles Board" -> FASB (APB đã giải thể từ 1973)           ║
║                                                                              ║
║  ĐỐI CHIẾU 2026                                                              ║
║    2017  Greenberg THỪA NHẬN khởi xướng hai giao dịch giả, trả 9,9 tr đô     ║
║          => cả Shiller (`05 25:49`) lẫn Greenberg (`14 31:23`) đều sai       ║
║          "cáo buộc chưa đứng vững" KHÔNG đồng nghĩa "vô tội" — chỉ là        ║
║          CHƯA XONG. Vụ kiện còn chạy thêm 6 năm sau buổi giảng.              ║
║    2012  Bộ Tài chính bán hết cổ phiếu AIG. Lãi ròng +22,7 tỷ đô.            ║
║          Nhưng hơn 90 tỷ đã chảy sang Goldman, Deutsche, Barclays.           ║
║    2025  Greenberg tròn 100 tuổi. Starr: 300 người (2011) -> 11,9 tỷ đô      ║
║                                                                              ║
║  🇻🇳 GÓC VIỆT NAM — QUỸ ĐÃ CÓ, RỒI BỊ BÃI BỎ                                  ║
║    NĐ 73/2016 Đ.107: trả 90 % trách nhiệm, tối đa 200 triệu/người/HĐ         ║
║      => "90 %" là ĐỒNG BẢO HIỂM: không ai được phủ 100 %, kể cả HĐ nhỏ       ║
║         — đúng cấu trúc đã làm sụp Northern Rock năm 2007                    ║
║    Luật KDBH 2022 Đ.157: từ 01/01/2023 DỪNG TRÍCH NỘP                        ║
║      lý do nêu ra: 12 năm, số dư ~1.000 tỷ, CHƯA DÙNG LẦN NÀO                ║
║      nhưng 1.000 tỷ / 200 triệu = chỉ đủ cho 5.000 NGƯỜI                     ║
║      -> đúng lời phê bình của Shiller `05 39:25`: quỹ này QUÁ NHỎ            ║
║    Thay bằng QUỸ DỰ TRỮ BẮT BUỘC (Đ.97): 5 % lợi nhuận sau thuế              ║
║      quỹ bảo lãnh = trả người mua SAU KHI doanh nghiệp sụp                   ║
║      quỹ dự trữ   = giữ doanh nghiệp KHÔNG SỤP ngay từ đầu                   ║
║      Việt Nam chọn vế hai — cùng triết lý Basel III (bài 3 mục 6)            ║
║                                                                              ║
║    HAI LÝ DO, HAI KẾT LUẬN KHÁC NHAU:                                        ║
║      "12 năm chưa dùng"   -> BỎ ĐI   (nhưng đó là kết quả MONG ĐỢI!)         ║
║      "chỉ đủ 5.000 người" -> LÀM CHO NÓ LỚN HƠN                              ║
║      Bản trình Quốc hội nêu lý do THỨ NHẤT.                                  ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

**Video gốc**

- Yale ECON 252 *Financial Markets* (2011), buổi 5 "Insurance, the Archetypal Risk Management
  Institution: Its Opportunities and Vulnerabilities" — YouTube `qfK9rCDCicE`, 73:13.
  [Transcript đầy đủ trên Open Yale Courses](https://oyc.yale.edu/economics/econ-252-11/lecture-5)
- Buổi 14, khách mời Maurice "Hank" Greenberg — YouTube `72qUcUAtRZc`, 70:48.
  [Transcript đầy đủ trên Open Yale Courses](https://oyc.yale.edu/economics/econ-252-11/lecture-14)
- Giáo trình Shiller giao: Fabozzi, Modigliani & Jones, *Foundations of Financial Markets and
  Institutions*.

**Nguồn cho các đính chính ở §10**

- CAT-Mex Ltd. (2006), quy mô 160 triệu đô — S&P xếp hạng BB+, đóng ngày 11/5/2006:
  [Insurance Journal](https://www.insurancejournal.com/news/international/2006/05/22/68654.htm) ·
  [Institutional Investor](https://www.institutionalinvestor.com/article/2btfs9c4abi7jaeqxbjeo/innovation/mexican-government-issues-cat-bond-to-protect-against-earthquakes)
- Mốc sự nghiệp Greenberg (vào C.V. Starr 1960, American Home 1962, kế nhiệm CEO 1968):
  [CNN Fast Facts](https://www.cnn.com/us/hank-greenberg-fast-facts) ·
  [Cornelius Vander Starr, His Life and Work — Columbia University Libraries](https://exhibitions.library.columbia.edu/exhibits/show/cvstarr/greenberg)

**Nguồn cho §11 — đối chiếu 2026**

- Dàn xếp ngày 10/2/2017, lời thừa nhận của Greenberg và Smith, hoàn trả 9,9 triệu đô —
  [Thông cáo của Tổng chưởng lý New York](https://ag.ny.gov/press-release/2017/ag-schneiderman-announces-settlement-martin-act-case-against-former-aig-ceo) ·
  [CNBC](https://www.cnbc.com/2017/02/10/ex-aig-ceo-hank-greenberg-to-settle-with-ny-ag.html) ·
  [Insurance Journal](https://www.insurancejournal.com/news/national/2017/02/12/441586.htm)
- Bộ Tài chính Mỹ bán hết cổ phiếu AIG tháng 12/2012, lãi ròng 22,7 tỷ đô —
  [Treasury, tình trạng chương trình AIG](https://home.treasury.gov/data/troubled-assets-relief-program/aig/status) ·
  [Insurance Journal](https://www.insurancejournal.com/news/national/2012/12/11/273456.htm)
- Greenberg tròn 100 tuổi (4/5/2025), Starr đạt 11,9 tỷ đô phí gốc —
  [The Insurer](https://www.theinsurer.com/ti/news/insurance-industry-icon-hank-greenberg-turns-100-2025-05-05/) ·
  [The Starr Foundation](https://starrfoundation.org/about-us/maurice-r-greenberg/)

**Nguồn cho §12 — Góc Việt Nam**

- Nghị định 73/2016/NĐ-CP Điều 107 — mức chi trả Quỹ bảo vệ người được bảo hiểm:
  [Thư viện Pháp luật](https://thuvienphapluat.vn/chinh-sach-phap-luat-moi/vn/ho-tro-phap-luat/chinh-sach-moi/41358/bai-bo-quy-bao-ve-nguoi-duoc-bao-hiem-tu-ngay-01-01-2023)
- Luật Kinh doanh bảo hiểm 2022, Điều 157 khoản 4–5 — dừng trích nộp từ 01/01/2023:
  [Tạp chí Tài chính](https://tapchitaichinh.vn/chinh-thuc-dung-trich-nop-quy-bao-ve-nguoi-duoc-bao-hiem-tu-nam-2023.html) ·
  [Luật Việt Nam](https://luatvietnam.vn/bao-hiem/luat-kinh-doanh-bao-hiem-2022-moi-nhat-dang-ap-dung-224108-d1.html)

---

**Bản đồ khoá học**

Yale ECON 252 — *Thị trường Tài chính*, Robert J. Shiller · [chỉ mục môn học](../README.md)

1. [Tài chính là hạ tầng xã hội](bai_01_ha_tang_xa_hoi.md) — phát minh, trách nhiệm hữu hạn, gắn chỉ số lạm phát
2. **Bảo hiểm** — gộp rủi ro, và ba chỗ nó gãy ← *bạn đang ở đây*
3. [Ngân hàng](bai_03_ngan_hang.md) — thanh khoản, lựa chọn ngược, bank run, Basel
4. [Chính sách tiền tệ](bai_04_chinh_sach_tien_te.md) — ngân hàng trung ương, công cụ, giới hạn
5. [Ngân hàng đầu tư](bai_05_ngan_hang_dau_tu.md) — shadow banking, repo, đòn bẩy
6. [Sở giao dịch, môi giới, dealer, HFT](bai_06_so_giao_dich.md) — sổ lệnh, tạo lập, thanh toán bù trừ
7. [Nhà quản lý quỹ và nghĩa vụ tín thác](bai_07_quan_ly_quy.md) — quy tắc người thận trọng, hưu trí, Mô hình Yale
8. [Cổ phiếu nhìn từ góc định chế](bai_08_co_phieu_dinh_che.md) — cổ tức, pha loãng, bảng cân đối, giá trên sổ sách
9. [Bất động sản](bai_09_bat_dong_san.md) — từ quyền tài sản tới MBS
10. [Quy định, tự quản, hành vi sai trái](bai_10_quy_dinh_tu_quan.md) — năm tầng, năm cửa thoát, con lắc của Laura Cha
11. [Tài chính công và phi lợi nhuận](bai_11_tai_chinh_cong.md) — phi lợi nhuận, ngân sách vốn, Bismarck và công nghệ thông tin
12. [Tài chính hành vi](bai_12_tai_chinh_hanh_vi.md) — Shiller phản biện Lo
13. [Mục đích, đạo đức, dân chủ hoá tài chính](bai_13_muc_dich_dao_duc.md) — bài giảng kết — bất bình đẳng là thất bại quản trị rủi ro

📐 Nửa **định giá** nằm ở kho bên cạnh: [MIT 15.401 — Lý thuyết Tài chính I](../../mit-15401-finance/README.md)
🐍 Chương trình Python tính mọi con số: [thuc_hanh/README.md](../thuc_hanh/README.md)
