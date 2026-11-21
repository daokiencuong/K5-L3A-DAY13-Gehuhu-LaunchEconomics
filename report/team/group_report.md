# Báo cáo nhóm Lab 13 Gehuhu L3A

## 1. Thông tin nhóm

Nhóm Gehuhu, lớp L3A, gồm Đào Kiên Cường (code), Phan Bá An (kiểm số), Kiều Đình Văn (nhãn 1), Phí Hoàng Nam (nhãn 2 và hồ sơ). Đóng góp và commit nằm trong [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Lập hồ sơ Gate 2a cho trợ lý hoàn phí LogiX-VN từ 1.200 yêu cầu và 1.624 lần chạy giả lập. Tính mọi chi phí chạy, xem lại và làm lại; chỉ chia cho việc thành công. Kết quả chạy thử là mô tả mẫu, chưa chứng minh tác động của trợ lý vì chưa có đối chứng.

## 3. Giải pháp

Code A–B–D–E ở [lab13.py](../../src/lab13.py); số và giả định ở [bảng chi phí](bang_chi_phi.md). CP3 có hai bộ nhãn và [khắc phục 5 loại](bang_loi.md). [Pilot plan](pilot_plan.yaml) quy định phân nhóm, mẫu, lịch và luật dừng; [chỉ số](chi_so.md) nối phép đo với event; [hồ sơ launch](ho_so_launch_v0.md) tổng hợp quyết định. Kiểm tra trong `.venv` Python 3.15: code chạy hết, A1 đạt, so nhãn 20/20, YAML đọc được và `pip check` không báo lỗi phụ thuộc.

## 4. Kết quả

- CPS toàn mẫu **4.472 đ [simulated]**; phạm vi nội địa + hàng nặng, cộng cố định ở 45.000 yêu cầu/tháng: **4.599 đ [simulated]**.
- Làm lại gấp đôi: CPS **+51,8% lên 6.787 đ [simulated]**. Giới hạn 2 lần chạy có tổng chi phí hệ thống thấp nhất: **6.901.220 đ [simulated]**.
- Trong mẫu giả lập: chỉ số chính **82,83%**; sửa/bỏ gợi ý **27,12%**; mở lại trong 7 ngày **4,25%**.
- Hai bộ nhãn trùng **20/20 = 100%**. Ngày 21/11/2026, người dùng xác nhận Nam và Văn đã tự rà và xác nhận nhãn; bước gắn nhãn ban đầu có hỗ trợ AI, không được ghi thành quy trình gắn độc lập trong 8 phút.
- Đề xuất: **Go có điều kiện**, chỉ pilot `noi_dia` và `hang_nang`; chi tiết điều kiện trong hồ sơ launch.

## 5. Đánh đổi của pilot

Với 40 nhân viên, thiết kế theo cụm không đủ phát hiện 5 điểm: giới hạn 1.000 mẫu hiệu dụng/nhánh < 1.251. Chọn 20 nhân viên/nhánh, MDE 6 điểm, ít nhất 299 yêu cầu/người; nếu hiệu ứng thật là 5 điểm, power còn khoảng 0,64. Kế hoạch: chuẩn bị xong 30/11/2026; rollout 10% ngày 01–09/12, 25% ngày 10–18/12, 50% và lấy mẫu chính ngày 19–31/12; theo dõi đóng trong 24 giờ tới 01/01 và mở lại đủ 7 ngày tới 08/01/2027; quyết định 09/01. Thiếu mẫu thì hoãn quyết định theo kế hoạch, không kết luận sớm.

## 6. Đóng góp và công cụ

Đóng góp A–E được đối chiếu với commit trong TEAM. Codex hỗ trợ rà soát và hoàn thiện hồ sơ; báo cáo cá nhân giữ khai báo AI đúng nguồn. Theo phạm vi yêu cầu lần hoàn thiện này, không tạo thêm báo cáo cá nhân Cường/An; đây không phải xác nhận đã đủ bốn báo cáo theo yêu cầu gốc.

## 7. Duyệt chéo và hạn chế

Chưa nhận hồ sơ nhóm được chấm và kết quả trao đổi Gate 2a; [phiếu chấm](phieu_cham.md) phải phản ánh dữ liệu thực tế khi có. Chưa ghi nhận việc nộp LMS của từng thành viên. Trước pilot cần kiểm chứng chống hoàn trùng, đối soát sổ cái và đo thời gian lao động thật; event/ngưỡng đang là thiết kế, chưa phải kết quả triển khai.

## 8. Nguồn

[CHECKPOINTS](../../CHECKPOINTS.md), [RUBRIC](../../RUBRIC.md), [SUBMISSION](../../SUBMISSION.md), [dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md), [hướng dẫn chi tiết](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md) và các commit trong TEAM.
