# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:08:31

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5537 | n/a | 0.1148 | 102.5470 | 0.004 | 18.0 | 1853.9 | `f44e5a24fe46` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6013 | n/a | 0.1630 | 101.6449 | 0.004 | 18.0 | 1833.4 | `b0f357626cde` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6236 | n/a | 0.1463 | 103.0837 | 0.004 | 18.0 | 1791.6 | `eee6929a9231` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6354 | n/a | 0.1611 | 96.7494 | 0.004 | 18.0 | 1678.6 | `23d0cb220fd6` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6035 +- 0.0313 [worst 0.6354] | 0.6354 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1463 +- 0.0193 [worst 0.1630] | 0.1630 |
| ammo_efficiency | 101.0062 +- 2.5109 [worst 96.7494] | 96.7494 |
| latency_p50 | 0.0036 +- 0.0000 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0047 +- 0.0014 [worst 0.0071] | 0.0071 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1789.3833 +- 67.7953 [worst 1678.6000] | 1678.6000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
