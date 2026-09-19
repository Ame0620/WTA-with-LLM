# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 06:53:31

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.4155 | 1.5170 | 0.3124 | 67.5115 | 0.627 | 70.0 | 4768.2 | `9c96e72b1bee` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.3739 | 1.3570 | 0.3586 | 67.5978 | 0.610 | 70.0 | 4768.7 | `d04ad9f05a55` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.3947 +- 0.0208 [worst 0.4155] | 0.4155 |
| gap_mean | 1.4370 +- 0.0800 [worst 1.5170] | 1.5170 |
| invalid_engagement_rate | 0.3355 +- 0.0231 [worst 0.3586] | 0.3586 |
| ammo_efficiency | 67.5547 +- 0.0432 [worst 67.5115] | 67.5115 |
| latency_p50 | 0.6184 +- 0.0086 [worst 0.6270] | 0.6270 |
| latency_p90 | 0.7271 +- 0.0402 [worst 0.7673] | 0.7673 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 4768.4167 +- 0.2500 [worst 4768.1667] | 4768.1667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
