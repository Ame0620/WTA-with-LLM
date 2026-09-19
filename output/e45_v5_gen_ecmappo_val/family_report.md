# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_10x100_K10_s27.txt', 'dn_10x100_K10_s28.txt', 'dn_10x100_K10_s29.txt', 'dn_10x100_K10_s30.txt']) | policy: **ecmappo** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 06:54:34

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s27.txt` | 8180 | 0.4296 | n/a | 0.2814 | 66.1412 | 0.013 | 70.0 | 4665.9 | `2ae945df0602` |
| `dn_10x100_K10_s28.txt` | 8560 | 0.4289 | n/a | 0.3261 | 71.3197 | 0.012 | 69.9 | 4888.5 | `832c5d3cb281` |
| `dn_10x100_K10_s29.txt` | 8553 | 0.4216 | n/a | 0.2343 | 71.1204 | 0.012 | 70.0 | 4946.8 | `55b0871d6764` |
| `dn_10x100_K10_s30.txt` | 8397 | 0.4335 | n/a | 0.3029 | 68.0589 | 0.014 | 70.0 | 4756.5 | `1f8ec990cb2e` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4284 +- 0.0043 [worst 0.4335] | 0.4335 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2862 +- 0.0339 [worst 0.3261] | 0.3261 |
| ammo_efficiency | 69.1601 +- 2.1698 [worst 66.1412] | 66.1412 |
| latency_p50 | 0.0129 +- 0.0008 [worst 0.0141] | 0.0141 |
| latency_p90 | 0.0163 +- 0.0044 [worst 0.0237] | 0.0237 |
| shots_total | 69.9750 +- 0.0433 [worst 70.0000] | 70.0000 |
| destroyed_value | 4814.4250 +- 110.0287 [worst 4665.9000] | 4665.9000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
