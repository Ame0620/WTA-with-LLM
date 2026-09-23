# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 02:00:58

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.7104 | n/a | 0.2333 | 70.8243 | 0.003 | 16.0 | 1141.6 | `8687be33fee3` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.7002 | n/a | 0.3289 | 76.4148 | 0.003 | 15.0 | 1145.0 | `d4e79d687e27` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7053 +- 0.0051 [worst 0.7104] | 0.7104 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2811 +- 0.0478 [worst 0.3289] | 0.3289 |
| ammo_efficiency | 73.6196 +- 2.7953 [worst 70.8243] | 70.8243 |
| latency_p50 | 0.0032 +- 0.0000 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0047 +- 0.0012 [worst 0.0060] | 0.0060 |
| shots_total | 15.5000 +- 0.5000 [worst 16.0000] | 16.0000 |
| destroyed_value | 1143.3333 +- 1.7000 [worst 1141.6333] | 1141.6333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
