#!/usr/bin/env python3
"""Nightly report generator for Glacier Mint."""

import csv
from collections import defaultdict
from pathlib import Path


def summarise(path: Path) -> dict[str, dict]:
    hubs: dict[str, list[float]] = defaultdict(list)
    with path.open(newline='', encoding='utf-8') as handle:
        for row in csv.DictReader(handle):
            hubs[row['hub']].append(float(row['temperature_c']))
    return {
        hub: {
            'samples': len(values),
            'min_c': min(values),
            'max_c': max(values),
            'mean_c': round(sum(values) / len(values), 2),
        }
        for hub, values in hubs.items()
    }


def main() -> None:
    import sys
    summary = summarise(Path(sys.argv[1]))
    for hub, entry in sorted(summary.items()):
        print(hub, entry)
