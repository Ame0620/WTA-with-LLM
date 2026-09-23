# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:15:33

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5609 | n/a | 0.1611 | 99.0792 | 0.003 | 18.0 | 1823.9 | `7c0e4b7ad2a9` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6002 | n/a | 0.1222 | 101.6676 | 0.003 | 18.0 | 1838.1 | `a028b9a6c13a` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6270 | n/a | 0.1593 | 103.5134 | 0.003 | 18.0 | 1775.3 | `028611196e85` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6572 | n/a | 0.2185 | 86.3921 | 0.003 | 18.0 | 1578.4 | `f4d658703cd6` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6113 +- 0.0354 [worst 0.6572] | 0.6572 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1653 +- 0.0344 [worst 0.2185] | 0.2185 |
| ammo_efficiency | 97.6631 +- 6.6952 [worst 86.3921] | 86.3921 |
| latency_p50 | 0.0031 +- 0.0001 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0039 +- 0.0011 [worst 0.0059] | 0.0059 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1753.9250 +- 103.9756 [worst 1578.4000] | 1578.4000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
