# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **greedy** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-18 19:54:09

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.7573 | 1.7967 | 0.6671 | 28.3588 | 0.728 | 70.0 | 1979.9 | `f926edabe40d` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.7012 | 1.3349 | 0.6214 | 32.1420 | 0.753 | 70.0 | 2275.3 | `a5315f597fd1` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7293 +- 0.0280 [worst 0.7573] | 0.7573 |
| gap_mean | 1.5658 +- 0.2309 [worst 1.7967] | 1.7967 |
| invalid_engagement_rate | 0.6443 +- 0.0229 [worst 0.6671] | 0.6671 |
| ammo_efficiency | 30.2504 +- 1.8916 [worst 28.3588] | 28.3588 |
| latency_p50 | 0.7404 +- 0.0123 [worst 0.7527] | 0.7527 |
| latency_p90 | 1.0816 +- 0.2137 [worst 1.2953] | 1.2953 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 2127.6167 +- 147.7167 [worst 1979.9000] | 1979.9000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
