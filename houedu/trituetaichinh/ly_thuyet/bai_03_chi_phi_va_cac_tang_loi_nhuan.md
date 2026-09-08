# Bài 3 — Chi phí và các tầng lợi nhuận

> Bài học dựng từ **Phần II — Những đặc thù của báo cáo kết quả kinh doanh**: chương 7 *Chi phí và nợ
> phải trả* (PDF tr. 54–65), chương 8 *Có nhiều kiểu lợi nhuận* (PDF tr. 66–73).
> 🎯 **Vòng 1.** Bài 2 đã dựng dòng **doanh thu**. Bài này dựng mọi dòng **bên dưới** nó — và cho thấy
> ranh giới giữa các dòng ấy là thứ **di chuyển được**.
> 💼 **Góc quản trị** — ví dụ thêm cho người đi làm, **không có trong sách**.
> 📚 **Mở rộng** — thứ sách nói lướt hoặc để trong hộp công cụ.
> 🇻🇳 **Đối chiếu Việt Nam** — sách viết theo US GAAP, mục này nối sang thực tế Việt Nam.
> ⚠️ — chỗ dễ hiểu sai, hoặc chỗ sách in sai.
> 📌 **Cần đọc trước:** [Bài 1](bai_01_nghe_thuat_tai_chinh.md) · [Bài 2](bai_02_loi_nhuan_chi_la_du_toan.md)
> — mục 3③ và 3④ của bài 1 đã chạm vào phân loại chi phí và khấu hao; bài này làm kỹ.
> ⚙️ **Code:** [`thuc_hanh/bai-03-chi-phi-va-cac-tang-loi-nhuan.py`](../thuc_hanh/bai-03-chi-phi-va-cac-tang-loi-nhuan.py)

---

## Mục lục

<!-- MUC-LUC -->

