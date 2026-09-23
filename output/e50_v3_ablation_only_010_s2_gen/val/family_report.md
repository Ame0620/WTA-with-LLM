# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 02:00:55

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.7011 | n/a | 0.3178 | 82.9346 | 0.003 | 15.0 | 1241.4 | `313cff20896f` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6803 | n/a | 0.1812 | 91.7046 | 0.003 | 16.0 | 1470.2 | `b974c75b0029` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.7195 | n/a | 0.2622 | 88.5877 | 0.003 | 15.0 | 1335.2 | `c469b5b8c972` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.8430 | n/a | 0.5889 | 48.5049 | 0.004 | 15.0 | 722.7 | `9818e958d964` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7360 +- 0.0633 [worst 0.8430] | 0.8430 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3375 +- 0.1530 [worst 0.5889] | 0.5889 |
| ammo_efficiency | 77.9330 +- 17.2786 [worst 48.5049] | 48.5049 |
| latency_p50 | 0.0033 +- 0.0002 [worst 0.0036] | 0.0036 |
| latency_p90 | 0.0042 +- 0.0011 [worst 0.0061] | 0.0061 |
| shots_total | 15.2500 +- 0.4330 [worst 16.0000] | 16.0000 |
| destroyed_value | 1192.3917 +- 283.1062 [worst 722.7000] | 722.7000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
