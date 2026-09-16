# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 13:45:34

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6463 | 0.4652 | 0.2093 | 87.0301 | 0.431 | 18.0 | 1394.3 | `5b891024fca9` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5727 | 0.2885 | 0.0500 | 90.0532 | 0.428 | 18.0 | 1631.7 | `03449ef74515` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6095 +- 0.0368 [worst 0.6463] | 0.6463 |
| gap_mean | 0.3769 +- 0.0883 [worst 0.4652] | 0.4652 |
| invalid_engagement_rate | 0.1296 +- 0.0796 [worst 0.2093] | 0.2093 |
| ammo_efficiency | 88.5416 +- 1.5115 [worst 87.0301] | 87.0301 |
| latency_p50 | 0.4293 +- 0.0014 [worst 0.4307] | 0.4307 |
| latency_p90 | 0.4768 +- 0.0042 [worst 0.4810] | 0.4810 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1513.0333 +- 118.7000 [worst 1394.3333] | 1394.3333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
