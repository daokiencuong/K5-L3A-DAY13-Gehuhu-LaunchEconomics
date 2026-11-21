# Hồ sơ launch v0 - Trợ lý hoàn phí LogiX-VN

Nhóm Gehuhu · L3A · Gate 2a · Dữ liệu lab giả lập; chỉ đề xuất pilot. Bằng chứng chi tiết: [chi phí](bang_chi_phi.md), [lỗi](bang_loi.md), [kế hoạch](pilot_plan.yaml), [chỉ số](chi_so.md).

| Mục | Con số chính và kết luận | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1. Chi phí mỗi việc thành công | Toàn mẫu: 4.373.585 / 978 = 4.472 đ; gấp 16,3 lần hoá đơn token/tool trên mỗi yêu cầu [simulated]. Nội địa + hàng nặng, cộng cố định 40 triệu/tháng: 4.599 đ ở 45.000 yêu cầu/tháng; 5.784 đ khi còn nửa khối lượng [simulated]. | Giả lập | PM trợ lý hoàn phí |
| 2. Ba yếu tố nhạy nhất | Gấp đôi làm lại: +51,8% lên 6.787 đ; gấp đôi xem lại: +40,7% lên 6.292 đ; lương tăng 25%: +23,1% [simulated]. Giảm nửa làm lại/xem lại lần lượt −25,9%/−20,3% [simulated]. | Giả lập | PM trợ lý hoàn phí |
| 3. So với nhân viên tự làm | Nhân viên: 12.000 đ/yêu cầu. CPS nội địa 0,22×; hàng nặng 0,69×; quốc tế 1,88×; đối tác 0,85× [simulated]. Chỉ pilot hai loại đầu. Xem lại 100%: 11.743–12.415 đ/việc [simulated], gần hoặc vượt chi phí nhân viên. Giới hạn 2 lần rẻ nhất cho cả hệ thống: 6.901.220 đ trên mẫu [simulated]. | Giả lập | PM trợ lý hoàn phí |
| 4. Chính, dùng, an toàn | Chạy thử: đóng 24h không mở lại 7 ngày 994/1.200 = 82,83%; sửa/bỏ gợi ý 48/177 = 27,12%; mở lại 51/1.200 = 4,25%. Có đặc tả event để đo pilot; chưa kết luận tác động nhân quả vì mẫu không có đối chứng. | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5. Lỗi và khắc phục | 20 ca, hai bộ nhãn trùng 20/20 = 100%; khắc phục đủ 5 loại, có event/ngưỡng/tần suất/vai trò. Người dùng xác nhận cả hai đã tự rà nhãn ngày 21/11/2026; khai báo AI trong báo cáo cá nhân. Ca 7 và 20 cần kiểm chứng ghi sổ và chống hoàn trùng trước pilot. | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6. Pilot plan | 20 nhân viên can thiệp + 20 đối chứng, phân tầng depot. MDE 6 điểm: 859 mẫu hiệu dụng/nhánh, tối thiểu 299 yêu cầu/người, DE 6,96 [giả định lab]. MDE 5 điểm cần 1.251; thiết kế chỉ đạt tối đa 1.000, power còn 0,64 nếu tác động thật 5 điểm. Lấy mẫu 19–31/12/2026; theo dõi hết 08/01/2027; quyết định 09/01. | Xong, có bằng chứng | Giám đốc vận hành |
| 7. Rủi ro kinh tế | Làm lại gấp đôi tăng CPS 51,8%; xem lại 100% với 15,3 phút làm lại làm CPS lên 1,03× nhân viên; giảm nửa khối lượng tăng cố định từ 1.185 lên 2.370 đ/việc [simulated]. Đo phút thật và giảm xem lại theo bậc khi an toàn cho phép. | Giả lập | PM trợ lý hoàn phí |

Điều kiện, đều là mốc kế hoạch: trước 30/11/2026, Kỹ sư trưởng xác minh ca 7/20 và rollback; Giám đốc vận hành ký đánh đổi MDE; Trưởng nhóm CSKH chốt cách giảm xem lại; PM xác minh event. PM thay phút simulated bằng đo thật sau tuần 1, kiểm tra ngày 08/12. Hoàn trùng từ 1 ca thì tắt ngay; các luật tỉ lệ, chi phí và sử dụng theo kế hoạch. Thiếu quota hoặc thời gian theo dõi thì không Go, gia hạn hai nhánh theo lịch đã ghi.

**Đề xuất: Go có điều kiện.** Chỉ pilot `noi_dia` + `hang_nang` khi đủ điều kiện trên; việc sửa lỗi và chạy pilot chưa được xác nhận đã thực hiện.
