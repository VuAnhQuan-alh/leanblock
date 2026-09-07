# Hình minh hoạ — 67 biểu đồ SVG

Mọi hình trong khoá học nằm ở đây. **Không có hình nào vẽ tay.** Tất cả sinh ra bằng Python thư
viện chuẩn, đọc thẳng dữ liệu từ [`../thuc_hanh/`](../thuc_hanh/README.md) — nên hình **không bao
giờ lệch** với con số trong bài học.

## Sinh lại toàn bộ

```bash
python3 sinh-hinh.py
```

Không cần cài gói nào. Không matplotlib, không numpy. Chỉ `math`, `pathlib`, `xml.sax.saxutils`.

## Vì sao là SVG chứ không phải PNG

| | |
| --- | --- |
| **Là văn bản** | Vào git sạch, xem được diff, không phình kho như ảnh nhị phân |
| **Không vỡ** | Phóng to bao nhiêu cũng nét — quan trọng khi đọc trên màn hình lớn hoặc in ra |
| **Hiển thị mọi nơi** | GitHub, Obsidian, VS Code, trình duyệt đều dựng được trực tiếp |
| **Nhẹ** | Cả 67 hình cộng lại chưa tới 540 KB |
| **Sửa được** | Muốn đổi màu hay chữ thì mở file text ra sửa, hoặc sửa `sinh-hinh.py` rồi chạy lại |

## Danh sách

