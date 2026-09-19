# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **qmix** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 07:10:06

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.7857 | 1.7240 | 0.4262 | 26.8466 | 0.694 | 70.0 | 1748.4 | `023c0256c406` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.7552 | 1.4046 | 0.4371 | 26.6740 | 0.698 | 70.0 | 1864.3 | `7dd87246482a` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7704 +- 0.0152 [worst 0.7857] | 0.7857 |
| gap_mean | 1.5643 +- 0.1597 [worst 1.7240] | 1.7240 |
| invalid_engagement_rate | 0.4317 +- 0.0055 [worst 0.4371] | 0.4371 |
| ammo_efficiency | 26.7603 +- 0.0863 [worst 26.6740] | 26.6740 |
| latency_p50 | 0.6960 +- 0.0024 [worst 0.6984] | 0.6984 |
| latency_p90 | 0.7980 +- 0.0155 [worst 0.8135] | 0.8135 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 1806.3167 +- 57.9500 [worst 1748.3667] | 1748.3667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
