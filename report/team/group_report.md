# Báo cáo nhóm · Lab 13 · Gehuhu · L3A

## 1. Thông tin nhóm

- Nhóm: Gehuhu · Lớp: L3A.
- Thành viên và vai trò: xem [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Nhóm lập hồ sơ Gate 2a cho trợ lý hoàn phí LogiX-VN từ dữ liệu giả lập: tính chi phí mỗi việc thành công; kiểm tra nhân viên có dùng gợi ý không; xác định cách phát hiện và xử lý lỗi; thiết kế pilot có đối chứng, cỡ mẫu và luật dừng. Các chỉ số trong đợt chạy thử được mô tả như số liệu mẫu, không diễn giải thành tác động nhân quả vì chưa có đối chứng trong bộ dữ liệu.

## 3. Giải pháp

- **A–B:** triển khai hàm chi phí và phân tích độ nhạy trong [`src/lab13.py`](../../src/lab13.py); kết quả và giả định ở [`bang_chi_phi.md`](bang_chi_phi.md).
- **C:** lập hai bộ nhãn, tính đồng thuận và đề xuất khắc phục năm loại lỗi trong [`bang_loi.md`](bang_loi.md). Trạng thái CP3 ghi rõ người gắn nhãn 2 còn phải tự rà, xác nhận quy trình trước khi nộp.
- **D:** tính cỡ mẫu, chọn phân nhóm theo nhân viên và ghi luật dừng trong [`pilot_plan.yaml`](pilot_plan.yaml).
- **E:** lập chỉ số, danh sách event và rủi ro kinh tế trong [`chi_so.md`](chi_so.md); tổng hợp đề xuất trong [`ho_so_launch_v0.md`](ho_so_launch_v0.md).

## 4. Kết quả

- Chi phí mỗi việc thành công toàn mẫu: **4.472 đ [simulated]**; trong phạm vi nội địa và hàng nặng, sau chi phí cố định là **4.599 đ** ở 45.000 yêu cầu/tháng.
- Làm lại là yếu tố nhạy nhất: gấp đôi làm CPS tăng **51,8% lên 6.787 đ [simulated]**. Giới hạn 2 lần có tổng chi phí hệ thống thấp nhất trong ba kịch bản: **6.901.220 đ [simulated]**.
- Chỉ số trong mẫu: đóng trong 24 giờ và không mở lại là **82,83%**; sửa/bỏ gợi ý là **27,12%**; mở lại trong 7 ngày là **4,25%**. Đây là mô tả dữ liệu giả lập, không phải mức tăng do trợ lý gây ra.
- Pilot phân ngẫu nhiên theo nhân viên, 20 can thiệp và 20 đối chứng; chấp nhận MDE 6 điểm. Nếu hiệu ứng thật chỉ 5 điểm, power ước tính là **0,64**.
- Đề xuất trong hồ sơ: **Go có điều kiện**, giới hạn phạm vi vào `noi_dia` và `hang_nang`, phụ thuộc vào điều kiện an toàn, đo lường và khắc phục đã ghi trong hồ sơ.

## 5. Khó khăn và cách xử lý

40 nhân viên không đủ để phát hiện mức chênh 5 điểm với thiết kế theo cụm: mẫu hiệu dụng tối đa là 1.000 mỗi nhánh, thấp hơn 1.251 yêu cầu cần thiết. Nhóm ghi rõ đánh đổi sang MDE 6 điểm và nêu power 0,64 nếu tác động thật chỉ là 5 điểm. Dữ liệu thời gian xem lại/làm lại là simulated, nên pilot cần thay bằng thời gian đo thật sau tuần đầu.

## 6. Tổng hợp đóng góp

Nhóm phân vai theo TEAM.md: Đào Kiên Cường phụ trách code và điều phối; Kiều Đình Văn gắn nhãn 1; Phí Hoàng Nam gắn nhãn 2 và giữ hồ sơ; Phan Bá An kiểm số. Mỗi thành viên cần tự xác nhận phần đóng góp và bằng chứng trong báo cáo cá nhân trước khi nộp; báo cáo cá nhân của Cường và An hiện chưa có trong repo.

## 7. Hạn chế và hướng cải thiện

Dữ liệu đầu vào hoàn toàn giả lập và đợt chạy thử chưa có nhóm đối chứng, nên chưa thể kết luận mức cải thiện do trợ lý. Cần sửa, xác minh khoá chống trùng và đối soát sổ cái ở các ca 7 và 20; xác nhận quy trình nhãn CP3; bật đủ event có `trace_id`; dùng số phút lao động đo thực tế; và giữ luật dừng trước khi bắt đầu pilot.

## 8. Tài liệu tham khảo

- `README.md`, `CHECKPOINTS.md`, `RUBRIC.md`, `SUBMISSION.md` trong repo bài lab.
- [`docs/du_lieu_va_cong_thuc.md`](../../docs/du_lieu_va_cong_thuc.md) và [`docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).
- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*; Google PAIR, *People + AI Guidebook*, “Errors + Graceful Failure”.
