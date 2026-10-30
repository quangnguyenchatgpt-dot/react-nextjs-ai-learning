#!/usr/bin/env python3
"""Validate the machine-readable learning path against curriculum and Lab paths."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def validate():
    path = json.loads((ROOT/"learning-path/learning-path.json").read_text(encoding="utf-8"))
    curriculum = json.loads((ROOT/"curriculum/syllabus.json").read_text(encoding="utf-8"))
    lessons = path["lessons"]
    ids = [x["id"] for x in curriculum["lessons"]]
    assert len(ids) == len(lessons) == 48
    assert [x["id"] for x in lessons] == ids
    assert sum(x["weeks"][1]-x["weeks"][0]+1 for x in path["phases"]) == 16
    assert path["theory_percent"] == 20 and path["practice_percent"] == 80
    phase_ids = {p["id"] for p in path["phases"]}
    for index, lesson in enumerate(lessons):
        assert lesson["phase"] in phase_ids
        assert lesson["prerequisites"] == ([ids[index-1]] if index else [])
        assert (ROOT/lesson["lab"]).is_file(), lesson["lab"]
    for phase in path["phases"]:
        assert phase["start"] in ids and phase["end"] in ids and phase["milestone"] in ids
    print("Learning Path valid: 5 phases, 48 lessons, linked Labs")

if __name__ == "__main__":
    validate()
