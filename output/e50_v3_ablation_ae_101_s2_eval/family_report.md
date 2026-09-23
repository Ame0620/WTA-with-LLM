# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:58:46

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6407 | 0.3943 | 0.1352 | 78.3065 | 0.005 | 18.0 | 1416.5 | `b66c830530d4` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.6010 | 0.2838 | 0.1037 | 84.3979 | 0.004 | 18.0 | 1523.8 | `9b694b71b717` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6208 +- 0.0198 [worst 0.6407] | 0.6407 |
| gap_mean | 0.3391 +- 0.0553 [worst 0.3943] | 0.3943 |
| invalid_engagement_rate | 0.1194 +- 0.0157 [worst 0.1352] | 0.1352 |
| ammo_efficiency | 81.3522 +- 3.0457 [worst 78.3065] | 78.3065 |
| latency_p50 | 0.0041 +- 0.0005 [worst 0.0046] | 0.0046 |
| latency_p90 | 0.0060 +- 0.0020 [worst 0.0080] | 0.0080 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1470.1333 +- 53.6333 [worst 1416.5000] | 1416.5000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
