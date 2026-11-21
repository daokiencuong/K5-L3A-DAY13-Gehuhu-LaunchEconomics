# Báo cáo cá nhân CP3 · Kiều Đình Văn · 2A202603376

## 1. Thông tin thành viên

- Họ tên: Kiều Đình Văn.
- MSSV: 2A202603376.
- Email: 26ai.vankd@vinuni.edu.vn.
- Nhóm: Gehuhu · Lớp: L3A.
- Vai trò: người gắn nhãn 1.

## 2. Phần việc phụ trách

Đọc đề, theo dõi điều kiện "Xong khi" và gắn nhãn 20 ca lỗi của nhiệm vụ C theo năm loại Google PAIR. Báo cáo này chỉ ghi phần CP3.

## 3. Đóng góp cụ thể

- Bộ nhãn người 1 cho 20 ca theo nguyên nhân gốc: ND 1, 6, 9, 14 · HT 2, 7, 8, 15, 20 · NC 3, 10, 16, 18 · GH 4, 11, 13, 19 · NG 5, 12, 17.
- Hai ca dễ lẫn: ca 13 xếp GH vì yêu cầu nằm ngoài phạm vi (việc trợ lý không nói rõ giới hạn là phần khắc phục); ca 8 xếp HT vì dẫn điều khoản không có là vi phạm chính sách, dù số tiền đúng.
- So với bộ nhãn người 2: trùng 20/20 = 100%, kiểm lại bằng `python so_nhan.py` trong `src/`.
- Dọn `bang_loi.md` sau khi merge PR #1 và #2: còn một bảng so nhãn duy nhất, bỏ dòng tỉ lệ để trống và bảng bị lỗi.

## 4. Bằng chứng

- Commit `d438c50` trên nhánh `gn1`, merge vào `main` qua PR #1.
- [Bộ nhãn người 1](nhan_nguoi_1.md), [bảng lỗi](bang_loi.md), mục Kiều Đình Văn trong [TEAM.md](../../TEAM.md).

## 5. Công cụ AI đã dùng

**Công cụ:** Claude Code, chạy trong VS Code trên repo nhóm.

- Đọc đề, tóm tắt yêu cầu của vai người gắn nhãn 1: lấy 20 ca từ đề Word, năm loại PAIR và các bước của nhiệm vụ C trong `CHECKPOINTS.md` và hướng dẫn chi tiết.
- Đề xuất nhãn cho 20 ca theo nguyên nhân gốc, kèm lý do cho các ca dễ lẫn (8, 13).

## 6. Tự đánh giá

Sản phẩm CP3 đủ: 20 cặp nhãn, tỉ lệ đồng thuận, quy tắc cho ca dễ lẫn, bảng khắc phục 5 loại. Điểm yếu là quy trình: chưa gắn độc lập trong 8 phút như đề yêu cầu. Trước khi nộp, tôi cần tự đọc lại 20 ca và giải thích được nguyên nhân gốc của từng nhãn.
