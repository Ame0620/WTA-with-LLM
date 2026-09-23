# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:53:23

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5981 | n/a | 0.1537 | 91.3251 | 0.004 | 18.0 | 1669.3 | `70a49c33c7f4` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6028 | n/a | 0.1074 | 101.2174 | 0.004 | 18.0 | 1826.3 | `9fdabdf3beb4` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6603 | n/a | 0.1000 | 89.4536 | 0.004 | 18.0 | 1617.0 | `40bdde2834cf` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6954 | n/a | 0.2611 | 77.1575 | 0.004 | 18.0 | 1402.5 | `29788065aebe` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6392 +- 0.0407 [worst 0.6954] | 0.6954 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1556 +- 0.0643 [worst 0.2611] | 0.2611 |
| ammo_efficiency | 89.7884 +- 8.5533 [worst 77.1575] | 77.1575 |
| latency_p50 | 0.0038 +- 0.0003 [worst 0.0043] | 0.0043 |
| latency_p90 | 0.0049 +- 0.0013 [worst 0.0070] | 0.0070 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1628.7917 +- 151.6656 [worst 1402.5000] | 1402.5000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
