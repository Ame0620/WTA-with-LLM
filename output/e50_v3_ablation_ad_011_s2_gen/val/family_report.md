# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:58:40

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.6326 | n/a | 0.2167 | 84.6051 | 0.004 | 18.0 | 1526.2 | `4dfb8363c21f` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6800 | n/a | 0.2741 | 82.4253 | 0.004 | 18.0 | 1471.1 | `cee6da757511` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6453 | n/a | 0.1187 | 104.0907 | 0.004 | 16.0 | 1688.3 | `f07db7b54c74` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.7020 | n/a | 0.3278 | 75.6378 | 0.004 | 18.0 | 1372.1 | `56ccb8529c18` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6650 +- 0.0275 [worst 0.7020] | 0.7020 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2343 +- 0.0774 [worst 0.3278] | 0.3278 |
| ammo_efficiency | 86.6897 +- 10.5767 [worst 75.6378] | 75.6378 |
| latency_p50 | 0.0038 +- 0.0003 [worst 0.0043] | 0.0043 |
| latency_p90 | 0.0050 +- 0.0014 [worst 0.0073] | 0.0073 |
| shots_total | 17.5000 +- 0.8660 [worst 18.0000] | 18.0000 |
| destroyed_value | 1514.4250 +- 114.5649 [worst 1372.0667] | 1372.0667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
