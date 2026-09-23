# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:13:00

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5619 | n/a | 0.1130 | 98.6468 | 0.003 | 18.0 | 1819.8 | `3c9e378c2d3d` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6284 | n/a | 0.1926 | 95.6385 | 0.003 | 18.0 | 1708.4 | `fbb7bf7e2809` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6451 | n/a | 0.1667 | 98.0178 | 0.003 | 17.0 | 1689.2 | `e024e9767e92` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6328 | n/a | 0.2130 | 91.5191 | 0.003 | 18.0 | 1690.4 | `f699e1789d33` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6171 +- 0.0324 [worst 0.6451] | 0.6451 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1713 +- 0.0375 [worst 0.2130] | 0.2130 |
| ammo_efficiency | 95.9555 +- 2.7964 [worst 91.5191] | 91.5191 |
| latency_p50 | 0.0031 +- 0.0001 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0039 +- 0.0012 [worst 0.0061] | 0.0061 |
| shots_total | 17.7500 +- 0.4330 [worst 18.0000] | 18.0000 |
| destroyed_value | 1726.9667 +- 54.1152 [worst 1689.2333] | 1689.2333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
