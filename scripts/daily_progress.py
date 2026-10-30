#!/usr/bin/env python3
"""Daily session state controller; human/agent verified events only."""
import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DAILY = ROOT / "progress" / "daily"
HISTORY = ROOT / "progress" / "session-history.jsonl"
SYLLABUS = ROOT / "curriculum" / "syllabus.json"


def now():
    return datetime.now(timezone.utc).isoformat()


def find_session(lesson):
    syllabus = json.loads(SYLLABUS.read_text(encoding="utf-8"))
    match = next((x for x in syllabus["lessons"] if x["id"] == lesson), None)
    if not match:
        raise ValueError("Unknown lesson: " + lesson)
    return DAILY / ("week-%02d" % match["week"]) / (lesson + ".json")


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path, value):
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(path)


def event(lesson, action, detail):
    with HISTORY.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"timestamp": now(), "lesson": lesson, "action": action,
                            "detail": detail}, ensure_ascii=False) + "\n")


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status")
    for name in ("start", "log", "submit", "review"):
        p = sub.add_parser(name)
        p.add_argument("--lesson", required=True)
        if name == "log":
            p.add_argument("--minutes", type=int, required=True)
            p.add_argument("--note", required=True)
        if name == "submit":
            p.add_argument("--evidence", required=True)
        if name == "review":
            p.add_argument("--score", type=int, required=True)
            p.add_argument("--feedback", required=True)
            p.add_argument("--result", required=True, choices=["passed", "needs_revision"])
            p.add_argument("--report")
    args = parser.parse_args()
    summary = read(ROOT / "progress" / "learning-state.json")
    if args.command == "status":
        print("Current:", summary["current_lesson"], "| Complete:", len(summary["completed_lessons"]), "/48")
        if summary["current_lesson"]:
            print(json.dumps(read(find_session(summary["current_lesson"])), ensure_ascii=False, indent=2))
        return
    path = find_session(args.lesson)
    row = read(path)
    if args.lesson != summary["current_lesson"]:
        raise ValueError("Only current session may be updated: " + str(summary["current_lesson"]))
    if row["status"] == "passed":
        raise ValueError("Already completed")
    stamp = now()
    if args.command == "start":
        if row["status"] not in ("not_started", "in_progress", "needs_revision"):
            raise ValueError("Can't start from status " + row["status"])
        row["status"] = "in_progress"
        row["study_dates"].append(stamp)
    elif args.command == "log":
        if row["status"] not in ("in_progress", "needs_revision"):
            raise ValueError("Start first")
        if not 1 <= args.minutes <= 360 or not args.note.strip():
            raise ValueError("Invalid study minutes/note")
        row["actual_minutes"] += args.minutes
        row["feedback"].append({"at": stamp, "type": "study_note", "text": args.note})
    elif args.command == "submit":
        if row["status"] not in ("in_progress", "needs_revision") or not args.evidence.strip():
            raise ValueError("Start first and provide evidence")
        row["status"] = "submitted"
        row["evidence"].append({"at": stamp, "reference": args.evidence})
        row["attempts"].append({"submitted_at": stamp, "evidence": args.evidence})
    elif args.command == "review":
        if row["status"] != "submitted":
            raise ValueError("Submit evidence before reviewing")
        if not 0 <= args.score <= 100 or not args.feedback.strip():
            raise ValueError("Invalid score/feedback")
        if args.result == "passed":
            if args.score < 75 or row["actual_minutes"] <= 0 or not args.report:
                raise ValueError("Passing requires >=75, recorded study time and report")
            # Validate report and advance summary before touching daily state.
            subprocess.run([sys.executable, str(ROOT / "scripts" / "learning_cli.py"),
                            "complete", "--lesson", args.lesson, "--score", str(args.score),
                            "--minutes", str(row["actual_minutes"]), "--report", args.report],
                           check=True, cwd=ROOT)
            row["completed_at"] = stamp
        row["scores"].append({"at": stamp, "score": args.score, "result": args.result})
        row["feedback"].append({"at": stamp, "type": "instructor_review", "text": args.feedback})
        row["status"] = args.result
    write(path, row)
    event(args.lesson, args.command, {"status": row["status"]})
    print(args.lesson, row["status"], row["actual_minutes"], "minutes")


if __name__ == "__main__":
    main()
