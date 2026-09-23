# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:06:38

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6444 | n/a | 0.2463 | 78.2943 | 0.003 | 18.0 | 1401.9 | `330bc30a620a` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5531 | n/a | 0.1111 | 95.3625 | 0.003 | 18.0 | 1706.7 | `5c1d36e5ac5d` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5987 +- 0.0456 [worst 0.6444] | 0.6444 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1787 +- 0.0676 [worst 0.2463] | 0.2463 |
| ammo_efficiency | 86.8284 +- 8.5341 [worst 78.2943] | 78.2943 |
| latency_p50 | 0.0034 +- 0.0000 [worst 0.0035] | 0.0035 |
| latency_p90 | 0.0052 +- 0.0015 [worst 0.0067] | 0.0067 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1554.2833 +- 152.4167 [worst 1401.8667] | 1401.8667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
