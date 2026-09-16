# E17-A4 BC 热启动报告

- 教师: greedy (dwta.dn_policies)，TRAIN split s03-s26
- 数据: 112 episodes -> 3024 样本（丢弃 0 个 inf 幅角/不可见槽位，0 空步）
- 训练: 200 步 x batch 64, Adam lr 0.001, clip 0.5
- 拟合: train top-1 agreement 0.6452, holdout 0.6604, final CE 0.9083
- 在线: kills/ep 教师 10.45 vs BC 12.80 (ratio 1.225, 门禁≥0.95: PASS)
- 注: 方案 7.1.1 的 51.6 门禁属 wta-main 大场景协议；此处采用本仓库协议的相对门禁 (≥95% 教师)
