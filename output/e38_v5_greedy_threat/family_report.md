# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **greedy_threat** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 19:59:50

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.8968 | 2.5670 | 0.8324 | 12.0203 | 0.794 | 70.0 | 842.0 | `c571b85199be` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.8833 | 1.9409 | 0.8543 | 12.6937 | 0.813 | 70.0 | 889.0 | `1057d9574dcb` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.8900 +- 0.0068 [worst 0.8968] | 0.8968 |
| gap_mean | 2.2540 +- 0.3130 [worst 2.5670] | 2.5670 |
| invalid_engagement_rate | 0.8433 +- 0.0110 [worst 0.8543] | 0.8543 |
| ammo_efficiency | 12.3570 +- 0.3367 [worst 12.0203] | 12.0203 |
| latency_p50 | 0.8039 +- 0.0094 [worst 0.8133] | 0.8133 |
| latency_p90 | 1.0929 +- 0.2048 [worst 1.2978] | 1.2978 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 865.5000 +- 23.5000 [worst 842.0000] | 842.0000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
