# Báo cáo cá nhân CP3 · Phí Hoàng Nam · 2A202603435

## 1. Thông tin thành viên

- Họ tên: Phí Hoàng Nam.
- MSSV: 2A202603435.
- Email: 26ai.namph3@vinuni.edu.vn.
- Nhóm: Gehuhu · Lớp: L3A.
- Vai trò: người gắn nhãn 2, kiêm giữ hồ sơ.

## 2. Phần việc phụ trách

Phân loại 20 ca lỗi theo 5 loại, chuẩn bị cách khắc phục và ghi trạng thái CP3 vào hồ sơ launch v0. Báo cáo này chỉ ghi phần CP3.

## 3. Đóng góp cụ thể

Đã chuẩn bị với Codex bộ nhãn người 2 có lý do từng ca: ND 4, HT 5, NC 4, GH 4, NG 3. Đã lưu bộ nhãn người 1 do người dùng cung cấp, đối chiếu từng cặp: 20/20 ca trùng = 100%, không có bất đồng.

Bảng khắc phục chọn các ca 9, 7, 18, 4, 17, mỗi ca có event, ngưỡng cảnh báo, tần suất và một vai trò chịu trách nhiệm. Đã cập nhật mục 5 của hồ sơ launch v0 với kết quả so nhãn và lưu ý về ca 7/20 trước pilot.

## 4. Bằng chứng

- [Bộ nhãn người 2](nhan_nguoi_2.md): 20 nhãn và căn cứ.
- [Bộ nhãn người 1](nhan_nguoi_1.md): nguyên nhãn do người dùng gửi, chuyển sang mã ND/HT/NC/GH/NG.
- [Bảng lỗi](bang_loi.md): 20 cặp nhãn trùng, cách tính 20/20 × 100% = 100%, 5 quy tắc phân biệt và khắc phục đủ 5 loại.
- [Hồ sơ launch v0](ho_so_launch_v0.md): mục 5; [TEAM.md](../../TEAM.md): mục Phí Hoàng Nam.
- `src/so_nhan.py`: công cụ kiểm tra hai tệp nhãn; số ca trùng 20/20 = 100%.

## 5. Công cụ AI đã dùng

Codex đọc đề Word gốc, CHECKPOINTS, RUBRIC và hướng dẫn; đề xuất nhãn có căn cứ, soạn bảng khắc phục và kiểm tra cấu trúc. Bộ nhãn người 2 đã được đối chiếu bảng tham khảo trong hướng dẫn; không trình bày như bằng chứng tự gắn độc lập trong 8 phút. Nhãn người 1 lấy từ nội dung người dùng gửi, không do AI tạo thêm.

Kiểm tra bằng công cụ: đủ 20 ca trong mỗi tệp, chỉ dùng 5 mã hợp lệ; so sánh từng cặp bằng `src/so_nhan.py`; bảo toàn các mục khác trong hồ sơ launch. Nam cần tự đọc lại 20 ca, giải thích nguyên nhân gốc và xác nhận bộ nhãn trước nộp; chưa ghi nhận bước xác nhận cá nhân này đã diễn ra.

## 6. Tự đánh giá

Phần soạn CP3 có đủ 20 cặp nhãn, đồng thuận theo hai bộ đã cung cấp là 100% và 5 phương án khắc phục. Còn Nam tự rà, xác nhận nhãn và khai báo đúng quy trình gắn nhãn. Các event/ngưỡng là đề xuất pilot, chưa phải tính năng đã triển khai hoặc kết quả đo thực tế.
