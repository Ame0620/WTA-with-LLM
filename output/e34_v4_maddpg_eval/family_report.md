# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_5x100_K10_s01.txt', 'dn_5x100_K10_s02.txt']) | policy: **maddpg** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 20:04:45

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_5x100_K10_s01.txt` | 8157 | 0.8390 | 0.3874 | 0.1567 | 43.8691 | 0.680 | 30.0 | 1313.4 | `4c8d83ff58a9` |
| `dn_5x100_K10_s02.txt` | 7616 | 0.8339 | 0.3417 | 0.1967 | 41.6346 | 0.673 | 30.0 | 1264.8 | `e50d90728531` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.8365 +- 0.0025 [worst 0.8390] | 0.8390 |
| gap_mean | 0.3645 +- 0.0228 [worst 0.3874] | 0.3874 |
| invalid_engagement_rate | 0.1767 +- 0.0200 [worst 0.1967] | 0.1967 |
| ammo_efficiency | 42.7519 +- 1.1172 [worst 41.6346] | 41.6346 |
| latency_p50 | 0.6765 +- 0.0039 [worst 0.6805] | 0.6805 |
| latency_p90 | 0.7717 +- 0.0061 [worst 0.7778] | 0.7778 |
| shots_total | 30.0000 +- 0.0000 [worst 30.0000] | 30.0000 |
| destroyed_value | 1289.1000 +- 24.3333 [worst 1264.7667] | 1264.7667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
