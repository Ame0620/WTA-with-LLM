# DN-WTA v3 family evaluation report

- split: **train** (24 instances: ['dn_10x100_K10_s03.txt', 'dn_10x100_K10_s04.txt', 'dn_10x100_K10_s05.txt', 'dn_10x100_K10_s06.txt', 'dn_10x100_K10_s07.txt', 'dn_10x100_K10_s08.txt', 'dn_10x100_K10_s09.txt', 'dn_10x100_K10_s10.txt', 'dn_10x100_K10_s11.txt', 'dn_10x100_K10_s12.txt', 'dn_10x100_K10_s13.txt', 'dn_10x100_K10_s14.txt', 'dn_10x100_K10_s15.txt', 'dn_10x100_K10_s16.txt', 'dn_10x100_K10_s17.txt', 'dn_10x100_K10_s18.txt', 'dn_10x100_K10_s19.txt', 'dn_10x100_K10_s20.txt', 'dn_10x100_K10_s21.txt', 'dn_10x100_K10_s22.txt', 'dn_10x100_K10_s23.txt', 'dn_10x100_K10_s24.txt', 'dn_10x100_K10_s25.txt', 'dn_10x100_K10_s26.txt']) | policy: **ecmappo** | seeds: 10 (base 42) | solver timelimit 30s
- generated at: 2026-09-19 06:54:26

## Per-instance metrics (mean +- std over 10 MC seeds)

| instance | total value | leak rate | gap mean | invalid | ammo eff | latency p50 (s) | shots | destroyed value | result hash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `dn_10x100_K10_s03.txt` | 8419 | 0.4565 | n/a | 0.2814 | 66.5526 | 0.013 | 70.0 | 4575.7 | `133bb58c74f8` |
| `dn_10x100_K10_s04.txt` | 8817 | 0.4330 | n/a | 0.2757 | 73.3419 | 0.012 | 68.2 | 4999.1 | `d0d76031a91c` |
| `dn_10x100_K10_s05.txt` | 10196 | 0.4755 | n/a | 0.2742 | 87.3471 | 0.013 | 62.0 | 5348.2 | `edc4fe9242f9` |
| `dn_10x100_K10_s06.txt` | 8176 | 0.4137 | n/a | 0.3357 | 68.6405 | 0.012 | 70.0 | 4793.9 | `034c3ca63ef7` |
| `dn_10x100_K10_s07.txt` | 8985 | 0.4506 | n/a | 0.3386 | 70.7640 | 0.014 | 70.0 | 4936.4 | `6fb7780f4944` |
| `dn_10x100_K10_s08.txt` | 9141 | 0.4676 | n/a | 0.4204 | 70.1265 | 0.013 | 69.7 | 4866.5 | `8946714eebbe` |
| `dn_10x100_K10_s09.txt` | 8511 | 0.4332 | n/a | 0.2586 | 69.4632 | 0.012 | 70.0 | 4824.2 | `52aeb06e9d49` |
| `dn_10x100_K10_s10.txt` | 9155 | 0.4472 | n/a | 0.3557 | 73.6757 | 0.013 | 70.0 | 5061.3 | `d7245aeb22ce` |
| `dn_10x100_K10_s11.txt` | 8850 | 0.4425 | n/a | 0.3329 | 71.5034 | 0.013 | 70.0 | 4934.1 | `d62f5b85025e` |
| `dn_10x100_K10_s12.txt` | 8909 | 0.4596 | n/a | 0.2829 | 68.3793 | 0.012 | 70.0 | 4814.8 | `f34572eb66f0` |
| `dn_10x100_K10_s13.txt` | 9905 | 0.4646 | n/a | 0.3588 | 79.3564 | 0.014 | 68.0 | 5302.7 | `dc8629d5b7ce` |
| `dn_10x100_K10_s14.txt` | 9190 | 0.4222 | n/a | 0.2925 | 80.6112 | 0.013 | 67.0 | 5309.8 | `b0de33624c02` |
| `dn_10x100_K10_s15.txt` | 7913 | 0.4056 | n/a | 0.2900 | 67.7582 | 0.012 | 70.0 | 4703.2 | `6293e67f7a43` |
| `dn_10x100_K10_s16.txt` | 8526 | 0.4885 | n/a | 0.3333 | 69.7957 | 0.014 | 63.0 | 4360.8 | `354eb966da79` |
| `dn_10x100_K10_s17.txt` | 9044 | 0.5197 | n/a | 0.3310 | 74.4653 | 0.013 | 58.0 | 4343.7 | `64113ce6f927` |
| `dn_10x100_K10_s18.txt` | 9002 | 0.4662 | n/a | 0.3114 | 69.4875 | 0.012 | 70.0 | 4805.3 | `c00871339928` |
| `dn_10x100_K10_s19.txt` | 8810 | 0.4192 | n/a | 0.2543 | 74.5037 | 0.013 | 70.0 | 5116.8 | `05b7af0eebdd` |
| `dn_10x100_K10_s20.txt` | 7875 | 0.3731 | n/a | 0.3157 | 70.5782 | 0.013 | 70.0 | 4936.5 | `7b6f9ebe5e7f` |
| `dn_10x100_K10_s21.txt` | 8376 | 0.4159 | n/a | 0.2629 | 70.5592 | 0.012 | 70.0 | 4892.3 | `7b17561bd783` |
| `dn_10x100_K10_s22.txt` | 9389 | 0.4516 | n/a | 0.2771 | 74.1966 | 0.013 | 70.0 | 5149.0 | `ef0e73b2c676` |
| `dn_10x100_K10_s23.txt` | 9402 | 0.4805 | n/a | 0.3100 | 70.0529 | 0.013 | 70.0 | 4884.0 | `11cfbd87f3a9` |
| `dn_10x100_K10_s24.txt` | 8684 | 0.3665 | n/a | 0.2814 | 78.5129 | 0.012 | 70.0 | 5501.6 | `d1984b20fd40` |
| `dn_10x100_K10_s25.txt` | 8264 | 0.4543 | n/a | 0.3357 | 65.1582 | 0.012 | 70.0 | 4509.9 | `87c2457aa8af` |
| `dn_10x100_K10_s26.txt` | 8976 | 0.4300 | n/a | 0.2329 | 74.1751 | 0.013 | 70.0 | 5116.5 | `4de92002b169` |

## Family aggregates (across 24 instances, per-key worst)

| metric | mean +- std | worst instance mean |
|---|---|---|
| leak_rate | 0.4432 +- 0.0341 [worst 0.5197] | 0.5197 |
| gap_mean | n/a | n/a |
| invalid_engagement_rate | 0.3060 +- 0.0411 [worst 0.4204] | 0.4204 |
| ammo_efficiency | 72.4586 +- 4.9047 [worst 65.1582] | 65.1582 |
| latency_p50 | 0.0127 +- 0.0007 [worst 0.0137] | 0.0137 |
| latency_p90 | 0.0139 +- 0.0020 [worst 0.0219] | 0.0219 |
| shots_total | 68.5792 +- 3.0610 [worst 70.0000] | 70.0000 |
| destroyed_value | 4920.2625 +- 289.3630 [worst 4343.7000] | 4343.7000 |

Notes: `gap mean` is the per-step optimality gap vs the centralised myopic CPLEX reference (0 by definition for the cplex policy; n/a when no reference runs); evaluation protocol and split are fixed by `data/dn-data-v3/MANIFEST.md`.
