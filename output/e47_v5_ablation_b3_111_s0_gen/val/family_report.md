# DN-WTA v3 family evaluation report

- split: **val** (4 instances: ['dn_10x100_K10_s27.txt', 'dn_10x100_K10_s28.txt', 'dn_10x100_K10_s29.txt', 'dn_10x100_K10_s30.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-20 13:12:07

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s27.txt` | 8180 | 0.5004 | n/a | 0.3789 | 61.8858 | 0.022 | 66.3 | 4087.0 | `5e89813dc660` |
| `dn_10x100_K10_s28.txt` | 8560 | 0.4144 | n/a | 0.3060 | 75.6628 | 0.019 | 66.5 | 5012.5 | `97298b31782b` |
| `dn_10x100_K10_s29.txt` | 8553 | 0.4333 | n/a | 0.2943 | 70.5561 | 0.019 | 68.7 | 4847.0 | `9d8b5f391db3` |
| `dn_10x100_K10_s30.txt` | 8397 | 0.4401 | n/a | 0.3119 | 67.2193 | 0.018 | 70.0 | 4701.7 | `26466e5dd932` |

## Family aggregates (across 4 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4470 +- 0.0322 [worst 0.5004] | 0.5004 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3228 +- 0.0330 [worst 0.3789] | 0.3789 |
| ammo_efficiency | 68.8310 +- 5.0121 [worst 61.8858] | 61.8858 |
| latency_p50 | 0.0197 +- 0.0015 [worst 0.0222] | 0.0222 |
| latency_p90 | 0.0231 +- 0.0033 [worst 0.0287] | 0.0287 |
| shots_total | 67.8833 +- 1.5502 [worst 70.0000] | 70.0000 |
| destroyed_value | 4662.0500 +- 349.7561 [worst 4086.9667] | 4086.9667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