| Hình | Bài | Nội dung | Nguồn dữ liệu |
| --- | :---: | --- | --- |
| [bai01-bon-thanh-phan.svg](bai01-bon-thanh-phan.svg) | 1 | Sơ đồ bốn thành phần hệ thống tài chính | sơ đồ |
| [bai01-dau-gia.svg](bai01-dau-gia.svg) | 1 | Bậc thang giá thầu thật của lớp học | `bai-01` |
| [bai02-duong-thoi-gian.svg](bai02-duong-thoi-gian.svg) | 2 | Đường thời gian và phép chiết khấu | sơ đồ |
| [bai02-ba-dong-tien.svg](bai02-ba-dong-tien.svg) | 2 | Vĩnh viễn · Gordon · niên kim theo r | công thức |
| [bai02-ghep-lai.svg](bai02-ghep-lai.svg) | 2 | APR so với EAR theo tần suất ghép lãi | công thức |
| [bai03-don-bay.svg](bai03-don-bay.svg) | 3 | Vốn chủ còn lại theo mức đòn bẩy | `bai-03` |
| [bai04-duong-cong-lai-suat.svg](bai04-duong-cong-lai-suat.svg) | 4 | Ba hình dạng đường cong lãi suất | `bai-04` |
| [bai04-lai-suat-ky-han.svg](bai04-lai-suat-ky-han.svg) | 4 | Suy ra lãi suất kỳ hạn từ hai mức giá | sơ đồ |
| [bai05-duration-convexity.svg](bai05-duration-convexity.svg) | 5 | Đường thẳng duration so với đường cong thật | `bai-05` |
| [bai05-co-may-aaa.svg](bai05-co-may-aaa.svg) | 5 | Cỗ máy cắt lớp, và chỗ nó gãy | sơ đồ |
| [bai05-loi-am.svg](bai05-loi-am.svg) | 5 | Lồi âm: quyền trả trước ép phẳng đường giá | `bai-05` |
| [bai05-phong-ho-dong.svg](bai05-phong-ho-dong.svg) | 5 | Phòng hộ từng bước chốt lại một con số | `bai-05` |
| [bai06-gordon.svg](bai06-gordon.svg) | 6 | Giá cổ phiếu khi g tiến tới r | `bai-06` |
| [bai06-tang-truong.svg](bai06-tang-truong.svg) | 6 | Giá theo tỷ lệ giữ lại, ba mức ROE | `bai-06` |
| [bai07-payoff-ky-han.svg](bai07-payoff-ky-han.svg) | 7 | Payoff kỳ hạn — đường thẳng | công thức |
| [bai08-payoff-quyen-chon.svg](bai08-payoff-quyen-chon.svg) | 8 | Payoff call và put, gộp và ròng | công thức |
| [bai08-chien-luoc-ket-hop.svg](bai08-chien-luoc-ket-hop.svg) | 8 | Straddle · bull spread · butterfly | công thức |
| [bai08-cay-nhi-thuc.svg](bai08-cay-nhi-thuc.svg) | 8 | Cây nhị thức một bước và tham số biến mất | công thức |
| [bai08-ngang-gia-put-call.svg](bai08-ngang-gia-put-call.svg) | 8 | Hai danh mục trùng khít ở mọi trạng thái | công thức |
| [bai09-duoi-beo.svg](bai09-duoi-beo.svg) | 9 | Phân phối lợi suất thật so với phân phối chuẩn | `bai-09` |
| [bai10-duong-dan.svg](bai10-duong-dan.svg) | 10 | Đường đạn hai tài sản theo năm mức tương quan | `bai-10` |
| [bai10-gioi-han-da-dang-hoa.svg](bai10-gioi-han-da-dang-hoa.svg) | 10 | Rủi ro danh mục theo n — Mỹ và Việt Nam | `bai-10` |
| [bai10-huu-dung-lom.svg](bai10-huu-dung-lom.svg) | 10 | Hàm hữu dụng lõm và phí rủi ro | `bai-10` |
| [bai10-bien-hieu-qua.svg](bai10-bien-hieu-qua.svg) | 10 | Biên hiệu quả, tiếp tuyến, và CAL | `bai-10` |
| [bai11-cml-sml.svg](bai11-cml-sml.svg) | 11 | CML và SML đặt cạnh nhau | sơ đồ |
| [bai11-sml-do-that.svg](bai11-sml-do-that.svg) | 11 | SML lý thuyết so với SML đo được | `bai-11` |
| [bai12-la-chan-thue.svg](bai12-la-chan-thue.svg) | 12 | Khấu hao đường thẳng so với nhanh dần | `bai-12` |
| [bai12-npv-irr.svg](bai12-npv-irr.svg) | 12 | NPV theo r — một nghiệm và ba nghiệm | công thức |
| [bai13-su-kien-737max.svg](bai13-su-kien-737max.svg) | 13 | Nghiên cứu sự kiện Boeing 737 MAX | `bai-13` |
| [bai13-tu-tuong-quan-the-ky.svg](bai13-tu-tuong-quan-the-ky.svg) | 13 | Tự tương quan lăn cận 60 tháng, 1931–2026 | `bai-13` |
| [bai13-sml-hai-che-do.svg](bai13-sml-hai-che-do.svg) | 13 | SML trong thị trường bình lặng và căng thẳng | `bai-13` |
| [bai14-ban-do-sinh-loi.svg](bai14-ban-do-sinh-loi.svg) | 14 | Bản đồ sinh lời: biên × vòng quay = ROA | `bai-14` |
| [bai14-dupont-cot.svg](bai14-dupont-cot.svg) | 14 | Ba thành phần DuPont, bảy doanh nghiệp | `bai-14` |
| [bai14-apple-don-bay.svg](bai14-apple-don-bay.svg) | 14 | Apple mười năm: ROE tăng do đâu | `bai-14` |
| [bai14-chu-ky-tien-mat.svg](bai14-chu-ky-tien-mat.svg) | 14 | Chu kỳ tiền mặt năm doanh nghiệp | `bai-14` |
| [bai14-roic.svg](bai14-roic.svg) | 14 | ROIC nhiều năm, bốn doanh nghiệp | `bai-14` |
| [bai15-thanh-phan-wacc.svg](bai15-thanh-phan-wacc.svg) | 15 | WACC tách thành phần vốn chủ và nợ | `bai-15` |
| [bai15-do-nhay.svg](bai15-do-nhay.svg) | 15 | WACC theo phần bù rủi ro giả định | `bai-15` |
| [bai15-hamada.svg](bai15-hamada.svg) | 15 | Beta có và không đòn bẩy | `bai-15` |
| [bai15-roic-wacc.svg](bai15-roic-wacc.svg) | 15 | ROIC so với WACC, năm doanh nghiệp | `bai-15` |
| [bai16-ba-the-gioi.svg](bai16-ba-the-gioi.svg) | 16 | WACC theo đòn bẩy trong ba thế giới lý thuyết | `bai-16` |
| [bai16-hvn.svg](bai16-hvn.svg) | 16 | Vốn chủ Vietnam Airlines 2013–2025 | `bai-16` |
| [bai16-duoi-trai.svg](bai16-duoi-trai.svg) | 16 | Khả năng trả lãi và đuôi trái của vốn chủ | `bai-16` |
| [bai16-trat-tu-uu-tien.svg](bai16-trat-tu-uu-tien.svg) | 16 | Nguồn vốn của 12 doanh nghiệp Mỹ | `bai-16` |
| [bai16-dua-ngua.svg](bai16-dua-ngua.svg) | 16 | Sinh lời so với đòn bẩy, 28 doanh nghiệp | `bai-16` |
| [bai17-chuyen-rui-ro.svg](bai17-chuyen-rui-ro.svg) | 17 | Vốn chủ là quyền chọn mua trên tài sản | `bai-17` |
| [bai17-co-tuc-muot.svg](bai17-co-tuc-muot.svg) | 17 | Biến thiên của lợi nhuận so với cổ tức | `bai-17` |
| [bai17-co-tuc-vs-mua-lai.svg](bai17-co-tuc-vs-mua-lai.svg) | 17 | Kênh cam kết và kênh linh hoạt | `bai-17` |
| [bai17-boeing.svg](bai17-boeing.svg) | 17 | Boeing: tiền ra ngoài so với tiền vào nhà máy | `bai-17` |
| [bai17-chi-tra-vn.svg](bai17-chi-tra-vn.svg) | 17 | Chi trả và tăng trưởng, 27 doanh nghiệp | `bai-17` |
| [bai17-loi-nhuan-khong-phai-tien.svg](bai17-loi-nhuan-khong-phai-tien.svg) | 17 | Lợi nhuận so với dòng tiền cộng dồn | `bai-17` |
| [bai18-gia-tri-cuoi-ky.svg](bai18-gia-tri-cuoi-ky.svg) | 18 | Phần giá trị nằm ở giai đoạn dự báo | `bai-18` |
| [bai18-do-nhay.svg](bai18-do-nhay.svg) | 18 | Giá trị một cổ phiếu theo WACC và g | `bai-18` |
| [bai18-dcf-hong.svg](bai18-dcf-hong.svg) | 18 | Dòng tiền tự do bình quân 5 năm, 28 doanh nghiệp | `bai-18` |
| [bai18-dcf-nguoc.svg](bai18-dcf-nguoc.svg) | 18 | Tăng trưởng hàm ý so với tăng trưởng thực tế | `bai-18` |
| [bai18-boi-so.svg](bai18-boi-so.svg) | 18 | Ba bội số trên cùng một mẫu | `bai-18` |
| [bai18-loi-nguyen.svg](bai18-loi-nguyen.svg) | 18 | Lời nguyền người thắng cuộc theo số đối thủ | `bai-18` |
| [bai19-apv-vs-wacc.svg](bai19-apv-vs-wacc.svg) | 19 | Tỷ trọng nợ thay đổi khi trả theo lịch | `bai-19` |
| [bai19-hai-cong-thuc-beta.svg](bai19-hai-cong-thuc-beta.svg) | 19 | Hamada so với tái cân bằng | `bai-19` |
| [bai19-nguong-dau-tu.svg](bai19-nguong-dau-tu.svg) | 19 | Ngưỡng đầu tư theo biến động | `bai-19` |
| [bai19-bien-dong-that.svg](bai19-bien-dong-that.svg) | 19 | Biến động vốn chủ so với tài sản | `bai-19` |
| [bai19-gia-tri-quyen-cho.svg](bai19-gia-tri-quyen-cho.svg) | 19 | Giá trị quyền chờ so với NPV làm ngay | `bai-19` |
| [bai20-don-bay-va-gia.svg](bai20-don-bay-va-gia.svg) | 20 | Cho vay thêm làm giá tăng, dòng tiền không đổi | `bai-20` |
| [bai20-nguoi-mua-bien.svg](bai20-nguoi-mua-bien.svg) | 20 | Đòn bẩy đẩy người mua biên lên | `bai-20` |
| [bai20-ba-luc.svg](bai20-ba-luc.svg) | 20 | Tách cú sụp thành ba lực | `bai-20` |
| [bai20-bien-dong-don-bay.svg](bai20-bien-dong-don-bay.svg) | 20 | Biến động quyết định đòn bẩy | `bai-20` |
| [bai20-tuong-quan-vn.svg](bai20-tuong-quan-vn.svg) | 20 | Ba cú sụp Việt Nam: biến động và tương quan | `bai-20` |

