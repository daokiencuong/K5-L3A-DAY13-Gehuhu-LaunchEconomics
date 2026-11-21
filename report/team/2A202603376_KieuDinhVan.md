# Báo cáo cá nhân CP3 Kiều Đình Văn 2A202603376

## 1. Thông tin thành viên

- Họ tên: Kiều Đình Văn · MSSV: 2A202603376.
- Email: 26ai.vankd@vinuni.edu.vn.
- Nhóm: Gehuhu · Lớp: L3A.
- Vai trò: người gắn nhãn 1.

## 2. Phần việc phụ trách

Đọc yêu cầu CP3, lập nhãn 20 ca theo năm loại PAIR, đối chiếu nguyên nhân gốc và giữ bằng chứng so nhãn. Báo cáo ghi phần CP3.

## 3. Đóng góp cụ thể

- Nhãn người 1: ND 1, 6, 9, 14 · HT 2, 7, 8, 15, 20 · NC 3, 10, 16, 18 · GH 4, 11, 13, 19 · NG 5, 12, 17.
- Ca 13 là GH vì yêu cầu ngoài phạm vi; cách trả lời chung chung là điểm khắc phục. Ca 8 là HT vì dẫn điều khoản không tồn tại, dù số tiền đúng.
- So với người 2: trùng 20/20 = 100%, kiểm bằng `python so_nhan.py` trong `src/`.
- Dọn bảng lỗi sau merge PR #1/#2, bổ sung báo cáo cá nhân và khai báo AI.
- Ngày 21/11/2026, người dùng xác nhận Nam và Văn đều đã tự rà lại 20 ca và xác nhận nhãn; xác nhận này ghi bước rà soát sau hỗ trợ AI.

## 4. Bằng chứng

Commit `d438c50` (nhánh `gn1`, PR #1); `37c6e0e` (dọn bảng lỗi, thêm báo cáo); `3f63bec` (khai báo AI). Các tệp: [nhãn người 1](nhan_nguoi_1.md), [bảng lỗi](bang_loi.md), [TEAM](../../TEAM.md).

## 5. Công cụ AI và cách kiểm tra

Theo khai báo đã có trong repo, Claude Code chạy trong VS Code hỗ trợ đọc đề, tóm tắt năm loại PAIR, đề xuất nhãn và lý do cho ca dễ lẫn 8, 13. Codex chuẩn hóa báo cáo trong lần hoàn thiện này dựa trên lịch sử Git và xác nhận người dùng; không tạo thêm lời xác nhận của Văn.

Cách kiểm tra: đọc mô tả từng ca theo nguyên nhân gốc; đối chiếu hai bộ nhãn bằng `so_nhan.py`, đếm 20/20 cặp bằng nhau. Người dùng đã xác nhận ngày 21/11/2026 rằng Văn tự rà và xác nhận nhãn.

## 6. Tự đánh giá

Sản phẩm có đủ 20 cặp nhãn, đồng thuận 100%, quy tắc cho ca dễ lẫn và khắc phục đủ 5 loại. Giai đoạn ban đầu chưa thực hiện gắn độc lập trong 8 phút theo đề và có hỗ trợ AI như khai báo. Bước tự rà được xác nhận sau đó không được trình bày như việc quy trình ban đầu đã diễn ra đúng yêu cầu.
