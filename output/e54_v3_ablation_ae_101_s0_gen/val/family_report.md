# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:06:35

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5577 | n/a | 0.1593 | 99.7325 | 0.004 | 18.0 | 1837.2 | `2ba8c0836fa2` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.5952 | n/a | 0.1463 | 103.0057 | 0.004 | 18.0 | 1861.5 | `92d4de8a2c30` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6417 | n/a | 0.1537 | 97.6226 | 0.004 | 18.0 | 1705.4 | `52334624521b` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6522 | n/a | 0.1722 | 97.6784 | 0.004 | 18.0 | 1601.1 | `fb0f6bf774a5` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6117 +- 0.0379 [worst 0.6522] | 0.6522 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1579 +- 0.0095 [worst 0.1722] | 0.1722 |
| ammo_efficiency | 99.5098 +- 2.1901 [worst 97.6226] | 97.6226 |
| latency_p50 | 0.0036 +- 0.0001 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0046 +- 0.0014 [worst 0.0070] | 0.0070 |
| shots_total | 18.0000 +- 0.0000 [worst 18.0000] | 18.0000 |
| destroyed_value | 1751.3083 +- 105.1031 [worst 1601.1000] | 1601.1000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
