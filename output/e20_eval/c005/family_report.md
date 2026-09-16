# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-09 20:23:29

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6608 | 0.4807 | 0.2196 | 89.5606 | 0.415 | 17.0 | 1336.9 | `e929317b293d` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5455 | 0.2935 | 0.0981 | 95.9710 | 0.403 | 18.0 | 1735.6 | `d6731c676833` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6032 +- 0.0577 [worst 0.6608] | 0.6608 |
| gap_mean | 0.3871 +- 0.0936 [worst 0.4807] | 0.4807 |
| invalid_engagement_rate | 0.1589 +- 0.0607 [worst 0.2196] | 0.2196 |
| ammo_efficiency | 92.7658 +- 3.2052 [worst 89.5606] | 89.5606 |
| latency_p50 | 0.4090 +- 0.0064 [worst 0.4154] | 0.4154 |
| latency_p90 | 0.4564 +- 0.0213 [worst 0.4776] | 0.4776 |
| shots_total | 17.5000 +- 0.5000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1536.2667 +- 199.3333 [worst 1336.9333] | 1336.9333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
