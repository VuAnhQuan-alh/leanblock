# Bài 1 — Lí thuyết phản thân

> [!info] Định hướng
> Dựa **Phần I, Chương 1** của *Giả kim thuật Tài chính*. Bài này đặt tên chính xác cho vòng
> lặp đã gặp ở Bài 0, viết nó ra thành hai hàm, và giải thích vì sao thị trường **không** về
> cân bằng như sách giáo khoa hứa.
> **Cần đọc trước:** [Bài 0 — Nhập môn](bai_00_nhap_mon.md).

## Nhắc lại chỗ đứng

Ở Bài 0 ta thấy: người tham gia thị trường vừa **quan sát** vừa **tác động** lên cái họ quan
sát. Soros gọi tình thế đó là **phản thân** (*reflexivity*) — mượn cách người Pháp gọi động
từ mà chủ ngữ và tân ngữ là một (kiểu "tự soi mình"). Bài này biến trực giác đó thành một bộ
khung ta dùng được suốt khoá.

## Hai vai của tư duy: hiểu và làm

Soros tách mối quan hệ giữa người tham gia và tình thế thành **hai hàm** chạy ngược chiều:

- **Hàm nhận thức** (*cognitive function*): tình thế tác động lên **nhận thức** của người
  tham gia. Đầu vào là thế giới, đầu ra là ý nghĩ trong đầu. (Bạn *hiểu* thị trường.)
- **Hàm tham dự** (*participating function*): nhận thức của người tham gia tác động lên
  **tình thế**. Đầu vào là ý nghĩ, đầu ra là thế giới bị đổi. (Bạn *làm* thị trường đổi.)

Gọi tình thế là `x`, nhận thức là `y`, viết gọn:

```
y = f(x)     hàm nhận thức   — nhận thức phụ thuộc tình thế
x = φ(y)     hàm tham dự      — tình thế phụ thuộc nhận thức
```

Điểm chết người nằm ở chỗ **cả hai chạy cùng lúc**. Đầu ra của hàm này là đầu vào của hàm
kia, nên thay vì một kết quả đứng yên, ta được một cặp **đệ quy** cắn đuôi nhau:

```
y = f(φ(y))
x = φ(f(x))
```

> [!quote] Bản gốc, tr. 43
> Soros viết đúng cặp phương trình này và gọi nó là "nền tảng lí thuyết của cách tiếp cận
> của tôi" — *"Hai hàm đệ quy này không tạo ra một cân bằng mà tạo ra một quá trình biến
> đổi không ngừng."*

Đọc dòng in đậm đó hai lần. Trong toán, một hàm cần biến độc lập để cho ra kết quả xác định.
Nhưng ở đây biến "độc lập" của hàm này lại là kết quả "phụ thuộc" của hàm kia — **không có
điểm tựa cố định nào**. Hệ không hội tụ về một số; nó chạy mãi.

## Vì sao thị trường không về cân bằng

Lý thuyết cân bằng cổ điển đứng được là nhờ **lặng lẽ vứt bỏ hàm nhận thức** — nó giả định
người tham gia có **tri thức hoàn hảo**, tức nhận thức luôn khớp thực tại, nên chỉ còn hàm
tham dự (đường cung–cầu) hoạt động. Bỏ hàm nhận thức đi thì đường cung–cầu đứng yên như dữ
liệu cho sẵn, và quả bóng lăn về đáy bát.

Soros bảo: hàm nhận thức có thật và nó **động**. Khi nhận thức của người tham gia thay đổi,
nó làm dịch chuyển luôn đường cung–cầu (vì quyết định mua–bán dựa trên kì vọng, mà kì vọng
là nhận thức). Đáy bát bị dời mỗi khi quả bóng lăn. Mục tiêu mà quá trình điều chỉnh hướng
tới **tự di chuyển** — nên cân bằng là cái đích không bao giờ tới.

> [!tip] Một câu để nhớ
> Kinh tế học cổ điển sống được vì nó **giả vờ hàm nhận thức không tồn tại**. Bỏ giả vờ đó
> đi, cân bằng sụp theo.

## Không phải lúc nào cũng "phản thân"

Đây là chỗ dễ hiểu sai, và chính Soros về sau tự đính chính.

