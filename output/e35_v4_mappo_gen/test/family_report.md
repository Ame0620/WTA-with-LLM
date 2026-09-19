# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_5x100_K10_s01.txt', 'dn_5x100_K10_s02.txt']) | policy: **mappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 20:26:23

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s01.txt` | 8157 | 0.7013 | n/a | 0.1544 | 80.6270 | 0.006 | 30.0 | 2436.3 | `da402f9edf9e` |
| `dn_5x100_K10_s02.txt` | 7616 | 0.6924 | n/a | 0.2478 | 78.3911 | 0.006 | 30.0 | 2343.0 | `a7a2f0a8a877` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6968 +- 0.0045 [worst 0.7013] | 0.7013 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2011 +- 0.0467 [worst 0.2478] | 0.2478 |
| ammo_efficiency | 79.5090 +- 1.1180 [worst 78.3911] | 78.3911 |
| latency_p50 | 0.0057 +- 0.0001 [worst 0.0058] | 0.0058 |
| latency_p90 | 0.0076 +- 0.0014 [worst 0.0089] | 0.0089 |
| shots_total | 30.0000 +- 0.0000 [worst 30.0000] | 30.0000 |
| destroyed_value | 2389.6333 +- 46.6667 [worst 2342.9667] | 2342.9667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
