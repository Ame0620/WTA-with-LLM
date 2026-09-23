# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:07:03

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5728 | n/a | 0.1680 | 101.5692 | 0.003 | 17.1 | 1774.4 | `7e9d4329c9f3` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5843 | n/a | 0.0722 | 105.2040 | 0.003 | 18.0 | 1911.5 | `4050116806d7` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6401 | n/a | 0.2148 | 100.9527 | 0.003 | 18.0 | 1713.2 | `2ae434557b5f` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6496 | n/a | 0.1648 | 88.6448 | 0.003 | 18.0 | 1613.4 | `e4ac0d657881` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6117 +- 0.0335 [worst 0.6496] | 0.6496 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1550 +- 0.0517 [worst 0.2148] | 0.2148 |
| ammo_efficiency | 99.0927 +- 6.2470 [worst 88.6448] | 88.6448 |
| latency_p50 | 0.0031 +- 0.0001 [worst 0.0032] | 0.0032 |
| latency_p90 | 0.0040 +- 0.0012 [worst 0.0060] | 0.0060 |
| shots_total | 17.7667 +- 0.4041 [worst 18.0000] | 18.0000 |
| destroyed_value | 1753.1167 +- 107.9883 [worst 1613.4000] | 1613.4000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
