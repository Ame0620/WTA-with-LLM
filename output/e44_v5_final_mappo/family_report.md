# DN-WTA v3 family evaluation report

- split: **test** (2 instances: ['dn_10x100_K10_s01.txt', 'dn_10x100_K10_s02.txt']) | policy: **mappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 23:13:52

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s01.txt` | 8157 | 0.5410 | 2.3567 | 0.3932 | 53.9372 | 0.734 | 69.0 | 3744.5 | `a5056b7cdeb6` |
| `dn_10x100_K10_s02.txt` | 7616 | 0.4028 | 1.6499 | 0.2852 | 64.9658 | 0.710 | 70.0 | 4547.9 | `6671cf43f24c` |

## Family aggregates (across 2 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4719 +- 0.0691 [worst 0.5410] | 0.5410 |
| gap_mean | 2.0033 +- 0.3534 [worst 2.3567] | 2.3567 |
| invalid_engagement_rate | 0.3392 +- 0.0540 [worst 0.3932] | 0.3932 |
| ammo_efficiency | 59.4515 +- 5.5143 [worst 53.9372] | 53.9372 |
| latency_p50 | 0.7217 +- 0.0119 [worst 0.7337] | 0.7337 |
| latency_p90 | 0.9036 +- 0.0320 [worst 0.9356] | 0.9356 |
| shots_total | 69.5000 +- 0.5000 [worst 70.0000] | 70.0000 |
| destroyed_value | 4146.2000 +- 401.7333 [worst 3744.4667] | 3744.4667 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
