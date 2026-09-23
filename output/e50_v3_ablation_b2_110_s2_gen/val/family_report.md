# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:59:49

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.6591 | n/a | 0.1080 | 81.4956 | 0.004 | 17.2 | 1416.2 | `6409630f1a73` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6871 | n/a | 0.1296 | 78.8979 | 0.003 | 18.0 | 1438.5 | `342d91d53a0e` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6994 | n/a | 0.2611 | 78.9176 | 0.003 | 18.0 | 1430.8 | `1b61809b1aff` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6776 | n/a | 0.1593 | 80.8447 | 0.003 | 18.0 | 1484.2 | `531d5ec1281a` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6808 +- 0.0147 [worst 0.6994] | 0.6994 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1645 +- 0.0587 [worst 0.2611] | 0.2611 |
| ammo_efficiency | 80.0389 +- 1.1544 [worst 78.8979] | 78.8979 |
| latency_p50 | 0.0032 +- 0.0004 [worst 0.0038] | 0.0038 |
| latency_p90 | 0.0044 +- 0.0020 [worst 0.0078] | 0.0078 |
| shots_total | 17.8000 +- 0.3464 [worst 18.0000] | 18.0000 |
| destroyed_value | 1442.4167 +- 25.3953 [worst 1416.2333] | 1416.2333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
