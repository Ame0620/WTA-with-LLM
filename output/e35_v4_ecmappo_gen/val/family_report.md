# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_5x100_K10_s27.txt', 'dn_5x100_K10_s28.txt', 'dn_5x100_K10_s29.txt', 'dn_5x100_K10_s30.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 20:27:33

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s27.txt` | 8180 | 0.6467 | n/a | 0.2144 | 95.7836 | 0.008 | 30.0 | 2890.3 | `858815fcce66` |
| `dn_5x100_K10_s28.txt` | 8560 | 0.6219 | n/a | 0.1356 | 108.2244 | 0.008 | 30.0 | 3236.8 | `6121d49521b8` |
| `dn_5x100_K10_s29.txt` | 8553 | 0.6681 | n/a | 0.1944 | 95.6984 | 0.008 | 30.0 | 2838.8 | `37293f79c60a` |
| `dn_5x100_K10_s30.txt` | 8397 | 0.6304 | n/a | 0.1211 | 103.0756 | 0.008 | 30.0 | 3103.2 | `ef8fa378497b` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6418 +- 0.0176 [worst 0.6681] | 0.6681 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1664 +- 0.0390 [worst 0.2144] | 0.2144 |
| ammo_efficiency | 100.6955 +- 5.2784 [worst 95.6984] | 95.6984 |
| latency_p50 | 0.0082 +- 0.0001 [worst 0.0084] | 0.0084 |
| latency_p90 | 0.0109 +- 0.0012 [worst 0.0130] | 0.0130 |
| shots_total | 30.0000 +- 0.0000 [worst 30.0000] | 30.0000 |
| destroyed_value | 3017.2667 +- 160.8917 [worst 2838.8000] | 2838.8000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
