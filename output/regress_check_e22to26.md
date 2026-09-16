# 回归核查记录（E22-E26 基线扩展后）

日期: 2026-09-08 | 命令: 按锁定 argv 全量重跑（--split test --seeds 30 --timelimit 30）
输出: /tmp/regress_check/{greedy,pocplex,cplex} | 锁定: output/fix_regress/*

| policy | instance | result_hash (重跑 = 锁定) |
|---|---|---|
| greedy | dn_3x50_K10_s01.txt | d96c7504044db3d4b78974f5fc0cd96dc3dcd634e6081d6dbefe3dd0f9cef32c |
| greedy | dn_3x50_K10_s02.txt | 3446b7a8f98628cfd34a44a56fb48e59b7153a6805d3cc7c491b49cd73d5b975 |
| pocplex | dn_3x50_K10_s01.txt | df512d01e5030e9b1b15b1470ee197239544fdaa5918bbcab310ebe7fb155fe1 |
| pocplex | dn_3x50_K10_s02.txt | 96d35c879acd46d7ca19de705f26d9979192ee82b87e16345dd5a56e27a712f4 |
| cplex | dn_3x50_K10_s01.txt | df512d01e5030e9b1b15b1470ee197239544fdaa5918bbcab310ebe7fb155fe1 |
| cplex | dn_3x50_K10_s02.txt | 96d35c879acd46d7ca19de705f26d9979192ee82b87e16345dd5a56e27a712f4 |

结论: ALL PASS（6/6 result_hash 逐位一致，既有五策略行为未被 E22-E26 改动波及）
