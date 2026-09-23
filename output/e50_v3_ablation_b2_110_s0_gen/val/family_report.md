# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:50:23

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.6508 | n/a | 0.0557 | 82.6885 | 0.003 | 17.2 | 1450.7 | `0c5fd9a883d6` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6670 | n/a | 0.0759 | 83.8931 | 0.004 | 18.0 | 1531.1 | `492362befcc0` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.7332 | n/a | 0.3373 | 80.0594 | 0.003 | 17.0 | 1270.2 | `51a394aa66ef` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6676 | n/a | 0.1185 | 84.1804 | 0.003 | 18.0 | 1530.4 | `71ee0e59a204` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6796 +- 0.0316 [worst 0.7332] | 0.7332 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1468 +- 0.1123 [worst 0.3373] | 0.3373 |
| ammo_efficiency | 82.7054 +- 1.6270 [worst 80.0594] | 80.0594 |
| latency_p50 | 0.0032 +- 0.0003 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0041 +- 0.0012 [worst 0.0061] | 0.0061 |
| shots_total | 17.5500 +- 0.4555 [worst 18.0000] | 18.0000 |
| destroyed_value | 1445.6167 +- 106.4172 [worst 1270.2000] | 1270.2000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
