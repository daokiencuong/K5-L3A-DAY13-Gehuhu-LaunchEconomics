# Báo cáo cá nhân · Kiều Đình Văn · 2A202603376

## 1. Thông tin thành viên

- Họ tên: Kiều Đình Văn
- MSSV: 2A202603376
- Email: 26ai.vankd@vinuni.edu.vn
- GitHub: vankd2307
- Nhóm: Gehuhu · Lớp: L3A
- Vai trong nhóm: người gắn nhãn 1

## 2. Phần việc phụ trách

Theo `TEAM.md` và hướng dẫn buổi chiều, vai người gắn nhãn 1 gồm ba việc:

1. **Đọc đề** và tóm tắt cho nhóm yêu cầu của từng checkpoint.
2. **Theo dõi điều kiện "Xong khi"** của từng nhiệm vụ, và rà checklist nộp bài trong `SUBMISSION.md` cùng `RUBRIC.md` trước khi nộp.
3. **CP3 · Nhiệm vụ C:** gắn nhãn 20 ca lỗi theo năm loại Google PAIR, so với người gắn nhãn 2, chốt nhãn thống nhất và hoàn thiện `bang_loi.md`.

## 3. Đóng góp cụ thể

### 3.1. Đọc đề và tóm tắt yêu cầu

- **CP3:** lấy 20 ca từ mục "Hai mươi ca lỗi" trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, cùng bảng năm loại và câu hỏi nhận diện, bốn bước (8 phút gắn · 3 phút so · 5 phút thống nhất · 14 phút khắc phục) và ngưỡng 16/20.
- **CP4:** tóm tắt cho nhóm ba phần D1 (5 câu cỡ mẫu), D2 (5 câu "tách được tác động"), D3 (điền yaml, 3 luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ), kèm bốn điều kiện "Xong khi". Lưu ý mấu chốt đã báo nhóm: với 40 nhân viên, không cách chia theo cụm nào đủ mẫu cho mức chênh 5 điểm, nên phải chọn và ghi rõ đánh đổi.

### 3.2. CP3 · Gắn nhãn 20 ca theo nguyên nhân gốc

| Loại | Ca | Lý do chung |
| --- | --- | --- |
| Do người dùng (ND) | 1, 6, 9, 14 | Đầu vào hoặc thao tác của khách sai: thiếu số tài khoản, chọn sai mục, nhập mã sàn thay mã vận đơn, bấm nhầm xác nhận |
| Hệ thống (HT) | 2, 7, 8, 15, 20 | Trợ lý làm trái thiết kế hoặc chính sách và lỗi đã lộ ra: sai tham số hàng nặng, báo hoàn khi sổ cái lỗi 503, dẫn điều khoản không có, tính 100% thay vì 50%, hoàn trùng vì thiếu khoá chống trùng |
| Ngữ cảnh (NC) | 3, 10, 16, 18 | Làm đúng thiết kế nhưng không khớp kỳ vọng của khách: hoàn về ví, bất khả kháng khi app vẫn hiện "cam kết 24 giờ", gửi tin lúc 2:14 sáng, tin nhắn thiếu cách tính |
| Giới hạn hệ thống (GH) | 4, 11, 13, 19 | Không thể làm được: thiếu dữ liệu chặng nước ngoài, không xử lý âm thanh, sản phẩm bảo hiểm ngoài phạm vi, đơn quá 12 tháng |
| Ngầm (NG) | 5, 12, 17 | Có sai nhưng khách và hệ thống đều không thấy, chỉ lộ khi kiểm tra: hoàn thừa mã giảm giá, chi phí token D05 gấp 3 lần, dùng bảng giá cũ trong cache |

Quy tắc tôi dùng cho các ca dễ lẫn:

- **Ca 6, 9 (ND, không phải HT):** gốc lỗi là khách chọn hoặc nhập sai. Việc trợ lý không gợi ý là chỗ cần cải thiện, thuộc cột khắc phục.
- **Ca 8 (HT):** dẫn một điều khoản không tồn tại là vi phạm chính sách, dù số tiền vẫn đúng.
- **Ca 12 (NG, không phải HT):** kết quả cuối đúng, nhưng chi phí gấp 3 lần suốt 3 tuần mà không ai nhận ra.
- **Ca 13 (GH):** yêu cầu nằm ngoài phạm vi. Việc trợ lý không nói rõ giới hạn là phần khắc phục, không đổi nguyên nhân gốc.
- **Ca 15 (HT, không phải NG):** lỗi đã được nhân viên xem lại bắt được, nên không còn là lỗi ngầm.
- **Ca 18 (NC, không phải HT):** số tiền 15.000 đ đúng; khách thấy sai vì tin nhắn thiếu cách tính.

### 3.3. CP3 · So nhãn và hoàn thiện `bang_loi.md`

