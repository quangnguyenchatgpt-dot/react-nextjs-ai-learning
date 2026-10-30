import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

class DailyPlanTests(unittest.TestCase):
    def test_daily_records(self):
        syllabus = json.loads((ROOT / "curriculum/syllabus.json").read_text(encoding="utf-8"))
        self.assertEqual(len(syllabus["lessons"]), 48)
        for lesson in syllabus["lessons"]:
            file = ROOT / "progress/daily" / ("week-%02d" % lesson["week"]) / (lesson["id"] + ".json")
            rec = json.loads(file.read_text(encoding="utf-8"))
            self.assertEqual(rec["lesson_id"], lesson["id"])
            self.assertIn(rec["status"], {"not_started", "in_progress", "submitted", "passed", "needs_revision"})
            self.assertGreaterEqual(rec["actual_minutes"], 0)

    def test_six_skills(self):
        names = ["plan-daily-learning", "teach-lesson", "review-assignment", "conduct-exam",
                 "debug-coach", "update-progress"]
        for base in (".agent/skills", ".agents/skills"):
            for name in names:
                self.assertTrue((ROOT / base / name / "SKILL.md").is_file())
