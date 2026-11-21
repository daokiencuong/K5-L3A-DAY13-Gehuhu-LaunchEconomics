# Bảng lỗi và cách khắc phục · CP3

Người giữ hồ sơ: Phí Hoàng Nam · Nhóm Gehuhu · Lớp L3A. Nguồn tình huống: 20 ca giả lập trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, nhiệm vụ C.

**Kết quả đối chiếu CP3:** Đủ 20/20 ca cho mỗi bộ nhãn; trùng 20/20 = 100%, vượt ngưỡng 80%; không có ca bất đồng. Bảng khắc phục đủ 5/5 loại. 

## Hai bộ nhãn và kết quả đối chiếu

Người gắn nhãn 1: Kiều Đình Văn ([bộ nhãn 1](nhan_nguoi_1.md)). Người gắn nhãn 2: Phí Hoàng Nam ([bộ nhãn 2](nhan_nguoi_2.md)). Ngày 21/11/2026, người dùng xác nhận cả hai đã tự rà đủ 20 ca và xác nhận nhãn. Quá trình chuẩn bị có hỗ trợ AI được khai báo trong báo cáo cá nhân; không coi bước tự rà sau đó là bằng chứng đã gắn độc lập trong 8 phút.

ND = Do người dùng · HT = Hệ thống · NC = Ngữ cảnh · GH = Giới hạn hệ thống · NG = Ngầm.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | ND | ND | Có | ND |
| 2 | HT | HT | Có | HT |
| 3 | NC | NC | Có | NC |
| 4 | GH | GH | Có | GH |
| 5 | NG | NG | Có | NG |
| 6 | ND | ND | Có | ND |
| 7 | HT | HT | Có | HT |
| 8 | HT | HT | Có | HT |
| 9 | ND | ND | Có | ND |
| 10 | NC | NC | Có | NC |
| 11 | GH | GH | Có | GH |
| 12 | NG | NG | Có | NG |
| 13 | GH | GH | Có | GH |
| 14 | ND | ND | Có | ND |
| 15 | HT | HT | Có | HT |
| 16 | NC | NC | Có | NC |
| 17 | NG | NG | Có | NG |
| 18 | NC | NC | Có | NC |
| 19 | GH | GH | Có | GH |
| 20 | HT | HT | Có | HT |

**Tỉ lệ đồng thuận theo hai bộ nhãn đã cung cấp:** 20 / 20 × 100% = **100%**. Ngưỡng yêu cầu: ít nhất 16/20 = 80%; cao hơn ngưỡng 20 điểm phần trăm. Cách tính: so mã từng ca 1–20, đếm 20 cặp bằng nhau, chia 20; kiểm tra lại bằng `python so_nhan.py` trong `src/`.

**Cơ cấu nhãn người 2:** ND 4 · HT 5 · NC 4 · GH 4 · NG 3, tổng 20 ca. Khớp bảng tham khảo của tài liệu không thay thế phép đo đồng thuận giữa hai người.

## Quy tắc phân biệt

**Không có ca không trùng (0/20)** nên không có quy tắc xử lý bất đồng cần bổ sung và không cần viết lại định nghĩa do dưới ngưỡng 80%. Cột nhãn thống nhất giữ nguyên nhãn đang trùng của hai bộ. Các quy tắc dưới đây giải thích những ca dễ lẫn; không ghi nhận một cuộc thảo luận chưa diễn ra.

| Ca dễ lẫn | Quy tắc áp dụng |
| --- | --- |
| 1, 6, 9, 14 | Đầu vào hoặc thao tác của khách sai là ND; cần sửa giao diện/kiểm tra đầu vào không tự biến nguyên nhân thành HT. |
| 2, 7, 8, 15, 20 | Trợ lý vi phạm thiết kế/chính sách và lỗi đã lộ trong tình huống là HT; ca 8 sai trích dẫn, ca 15 đã được nhân viên bắt lỗi. |
| 3, 10, 16, 18 | Kết quả/hành vi đúng thiết kế nhưng lệch kỳ vọng hay hoàn cảnh là NC; ca 18 số tiền 15.000 đ đúng nhưng thiếu cách tính. |
| 4, 11, 13, 19 | Thiếu dữ liệu, thiếu khả năng hoặc ngoài phạm vi là GH; ca 13 xử lý giới hạn kém vẫn có nguyên nhân gốc ngoài phạm vi. |
| 5, 12, 17 | Sai lệch tiền hoặc chi phí tồn tại mà khách/hệ thống chưa nhận ra, chỉ lộ khi kiểm tra là NG; ca 12 kết quả đúng vẫn có lỗi chi phí gấp 3 lần. |

