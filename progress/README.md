# Daily progress / nhật ký học tập

- `daily/week-XX/WXXDYY.json`: tiến độ chi tiết cho từng buổi, bao gồm trạng thái, thời gian thực tế, ngày học, điểm, phản hồi, blocker và việc tiếp theo.
- `learning-state.json`: trạng thái tổng hợp, hiện chỉ tự tăng completed qua `learning_cli.py complete`.
- `session-history.jsonl`: audit log; không xóa hoặc ghi đè lịch sử.
- `DAILY_PLAN.md`: lịch học 48 buổi, không ép theo ngày trong tuần.

## CLI
```powershell
python scripts/daily_progress.py status
python scripts/daily_progress.py start --lesson W01D01
python scripts/daily_progress.py log --lesson W01D01 --minutes 45 --note "Đã học semantic tags"
python scripts/daily_progress.py submit --lesson W01D01 --evidence "projects/react-foundation/profile/index.html"
python scripts/daily_progress.py review --lesson W01D01 --score 68 --feedback "Cần sửa accessibility" --result needs_revision
# Chỉ sau khi có báo cáo đúng rubric và đạt điểm:
python scripts/daily_progress.py review --lesson W01D01 --score 80 --feedback "Đã kiểm thử" --result passed --report assessments/reports/W01D01.md
```

**Quy tắc:** không chấm điểm khống, không ghi một buổi đã hoàn thành khi thiếu bằng chứng. `review passed` gọi `learning_cli.py complete` để cập nhật summary; mỗi lần cập nhật cần commit/push để đồng bộ máy/Agent.
