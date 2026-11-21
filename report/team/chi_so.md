# Chỉ số event và rủi ro kinh tế · Nhiệm vụ E

Các số tính thử đến từ dữ liệu **simulated** của lab và `src/lab13.py`. Đây là mô tả đợt chạy thử không có đối chứng; không kết luận trợ lý đã làm tăng chỉ số. Các event, ngưỡng và hành động dưới đây là đặc tả đề xuất cho pilot, chưa phải hệ thống đã triển khai.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức và mẫu số | Tính thử trên dữ liệu lab |
| --- | --- | --- | --- |
| Chính | Đóng trong 24 giờ và không mở lại trong 7 ngày | Request đóng đầu không quá 24h từ created_at, không mở lại trong 7 ngày sau đóng / tổng request đủ điều kiện, đủ theo dõi; báo theo arm ban đầu, kể cả không mở trợ lý | **994/1.200 = 82,83%** từ hai cột cờ của CSV [simulated] |
| Dùng | Tỉ lệ nhân viên sửa hoặc bỏ gợi ý | Request được xem lại có quyết định cuối sua/bo / request có quyết định cuối giu/sua/bo; đếm request duy nhất | **48/177 = 27,12%** [simulated] |
| An toàn | Tỉ lệ mở lại trong 7 ngày | Request mở lại trong 7 ngày sau lần đóng đầu / request đã đóng đủ 7 ngày theo dõi; báo riêng từng arm | **51/1.200 = 4,25%** theo cờ CSV [simulated]; pilot dùng mẫu số đã trưởng thành |
| Dùng bổ sung | Tỉ lệ yêu cầu can thiệp có gợi ý được hiển thị | Request đủ điều kiện ở arm can thiệp có agent_suggestion_shown / mọi request đủ điều kiện của arm can thiệp | Chưa có event/arm trong CSV; đo trong pilot |
| An toàn bổ sung | Tỉ lệ hoàn sai tiền qua kiểm toán mẫu | Request kiểm toán có amount_paid khác amount_expected / tổng request được kiểm toán; giữ số tiền lệch và phiên bản bảng giá | Chưa có kiểm toán trong CSV; đo hằng tuần |

Trong CSV, các cờ đã được cho sẵn nên tính thử dùng toàn bộ 1.200 yêu cầu; không suy ra ngày tạo/đóng thật từ các cờ. Trong pilot, chỉ số chính chỉ phân tích cohort 299 request đầu tiên của từng nhân viên ở giai đoạn 50% theo `pilot_plan.yaml`. Request không đóng trong 24h là không đạt; chờ tối thiểu 8 ngày từ tạo để mọi request có cùng cơ hội đóng 24h rồi theo dõi 7 ngày sau đóng. Mẫu số bằng 0 báo “chưa đo được”, không ghi 0%.

## Danh sách event đề xuất cho pilot

Mọi event có **event_id, event_time, trace_id, request_id**; event_time lưu ISO 8601 có múi giờ, đồng hồ đồng bộ. Một request giữ trace_id gốc, mỗi lần chạy có run_id để nối mọi lần thử; event_id chống ghi trùng. Gán arm và staff_id theo danh sách phân nhóm đã khoá; giữ nguyên arm khi nhân viên không sử dụng trợ lý. Các trường chung vẫn ghi rõ trace_id trong bảng để kiểm tra từng dòng.

