# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:14:04

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5604 | n/a | 0.0696 | 106.1915 | 0.004 | 17.1 | 1826.2 | `f14d1428f51d` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6031 | n/a | 0.1722 | 99.9449 | 0.004 | 18.0 | 1824.9 | `c6e738bd09ca` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6301 | n/a | 0.1537 | 102.8612 | 0.004 | 18.0 | 1760.6 | `9861ec9ebe43` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6411 | n/a | 0.2167 | 90.5155 | 0.004 | 18.0 | 1652.5 | `23bc4478f43c` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6087 +- 0.0311 [worst 0.6411] | 0.6411 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1531 +- 0.0533 [worst 0.2167] | 0.2167 |
| ammo_efficiency | 99.8783 +- 5.8400 [worst 90.5155] | 90.5155 |
| latency_p50 | 0.0036 +- 0.0001 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0045 +- 0.0013 [worst 0.0067] | 0.0067 |
| shots_total | 17.7750 +- 0.3897 [worst 18.0000] | 18.0000 |
| destroyed_value | 1766.0417 +- 70.6992 [worst 1652.5333] | 1652.5333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
