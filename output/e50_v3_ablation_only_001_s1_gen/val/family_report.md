# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:56:53

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5582 | n/a | 0.1130 | 100.0086 | 0.004 | 18.0 | 1835.1 | `45852360764a` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5966 | n/a | 0.1148 | 102.8569 | 0.004 | 18.0 | 1855.0 | `fd129f894059` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6632 | n/a | 0.2056 | 88.0859 | 0.004 | 18.0 | 1603.4 | `43c0894b1fe4` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6875 | n/a | 0.2685 | 79.3084 | 0.004 | 18.0 | 1438.9 | `0fff377fcb06` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6264 +- 0.0515 [worst 0.6875] | 0.6875 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1755 +- 0.0655 [worst 0.2685] | 0.2685 |
| ammo_efficiency | 92.5650 +- 9.4489 [worst 79.3084] | 79.3084 |
| latency_p50 | 0.0038 +- 0.0003 [worst 0.0043] | 0.0043 |
| latency_p90 | 0.0051 +- 0.0021 [worst 0.0087] | 0.0087 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1683.1167 +- 172.2158 [worst 1438.9333] | 1438.9333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
