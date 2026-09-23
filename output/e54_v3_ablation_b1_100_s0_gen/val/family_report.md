# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:07:31

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5854 | n/a | 0.2093 | 94.1408 | 0.003 | 18.0 | 1722.4 | `b1a1e765d3b5` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5874 | n/a | 0.0469 | 107.9997 | 0.003 | 17.6 | 1897.3 | `4e6cecfa225e` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6579 | n/a | 0.2093 | 95.1777 | 0.003 | 18.0 | 1628.3 | `540e64a6ec97` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6350 | n/a | 0.1537 | 91.7768 | 0.003 | 18.0 | 1680.6 | `ec210b1988d6` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6164 +- 0.0311 [worst 0.6579] | 0.6579 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1548 +- 0.0663 [worst 0.2093] | 0.2093 |
| ammo_efficiency | 97.2737 +- 6.3141 [worst 91.7768] | 91.7768 |
| latency_p50 | 0.0030 +- 0.0001 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0039 +- 0.0012 [worst 0.0059] | 0.0059 |
| shots_total | 17.8917 +- 0.1876 [worst 18.0000] | 18.0000 |
| destroyed_value | 1732.1500 +- 101.0131 [worst 1628.3000] | 1628.3000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
