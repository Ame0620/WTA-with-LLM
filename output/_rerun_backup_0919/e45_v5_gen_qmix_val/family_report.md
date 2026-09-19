# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_10x100_K10_s27.txt', 'dn_10x100_K10_s28.txt', 'dn_10x100_K10_s29.txt', 'dn_10x100_K10_s30.txt']) | policy: **qmix** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 07:11:03

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s27.txt` | 8180 | 0.7139 | n/a | 0.2986 | 38.1680 | 0.012 | 70.0 | 2340.1 | `df54be24b3d6` |
| `dn_10x100_K10_s28.txt` | 8560 | 0.7448 | n/a | 0.4143 | 33.8580 | 0.010 | 70.0 | 2184.9 | `5805e3861429` |
| `dn_10x100_K10_s29.txt` | 8553 | 0.7942 | n/a | 0.4814 | 27.9212 | 0.010 | 70.0 | 1760.1 | `ddcc4a99ae54` |
| `dn_10x100_K10_s30.txt` | 8397 | 0.7709 | n/a | 0.4643 | 28.8128 | 0.012 | 70.0 | 1923.4 | `9b150a3fc858` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7560 +- 0.0299 [worst 0.7942] | 0.7942 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.4146 +- 0.0714 [worst 0.4814] | 0.4814 |
| ammo_efficiency | 32.1900 +- 4.1276 [worst 27.9212] | 27.9212 |
| latency_p50 | 0.0108 +- 0.0008 [worst 0.0118] | 0.0118 |
| latency_p90 | 0.0140 +- 0.0048 [worst 0.0222] | 0.0222 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 2052.1250 +- 224.9486 [worst 1760.1000] | 1760.1000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
