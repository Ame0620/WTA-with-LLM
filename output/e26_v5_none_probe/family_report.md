# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **none** | seeds: 3 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 16:12:01

## Per-instance metrics (mean +- std over 3 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 1.0000 | n/a | 0.0000 | n/a | 0.000 | 0.0 | 0.0 | `92c1da1ce148` |
| `dn_10x100_K10_s02.txt` | 7616 | 1.0000 | n/a | 0.0000 | n/a | 0.000 | 0.0 | 0.0 | `4944b2839576` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 1.0000 +- 0.0000 [worst 1.0000] | 1.0000 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| ammo_efficiency | n/a | n/a |
| latency_p50 | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| latency_p90 | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| shots_total | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |
| destroyed_value | 0.0000 +- 0.0000 [worst 0.0000] | 0.0000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
