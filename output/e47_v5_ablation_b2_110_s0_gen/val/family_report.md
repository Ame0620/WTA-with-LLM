# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_10x100_K10_s27.txt', 'dn_10x100_K10_s28.txt', 'dn_10x100_K10_s29.txt', 'dn_10x100_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:39:11

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s27.txt` | 8180 | 0.5218 | n/a | 0.3183 | 57.1772 | 0.015 | 68.2 | 3911.6 | `e7119f515b40` |
| `dn_10x100_K10_s28.txt` | 8560 | 0.4122 | n/a | 0.2552 | 71.5475 | 0.015 | 70.0 | 5031.6 | `2f7ec7c48d7f` |
| `dn_10x100_K10_s29.txt` | 8553 | 0.4889 | n/a | 0.2352 | 62.4727 | 0.015 | 70.0 | 4371.1 | `dfc4e18ae589` |
| `dn_10x100_K10_s30.txt` | 8397 | 0.4564 | n/a | 0.2724 | 65.4771 | 0.015 | 70.0 | 4564.9 | `e100504bc73f` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4698 +- 0.0405 [worst 0.5218] | 0.5218 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.2703 +- 0.0307 [worst 0.3183] | 0.3183 |
| ammo_efficiency | 64.1686 +- 5.1941 [worst 57.1772] | 57.1772 |
| latency_p50 | 0.0149 +- 0.0001 [worst 0.0151] | 0.0151 |
| latency_p90 | 0.0168 +- 0.0016 [worst 0.0195] | 0.0195 |
| shots_total | 69.5417 +- 0.7939 [worst 70.0000] | 70.0000 |
| destroyed_value | 4469.7917 +- 401.8799 [worst 3911.6000] | 3911.6000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
