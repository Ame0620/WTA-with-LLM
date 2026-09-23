# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:55:10

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.6150 | n/a | 0.1292 | 98.8275 | 0.003 | 16.0 | 1599.3 | `9adb58dfa100` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6510 | n/a | 0.1686 | 93.7783 | 0.003 | 17.0 | 1604.9 | `6f1263690713` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6736 | n/a | 0.1187 | 96.3212 | 0.004 | 16.0 | 1553.6 | `1c83f6a8b72a` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6871 | n/a | 0.1958 | 89.3577 | 0.003 | 16.0 | 1440.6 | `8bc091d8a8bd` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6567 +- 0.0273 [worst 0.6871] | 0.6871 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1531 +- 0.0309 [worst 0.1958] | 0.1958 |
| ammo_efficiency | 94.5712 +- 3.4995 [worst 89.3577] | 89.3577 |
| latency_p50 | 0.0032 +- 0.0003 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0042 +- 0.0013 [worst 0.0063] | 0.0063 |
| shots_total | 16.2500 +- 0.4330 [worst 17.0000] | 17.0000 |
| destroyed_value | 1549.6083 +- 66.0027 [worst 1440.6000] | 1440.6000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
