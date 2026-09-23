# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:52:45

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.6319 | n/a | 0.0617 | 88.2030 | 0.004 | 17.2 | 1529.2 | `ef33be235106` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6292 | n/a | 0.1111 | 93.9025 | 0.003 | 18.0 | 1705.1 | `2ba738d0693e` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6720 | n/a | 0.1647 | 91.1261 | 0.003 | 17.0 | 1561.4 | `b6a42f63711d` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6807 | n/a | 0.1574 | 80.9636 | 0.003 | 18.0 | 1470.0 | `07612b4d2586` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6534 +- 0.0231 [worst 0.6807] | 0.6807 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1237 +- 0.0413 [worst 0.1647] | 0.1647 |
| ammo_efficiency | 88.5488 +- 4.8208 [worst 80.9636] | 80.9636 |
| latency_p50 | 0.0032 +- 0.0002 [worst 0.0036] | 0.0036 |
| latency_p90 | 0.0042 +- 0.0016 [worst 0.0071] | 0.0071 |
| shots_total | 17.5500 +- 0.4555 [worst 18.0000] | 18.0000 |
| destroyed_value | 1566.4167 +- 86.4930 [worst 1470.0333] | 1470.0333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
