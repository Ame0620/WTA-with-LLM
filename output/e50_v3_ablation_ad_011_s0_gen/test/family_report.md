# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:49:11

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6323 | n/a | 0.1593 | 79.1354 | 0.004 | 18.0 | 1449.3 | `f5989bf221df` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6201 | n/a | 0.1222 | 80.5970 | 0.004 | 18.0 | 1450.9 | `edc744a42b36` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6262 +- 0.0061 [worst 0.6323] | 0.6323 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1407 +- 0.0185 [worst 0.1593] | 0.1593 |
| ammo_efficiency | 79.8662 +- 0.7308 [worst 79.1354] | 79.1354 |
| latency_p50 | 0.0039 +- 0.0003 [worst 0.0042] | 0.0042 |
| latency_p90 | 0.0059 +- 0.0020 [worst 0.0078] | 0.0078 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1450.1167 +- 0.7833 [worst 1449.3333] | 1449.3333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
