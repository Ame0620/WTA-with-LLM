# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **ga** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 19:38:47

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.4816 | 0.1826 | 0.1314 | 68.1654 | 0.652 | 70.0 | 4228.5 | `93400e03fa5c` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.4420 | 0.2375 | 0.1214 | 64.5694 | 0.607 | 70.0 | 4249.4 | `e708c17ab870` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4618 +- 0.0198 [worst 0.4816] | 0.4816 |
| gap_mean | 0.2100 +- 0.0275 [worst 0.2375] | 0.2375 |
| invalid_engagement_rate | 0.1264 +- 0.0050 [worst 0.1314] | 0.1314 |
| ammo_efficiency | 66.3674 +- 1.7980 [worst 64.5694] | 64.5694 |
| latency_p50 | 0.6298 +- 0.0224 [worst 0.6522] | 0.6522 |
| latency_p90 | 0.7436 +- 0.0589 [worst 0.8025] | 0.8025 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 4238.9500 +- 10.4500 [worst 4228.5000] | 4228.5000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
