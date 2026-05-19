#!/usr/bin/env python3
"""Audit seed mix distributions from a manifest.

Usage:
  python3 seed_mix_audit.py --manifest path/to/manifest.json --split train|eval|all [--out report.json]
"""

import argparse
import json
import os
from collections import Counter, defaultdict


def _load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _iter_seed_files(manifest, manifest_path, split):
    if split == "all":
        splits = ["train", "eval"]
    else:
        splits = [split]
    for sp in splits:
        for rel in manifest.get(sp, []):
            yield sp, os.path.join(os.path.dirname(manifest_path), rel)


def _has_injection(item):
    inj = item.get("injection_id")
    return inj is not None


def _count_surface_injection(items):
    if not items:
        return False
    return any(_has_injection(x) for x in items)


def _collect_trust(items, counter):
    for item in items or []:
        tier = item.get("trust_tier")
        source = item.get("source")
        if tier is not None:
            counter["trust_tier"][tier] += 1
        if source is not None:
            counter["source"][source] += 1


def _collect_objectives(seed, counter):
    obj = seed.get("attack_graph", {}).get("objectives") or []
    counter["objective_length"][len(obj)] += 1
    for o in obj:
        counter["objectives"][o] += 1


def _collect_max_steps(seed, counter):
    ms = seed.get("max_steps")
    if ms is not None:
        counter["max_steps"][str(ms)] += 1


def _collect_injection_meta(seed, counter):
    payloads = seed.get("prompt_injection_payloads") or []
    for p in payloads:
        it = p.get("injection_type")
        obj = p.get("objective")
        src = p.get("source")
        if it is not None:
            counter["injection_type"][it] += 1
        if obj is not None:
            counter["injection_objective"][obj] += 1
        if src is not None:
            counter["injection_source"][src] += 1


def main(args):
    manifest = _load_json(args.manifest)

    totals = Counter()
    surface_injection = Counter()
    counters = defaultdict(Counter)

    for split, seed_path in _iter_seed_files(manifest, args.manifest, args.split):
        seed = _load_json(seed_path)
        totals["seeds"] += 1
        totals[f"seeds_{split}"] += 1

        emails = seed.get("emails") or []
        alerts = seed.get("alerts") or []
        process_events = seed.get("process_events") or []

        if _count_surface_injection(emails):
            surface_injection["email"] += 1
        if _count_surface_injection(alerts):
            surface_injection["alert"] += 1
        if _count_surface_injection(process_events):
            surface_injection["log"] += 1

        _collect_trust(emails, counters)
        _collect_trust(alerts, counters)
        _collect_trust(process_events, counters)
        _collect_objectives(seed, counters)
        _collect_max_steps(seed, counters)
        _collect_injection_meta(seed, counters)

    report = {
        "totals": dict(totals),
        "surface_injection_counts": dict(surface_injection),
        "surface_injection_rates": {
            k: (surface_injection[k] / totals["seeds"] if totals["seeds"] else 0.0)
            for k in ["email", "alert", "log"]
        },
        "trust_tier": dict(counters["trust_tier"]),
        "source": dict(counters["source"]),
        "objective_length": dict(counters["objective_length"]),
        "objectives": dict(counters["objectives"]),
        "max_steps": dict(counters["max_steps"]),
        "injection_type": dict(counters["injection_type"]),
        "injection_objective": dict(counters["injection_objective"]),
        "injection_source": dict(counters["injection_source"]),
    }

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, sort_keys=True)
    else:
        print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audit seed mix distributions")
    parser.add_argument("--manifest", required=True, help="Path to manifest.json")
    parser.add_argument("--split", default="all", choices=["train", "eval", "all"])
    parser.add_argument("--out", help="Optional JSON output path")
    args = parser.parse_args()
    main(args)
