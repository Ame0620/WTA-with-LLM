# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **marl** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-09 20:27:45

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5788 | n/a | 0.1706 | 101.2016 | 0.006 | 17.0 | 1749.6 | `4f43d184f23f` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5999 | n/a | 0.1241 | 100.7719 | 0.005 | 18.0 | 1839.9 | `bbd86f3fb05b` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6240 | n/a | 0.1038 | 103.9119 | 0.005 | 17.0 | 1789.7 | `a9c70b9530b7` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6005 | n/a | 0.1056 | 99.2422 | 0.005 | 18.0 | 1839.1 | `94ce5e893be2` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6008 +- 0.0160 [worst 0.6240] | 0.6240 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1260 +- 0.0269 [worst 0.1706] | 0.1706 |
| ammo_efficiency | 101.2819 +- 1.6840 [worst 99.2422] | 99.2422 |
| latency_p50 | 0.0053 +- 0.0002 [worst 0.0056] | 0.0056 |
| latency_p90 | 0.0076 +- 0.0015 [worst 0.0101] | 0.0101 |
| shots_total | 17.5083 +- 0.4918 [worst 18.0000] | 18.0000 |
| destroyed_value | 1804.5750 +- 37.6740 [worst 1749.6333] | 1749.6333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
