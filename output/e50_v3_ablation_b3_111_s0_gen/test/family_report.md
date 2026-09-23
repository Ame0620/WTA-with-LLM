# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:48:30

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6490 | n/a | 0.0871 | 89.5059 | 0.004 | 15.5 | 1383.6 | `e7db44b05f21` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5999 | n/a | 0.1132 | 89.1766 | 0.004 | 17.1 | 1528.1 | `8de726c1cefb` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6244 +- 0.0246 [worst 0.6490] | 0.6490 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1001 +- 0.0131 [worst 0.1132] | 0.1132 |
| ammo_efficiency | 89.3413 +- 0.1647 [worst 89.1766] | 89.1766 |
| latency_p50 | 0.0040 +- 0.0001 [worst 0.0041] | 0.0041 |
| latency_p90 | 0.0060 +- 0.0015 [worst 0.0075] | 0.0075 |
| shots_total | 16.2833 +- 0.7833 [worst 17.0667] | 17.0667 |
| destroyed_value | 1455.8333 +- 72.2667 [worst 1383.5667] | 1383.5667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