- [1. Không có quy tắc bất di bất dịch nào](#1-không-có-quy-tắc-bất-di-bất-dịch-nào)
- [2. Trên vạch, dưới vạch — và cái vạch thì di chuyển được](#2-trên-vạch-dưới-vạch--và-cái-vạch-thì-di-chuyển-được)
- [3. Chi phí hoạt động — cholesterol của doanh nghiệp](#3-chi-phí-hoạt-động--cholesterol-của-doanh-nghiệp)
- [4. ⚠️ COGS không phải là biến phí](#4--cogs-không-phải-là-biến-phí)
- [5. Khấu hao — một giả định, không phải một số đo được](#5-khấu-hao--một-giả-định-không-phải-một-số-đo-được)
- [6. Waste Management — cùng thủ thuật, nhân lên hai vạn lần](#6-waste-management--cùng-thủ-thuật-nhân-lên-hai-vạn-lần)
- [7. Khoản trả một lần — cờ vàng cảnh báo](#7-khoản-trả-một-lần--cờ-vàng-cảnh-báo)
- [8. Ba tầng lợi nhuận](#8-ba-tầng-lợi-nhuận)
- [9. Ba cách chữa lợi nhuận thuần thấp — cái nào rẻ, cái nào nhanh](#9-ba-cách-chữa-lợi-nhuận-thuần-thấp--cái-nào-rẻ-cái-nào-nhanh)
- [10. 📚 Hộp công cụ — chênh lệch tốt hay xấu?](#10--hộp-công-cụ--chênh-lệch-tốt-hay-xấu)
- [11. Adelphia — tạo doanh thu từ không khí](#11-adelphia--tạo-doanh-thu-từ-không-khí)
- [12. 🇻🇳 Đối chiếu Việt Nam](#12--đối-chiếu-việt-nam)
- [13. Tự thử](#13-tự-thử)
- [14. Từ điển thuật ngữ](#14-từ-điển-thuật-ngữ)
- [15. Câu hỏi tự kiểm tra](#15-câu-hỏi-tự-kiểm-tra)
- [Tóm tắt một trang](#tóm-tắt-một-trang)
- [Nguồn](#nguồn)

<!-- /MUC-LUC -->

---

## 1. Không có quy tắc bất di bất dịch nào

Chi phí trên báo cáo kết quả kinh doanh rơi vào **hai nhóm cơ bản**:

> **Giá vốn hàng bán** (*cost of goods sold*, COGS) hay **giá thành dịch vụ** (*cost of service*, COS)
> là *"một hạng mục chi phí, bao gồm tất cả các chi phí liên quan trực tiếp đến quá trình sản xuất
> hoặc thực hiện dịch vụ."* — ch. 7 · PDF tr. 54
>
> **Chi phí hoạt động** là *"nhóm chi phí lớn còn lại. Nhóm này bao gồm những chi phí không liên quan
> trực tiếp đến quá trình làm ra sản phẩm hay thực hiện dịch vụ."* — ch. 7 · PDF tr. 58

Nghe thì gọn. Sách phá ngay:

> *"Nếu bạn ngờ rằng quy tắc này sẽ mở ra cho bạn **hàng tấn các diễn giải**, thì bạn đã hoàn toàn
> đúng. Bộ phận kế toán phải ra quyết định sẽ bao gồm những gì trong COGS và những gì ở các hạng mục
> khác."* — ch. 7 · PDF tr. 54

Một số quyết định dễ. Lương công nhân dây chuyền và nguyên vật liệu **chắc chắn vào** COGS; giấy bút
của phòng kế toán và lương giám đốc nhân sự **chắc chắn ra**. Nhưng rồi:

> *"Tiếp đó sẽ là những khoản nằm ở **vùng xám** − những khoản này thì **nhiều vô kể**. Ví dụ: Thế
> còn lương của giám đốc nhà máy sản xuất ra sản phẩm? Lương của quản đốc nhà máy thì sao? Hoa hồng
> bán hàng thì thế nào?"* — ch. 7 · PDF tr. 55

Ai cũng tưởng đây là chỗ GAAP sẽ ra tay. Sách dập tắt hy vọng ấy bằng con số:

> *"Bộ tiêu chuẩn GAAP… **dày đến 4.000 trang** và có rất nhiều quy tắc chi tiết. Bạn có thể tưởng
> rằng GAAP sẽ quy định: 'giám đốc sản xuất không được tính' hoặc 'quản đốc thì tính'. **Không may
> mắn như vậy**, GAAP chỉ cung cấp cho ta các **định hướng**."* — ch. 7 · PDF tr. 55

Thay cho quy tắc, chỉ có hai bài kiểm tra:

> *"Mấu chốt, như các kế toán viên vẫn thường nói, là **sự hợp lý và nhất quán**. Chừng nào logic của
> doanh nghiệp vẫn còn hợp lý và chừng nào logic đó vẫn còn được áp dụng nhất quán, thì chừng đó
> **doanh nghiệp muốn làm gì cũng được**."* — ch. 7 · PDF tr. 55

Câu cuối là toàn bộ bài học. Bốn nghìn trang quy tắc, và ranh giới quan trọng nhất trên báo cáo kết
quả kinh doanh vẫn là một **phán đoán**.

---

## 2. Trên vạch, dưới vạch — và cái vạch thì di chuyển được

> *"Từ **'vạch'** ở đây thường ám chỉ **lợi nhuận gộp**. Phía trên vạch lợi nhuận gộp của báo cáo kết
> quả kinh doanh thường là doanh thu và giá vốn hàng bán, hoặc giá thành dịch vụ. Phía dưới vạch là
> chi phí hoạt động, lãi vay, và thuế."* — ch. 7 · PDF tr. 57

Vì sao phải phân biệt?

> *"Những khoản mục **trên vạch** (trong ngắn hạn) thường **biến đổi nhiều hơn** những khoản mục dưới
> vạch, và vì vậy thường được **ban quản lý chú ý đến hơn**."* — ch. 7 · PDF tr. 57

Sách kể hai tình huống. Cái thứ nhất là bạn bị đẩy qua vạch — bộ phận phân tích kỹ thuật của một công
ty kiến trúc bị chuyển ra khỏi COS, hoàn toàn hợp lý về mặt kế toán, nhưng:

> *"Bạn và nhân viên của mình sẽ **không còn là một phần của cái gọi là 'trên vạch' nữa**. Nghĩa là
> bạn sẽ xuất hiện một cách khác đi trên màn hình ra-đa của doanh nghiệp… Một khi bạn được định khoản
> bên ngoài COS − 'dưới vạch' − **mức độ chú ý dành cho bạn có thể ít đi đáng kể**."* — ch. 7 · PDF tr. 56

Cái thứ hai là bạn tự đẩy cái vạch. Đây là tình huống có số:

| | đô-la |
| --- | ---: |
| chỉ tiêu lợi nhuận gộp tháng này | 1.000.000 |
| thực tế (kém 20.000) | 980.000 |
| chuyển "quản lý hợp đồng các đơn hàng của nhà máy" ra khỏi COGS | 25.000 |
| **lợi nhuận gộp sau khi chuyển** | **1.005.000** |

> *"Bạn kiến nghị kế toán trưởng chuyển các khoản đó vào chi phí hoạt động. Kế toán trưởng đồng ý;
> thay đổi được tiến hành. **Bạn đạt được chỉ tiêu, và mọi người đều hân hoan.** Ngay cả một người
> ngoài cũng có thể nhìn vào những gì đang diễn ra và **tin rằng lợi nhuận gộp đã cải thiện** − tất
> cả là nhờ thay đổi mà bạn đã thực hiện vì bạn đang cố gắng đạt chỉ tiêu."* — ch. 7 · PDF tr. 56

Không một đồng doanh thu nào thay đổi. Không một đồng chi phí nào biến mất.

**Sách dừng ở đây.** Câu nó không hỏi: *nếu làm vậy trên một doanh nghiệp thật thì đi được bao xa?*
Chuyển X triệu từ COGS sang SG&A của công ty mẫu:

| chuyển | LN gộp | biên gộp | SG&A | EBIT | LN thuần |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 1.933 | 22,2% | 1.061 | **652** | **248** |
| 87 | 2.020 | 23,2% | 1.148 | **652** | **248** |
| 174 | 2.107 | 24,2% | 1.235 | **652** | **248** |
| 435 | 2.368 | 27,3% | 1.496 | **652** | **248** |

⭐ **Hai cột cuối không nhúc một li** — và điều đó được chốt bằng `assert` trong code, không phải bằng
lời hứa. Chuyển chi phí qua vạch **không tạo ra một đồng lời lỗ nào**; nó chỉ đổi chỗ ngồi.

Con số đáng nhớ: muốn biên lợi nhuận gộp tăng **đúng một điểm phần trăm**, phải chuyển **87 triệu**.
Đó là **1,29% của COGS** — nhưng cũng chính là **8,2% của SG&A**.

💼 Vì sao một con số lại nhỏ ở bên này và to ở bên kia: COGS lớn gấp **6,4 lần** SG&A. Nên cùng một
bút toán, người theo dõi biên lợi nhuận gộp báo cáo *"cải thiện một điểm"*, còn người theo dõi chi phí
chung báo cáo *"SG&A phình ra 8%"*. Hai bản tin trái ngược, cả hai đều thật.

⚠️ Sách nói thẳng là **việc này hợp pháp**: *"Một lần nữa, những thay đổi này cũng hợp pháp, miễn là
chúng đáp ứng được bài kiểm tra hợp lý và nhất quán. Thậm chí bạn còn có thể rút một khoản mục chi phí
ra khỏi COGS trong một tháng và kiến nghị tính gộp nó trở lại vào tháng sau."* — ch. 7 · PDF tr. 57.
Ranh giới duy nhất là thói quen: *"việc liên tục thay đổi các quy tắc giữa các kỳ kế toán là một hình
thức không hay."*

📌 **Đây là mẫu hình thứ ba cùng loại trong khoá học.** [Bài 1](bai_01_nghe_thuat_tai_chinh.md) mục 3⑤
đã cho thấy phân bổ lương làm biên gộp chạy 21,1%↔23,4% mà EBIT không đổi;
[bài 2](bai_02_loi_nhuan_chi_la_du_toan.md) mục 8 cho thấy bút toán Tyco +739 vào cả hai vế làm lợi
nhuận gộp tăng đúng bằng 0. Mục này là phiên bản tổng quát của cả hai.

---

## 3. Chi phí hoạt động — cholesterol của doanh nghiệp

Chi phí bị loại khỏi COGS thì đi đâu? Vào **chi phí hoạt động**, còn gọi là **chi phí chung**
(*overhead*), hoặc **SG&A** (*sales, general and administrative*), hoặc chỉ **G&A**.

Sách lưu ý cách doanh nghiệp **tự chọn** mức chi tiết:

> *"Microsoft chọn cách thể hiện chi phí bán hàng và chi phí marketing ở dòng riêng vì hai loại chi
> phí này chiếm một phần đáng kể trong tổng chi phí của tập đoàn. Ngược lại, các công ty công nghệ
> sinh học lại… gộp chung chi phí bán hàng và marketing vào chi phí G&A. Cả hai nhóm đều **tách riêng
> chi phí nghiên cứu và phát triển** vì khoản mục này có tầm quan trọng tương đối cao."*
> — ch. 7 · PDF tr. 57

Nguyên tắc rút ra: **dòng nào được tách riêng cho biết doanh nghiệp coi cái gì là quan trọng.** Bản
thân cách bày báo cáo đã là một thông điệp.

Còn đây là hình ảnh mà sách chọn để nói về chất lượng của nhóm chi phí này:

> *"Bạn có thể coi chi phí hoạt động như **cholesterol** trong doanh nghiệp. Cholesterol tốt sẽ làm
> bạn khỏe mạnh, nhưng cholesterol xấu sẽ làm động mạch của bạn tắc nghẽn. Chi phí hoạt động tốt sẽ
> giúp doanh nghiệp vững mạnh, và chi phí hoạt động xấu sẽ kéo tụt kết quả kinh doanh… (Một cách gọi
> khác cho những chi phí hoạt động xấu là **'thủ tục quan liêu không cần thiết'**. Cũng có thể gọi là
> **'việc đèo bòng'**.)"* — ch. 7 · PDF tr. 58

Điểm đáng giữ: sách **không** nói chi phí hoạt động là xấu. Nó nói có hai loại, và bảng báo cáo
**không phân biệt được chúng** — chỉ có người trong cuộc mới phân biệt được.

---

## 4. ⚠️ COGS không phải là biến phí

Đây là chỗ gần như ai cũng nhầm, và sách chỉ dành cho nó một đoạn văn:

> *"Bạn có thể cho rằng COGS cũng giống như **'chi phí biến đổi'** − những chi phí thay đổi theo khối
> lượng sản xuất − và rằng chi phí hoạt động là **chi phí cố định**… **Nhưng rủi thay, mọi thứ không
> đơn giản như vậy.** Chẳng hạn, nếu tiền lương của các quản đốc được tính vào COGS, thì khi đó khoản
> mục này là **cố định trong ngắn hạn**, bất kể bạn làm ra 100.000 hay 150.000 sản phẩm. Hoặc… nếu bạn
> có một đội ngũ bán hàng ăn hoa hồng, chi phí bán hàng ở một chừng mực nào đó sẽ là **biến phí**, tuy
> vậy chúng lại thường được tính vào chi phí hoạt động."* — ch. 7 · PDF tr. 58

Có **hai cách phân loại chi phí**, và chúng **cắt chéo nhau**:

|  | **biến đổi** theo sản lượng | **cố định** trong ngắn hạn |
| --- | --- | --- |
| **trên vạch** (COGS) | nguyên vật liệu, lương công nhân dây chuyền | lương quản đốc, khấu hao nhà xưởng |
| **dưới vạch** (SG&A) | hoa hồng bán hàng | lương phòng nhân sự, tiền thuê văn phòng |

Cả bốn ô đều có thật. Ai đọc báo cáo mà tưởng cột trái trùng hàng trên là đang dùng một mô hình sai.

**Cái giá của việc tin vào nó.** Một doanh nghiệp: doanh thu 10.000, COGS 6.000 (4.500 biến + 1.500
cố định), SG&A 3.000 (2.400 cố định + 600 biến). Lợi nhuận 1.000, biên gộp 40%.

| sản lượng | **mô hình thô**<br>COGS biến 100% | **mô hình thật**<br>tách biến / cố định |
| --- | ---: | ---: |
| ×1,5 | 3.000 | **3.450** |
| ×1,0 | 1.000 | 1.000 |
| ×0,5 | −1.000 | **−1.450** |
| **biên độ** | ±2.000 | **±2.450** |

⭐ Mô hình thô **sai cả hai chiều, và sai theo cùng một kiểu**: nó dẹp bẹp **đòn bẩy hoạt động**. Lợi
nhuận thật đảo mạnh hơn dự báo **22,5%** — năm tốt thì tốt hơn bạn tưởng, năm xấu thì xấu hơn bạn
tưởng. Biên lợi nhuận gộp cũng không đứng yên: mô hình thô nói mãi là 40%, thực tế chạy từ **25%** (sản
lượng nửa) lên **45%** (sản lượng rưỡi).

💼 Bất kỳ ngân sách nào viết *"doanh thu tăng 15%, giá vốn tăng 15%"* đều đang dùng mô hình thô. Cách
kiểm rẻ nhất: hỏi kế toán xem trong COGS có bao nhiêu là **lương quản đốc, khấu hao nhà xưởng, thuê
đất** — những thứ không nhúc khi sản lượng đổi.

---

## 5. Khấu hao — một giả định, không phải một số đo được

Sách giới thiệu khấu hao bằng một câu cảnh báo hiếm gặp về mức độ nghiêm trọng:

> *"Ở những câu khô khan trên ẩn chứa **một công cụ rất quyền năng mà các nghệ sỹ tài chính có thể ứng
> dụng**. Nó đáng để chúng ta đi sâu vào chi tiết."* — ch. 7 · PDF tr. 59

Ví dụ: công ty chuyển phát, tháng đầu doanh thu 10.000, COGS 5.000, chi phí 3.000. Mua xe tải 36.000
đô-la, khấu hao đường thẳng.

| giả định tuổi đời | khấu hao/tháng | LN thuần | **EBITDA** |
| --- | ---: | ---: | ---: |
| 1 năm | 3.000 | **−1.000** | 2.000 |
| 2 năm | 1.500 | 500 | 2.000 |
| **3 năm** (sách) | **1.000** | **1.000** | 2.000 |
| 6 năm | 500 | **1.500** | 2.000 |
| 10 năm | 300 | 1.700 | 2.000 |

Ba hàng in đậm là ba con số sách nêu, và cả ba đều khớp:

> *"Họ có thể giả định rằng chiếc xe chỉ dùng được một năm… Cách tính này làm kết quả kinh doanh tụt
> giảm 2.000 đô-la, và đẩy công ty từ chỗ **có lãi 1.000 đô-la thành lỗ 1.000 đô-la**. Hoặc họ giả
> định rằng chiếc xe có thể sử dụng được trong sáu năm… lợi nhuận thuần sẽ lên đến 1.500 đô-la… chúng
> ta lại **tăng được lợi nhuận thuần lên 50%** − chỉ bằng việc thay đổi giả định về khấu hao."*
> — ch. 7 · PDF tr. 60

⭐ **Cột EBITDA không đổi — 2.000 ở cả năm dòng.** Đó chính là lý do EBITDA tồn tại. Khấu hao là dòng
duy nhất trong bảng mà **không ai chi tiền ra cả**:

> **Chi phí phi tiền mặt** (*noncash expense*): *"loại chi phí được tính cho một kỳ báo cáo kết quả
> kinh doanh, nhưng **không được chi trả thật sự bằng tiền mặt**. Khấu hao là một ví dụ… doanh nghiệp
> không có nghĩa vụ phải chi số tiền đó, vì thiết bị **đã được mua từ trước**."* — ch. 7 · PDF tr. 62

Bỏ nó đi thì cái đòn bẩy của cả mục này tắt ngúm. Mục 8 sẽ đặt tên cho việc đó.

⚠️ Nhưng **tổng chi phí cả đời xe vẫn là 36.000 đô-la** — không giả định nào đổi được. Giống hệt xe tải
của [bài 2](bai_02_loi_nhuan_chi_la_du_toan.md) mục 2 và dự án 18 tháng của bài 2 mục 7: chỉ **dịch**,
không **tạo ra**. Giả định khấu hao dài chỉ vay lợi nhuận của những năm sau, và món nợ đó không quỵt
được.

### 📚 Khấu hao vô hình, và vì sao nó không phải là mất giá

*Amortization* (tài sản vô hình) và *depreciation* (tài sản hữu hình) là **cùng một ý tưởng**; sách
thẳng thắn về việc tiếng Anh có hai từ: *"Chúng tôi không biết chắc lý do − nhưng dù vì lẽ gì, đó cũng
là nguồn cơn gây khó hiểu."* — ch. 7 · PDF tr. 63.

Chỗ đáng nhớ hơn là phân biệt giữa **kinh tế** và **kế toán**:

> *"Trong kinh tế, khấu hao ngầm chỉ rằng món tài sản **mất dần giá trị** theo thời gian… Nhưng việc
> khấu hao… trong kế toán lại mang ý nghĩa **phân bổ chi phí** nhiều hơn là khấu trừ giá trị. Chẳng
> hạn, một chiếc xe tải có thể sẽ được khấu hao trong ba năm, cho nên giá trị kế toán của chiếc xe tải
> đó ở cuối giai đoạn đó sẽ **bằng 0**. Nhưng nó **vẫn có giá trị nào đó trên thị trường**… Thế nên,
> các tài sản **thường hiếm khi đáng giá như những gì được thể hiện trên sổ sách**."* — ch. 7 · PDF tr. 63

Câu cuối là một trong những câu quan trọng nhất cả cuốn sách, và nó quay lại ở
[bài 4](bai_04_bang_can_doi_ke_toan.md) khi ta đọc
cột tài sản.

---

## 6. Waste Management — cùng thủ thuật, nhân lên hai vạn lần

Sách nói trước rằng đừng coi mục 5 là bài tập sách vở:

> *"WMI là một trong những câu chuyện doanh nghiệp thành công trong thập niên 1970-1980. Chính bởi
> vậy, mọi người đều choáng váng khi năm 1998 công ty này thông báo mình sẽ phải trả một khoản trước
> thuế lên đến **3,54 tỷ đô-la** từ thu nhập."* — ch. 7 · PDF tr. 60

Cơ chế thì đúng bằng ví dụ xe tải, chỉ khác quy mô:

> *"Họ bắt đầu chú ý trước tiên tới **đội xe gồm 20.000 xe rác, mỗi xe có giá trung bình 150.000
> đô-la**. Tính đến thời điểm đó, đoàn xe tải đã được khấu hao từ **8 đến 10 năm**, đây là mức khấu
> hao tiêu chuẩn của ngành. Ban điều hành quyết định, bấy nhiêu thời gian là không đủ… Khi **thêm 4
> năm nữa** vào bảng khấu hao xe tải, người ta có thể tạo nên điều kỳ diệu cho kết quả kinh doanh;
> việc đó giống như ví dụ nho nhỏ chúng tôi đã nêu khi nãy, **nhưng được nhân lên với cấp số hàng
> ngàn**."* — ch. 7 · PDF tr. 61

Sách để nguyên đó và không tính ra. Ta tính. Đội xe: 20.000 × 150.000 = **3,0 tỷ đô-la**.

| tuổi đời giả định | khấu hao/năm (triệu $) | |
| --- | ---: | --- |
| 8 năm | 375,0 | ← chuẩn ngành |
| 10 năm | 300,0 | ← chuẩn ngành |
| 12 năm | 250,0 | ← sau khi kéo dài |
| 14 năm | 214,3 | ← sau khi kéo dài |

| kéo dài thêm 4 năm | tiết kiệm / năm (triệu $) |
| --- | ---: |
| 10 → 14 năm | 85,7 |
| 9 → 13 năm | 102,6 |
| 8 → 12 năm | 125,0 |

Sách cho biết kết quả cuối:

> *"Bằng cách gian lận các số liệu khấu hao xe tải và thùng rác, ban điều hành WMI đã bơm lợi nhuận
> trước thuế của công ty lên con số khổng lồ là **716 triệu đô-la**."* — ch. 7 · PDF tr. 61

⭐ Riêng đội xe cho **85,7–125,0 triệu mỗi năm**, tức là để tích đủ 716 triệu **chỉ bằng xe tải** cần
khoảng **5,7–8,4 năm**. Sách đặt mốc công ty bắt đầu trượt dốc *"khoảng năm 1992"* và khoản xử lý nợ
xấu năm 1998 — **nhiều nhất sáu năm**. Con số của riêng đội xe rơi đúng vào khoảng đó; phần còn lại là
**1,5 triệu thùng rác** (kéo từ 12 lên 15, 18 hoặc 20 năm).

Nghĩa là: con số 716 triệu **không cần một thủ thuật nào kỳ quặc cả** — chỉ cần đổi một cột trong bảng
khấu hao, và kiên nhẫn.

⚠️ *(Cửa sổ "nhiều nhất sáu năm" là **suy ra từ hai mốc của sách**; sách không nói gian lận kéo dài bao
lâu. Con số 716 triệu và mọi đầu vào khác đều là của sách.)*

Đặt cạnh khoản xử lý nợ xấu 3.540 triệu năm 1998, riêng phần khấu hao chiếm **20,2%** — đúng như sách
nói: *"đây mới chỉ là một trong những chiêu trò họ sử dụng."*

---

## 7. Khoản trả một lần — cờ vàng cảnh báo

Ngoài COGS và chi phí hoạt động, mỗi báo cáo còn có một nhóm hổ lốn. Phần lớn không đáng bận tâm, trừ
một dòng:

> *"Nhãn tên phổ biến nhất cho nó là **'khoản trả một lần'**."* — ch. 7 · PDF tr. 63

Tiếng lóng của nghề: **taking the big bath** (gột rửa). Tên chính thức: **khoản đặc biệt**
(*extraordinary item*), **xử lý nợ xấu** (*write-off*), **phí tái cơ cấu** (*restructuring charge*).

Nó thường xuất hiện khi *"một CEO mới lên nắm quyền và muốn tái cơ cấu, tái tổ chức, đóng cửa nhà máy
và có thể cắt giảm biên chế"* (PDF tr. 64). Và vì GAAP buộc kế toán phải ghi nhận chi phí **ngay khi
biết nó phát sinh, kể cả khi phải ước tính**, nên:

> *"Đây thật sự là nơi cần **cắm cờ vàng cảnh báo** − một nơi tuyệt vời cho các định kiến số liệu. Nói
> cho cùng thì bạn thực sự **ước tính** chi phí tái cơ cấu như thế nào?"* — ch. 7 · PDF tr. 64

Ước sai theo cả hai hướng đều bóp méo, và **cả hai lần đều là kỳ SAU chịu**:

| ước tính | chuyện gì xảy ra | ai hưởng, ai chịu |
| --- | --- | --- |
| **quá cao** | một phần khoản phí phải *"đảo ngược lại"* | kỳ sau lãi **tăng chóng mặt so với lợi nhuận thực** |
| **quá thấp** | phải chi thêm một khoản phí nữa sau đó | kỳ sau lãi **thấp hơn so với thực tế** |

> *"Người ta từng kháo nhau rằng **Al Dunlap 'Cưa Xích'**, CEO khét tiếng của Sunbeam, đã coi bộ phận
> kế toán như một **trung tâm lợi nhuận**… (Nếu bạn nghe một nhà điều hành cấp cao nói về bộ phận kế
> toán theo cách ấy, **công ty của bạn ắt có vấn đề**)."* — ch. 7 · PDF tr. 64

Và phép thử đơn giản nhất để phát hiện lạm dụng — đếm:

> *"Trong suốt giai đoạn đầu những năm 1990, **năm nào AT&T cũng thực hiện một khoản tái cơ cấu 'một
> lần'**… Hơn nữa, nếu một công ty liên tục chi các khoản tái cơ cấu một lần đặc biệt suốt nhiều năm,
> thì những khoản chi ấy có thể **đặc biệt** đến thế nào?"* — ch. 7 · PDF tr. 65

📌 Nối với [bài 2](bai_02_loi_nhuan_chi_la_du_toan.md) mục 5: **báo cáo hình thức** là báo cáo loại trừ
đúng những khoản này. Nghĩa là một công ty có thể vừa dồn tin xấu vào một khoản "một lần", vừa công bố
một bản hình thức đã loại nó ra. Hai thủ thuật ăn khớp với nhau.

---

## 8. Ba tầng lợi nhuận

Chương 8 mở bằng việc dọn từ vựng. **Lợi nhuận, thu nhập, thu nhập thuần, biên lợi nhuận thuần** —
sách ghi nhận rằng nhiều doanh nghiệp dùng *"tất cả những thuật ngữ khác nhau này để chỉ lợi nhuận,
đôi khi còn sử dụng tất cả trong cùng một tài liệu"* và cảnh báo: *"có vẻ họ đang nói về những khái
niệm khác nhau. Nhưng **thực sự là không phải vậy**."* — ch. 8 · PDF tr. 66.

> **Lợi nhuận** (*profit*): *"số tiền còn lại sau khi đã trừ tất cả các chi phí khỏi doanh thu. Có
> **ba loại lợi nhuận cơ bản**: lợi nhuận gộp, lợi nhuận hoạt động và lợi nhuận thuần. Mỗi loại được
> xác định bằng cách trừ khỏi doanh thu **những hạng mục chi phí nhất định**."* — ch. 8 · PDF tr. 66

Trên công ty mẫu:

| tầng | triệu đô-la | % doanh thu | đã trừ những gì |
| --- | ---: | ---: | --- |
| Doanh thu | 8.689 | 100,0% | — điểm xuất phát |
| **Lợi nhuận gộp** | 1.933 | 22,2% | COGS |
| **EBIT** | 652 | 7,5% | COGS + SG&A + khấu hao |
| *EBITDA* | *891* | *10,3%* | *COGS + SG&A (khấu hao **cộng lại**)* |
| **Lợi nhuận thuần** | 248 | 2,9% | tất cả, kể cả lãi vay và thuế |

⭐ Đọc cột phải theo chiều dọc: **100 → 22,2 → 7,5 → 2,9**. Từ 100 đô-la doanh thu còn lại chưa đầy
3 đô-la.

### Tầng 1 — lợi nhuận gộp: bao nhiêu thì đủ?

> *"Lợi nhuận gộp phải **đủ để bù chi phí hoạt động, thuế, chi phí tài chính và lợi nhuận thuần**."*
> — ch. 8 · PDF tr. 67

Không có ngưỡng chung. Sách nêu ba cách hiệu chuẩn:

- **So với ngành.** *"Trong ngành kinh doanh tạp hóa, lợi nhuận gộp thường chiếm tỷ lệ phần trăm rất
  nhỏ trong doanh thu. Trong khi đó, ở ngành kinh doanh trang sức, lợi nhuận gộp lại thường chiếm tỷ
  lệ lớn hơn hẳn."*
- **So với quy mô.** *"Một doanh nghiệp có doanh thu lớn hơn có thể toả sáng với tỷ lệ lợi nhuận gộp
  nhỏ hơn… (Đó là một trong những lý do khiến **Wal-Mart** có thể tính giá thấp đến vậy)."*
- **So với chính mình qua từng năm.** *"Nếu nó đang đi xuống, bạn có thể đặt câu hỏi tại sao."*

⚠️ Nhưng trước khi hỏi tại sao, phải kiểm xem con số có thật đổi không. Sách kể một tình huống trực
tiếp nối vào mục 2:

> *"Giả sử bạn là giám đốc nhân sự của một công ty nghiên cứu thị trường, và bạn nhận thấy rằng lợi
> nhuận gộp đang có chiều hướng đi xuống… Thế là bạn và các nhân viên của mình bắt đầu lên kế hoạch
> cắt giảm chi phí dịch vụ, thậm chí có thể sử dụng đến cả biện pháp **cắt giảm biên chế**. Nhưng khi
> nghiên cứu kỹ hơn, bạn phát hiện ra phần tiền lương vốn nằm trong chi phí hoạt động **đã được chuyển
> gộp vào COGS**. Do vậy, **thực tế là chi phí dịch vụ không tăng, và việc cắt giảm biên chế sẽ là sai
> lầm**."* — ch. 8 · PDF tr. 67–68

Đây là mục 2 nhìn từ phía người nhận hậu quả. Cùng một bút toán vô hại; ở đây nó suýt làm mất việc của
người thật.

### Tầng 2 — lợi nhuận hoạt động (EBIT): chìa khoá cho sự vững mạnh

> **Lợi nhuận hoạt động** (*operating profit*, **EBIT** — *earnings before interest and taxes*): lợi
> nhuận gộp trừ chi phí hoạt động, **bao gồm cả khấu hao**. — ch. 8 · PDF tr. 69

Vì sao thuế và lãi vay chưa bị trừ?

> *"Các khoản thuế không thực sự liên quan đến hiệu quả hoạt động… Và chi phí lãi vay thì phụ thuộc
> vào việc doanh nghiệp lấy vốn từ vay nợ, hay từ vốn chủ sở hữu… **Cơ cấu tài chính của doanh nghiệp
> không hề nói lên điều gì về hiệu quả của doanh nghiệp trên phương diện hoạt động.**"*
> — ch. 8 · PDF tr. 68

Đó là lý do EBIT là con số ai cũng nhìn: ngân hàng và nhà đầu tư xem khả năng trả nợ; nhà cung cấp xem
khả năng thanh toán hoá đơn; khách hàng lớn xem độ ổn định; và *"ngay cả những nhân viên khôn ngoan
cũng kiểm tra lợi nhuận hoạt động"* (PDF tr. 69).

### 📚 Vì sao Phố Wall bỏ EBIT sang EBITDA

> *"Từng có thời gian, các nhà phân tích của Phố Wall theo dõi sát sao lợi nhuận hoạt động − hay EBIT.
> Nhưng các doanh nghiệp mà về sau bị lộ tẩy là đã gian lận **hóa ra đều dàn cảnh với các số liệu khấu
> hao** (hãy nhớ lại câu chuyện của WMI), bởi vậy các số liệu EBIT của họ đều đáng ngờ. Chẳng bao lâu
> sau, Phố Wall bắt đầu tập trung vào một thông số khác − **EBITDA**."* — ch. 8 · PDF tr. 69

Đây là chỗ mục 5 và mục 8 khớp lại: cột EBITDA bất động qua **năm giả định khấu hao khác nhau** chính
là lý do một chỉ số ra đời. EBITDA không "tốt hơn" — nó **miễn nhiễm với đúng một thủ thuật cụ thể**,
và đổi lại nó giả vờ rằng tài sản không hao mòn.

⚠️ Với công ty mẫu, khấu hao 239 bằng **36,7% của EBIT**. Đây không phải chi tiết nhỏ: chọn EBIT hay
EBITDA là chênh nhau hơn một phần ba con số.

### Tầng 3 — lợi nhuận thuần: dòng dưới cùng

> **Lợi nhuận thuần** (*net profit*): *"là những gì còn lại sau khi trừ khỏi doanh thu **tất cả** giá
> thành và chi phí. Đó là lợi nhuận hoạt động sau khi trừ đi lãi vay, thuế, các khoản trả một lần và
> bất kỳ chi phí nào còn lại."* — ch. 8 · PDF tr. 71

> *"Khi có ai đó hỏi 'Kết quả kinh doanh thế nào?' thì đó **hầu như luôn là câu hỏi về lợi nhuận
> thuần**."* — ch. 8 · PDF tr. 69

Và một nhận xét về từ vựng mà sách kể bằng giọng chịu thua: **thu nhập trên cổ phần** và **tỷ suất giá
cả/lợi nhuận** đều tính từ lợi nhuận thuần, nên lẽ ra phải gọi là *"lợi nhuận trên cổ phần"*. *"Đúng là
rất lạ khi người ta không đơn giản gọi là… Nhưng người ta không gọi như thế."* — ch. 8 · PDF tr. 70.

---

## 9. Ba cách chữa lợi nhuận thuần thấp — cái nào rẻ, cái nào nhanh

> *"Ngoài cách chơi trò tiểu xảo với sổ sách, chỉ có **ba cách** khắc phục khả dĩ cho khả năng sinh
> lời thấp."* — ch. 8 · PDF tr. 70

| # | cách | sách nói về tốc độ |
| ---: | --- | --- |
| 1 | tăng những giao dịch bán hàng sinh lợi | *"gần như luôn đòi hỏi nhiều thời gian"* |
| 2 | hạ giá thành, điều hành hiệu quả hơn — **giảm COGS** | *"cũng tốn thời gian không kém"* |
| 3 | cắt chi phí hoạt động — *"gần như đồng nghĩa với việc cắt giảm số lượng nhân viên"* | ***"thường thì đây là phương pháp tức thời duy nhất"*** |

Sách xếp ba cách theo **tốc độ**. Nó chưa xếp theo **độ lớn**. Làm thử trên công ty mẫu — mỗi ô là mức
thay đổi cần thiết ở **riêng dòng đó** để đạt mục tiêu ở cột trái:

| muốn LN thuần tăng | cần thêm EBIT<br>(triệu $) | doanh thu<br>phải tăng | COGS<br>phải giảm | SG&A<br>phải giảm |
| --- | ---: | ---: | ---: | ---: |
| +5% | 23,1 | 1,19% | **0,34%** | 2,17% |
| **+10%** | **46,1** | **2,38%** | **0,68%** | **4,34%** |
| +25% | 115,2 | 5,96% | **1,71%** | 10,86% |
| +50% | 230,5 | 11,92% | **3,41%** | 21,72% |

⭐ Cùng một mục tiêu +10%, ba con số khác hẳn nhau: doanh thu **+2,38%** · COGS **−0,68%** · SG&A
**−4,34%**. Bất ngờ nhất là COGS — **tỷ lệ phải cắt nhỏ hơn bên SG&A đúng 6,4 lần**. Lý do đơn giản:
COGS là bắp thịt lớn nhất, 77,8 xu trên mỗi đô-la doanh thu, nên một phần trăm của nó lớn hơn nhiều
một phần trăm của bất kỳ dòng nào khác.

⚠️ **Vậy sao không ai làm cách rẻ nhất?** Vì bảng trên xếp theo **độ lớn**, còn thực tế xếp theo **độ
khó**. Cắt 0,68% COGS đòi bạn *"nghiên cứu quá trình sản xuất, tìm ra những điểm kém hiệu quả"* — vài
quý. Cắt 4,34% SG&A chỉ cần một quyết định. Đó là toàn bộ nội dung của từ **"tức thời"** trong câu văn
của sách.

💼 Đặt con số 4,34% ấy vào người thật. Nếu SG&A phần lớn là lương và một nhân sự tốn 100.000 đô-la một
năm *(giả định của bài học, sách không nêu)*, thì 46,1 triệu đô-la = **461 người**. Đó là cái giá thực
của dòng chữ *"+10% lợi nhuận"* trên một bản trình chiếu.

Sách cảnh báo ngay sau đó, và bằng một ví dụ tự phản:

> *"Tất nhiên, biện pháp cắt giảm nhân công **có thể phản tác dụng**. Tinh thần làm việc sẽ sa sút.
> Những người giỏi mà CEO muốn giữ có thể bắt đầu muốn đi tìm việc ở nơi khác."* — ch. 8 · PDF tr. 70

Al Dunlap cắt người ở Sunbeam, thu nhập tăng, Phố Wall đẩy cổ phiếu lên — rồi chính giá cổ phiếu cao
làm **không ai mua nổi công ty**, mà chiến lược của Dunlap lại là *"luôn phải bán công ty ở mức có lợi
nhuận"*. Sunbeam *"buộc phải lê lết tồn tại cho đến khi mọi sự lộ rõ rành rành"* và ông ta bị hội đồng
quản trị sa thải (PDF tr. 70–71).

Kết luận của chương:

> *"Đối với hầu hết các doanh nghiệp, biện pháp quản lý với tầm nhìn dài hạn… sẽ hiệu quả hơn. Dĩ
> nhiên, chi phí hoạt động cũng phải cắt giảm. Nhưng nếu đó là **mục tiêu duy nhất** mà bạn quan tâm,
> thì có lẽ bạn **chỉ đang cố trì hoãn ngày phán quyết** mà thôi."* — ch. 8 · PDF tr. 71

---

## 10. 📚 Hộp công cụ — chênh lệch tốt hay xấu?

**Chênh lệch** (*variance*) chỉ là sự khác biệt: giữa ngân sách và thực tế, giữa tháng này và tháng
trước. Sách khuyên dùng **tỷ lệ phần trăm** vì *"chúng mang lại cơ sở so sánh dễ dàng và nhanh chóng"*.

Cái bẫy nằm ở dấu:

> *"**Vấn đề nan giải duy nhất** với chênh lệch là ở việc xác định xem liệu chênh lệch đó là tốt hay
> xấu… Đôi khi, giới tài chính tỏ ra giúp đỡ, và cho bạn biết bằng một lưu ý nhỏ rằng khi chênh lệch
> được đặt trong dấu ngoặc… thì đó là chênh lệch bất lợi. **Nhưng thường thì bạn phải tự tìm hiểu.**"*
> — ch. 8 · PDF tr. 71

| khoản mục | ngân sách | thực tế | cột "phép toán" | cột "tốt/xấu" |
| --- | ---: | ---: | ---: | ---: |
| Doanh thu | 8.500 | 8.689 | +189 | 189 |
| Giá vốn hàng bán | 6.600 | 6.756 | +156 | **(156)** |
| SG&A | 1.050 | 1.061 | +11 | **(11)** |

⭐ Dòng doanh thu và dòng giá vốn **đều dương** ở cột "phép toán". Một cái là tin tốt, một cái là tin
xấu. Cột phải đảo dấu để nói điều đó — **nhưng không phải báo cáo nào cũng làm vậy**:

> *"Đôi khi dấu ngoặc đơn hay dấu trừ chỉ cho ta biết chênh lệch **trong phép toán**, chứ không chỉ ra
> sự tốt xấu. Trong trường hợp đó, dấu ngoặc ở dòng doanh thu có khi là **tốt**, còn dấu ngoặc ở dòng
> chi phí có thể mang ý nghĩa **xấu**."* — ch. 8 · PDF tr. 71–72

Và đây là lý do nên đọc cả hai dòng chứ không riêng dòng đầu:

| | |
| --- | ---: |
| doanh thu vượt ngân sách | **+2,2%** |
| lợi nhuận gộp vượt ngân sách | **+1,7%** |

Doanh thu vượt 2,2% nhưng lợi nhuận gộp chỉ vượt 1,7%, vì giá vốn cũng vượt theo. Báo ra ngoài con số
*"doanh thu vượt kế hoạch"* là **đúng** — nó chỉ không phải tin tốt đúng bằng mức nó nghe.

💼 Cách làm sách khuyên: *"tự tính toán, tìm xem những chênh lệch được cho biết là tốt hay xấu, rồi
kiểm tra xem chúng được thể hiện như thế nào. Hãy đảm bảo rằng bạn thực hiện các phép tính cho **cả
hai** khoản doanh thu và chi phí."*

---

## 11. Adelphia — tạo doanh thu từ không khí

Chương 8 đóng lại bằng một ví dụ mà sách rào trước: *"Đừng cố thử thủ thuật dưới đây trong công ty của
bạn: **đó là một kiểu gian lận**."*

Cơ chế, theo sách (PDF tr. 72):

1. Adelphia mua hộp thu sóng truyền hình cáp, giá **500 đô-la**.
2. Adelphia tính **phí marketing 26 đô-la** mỗi hộp **cho nhà cung cấp**, vì đã dùng hộp của họ.
3. Nhà cung cấp **nâng giá lên 526** đúng bằng mức đó.
4. Hoá đơn 526 trừ 26 phí marketing → Adelphia vẫn trả **500**. *"Thậm chí chẳng cần phải trao đổi
   bằng tiền mặt."*
5. Nhưng 26 đô-la vào **doanh thu ngay**, còn chi phí marketing thì *"được khấu hao trong nhiều năm"*
   — và **không hề có chiến dịch marketing nào**, *"theo những gì Adelphia thừa nhận"*.

> *"Vì các chi phí được dẫn ra đã được khấu hao theo thời gian, nên **gần như toàn bộ 26 đô-la** thu
> được từ mỗi hộp sẽ đi thẳng xuống dòng kết quả kinh doanh cuối cùng của Adelphia. Tác động này đã
> thổi thu nhập của công ty từ **37 triệu đô-la năm 2000 lên 54 triệu đô-la năm 2001**."*
> — ch. 8 · PDF tr. 72

Phí bằng **5,2%** giá hộp — đủ nhỏ để không ai soi một hoá đơn 526.

**Sách không cho biết bao nhiêu cái hộp.** Suy ngược từ 17 triệu đô-la chênh lệch:

| khấu hao phí trong | rơi xuống dòng cuối | số hộp cần có |
| --- | ---: | ---: |
| 1 năm | 0,00 $/hộp | *không bao giờ đủ* |
| 3 năm | 17,33 $/hộp | 980.769 |
| 5 năm | 20,80 $/hộp | **817.308** |
| 10 năm | 23,40 $/hộp | 726.496 |

⭐ Khấu hao 5 năm thì mỗi hộp rơi **20,80 đô-la** xuống dòng cuối ngay năm đầu — đúng chữ *"gần như
toàn bộ"* của sách. Cần khoảng **817 nghìn cái hộp**. Giới hạn dưới tuyệt đối, nếu cả 26 đô-la rơi trọn
vẹn: **653.846 cái**.

Câu để tự trả lời: **một công ty truyền hình cáp có lắp ngần ấy hộp trong một năm không?** Nếu có, thì
thủ thuật này không cần quy mô kỳ lạ nào cả — nó chỉ cần một nhà cung cấp chịu nâng giá và một kế toán
chịu vốn hoá khoản phí.

⚠️ **Đây không phải mục 2.** Mục 2 đổi chỗ một con số có thật giữa hai dòng; mục này bịa ra một con số
**không có thật**. Sách vạch ranh giới rất rõ:

> *"**Nghệ thuật tài chính không mở rộng đến việc có thể tạo ra doanh thu và lợi nhuận từ không khí.**
> Đồng thời, hãy tỉnh táo trước những chiêu trò kế toán muôn hình vạn trạng. Cuốn sách này sẽ không
> trang bị cho bạn trở thành một kiểm toán viên tòa án, nhưng nó sẽ giúp bạn trở thành một nhà quản lý
> thông minh về tài chính, **có khả năng đặt ít nhất một hoặc hai câu hỏi**."* — ch. 8 · PDF tr. 72–73

Adelphia đã phá sản.

---

## 12. 🇻🇳 Đối chiếu Việt Nam

**Ranh giới COGS/chi phí hoạt động tồn tại y hệt trong VAS**, và cũng mờ y hệt. Nhưng cách trình bày
khác, và khác ở ba chỗ đáng nhớ.

**① VAS tách sẵn cái mà sách bảo phải tự tách.** Sách khen Microsoft vì tách chi phí bán hàng ra dòng
riêng. Báo cáo Việt Nam **bắt buộc** tách: *"chi phí bán hàng"* và *"chi phí quản lý doanh nghiệp"* là
hai dòng riêng theo mẫu B02-DN. Bạn được cho sẵn mức chi tiết mà người đọc báo cáo Mỹ phải đi xin.

Vinamilk 2024 (IFRS, triệu đồng): chi phí bán hàng **3.728.884** và chi phí quản lý **1.784.433** — tỷ
lệ hơn 2:1. Gộp chung thành một dòng "SG&A" là mất đúng thông tin đó.

**② Không có dòng EBIT.** Báo cáo VAS đi thẳng từ *"lợi nhuận gộp"* qua *"lợi nhuận thuần từ hoạt động
kinh doanh"* — nhưng dòng này **đã trừ chi phí tài chính** (gồm lãi vay) và **đã cộng doanh thu tài
chính**. Nó **không phải EBIT**. Muốn có EBIT theo nghĩa của mục 8, bạn phải tự cộng lãi vay trở lại,
và lấy số lãi vay từ **thuyết minh** hoặc từ báo cáo lưu chuyển tiền tệ.

⚠️ Đây là lỗi so sánh phổ biến nhất khi đọc báo cáo Việt Nam bằng khung của sách này. Trong
[`thuc_hanh/doi_chieu_viet_nam.py`](../thuc_hanh/doi_chieu_viet_nam.py), EBIT của Vinamilk được dựng lại
**từ lợi nhuận gộp trừ đi chi phí bán hàng, quản lý và chi phí khác** đúng vì lý do này.

**③ Khấu hao ở Việt Nam có khung cứng hơn.** Mục 5 dựa trên chỗ GAAP cho kế toán *"linh hoạt đáng kể"*
về tuổi đời tài sản. Việt Nam hẹp hơn: **Thông tư 45/2013/TT-BTC** (và các văn bản sửa đổi) quy định
**khung thời gian trích khấu hao tối thiểu – tối đa** cho từng nhóm tài sản cố định, và doanh nghiệp
phải chọn trong khung ấy.

Điều đó **không** làm biến mất thủ thuật của mục 5 — nó chỉ **thu hẹp biên độ**. Xe tải WMI kéo từ 8–10
năm lên 12–14 năm sẽ không qua được một khung như vậy; nhưng chọn cận trên thay vì cận dưới của khung
thì vẫn hợp pháp và vẫn đủ để dịch lợi nhuận. Câu hỏi cần đặt khi đọc báo cáo Việt Nam không phải *"họ
có phạm luật không"* mà là ***"họ nằm ở đâu trong khung, và năm ngoái họ nằm ở đâu"*** — và câu trả lời
nằm trong **thuyết minh chính sách kế toán**.

💼 Ba mục cần đọc trong thuyết minh của bất kỳ báo cáo Việt Nam nào, theo đúng thứ tự bài này:
*chính sách ghi nhận doanh thu* (bài 2) → *phân loại giá vốn* (mục 1–2) → *thời gian khấu hao* (mục 5).

---

## 13. Tự thử

Mọi bài dưới đây sửa tham số trong
[`thuc_hanh/bai-03-chi-phi-va-cac-tang-loi-nhuan.py`](../thuc_hanh/bai-03-chi-phi-va-cac-tang-loi-nhuan.py)
rồi chạy lại. Không có lời giải.

1. **Đẩy vạch tới hạn.** Ở mục 2, tìm số tiền phải chuyển từ COGS sang SG&A để biên lợi nhuận gộp đạt
   **30%**. Khi đó SG&A đã phình lên bao nhiêu phần trăm? Còn ai tin nổi con số ấy không?

2. **Vạch chạy ngược.** Vẫn mục 2, chuyển **từ SG&A vào COGS** (X âm). Biên gộp tụt tới đâu thì SG&A
   về 0? Vì sao chiều này gần như không ai làm?

3. **Đòn bẩy ở doanh nghiệp nhẹ vốn.** Ở mục 4, đổi COGS thành 1.000 cố định + 5.000 biến. Biên độ lợi
   nhuận thật giờ là bao nhiêu? So sánh với doanh nghiệp nặng vốn (3.000 cố định + 3.000 biến). Loại
   nào **an toàn hơn khi doanh thu sụt**?

4. **Điểm hoà vốn thật.** Vẫn mục 4, tìm hệ số sản lượng làm lợi nhuận **bằng đúng 0** ở cả hai mô
   hình. Hai điểm hoà vốn đó cách nhau bao xa? Mô hình nào **lạc quan hơn**?

5. **Xe tải hỏng giữa chừng.** Ở mục 5, công ty khấu hao 6 năm nhưng xe hỏng ở năm thứ 3. Phải ghi
   nhận khoản gì vào lúc đó, và nó rơi vào mục nào của bài này?

6. **WMI với thùng rác.** Ở mục 6, sách nói có **1,5 triệu thùng rác** kéo từ 12 lên 15/18/20 năm
   nhưng không cho giá mỗi thùng. Nếu tổng 716 triệu là đúng và đội xe đóng góp phần của nó trong 6
   năm, thì mỗi thùng rác phải có giá khoảng bao nhiêu? Con số đó có hợp lý không?

7. **Ngưỡng EBITDA.** Ở mục 8, khấu hao đang bằng 36,7% EBIT. Ở mức nào thì việc chọn EBIT hay EBITDA
   làm **đổi hẳn kết luận** (một cái dương, một cái âm)?

8. **Ba cách chữa ở biên mỏng.** Ở mục 9, thử với doanh nghiệp biên gộp chỉ **10%**. Ba con số phần
   trăm đổi thế nào? Doanh nghiệp biên mỏng nên tấn công dòng nào trước?

9. **Đảo chiều mục tiêu.** Vẫn mục 9, thay vì tăng lợi nhuận, hỏi ngược: doanh thu **giảm** bao nhiêu
   phần trăm thì lợi nhuận thuần về 0? Con số đó nói gì về mức an toàn của công ty mẫu?

10. **Adelphia với phí nhỏ hơn.** Ở mục 11, giảm phí từ 26 xuống **10 đô-la** mỗi hộp. Cần bao nhiêu
    hộp? Phí càng nhỏ thì càng **khó bị phát hiện** nhưng càng cần quy mô — đâu là điểm cân bằng?

---

## 14. Từ điển thuật ngữ

| Tiếng Việt | Tiếng Anh | Nghĩa ngắn |
| --- | --- | --- |
| Giá vốn hàng bán | cost of goods sold (COGS) | chi phí **liên quan trực tiếp** đến làm ra sản phẩm |
| Giá thành dịch vụ | cost of service (COS) | cùng ý, ở doanh nghiệp dịch vụ |
| Chi phí hoạt động | operating expenses | nhóm lớn còn lại — **không** liên quan trực tiếp |
| SG&A | sales, general and administrative | tên thường gặp của chi phí hoạt động |
| Chi phí chung | overhead | tên khác nữa của cùng nhóm |
| Trên vạch / dưới vạch | above / below the line | "vạch" = **lợi nhuận gộp** |
| GAAP | generally accepted accounting principles | 4.000 trang, nhưng chỉ cho **định hướng** |
| Khấu hao tài sản hữu hình | depreciation | phân bổ chi phí tài sản vật chất theo tuổi đời **ước tính** |
| Khấu hao tài sản vô hình | amortization | cùng ý tưởng, cho bằng sáng chế / bản quyền / lợi thế thương mại |
| Chi phí phi tiền mặt | noncash expense | tính vào kỳ này nhưng tiền **đã chi từ trước** |
| Khoản trả một lần | one-time charge | phí tái cơ cấu, xử lý nợ xấu, khoản đặc biệt |
| Gột rửa | taking the big bath | dồn hết tin xấu vào một kỳ |
| Đảo ngược | reversal | ước quá cao thì kỳ sau lãi tăng ảo |
| Lợi nhuận gộp | gross profit | doanh thu − COGS |
| Lợi nhuận hoạt động | operating profit / EBIT | lợi nhuận gộp − chi phí hoạt động (**gồm khấu hao**) |
| EBITDA | earnings before interest, taxes, D&A | EBIT **cộng lại** khấu hao |
| Lợi nhuận thuần | net profit | dòng dưới cùng, đã trừ tất cả |
| Chênh lệch | variance | khác biệt thực tế vs ngân sách — **phải tự xác định tốt/xấu** |
| 💼 Đòn bẩy hoạt động | operating leverage | tỷ trọng chi phí cố định — **cụm từ không có trong sách** |
| 💼 Biến phí / định phí | variable / fixed cost | cách phân loại **cắt chéo** với trên vạch / dưới vạch |

---

## 15. Câu hỏi tự kiểm tra

1. Hai nhóm chi phí cơ bản trên báo cáo kết quả kinh doanh là gì? (mục 1)
2. Kể ba khoản "vùng xám" mà sách nêu tên. (mục 1)
3. GAAP dày bao nhiêu trang, và nó **có** giải quyết vùng xám không? (mục 1)
4. Hai bài kiểm tra thay cho quy tắc là gì? Câu kết luận của sách sau đó là gì? (mục 1)
5. "Vạch" ám chỉ dòng nào? Cái gì ở trên, cái gì ở dưới? (mục 2)
6. Vì sao khoản mục trên vạch được chú ý hơn? (mục 2)
7. Bị chuyển từ trên vạch xuống dưới vạch thì hậu quả với bộ phận của bạn là gì? (mục 2)
8. Giám đốc nhà máy kém chỉ tiêu 20.000 và chuyển 25.000 ra khỏi COGS — kết quả? Có hợp pháp không? (mục 2)
9. Chuyển 87 triệu từ COGS sang SG&A của công ty mẫu: **biên gộp** đổi bao nhiêu? **EBIT** đổi bao
   nhiêu? **Lợi nhuận thuần** đổi bao nhiêu? (mục 2)
10. Vì sao cùng 87 triệu mà là "1,3% của COGS" nhưng "8,2% của SG&A"? (mục 2)
11. Vì sao Microsoft tách chi phí bán hàng ra dòng riêng còn công ty công nghệ sinh học thì không? (mục 3)
12. Giải thích ẩn dụ **cholesterol**. Sách có nói chi phí hoạt động là xấu không? (mục 3)
13. Cho một ví dụ chi phí **cố định** nằm **trong** COGS, và một chi phí **biến đổi** nằm **ngoài** COGS. (mục 4)
14. Mô hình "COGS biến 100%" sai theo hướng nào khi sản lượng tăng? Khi sản lượng giảm? (mục 4)
15. Xe tải 36.000: ba giả định 1 / 3 / 6 năm cho lợi nhuận thuần bao nhiêu? (mục 5)
16. Vì sao **cột EBITDA giống hệt nhau** ở mọi giả định khấu hao? (mục 5, mục 8)
17. **Chi phí phi tiền mặt** nghĩa là gì? Tiền đã đi đâu? (mục 5)
18. Vì sao kế toán dùng *amortization* thay vì *depreciation* cho tài sản vô hình? Sách giải thích được không? (mục 5)
19. Khấu hao trong **kinh tế** và trong **kế toán** khác nhau chỗ nào? Hệ quả cho bảng cân đối là gì? (mục 5)
20. Đội xe WMI trị giá bao nhiêu? Kéo dài 4 năm thì tiết kiệm bao nhiêu mỗi năm? (mục 6)
21. Tổng con số WMI bơm lên là bao nhiêu, và nó bằng bao nhiêu phần trăm khoản xử lý nợ xấu 1998? (mục 6)
22. Ba tên gọi khác của "khoản trả một lần" là gì? Tiếng lóng của nghề là gì? (mục 7)
23. Ước tính phí tái cơ cấu **quá cao** thì kỳ sau ra sao? **Quá thấp** thì sao? (mục 7)
24. Phép thử đơn giản nhất để biết một công ty đang lạm dụng "khoản một lần" là gì? AT&T làm gì? (mục 7)
25. Ba tầng lợi nhuận là gì? Mỗi tầng đã trừ những gì? (mục 8)
26. Trên công ty mẫu, chuỗi phần trăm doanh thu qua ba tầng là gì? (mục 8)
27. Vì sao EBIT **chưa** trừ thuế và lãi vay? (mục 8)
28. Giám đốc nhân sự công ty nghiên cứu thị trường suýt làm sai chuyện gì, và vì sao? (mục 8)
29. Vì sao Phố Wall chuyển từ EBIT sang EBITDA? EBITDA có "tốt hơn" không? (mục 8)
30. Ba cách chữa lợi nhuận thuần thấp là gì? Sách nói cách nào **tức thời**? (mục 9)
31. Để lợi nhuận thuần +10%: doanh thu phải tăng bao nhiêu %, COGS giảm bao nhiêu %, SG&A giảm bao nhiêu %? (mục 9)
32. Cách nào **rẻ nhất về tỷ lệ**? Vì sao vẫn không ai chọn nó trước? (mục 9)
33. Chuyện gì xảy ra với Al Dunlap ở Sunbeam, và vì sao chiến lược của ông ta tự đánh bại chính nó? (mục 9)
34. Doanh thu vượt ngân sách 189 và giá vốn vượt 156 — cả hai đều "+". Cái nào tốt? Làm sao biết? (mục 10)
35. Dấu ngoặc ở dòng doanh thu **luôn** là xấu, đúng hay sai? (mục 10)
36. Mô tả cơ chế Adelphia bằng năm bước. Có đồng tiền mặt nào đổi chủ không? (mục 11)
37. Vì sao *"gần như toàn bộ 26 đô-la"* rơi xuống dòng cuối chứ không phải toàn bộ? (mục 11)
38. Vì sao mục 11 khác hẳn về bản chất so với mục 2? (mục 11)
39. Báo cáo VAS **có** dòng EBIT không? Nếu không, dựng lại thế nào? (mục 12)
40. Thông tư 45/2013/TT-BTC làm hẹp chỗ nào của mục 5? Nó có xoá bỏ thủ thuật đó không? (mục 12)

---

## Tóm tắt một trang

```
╔══════════════════════════════════════════════════════════════════════════╗
║  BÀI 3 — CHI PHÍ VÀ CÁC TẦNG LỢI NHUẬN  (ch. 7–8, PDF tr. 54–73)         ║
╠══════════════════════════════════════════════════════════════════════════╣
║  GAAP DÀY 4.000 TRANG — và vẫn không nói lương quản đốc vào đâu.         ║
║     Chỉ có hai bài kiểm tra: HỢP LÝ và NHẤT QUÁN.                        ║
║     "Chừng nào logic đó vẫn được áp dụng nhất quán, thì chừng đó         ║
║      doanh nghiệp MUỐN LÀM GÌ CŨNG ĐƯỢC."                                ║
║                                                                          ║
║  ⭐ VẠCH = LỢI NHUẬN GỘP — và cái vạch DI CHUYỂN ĐƯỢC                    ║
║     giám đốc nhà máy: kém 20.000 → chuyển 25.000 ra khỏi COGS → đạt      ║
║     công ty mẫu: chuyển 87 triệu → biên gộp 22,2% → 23,2%                ║
║                  nhưng EBIT 652 và LN thuần 248 KHÔNG NHÚC MỘT LI        ║
║     87 triệu = 1,3% của COGS = 8,2% của SG&A  (COGS gấp 6,4 lần SG&A)    ║
║                                                                          ║
║  ⚠️ COGS ≠ BIẾN PHÍ. Hai cách phân loại CẮT CHÉO nhau:                   ║
║     lương quản đốc  → trong COGS  nhưng CỐ ĐỊNH                          ║
║     hoa hồng bán hàng → trong SG&A nhưng BIẾN ĐỔI                        ║
║     tin vào mô hình thô → dẹp bẹp đòn bẩy: ±2.000 thay vì ±2.450         ║
║                                                                          ║
║  ⭐ KHẤU HAO — "công cụ rất quyền năng của các nghệ sỹ tài chính"        ║
║     xe tải 36.000:  1 năm → LỖ 1.000  ·  3 năm → lãi 1.000               ║
║                     6 năm → lãi 1.500  (+50%)                            ║
║     → EBITDA = 2.000 Ở CẢ NĂM GIẢ ĐỊNH. Đó là lý do EBITDA tồn tại.      ║
║     → nhưng tổng cả đời xe VẪN LÀ 36.000. Chỉ DỊCH, không TẠO RA.        ║
║                                                                          ║
║  WMI: 20.000 xe × 150.000 = 3,0 TỶ. Kéo 4 năm → 86–125 triệu/NĂM.        ║
║     Đủ tích 716 triệu trong ~6 năm. Không cần thủ thuật kỳ quặc nào.     ║
║                                                                          ║
║  KHOẢN TRẢ MỘT LẦN — cờ vàng. Ước cao → kỳ sau lãi ảo.                   ║
║     Phép thử: ĐẾM. AT&T năm nào cũng "một lần" suốt đầu 1990s.           ║
║                                                                          ║
║  BA TẦNG:  100  →  22,2 (gộp)  →  7,5 (EBIT)  →  2,9 (thuần)             ║
║     EBITDA 10,3% — khấu hao bằng 36,7% EBIT, không phải chi tiết nhỏ.    ║
║                                                                          ║
║  ⭐ BA CÁCH CHỮA, để LN thuần +10%:                                      ║
║     doanh thu +2,38%  ·  COGS −0,68%  ·  SG&A −4,34%                     ║
║     COGS RẺ NHẤT (6,4 lần) — nhưng SG&A là cái DUY NHẤT làm được ngay.   ║
║     4,34% SG&A ≈ 461 người. Đó là giá thực của "+10%".                   ║
║                                                                          ║
║  CHÊNH LỆCH: +189 doanh thu và +156 giá vốn — cùng dấu, ngược nghĩa.     ║
║     doanh thu vượt 2,2% nhưng lợi nhuận gộp chỉ vượt 1,7%.               ║
║                                                                          ║
║  ADELPHIA: 26 $/hộp vào doanh thu, chi phí khấu hao nhiều năm.           ║
║     +17 triệu thu nhập ⇒ cần ~817 nghìn hộp. KHÔNG đồng tiền nào đổi chủ.║
║     "Nghệ thuật tài chính KHÔNG mở rộng đến việc tạo ra lợi nhuận        ║
║      từ không khí." → phá sản.                                           ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Nguồn

- **Karen Berman & Joe Knight (với John Case), *Trí tuệ tài chính*** — bản dịch Alphabooks /
  NXB Lao Động Xã Hội, 4/2014. Tệp trong kho:
  `tai_lieu/Tri Tue Tai Chinh - Karen Berman & Joe Knight.pdf`.
  - **Phần II — Những đặc thù của báo cáo kết quả kinh doanh**, PDF tr. 35–73.
    - Ch. 7 *Chi phí và nợ phải trả*, PDF tr. 54–65
      — định nghĩa **COGS / COS** và *"hàng tấn các diễn giải"* (tr. 54); **vùng xám** — giám đốc nhà
      máy, quản đốc, hoa hồng (tr. 55); **GAAP 4.000 trang**, *"hợp lý và nhất quán"* (tr. 55);
      hai kịch bản — công ty kiến trúc và **giám đốc nhà máy 20.000 / 25.000** (tr. 56);
      định nghĩa **trên vạch / dưới vạch** (tr. 57); **Microsoft** và công ty công nghệ sinh học
      (tr. 57); **cholesterol** và *"việc đèo bòng"* (tr. 58); **COGS ≠ biến phí** — quản đốc và hoa
      hồng (tr. 58); ví dụ **xe tải chuyển phát 36.000** với ba giả định 1 / 3 / 6 năm (tr. 59–60);
      **Waste Management** — 3,54 tỷ, 20.000 xe × 150.000, 8–10 năm + 4, 1,5 triệu thùng rác,
      **716 triệu** (tr. 60–61); định nghĩa **chi phí phi tiền mặt** (tr. 62); **amortization** và
      khấu hao kinh tế vs kế toán (tr. 62–63); **khoản trả một lần**, *"taking the big bath"*,
      **Al Dunlap / Sunbeam**, **AT&T** (tr. 63–65)
    - Ch. 8 *Có nhiều kiểu lợi nhuận*, PDF tr. 66–73
      — nhập nhằng từ vựng lợi nhuận / thu nhập (tr. 66); định nghĩa **lợi nhuận** và ba loại
      (tr. 66); **lợi nhuận gộp**, tạp hoá vs trang sức, **Wal-Mart** (tr. 66–67); **giám đốc nhân sự
      công ty nghiên cứu thị trường** (tr. 67–68); **EBIT** và lý do chưa trừ thuế / lãi vay
      (tr. 68); **EBITDA** và lý do Phố Wall chuyển sang (tr. 69); **lợi nhuận thuần** và
      **ba cách chữa** (tr. 69–71); **Al Dunlap ở Sunbeam** (tr. 70–71);
      hộp công cụ **chênh lệch** (tr. 71–72); **Adelphia** — 500 / 26 / 526, 37 → 54 triệu
      (tr. 72–73)
  - Phụ lục, PDF tr. 223–227 — công ty mẫu, dùng ở mục 2, 8, 9, 10
- **Thông tư 45/2013/TT-BTC** của Bộ Tài chính — chế độ quản lý, sử dụng và trích khấu hao tài sản cố
  định; khung thời gian trích khấu hao. Nhắc ở [mục 12](#12--đối-chiếu-việt-nam).
- **Công ty Cổ phần Sữa Việt Nam (HOSE: VNM)** — Báo cáo tài chính hợp nhất đã kiểm toán 2024 theo
  IFRS, trong *Báo cáo thường niên Vinamilk 2024*, tr. 180–185.
  [Nguồn gốc](https://www.vinamilk.com.vn/bao-cao-thuong-nien/bao-cao/2024/doc/vi/bctc-ifrs.pdf),
  truy xuất 08/09/2026. Dùng ở [mục 12](#12--đối-chiếu-việt-nam).
- **Đã kiểm chứng bằng code** — [`thuc_hanh/bai-03-chi-phi-va-cac-tang-loi-nhuan.py`](../thuc_hanh/bai-03-chi-phi-va-cac-tang-loi-nhuan.py):
  - chuyển chi phí qua vạch: **EBIT và lợi nhuận thuần không đổi** ở mọi mức chuyển, chốt bằng `assert`;
  - xe tải: ba con số của sách (−1.000 / 1.000 / 1.500 và **+50%**) khớp, chốt bằng `assert`;
  - **EBITDA bằng 2.000 ở cả năm giả định khấu hao**, chốt bằng `assert`;
  - mô hình thô và mô hình thật: biên độ **±2.000 so với ±2.450**, chốt bằng `assert`;
  - WMI: khoảng thời gian cần thiết nằm trong 5–9 năm, chốt bằng `assert`;
  - chênh lệch: lợi nhuận gộp vượt **ít hơn** doanh thu vượt, chốt bằng `assert`.
- ⚠️ **Con số do bài học đặt ra, không có trong sách:** mức chuyển 87 / 174 / 435 triệu ở mục 2; toàn
  bộ cơ cấu biến phí / định phí ở mục 4; ngân sách 8.500 / 6.600 / 1.050 ở mục 10; chi phí nhân sự
  100.000 đô-la/năm ở mục 9; kỳ khấu hao 1 / 3 / 5 / 10 năm ở mục 11. Mọi con số **của sách** đều được
  trích kèm mốc `ch. N · PDF tr. M`.

---

<!-- BAN-DO -->

**Bản đồ khoá học**

| # | Bài | Chương sách | Ưu tiên |
| ---: | --- | --- | :---: |
| 0 | [Bắt đầu từ đâu](bai_00_bat_dau_tu_dau.md) | — | 🔸 |
| 1 | [Nghệ thuật tài chính](bai_01_nghe_thuat_tai_chinh.md) | ch. 1–3 | 🎯 |
| 2 | [Lợi nhuận chỉ là dự toán](bai_02_loi_nhuan_chi_la_du_toan.md) | ch. 4–6 | 🎯 |
| **3** | **Chi phí và các tầng lợi nhuận** ← *bạn đang ở đây* | ch. 7–8 | 🎯 |
| 4 | [Bảng cân đối kế toán](bai_04_bang_can_doi_ke_toan.md) | ch. 9–11 | 🎯 |
| 5 | [Vì sao bảng cân đối lại cân](bai_05_vi_sao_bang_can_doi_lai_can.md) | ch. 12–13 | 🎯 |
| 6 | [Lợi nhuận ≠ tiền mặt](bai_06_loi_nhuan_khac_tien_mat.md) | ch. 14–15 | 🎯⭐ |
| 7 | [Báo cáo lưu chuyển tiền tệ](bai_07_bao_cao_luu_chuyen_tien_te.md) | ch. 16–18 | 🎯⭐ |
| 8 | [Tỷ lệ lợi nhuận, đòn bẩy, thanh toán](bai_08_ty_le_loi_nhuan_don_bay_thanh_toan.md) | ch. 19–22 | 🎯 |
| 9 | [Tỷ lệ hiệu suất và phân rã DuPont](bai_09_ty_le_hieu_suat_va_dupont.md) | ch. 23 | 🎯⭐ |
| 10 | [Tính tỷ lệ hoàn vốn đầu tư](bai_10_tinh_ty_le_hoan_von_dau_tu.md) | ch. 24–25 | 🔸 |
| 11 | [Vốn lưu động và chu kỳ tiền mặt](bai_11_von_luu_dong_va_chu_ky_tien_mat.md) | ch. 26–28 | 🎯⭐ |
| 12 | [Tổ chức có trí tuệ tài chính](bai_12_to_chuc_co_tri_tue_tai_chinh.md) | ch. 29–31 | 🔸 |

🎯 vòng 1 — học kỹ · 🔸 vòng 2 — đọc hiểu · ⭐ chương dùng được ngay trong công việc

Chỉ mục môn học: [README.md](../README.md)

<!-- /BAN-DO -->
