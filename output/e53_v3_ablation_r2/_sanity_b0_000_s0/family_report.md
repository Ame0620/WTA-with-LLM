# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 3 (base 7) | solver timelimit 30s
- generated at: 2026-09-22 18:47:34

## Per-instance metrics (mean +- std over 3 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5712 | n/a | 0.0926 | 103.3549 | 0.010 | 18.0 | 1781.3 | `4514ff188373` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6516 | n/a | 0.2037 | 90.6284 | 0.009 | 18.0 | 1602.0 | `317f7ba908a0` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6325 | n/a | 0.1667 | 103.4042 | 0.005 | 18.0 | 1749.3 | `779576e83180` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6281 | n/a | 0.1852 | 91.5256 | 0.003 | 18.0 | 1712.3 | `893d2531ffdb` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6208 +- 0.0300 [worst 0.6516] | 0.6516 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1620 +- 0.0422 [worst 0.2037] | 0.2037 |
| ammo_efficiency | 97.2283 +- 6.1595 [worst 90.6284] | 90.6284 |
| latency_p50 | 0.0068 +- 0.0030 [worst 0.0105] | 0.0105 |
| latency_p90 | 0.0498 +- 0.0745 [worst 0.1788] | 0.1788 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1711.2500 +- 67.6364 [worst 1602.0000] | 1602.0000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
