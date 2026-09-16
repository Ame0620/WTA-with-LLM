# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 13:53:08

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6519 | 0.2878 | 0.1796 | 83.1983 | 0.435 | 18.0 | 1372.2 | `9f0e34d5aff8` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6409 | 0.2264 | 0.1704 | 75.1511 | 0.408 | 18.0 | 1371.6 | `1bd4b9474448` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6464 +- 0.0055 [worst 0.6519] | 0.6519 |
| gap_mean | 0.2571 +- 0.0307 [worst 0.2878] | 0.2878 |
| invalid_engagement_rate | 0.1750 +- 0.0046 [worst 0.1796] | 0.1796 |
| ammo_efficiency | 79.1747 +- 4.0236 [worst 75.1511] | 75.1511 |
| latency_p50 | 0.4215 +- 0.0131 [worst 0.4346] | 0.4346 |
| latency_p90 | 0.4574 +- 0.0044 [worst 0.4618] | 0.4618 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1371.8833 +- 0.3167 [worst 1371.5667] | 1371.5667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
