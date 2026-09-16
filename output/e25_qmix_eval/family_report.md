# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **qmix** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-08 17:18:50

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.8742 | 0.6292 | 0.3944 | 27.3084 | 0.493 | 18.0 | 495.8 | `031c28ee4ba3` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.7781 | 0.5694 | 0.2778 | 45.2348 | 0.471 | 18.0 | 847.3 | `0283d73d808b` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.8262 +- 0.0480 [worst 0.8742] | 0.8742 |
| gap_mean | 0.5993 +- 0.0299 [worst 0.6292] | 0.6292 |
| invalid_engagement_rate | 0.3361 +- 0.0583 [worst 0.3944] | 0.3944 |
| ammo_efficiency | 36.2716 +- 8.9632 [worst 27.3084] | 27.3084 |
| latency_p50 | 0.4818 +- 0.0111 [worst 0.4929] | 0.4929 |
| latency_p90 | 0.5713 +- 0.0304 [worst 0.6018] | 0.6018 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 671.5333 +- 175.7667 [worst 495.7667] | 495.7667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
