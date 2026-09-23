# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_10x100_K10_s27.txt', 'dn_10x100_K10_s28.txt', 'dn_10x100_K10_s29.txt', 'dn_10x100_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:02:21

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s27.txt` | 8180 | 0.4987 | n/a | 0.2853 | 62.7666 | 0.015 | 65.1 | 4100.5 | `e8c364d37330` |
| `dn_10x100_K10_s28.txt` | 8560 | 0.4487 | n/a | 0.3149 | 69.0944 | 0.015 | 68.3 | 4718.9 | `9d633b61cdf2` |
| `dn_10x100_K10_s29.txt` | 8553 | 0.5113 | n/a | 0.3020 | 61.8012 | 0.015 | 67.2 | 4180.2 | `765eb8a8b58a` |
| `dn_10x100_K10_s30.txt` | 8397 | 0.4655 | n/a | 0.3005 | 65.6887 | 0.016 | 68.0 | 4488.6 | `a16b1cb11c57` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4810 +- 0.0251 [worst 0.5113] | 0.5113 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3007 +- 0.0105 [worst 0.3149] | 0.3149 |
| ammo_efficiency | 64.8377 +- 2.8440 [worst 61.8012] | 61.8012 |
| latency_p50 | 0.0154 +- 0.0002 [worst 0.0157] | 0.0157 |
| latency_p90 | 0.0192 +- 0.0007 [worst 0.0204] | 0.0204 |
| shots_total | 67.1333 +- 1.2561 [worst 68.2667] | 68.2667 |
| destroyed_value | 4372.0583 +- 247.2030 [worst 4100.5000] | 4100.5000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
