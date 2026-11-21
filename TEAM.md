# Team Gehuhu

## Thông tin nhóm

- Tên nhóm: Gehuhu · Lớp: L3A.
- Repo nhóm: [K5-L3A-DAY13-Gehuhu-LaunchEconomics](https://github.com/daokiencuong/K5-L3A-DAY13-Gehuhu-LaunchEconomics).
- Nhánh nộp: `main`; nhánh làm việc: `label/nguoi2-raymond`.
- Commit nền đã đối chiếu: `99f5158`. Commit nộp cuối là commit chứa bộ hồ sơ hoàn thiện được push lên `main`, xác định bằng `git rev-parse origin/main` sau khi chốt.

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | --- | --- | --- | --- | --- |
| 1 | Đào Kiên Cường | 2A202603396 | <26ai.cuongdk@vinuni.edu.vn> | daokiencuong | Người viết code |
| 2 | Kiều Đình Văn | 2A202603376 | <26ai.vankd@vinuni.edu.vn> | vankd2307 | Người gắn nhãn 1 |
| 3 | Phí Hoàng Nam | 2A202603435 | <26ai.namph3@vinuni.edu.vn> | PhiHoangNamRaymond | Người gắn nhãn 2, kiêm giữ hồ sơ |
| 4 | Phan Bá An | 2A202603375 | <26ai.anpb@vinuni.edu.vn> | anphn3 | Người kiểm số |

## Đào Kiên Cường · 2A202603396

### Phần việc phụ trách

Triển khai và chạy mô hình chi phí, phân tích độ nhạy, cỡ mẫu và chỉ số trong `src/lab13.py`; tổng hợp kết quả tính vào các hồ sơ liên quan.

### Đóng góp cụ thể

- CP1: hoàn thiện hàm A1, mô hình chi phí và phần A trong commit `6e518bf`.
- CP2: bổ sung các kịch bản độ nhạy và giới hạn chạy lại trong commit `7bc8a2a`.
- CP4: bổ sung tính D1 và kế hoạch pilot trong commit `603d657`.
- CP5: bổ sung phép tính chỉ số E1, chỉ số/event, hồ sơ và báo cáo nhóm trong commit `99f5158`.

### Bằng chứng

Lịch sử Git ghi tác giả `daokiencuong` ở bốn commit trên; các tệp [code](src/lab13.py), [bảng chi phí](report/team/bang_chi_phi.md), [kế hoạch pilot](report/team/pilot_plan.yaml), [chỉ số](report/team/chi_so.md) và [hồ sơ launch](report/team/ho_so_launch_v0.md). Việc merge PR #1 và #2 được ghi trong `df67de3` và `731791e`.

## Kiều Đình Văn · 2A202603376

### Phần việc phụ trách

Người gắn nhãn 1: đọc yêu cầu CP3, lập bộ nhãn 20 ca và đối chiếu bảng lỗi.

### Đóng góp cụ thể

- Lập nhãn người 1 trong commit `d438c50` (nhánh `gn1`, PR #1); hai bộ nhãn trùng 20/20 = 100%.
- Dọn bảng lỗi sau merge và bổ sung báo cáo cá nhân trong `37c6e0e`; cập nhật khai báo công cụ AI trong `3f63bec`.
- Người dùng xác nhận ngày 21/11/2026 rằng Văn và Nam đều đã tự rà và xác nhận 20 nhãn. Xác nhận này ghi nhận bước rà soát sau hỗ trợ AI; không thay đổi lịch sử quy trình gắn nhãn ban đầu.

### Bằng chứng

[Nhãn người 1](report/team/nhan_nguoi_1.md), [bảng lỗi](report/team/bang_loi.md), [báo cáo Kiều Đình Văn](report/team/2A202603376_KieuDinhVan.md) và các commit nêu trên.

## Phí Hoàng Nam · 2A202603435

### Phần việc phụ trách

Người gắn nhãn 2, kiêm giữ hồ sơ: lập nhãn 20 ca, duy trì hồ sơ launch và kiểm tra tính nhất quán giữa các sản phẩm CP1–CP5.

### Đóng góp cụ thể

- Cập nhật bảng chi phí/hồ sơ ở `93a0c3c`, `e87ce3a`; thêm tệp nhãn và công cụ so nhãn ở `1b2148a`; tổng hợp nhãn, bảng khắc phục, hồ sơ và báo cáo cá nhân trong `93d7395`.
- Bộ nhãn người 2 có ND 4, HT 5, NC 4, GH 4, NG 3; so với người 1 trùng 20/20 = 100%; bảng khắc phục bao phủ đủ 5 loại.
- Trong lần hoàn thiện này, dùng Codex đối chiếu số liệu, chuẩn hóa event, lịch pilot, luật dừng và hồ sơ; nguồn hỗ trợ AI được khai báo trong báo cáo cá nhân.
- Người dùng xác nhận ngày 21/11/2026 rằng Nam và Văn đều đã tự rà và xác nhận 20 nhãn; không ghi lại bước này thành việc gắn độc lập trong 8 phút trước khi so.

### Bằng chứng

[Nhãn người 2](report/team/nhan_nguoi_2.md), [bảng lỗi](report/team/bang_loi.md), [hồ sơ launch](report/team/ho_so_launch_v0.md), [báo cáo Phí Hoàng Nam](report/team/2A202603435_PhiHoangNam.md) và các commit nêu trên.

## Phan Bá An · 2A202603375

### Phần việc phụ trách

Người kiểm số: đối chiếu kết quả A–B, điền bảng chi phí và kiểm tra nhãn `simulated`.

### Đóng góp cụ thể

- Commit `7559d90`: kiểm số phần A, bổ sung nhãn `simulated`.
- Commit `1125122`: bỏ câu trả lời A3/A4 bị lặp sau merge.
- Commit `d3fff9f`: điền và kiểm số B1–B4, ghi bảng B1/B3 và câu trả lời B2/B3/B4; thông điệp commit ghi việc đối chiếu output với script kiểm độc lập và có đồng tác giả Claude Opus 5.5.

### Bằng chứng

Lịch sử Git ghi tác giả `Phan Ba An` ở ba commit trên; [bảng chi phí](report/team/bang_chi_phi.md). Các con số đã đối chiếu gồm 4.472 đ/việc [simulated] ở A2, 6.543 đ/việc [simulated] khi token và xem lại cùng gấp đôi, và 6.901.220 đ [simulated] cho tổng hệ thống khi giới hạn 2 lần chạy.

## Báo cáo cá nhân trong bản đóng gói

Bản đóng gói này giữ [báo cáo Nam](report/team/2A202603435_PhiHoangNam.md) và [báo cáo Văn](report/team/2A202603376_KieuDinhVan.md). Theo yêu cầu của người dùng ở lần hoàn thiện này, không tạo thêm hai báo cáo cá nhân của Cường và An; phần đóng góp của hai thành viên vẫn được ghi bằng bằng chứng Git ở trên.
