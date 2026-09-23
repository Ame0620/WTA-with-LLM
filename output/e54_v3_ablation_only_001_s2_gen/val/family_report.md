# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:16:33

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5584 | n/a | 0.1574 | 99.4167 | 0.004 | 18.0 | 1834.4 | `3f2ba5534391` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5992 | n/a | 0.1093 | 101.2281 | 0.004 | 18.0 | 1842.7 | `cf429496f3f5` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6253 | n/a | 0.1593 | 104.7592 | 0.004 | 18.0 | 1783.5 | `3b4b7496e2f5` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6164 | n/a | 0.1667 | 96.1500 | 0.004 | 18.0 | 1766.1 | `5bf85c88c14a` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5998 +- 0.0257 [worst 0.6253] | 0.6253 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1481 +- 0.0227 [worst 0.1667] | 0.1667 |
| ammo_efficiency | 100.3885 +- 3.1112 [worst 96.1500] | 96.1500 |
| latency_p50 | 0.0036 +- 0.0001 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0047 +- 0.0013 [worst 0.0069] | 0.0069 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1806.6667 +- 32.6211 [worst 1766.0667] | 1766.0667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
