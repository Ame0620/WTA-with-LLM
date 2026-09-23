# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_10x100_K10_s27.txt', 'dn_10x100_K10_s28.txt', 'dn_10x100_K10_s29.txt', 'dn_10x100_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:55:20

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s27.txt` | 8180 | 0.5911 | n/a | 0.2833 | 62.1083 | 0.011 | 54.0 | 3344.9 | `258b709d37da` |
| `dn_10x100_K10_s28.txt` | 8560 | 0.5386 | n/a | 0.2752 | 75.9184 | 0.011 | 52.3 | 3949.8 | `4ba2bdb49c75` |
| `dn_10x100_K10_s29.txt` | 8553 | 0.6022 | n/a | 0.2958 | 59.8829 | 0.011 | 57.1 | 3402.2 | `8c51c4f54a98` |
| `dn_10x100_K10_s30.txt` | 8397 | 0.5564 | n/a | 0.2943 | 64.4110 | 0.011 | 58.0 | 3724.9 | `763785d6cbdc` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5721 +- 0.0257 [worst 0.6022] | 0.6022 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2871 +- 0.0084 [worst 0.2958] | 0.2958 |
| ammo_efficiency | 65.5802 +- 6.1798 [worst 59.8829] | 59.8829 |
| latency_p50 | 0.0109 +- 0.0001 [worst 0.0111] | 0.0111 |
| latency_p90 | 0.0122 +- 0.0014 [worst 0.0147] | 0.0147 |
| shots_total | 55.3667 +- 2.2981 [worst 58.0000] | 58.0000 |
| destroyed_value | 3605.4500 +- 245.9908 [worst 3344.8667] | 3344.8667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
