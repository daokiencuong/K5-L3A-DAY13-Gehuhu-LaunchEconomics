# Báo cáo cá nhân · Đào Kiên Cường · 2A202603396

## 1. Thông tin thành viên

- Họ tên: Đào Kiên Cường.
- MSSV: 2A202603396.
- Email: 26ai.cuongdk@vinuni.edu.vn.
- Nhóm: Gehuhu · Lớp: L3A.
- Vai trò: người viết code.

## 2. Phần việc phụ trách

Hoàn thiện và chạy `src/lab13.py` để tính chi phí (A), độ nhạy (B), cỡ mẫu pilot (D1) và ba chỉ số dùng trong hồ sơ (E1).

## 3. Đóng góp cụ thể

- CP1: triển khai ba hàm A1 và `mo_hinh()` cho A2; tính A3 theo `loai` và A4 khi cộng chi phí cố định. Ba phép thử A1 in **ĐẠT** (1,20 · 1,25 · 1,25); A2 cho **4.472 đ/việc thành công [simulated]**.
- CP2: dùng lại `mo_hinh()` cho chín kịch bản B1, kịch bản kết hợp B2, chi phí cả hệ thống ở B3 và xem lại 100% ở B4. Giới hạn hai lần chạy cho tổng chi phí hệ thống thấp nhất: **6.901.220 đ [simulated]**.
- CP4: tính D1 với baseline 0,70, alpha 0,05, power 0,80 và ICC 0,02; MDE 5 điểm cần **1.251 yêu cầu/nhánh**, còn phương án theo nhân viên chấp nhận MDE 6 điểm với **859 mẫu hiệu dụng/nhánh**.
- CP5: tính thử chỉ số chính **82,83% (994/1.200)**, sửa/bỏ gợi ý **27,12% (48/177)** và mở lại trong 7 ngày **4,25% (51/1.200)** trên dữ liệu giả lập.

## 4. Bằng chứng

- [Code tính A, B, D1 và E1](../../src/lab13.py).
- [Bảng chi phí và độ nhạy](bang_chi_phi.md), [kế hoạch pilot](pilot_plan.yaml), [đặc tả chỉ số](chi_so.md).
- Chạy trong thư mục `src/`: `.\.venv\Scripts\python.exe -X utf8 lab13.py`; đầu ra in ba phép thử A1 ĐẠT và các bảng A–E1.

## 5. Công cụ AI đã dùng

Codex hỗ trợ viết và chỉnh sửa code, đọc yêu cầu lab, đối chiếu đầu ra với dữ liệu và điền số vào hồ sơ. Code được chạy trong môi trường `.venv` của repo; kết quả A1, chi phí, cỡ mẫu và ba chỉ số E1 đã được kiểm tra từ đầu ra. Phần tính từ hai cột phút `_simulated` được ghi nhãn `simulated` trong báo cáo.

## 6. Tự đánh giá

Phần code hiện chạy từ đầu đến cuối và in đủ kết quả A, B, D1, E1. Trước khi nộp, tôi cần tự đọc lại công thức và giải thích được vì sao chi phí tính mọi lần chạy nhưng chỉ chia cho số việc thành công, cũng như đánh đổi cỡ mẫu khi chọn MDE 6 điểm.
