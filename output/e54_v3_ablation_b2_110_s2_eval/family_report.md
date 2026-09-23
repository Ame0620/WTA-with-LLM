# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:04:25

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6764 | 0.5321 | 0.2139 | 77.9869 | 0.003 | 16.2 | 1275.6 | `50f81c7ec2a3` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5860 | 0.3205 | 0.0648 | 87.4881 | 0.003 | 18.0 | 1581.2 | `a3bbcab04326` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6312 +- 0.0452 [worst 0.6764] | 0.6764 |
| gap_mean | 0.4263 +- 0.1058 [worst 0.5321] | 0.5321 |
| invalid_engagement_rate | 0.1394 +- 0.0746 [worst 0.2139] | 0.2139 |
| ammo_efficiency | 82.7375 +- 4.7506 [worst 77.9869] | 77.9869 |
| latency_p50 | 0.0032 +- 0.0000 [worst 0.0033] | 0.0033 |
| latency_p90 | 0.0048 +- 0.0012 [worst 0.0060] | 0.0060 |
| shots_total | 17.1167 +- 0.8833 [worst 18.0000] | 18.0000 |
| destroyed_value | 1428.3667 +- 152.8000 [worst 1275.5667] | 1275.5667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
