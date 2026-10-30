# React & Next.js AI Learning Academy

Học React với AI Agent đóng vai giảng viên: **16 tuần · 48 buổi · 96 giờ · 3 buổi/tuần · 2 giờ/buổi**. Đối tượng: beginner.

## Daily Plan & six Agent Skills

- [48-buổi Daily Plan](DAILY_PLAN.md) có lesson, bài tập, nguồn tài liệu và status.
- [Daily Progress](progress/README.md) có trạng thái từng ngày, điểm, phản hồi và thời gian thực tế.
- 6 skills: `plan-daily-learning`, `teach-lesson`, `review-assignment`, `conduct-exam`, `debug-coach`, `update-progress` (Codex ở `.agents/skills`, Antigravity ở `.agent/skills`).

## Bắt đầu
1. Clone repository và mở bằng VS Code/Codex hoặc Google Antigravity.
2. Đọc `AGENTS.md`, `curriculum/syllabus.json`, `progress/learning-state.json`.
3. Yêu cầu Agent: **"Bắt đầu buổi học tiếp theo theo AGENTS.md"**.
4. Hoàn thành bài tập bằng code; Agent review theo rubric và cập nhật tiến độ bằng `python scripts/learning_cli.py ...`.
5. Commit/push thay đổi về GitHub sau mỗi buổi (bảo đảm không đẩy secrets).

## Nguyên tắc
Agent là giảng viên, không làm bài thay học viên. Đánh giá dựa trên bằng chứng và yêu cầu giải thích. Chỉ khi đạt **75/100** mới được hoàn tất buổi học. Các buổi đánh giá tích hợp có deliverable riêng.

## Nội dung
React, JS, TypeScript, React Hooks, Zustand/Redux Toolkit, TanStack Query, Zod, React Hook Form, Next.js App Router, Material UI, Refine, testing, dashboard thực tế.

Đọc `LEARNING_PLAN.md` cho hướng dẫn chi tiết và `resources/references.md` cho nguồn học chính thức. `projects/final-project/README.md` mô tả bài cuối khóa.

> GitHub lưu dữ liệu bền vững sau commit/push; bản sửa chưa push sẽ không tự đồng bộ sang máy hoặc Agent khác.
