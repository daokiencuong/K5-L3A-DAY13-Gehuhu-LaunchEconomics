# Rules

## AI và công cụ

- Lab không gọi model thật, không cần và không dùng API key.
- Được dùng trợ lý AI (ChatGPT, Claude, Gemini, Copilot, Cursor…) để giải thích khái niệm, gợi ý code và soát lỗi.
- Mọi con số trong hồ sơ phải do `src/lab13.py` của nhóm tính ra, hoặc tính tay có ghi cách tính. Không dùng AI để bịa số, nhãn lỗi hay kết quả duyệt chéo.
- Nhóm phải tự giải thích được: vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công, cách tính cỡ mẫu hiệu dụng khi chia theo cụm, và lý do của đề xuất cuối. Hội đồng và giảng viên có thể hỏi trực tiếp.
- Mỗi thành viên ghi công cụ AI đã dùng và cách tự kiểm tra trong báo cáo cá nhân `report/team/MSSV_HoTen.md`.

## Làm bài và liêm chính

- Không sao chép bài hoặc nhận bài làm thay.
- Ghi nguồn khi dùng code, dữ liệu hoặc tài liệu bên ngoài.
- Bài nhóm phải ghi rõ đóng góp của từng thành viên trong `TEAM.md`.
- Nhiệm vụ C: hai người gắn nhãn phải gắn độc lập, không trao đổi, trước khi so nhãn. Không sửa bộ nhãn độc lập sau khi đã so.
- Bài làm mẫu `docs/example.zip`: tự làm trước rồi mới mở để đối chiếu. Không nộp lại nội dung bài mẫu như bài của nhóm.
- Không sửa hai file dữ liệu `src/logix_runs.csv`, `src/logix_requests.csv`.
- Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Không dùng từ "production" trong hồ sơ.

## Secret và API key

- Lab chạy offline, không cần API key. Không commit API key, password hoặc file `.env`.
- Không commit `.venv/` hay thư mục giải nén bài mẫu `example/` (đã có trong `.gitignore`).

## Nộp muộn và lỗi kỹ thuật

- Deadline và gia hạn: xem [SUBMISSION.md](SUBMISSION.md#deadline-gmt7).
- Nếu gặp lỗi kỹ thuật (cài đặt, máy không chạy được Python), mô tả lỗi và đưa bằng chứng (lệnh đã chạy, output, ảnh chụp) vào mục 5 "Khó khăn và cách xử lý" của `report/team/group_report.md`.
- Không force-push, xóa commit hoặc sửa ngày commit. Bổ sung sau deadline dùng commit mới và ghi rõ thay đổi.
