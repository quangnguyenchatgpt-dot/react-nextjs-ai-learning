---
name: plan-daily-learning
description: Create and conduct the next personalized 120-minute lesson plan, tracking attempts and daily learning notes.
---
# Plan Daily Learning

1. Read AGENTS.md, DAILY_PLAN.md, curriculum/syllabus.json, current progress summary and corresponding progress/daily/Wxx record.
2. Identify next unpassed lesson, weak concepts, outstanding feedback; never select a later lesson by assumption.
3. Deliver goals, prerequisite check, official references and 15/25/60/20 minute agenda in Vietnamese.
4. Start via `python scripts/daily_progress.py start --lesson WxxDyy`, only after learner actually starts.
5. Guide learner practice via layered hints; log actual time via `log`; never assume 120 minutes occurred.
6. Receive evidence via `submit`; review using the assessment rubric and an instructor report; call `review` to store grade and advance the course only on verified pass.
7. Conclude with learned concepts, mistakes, unfinished work, next action, and reminder to commit/push. Preserve previous history.
