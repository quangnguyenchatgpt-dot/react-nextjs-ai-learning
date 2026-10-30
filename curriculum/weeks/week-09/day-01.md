# W09D01 — Pagination and resilient APIs

**Tuần 9, buổi 1 · 120 phút · Mức beginner**

## Mục tiêu học tập
- Giải thích được các khái niệm: Query params, dependent queries, retries.
- Tự triển khai bài tập "Build paginated Jobs table" và trình bày cách giải.
- Xác minh yêu cầu và nêu ít nhất một hạn chế/edge case.

## Tài liệu bắt buộc
- https://tanstack.com/query/latest/docs/framework/react/guides/paginated-queries
- [Thư viện tài liệu chính thức](../../../resources/references.md)

## Lesson plan (120 phút)
1. **15 phút ôn tập:** Agent hỏi 2-3 câu về bài trước; buổi đầu kiểm tra môi trường học và kiến thức nền.
2. **25 phút lý thuyết:** Agent chia nhỏ chủ đề "Query params, dependent queries, retries", có minh họa tối thiểu và câu hỏi kiểm tra.
3. **60 phút thực hành:** Học viên tự code "Build paginated Jobs table"; Agent hướng dẫn theo 3 mức gợi ý, không làm hộ.
4. **20 phút tổng kết:** Demo, code review, tự giải thích, báo cáo điểm và kế hoạch sửa lỗi.

## Assignment
**Task:** Build paginated Jobs table.

**Deliverables:** Source code trong thư mục `projects/` tương ứng; README ngắn về cách chạy; ảnh/chứng cứ terminal hoặc test nếu phù hợp; giải thích 3 quyết định kỹ thuật.

**Acceptance criteria:**
- Triển khai đúng hành vi bài tập và demo được.
- Code rõ ràng, có type khi dùng TypeScript.
- Có xử lý trường hợp đầu vào không hợp lệ hoặc empty/error khi phù hợp.
- Giải thích được tại sao dùng khái niệm vừa học.

## Questions & reflection
- Query params, dependent queries, retries giải quyết vấn đề gì?
- Cách làm của bạn khác với giải pháp thay thế nào?
- Nếu yêu cầu tăng gấp đôi độ phức tạp, bạn sẽ refactor ở đâu?

## Assessment
Dùng `assessments/rubrics/default.md`, chấm theo thực tế, pass >=75 và chức năng bắt buộc hoàn tất. Lưu `assessments/reports/W09D01.md`, sau đó mới chạy CLI `complete`. Nếu chưa đạt, đưa gợi ý và luyện tập tương tự.
