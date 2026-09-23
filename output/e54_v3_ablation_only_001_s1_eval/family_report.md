# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_3x50_K10_s01.txt', 'dn_3x50_K10_s02.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:04:11

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s01.txt` | 3942 | 0.6686 | 0.4747 | 0.2593 | 82.3562 | 0.004 | 18.0 | 1306.4 | `34691c08de54` |
| `dn_3x50_K10_s02.txt` | 3819 | 0.5528 | 0.3764 | 0.1481 | 93.8685 | 0.004 | 18.0 | 1708.0 | `5dd09cef418f` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6107 +- 0.0579 [worst 0.6686] | 0.6686 |
| gap_mean | 0.4256 +- 0.0492 [worst 0.4747] | 0.4747 |
| invalid_engagement_rate | 0.2037 +- 0.0556 [worst 0.2593] | 0.2593 |
| ammo_efficiency | 88.1124 +- 5.7561 [worst 82.3562] | 82.3562 |
| latency_p50 | 0.0038 +- 0.0001 [worst 0.0038] | 0.0038 |
| latency_p90 | 0.0056 +- 0.0016 [worst 0.0071] | 0.0071 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1507.2000 +- 200.7667 [worst 1306.4333] | 1306.4333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
