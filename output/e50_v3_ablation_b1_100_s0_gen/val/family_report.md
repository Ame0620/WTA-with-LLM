# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:51:03

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.8268 | n/a | 0.2759 | 39.9845 | 0.003 | 18.0 | 719.4 | `8218cb1c77c8` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.7578 | n/a | 0.1500 | 60.6637 | 0.004 | 18.0 | 1113.5 | `1e61b569a0e9` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.8063 | n/a | 0.2611 | 56.3466 | 0.003 | 18.0 | 922.2 | `e59354e59aef` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.7713 | n/a | 0.0944 | 59.3886 | 0.003 | 18.0 | 1053.1 | `bb3660cc1edd` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7905 +- 0.0274 [worst 0.8268] | 0.8268 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1954 +- 0.0759 [worst 0.2759] | 0.2759 |
| ammo_efficiency | 54.0959 +- 8.2968 [worst 39.9845] | 39.9845 |
| latency_p50 | 0.0032 +- 0.0002 [worst 0.0035] | 0.0035 |
| latency_p90 | 0.0042 +- 0.0011 [worst 0.0060] | 0.0060 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 952.0417 +- 151.0691 [worst 719.4000] | 719.4000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
