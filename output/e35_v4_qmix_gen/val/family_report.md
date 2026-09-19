# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_5x100_K10_s27.txt', 'dn_5x100_K10_s28.txt', 'dn_5x100_K10_s29.txt', 'dn_5x100_K10_s30.txt']) | policy: **qmix** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 20:25:27

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s27.txt` | 8180 | 0.8043 | n/a | 0.1367 | 52.0611 | 0.006 | 30.0 | 1600.4 | `7ba0d52341bf` |
| `dn_5x100_K10_s28.txt` | 8560 | 0.8294 | n/a | 0.0978 | 47.4854 | 0.006 | 30.0 | 1460.0 | `a0a8bb7a7700` |
| `dn_5x100_K10_s29.txt` | 8553 | 0.8196 | n/a | 0.1267 | 51.1356 | 0.006 | 30.0 | 1543.3 | `369636f55b3e` |
| `dn_5x100_K10_s30.txt` | 8397 | 0.8016 | n/a | 0.1256 | 55.2564 | 0.006 | 30.0 | 1665.6 | `ec7aa060c282` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.8137 +- 0.0113 [worst 0.8294] | 0.8294 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1217 +- 0.0145 [worst 0.1367] | 0.1367 |
| ammo_efficiency | 51.4846 +- 2.7692 [worst 47.4854] | 47.4854 |
| latency_p50 | 0.0059 +- 0.0001 [worst 0.0060] | 0.0060 |
| latency_p90 | 0.0079 +- 0.0017 [worst 0.0107] | 0.0107 |
| shots_total | 30.0000 +- 0.0000 [worst 30.0000] | 30.0000 |
| destroyed_value | 1567.3333 +- 75.5719 [worst 1460.0333] | 1460.0333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
