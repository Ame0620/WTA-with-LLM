# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:59:23

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.7270 | 0.6010 | 0.1647 | 63.2186 | 0.003 | 17.0 | 1076.1 | `99dd221e0666` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6519 | 0.5406 | 0.1870 | 73.8237 | 0.003 | 18.0 | 1329.2 | `1f5a7bec20f4` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6895 +- 0.0375 [worst 0.7270] | 0.7270 |
| gap_mean | 0.5708 +- 0.0302 [worst 0.6010] | 0.6010 |
| invalid_engagement_rate | 0.1759 +- 0.0112 [worst 0.1870] | 0.1870 |
| ammo_efficiency | 68.5211 +- 5.3026 [worst 63.2186] | 63.2186 |
| latency_p50 | 0.0031 +- 0.0001 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0047 +- 0.0014 [worst 0.0061] | 0.0061 |
| shots_total | 17.5000 +- 0.5000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1202.6500 +- 126.5833 [worst 1076.0667] | 1076.0667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
