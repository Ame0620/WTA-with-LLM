# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_10x100_K10_s27.txt', 'dn_10x100_K10_s28.txt', 'dn_10x100_K10_s29.txt', 'dn_10x100_K10_s30.txt']) | policy: **maddpg** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 07:18:03

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s27.txt` | 8180 | 0.7059 | n/a | 0.4429 | 33.6937 | 0.012 | 70.0 | 2405.7 | `7d959f6b7124` |
| `dn_10x100_K10_s28.txt` | 8560 | 0.6726 | n/a | 0.4114 | 39.3873 | 0.011 | 70.0 | 2802.6 | `b82a0aadccf4` |
| `dn_10x100_K10_s29.txt` | 8553 | 0.7333 | n/a | 0.4443 | 32.5635 | 0.010 | 70.0 | 2281.4 | `4cce55d3feb2` |
| `dn_10x100_K10_s30.txt` | 8397 | 0.7399 | n/a | 0.4057 | 31.6940 | 0.010 | 70.0 | 2184.0 | `43b1148a80f0` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7129 +- 0.0265 [worst 0.7399] | 0.7399 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.4261 +- 0.0176 [worst 0.4443] | 0.4443 |
| ammo_efficiency | 34.3346 +- 3.0021 [worst 31.6940] | 31.6940 |
| latency_p50 | 0.0108 +- 0.0009 [worst 0.0120] | 0.0120 |
| latency_p90 | 0.0140 +- 0.0043 [worst 0.0212] | 0.0212 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 2418.4250 +- 235.3101 [worst 2184.0000] | 2184.0000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
