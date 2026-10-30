#!/usr/bin/env python3
"""Validate and update local course progress. Standard library only."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "progress" / "learning-state.json"
HISTORY = ROOT / "progress" / "session-history.jsonl"
SYLLABUS = ROOT / "curriculum" / "syllabus.json"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def atomic_json(path, data):
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def validate():
    syllabus = read_json(SYLLABUS)
    state = read_json(STATE)
    lessons = [row["id"] for row in syllabus["lessons"]]
    assert len(lessons) == 48 and len(set(lessons)) == 48, "Curriculum must have 48 unique lessons"
    assert state["total_lessons"] == len(lessons), "Incorrect total_lessons"
    completed = state["completed_lessons"]
    assert len(set(completed)) == len(completed), "Duplicate completed lessons"
    assert all(item in lessons for item in completed), "Unknown completed lesson"
    next_id = next((item for item in lessons if item not in completed), None)
    assert state["current_lesson"] == next_id, "current_lesson is inconsistent"
    assert state["total_study_minutes"] >= 0, "Negative study duration"
    for lesson_id in completed:
        assert (ROOT / "assessments" / "reports" / (lesson_id + ".md")).is_file(), "Missing report for " + lesson_id
    return state


def complete(args):
    state = validate()
    syllabus = read_json(SYLLABUS)
    ids = [row["id"] for row in syllabus["lessons"]]
    if args.lesson != state["current_lesson"]:
        raise ValueError("Complete only current lesson: " + str(state["current_lesson"]))
    if not 75 <= args.score <= 100:
        raise ValueError("A verified passing score between 75 and 100 is required")
    if not 1 <= args.minutes <= 360:
        raise ValueError("Study duration must be 1-360 minutes")
    expected = ROOT / "assessments" / "reports" / (args.lesson + ".md")
    report = (ROOT / args.report).resolve()
    if report != expected.resolve() or not report.is_file() or len(report.read_text(encoding="utf-8").strip()) < 100:
        raise ValueError("A substantive report at assessments/reports/<lesson>.md is required")
    content = report.read_text(encoding="utf-8")
    for marker in ("Functionality:", "Understanding:", "Code quality:", "Tests:", "Documentation:", "Mandatory criteria:"):
        if marker not in content:
            raise ValueError("Report missing criterion: " + marker)
    now = datetime.now(timezone.utc).isoformat()
    record = {"date": now, "lesson": args.lesson, "score": args.score, "minutes": args.minutes, "report": args.report}
    state["completed_lessons"].append(args.lesson)
    state["total_study_minutes"] += args.minutes
    state["last_assessment"] = record
    state["updated_at"] = now
    state["current_lesson"] = ids[len(state["completed_lessons"])] if len(state["completed_lessons"]) < len(ids) else None
    # Append audit record before writing snapshot; if interrupted, inspect git diff before retry.
    with HISTORY.open("a", encoding="utf-8") as out:
        out.write(json.dumps(record, ensure_ascii=False) + "\n")
    atomic_json(STATE, state)
    validate()
    print("Completed:", args.lesson, "Next:", state["current_lesson"])


def main():
    parser = argparse.ArgumentParser(description="React academy progress CLI")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status")
    sub.add_parser("validate")
    done = sub.add_parser("complete")
    done.add_argument("--lesson", required=True)
    done.add_argument("--score", required=True, type=int)
    done.add_argument("--minutes", required=True, type=int)
    done.add_argument("--report", required=True)
    args = parser.parse_args()
    if args.command == "complete":
        complete(args)
    else:
        state = validate()
        if args.command == "status":
            print(json.dumps(state, ensure_ascii=False, indent=2))
        else:
            print("Progress valid:", len(state["completed_lessons"]), "/48")


if __name__ == "__main__":
    main()
