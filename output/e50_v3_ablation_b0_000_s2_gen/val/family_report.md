# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:57:26

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.6350 | n/a | 0.1278 | 86.8056 | 0.004 | 17.2 | 1516.1 | `1a58dac24bf2` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6372 | n/a | 0.1315 | 93.0224 | 0.003 | 18.0 | 1667.9 | `c13981a38b7e` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6527 | n/a | 0.2148 | 98.4411 | 0.003 | 18.0 | 1653.3 | `2d0ae77de3b1` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6807 | n/a | 0.1574 | 80.9636 | 0.003 | 18.0 | 1470.0 | `07612b4d2586` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6514 +- 0.0182 [worst 0.6807] | 0.6807 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1579 +- 0.0348 [worst 0.2148] | 0.2148 |
| ammo_efficiency | 89.8082 +- 6.5593 [worst 80.9636] | 80.9636 |
| latency_p50 | 0.0032 +- 0.0003 [worst 0.0036] | 0.0036 |
| latency_p90 | 0.0042 +- 0.0016 [worst 0.0069] | 0.0069 |
| shots_total | 17.8000 +- 0.3464 [worst 18.0000] | 18.0000 |
| destroyed_value | 1576.8500 +- 85.5077 [worst 1470.0333] | 1470.0333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
