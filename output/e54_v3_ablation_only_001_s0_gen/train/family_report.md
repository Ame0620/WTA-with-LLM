# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_3x50_K10_s03.txt', 'dn_3x50_K10_s04.txt', 'dn_3x50_K10_s05.txt', 'dn_3x50_K10_s06.txt', 'dn_3x50_K10_s07.txt', 'dn_3x50_K10_s08.txt', 'dn_3x50_K10_s09.txt', 'dn_3x50_K10_s10.txt', 'dn_3x50_K10_s11.txt', 'dn_3x50_K10_s12.txt', 'dn_3x50_K10_s13.txt', 'dn_3x50_K10_s14.txt', 'dn_3x50_K10_s15.txt', 'dn_3x50_K10_s16.txt', 'dn_3x50_K10_s17.txt', 'dn_3x50_K10_s18.txt', 'dn_3x50_K10_s19.txt', 'dn_3x50_K10_s20.txt', 'dn_3x50_K10_s21.txt', 'dn_3x50_K10_s22.txt', 'dn_3x50_K10_s23.txt', 'dn_3x50_K10_s24.txt', 'dn_3x50_K10_s25.txt', 'dn_3x50_K10_s26.txt']) | policy: **ecmappo** | seeds: 30 (base 42) | solver timelimit 30s
- generated at: 2026-09-23 01:08:26

## Per-instance metrics (mean +- std over 30 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_3x50_K10_s03.txt` | 4116 | 0.5946 | n/a | 0.1444 | 92.0826 | 0.004 | 18.0 | 1668.6 | `87918eb67932` |
| `dn_3x50_K10_s04.txt` | 4203 | 0.5903 | n/a | 0.0709 | 99.2530 | 0.004 | 17.2 | 1722.1 | `0a95cb1fad3c` |
| `dn_3x50_K10_s05.txt` | 4828 | 0.6045 | n/a | 0.0685 | 106.4962 | 0.004 | 18.0 | 1909.4 | `3ab68ac9ee79` |
| `dn_3x50_K10_s06.txt` | 4126 | 0.6104 | n/a | 0.1093 | 89.1936 | 0.004 | 18.0 | 1607.4 | `226c79cf8d9a` |
| `dn_3x50_K10_s07.txt` | 4910 | 0.5914 | n/a | 0.1130 | 109.8710 | 0.004 | 18.0 | 2006.0 | `7911df0a5ea6` |
| `dn_3x50_K10_s08.txt` | 4385 | 0.4909 | n/a | 0.0037 | 123.8367 | 0.004 | 18.0 | 2232.3 | `b185bb307028` |
| `dn_3x50_K10_s09.txt` | 4246 | 0.5666 | n/a | 0.0537 | 100.9079 | 0.004 | 18.0 | 1840.1 | `56770c40db35` |
| `dn_3x50_K10_s10.txt` | 5241 | 0.6134 | n/a | 0.1059 | 116.4042 | 0.004 | 17.0 | 2026.2 | `fabd156d294c` |
| `dn_3x50_K10_s11.txt` | 4367 | 0.5860 | n/a | 0.0500 | 99.4510 | 0.004 | 18.0 | 1808.1 | `706f04ba1cff` |
| `dn_3x50_K10_s12.txt` | 5051 | 0.6001 | n/a | 0.1094 | 125.7208 | 0.004 | 17.1 | 2019.9 | `18df9ba75ca7` |
| `dn_3x50_K10_s13.txt` | 4377 | 0.5724 | n/a | 0.1463 | 103.1150 | 0.004 | 18.0 | 1871.7 | `440c363cf0b1` |
| `dn_3x50_K10_s14.txt` | 3997 | 0.5855 | n/a | 0.1611 | 91.4681 | 0.004 | 18.0 | 1656.6 | `aae70d5d1e23` |
| `dn_3x50_K10_s15.txt` | 4154 | 0.6067 | n/a | 0.0944 | 94.1166 | 0.004 | 18.0 | 1633.9 | `d83707eb56aa` |
| `dn_3x50_K10_s16.txt` | 4159 | 0.5371 | n/a | 0.0111 | 106.1707 | 0.004 | 18.0 | 1925.0 | `3ead4d3a06c2` |
| `dn_3x50_K10_s17.txt` | 4312 | 0.6120 | n/a | 0.2574 | 91.6871 | 0.004 | 18.0 | 1672.9 | `b5fd778717b1` |
| `dn_3x50_K10_s18.txt` | 4294 | 0.5824 | n/a | 0.1019 | 105.4636 | 0.004 | 18.0 | 1793.4 | `62cf1abab612` |
| `dn_3x50_K10_s19.txt` | 4236 | 0.5607 | n/a | 0.1019 | 103.0339 | 0.004 | 18.0 | 1860.9 | `12d9b2837933` |
| `dn_3x50_K10_s20.txt` | 3766 | 0.5367 | n/a | 0.1630 | 95.2012 | 0.004 | 18.0 | 1744.9 | `a71e6f017d48` |
| `dn_3x50_K10_s21.txt` | 3743 | 0.5584 | n/a | 0.1611 | 91.9822 | 0.004 | 18.0 | 1653.1 | `a17f79e4838b` |
| `dn_3x50_K10_s22.txt` | 4635 | 0.5561 | n/a | 0.0537 | 113.6190 | 0.004 | 18.0 | 2057.7 | `6ad456267385` |
| `dn_3x50_K10_s23.txt` | 4764 | 0.6278 | n/a | 0.1463 | 98.0744 | 0.004 | 18.0 | 1773.1 | `5ea0ad87a2f6` |
| `dn_3x50_K10_s24.txt` | 4450 | 0.5385 | n/a | 0.0074 | 113.6779 | 0.004 | 18.0 | 2053.7 | `7d313bda1584` |
| `dn_3x50_K10_s25.txt` | 3749 | 0.5580 | n/a | 0.0815 | 91.5783 | 0.004 | 18.0 | 1657.2 | `65143573c260` |
| `dn_3x50_K10_s26.txt` | 4694 | 0.5953 | n/a | 0.0519 | 104.9879 | 0.004 | 18.0 | 1899.7 | `33c0953e9abd` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.5782 +- 0.0311 [worst 0.6278] | 0.6278 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.0987 +- 0.0577 [worst 0.2574] | 0.2574 |
| ammo_efficiency | 102.8080 +- 10.1101 [worst 89.1936] | 89.1936 |
| latency_p50 | 0.0036 +- 0.0000 [worst 0.0037] | 0.0037 |
| latency_p90 | 0.0039 +- 0.0006 [worst 0.0065] | 0.0065 |
| shots_total | 17.8861 +- 0.3028 [worst 18.0000] | 18.0000 |
| destroyed_value | 1837.2347 +- 163.9182 [worst 1607.4333] | 1607.4333 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
