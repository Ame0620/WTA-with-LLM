# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_3x50_K10_s27.txt', 'dn_3x50_K10_s28.txt', 'dn_3x50_K10_s29.txt', 'dn_3x50_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-21 01:58:03

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s27.txt` | 4154 | 0.5786 | n/a | 0.1294 | 102.2787 | 0.004 | 17.0 | 1750.7 | `3f1f54f7c865` |
| `dn_3x50_K10_s28.txt` | 4598 | 0.6230 | n/a | 0.1593 | 96.0082 | 0.004 | 18.0 | 1733.7 | `2b54629d7bcc` |
| `dn_3x50_K10_s29.txt` | 4760 | 0.6563 | n/a | 0.1792 | 101.8738 | 0.004 | 16.0 | 1635.8 | `f646a489da56` |
| `dn_3x50_K10_s30.txt` | 4604 | 0.6649 | n/a | 0.2222 | 84.4433 | 0.004 | 18.0 | 1542.9 | `d1e673e13aca` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.6307 +- 0.0339 [worst 0.6649] | 0.6649 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.1725 +- 0.0337 [worst 0.2222] | 0.2222 |
| ammo_efficiency | 96.1510 +- 7.2005 [worst 84.4433] | 84.4433 |
| latency_p50 | 0.0038 +- 0.0002 [worst 0.0041] | 0.0041 |
| latency_p90 | 0.0050 +- 0.0013 [worst 0.0073] | 0.0073 |
| shots_total | 17.2500 +- 0.8292 [worst 18.0000] | 18.0000 |
| destroyed_value | 1665.7750 +- 83.3818 [worst 1542.9333] | 1542.9333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