- So với bộ nhãn người 2 bằng `python so_nhan.py` trong `src/`: đủ 20 ca mỗi bộ, chỉ dùng 5 mã hợp lệ, trùng **20/20 = 100%** (ngưỡng 80%). Cơ cấu: ND 4 · HT 5 · NC 4 · GH 4 · NG 3.
- Dọn `bang_loi.md` sau khi merge PR #1 (`gn1`) và PR #2 (`label/nguoi2-raymond`): gộp hai bảng bị lẫn thành một bảng 20 ca có đủ năm cột (người 1, người 2, trùng, thống nhất), bỏ dòng tỉ lệ để trống và bảng hỏng.
- Bảng khắc phục 5 ca (9, 7, 18, 4, 17) đủ năm loại, mỗi dòng có event, ngưỡng, tần suất và một vai trò phụ trách.

### 3.4. Theo dõi "Xong khi" và rà checklist nộp bài

Đã rà toàn bộ repo theo `SUBMISSION.md` và `RUBRIC.md`:

| Kiểm tra | Kết quả |
| --- | --- |
| `cd src && python lab13.py` | Chạy hết, ba phép thử A1 ĐẠT. Máy thứ ba thiếu `statsmodels`: gói đã có trong `requirements.txt`, cài vào là chạy được |
| Sáu file hồ sơ trong `report/team/` | Đủ, đúng tên |
| `pilot_plan.yaml` | `yaml.safe_load` đọc được, không còn `?` ngoài chú thích, 3 luật dừng |
| `grep -rni production report/team` | Không in gì |
| Hồ sơ launch v0 | Đủ bảy mục, có trạng thái và vai trò; dòng cuối "Go có điều kiện" |
| Báo cáo cá nhân | Đủ 4 file đúng định dạng `MSSV_HoTen.md` |

Các chỗ phát hiện thiếu hoặc lệch, đã sửa:

- `TEAM.md`: điền nhánh nộp; điền mục Phan Bá An từ báo cáo cá nhân của An; sửa mục Phí Hoàng Nam cho đúng nguồn của bộ nhãn người 1.
- `group_report.md` mục 6: bỏ câu "báo cáo cá nhân của Cường và An chưa có", vì đã có.
- Khai báo hỗ trợ AI của CP3 thống nhất giữa hai file nhãn, `bang_loi.md`, hồ sơ và các báo cáo.

Còn lại cho nhóm: `phieu_cham.md` (chờ hồ sơ của nhóm n + 1 khi duyệt chéo); trạng thái mục 5 của hồ sơ chờ Nam xác nhận nhãn người 2.

## 4. Bằng chứng

- Commit `d438c50`: gắn nhãn người 1 cho 20 ca (nhánh `gn1`, merge vào `main` qua PR #1).
- Commit `37c6e0e`: dọn bảng lỗi sau merge, thêm báo cáo cá nhân.
- Commit `3f63bec`: cập nhật mục công cụ AI trong báo cáo cá nhân.
- Commit sửa `TEAM.md`, `group_report.md` và hai file nhãn sau khi rà checklist.
- File: [bộ nhãn người 1](nhan_nguoi_1.md), [bảng lỗi](bang_loi.md), mục Kiều Đình Văn và Phan Bá An trong [TEAM.md](../../TEAM.md).

## 5. Công cụ AI đã dùng

**Công cụ:** Claude Code, chạy trong VS Code trên repo nhóm.

**Dùng vào việc gì:**

- Đọc đề Word, `CHECKPOINTS.md`, `SUBMISSION.md`, `RUBRIC.md` và hướng dẫn chi tiết; tóm tắt yêu cầu CP3 và CP4.
- Đề xuất 20 nhãn theo nguyên nhân gốc, kèm lý do cho các ca dễ lẫn.
- Dọn `bang_loi.md`, chạy `so_nhan.py`, rà checklist nộp bài, soạn các sửa đổi trong `TEAM.md`, `group_report.md` và báo cáo này.
- Thao tác git: commit, push nhánh `gn1` và `main`.

**Tự kiểm tra ra sao:** đối chiếu nhãn với mô tả ca trong đề Word bằng câu hỏi nhận diện của từng loại; chạy `so_nhan.py`, `lab13.py` và các lệnh tự kiểm của `pilot_plan.yaml`; xem `git diff` trước mỗi commit để chỉ đổi đúng file cần đổi.

## 6. Tự đánh giá

**Làm được:** CP3 đủ sản phẩm (20 cặp nhãn, tỉ lệ đồng thuận, quy tắc cho ca dễ lẫn, bảng khắc phục đủ năm loại). Phần theo dõi "Xong khi" giúp nhóm phát hiện và sửa các chỗ lệch giữa `TEAM.md`, `group_report.md` và các báo cáo trước khi nộp.

**Điều tôi hiểu:** gắn nhãn theo nguyên nhân gốc chứ không theo chỗ cần sửa (ca 6, 9, 13); khác nhau giữa lỗi hệ thống đã lộ ra (ca 15, nhân viên bắt được) và lỗi ngầm chỉ thấy qua kiểm tra mẫu (ca 5, 12, 17). Hai ca hệ thống 7 và 20 cần sửa trước pilot vì làm sai trạng thái hoặc sai tiền.


