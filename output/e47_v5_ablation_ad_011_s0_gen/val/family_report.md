# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_10x100_K10_s27.txt', 'dn_10x100_K10_s28.txt', 'dn_10x100_K10_s29.txt', 'dn_10x100_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:21:42

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s27.txt` | 8180 | 0.5951 | n/a | 0.2829 | 64.6524 | 0.021 | 51.1 | 3312.1 | `95f38208c9f1` |
| `dn_10x100_K10_s28.txt` | 8560 | 0.5289 | n/a | 0.1820 | 81.0093 | 0.021 | 50.0 | 4033.0 | `cbf6df0ca30f` |
| `dn_10x100_K10_s29.txt` | 8553 | 0.6170 | n/a | 0.2543 | 62.7274 | 0.021 | 52.4 | 3275.4 | `6f1260e86d9c` |
| `dn_10x100_K10_s30.txt` | 8397 | 0.5675 | n/a | 0.2630 | 67.1758 | 0.021 | 54.0 | 3631.7 | `fcc73af08c22` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5771 +- 0.0329 [worst 0.6170] | 0.6170 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2455 +- 0.0381 [worst 0.2829] | 0.2829 |
| ammo_efficiency | 68.8912 +- 7.1720 [worst 62.7274] | 62.7274 |
| latency_p50 | 0.0207 +- 0.0001 [worst 0.0208] | 0.0208 |
| latency_p90 | 0.0234 +- 0.0014 [worst 0.0258] | 0.0258 |
| shots_total | 51.8917 +- 1.4910 [worst 54.0000] | 54.0000 |
| destroyed_value | 3563.0750 +- 304.6636 [worst 3275.4333] | 3275.4333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
