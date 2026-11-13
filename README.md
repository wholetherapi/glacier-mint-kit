# Glacier Mint Launch Kit

Released reference implementation for the Glacier Mint launch kit.

Glacier Mint monitors cold-storage drift across regional hubs. The repository contains the chiller controller, the nightly reporting job, and the drift analysis used by the reliability team.

## Contents

- `src/chiller.py` - controller and simulator.
- `src/report.py` - nightly report generator.
- `data/readings.csv` - sample hub readings.
- `experiments/drift_analysis.md` - drift study.

## Running the simulator

    python src/chiller.py --readings data/readings.csv
