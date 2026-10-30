# Competency-based Learning Path

Learning Path complements (does not replace) `curriculum/syllabus.json`. Progress data lives only in `progress/` and is never edited by this file.

## Order
1. **Web & TypeScript Foundations** — weeks 1–2 (W01D01–W02D03)
2. **React Core** — weeks 3–6 (W03D01–W06D03)
3. **React Advanced & Forms** — weeks 7–10 (W07D01–W10D03)
4. **Next.js & UI** — weeks 11–14 (W11D01–W14D03)
5. **Refine, Testing & Capstone** — weeks 15–16 (W15D01–W16D03)

## Progression
- All 48 lessons have an explicit prerequisite chain and linked Lab in `learning-path.json`.
- Prior lesson must be **passed** according to authoritative progress records before moving forward.
- At milestones, review practical implementation, tests, explanations and skill evidence.
- Pass requires score >=75/100 plus mandatory functional criteria; never infer pass from elapsed time.
- Weaknesses trigger review Lab / targeted practice, but cannot skip required lessons.
- Curriculum and Learning Path are plans; session state and scores belong to progress files.

## Teaching rhythm
10m coding recall + 24m theory + 16m guided coding + 50m Lab + 10m debug/testing + 10m evidence-based assessment.

## Check structural alignment
`python scripts/validate_learning_path.py`
