# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:47:48

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.6284 | n/a | 0.0481 | 83.8822 | 0.003 | 18.0 | 1543.5 | `93847bff301e` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6585 | n/a | 0.1222 | 87.4075 | 0.004 | 18.0 | 1570.4 | `67b2994a0634` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.7187 | n/a | 0.3148 | 80.3315 | 0.003 | 18.0 | 1338.9 | `13b8762a487b` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6813 | n/a | 0.1222 | 80.3435 | 0.003 | 18.0 | 1467.1 | `339fd7f2dbe1` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6717 +- 0.0330 [worst 0.7187] | 0.7187 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1519 +- 0.0988 [worst 0.3148] | 0.3148 |
| ammo_efficiency | 82.9912 +- 2.9318 [worst 80.3315] | 80.3315 |
| latency_p50 | 0.0031 +- 0.0003 [worst 0.0036] | 0.0036 |
| latency_p90 | 0.0041 +- 0.0011 [worst 0.0060] | 0.0060 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1479.9667 +- 89.8154 [worst 1338.9333] | 1338.9333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
