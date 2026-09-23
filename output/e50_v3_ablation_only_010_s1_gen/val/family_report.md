# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:56:16

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.6599 | n/a | 0.2000 | 92.9619 | 0.003 | 15.0 | 1412.7 | `b08fb0b6c617` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.7255 | n/a | 0.2556 | 83.7297 | 0.004 | 15.0 | 1262.2 | `2bdca301106d` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.7333 | n/a | 0.2511 | 83.9196 | 0.003 | 15.0 | 1269.6 | `b2ac063a1691` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.8040 | n/a | 0.3956 | 59.8712 | 0.003 | 15.0 | 902.5 | `d780fa0d4af5` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.7307 +- 0.0510 [worst 0.8040] | 0.8040 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2756 +- 0.0726 [worst 0.3956] | 0.3956 |
| ammo_efficiency | 80.1206 +- 12.2719 [worst 59.8712] | 59.8712 |
| latency_p50 | 0.0032 +- 0.0002 [worst 0.0036] | 0.0036 |
| latency_p90 | 0.0043 +- 0.0011 [worst 0.0062] | 0.0062 |
| shots_total | 15.0000 +- 0.0000 [worst 15.0000] | 15.0000 |
| destroyed_value | 1211.7583 +- 188.3332 [worst 902.5333] | 902.5333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
