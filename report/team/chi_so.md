# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Toàn bộ số dưới đây đến từ bộ dữ liệu giả lập của lab. Chỉ mô tả kết quả trong đợt chạy thử; không kết luận trợ lý làm thay đổi chỉ số vì chưa có nhóm đối chứng trong dữ liệu này.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính | Tỉ lệ yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu có `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0` / tổng yêu cầu | **82,83% (994/1.200)** |
| Dùng | Tỉ lệ nhân viên sửa hoặc bỏ gợi ý | Số yêu cầu được xem lại có `quyet_dinh_xem_lai` là `sua` hoặc `bo` / số yêu cầu được xem lại | **27,12% (48/177)** |
| An toàn | Tỉ lệ mở lại trong 7 ngày | Số yêu cầu có `mo_lai_trong_7_ngay = 1` / tổng yêu cầu | **4,25% (51/1.200)** |
| Dùng bổ sung | Tỉ lệ yêu cầu can thiệp được mở bằng trợ lý | Số request ở nhánh can thiệp có event `agent_suggestion_shown` / tổng request đủ điều kiện ở nhánh can thiệp | Chưa có event/arm trong CSV; đo trong pilot |
| An toàn bổ sung | Tỉ lệ đơn sai số tiền qua kiểm toán mẫu | Số đơn có `amount_paid != amount_expected` / tổng đơn kiểm toán | Chưa có kiểm toán trong CSV; đo bằng `audit_sample_checked` hằng tuần |

**Diễn giải:** chỉ số trong đợt chạy thử là 82,83%, tỉ lệ sửa/bỏ gợi ý là 27,12%, và tỉ lệ mở lại là 4,25%. Đây là mô tả dữ liệu giả lập, không phải mức tăng do trợ lý gây ra.

## Danh sách event đề xuất cho pilot

Mỗi event cần `trace_id`; dùng thêm `request_id` và `staff_id` khi có để nối dữ liệu theo yêu cầu và nhân viên.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien`, `arm`, `staff_id`, `trace_id` | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | `request_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lượt chạy, kể cả lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `request_id`, `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý được hiển thị |
| `staff_review_decision` | Nhân viên | `request_id`, `staff_id`, `quyet_dinh` (giu/sua/bo), `phut_xem_lai`, `trace_id` | Khi nhân viên gửi, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên | `request_id`, `staff_id`, `phut_lam_lai`, `ly_do`, `trace_id` | Khi xử lý làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `refund_id`, `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi sổ hoàn tiền |
| `handoff_to_staff` | Agent | `request_id`, `reason`, `tom_tat`, `trace_id` | Khi trợ lý chuyển cho nhân viên |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `trace_id` | Khi đóng yêu cầu |
| `ticket_reopened` | Hệ thống ticket | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi khách hoặc nhân viên mở lại |
| `audit_sample_checked` | Kế toán | `request_id`, `amount_paid`, `amount_expected`, `tariff_version`, `trace_id` | Hằng tuần khi kiểm tra mẫu |

**Nối event với chỉ số:**

- Chỉ số chính: mẫu số từ `refund_request_created`; đóng trong 24h từ `ticket_closed`; mở lại 7 ngày từ `ticket_reopened`, nối bằng `request_id` và `trace_id`.
- Tỉ lệ sửa/bỏ gợi ý: `staff_review_decision` với quyết định `sua` hoặc `bo`, chia số yêu cầu có quyết định xem lại.
- Tỉ lệ mở lại: `ticket_reopened` chia tổng `refund_request_created` đủ 7 ngày theo dõi.
- Tỉ lệ mở trợ lý: `agent_suggestion_shown` chia request đủ điều kiện ở nhánh can thiệp.
- Tỉ lệ sai số tiền: `audit_sample_checked` với `amount_paid != amount_expected`, chia số đơn kiểm toán.

## E2 · Rủi ro kinh tế

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | CPS tăng **51,8% lên 6.787 đ/việc** [simulated] | Tỉ lệ làm lại theo tuần vượt 7%; đợt chạy thử trong phạm vi là 4,9% [simulated] | Thu hẹp về `noi_dia`, rà 20 trace làm lại và không tăng rollout | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | **11.743 đ/việc (0,98×)** nếu làm lại 9 phút; **12.415 đ/việc (1,03×)** với trung bình 15,3 phút [simulated] | Tỉ lệ yêu cầu được xem lại vẫn trên 50% cuối bước rollout 25% | Giảm tỉ lệ xem lại theo bậc nếu tỉ lệ sửa/bỏ dưới 15%; giữ kiểm toán mẫu an toàn | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu/tháng cộng **1.185 đ/việc** ở 45.000 yêu cầu, hoặc **2.370 đ/việc** nếu còn nửa khối lượng [simulated] | Số việc thành công theo tuần dưới 50% kế hoạch | Không mở rộng rollout; PM rà lại giả định khối lượng và chi phí cố định | PM trợ lý hoàn phí |
