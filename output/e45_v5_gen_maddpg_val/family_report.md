# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_10x100_K10_s27.txt', 'dn_10x100_K10_s28.txt', 'dn_10x100_K10_s29.txt', 'dn_10x100_K10_s30.txt']) | policy: **maddpg** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 23:31:24

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s27.txt` | 8180 | 0.5362 | n/a | 0.2843 | 54.8597 | 0.015 | 70.0 | 3793.5 | `d41a6ed6685a` |
| `dn_10x100_K10_s28.txt` | 8560 | 0.5018 | n/a | 0.2429 | 60.4880 | 0.014 | 70.0 | 4264.3 | `84a0c3997b8e` |
| `dn_10x100_K10_s29.txt` | 8553 | 0.5982 | n/a | 0.2814 | 49.5171 | 0.014 | 70.0 | 3436.4 | `056d952dbfa8` |
| `dn_10x100_K10_s30.txt` | 8397 | 0.5605 | n/a | 0.2871 | 53.2444 | 0.014 | 70.0 | 3690.4 | `37f4f4d393e3` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5492 +- 0.0352 [worst 0.5982] | 0.5982 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2739 +- 0.0181 [worst 0.2871] | 0.2871 |
| ammo_efficiency | 54.5273 +- 3.9493 [worst 49.5171] | 49.5171 |
| latency_p50 | 0.0144 +- 0.0003 [worst 0.0149] | 0.0149 |
| latency_p90 | 0.0190 +- 0.0050 [worst 0.0276] | 0.0276 |
| shots_total | 70.0000 +- 0.0000 [worst 70.0000] | 70.0000 |
| destroyed_value | 3796.1500 +- 299.9061 [worst 3436.4000] | 3436.4000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
