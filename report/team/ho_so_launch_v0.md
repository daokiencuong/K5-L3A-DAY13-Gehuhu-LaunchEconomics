# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Gehuhu · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu: 4.472 đ (4.373.585 ÷ 978), gấp 16,3× hoá đơn 274,7 đ [simulated]. Trong scope noi_dia + hang_nang, cộng cố định: 4.599 đ ở 45.000 yc/tháng; 5.784 đ nếu còn nửa sản lượng [simulated]. | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2: CPS +51,8% lên 6.787 đ; xem lại ×2: +40,7% lên 6.292 đ; lương +25%: +23,1%. Theo dõi làm lại và xem lại trước giá token (±5,6%) [simulated]. | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | So với 12.000 đ: noi_dia 0,22×, hang_nang 0,69×, quoc_te 1,88×, doi_tac 0,85×; pilot chỉ hai loại đầu [simulated]. Giới hạn 2 lần rẻ nhất toàn hệ thống (6.901.220 đ). Xem lại 100% có thể lên 12.415 đ = 1,03× [simulated]. | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, dùng, an toàn | Chạy thử: 82,83% (994/1.200); sửa/bỏ 27,12% (48/177); mở lại 4,25% (51/1.200) [simulated]. Chỉ mô tả mẫu, chưa kết luận tác động; pilot cần event `agent_suggestion_shown`, `audit_sample_checked`. | Giả lập | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Hai bộ nhãn đủ 20 ca, trùng 20/20 = 100% (ngưỡng 80%); khắc phục đủ 5 loại. Nhãn người 2 có hỗ trợ AI; ca 7 và 20 cần xác minh sửa trước pilot. Chi tiết: [bảng lỗi](bang_loi.md), [nhãn 1](nhan_nguoi_1.md), [nhãn 2](nhan_nguoi_2.md). | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | Ngẫu nhiên 20 nhân viên can thiệp + 20 đối chứng, cùng depot. MDE 5 điểm cần 1.251 mẫu hiệu dụng/nhánh, tối đa 1.000; chọn MDE 6 điểm: 859/nhánh, 299 yêu cầu/người, DE 6,96; power 0,64 nếu hiệu ứng thật là 5 điểm. Dừng nếu chênh mở lại ≥2 điểm hoặc vượt 6%. | Giả lập | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại ×2: CPS +51,8% lên 6.787 đ; xem lại 100%: tới 12.415 đ = 1,03×; nửa sản lượng làm cố định tăng 1.185 → 2.370 đ/việc [simulated]. Theo dõi ba chỉ số này hằng tuần. | Giả lập | PM trợ lý hoàn phí |

Điều kiện trước pilot: Kỹ sư trưởng xác minh chống trùng/đối soát ca 7, 20; Giám đốc vận hành chấp nhận MDE 6 điểm và power 0,64; Trưởng nhóm CSKH chốt giảm xem lại; PM bật event có `trace_id` và thay phút simulated bằng phút đo sau tuần đầu. Hạn sẵn sàng **2026-12-15**, kiểm event **2026-12-22**, quyết định **2027-01-05**.

**Đề xuất: Go có điều kiện.** Chỉ pilot `noi_dia` và `hang_nang` theo kế hoạch, với ba luật dừng an toàn, chi phí và mức sử dụng trong `pilot_plan.yaml`.
