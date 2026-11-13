#!/usr/bin/env python3
"""Cold-storage controller simulator for Glacier Mint."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass


@dataclass
class Reading:
    hub: str
    temperature_c: float
    humidity_pct: float
    target_c: float


def load_readings(path: str) -> list[Reading]:
    readings = []
    with open(path, newline='', encoding='utf-8') as handle:
        for row in csv.DictReader(handle):
            readings.append(
                Reading(
                    hub=row['hub'],
                    temperature_c=float(row['temperature_c']),
                    humidity_pct=float(row['humidity_pct']),
                    target_c=float(row['target_c']),
                )
            )
    return readings


def correction(reading: Reading) -> float:
    drift = reading.temperature_c - reading.target_c
    humidity_penalty = max(0.0, reading.humidity_pct - 70.0) * 0.02
    return round(-1.6 * drift - humidity_penalty, 2)


def simulate(readings: list[Reading]) -> dict[str, float]:
    return {reading.hub: correction(reading) for reading in readings}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--readings', required=True)
    args = parser.parse_args()
    for hub, value in sorted(simulate(load_readings(args.readings)).items()):
        print(f'{hub}: {value:+.2f} C')


if __name__ == '__main__':
    main()
