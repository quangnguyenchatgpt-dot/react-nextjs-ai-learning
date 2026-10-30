import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

class TeachingModelTests(unittest.TestCase):
    def test_schedule(self):
        sy = json.loads((ROOT / "curriculum/syllabus.json").read_text(encoding="utf-8"))
        schedule = sy["pedagogy"]["schedule"]
        self.assertEqual(sum(schedule.values()), 120)
        self.assertEqual(schedule["theory"], 24)
        self.assertEqual(sum(v for k,v in schedule.items() if k != "theory"), 96)
    def test_all_labs_and_skills(self):
        sy=json.loads((ROOT/"curriculum/syllabus.json").read_text(encoding="utf-8"))
        for row in sy["lessons"]:
            lab=ROOT/"labs"/f'week-{row["week"]:02d}'/f'LAB-{row["id"]}'/"README.md"
            self.assertTrue(lab.is_file(),str(lab))
        for name in ("plan-daily-learning","teach-lesson","review-assignment","conduct-exam","debug-coach","update-progress"):
            a=(ROOT/".agent"/"skills"/name/"SKILL.md").read_text(encoding="utf-8")
            b=(ROOT/".agents"/"skills"/name/"SKILL.md").read_text(encoding="utf-8")
            self.assertEqual(a,b)
