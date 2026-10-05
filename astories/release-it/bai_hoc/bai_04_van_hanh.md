# Bài 4 — Vận hành: nhìn thấy hệ thống và để nó thay đổi mà không đau

> [!info] Về bài này
> Dựng từ **Part IV — Operations** của *Release It!* (Michael T. Nygard, 2007, `tai_lieu/`, `tr. 251–335`): case **Ch.16 "Phenomenal Cosmic Powers, Itty-Bitty Living Space"** (tr. 252–264), **Ch.17 Transparency** (tr. 265–309), **Ch.18 Adaptation** (tr. 310–335).
> Trích theo `Ch. N` và `tr. X` (**số trang in = số trang PDF**). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, dịch gọn ngay dưới.
> Đây là **bài cuối** của khoá 5 bài; mục 16 khép lại cả khoá.
> *Cần đọc trước:* [Bài 1 — Ổn định](bai_01_on_dinh.md). Nên đọc lại [Bài 0 — Nhập môn](bai_00_nhap_mon.md) trước mục 16.

## Mục lục

1. [Mở đầu: Black Friday ở nhà bố mẹ](#1-mở-đầu-black-friday-ở-nhà-bố-mẹ)
2. [Mổ xẻ ca Black Friday: năm phút thay vì sáu giờ](#2-mổ-xẻ-ca-black-friday-năm-phút-thay-vì-sáu-giờ)
3. [Minh bạch: nghe tiếng máy như thợ máy tàu thuỷ](#3-minh-bạch-nghe-tiếng-máy-như-thợ-máy-tàu-thuỷ)
4. [Bốn góc nhìn: quá khứ, tương lai, hiện trạng, khoảnh khắc](#4-bốn-góc-nhìn-quá-khứ-tương-lai-hiện-trạng-khoảnh-khắc)
5. [Minh bạch phải được thiết kế, không gắn thêm](#5-minh-bạch-phải-được-thiết-kế-không-gắn-thêm)
6. [Log: công cụ cũ nhất vẫn đáng tin nhất](#6-log-công-cụ-cũ-nhất-vẫn-đáng-tin-nhất)
7. [Hệ thống giám sát và điều nó không thấy](#7-hệ-thống-giám-sát-và-điều-nó-không-thấy)
8. [Chuẩn giám sát và nên phơi ra những gì](#8-chuẩn-giám-sát-và-nên-phơi-ra-những-gì)
9. [Cơ sở dữ liệu vận hành (OpsDB)](#9-cơ-sở-dữ-liệu-vận-hành-opsdb)
10. [Quy trình hỗ trợ: dữ liệu không ai nhìn thì vô dụng](#10-quy-trình-hỗ-trợ-dữ-liệu-không-ai-nhìn-thì-vô-dụng)
11. [Thích nghi: hệ thống ra đời vào ngày ra mắt](#11-thích-nghi-hệ-thống-ra-đời-vào-ngày-ra-mắt)
12. [Thiết kế phần mềm dễ thích nghi](#12-thiết-kế-phần-mềm-dễ-thích-nghi)
13. [Kiến trúc doanh nghiệp như một hệ sinh thái](#13-kiến-trúc-doanh-nghiệp-như-một-hệ-sinh-thái)
14. [Release không nên đau](#14-release-không-nên-đau)
15. [Triển khai không downtime: mở rộng, rollout, dọn dẹp](#15-triển-khai-không-downtime-mở-rộng-rollout-dọn-dẹp)
16. [Khép lại khoá học: từ feature complete tới production ready](#16-khép-lại-khoá-học-từ-feature-complete-tới-production-ready)
17. [Đối chiếu 2026](#17-đối-chiếu-2026)
18. [Áp dụng vào việc của bạn](#18-áp-dụng-vào-việc-của-bạn)
19. [Từ điển thuật ngữ](#19-từ-điển-thuật-ngữ)
20. [Câu hỏi tự kiểm tra](#20-câu-hỏi-tự-kiểm-tra)
21. [Tóm tắt một trang](#tóm-tắt-một-trang)
22. [Nguồn](#nguồn)

---

## 1. Mở đầu: Black Friday ở nhà bố mẹ

Mỗi ngành có "niên giám" riêng, Nygard mở chương: bảo hiểm xoay quanh kỳ đăng ký, hàng hoa xoay quanh Valentine, còn bán lẻ xoay quanh "mùa lễ", khi có tới 50% doanh thu cả năm rơi vào tháng 11 và 12 (tr. 252–253). Ở Mỹ, mùa ấy mở bằng Lễ Tạ ơn và cơn hoảng loạn mua quà gọi là **Black Friday**.

> [!quote] Release It! — Ch.16 (tr. 253)
> "Traffic at online stores can increase by 1,000%. This is the real load test, the only one that matters."
>
> *Lưu lượng ở cửa hàng trực tuyến có thể tăng 1.000%. Đó mới là bài kiểm tải thật, bài duy nhất có ý nghĩa.*

**Trước giờ G.** Khách của Nygard ra mắt cửa hàng trực tuyến vào mùa hè. Đội bước vào mùa lễ với "lạc quan thận trọng": server gần gấp đôi, có dữ liệu về mức tải làm độ trễ leo, và nhất là có **tầm nhìn và quyền điều khiển vào bên trong** hệ thống hơn mọi hệ thống ông từng làm; theo ông, đó rốt cuộc là khác biệt giữa một cuối tuần khó khăn nhưng thành công và một thảm hoạ (tr. 254). Ông về nhà bố mẹ nghỉ lễ, vẫn mang laptop (tr. 254). Công cụ của ông là bộ script Perl **cào màn hình** giao diện quản trị HTML của application server: đọc, đặt thuộc tính, gọi phương thức trên mọi thành phần, lấy mẫu mọi server rồi lặp. Nhờ nó, cả đội thuộc nhịp bình thường của trang (tr. 255).

**Lễ Tạ ơn** trôi qua với số đơn một ngày bằng cả tháng Mười, và trang đứng vững (tr. 256). **Sáng Black Friday**, độ trễ vẫn quanh 250 mili giây; ông ra phố với mẹ mua đồ nấu cà ri, và nửa đường thì SOC (trung tâm giám sát vận hành) gọi: "SiteScope đang báo đỏ trên tất cả DRP" (tr. 256). SiteScope truy cập trang như khách thật; DRP là các instance phục vụ trang; tất cả đỏ là trang sập, mất đơn **khoảng một triệu đô mỗi giờ**, và restart cuốn chiếu không cứu được (tr. 257).

**Dấu hiệu sinh tồn.** Session rất cao; độ trễ cao; CPU của web, application, database **thấp, thấp thật sự**; server tìm kiếm, "nghi phạm thường trực", vẫn khoẻ; luồng xử lý gần như bận hết, nhiều luồng đã xử lý request hơn năm giây (tr. 258). Và một cái bẫy trong chính số liệu:

> [!quote] Release It! — Ch.16 (tr. 258)
> "Because requests were timing out, it was effectively infinite. The statistics showed us only the average of requests that completed."
>
> *Vì request bị hết giờ, độ trễ thực chất là vô hạn. Số liệu chỉ cho chúng tôi trung bình của những request đã hoàn tất.*

Đã gần chín mươi phút từ khi trang sập, sắp lỡ SLA (tr. 259).

**Xét nghiệm.** Thread dump trên mọi DRP cho cùng một mẫu: vài luồng đang gọi xuống hệ thống phía sau, còn lại chờ kết nối để gọi.

> [!quote] Release It! — Ch.16 (tr. 259)
> "The waiting threads were all blocked on a resource pool, one that had no timeout."
>
> *Các luồng đang chờ đều bị chặn trên một resource pool, một pool không có timeout.*

Toàn bộ 3.000 luồng chờ một câu trả lời không bao giờ tới, nên CPU thấp (tr. 259). *Ghi chú của khoá:* tr. 259 và 261 ghi 100 (DRP, server), còn các hình 16.1–16.3 ghi 20 host, 75 DRP; sách không giải thích. Bộ số 20 host, 75 instance, 3.000 luồng, 450 luồng này cũng là bộ số của Hình 4.13 ở [Bài 1 — Ổn định](bai_01_on_dinh.md), nơi Nygard nêu kịch bản giả định về một đợt khuyến mãi đè bẹp hệ thống lên lịch. Hệ thống đơn hàng phía sau, 450 luồng, cũng y hệt: mọi luồng chờ gọi hệ thống **lên lịch giao hàng tận nhà**, của một nhóm không trực 24/7 (tr. 259).

**Chuyên gia vào cuộc.** Trong bốn server lên lịch, hai đang **bảo trì đúng cuối tuần lễ**, một trục trặc. Server còn lại chịu được 25 request đồng thời mà đang nhận khoảng 90, kẹt ở 100% CPU; kỹ sư trực được nhắn vài lần nhưng không phản hồi (tr. 260–261):

> [!quote] Release It! — Ch.16 (tr. 261)
> "All the false positives had quite effectively trained them to ignore high CPU conditions."
>
> *Tất cả những lần báo động giả đã huấn luyện họ, rất hiệu quả, để phớt lờ tình trạng CPU cao.*

Rồi người tài trợ nghiệp vụ báo tin: marketing đã in quảng cáo kẹp báo sáng thứ Sáu, **miễn phí giao hàng tận nhà cho mọi đơn online trước thứ Hai**. Cả cầu hội nghị lần đầu tiên im lặng sau bốn giờ (tr. 261). Ba tầng 3.000 / 450 / 25, kéo dài tới thứ Hai, và không có kịch bản nào cho tình huống này (tr. 261–262).

**Phác đồ.** Lời giải duy nhất là bớt gọi hệ thống lên lịch, mà hệ thống đơn hàng không có cách bóp. Tia hy vọng: code cửa hàng dùng một connection pool **riêng** cho request lên lịch, "có lẽ là một ví dụ của định luật Conway", và chính nó cứu cả cuối tuần (tr. 262). Không có thuộc tính `enabled`, thì:

> [!quote] Release It! — Ch.16 (tr. 262)
> "A resource pool with a zero maximum is effectively disabled anyway."
>
> *Một resource pool có mức tối đa bằng không thì dù sao cũng coi như đã tắt.*

Pool trả null thì người dùng thấy lời nhắn lịch sự (tr. 262). Đặt `max` về 0 trên **một** DRP: không có gì xảy ra, vì `max` chỉ có tác dụng lúc pool khởi động. Gọi thêm `stopService()` rồi `startService()`: DRP ấy sống lại, rồi bị cân tải dồn hết request vào (tr. 262–263). Chạy cho tất cả DRP:

> [!quote] Release It! — Ch.16 (tr. 263)
> "If we had needed to change the configuration files and restart all the servers, it would have taken more than six hours under that level of load. Dynamically reconfiguring and restarting just the connection pool took less than five minutes (once we knew what to do)."
>
> *Nếu phải sửa file cấu hình rồi restart mọi server thì dưới mức tải đó sẽ mất hơn sáu giờ. Cấu hình lại động và chỉ khởi động lại connection pool mất chưa tới năm phút (một khi đã biết phải làm gì).*

Khoảng chín mươi giây sau, SiteScope xanh lại. Ông viết thêm một script một lệnh để người trực tự vặn mức tối đa; nó được dùng suốt cuối tuần: người tài trợ nghiệp vụ muốn tăng khi tải nhẹ và hạ về **một** (không phải không) khi tải nặng, vì đặt 0 là tắt hẳn giao hàng tận nhà (tr. 263). Rồi ông đi dỗ con ngủ.

## 2. Mổ xẻ ca Black Friday: năm phút thay vì sáu giờ

Phần này là **cách khoá đọc lại** ca trên; Ch.16 không tự liệt kê bài học, ngoài khung ROC ở cuối.

**Nguyên nhân gốc là chuyện ổn định**: điểm tích hợp (integration point) chậm, pool không timeout, ba tầng công suất lệch nhau, cộng lịch bảo trì của nhóm khác và tờ quảng cáo. [Bài 1 — Ổn định](bai_01_on_dinh.md) gọi tên từng mắt xích ấy. **Nhưng cái cứu trang là chuyện vận hành**: *nhìn* vào bên trong ở mức thành phần, *điều khiển* thành phần khi đang chạy, và *script hoá* thao tác. Chi tiết báo động giả dạy người ta phớt lờ cảnh báo thật sẽ quay lại ở Ch.17 (tr. 303–304). *Ghi chú của khoá:* chuyện "trung bình" chỉ tính request đã xong thì Ch.17 không bàn lại, nhưng sách SRE của Google biến nó thành quy tắc (mục 17).

Khung cuối chương giới thiệu **Recovery-Oriented Computing (ROC)**, dự án chung Berkeley–Stanford. Ba nguyên lý: hỏng hóc là không tránh được; không thể dự đoán trước mọi kiểu hỏng; và hành động của con người là một nguồn lớn gây sự cố. Khác phần lớn nghiên cứu độ tin cậy vốn tìm cách loại bỏ nguồn hỏng, ROC chấp nhận hỏng hóc sẽ tới, "một chủ đề lớn của cuốn sách này" (tr. 264). Khả năng khởi động lại từng thành phần thay vì cả server, như trong ca trên, là một khái niệm then chốt của ROC (tr. 263).

Nygard khuyên theo ba trọng tâm của ROC: khoanh vùng thiệt hại, tự động phát hiện lỗi, khởi động lại mức thành phần (tr. 264).

## 3. Minh bạch: nghe tiếng máy như thợ máy tàu thuỷ

Thợ máy lành nghề trên tàu biết sắp có chuyện chỉ qua tiếng động cơ diesel. Hệ thống của ta thì chạy trong những chiếc hộp vô diện, ta ngồi khác phòng, khác thành phố. Muốn có "nhận thức môi trường" như người thợ máy, ta phải **xây minh bạch vào hệ thống** (tr. 265). Nygard định nghĩa **minh bạch** là những phẩm chất cho phép người vận hành, dev và người tài trợ nghiệp vụ hiểu xu hướng lịch sử, hiện trạng, trạng thái tức thời và dự báo tương lai của hệ thống (tr. 265).

> [!quote] Release It! — Ch.17 (tr. 265)
> "Transparent systems communicate, and in communicating, they train their attendant humans."
>
> *Hệ thống minh bạch thì giao tiếp, và trong khi giao tiếp, chúng huấn luyện những con người chăm sóc chúng.*

Thiếu tầm nhìn mức thành phần, đội Black Friday chỉ biết trang chậm mà không biết vì sao, như nuôi con cá vàng ốm (tr. 265–266). Thiếu dữ liệu đáng tin, quyết định sẽ dựa trên "thế lực chính trị, định kiến, hay kiểu tóc của ai đó" (tr. 266).

> [!quote] Release It! — Ch.17 (tr. 266)
> "Without transparency, the system will drift into decay, functioning a bit worse with each release. Systems can mature well if, and only if, they have some degree of transparency."
>
> *Không có minh bạch, hệ thống sẽ trôi dần vào mục ruỗng, chạy tệ hơn một chút sau mỗi lần release. Hệ thống trưởng thành tốt khi và chỉ khi nó có một mức minh bạch nào đó.*

## 4. Bốn góc nhìn: quá khứ, tương lai, hiện trạng, khoảnh khắc

Câu "Mọi thứ thế nào?" nghĩa rất khác khi đến từ CEO hay từ quản trị hệ thống, như câu "Thời tiết thế nào?" với người làm vườn, phi công và nhà khí tượng (tr. 267). Nygard chia minh bạch thành bốn góc nhìn.

**Xu hướng lịch sử** (tr. 267–268): ngoại suy ngày mai từ hôm qua, cho số liệu nghiệp vụ lẫn hệ thống; hợp với một cơ sở dữ liệu (OpsDB, mục 9) và báo cáo hơn là dashboard.

**Dự báo tương lai** (tr. 268–269): "thời tiết hôm qua" của Beck và Fowler, đoán hôm nay giống hôm qua đúng khoảng 70%. Mô hình "đủ tốt" từ tương quan trong dữ liệu cũ là dùng được, nhưng phải kiểm lại sau **mỗi release**, vì release có thể phá tương quan. "Qua được mùa lễ này không?" là dự báo chồng dự báo, sai số không nhân đôi mà bình phương (tr. 269).

**Hiện trạng** (tr. 270–273): người béo đang chạy bộ, hành vi tức thời hướng tới sức khoẻ, nhưng hiện trạng có thể chỉ cách cơn đau tim một "thịch" (tr. 270). Hiện trạng dựng từ **sự kiện** (có sự kiện *bắt buộc*, như file tồn kho hằng ngày, vắng mặt mới đáng báo động) và **tham số** (thread pool, connection pool, điểm tích hợp, circuit breaker..., trong đó có "luồng bận quá năm giây") (tr. 270–271). *Ghi chú của khoá:* "năm giây" đúng là con số của sáng Black Friday.

> [!quote] Release It! — Ch.17 (tr. 271)
> "For continuous metrics, a handy rule-of-thumb definition for nominal would be “the mean value for this time period plus or minus two standard deviations.” The choice of time period is where it gets interesting."
>
> *Với số đo liên tục, một định nghĩa ngón tay cái tiện dụng cho "trong ngưỡng" là "giá trị trung bình của khoảng thời gian này cộng trừ hai độ lệch chuẩn". Chọn khoảng thời gian mới là chỗ thú vị.*

Với số đo theo lưu lượng, khoảng ổn định nhất thường là "giờ trong tuần" (2 giờ chiều thứ Ba); ngày trong tháng ít nghĩa (tr. 271).

**Dashboard.** Hình 17.1 (tr. 273), định nghĩa màu Nygard từng dùng:

```
XANH  TẤT CẢ: sự kiện mong đợi đã có; không bất thường; số đo trong ngưỡng.
VÀNG  ÍT NHẤT MỘT: sự kiện mong đợi chưa có; bất thường mức vừa; tham số
      trên HOẶC dưới ngưỡng; tính năng phụ bị circuit breaker cắt.
ĐỎ    ÍT NHẤT MỘT: sự kiện BẮT BUỘC chưa có; bất thường mức cao; tham số
      lệch XA ngưỡng; "đang nhận request" = false.
```

Định nghĩa này bắt được một tình trạng hay bị bỏ sót, "too much of a good thing": trên ngưỡng cũng là vàng (tr. 272). Dashboard cũng phải hiện batch job đã chạy chưa, vì "một số lượng đáng sửng sốt" sự cố nghiệp vụ lần về batch job hỏng âm thầm 33 ngày liền (tr. 272).

**Hành vi tức thời** (tr. 273–275) trả lời câu "Chuyện quái gì đang xảy ra?", địa hạt của giám sát và thread dump. Vận hành thường thấy bị đe doạ khi người khác đòi xem góc này (tr. 274).

> [!quote] Release It! — Ch.17 (tr. 274)
> "When sponsors ask for more information, what they usually want is status, not instantaneous behavior."
>
> *Khi người tài trợ đòi thêm thông tin, cái họ thường muốn là hiện trạng, không phải hành vi tức thời.*

## 5. Minh bạch phải được thiết kế, không gắn thêm

Một nhà bán lẻ tối ưu chuỗi batch job đêm để hàng lên web sớm hơn; batch xong sớm hai giờ, nhưng hàng vẫn lên lúc 5–6 giờ sáng vì còn một tiến trình song song chạy dài (tr. 275). "Tầm nhìn cục bộ dẫn tới tối ưu cục bộ." Ca khác: chỉ khi đặt thống kê mọi cache lên một trang, đội mới thấy mỗi server đang đá món hàng ra khỏi cache của mọi server khác; không thấy thì đã thêm server, và mỗi server lại làm tệ thêm (tr. 275). Theo Nygard, "thêm minh bạch" vào cuối giai đoạn phát triển cũng hiệu quả ngang với "thêm chất lượng" (tr. 275).

Lời khuyên thiết kế: giám sát nên như **bộ xương ngoài** dựng quanh hệ thống, không đan vào nó. Chọn số đo nào kích cảnh báo, ngưỡng đặt ở đâu, gộp trạng thái thế nào là **quyết định chính sách**, thay đổi với nhịp khác hẳn code, nên để ngoài ứng dụng (tr. 275).

Một tiến trình vốn mờ đục "như con mèo của Schrödinger", không nhìn thì không biết sống hay chết (tr. 276). Công nghệ **hộp đen** đứng ngoài, quan sát cái thấy được, gắn sau được; công nghệ **hộp trắng** chạy bên trong, hệ thống cố ý phơi mình, phải tích hợp lúc phát triển và khớp nối chặt hơn (tr. 276).

## 6. Log: công cụ cũ nhất vẫn đáng tin nhất

Hàng triệu đô cho các bộ quản lý ứng dụng và màn plasma khổng lồ, vậy mà file log vẫn là phương tiện thông tin đáng tin và linh hoạt nhất (tr. 276). Log là hộp trắng nhưng khớp nối lỏng nhất: mọi công cụ đều cào được log (tr. 277). Dù vậy, log bị lạm dụng nặng.

**Mức log** (tr. 277–278).

> [!quote] Release It! — Ch.17 (tr. 277)
> "Most developers implement logging as though they are the primary consumer of the log files. In fact, administrators and engineers in operations will spend far more time with these log files than developers will."
>
> *Phần lớn dev viết log như thể mình là người dùng chính của file log. Thật ra, quản trị và kỹ sư vận hành sẽ ở với những file này lâu hơn dev rất nhiều.*

Hệ quả: ERROR phải là thứ **vận hành cần hành động**. Người dùng nhập sai số thẻ thì không; circuit breaker nhảy sang "mở" hay mất kết nối database thì có; "một NullPointerException không tự động là một lỗi" (tr. 278). Và đừng để log debug ở production (tr. 278).

**Danh mục và mã thông điệp** (tr. 278–279). Gom mọi thông điệp vào một file tài nguyên và gắn mã cho từng dòng: vận hành và dev nói cùng một thứ, hết cảnh "chỉ nhớ nó nói gì đó về lỗi nghiêm trọng", và tra được trong run book.

**Yếu tố con người** (tr. 280–281).

> [!quote] Release It! — Ch.17 (tr. 280)
> "Above all else, log files are human-readable. That means they constitute a human-computer interface and should be examined in terms of human factors."
>
> *Trên hết, file log là thứ người đọc. Nghĩa là nó cấu thành một giao diện người-máy, và phải được xét theo yếu tố con người.*

Người vận hành Three Mile Island hiểu sai số đo chất làm mát và hành động sai ở mọi bước (tr. 280). Định dạng cột thẳng hàng giúp mắt người quét nhanh; định dạng hai dòng mặc định của `java.util.logging` thì "đánh bại cả người lẫn máy" (tr. 280–281).

**Vận hành kiểu bùa phép** (tr. 281–283). Máy nhắn tin của một quản trị viên kêu; cô lập tức failover database, vì tin rằng thông điệp báo database sắp hỏng. Thông điệp là:

> [!quote] Release It! — Ch.17 (tr. 282)
> "It said, “Data channel lifetime limit reached. Reset required.”"
>
> *Nó ghi: "Kênh dữ liệu đã đạt giới hạn thời gian sống. Cần reset."*

Chính Nygard viết dòng đó: một log debug báo kênh mã hoá tới nhà cung cấp đã chạy đủ lâu để khoá có nguy cơ lộ, và ứng dụng tự reset ngay sau đó. "Reset required" không nói *ai* phải reset, người đọc không có code, và ông quên tắt dòng debug (tr. 282–283). Gốc của huyền thoại: sáu tháng trước, Sybase sập, và dòng ấy là thứ cuối cùng được log trước đó. Liên hệ thời gian, không phải nhân quả:

> [!quote] Release It! — Ch.17 (tr. 283)
> "That temporal connection, combined with an ambiguous, obscurely worded message, led the administrators to perform weekly database failovers during peak hours for six months."
>
> *Mối liên hệ thời gian ấy, cộng với một thông điệp mơ hồ, tối nghĩa, khiến các quản trị viên failover database hằng tuần vào giờ cao điểm suốt sáu tháng.*

**Ghi chú cuối** (tr. 283): thông điệp nên mang **định danh để lần theo các bước của một giao dịch** (ID người dùng, session, giao dịch); đọc 10.000 dòng log sau sự cố mà có chuỗi để grep thì đỡ rất nhiều. Và log mọi **chuyển trạng thái** đáng chú ý, vì chúng quan trọng khi điều tra sau sự cố.

## 7. Hệ thống giám sát và điều nó không thấy

"Tiến trình chết không kể chuyện. Tiến trình treo cũng vậy" (tr. 283). Nên phải có công cụ hộp đen bên ngoài: agent trên host, đường truyền tin cậy, console cảnh báo (tr. 284). Agent bắt tốt đúng những gì được dặn trước; host sập thì agent sập theo, nên cần heartbeat; traffic giám sát không nên đi chung mạng production, kẻo mạng production hỏng thì giám sát tắt theo (tr. 284–285). Hệ thống thương mại thì hướng vào IT, khó chỉ ra tính năng nghiệp vụ nào chịu ảnh hưởng (tr. 286–287). Và:

> [!quote] Release It! — Ch.17 (tr. 287)
> "If there’s another major gap in these systems, it is that they can tell you only what the systems think is happening."
>
> *Nếu các hệ thống này còn một khoảng trống lớn nữa, thì là chúng chỉ nói được điều mà các hệ thống nghĩ là đang xảy ra.*

Mọi thành phần có thể "đang chạy" mà người dùng vẫn nhận kết quả tệ, điển hình khi luồng bị chặn (tr. 287). *Ghi chú của khoá:* đúng cảnh sáng Black Friday, CPU thấp, search khoẻ, còn SiteScope, công cụ đứng ở chỗ khách hàng, báo đỏ.

Hệ giám sát gần như luôn đã được chọn sẵn và sống lâu hơn cả cam kết về hệ điều hành, ngôn ngữ, nhà cung cấp phần cứng và sơ đồ tổ chức; để tránh bị khoá vào nhà cung cấp, hãy thiết kế theo **chuẩn** (tr. 289).

## 8. Chuẩn giám sát và nên phơi ra những gì

**SNMP** (từ 1988): "mọi thứ đều là biến"; nền tảng có sẵn SNMP cho ngay hàng nghìn biến, nhưng viết MIB cho code tự làm là việc lớn (tr. 289–291). **CIM** về nhiều mặt vượt SNMP về kỹ thuật nhưng tầng ứng dụng còn ít hỗ trợ (tr. 292–293). **JMX** dùng **MBean** làm proxy quản lý cho đối tượng, gọi được từ xa, ví dụ để đọc trạng thái hay ép reset một circuit breaker (tr. 293–295). Một trong những lợi ích tốt nhất là viết script được:

> [!quote] Release It! — Ch.17 (tr. 296)
> "Nevertheless, make your application’s administrative functions scriptable, and they will bless your name."
>
> *Dẫu vậy, hãy làm cho các chức năng quản trị của ứng dụng viết script được, và họ sẽ chúc phúc cho tên bạn.*

"Họ" là dân vận hành. Ông trỏ về lời than về giao diện quản trị đồ hoạ ở mục 14.4, phần của [Bài 3 — Thiết kế tổng quát](bai_03_thiet_ke_tong_quat.md). *Ghi chú của khoá:* bộ Perl cào GUI trong ca Black Friday chính là một lớp script tự chế.

**Nên phơi ra những gì** (tr. 297–298). Đoán trước số đo then chốt thì dễ sai, và đoán đúng thì nó cũng đổi theo thời gian.

> [!quote] Release It! — Ch.17 (tr. 297)
> "Provide universal visibility now, but externalize the policy so you can defer those decisions."
>
> *Cho tầm nhìn toàn diện ngay bây giờ, nhưng đưa chính sách ra ngoài để hoãn được những quyết định đó.*

Năm nhóm Nygard luôn thấy hữu ích (tr. 297–298):

| Nhóm | Ví dụ số đo |
| --- | --- |
| Lưu lượng | tổng request, số giao dịch, session đồng thời |
| Resource pool | trạng thái bật, tài nguyên đang mượn, mức cao nhất, **số luồng đang chờ tài nguyên** |
| Kết nối DB | số SQLException, số truy vấn, thời gian phản hồi |
| Điểm tích hợp | trạng thái circuit breaker, số timeout, loại lỗi, request đồng thời và mức cao nhất |
| Cache | số mục, bộ nhớ, tỉ lệ trúng, giới hạn cấu hình |

Mọi bộ đếm đọc như "trong n phút qua" (tr. 298). *Ghi chú của khoá:* hai hàng **Resource pool** và **Điểm tích hợp** đúng là những gì đội cần thấy sáng Black Friday.

## 9. Cơ sở dữ liệu vận hành (OpsDB)

Log và giám sát giỏi hành vi tức thời, kém ở quá khứ và tương lai. Hình 17.10 (tr. 299) chấm điểm:

```
                 Log               Giám sát          OpsDB
Lịch sử          kém               kém               rất hợp
Tương lai        kém               kém               rất hợp
Hiện trạng       được, tốn công    được, tốn công    rất hợp
Hành vi tức thời rất hợp           rất hợp           KHÔNG hợp
```

Nygard đề xuất **OpsDB** gom trạng thái và số đo từ mọi server, ứng dụng, batch job, làm "một tấm kính duy nhất" hiện số đo nghiệp vụ, số đo hệ thống và tương quan giữa chúng (tr. 299–300). Cấu trúc tựa mẫu Observation của Fowler (tr. 301–302): **Feature** (tính năng nghiệp vụ, đúng thứ SLA nói tới) cần nhiều **Node** (host, ứng dụng, job); Node sinh **Observation**, gồm Measurement (số đo định kỳ), Event, Status (chuyển trạng thái).

> [!quote] Release It! — Ch.17 (tr. 302)
> "It is not critical to the financial success of the system, so there is absolutely no reason that a failure in the OpsDb should have a noticeable effect on the system’s primary function."
>
> *Nó không trọng yếu với thành công tài chính của hệ thống, nên tuyệt đối không có lý do gì để một sự cố ở OpsDb gây ảnh hưởng thấy được lên chức năng chính.*

Từ dữ liệu tích luỹ, đặt **Expectation**: khoảng, khung thời gian hay trạng thái cho phép; vi phạm thì cảnh báo. Kỳ vọng nên lấy từ chính lịch sử để khớp thực tế và tránh báo động giả (tr. 303). Khung "The Danger of False Positives" kể một người vận hành bị hệ thống huấn luyện tới mức tắt chuông cảnh báo mà không hề ý thức (tr. 304). Kỳ vọng siết dần: CPU web server ">0% và <80%", rồi ">5% và <50%", rồi theo nhịp kinh doanh; và dữ liệu cũ phải cô đặc, theo mẫu Steady State (tr. 304).

## 10. Quy trình hỗ trợ: dữ liệu không ai nhìn thì vô dụng

Một báo cáo gửi tự động cho cả danh sách, và nửa danh sách có luật Outlook tự xoá nó. Nygard thấy vậy là biết báo cáo vô dụng, thậm chí tệ hơn (tr. 305).

> [!quote] Release It! — Ch.17 (tr. 305)
> "That report is an example of transparency without a closed-loop feedback process. It costs money to implement and operate but provides no value. It creates a false sense of security. The best data in the world can’t help if nobody is looking."
>
> *Báo cáo ấy là ví dụ về minh bạch mà không có vòng phản hồi khép kín. Nó tốn tiền làm và vận hành nhưng không mang lại giá trị. Nó tạo cảm giác an toàn giả. Dữ liệu tốt nhất thế giới cũng vô ích nếu không ai nhìn.*

Phản hồi hiệu quả là "hành động đáp lại dữ liệu có ý nghĩa": xem xét, diễn giải, cân các hành động (kể cả không làm gì), quyết định, thực hiện, quan sát lại (tr. 305). Nygard dẫn vòng **O-O-D-A** của John Boyd: quan sát không bị "spin" tô màu, và đi vòng nhanh hơn đối thủ (tr. 306–307).

Nhịp quan sát ông đề xuất (tr. 307–308): *hằng tuần* xem ticket tìm vấn đề lặp; *hằng tháng* xem tổng số và mức nghiêm trọng; *mỗi bốn đến sáu tháng* kiểm lại tương quan cũ; và xem đường bao nhu cầu, vì một khung giờ đông khách đột nhiên vắng có lẽ là hệ thống quá chậm lúc ấy. Số đo nào hết cho thông tin hữu ích thì thôi xem nó (tr. 308).

Tóm tắt chương: minh bạch cần ba điều, phơi phần bên trong, có phương tiện thu thập và hiểu dữ liệu, và một quy trình phản hồi hành động theo hiểu biết ấy (tr. 309).

## 11. Thích nghi: hệ thống ra đời vào ngày ra mắt

Dù tầm nhìn táo bạo tới đâu, hệ thống ra mắt bao giờ cũng kém hơn nó có thể đã là (tr. 310).

> [!quote] Release It! — Ch.18 (tr. 310)
> "The true birth of a system comes not on the day that design and development begins, or even when the project is conceived, but on the day it launches into production."
>
> *Ngày ra đời thật sự của một hệ thống không phải ngày bắt đầu thiết kế và phát triển, cũng không phải lúc dự án được nghĩ ra, mà là ngày nó ra mắt ở production.*

"Một hệ thống không thể thích nghi với môi trường là một hệ thống chết từ trong bụng mẹ" (tr. 310). Nó không tự vừa khít hơn nhờ được dùng; phần lớn thời gian nó huấn luyện người dùng "một cách đau đớn", và chỉ vừa hơn nhờ **hành động có chủ đích** (tr. 310). Petroski thay "hình thức theo chức năng" bằng **"form follows failure"**: cái dĩa, cái kẹp giấy đổi dạng chủ yếu vì những gì thiết kế cũ làm kém; mỗi release phần mềm cũng lấp một chỗ hụt hay giũa một chỗ lồi (tr. 311).

Thay đổi có giá, Nygard gọi là **năng lượng hoạt hoá**: thiết kế, phát triển, kiểm thử, cộng chi phí release. Nếu giá vượt giá trị thu về, hợp lý là không đổi (tr. 311). Và:

> [!quote] Release It! — Ch.18 (tr. 311)
> "Finally, as a matter of simple economics, somewhere between 40% and 90% of a system’s cost of development will be incurred after the first release."
>
> *Cuối cùng, như một lẽ kinh tế đơn giản, đâu đó từ 40% tới 90% chi phí phát triển của một hệ thống sẽ phát sinh sau lần release đầu tiên.*

Cái ít được hiểu hơn là cái giá của việc **đưa thay đổi ra thế giới thật** (tr. 311). Mục tiêu là thay đổi **"exoeconomic"**, chữ ghép theo mẫu *exothermic* (toả nhiệt): sinh ra nhiều tiền hơn chi phí của nó (tr. 312).

## 12. Thiết kế phần mềm dễ thích nghi

Nygard coi phần này là một "lớp phủ" lên phương pháp bạn chọn, tập trung vào khả năng đổi **mà không làm gián đoạn vận hành** (tr. 312).

**Tiêm phụ thuộc** (tr. 312–313): thành phần tương tác qua interface, một tác nhân khác "đấu dây"; nó khuyến khích khớp lỏng và giúp unit test.

**Thiết kế đối tượng** (tr. 314–316): "khớp nối ảnh hưởng tới thích nghi nhiều hơn độ gắn kết" (tr. 315). Cụm đối tượng khớp chặt giống **tinh thể trong kim loại**: tinh thể lớn thì dễ nứt; lan tới biên ứng dụng thì thành "cung điện pha lê" (tr. 315).

> [!quote] Release It! — Ch.18 (tr. 315)
> "These tend to be dead structures. Developers tiptoe through crystal palaces, speaking in hushed tones and trying not to touch anything."
>
> *Chúng thường là cấu trúc chết. Dev rón rén đi qua cung điện pha lê, nói khẽ và cố không chạm vào thứ gì.*

**Refactoring và unit test** (tr. 316–317): refactoring chống "kết tinh"; không có unit test thì refactoring chỉ là lục lọi ngẫu nhiên.

**Database linh hoạt** (tr. 317–319). Schema cứng thì lập trình viên vẫn lách, nhồi XML vào CLOB, và sự ô nhiễm ngữ nghĩa lan sang mọi bên dùng dữ liệu; vậy schema phải đổi được (tr. 318).

> [!quote] Release It! — Ch.18 (tr. 319)
> "Every schema should include a table that indicates the current structure revision."
>
> *Mọi schema nên có một bảng cho biết phiên bản cấu trúc hiện tại.*

Ứng dụng kiểm phiên bản lúc khởi động và, theo **Fail Fast**, từ chối khởi động nếu không dùng được schema; số phiên bản còn kích migration tự động kiểu Rails, và phải tăng cả khi chỉ đổi *cách hiểu* dữ liệu (tr. 319).

## 13. Kiến trúc doanh nghiệp như một hệ sinh thái

Có kiến trúc sư mơ một cỗ máy doanh nghiệp liền mạch, đi từ trên xuống với Zachman hay TOGAF; có quyền thì treo dự án chờ kiến trúc xong. "Tôi nhìn những người không tưởng ấy với sự nghi ngờ sâu sắc" (tr. 319). Hai giả định sai: kiến trúc có thể "xong", và tổ chức giữ được thời gian đứng yên trong lúc chờ (tr. 319–320). Tệ nhất, nó đòi các nhóm đổi đồng loạt; với thay đổi giao thức ESB, mọi hệ thống phải nâng cấp cùng lúc, nên thay đổi lớn "sẽ không bao giờ xảy ra". Hệ cơ khí, theo ông, vừa cứng nhắc vừa mong manh (tr. 320).

Nygard nhìn tổ chức như **hệ sinh thái**: ông từng thấy công ty có bảy bản cài SAP độc lập, rất kém hiệu quả nhưng rất bền, mỗi bản đổi độc lập được (tr. 320–321). Tiêu chí: kiến trúc có làm IT đáp ứng nhu cầu người dùng tốt hơn không (tr. 321). Trong một hệ thống, hãy dựng **cụm lỏng**: mất một thành viên như mất một cái cây trong rừng, và tầng này phụ thuộc vào tên dịch vụ hay IP ảo của tầng kia, không vào từng thành viên (tr. 321–323).

**Giao thức** (tr. 323–325). Hai đầu phải đổi cùng lúc thì cả hai phải downtime, và đội làm iteration hai tuần bị kéo theo đội phát hành theo quý (tr. 323–324).

> [!quote] Release It! — Ch.18 (tr. 324)
> "We must design protocols so that either endpoint can change independently of the other. The solution lies in protocol versioning."
>
> *Ta phải thiết kế giao thức sao cho mỗi đầu đổi được độc lập với đầu kia. Lời giải nằm ở việc đánh phiên bản giao thức.*

Có một giai đoạn bên cung cấp nói được cả bản N và N+1 (tr. 324–325). **Database** là đoạn gắt nhất (tr. 326–327):

> [!quote] Release It! — Ch.18 (tr. 326)
> "Integration databases—don’t do it! Seriously! Not even with views. Not even with stored procedures."
>
> *Database tích hợp: đừng làm! Nghiêm túc đấy! Kể cả qua view. Kể cả qua stored procedure.*

Hãy bọc database bằng web service; database nhiều hệ thống cùng chọc vào sẽ thành "nút thắt cứng nhắc" mà khả năng cao nhất là schema không bao giờ đổi. Cần dữ liệu cho báo cáo thì dùng ETL, tài khoản chỉ SELECT (tr. 326–327).

## 14. Release không nên đau

Một nhà bán lẻ có quy trình release sánh với phóng tàu NASA, từ chiều tới khuya, từng cần hơn hai mươi người. Vì gian nan nên ít release; ít nên mỗi lần lại khác; khác nên càng đau (tr. 327).

> [!quote] Release It! — Ch.18 (tr. 327)
> "Releases should about as big an event as getting a haircut (or compiling a new kernel, for you gray-ponytailed UNIX hackers)."
>
> *Release nên là sự kiện cỡ đi cắt tóc (hay biên dịch một kernel mới, với các hacker UNIX tóc đuôi ngựa hoa râm).*

Release thường xuyên buộc bạn giỏi release, và làm vòng phản hồi của chương 17 chạy nhanh hơn (tr. 327–328). Quy trình thủ công chỉ cầm cự được ba bốn lần một năm; làm chậm lịch release thì "giống như vì đau mà ít đi nha sĩ", chỉ tệ thêm. Cách đúng: giảm công sức, **rút người khỏi quy trình**, tự động hoá và chuẩn hoá (tr. 328).

**Chi phí** (tr. 328–330). Trừ công ty làm sản phẩm, chi phí release gần như không bao giờ có dòng trong ngân sách; khoản gián tiếp lớn nhất là downtime (tr. 328). Vận hành có lẽ tính availability chỉ theo downtime ngoài kế hoạch: 99,5% chỉ có nghĩa dưới 216 phút "bất ngờ" mỗi tháng, trong khi hệ thống có thể đã ngừng năm giờ trong cửa sổ thay đổi (tr. 330).

> [!quote] Release It! — Ch.18 (tr. 330)
> "Do the users of the system care whether downtime is planned or unplanned? No! To a user, down is down."
>
> *Người dùng có quan tâm downtime là có kế hoạch hay không? Không! Với người dùng, sập là sập.*

> [!note] Mở rộng — tự tính lại con số 216 phút
> Phần tính của khoá. Tháng 30 ngày có 43.200 phút; 0,5% là **216 phút**, khớp sách. Cộng năm giờ (300 phút) có kế hoạch thì tổng ngừng 516 phút, availability thật với người dùng khoảng **98,8%**. Đặt cạnh phép tính 98% và 99,99% ở [Bài 0 — Nhập môn](bai_00_nhap_mon.md): chính downtime "có kế hoạch" đẩy bạn tụt bậc số chín.

Khung "The View from Operations" (tr. 329): dev và nghiệp vụ nhìn release thấy cải tiến, vận hành thấy rủi ro, và "họ đều đúng". Về **thời điểm** (tr. 330): khách thường không biết ngày release, vậy mà Nygard từng ngồi họp go/no-go lúc 4 giờ chiều, QA nói chưa qua kiểm thử, và cả bàn vẫn giơ ngón cái. Sao lại đặt khách hàng vào rủi ro vì một ngày chọn tuỳ tiện từ nhiều tháng trước?

## 15. Triển khai không downtime: mở rộng, rollout, dọn dẹp

Ta đã hết chấp nhận downtime khi bảo trì phần cứng, sao lại chấp nhận khi đổi phần mềm? Gọi là "có kế hoạch" không xoá chi phí: downtime 10.000 đô/giờ thì bốn giờ triển khai tốn 40.000 đô (tr. 331).

> [!quote] Release It! — Ch.18 (tr. 331)
> "Ironically, it’s exactly because of the same architecture feature that is supposed to increase uptime: redundancy."
>
> *Trớ trêu thay, chính là vì đúng cái đặc điểm kiến trúc lẽ ra để tăng uptime: sự dư thừa.*

Nhiều server nghĩa là lúc triển khai có server ở bản N, có server ở N+1, trong khi ứng dụng dùng chung database, web service, URL tới CSS và JavaScript: đủ chỗ xung đột. Có thể trải một lần triển khai qua nhiều ngày cho hai bản cùng sống; nó đòi dev và vận hành hợp tác, "đó là lý do nó hiếm khi xảy ra". Chìa khoá: **chia thành các pha**, thêm cái mới sớm, xoá cái cũ và thêm ràng buộc sau (tr. 331).

**Mở rộng** (tr. 332–333). File tĩnh mỗi bản một URL (`/static/1.2/styles.css`); web service mỗi bản một endpoint; giao thức socket mang mã phiên bản, bên nhận nâng cấp trước. Database là nơi xung đột nhiều và khó nhất:

> [!quote] Release It! — Ch.18 (tr. 333)
> "Any columns that will eventually be NOT NULL are added as nullable, because the old version doesn’t know how to fill these in."
>
> *Cột nào rốt cuộc sẽ là NOT NULL thì được thêm vào dạng cho phép null, vì bản cũ không biết điền chúng.*

Ràng buộc tham chiếu cũng để sau. **Trigger bắc cầu** điền cấu trúc mới từ dữ liệu bản cũ ghi, và ngược lại. Điều kiện: INSERT, UPDATE ghi rõ cột, tránh `SELECT *`; thay mọi `SELECT *` ngay trước release thì "sẽ không được đón nhận vui vẻ" (tr. 333).

**Rollout** (tr. 333–334): vài giờ tới vài ngày, có thể để vài server "ủ" trên code mới; hết áp lực thời gian thì tắt bật máy tử tế được (mục 14.3, xem [Bài 3 — Thiết kế tổng quát](bai_03_thiet_ke_tong_quat.md)). **Dọn dẹp** (tr. 334): gỡ trigger, xoá đồ cũ, rồi mới thêm NOT NULL và ràng buộc. Hình 18.4 (tr. 335) là danh sách gạch đầu dòng; khoá xếp lại thành ba cột:

```
MỞ RỘNG                     ROLLOUT (từng server)      DỌN DẸP
file tĩnh mới               giải nén code              gỡ trigger bắc cầu
service pool mới nếu cần    ngừng nhận request mới     gỡ ràng buộc tham chiếu cũ
thêm bảng, thêm cột         tắt server                 xoá cột, bảng cũ
chạy migration dữ liệu      trỏ sang code mới          thêm ràng buộc tham chiếu mới
thêm trigger bắc cầu        bật server                 thêm NOT NULL
"ZDD đệ quy" cho cụm phụ    kiểm khởi động sạch        xoá file tĩnh cũ, code cũ
                                                       gỡ service pool cũ
(dòng khoá thêm) suốt ba pha: N và N+1 cùng sống; sau dọn dẹp chỉ còn N+1
```

## 16. Khép lại khoá học: từ feature complete tới production ready

Tóm tắt chương 18 chỉ bốn câu, và chúng khép cả cuốn sách:

> [!quote] Release It! — Ch.18 (tr. 334)
> "Change is the defining characteristic of software. That change—that adaptation—begins with release. Release is the beginning of the software’s true life; everything before that release is gestation. Either systems grow over time—adapting to their changing environment—or they decay until their costs outweigh their benefits and then die."
>
> *Thay đổi là đặc tính định nghĩa của phần mềm. Thay đổi ấy, sự thích nghi ấy, bắt đầu từ release. Release là khởi đầu cuộc đời thật của phần mềm; mọi thứ trước đó chỉ là thai nghén. Hoặc hệ thống lớn lên theo thời gian, thích nghi với môi trường đổi thay, hoặc nó mục dần cho tới khi chi phí vượt lợi ích, rồi chết.*

Đặt cạnh câu mà [Bài 0 — Nhập môn](bai_00_nhap_mon.md) đã trích từ Preface:

> [!quote] Release It! — Preface (tr. 11)
> "Second, realize that “Release 1.0” is not the end of the development project but the beginning of the system’s life on its own."
>
> *Thứ hai, hãy hiểu rằng "Release 1.0" không phải là lúc dự án phát triển kết thúc, mà là lúc hệ thống bắt đầu cuộc đời tự lập của nó.*

Sách mở và đóng bằng cùng một ý. Câu hỏi của Bài 0, "feature complete có phải production ready không?", giờ trả lời được đầy đủ. Phần dưới là **tổng kết của khoá**, không phải lời Nygard:

- **Feature complete** trả lời "hệ thống làm được gì". Đó là đích của *dự án*.
- **Production ready** trả lời thêm bốn câu: nó có *sống sót* được không (Bài 1: một exception không bắt ở `Statement.close()` làm cạn connection pool và cả hãng bay nằm đất, tr. 32–34); nó có *chịu được tải thật* không (Bài 2: site mới sập sau khoảng ba mươi phút ra mắt, khi số session lên 250.000, tr. 148); nó có *hợp với trung tâm dữ liệu và người vận hành* không (Bài 3); và người ta có *nhìn thấy và thay đổi* được nó không (Bài 4).

Bài 0 nêu lời khuyên đừng né chi phí phát triển một lần để gánh chi phí vận hành lặp lại (Ch.1, tr. 18). Bài 4 cho thấy khoản chi ấy cụ thể: một script đổi pool trong năm phút, một dòng log nói rõ ai phải làm gì, một cột thêm dạng nullable trước khi thêm ràng buộc. Vì hệ thống chỉ vừa khít hơn nhờ hành động có chủ đích (tr. 310), production ready không phải trạng thái đạt một lần vào ngày release, mà là năng lực **tiếp tục nhìn thấy và tiếp tục thay đổi** hệ thống suốt đời sống của nó.

## 17. Đối chiếu 2026

> [!warning] Đối chiếu 2026
> **Phần còn sống.**
> - *Minh bạch nay gọi là observability.* OpenTelemetry tự mô tả là khung và bộ công cụ observability để sinh, xuất, thu telemetry như **traces, metrics, logs** (tín hiệu hiện hỗ trợ còn có baggage; profiles đang phát triển). Nó là dự án CNCF, trung lập nhà cung cấp, và **không phải backend**: lưu trữ, hiển thị giao cho Jaeger, Prometheus hay hàng thương mại. Đó chính là "bộ xương ngoài" và "thiết kế theo chuẩn" (tr. 275, 289), với OpenTelemetry thay chỗ SNMP, CIM, JMX.
> - *ID giao dịch (tr. 283) nay là chuẩn.* W3C Trace Context (Recommendation, 23/11/2021) định nghĩa header `traceparent`, `tracestate`; khi thêm autoinstrumentation hoặc kích hoạt SDK, OpenTelemetry tự gắn TraceId, SpanId vào log, và coi log có cấu trúc là lựa chọn ưu tiên ở production.
> - *Bài học sáng Black Friday thành quy tắc.* Sách *Site Reliability Engineering* của Google định nghĩa giám sát hộp trắng, hộp đen; dặn theo dõi riêng độ trễ của request lỗi vì "một lỗi chậm còn tệ hơn lỗi nhanh"; cảnh báo trung bình che đuôi phân bố; và yêu cầu mỗi lần page phải hành động được.
> - *Release thường xuyên.* DORA: "DORA's research has repeatedly demonstrated that speed and stability are not tradeoffs." (Bài 0, mục 9 đã dẫn ý này; ở đây là để nối với năm chỉ số ở phần dưới.)
>
> **Phần cần chỉnh.**
> - *Tên gọi mới cho kỹ thuật của Nygard.* Ba pha mở rộng, rollout, dọn dẹp nay là **expand and contract** (parallel change; Danilo Sato, 2014). Mẹo "pool max = 0" (tr. 262) là một **Ops Toggle** trong phân loại feature toggle của Pete Hodgson (2017), người cũng cảnh báo toggle là hàng tồn kho có chi phí, phải chủ động gỡ. "Để vài server ủ" nay là **canary release** (Sato, 2014) hoặc **blue-green** (Fowler, 2010: hai môi trường production, chuyển router giữa chúng, đổi database trước ứng dụng).
> - *OpsDB tự dựng* nay thường nhường cho backend observability. Ý cốt lõi, gắn số đo kỹ thuật với tính năng nghiệp vụ, vẫn nguyên giá trị.
> - *Đo release.* Nygard đo bằng số người và giờ downtime; DORA dùng năm chỉ số: change lead time, deployment frequency, failed deployment recovery time (thông lượng), change fail rate, deployment rework rate (bất ổn).
>
> **Phần đã lỗi thời.** ATG Dynamo, SiteScope, HP OpenView, WebLogic 9.2, cvs/svn, máy nhắn tin. Các dự đoán thị trường của Ch.17 (CIM, EAM) khoá không đánh giá vì thiếu nguồn chắc; chính Nygard dặn nhiều công ty ông nêu có lẽ sẽ bị mua lại (tr. 267).

## 18. Áp dụng vào việc của bạn

> [!question] Khi thiết kế và viết code
> 1. **Rà năm dòng log ERROR.** Dòng nào không đòi vận hành hành động thì hạ mức. Dòng nào giữ lại: có mã thông điệp, trace ID, và nói rõ *ai* phải làm gì chưa (bài học "Reset required", tr. 282)?
> 2. **Thêm một công tắc vận hành.** Tính năng phụ gọi xuống hệ thống chậm nhất có tắt được lúc đang chạy, không deploy, với lời nhắn lịch sự không? Nếu phải sửa config rồi restart, bạn đang ở phía "sáu giờ" chứ không phải "năm phút" (tr. 263).
> 3. **Tách migration kế tiếp thành ba pha.** Ghi ra: mở rộng thêm gì (cột nullable, bảng, trigger), rollout kiểm gì, dọn dẹp mới thêm NOT NULL và ràng buộc nào (tr. 332–334).

> [!question] Khi vận hành, trực on-call, viết postmortem
> 1. **Đếm báo động giả.** Bao nhiêu phần trăm page tháng trước không cần hành động? Mỗi cái đang huấn luyện người trực phớt lờ đúng loại cảnh báo đó (tr. 261, 304).
> 2. **Kiểm "trung bình nói dối".** Biểu đồ độ trễ có tính request timeout và request lỗi không, hay chỉ request đã xong (tr. 258)?
> 3. **Dò huyền thoại trong run book.** Chọn một bước "thấy X thì làm Y". Ai chứng minh Y chữa X, hay chỉ là liên hệ thời gian như vụ Sybase (tr. 283)?
> 4. **Thêm hai câu vào mẫu postmortem.** "Ta *nhìn thấy* nguyên nhân bằng công cụ nào, mất bao lâu? Ta *thay đổi* hệ thống bằng thao tác gì, nó đã có script chưa?"

## 19. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **ROC** | Recovery-Oriented Computing: hỏng là tất yếu; khởi động lại mức thành phần (tr. 263–264). |
| **Minh bạch** | Hiểu được lịch sử, hiện trạng, trạng thái tức thời, dự báo của hệ thống (tr. 265). |
| **Nominal** | Trong ngưỡng; ngón tay cái: trung bình ± hai độ lệch chuẩn (tr. 271). |
| **Hộp trắng / hộp đen** | Quan sát từ bên trong, tích hợp lúc phát triển / từ bên ngoài, gắn sau được (tr. 276). |
| **Mã thông điệp** | Mã duy nhất cho mỗi thông điệp log, tra được trong run book (tr. 278–279). |
| **OpsDB, Expectation** | Cơ sở dữ liệu vận hành / khoảng hay trạng thái cho phép, vi phạm thì cảnh báo (tr. 299–304). |
| **Báo động giả** | Cảnh báo không ứng với sự cố thật; lặp đủ nhiều sẽ dạy người ta phớt lờ (tr. 261, 304). |
| **O-O-D-A** | Quan sát, định hướng, quyết định, hành động (John Boyd) (tr. 306). |
| **Năng lượng hoạt hoá** | Tổng chi phí thực hiện một thay đổi, gồm cả chi phí release (tr. 311). |
| **Cung điện pha lê** | Cụm đối tượng khớp chặt lan tới biên ứng dụng, không đổi được gì (tr. 315). |
| **Database tích hợp** | Nhiều hệ thống đọc ghi chung một database; "đừng làm!" (tr. 326). |
| **Trigger bắc cầu** | Điền cấu trúc mới từ dữ liệu cũ và ngược lại khi hai bản cùng chạy (tr. 333). |
| **OpenTelemetry, expand and contract, canary, Ops Toggle, DORA** | Không có trong sách; tên 2026, xem mục 17. |

## 20. Câu hỏi tự kiểm tra

1. Vì sao CPU mọi tầng *thấp* trong khi trang sập? Chuỗi 3.000 / 450 / 25 nghĩa là gì? *(tr. 258–261)*
2. Vì sao đặt `max` về 0 lúc đầu không có tác dụng, và vì sao sau đó người tài trợ muốn hạ về 1 chứ không phải 0? *(tr. 262–263)*
3. Phân biệt hiện trạng và hành vi tức thời. Người tài trợ thường cần cái nào? *(tr. 270, 274)*
4. Theo hình 17.1, circuit breaker cắt một tính năng phụ làm dashboard màu gì? "Đang nhận request" bằng false thì sao? *(tr. 273)*
5. Nêu ba lỗi thiết kế log trong chuyện "Reset required". *(tr. 282–283)*
6. Năng lượng hoạt hoá của một thay đổi gồm những phần nào; phần nào ít được hiểu nhất? *(tr. 311)*
7. Vì sao dư thừa lại khiến release cần downtime? Việc nào chỉ được làm ở pha dọn dẹp? *(tr. 331–334)*
8. Trả lời lại câu hỏi của Bài 0 bằng ba ví dụ từ bài này. *(tr. 10, 310, 334)*

## Tóm tắt một trang

```
BÀI 4 — VẬN HÀNH: NHÌN THẤY HỆ THỐNG VÀ ĐỂ NÓ THAY ĐỔI MÀ KHÔNG ĐAU
───────────────────────────────────────────────────────────────────
BLACK FRIDAY (tr. 252–264)
  Quảng cáo miễn phí giao hàng → 3.000 luồng → 450 → 25 request.
  Pool KHÔNG timeout; CPU thấp; "trung bình" chỉ tính request đã xong.
  Báo động giả dạy người trực phớt lờ CPU 100%.
  Cứu: pool max=0 + stop/start thành phần bằng script → <5 phút (vs >6 giờ).
  ROC: hỏng là tất yếu; khởi động lại MỨC THÀNH PHẦN.

MINH BẠCH (Ch.17)
  4 góc nhìn: LỊCH SỬ · DỰ BÁO · HIỆN TRẠNG · TỨC THỜI
  Nominal ≈ trung bình ± 2 độ lệch chuẩn theo "giờ trong tuần".
  Giám sát là BỘ XƯƠNG NGOÀI; chính sách để ngoài app.
  Log = giao diện người-máy: ERROR đòi hành động; mã; ID giao dịch.
  Giám sát chỉ nói điều hệ thống NGHĨ. Phơi ra MỌI THỨ.
  OpsDB + kỳ vọng khớp thực tế. Không vòng phản hồi → dữ liệu vô dụng.

THÍCH NGHI (Ch.18)
  Ra mắt = ra đời. Form follows failure. 40–90% chi phí SAU 1.0.
  Khớp lỏng; tránh cung điện pha lê; bảng phiên bản schema + Fail Fast.
  Hệ sinh thái; cụm lỏng; phiên bản giao thức; DB TÍCH HỢP: ĐỪNG.
  Release nhẹ như cắt tóc. Với người dùng, sập là sập.
  Không downtime: MỞ RỘNG → ROLLOUT → DỌN DẸP.

KHÉP KHOÁ  Production ready = sống sót (B1) + chịu tải (B2)
           + hợp trung tâm dữ liệu (B3) + NHÌN THẤY, THAY ĐỔI được (B4).
2026       OpenTelemetry · Trace Context · expand/contract · Ops Toggle · DORA
```

## Nguồn

- **Michael T. Nygard**, *Release It! Design and Deploy Production-Ready Software* (Pragmatic Bookshelf, 2007), `tai_lieu/Release It! Design and Deploy Production-Ready Software.pdf`:
  - **Part IV — Operations** (`tr. 251`).
  - **Ch.16 Case Study** (`tr. 252–264`), **Ch.17 Transparency** (`tr. 265–309`), **Ch.18 Adaptation** (`tr. 310–335`); trang từng mục con ghi ngay trong thân bài.
  - **Preface** (`tr. 11`) và **Ch.1** (`tr. 18`), trích lại ở mục 16.
  - Quy ước trích: `tr. X` = số trang in = số trang PDF.
- Nguồn web dùng ở Đối chiếu 2026 (truy cập 9/2026):
  - OpenTelemetry, "What is OpenTelemetry?": https://opentelemetry.io/docs/what-is-opentelemetry/
  - OpenTelemetry, "Signals": https://opentelemetry.io/docs/concepts/signals/
  - OpenTelemetry, "Logs": https://opentelemetry.io/docs/concepts/signals/logs/
  - W3C, "Trace Context": https://www.w3.org/TR/trace-context/
  - Google, *Site Reliability Engineering*, Ch.6 "Monitoring Distributed Systems": https://sre.google/sre-book/monitoring-distributed-systems/
  - Danilo Sato, "ParallelChange" (2014): https://martinfowler.com/bliki/ParallelChange.html
  - Martin Fowler, "BlueGreenDeployment" (2010): https://martinfowler.com/bliki/BlueGreenDeployment.html
  - Danilo Sato, "CanaryRelease" (2014): https://martinfowler.com/bliki/CanaryRelease.html
  - Pete Hodgson, "Feature Toggles (aka Feature Flags)" (2017): https://martinfowler.com/articles/feature-toggles.html
  - DORA, "DORA's software delivery performance metrics": https://dora.dev/guides/dora-metrics/

---

**Bản đồ khoá học:** [Bài 0 — Nhập môn](bai_00_nhap_mon.md) · [Bài 1 — Ổn định](bai_01_on_dinh.md) · [Bài 2 — Công suất](bai_02_cong_suat.md) · [Bài 3 — Thiết kế tổng quát](bai_03_thiet_ke_tong_quat.md) · [Bài 4 ← bạn đang ở đây]

Xem thêm [README khoá học](../README.md).
