# Bài 10 — Ước lượng: một lời đoán, không phải một lời hứa

> [!info] Về bài này
> Dựng từ **Chương 10 — Estimation** của *The Clean Coder* (Robert C. Martin, `tai_lieu/`, `tr. 135–148`).
> Trích theo `Ch. N` và `tr. X` (số trang in sách; PDF = X + 33). Câu chốt để **nguyên văn tiếng Anh** trong `[!quote]`, dịch gọn ngay dưới. Công thức PERT để trong khối mã (không phải trích nguyên văn).
> Cần đọc trước: [Bài 3 — Nói Có](bai_03_noi_co.md) (ngôn ngữ cam kết), [Bài 4 — Viết code](bai_04_viet_code.md) (ba mốc best/nominal/worst).

## Mục lục

1. [Mở đầu: 32 con chip, lời hứa một tháng, và đêm Giáng sinh say khướt](#1-mở-đầu-32-con-chip-lời-hứa-một-tháng-và-đêm-giáng-sinh-say-khướt)
2. [Estimate ≠ commitment: khác nhau tận gốc](#2-estimate--commitment-khác-nhau-tận-gốc)
3. [Ca 1 — "Ba ngày": ước lượng là một phân phối xác suất](#3-ca-1--ba-ngày-ước-lượng-là-một-phân-phối-xác-suất)
4. [PERT: ba con số biến lời đoán thành phân phối](#4-pert-ba-con-số-biến-lời-đoán-thành-phân-phối)
5. [Ước lượng cùng đội: wideband delphi](#5-ước-lượng-cùng-đội-wideband-delphi)
6. [Luật số lớn](#6-luật-số-lớn)
7. [Đối chiếu 2026](#7-đối-chiếu-2026)
8. [Áp dụng vào việc của bạn](#8-áp-dụng-vào-việc-của-bạn)
9. [Từ điển thuật ngữ](#9-từ-điển-thuật-ngữ)
10. [Câu hỏi tự kiểm tra](#10-câu-hỏi-tự-kiểm-tra)
11. [Tóm tắt một trang](#tóm-tắt-một-trang)
12. [Nguồn](#nguồn)

---

## 1. Mở đầu: 32 con chip, lời hứa một tháng, và đêm Giáng sinh say khướt

Năm 1978, Uncle Bob (26 tuổi) làm lead cho một chương trình nhúng 32K viết bằng assembly Z-80, nạp lên **32 con chip EEprom** cắm trên ba bo mạch. Có hàng trăm thiết bị lắp ở tổng đài điện thoại khắp nước Mỹ; mỗi bận sửa một con bug hay thêm một tính năng là kỹ thuật viên hiện trường phải chạy tới từng máy **thay cả 32 con chip** — chân chip thì dễ cong gãy, mối hàn thì dễ hỏng, chi phí đội lên khủng khiếp. Sếp Ken Finder nhờ anh gỡ: làm sao đổi được *một* con chip mà khỏi phải đụng tới cả 32.

Cái khó là: phần mềm vốn là một khối liên kết duy nhất — thêm một dòng code thôi là mọi địa chỉ phía sau xô nhau đổi, kéo theo gần như mọi con chip cũng đổi. Lời giải của Bob: **tách mỗi con chip thành một đơn vị biên dịch độc lập**; đầu mỗi chip đặt một bảng con trỏ tới các hàm, lúc khởi động thì chép vào RAM, và mọi lời gọi hàm đều đi *qua vector RAM* chứ không gọi thẳng. (Ngẫm lại thì: mỗi con chip chính là một *object* có *vtable*, còn hàm thì được *gọi đa hình* — anh học nguyên lý thiết kế hướng đối tượng ngay từ đây, trước cả khi biết "object" nghĩa là gì, và đây cũng là gốc của cái bài học *independent deployability* mà anh giảng suốt cả đời.)

Anh ước lượng việc này **mất chừng một tháng**. Rốt cuộc nó **mất ba tháng**. Tại tiệc Giáng sinh Teradyne năm 1978, một trận bão tuyết chặn cả ban nhạc lẫn người phục vụ không tới được, nhưng "rượu thì thừa mứa". Bob — một trong hai lần say duy nhất đời — ngồi bệt xuống sàn cạnh Ken (sếp, 29 tuổi, tỉnh táo) mà **khóc** vì việc kéo dài quá lâu, men rượu đã cởi trói cho mọi nỗi lo âu bấy lâu về cái ước lượng của anh. Anh hỏi Ken có giận mình không:

> [!quote] The Clean Coder — Ch.10 (tr. 137)
> "Yes, I think it's taken you a long time, but I can see that you are working hard on it, and making good progress. It's something we really need. So, no, I'm not mad."
>
> *Ừ, tôi thấy cậu làm lâu thật, nhưng tôi thấy cậu làm rất chăm và tiến triển tốt. Với lại đây là thứ ta thật sự cần. Nên, không, tôi không giận.*

Câu đáp đó Uncle Bob nhớ mãi mấy chục năm — vì Ken đã tách bạch được **ước lượng trượt** với **thất bại đạo đức**. Và đó cũng là luận đề của cả chương.

## 2. Estimate ≠ commitment: khác nhau tận gốc

Cả cái sự ngờ vực giữa nghiệp vụ và lập trình viên bắt nguồn từ một hiểu lầm: **nghiệp vụ coi ước lượng là cam kết; còn lập trình viên coi ước lượng là lời đoán.**

- **Cam kết (commitment)** là thứ bạn *phải* đạt. Người chuyên nghiệp **không cam kết trừ khi chắc chắn làm được** — bị đòi cam kết một điều mình không chắc thì họ có bổn phận từ chối:

> [!quote] The Clean Coder — Ch.10 (tr. 138)
> "Missing a commitment is an act of dishonesty only slightly less onerous than an overt lie."
>
> *Lỡ một cam kết là một hành vi thiếu trung thực, chỉ nhẹ hơn một lời nói dối trắng trợn có chút xíu.*

- **Ước lượng (estimate)** thì chỉ là một *lời đoán* — không hàm ý cam kết, không hứa hẹn gì, mà lỡ nó thì cũng *chẳng* có gì đáng hổ thẹn:

> [!quote] The Clean Coder — Ch.10 (tr. 138)
> "An estimate is a guess. No commitment is implied. No promise is made. Missing an estimate is not in any way dishonorable."
>
> *Ước lượng chỉ là một lời đoán. Không hàm ý cam kết. Chẳng lời hứa nào. Lỡ một ước lượng thì **chẳng có gì đáng hổ thẹn cả**.*

## 3. Ca 1 — "Ba ngày": ước lượng là một phân phối xác suất

**Chuyện gì đã xảy ra.** Vì sao lập trình viên ước lượng dở? Không phải vì thiếu bí kíp gì, mà vì hiểu sai *bản chất* của ước lượng:

> [!quote] The Clean Coder — Ch.10 (tr. 138)
> "An estimate is not a number. An estimate is a distribution."
>
> *Ước lượng **không phải một con số**. Ước lượng là một **phân phối**.*

Uncle Bob minh hoạ: Mike hỏi Peter ước lượng cho task Frazzle, Peter đáp gọn "Ba ngày". Nhưng Peter có *thật sự* xong trong ba ngày không? Có thể — mà khả năng bao nhiêu thì *chẳng ai biết*, vì Peter đã nói ba ngày *chắc* tới đâu so với bốn hay năm ngày đâu. Đến lúc Mike hỏi sâu, sự thật mới lộ dần: Peter thấy 50–60% khả năng xong trong 3 ngày, 95% chắc là xong trước 6 ngày, còn nếu *mọi thứ* trục trặc thì có khi lên 10–11 ngày. "Ba ngày" hoá ra chỉ là **cái cột cao nhất** trên biểu đồ — tức thời lượng *khả dĩ nhất*, chứ không phải điều *chắc chắn*. Còn Mike thì nơm nớp lo cái **đuôi bên phải** của phân phối (11 ngày).

**Điều rút ra.** Chỗ nguy hiểm nằm ở **cam kết ngầm**. Khi Mike xin "cậu *cố* trong 6 ngày nhé", thì chữ "cố" (đã mổ ở [Bài 2](bai_02_noi_khong.md)) đã biến ước lượng thành một cam kết:

> [!quote] The Clean Coder — Ch.10 (tr. 140)
> "Agreeing to try is agreeing to succeed."
>
> *Đồng ý "cố" là đồng ý **sẽ thành công**.*

Người chuyên nghiệp thì vạch ranh giới cho rõ giữa ước lượng và cam kết, cẩn thận không để lọt cam kết ngầm nào, và **truyền đạt cái phân phối xác suất** của ước lượng cho rõ nhất có thể, để cấp quản lý còn lập kế hoạch cho đúng.

## 4. PERT: ba con số biến lời đoán thành phân phối

**Chuyện gì đã xảy ra.** Năm 1957, kỹ thuật **PERT** (Program Evaluation and Review Technique) ra đời phục vụ dự án tàu ngầm Polaris của Hải quân Mỹ. Nó cho một cách đơn giản để biến ước lượng thành một phân phối xác suất dùng được — gọi là **phân tích ba biến** (trivariate): với mỗi task, đưa ra *ba* con số:

- **O — lạc quan:** chỉ đạt được nếu *mọi thứ* đều trơn tru (xác suất < 1%).
- **N — bình thường:** khả dĩ nhất (cái cột cao nhất trên biểu đồ).
- **P — bi quan:** loại trừ mọi thứ, chỉ chừa lại thảm hoạ (xác suất < 1%).

Từ ba số đó, tính ra thời lượng kỳ vọng μ và độ lệch chuẩn σ (thước đo độ bất định):

```
μ (kỳ vọng)        = (O + 4N + P) / 6
σ (bất định task)  = (P − O) / 6

Ví dụ Peter: O=1, N=3, P=12  →  μ = (1 + 12 + 12)/6 ≈ 4,2 ngày
                                 σ = (12 − 1)/6      ≈ 1,8 ngày

Chuỗi nhiều task nối tiếp:
  μ_chuỗi = Σ μ_task                    (cộng thẳng)
  σ_chuỗi = √( Σ σ_task² )              (căn tổng bình phương)

Ba task (4,2/1,8 · 3,5/2,2 · 6,5/1,3):
  μ_chuỗi = 4,2 + 3,5 + 6,5            = 14 ngày (khả dĩ)
  σ_chuỗi = √(1,8² + 2,2² + 1,3²) ≈ 3  → 17 ngày (1σ), 20 ngày (2σ)
```

**Điều rút ra.** Hãy thử cảm cái **áp lực** phải làm xong ba task "trong 5 ngày" (best-case là 1+1+3), trong khi ngay cả nominal cộng lại đã 10 ngày — mà con số thực tế lại là 14, có khi vọt tới 17 hay 20. Sự bất định của từng task **cộng dồn** lại theo cách *thêm phần hiện thực* vào kế hoạch. Ai làm nghề vài năm cũng từng thấy những dự án ước lượng lạc quan rồi kéo dài gấp 3–5 lần; PERT là một cách hợp lý để chặn bớt cái kỳ vọng lạc quan đó.

## 5. Ước lượng cùng đội: wideband delphi

Sai lầm của Mike và Peter là: Mike chỉ đi hỏi *mỗi mình* Peter. Mà nguồn lực ước lượng quý nhất lại là **những người quanh bạn** — họ thấy những thứ bạn không thấy. Barry Boehm (thập niên 1970) đưa ra **wideband delphi**: cả nhóm cùng bàn, cùng ước lượng, lặp đi lặp lại tới khi *đồng thuận*. Uncle Bob chuộng mấy biến thể nhẹ nhàng:

- **Flying Fingers (giơ ngón tay).** Bàn từng task một, rồi mọi người giấu tay dưới bàn, giơ 0–5 ngón theo ước lượng của mình; đếm 1-2-3 là cùng xoè ra. Gần nhau là coi như đủ đồng thuận; lệch nhiều thì bàn tiếp. Chuyện *cùng giơ một lúc* rất quan trọng — để không ai kịp đổi ước lượng theo người khác.
- **Planning Poker.** James Grenning (2002) — biến thể phổ biến tới mức có cả bộ bài lẫn website planningpoker.com. Mỗi người rút một lá úp mặt lại rồi cùng lật; y hệt flying fingers. Có người dùng dãy Fibonacci; Uncle Bob thì thấy 5 lá **0, 1, 3, 5, 10** là đủ.
- **Affinity Estimation.** (Lowell Lindstrom) Viết task lên thẻ, cả nhóm *im lặng* xếp thẻ trên bàn hay trên tường: việc lâu hơn thì đẩy sang phải, việc nhỏ hơn thì kéo sang trái; thẻ nào bị dịch qua dịch lại quá nhiều lần thì để riêng ra một bên để bàn. Xong rồi mới vạch các "xô" kích thước (thường là 5 xô Fibonacci: 1, 2, 3, 5, 8).

Mấy kỹ thuật này cho ra *một* con số nominal; muốn có đủ ba số PERT thì chỉ cần bảo cả đội giơ lá bi quan rồi lấy cao nhất, giơ lá lạc quan rồi lấy thấp nhất.

## 6. Luật số lớn

> [!quote] The Clean Coder — Ch.10 (tr. 147)
> "if you break up a large task into many smaller tasks and estimate them independently, the sum of the estimates of the small tasks will be more accurate than a single estimate of the larger task."
>
> *nếu bạn chẻ một task lớn ra thành nhiều task nhỏ rồi ước lượng độc lập, thì **tổng** ước lượng của mấy task nhỏ sẽ **chính xác hơn** một ước lượng đơn cho cả task lớn.*

Lý do là: sai số ở các task nhỏ có xu hướng *triệt tiêu lẫn nhau*. Nhưng Uncle Bob cũng nói thật thêm rằng điều này hơi lạc quan, bởi "**sai số ước lượng thường nghiêng về phía *dưới* mức chứ không phải trên mức**" (tr. 147) — nên triệt tiêu chẳng hoàn hảo được. Dù vậy, chẻ nhỏ vẫn là hay: một phần sai số *có* triệt tiêu thật, mà chẻ nhỏ còn giúp *hiểu* task hơn và lôi mấy bất ngờ ra sớm.

## 7. Đối chiếu 2026

> [!warning] Đối chiếu 2026 — lõi bất hủ, và một cuộc tranh cãi mới
> **Còn sống — cái lõi:** chỗ phân biệt *estimate ≠ commitment*, câu "ước lượng là một phân phối", việc truyền đạt độ bất định, và chuyện không để ước lượng biến thành cam kết — tất cả đều **đúng hơn theo năm tháng**, và làm nền cho *mọi* trường phái năm 2026. Planning poker cùng story point Fibonacci vẫn là thực hành phổ biến. Cái phản ứng nhân văn của Ken ("ước lượng trượt ≠ thất bại đạo đức") khớp hoàn hảo với văn hoá *blameless / psychological safety* của 2026.
> **Một sắc thái đã tinh chỉnh — PERT vs dự báo thực nghiệm:** PERT bắt bạn phải *đoán* O/N/P *trước*. Năm 2026 nhiều đội chuyển sang **dự báo thực nghiệm**: chạy **mô phỏng Monte Carlo** trên *dữ liệu lịch sử* (throughput, cycle time) để nói kiểu "85% khả năng xong trước ngày X" — thay vì ngồi đoán phân phối một cách tiên nghiệm. Vẫn cùng tinh thần "trả lời bằng xác suất chứ không bằng một con số", nhưng lấy từ *đo đạc* thay vì *phỏng đoán*.
> **Một cuộc tranh cãi lớn ông chưa nhắc — #NoEstimates:** khoảng 2012 trở đi (Woody Zuill, Vasco Duarte) nổi lên phong trào **#NoEstimates**, lập luận rằng nhiều hoạt động ước lượng thực ra là *lãng phí*; thay vào đó, hãy *chẻ việc cho thật nhỏ và đều*, rồi *đếm thông lượng* mà dự báo. Đây chính là "chương gây tranh cãi" của Ch.10, hệt vai trò của [Bài 5 (TDD)](bai_05_tdd.md): cái lõi (giao tiếp bằng xác suất, đừng hứa điều chưa chắc) thì sống khoẻ; còn *cách* nặn ra con số (PERT thủ công, hay Monte Carlo, hay không ước lượng gì cả) thì năm 2026 có nhiều trường phái đua nhau.

## 8. Áp dụng vào việc của bạn

> [!question] Nếu bạn là lập trình viên
> 1. **Đổi một con số thành một phân phối.** Task kế tiếp, đừng báo mỗi "3 ngày"; hãy đưa O/N/P rồi tính μ/σ theo công thức PERT ở trên. Con số μ ra có làm bạn (và cả sếp) bất ngờ so với cái "trực giác một con số" không?
> 2. **Chơi một ván planning poker.** Với một task còn mơ hồ, rủ cả đội ước lượng *cùng một lúc*. Chỗ *bất đồng* sẽ lôi ra giả định ẩn nào?
> 3. **So PERT với dữ liệu thật.** Nếu đội bạn có sẵn lịch sử throughput, thử dự báo bằng cách đếm (mỗi tuần xong bao nhiêu story) rồi đem so với ước lượng PERT. Cái nào khớp thực tế hơn?

> [!question] Suy rộng ra mọi nghề tri thức
> 1. **"Cố" = cam kết ngầm.** Nhớ một lần bạn nói "để tôi *cố* xong trước ngày X" trong nghề mình. Nó đã âm thầm biến một lời đoán thành một lời hứa ra sao?
> 2. **Người sếp như Ken.** Bạn (hoặc sếp bạn) có tách được *ước lượng trượt* ra khỏi *thất bại đạo đức* không? Khi làm được điều đó thì có gì thay đổi?

## 9. Từ điển thuật ngữ

| Thuật ngữ | Nghĩa trong khoá |
| --- | --- |
| **Estimate vs commitment** | Ước lượng = lời đoán (lỡ không đáng hổ thẹn); cam kết = phải đạt (lỡ ≈ nói dối) (tr. 138). |
| **"Estimate is a distribution"** | Ước lượng đúng nghĩa là một *phân phối xác suất*, không phải một con số (tr. 138). |
| **Cam kết ngầm** | "Cố xong trước X" biến ước lượng thành cam kết — tránh (tr. 140). |
| **PERT (O/N/P)** | Ba con số → μ=(O+4N+P)/6, σ=(P−O)/6; chuỗi cộng μ, căn-tổng-bình-phương σ (tr. 141–143). |
| **Wideband delphi** | Ước lượng đồng thuận cả đội: flying fingers, planning poker, affinity estimation (tr. 144–146). |
| **Luật số lớn** | Chia nhỏ + ước lượng độc lập → tổng chính xác hơn; nhưng sai số nghiêng về *dưới* mức (tr. 147). |
| **#NoEstimates / Monte Carlo** | (Khung 2026) dự báo bằng *dữ liệu throughput* thay vì đoán phân phối tiên nghiệm. |

## 10. Câu hỏi tự kiểm tra

1. Ken đã tách hai thứ gì ra khỏi nhau trong câu "no, I'm not mad"? *(tr. 137)*
2. Nghiệp vụ và lập trình viên nhìn "ước lượng" khác nhau thế nào, và vì sao khác biệt đó nguy hiểm? *(tr. 138)*
3. "Estimate is a distribution" nghĩa là gì? "Ba ngày" của Peter tương ứng phần nào của phân phối? *(tr. 138–139)*
4. Viết công thức μ và σ của PERT, và giải thích vì sao chuỗi task lại ra 14 ngày chứ không phải 10. *(tr. 141–143)*
5. Kể ba biến thể wideband delphi. Vì sao "giơ đồng thời" lại quan trọng? *(tr. 144–146)*
6. #NoEstimates và Monte Carlo (2026) giữ cái lõi nào của chương và thay cái gì?

## Tóm tắt một trang

```
BÀI 10 — ƯỚC LƯỢNG: MỘT LỜI ĐOÁN, KHÔNG PHẢI MỘT LỜI HỨA
────────────────────────────────────────────────────────
MỞ ĐẦU  1978, 32 chip: hứa 1 tháng → mất 3 tháng. Tiệc Giáng
        sinh, Bob khóc; Ken: "no, I'm not mad" (tr. 137) — tách
        ước-lượng-trượt khỏi thất-bại-đạo-đức.

LÕI  Nghiệp vụ coi ước lượng = cam kết; dev coi = lời đoán.
     Lỡ commitment ≈ nói dối (tr. 138). "An estimate is a guess…
     missing it is not dishonorable" (tr. 138).

CA 1  "Estimate is not a number. It's a distribution" (tr. 138).
     "Ba ngày" = cột cao nhất, không phải điều chắc. "Cố" = cam
     kết ngầm; "agreeing to try is agreeing to succeed" (tr.140).

PERT  O/N/P → μ=(O+4N+P)/6, σ=(P−O)/6. Chuỗi: Σμ, √Σσ². Ba task
     10 ngày nominal → 14 khả dĩ, 17 (1σ), 20 (2σ).

ĐỘI  wideband delphi: flying fingers · planning poker (0,1,3,5,10)
     · affinity. Giơ ĐỒNG THỜI.

LUẬT SỐ LỚN  chia nhỏ + ước lượng độc lập → tổng chính xác hơn;
     nhưng sai số nghiêng về DƯỚI mức (tr. 147).

2026  Lõi (xác suất, estimate≠commitment) = GIỮ. PERT thủ công →
      dự báo Monte Carlo từ dữ liệu. Tranh cãi mới: #NoEstimates.
```

## Nguồn

- **Robert C. Martin**, *The Clean Coder*, Ch.10 **Estimation** (`tr. 135–148`): ca 32 chip / vectorization và tiệc Giáng sinh 1978, "no, I'm not mad" (tr. 135–137); "What Is an Estimate?" — commitment vs estimate (tr. 138); ca Mike–Peter "ba ngày", phân phối xác suất, implied commitments (tr. 138–140); "PERT" — trivariate O/N/P, μ, σ, chuỗi task (tr. 141–143); "Estimating Tasks" / "Wideband Delphi" — flying fingers, planning poker, affinity (tr. 144–146); "The Law of Large Numbers" (tr. 147); Conclusion (tr. 147). `tai_lieu/The Clean Coder-A Code of Conduct for Professional Programmers.pdf`
- Bối cảnh 2026 (ngoài sách): #NoEstimates (Woody Zuill, Vasco Duarte), dự báo Monte Carlo từ throughput/cycle-time, blameless culture.
- Quy ước trích: `tr. X` = số trang in trong sách; trang tệp PDF = `X + 33`.

---

**Bản đồ khoá học:** [Bài 0 — Nhập môn](bai_00_nhap_mon.md) · [Bài 1 — Tính chuyên nghiệp](bai_01_tinh_chuyen_nghiep.md) · [Bài 2 — Nói Không](bai_02_noi_khong.md) · [Bài 3 — Nói Có](bai_03_noi_co.md) · [Bài 4 — Viết code](bai_04_viet_code.md) · [Bài 5 — Phát triển hướng kiểm thử (TDD)](bai_05_tdd.md) · [Bài 6 — Luyện tập](bai_06_luyen_tap.md) · [Bài 7 — Kiểm thử chấp nhận](bai_07_acceptance_testing.md) · [Bài 8 — Chiến lược kiểm thử](bai_08_chien_luoc_kiem_thu.md) · [Bài 9 — Quản lý thời gian](bai_09_quan_ly_thoi_gian.md) · [Bài 10 ← bạn đang ở đây] · [Bài 11 — Áp lực](bai_11_ap_luc.md) · [Bài 12 — Cộng tác](bai_12_cong_tac.md) · [Bài 13 — Đội và dự án](bai_13_doi_va_du_an.md) · [Bài 14 — Dẫn dắt, học nghề & nghề thủ công](bai_14_dan_dat_hoc_nghe.md)

Xem thêm [README khoá học](../README.md).
