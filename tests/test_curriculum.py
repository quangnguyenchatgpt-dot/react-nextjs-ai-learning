import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CurriculumTests(unittest.TestCase):
    def test_lesson_files_and_unique_ids(self):
        lessons = json.loads((ROOT / "curriculum/syllabus.json").read_text(encoding="utf-8"))["lessons"]
        self.assertEqual(len(lessons), 48)
        self.assertEqual(len({lesson["id"] for lesson in lessons}), 48)
        for lesson in lessons:
            self.assertTrue((ROOT / lesson["file"]).is_file(), lesson["id"])
            self.assertTrue(lesson["resource"].startswith("https://"))
            self.assertEqual(lesson["duration_minutes"], 120)

    def test_planned_hours(self):
        syllabus = json.loads((ROOT / "curriculum/syllabus.json").read_text(encoding="utf-8"))
        self.assertEqual(sum(x["duration_minutes"] for x in syllabus["lessons"]), 5760)


if __name__ == "__main__":
    unittest.main()
