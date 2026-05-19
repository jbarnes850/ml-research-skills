#!/usr/bin/env python3
"""Audit RL environment task metadata for quality-gate coverage.

Usage:
  python3 task_quality_audit.py --tasks tasks.jsonl
  python3 task_quality_audit.py --tasks tasks.json --out report.json
  python3 task_quality_audit.py --self-test

Input may be JSONL, a JSON list, or a JSON object with a "tasks" list.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path


REQUIRED_FIELDS = [
    "task_id",
    "split",
    "task_family",
    "capability_axis",
    "difficulty_band",
    "verifier_type",
    "source",
]

RECOMMENDED_FIELDS = [
    "horizon",
    "tool_count",
    "construction_mode",
    "public_status",
    "solvability_evidence",
    "reward_hack_controls",
]

HIGH_SEVERITY_CONTROLS = [
    "protected_evaluator",
    "hidden_or_recomputed_checks",
    "strict_fail_closed_parser",
]


def _load_tasks(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    if path.suffix == ".jsonl":
        return [json.loads(line) for line in text.splitlines() if line.strip()]
    data = json.loads(text)
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and isinstance(data.get("tasks"), list):
        return data["tasks"]
    raise ValueError("expected JSON list, JSON object with tasks list, or JSONL")


def _as_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _rate(count: int, total: int) -> float:
    return round(count / total, 4) if total else 0.0


def audit(tasks: list[dict]) -> dict:
    counters: dict[str, Counter] = defaultdict(Counter)
    missing_required = Counter()
    missing_recommended = Counter()
    blockers: list[dict] = []
    warnings: list[dict] = []

    for idx, task in enumerate(tasks):
        task_id = str(task.get("task_id", f"idx:{idx}"))
        for field in REQUIRED_FIELDS:
            if task.get(field) in (None, "", []):
                missing_required[field] += 1
        for field in RECOMMENDED_FIELDS:
            if task.get(field) in (None, "", []):
                missing_recommended[field] += 1

        for field in [
            "split",
            "task_family",
            "capability_axis",
            "difficulty_band",
            "verifier_type",
            "source",
            "construction_mode",
            "public_status",
        ]:
            value = task.get(field)
            if value not in (None, "", []):
                for item in _as_list(value):
                    counters[field][str(item)] += 1

        controls = set(str(x) for x in _as_list(task.get("reward_hack_controls")))
        missing_controls = [c for c in HIGH_SEVERITY_CONTROLS if c not in controls]
        if missing_controls:
            warnings.append(
                {
                    "task_id": task_id,
                    "type": "missing_high_severity_reward_hack_controls",
                    "missing": missing_controls,
                }
            )

        if task.get("split") in {"eval", "private_eval"} and task.get("public_status") == "public":
            warnings.append(
                {
                    "task_id": task_id,
                    "type": "public_eval_task",
                    "detail": "public eval tasks need contamination/private-refresh mitigation",
                }
            )

        if task.get("solvability_evidence") in (None, "", [], "none", "unknown"):
            blockers.append({"task_id": task_id, "type": "missing_solvability_evidence"})

        if task.get("verifier_type") in {"llm_judge", "learned_reward"} and not task.get(
            "verifier_calibration"
        ):
            blockers.append({"task_id": task_id, "type": "uncalibrated_judge_or_reward"})

    total = len(tasks)
    dominance = []
    for field in ["task_family", "difficulty_band", "verifier_type", "source"]:
        if counters[field]:
            name, count = counters[field].most_common(1)[0]
            if _rate(count, total) > 0.6:
                dominance.append({"field": field, "value": name, "rate": _rate(count, total)})

    report = {
        "total_tasks": total,
        "missing_required": dict(missing_required),
        "missing_recommended": dict(missing_recommended),
        "distributions": {k: dict(v) for k, v in sorted(counters.items())},
        "dominance_warnings": dominance,
        "warnings": warnings,
        "blockers": blockers
        + [
            {"type": "missing_required_fields", "fields": dict(missing_required)}
            for _ in [0]
            if missing_required
        ],
        "pass": not missing_required and not blockers,
    }
    return report


def _self_test() -> int:
    tasks = [
        {
            "task_id": "t1",
            "split": "train",
            "task_family": "support_refund",
            "capability_axis": "domain_reasoning",
            "difficulty_band": "medium",
            "verifier_type": "executable",
            "source": "expert",
            "horizon": 6,
            "tool_count": 4,
            "construction_mode": "handcrafted",
            "public_status": "private",
            "solvability_evidence": "expert_solution",
            "reward_hack_controls": [
                "protected_evaluator",
                "hidden_or_recomputed_checks",
                "strict_fail_closed_parser",
            ],
        }
    ]
    report = audit(tasks)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["pass"] else 1


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Audit RL task metadata quality gates")
    parser.add_argument("--tasks", type=Path, help="JSON/JSONL task metadata file")
    parser.add_argument("--out", type=Path, help="Optional JSON report path")
    parser.add_argument("--self-test", action="store_true", help="Run built-in smoke test")
    args = parser.parse_args(argv)

    if args.self_test:
        return _self_test()
    if not args.tasks:
        parser.error("--tasks is required unless --self-test is set")

    report = audit(_load_tasks(args.tasks))
    rendered = json.dumps(report, indent=2, sort_keys=True)
    if args.out:
        args.out.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0 if report["pass"] else 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
