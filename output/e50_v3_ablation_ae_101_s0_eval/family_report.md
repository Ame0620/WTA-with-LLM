# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:49:17

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6120 | 0.3881 | 0.0521 | 84.4759 | 0.004 | 17.9 | 1529.4 | `01c635d071a6` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5725 | 0.2903 | 0.0648 | 90.2732 | 0.004 | 18.0 | 1632.5 | `7b0ba4ba0f4e` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5923 +- 0.0198 [worst 0.6120] | 0.6120 |
| gap_mean | 0.3392 +- 0.0489 [worst 0.3881] | 0.3881 |
| invalid_engagement_rate | 0.0584 +- 0.0064 [worst 0.0648] | 0.0648 |
| ammo_efficiency | 87.3745 +- 2.8986 [worst 84.4759] | 84.4759 |
| latency_p50 | 0.0041 +- 0.0001 [worst 0.0042] | 0.0042 |
| latency_p90 | 0.0478 +- 0.0124 [worst 0.0602] | 0.0602 |
| shots_total | 17.9667 +- 0.0333 [worst 18.0000] | 18.0000 |
| destroyed_value | 1580.9667 +- 51.5667 [worst 1529.4000] | 1529.4000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