> [!warning] Soros nói quá, và tự nhận
> Trong lần tái bản 1994, Soros thừa nhận bản 1987 trình bày phản thân **như thể lúc nào cũng
> đúng**. Thật ra phần lớn thời gian nó yếu tới mức bỏ qua được. Ông phân biệt:
> - **Gần-cân bằng** (*near-equilibrium*): các cơ chế hiệu chỉnh giữ nhận thức và thực tế
>   không lệch nhau quá xa → dùng lý thuyết cổ điển cũng tạm ổn, lệch coi như "nhiễu".
> - **Xa-cân bằng** (*far-from-equilibrium*): vòng phản hồi kép hoạt động mạnh, nhận thức và
>   thực tế cuốn nhau đi một chiều **không đảo ngược được** → đây mới là lúc phản thân quan
>   trọng, và là lúc bong bóng/sụp đổ sinh ra.
>
> Nói cách khác: phản thân là **hiện tượng từng lúc, từng hồi**, không phải trạng thái
> thường trực. Nghề của nhà đầu tư là nhận ra *khi nào* thị trường bước vào vùng xa-cân bằng.

## "Lí thuyết dây giày": không phải cân bằng, mà là lịch sử

Vì hệ chạy mãi không dừng, Soros bảo diễn biến thị trường giống một **quá trình lịch sử** hơn
là một bài toán cân bằng — mỗi bước nặn ra bước sau, không lặp lại. Ông gọi vui là lí thuyết
**"dây giày"** (*bootstrap*): thực tại tự kéo mình lên bằng chính dây giày của nó, qua trung
gian là nhận thức của người tham gia. Ông cũng nhận đây là một dạng **biện chứng** — tổng
hợp giữa biện chứng ý tưởng (Hegel) và biện chứng vật chất (Marx), nhưng cố tránh dùng chữ
"biện chứng" vì gánh nặng đi kèm.

> [!example] Vòng lặp trong một câu chuyện thật rút gọn
> Cuối thập niên 1970, ngân hàng quốc tế cho các nước đang phát triển vay ồ ạt, đo sức khoẻ
> con nợ bằng "tỉ số nợ". Nhưng chính việc cho vay làm các tỉ số đó **đẹp lên** (tiền vào,
> kinh tế tạm khởi sắc) → thấy con nợ khoẻ → cho vay thêm → tỉ số lại đẹp. Nhận thức "nước
> này trả được nợ" tự làm mình thành thật... cho tới khi ngân hàng đòi tiền và vòng lặp quay
> ngược thành khủng hoảng nợ 1982. Ta sẽ mổ case này ở Bài 5.

## Câu hỏi tự kiểm tra

1. Viết lại hai hàm `y = f(x)` và `x = φ(y)` bằng lời, không dùng ký hiệu. Hàm nào là "hiểu",
   hàm nào là "làm"?
2. Lý thuyết cân bằng cổ điển "vứt bỏ" hàm nào để đứng được? Nó thay hàm đó bằng giả định gì?
3. Phân biệt **gần-cân bằng** và **xa-cân bằng**. Vì sao Soros nói phản thân chỉ quan trọng
   ở vùng thứ hai?
4. Vì sao Soros gọi diễn biến thị trường là "quá trình lịch sử" chứ không phải "trạng thái
   cân bằng"? Từ khoá: *mục tiêu di động*.

## Tóm tắt

- Phản thân = **hai hàm** chạy ngược chiều đồng thời: nhận thức ← tình thế (*cognitive*) và
  tình thế ← nhận thức (*participating*).
- Ghép lại thành cặp **đệ quy** không có điểm tựa cố định → **không hội tụ về cân bằng**.
- Cân bằng cổ điển chỉ đứng được nhờ **bỏ hàm nhận thức** (giả định tri thức hoàn hảo).
- Phản thân là hiện tượng **từng lúc**: mạnh ở vùng **xa-cân bằng** (nơi sinh bong bóng/sụp
  đổ), yếu ở vùng **gần-cân bằng**.
- Hệ quả: đọc thị trường như một **quá trình lịch sử**, không phải bài toán tìm giá đúng.

---

**Bản đồ khoá học** · [Mục lục khoá](../README.md)

Trước: [Bài 0 — Nhập môn](bai_00_nhap_mon.md)
Bạn đang ở **Bài 1 — Lí thuyết phản thân** ← *bạn đang ở đây*
Tiếp theo: [Bài 2 — Phản thân trong thị trường cổ phiếu](bai_02_thi_truong_co_phieu.md)
