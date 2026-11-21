# Báo cáo cá nhân Lab 13 Phí Hoàng Nam 2A202603435

## 1. Thông tin thành viên

- Họ tên: Phí Hoàng Nam · MSSV: 2A202603435.
- Email: 26ai.namph3@vinuni.edu.vn.
- Nhóm: Gehuhu · Lớp: L3A.
- Vai trò: người gắn nhãn 2, kiêm giữ hồ sơ.

## 2. Phần việc phụ trách

Lập bộ nhãn người 2, bảng khắc phục và giữ hồ sơ launch; đối chiếu nội dung A–E, trạng thái, nhãn `simulated` và bằng chứng đóng góp. Các thay đổi của lần hoàn thiện này được chuẩn bị với hỗ trợ Codex, không thay thế xác nhận thực tế của các thành viên hay hội đồng.

## 3. Đóng góp cụ thể

- Cập nhật chi phí và hồ sơ ở `93a0c3c`, `e87ce3a`; thêm tệp nhãn và công cụ so nhãn ở `1b2148a`; tổng hợp CP3 trong `93d7395`.
- Bộ nhãn người 2: ND 4, HT 5, NC 4, GH 4, NG 3. Đối chiếu nguyên bộ nhãn người 1: 20/20 ca trùng = 100%, không có ca bất đồng; chuẩn bị khắc phục ca 9, 7, 18, 4, 17, đủ năm loại.
- Trong lần hoàn thiện, dùng Codex rà lại số liệu và thống nhất hồ sơ: event phát hiện lỗi, chỉ số, luật dừng, lịch thu mẫu và theo dõi 7 ngày, kết luận Go có điều kiện cùng người phụ trách và hạn kiểm tra.
- Ngày 21/11/2026, người dùng xác nhận cả Nam và Văn đã tự rà lại 20 ca và xác nhận bộ nhãn. Đây là xác nhận rà soát sau hỗ trợ AI; không ghi thành việc đã gắn độc lập trong 8 phút trước khi so nhãn.

## 4. Bằng chứng

[Nhãn người 2](nhan_nguoi_2.md), [nhãn người 1](nhan_nguoi_1.md), [bảng lỗi](bang_loi.md), [hồ sơ launch](ho_so_launch_v0.md), [chỉ số](chi_so.md), [kế hoạch pilot](pilot_plan.yaml), [báo cáo nhóm](group_report.md) và [TEAM](../../TEAM.md). Các commit trên ghi tác giả Raymond; `src/so_nhan.py` kiểm tra 20 cặp nhãn trùng = 100%.

## 5. Công cụ AI và cách kiểm tra

Codex đọc đề Word, CHECKPOINTS, RUBRIC và hướng dẫn; đề xuất nhãn có căn cứ, soạn khắc phục, rà số liệu và cấu trúc hồ sơ. Nhãn người 2 đã được đối chiếu bảng tham khảo; bộ nhãn người 1 được nhận từ dữ liệu người dùng cung cấp và repo nhóm.

Kiểm tra bằng công cụ gồm ba phép thử A1, tính lại chi phí/độ nhạy/cỡ mẫu/chỉ số từ CSV, đọc YAML và chạy công cụ so nhãn. Trong lần hoàn thiện này, code chạy hết bằng `.venv` Python 3.15, A1 đạt, so nhãn 20/20, YAML đọc được và `pip check` không báo lỗi phụ thuộc. Xác nhận cá nhân về nhãn là thông tin người dùng cung cấp ngày 21/11/2026. Việc duyệt chéo và nộp LMS chỉ ghi khi có bằng chứng thực tế; không dùng kết quả AI để điền thay.

## 6. Tự đánh giá

Phần hồ sơ có đủ 20 cặp nhãn, đồng thuận 100% và khắc phục đủ 5 loại. Điểm hạn chế là giai đoạn gắn nhãn ban đầu có hỗ trợ AI và tham khảo hướng dẫn; bước tự rà đã được xác nhận nhưng không xoá hạn chế lịch sử đó. Các số phút lao động là simulated; event, ngưỡng và lịch pilot là đề xuất cần kiểm chứng khi chạy. Kết quả Gate 2a và trạng thái nộp LMS phụ thuộc thông tin thực tế của nhóm.
