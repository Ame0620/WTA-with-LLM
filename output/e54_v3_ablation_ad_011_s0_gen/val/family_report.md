# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:06:03

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5592 | n/a | 0.1111 | 100.2736 | 0.003 | 18.0 | 1831.1 | `21d9842f03c9` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5696 | n/a | 0.0648 | 108.7060 | 0.003 | 18.0 | 1978.8 | `7feaec5875ba` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6256 | n/a | 0.1160 | 103.3706 | 0.004 | 17.2 | 1782.0 | `a8cb0f232939` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6662 | n/a | 0.3185 | 84.6729 | 0.004 | 18.0 | 1536.6 | `21c91fe72d25` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6052 +- 0.0434 [worst 0.6662] | 0.6662 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1526 +- 0.0978 [worst 0.3185] | 0.3185 |
| ammo_efficiency | 99.2558 +- 8.9434 [worst 84.6729] | 84.6729 |
| latency_p50 | 0.0035 +- 0.0001 [worst 0.0036] | 0.0036 |
| latency_p90 | 0.0045 +- 0.0012 [worst 0.0065] | 0.0065 |
| shots_total | 17.8083 +- 0.3320 [worst 18.0000] | 18.0000 |
| destroyed_value | 1782.1083 +- 159.1846 [worst 1536.6000] | 1536.6000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
