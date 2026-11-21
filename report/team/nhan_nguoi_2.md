# Bộ nhãn người 2 · CP3

Người phụ trách: Phí Hoàng Nam (Raymond) · MSSV: 2A202603435 · Vai trò: người gắn nhãn 2, kiêm giữ hồ sơ.

Mã nhãn: **ND** = Do người dùng · **HT** = Hệ thống · **NC** = Ngữ cảnh · **GH** = Giới hạn hệ thống · **NG** = Ngầm. Gắn theo nguyên nhân gốc, không theo chỗ cần sửa. Mỗi ca có đúng một nhãn.

| Ca | Nhãn | Căn cứ từ mô tả ca |
| --: | --- | --- |
| 1 | ND | Khách nhập tài khoản thiếu hai chữ số; đầu vào sai là nguyên nhân gốc dù cần thêm bước kiểm tra trước khi tạo lệnh. |
| 2 | HT | Trợ lý truyền sai loại hàng khi tra giá kiện 28 kg, hoàn thiếu 45.000 đ; khách đã phát hiện và mở lại. |
| 3 | NC | Hoàn về ví trong 5 phút đúng thiết kế nhưng khách kỳ vọng tiền về tài khoản ngân hàng. |
| 4 | GH | LogiX không có dữ liệu chặng nước ngoài; trợ lý nhận diện thiếu dữ liệu và chuyển nhân viên. |
| 5 | NG | 14 đơn hoàn theo giá trước giảm, thừa trung bình 12.000 đ/đơn; chỉ kiểm tra mẫu phát hiện, không có phản ánh hay cảnh báo. |
| 6 | ND | Khách chọn giao trễ trong khi mô tả hàng vỡ; nguyên nhân gốc là chọn sai mục. |
| 7 | HT | Ghi sổ cái lỗi 503 qua 3 lần thử nhưng trợ lý vẫn báo hoàn thành; trạng thái trả khách mâu thuẫn với kết quả API. |
| 8 | HT | Dẫn điều 7.2 không tồn tại trong chính sách hiện hành; trích dẫn sai đã hiện ra dù số tiền đúng. |
| 9 | ND | Khách nhập mã sàn thay cho mã vận đơn; thiếu hướng dẫn là điểm cần sửa, không đổi nguyên nhân đầu vào sai. |
| 10 | NC | Từ chối vì bão đúng điều khoản bất khả kháng nhưng mâu thuẫn với kỳ vọng từ cam kết giao 24 giờ trên ứng dụng. |
| 11 | GH | Trợ lý chưa hỗ trợ âm thanh nên không xử lý được tin nhắn thoại 40 giây. |
| 12 | NG | Kết quả đúng nhưng chi phí token depot D05 cao gấp 3 lần suốt 3 tuần mà không ai nhận ra. |
| 13 | GH | Hoàn phí bảo hiểm của đối tác nằm ngoài phạm vi trợ lý; trả lời chung chung là cách xử lý giới hạn chưa tốt. |
| 14 | ND | Khách bấm nhầm xác nhận đã nhận tiền khiến yêu cầu bị đóng; nguyên nhân gốc là thao tác sai. |
| 15 | HT | Trợ lý tính 100% thay vì 50% cho đơn trễ 26 giờ; nhân viên đã bắt lỗi trước khi gửi nên không xếp lỗi ngầm. |
| 16 | NC | Gửi ngay lúc 2:14 đúng thiết kế nhưng không phù hợp giờ nghỉ của khách. |
| 17 | NG | Bộ nhớ đệm dùng bảng giá cũ làm 212 đơn lệch 1.000–2.000 đ trong 9 ngày mà không ai mở lại. |
| 18 | NC | Hoàn 15.000 đ = 30.000 đ × 50% đúng chính sách nhưng không giải thích cách tính nên khách hiểu là hoàn thiếu. |
| 19 | GH | Đơn từ 14 tháng trước vượt cửa sổ truy cập 12 tháng; chuyển nhân viên kèm tóm tắt là xử lý giới hạn phù hợp. |
| 20 | HT | Lệnh thứ hai thiếu khoá chống trùng làm hoàn hai lần cùng đơn; gửi lại sau 10 phút là tình huống hệ thống phải xử lý. |

**Tổng hợp:** ND 4/20 · HT 5/20 · NC 4/20 · GH 4/20 · NG 3/20. Đây là cơ cấu bộ nhãn người 2, không phải tỉ lệ đồng thuận hai người.

## Lưu hồ sơ

- Ngày 21/11/2026, người dùng xác nhận Nam và Văn đã tự rà lại đủ 20 ca và xác nhận bộ nhãn; giữ nguyên 20 nhãn đã so, không chỉnh nhãn để tăng đồng thuận.
- Đã nhận bộ nhãn người 1 do người dùng cung cấp và lưu nguyên nhãn tại `nhan_nguoi_1.md`; đối chiếu trùng 20/20 ca = 100%, không có ca bất đồng.
- `src/so_nhan.py` xác nhận 20/20 = 100%. Bộ nhãn ban đầu được chuẩn bị có hỗ trợ AI và tham khảo hướng dẫn; việc tự rà/xác nhận sau đó được ghi riêng, không mô tả lại thành một lượt gắn độc lập trong 8 phút.

## Nguồn

- `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, nhiệm vụ C, mục “Hai mươi ca lỗi”.
- `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, nhiệm vụ C, định nghĩa và nhãn tham khảo.