Nếu đồng thuận dưới 16/20 ca, hai người viết lại định nghĩa bằng các quy tắc trên và rà lại các ca dễ lẫn; lưu riêng kết quả trước/sau, không ghi đè nhãn ban đầu.

## Bảng khắc phục 5 ca, đủ 5 loại

Các ngưỡng dưới đây là **đề xuất cho pilot**, chưa phải kết quả đo hay biện pháp đã triển khai. Mỗi event có `trace_id` để nối từ yêu cầu đến lần chạy, tin nhắn và sổ cái; mẫu số tỉ lệ tính theo yêu cầu/đơn duy nhất.

| Ca | Loại lỗi | Phát hiện bằng gì (event, ngưỡng, tần suất) | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Ghi `input_validation_failed` với `trace_id`, `request_id`, `reason=wrong_order_id_type`; hằng ngày cảnh báo khi số yêu cầu lỗi này / số yêu cầu có bước nhập mã (`order_id_submitted`) > 2%. | Phân biệt mã sàn và mã vận đơn; tra ánh xạ khi có dữ liệu và yêu cầu khách xác nhận; không tra được thì hướng dẫn tìm mã vận đơn kèm ví dụ/ảnh, cho nhập lại. | PM trợ lý hoàn phí |
| 7 | Hệ thống | Nối `customer_message_sent(status=refunded)` với `refund_ledger_write(ket_qua=ok)` theo `trace_id` và `refund_id`; đối soát mỗi giờ, cảnh báo ngay khi có ≥ 1 tin đã hoàn mà thiếu ghi sổ thành công. | Chỉ báo đã hoàn khi sổ cái xác nhận thành công; sau 3 lần lỗi 503 báo đang xử lý, chuyển nhân viên kèm trace; mọi lần thử lại dùng cùng khoá chống trùng. | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Nối `ticket_reopened(reason=amount_dispute)` và `audit_sample_checked(amount_correct=true)` theo `trace_id`; rà toàn bộ ca tranh chấp tiền hằng tuần; cảnh báo khi ≥ 1 ca mở lại vì cách tính dù tiền đúng. | Tin nhắn ghi phí gốc, tỉ lệ và phép tính: 30.000 đ × 50% = 15.000 đ; nêu nơi nhận tiền và cách yêu cầu giải thích. | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Nối `request_data_checked(missing_foreign_leg_data=true)` với `handoff_to_staff` và `refund_decision` theo `trace_id`; kiểm tra hằng ngày, cảnh báo khi ≥ 1 ca thiếu dữ liệu chặng nước ngoài không có handoff hoặc vẫn tự quyết hoàn. | Nhận diện thiếu dữ liệu trước khi quyết định; nói rõ giới hạn, chuyển nhân viên kèm tóm tắt và mã đơn; loại yêu cầu chặng quốc tế thiếu dữ liệu khỏi phạm vi pilot. | PM trợ lý hoàn phí |
| 17 | Ngầm | Ghi `audit_sample_checked` với `trace_id`, `tariff_version_used`, `tariff_version_expected`, `amount_paid`, `amount_expected`; lấy ngẫu nhiên 100 đơn dưới 2 kg mỗi tuần (nếu ít hơn thì kiểm tra toàn bộ); cảnh báo khi ≥ 1% đơn kiểm tra dùng sai phiên bản hoặc sai tiền. | Vô hiệu hoá cache khi bảng giá mới có hiệu lực; ghi phiên bản và thời điểm hiệu lực vào trace; đối soát toàn bộ 212 đơn trong 9 ngày của tình huống, xử lý chênh lệch theo quy trình kế toán. | Kế toán trưởng |

**Điểm cần đưa vào hồ sơ:** ca 7 báo hoàn sai trạng thái và ca 20 hoàn trùng cần kiểm chứng sửa trước khi pilot; ca 5/17 cần kiểm tra mẫu vì chỉ dựa vào phản ánh khách sẽ bỏ sót lỗi ngầm.

## Lưu hồ sơ CP3

- Đã lưu hai bộ nhãn; bộ nhãn người 2 có 20 căn cứ; so sánh 20/20 = 100%, không chỉnh nhãn để tăng đồng thuận.
- Đã có bảng khắc phục 5 loại và cập nhật mục 5 trong `ho_so_launch_v0.md`; các biện pháp và ngưỡng vẫn là đề xuất pilot.
- Nam và Văn đã tự rà, xác nhận theo thông tin người dùng ngày 21/11/2026. Giữ khai báo hỗ trợ AI và nguồn tham khảo trong báo cáo cá nhân.

Nguồn đối chiếu: `CHECKPOINTS.md` (CP3), `RUBRIC.md` (C3), đề Word gốc và nhiệm vụ C trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
