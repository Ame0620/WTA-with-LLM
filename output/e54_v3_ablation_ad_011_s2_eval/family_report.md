# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:04:20

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6493 | 0.4658 | 0.2074 | 84.5194 | 0.004 | 18.0 | 1382.4 | `c2ea9b64e4f4` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5806 | 0.3891 | 0.1611 | 88.2904 | 0.004 | 18.0 | 1601.6 | `8207f49fd6ab` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6150 +- 0.0344 [worst 0.6493] | 0.6493 |
| gap_mean | 0.4275 +- 0.0384 [worst 0.4658] | 0.4658 |
| invalid_engagement_rate | 0.1843 +- 0.0231 [worst 0.2074] | 0.2074 |
| ammo_efficiency | 86.4049 +- 1.8855 [worst 84.5194] | 84.5194 |
| latency_p50 | 0.0037 +- 0.0000 [worst 0.0038] | 0.0038 |
| latency_p90 | 0.0056 +- 0.0016 [worst 0.0072] | 0.0072 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1491.9833 +- 109.6167 [worst 1382.3667] | 1382.3667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
