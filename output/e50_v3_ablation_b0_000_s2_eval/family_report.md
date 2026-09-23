# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:56:59

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6371 | 0.5160 | 0.1500 | 78.3642 | 0.004 | 18.0 | 1430.4 | `de79d8699c5a` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6468 | 0.5321 | 0.1500 | 74.4531 | 0.003 | 18.0 | 1348.7 | `2304b80a5896` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6420 +- 0.0049 [worst 0.6468] | 0.6468 |
| gap_mean | 0.5240 +- 0.0081 [worst 0.5321] | 0.5321 |
| invalid_engagement_rate | 0.1500 +- 0.0000 [worst 0.1500] | 0.1500 |
| ammo_efficiency | 76.4087 +- 1.9556 [worst 74.4531] | 74.4531 |
| latency_p50 | 0.0033 +- 0.0003 [worst 0.0036] | 0.0036 |
| latency_p90 | 0.0132 +- 0.0063 [worst 0.0195] | 0.0195 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1389.5667 +- 40.8667 [worst 1348.7000] | 1348.7000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
