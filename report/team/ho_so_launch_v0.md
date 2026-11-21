# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Gehuhu · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc trên toàn mẫu [simulated] = 4.373.585 đ ÷ 978 việc thành công, gấp 16,3× hoá đơn token + tool chia số yêu cầu (274,7 đ). Làm lại chiếm 51,8%, xem lại 40,7% [simulated]. Phạm vi noi_dia + hang_nang, đã cộng cố định 40 triệu/tháng: 4.599 đ ở 45.000 yc/tháng (+1.185 đ/việc), 5.784 đ nếu khối lượng còn một nửa [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại ±51,8% (gấp đôi → 6.787 đ) · 2. Tỉ lệ xem lại ±40,7% (gấp đôi → 6.292 đ) · 3. Lương nhân viên +23,1% khi tăng 25% [simulated]. Giá token chỉ ±5,6% → pilot theo dõi tỉ lệ làm lại và xem lại, không phải giá token | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | So với 12.000 đ: noi_dia 0,22×, hang_nang 0,69×, quoc_te 1,88×, doi_tac 0,85× [simulated] → loại quoc_te, doi_tac khỏi pilot. Chi phí cả hệ thống: (4.373.585 + 222 × 12.000) ÷ 1.200 = 5.865 đ/yêu cầu = 0,49× [simulated]. Giới hạn 2 lần chạy rẻ nhất cho công ty: 6.901.220 đ cả hệ thống, rẻ hơn giới hạn 1 lần 548.561 đ dù cps cao hơn (4.237 so với 4.111 đ) [simulated]. Nếu phải xem lại 100%: 11.743 đ = 0,98×, hoặc 12.415 đ = 1,03× với 15,3 phút làm lại/ca như dữ liệu [simulated] → hoà vốn khi mỗi lần xem lại ≤ 5,1 phút | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | ... (đợi CP5) | ... | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Hai bộ nhãn đủ 20 ca, trùng 20/20 = 100% (ngưỡng 80%); 0 ca bất đồng. Khắc phục 5/5 loại có event, ngưỡng, tần suất và vai trò. Nhãn người 2 có hỗ trợ AI, cần Nam rà/xác nhận quy trình trước nộp. Ca 7 báo hoàn khi ghi sổ lỗi, ca 20 hoàn trùng: cần kiểm chứng sửa trước pilot. Bằng chứng: [bảng lỗi](bang_loi.md), [nhãn người 1](nhan_nguoi_1.md), [nhãn người 2](nhan_nguoi_2.md) | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | Phân ngẫu nhiên theo nhân viên, 20 can thiệp + 20 đối chứng cùng 12 depot; scope noi_dia + hang_nang. Với 40 nhân viên, MDE 5 điểm cần 1.251 mẫu hiệu dụng/nhánh nhưng giới hạn là 1.000; chấp nhận MDE 6 điểm, 859 mẫu hiệu dụng/nhánh, 299 yêu cầu/nhân viên, DE 6,96. Nếu hiệu ứng thật chỉ 5 điểm, power còn 0,64. Mở lại hiện tại 4,25% toàn mẫu, 3,97% phạm vi; dừng khi chênh ≥2 điểm hoặc vượt 6%. | Giả lập | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | ... (đợi CP5) | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go · Go có điều kiện · No-go (giữ một). Go có điều kiện: ghi từng điều kiện, người phụ trách, ngày kiểm tra. No-go: ghi việc phải làm để quay lại cổng.

- ...