Cột **Nguồn dữ liệu**: `bai-NN` nghĩa là hình đọc dữ liệu thật từ file thực hành tương ứng;
*công thức* nghĩa là hình vẽ từ hàm toán thuần tuý; *sơ đồ* nghĩa là hình khái niệm không có số.

## Quy ước vẽ

| Quy ước | Lý do |
| --- | --- |
| Bảng màu 6 màu cố định trong `svg_loi.py` | Phân biệt được cả khi in đen trắng và với người mù màu đỏ–lục |
| Nét liền = giá trị thật · nét đứt = xấp xỉ hoặc lý thuyết | Người đọc nhìn kiểu nét là biết ngay đâu là số đo, đâu là mô hình |
| Mỗi hình có một câu ghi chú ở đáy | Hình phải tự đứng được, không cần đọc thân bài |
| Con số trong tiêu đề và ghi chú do **code tính**, không gõ tay | Sửa dữ liệu là hình tự cập nhật, không có chỗ cho số cũ sót lại |
| Nhãn tiếng Việt có dấu | Hình là để đọc, không phải để đối chiếu với code |

## Kiến trúc

| File | Vai trò |
| --- | --- |
| [svg_loi.py](svg_loi.py) | Lõi vẽ: lớp `Hinh` với hệ toạ độ, trục, đường, cột, chấm, chú thích. ~230 dòng |
| [sinh-hinh.py](sinh-hinh.py) | Mỗi hình một hàm. Gọi `nap()` để mượn dữ liệu đã nhúng trong `thuc_hanh/` |

Hàm `nap()` nạp file trong `thuc_hanh/` như một module Python và nuốt phần in ra màn hình, chỉ giữ
lại các biến dữ liệu. Nhờ vậy **không có một con số nào bị chép lại lần thứ hai**.

---

Chỉ mục môn học: [README.md](../README.md)