| Event | Ai tạo | Thuộc tính chính ngoài event_id/event_time | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Hệ thống ticket | `trace_id`, `request_id`, `created_at`, `loai`, `order_id`, `refund_entitlement_id`, `input_type`, `so_tien`, `staff_id`, `arm`, `eligible`, `eligibility_reason`, `rollout_stage` | Khi tạo và định tuyến yêu cầu |
| `assistant_accessed` | Cổng quyền truy cập | `trace_id`, `request_id`, `staff_id`, `arm`, `access_allowed` | Mỗi lần mở trợ lý, kể cả bị chặn |
| `agent_run_completed` | Agent | `trace_id`, `request_id`, `run_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `tariff_version_used` | Sau mọi lượt chạy, kể cả lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `trace_id`, `request_id`, `run_id`, `staff_id`, `so_tien_de_xuat` | Khi gợi ý thực sự hiện ra |
| `staff_review_decision` | Giao diện nhân viên | `trace_id`, `request_id`, `staff_id`, `quyet_dinh` (giu/sua/bo), `is_final`, `phut_xem_lai` đo thật | Khi xác nhận quyết định xem lại |
| `staff_rework_completed` | Giao diện nhân viên | `trace_id`, `request_id`, `staff_id`, `phut_lam_lai` đo thật, `ly_do` | Khi xử lý làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | `trace_id`, `request_id`, `order_id`, `refund_entitlement_id`, `refund_id`, `idempotency_key`, `so_tien`, `ket_qua` (ok/loi), `tariff_version_used` | Mọi lần thử ghi sổ |
| `customer_message_sent` | Dịch vụ thông báo | `trace_id`, `request_id`, `refund_id`, `status` (refunded/pending/handoff), `channel`, `amount_explained` | Sau khi gửi thông báo cho khách |
| `order_id_submitted` | Giao diện nhập mã | `trace_id`, `request_id`, `id_type` (tracking/marketplace/unknown), `expected_id_type` (tracking), `submission_attempt` | Mỗi lần gửi mã; mẫu số đếm request duy nhất |
| `input_validation_failed` | Bộ kiểm tra đầu vào | `trace_id`, `request_id`, `input_type`, `reason` (gồm wrong_order_id_type), `validation_attempt` | Khi mã/tài khoản nhập vào không hợp lệ |
| `request_data_checked` | Dịch vụ tra cứu | `trace_id`, `request_id`, `missing_foreign_leg_data`, `missing_fields`, `lookup_status` | Sau kiểm tra dữ liệu, trước quyết định hoàn |
| `refund_decision` | Agent | `trace_id`, `request_id`, `run_id`, `decision` (refund/deny/handoff), `reason`, `amount_proposed` | Trước khi ghi sổ hoặc chuyển nhân viên |
| `handoff_to_staff` | Agent | `trace_id`, `request_id`, `reason`, `tom_tat`, `handoff_at` | Khi chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | `trace_id`, `request_id`, `closed_at`, `assistant_outcome` (thanh_cong/lam_lai/chuyen_nhan_vien), `resolution` (trạng thái xử lý ticket), `closed_by` | Mỗi lần đóng; chỉ số dùng lần đóng đầu |
| `ticket_reopened` | Hệ thống ticket | `trace_id`, `request_id`, `reopened_at`, `reason` (gồm amount_dispute), `related_closed_at` | Khi mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | `trace_id`, `request_id`, `amount_paid`, `amount_expected`, `amount_correct`, `tariff_version_used`, `tariff_version_expected`, `weight_kg`, `audit_reason` | Hằng tuần khi kiểm tra mẫu hoặc kiểm tra tranh chấp |

**Quy tắc nối và đếm:** nối request bằng request_id/trace_id; nối lượt chạy bằng run_id; nối tiền với thông báo bằng refund_id. Một quyền lợi hoàn được nhận diện bởi order_id + refund_entitlement_id, để không nhầm hai khoản hoàn hợp lệ thành hoàn trùng. Các lần thử lại phải dùng cùng idempotency_key. Lấy amount_paid từ sổ cái, amount_expected từ chính sách/bảng giá đúng ngày hiệu lực; amount_correct là kết quả so hai số đó.

| Phép đo hoặc phát hiện | Event và quy tắc |
| --- | --- |
| Chỉ số chính | refund_request_created (eligible, arm, created_at) + ticket_closed lần đầu + ticket_reopened; khử trùng request, chờ đủ cửa sổ 24h + 7 ngày; không loại ca không mở trợ lý khỏi arm can thiệp |
| Sửa/bỏ gợi ý | staff_review_decision có is_final=true; đếm một request mỗi tuần tạo cohort, không đếm mỗi lượt click |
| Mở lại 7 ngày | ticket_closed + ticket_reopened; đếm tối đa một lần mỗi request, chỉ mẫu đã đủ 7 ngày sau đóng |
| Mức dùng và truy cập sai nhánh | refund_request_created + agent_suggestion_shown; assistant_accessed của arm đối chứng hoặc access_allowed=false để rà spillover |
| Sai tiền, lỗi ngầm ca 17 | audit_sample_checked; kiểm ngẫu nhiên 100 đơn dưới 2 kg/tuần (ít hơn thì kiểm toàn bộ), cảnh báo khi ít nhất 1% mẫu sai tiền/phiên bản |
| Nhập sai mã ca 9 | Request có input_validation_failed(reason=wrong_order_id_type) / request có order_id_submitted(expected_id_type=tracking); mỗi request đếm tối đa một lần trong ngày, cảnh báo khi trên 2% mỗi ngày |
| Báo hoàn khi ghi sổ lỗi ca 7 | customer_message_sent(status=refunded) không có refund_ledger_write(ket_qua=ok) cùng refund_id/trace_id; đối soát mỗi giờ, cảnh báo từ 1 ca |
| Hiểu nhầm số tiền ca 18 | ticket_reopened(reason=amount_dispute) + audit_sample_checked(amount_correct=true); rà hằng tuần, từ 1 ca thì kiểm mẫu giải thích phép tính |
| Thiếu dữ liệu ca 4 | request_data_checked(missing_foreign_leg_data=true) phải có handoff_to_staff; cảnh báo từ 1 ca thiếu handoff hoặc vẫn có refund_decision(decision=refund), kiểm hằng ngày |
| Hoàn trùng ca 20 | Hai refund_id khác nhau cùng order_id + refund_entitlement_id có ledger ket_qua=ok; cảnh báo ngay và áp dụng luật dừng, không đợi phản ánh khách |

Trường assistant_outcome ghi kết quả của trợ lý; ca lam_lai hoặc chuyen_nhan_vien không trở thành thành công của trợ lý chỉ vì nhân viên xử lý xong ticket.

Đối soát hằng ngày việc thiếu event/trace_id, trùng event_id và timestamp sai thứ tự; không kết luận chỉ số khi log không đủ. Tỷ lệ dùng chưa thể tính chỉ từ số lần chạy vì một request có thể có nhiều run hoặc không mở trợ lý. Chi phí lấy token/tool của mọi run kể cả lỗi, cộng phút xem lại/làm lại thực đo; định nghĩa tử số/mẫu số và phần cố định nằm trong `pilot_plan.yaml`.

## E2 · Rủi ro kinh tế

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | CPS tăng **51,8% lên 6.787 đ/việc [simulated]** | Tỉ lệ làm lại theo tuần vượt 7%; đợt chạy thử trong phạm vi là 48/982 = 4,9% [simulated] | Thu hẹp về noi_dia, rà 20 trace làm lại và giữ rollout; thay can thiệp thì kết thúc đợt so sánh hiện tại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | **11.743 đ/việc (0,98×)** nếu làm lại 9 phút; **12.415 đ/việc (1,03×)** với trung bình 15,3 phút [simulated] | Tỉ lệ request được xem lại vẫn trên 50% cuối bước 25% | Trưởng nhóm CSKH chỉ giảm xem lại theo bậc sau khi sửa/bỏ dưới 15% và kiểm toán không thấy sai tiền; giữ kiểm toán mẫu; thay can thiệp phải đăng ký lại đợt đánh giá | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu/tháng cộng **1.185 đ/việc** ở 45.000 yêu cầu, hoặc **2.370 đ/việc** nếu còn nửa khối lượng [simulated] | Số việc thành công theo tuần dưới 50% kế hoạch; một nhân viên chưa đủ 299 ca trong cửa sổ chính | Không Go do thiếu mẫu; PM đề nghị Giám đốc vận hành gia hạn hai nhánh cùng thời gian, chờ đủ theo dõi; rà giả định volume và chi phí cố định | PM trợ lý hoàn phí |

Các ngưỡng 7%, 50%, 15% và hành động là **đề xuất kế hoạch**, không phải số đo mới. Các giá trị chi phí được đối chiếu bảng A–B; ngưỡng 8.000 đ/việc trong luật dừng áp dụng chi phí biến đổi, còn cố định và nhân viên làm thay phải được báo riêng để hội đồng xem tổng chi phí hệ thống.
