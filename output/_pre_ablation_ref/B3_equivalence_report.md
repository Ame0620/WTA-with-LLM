# B.3 等价性验证记录(全开 (1,1,1) vs 改造前基线)

日期: 2026-09-19
基线: git worktree /tmp/uas_premod_wt @ 39e24a7("pre-modification")
对照: 改造后主树(三开关默认全开)相同超参重训(seed=0, iters=50, epi=48)

## 结论: PASS(全部子项)

| 检查项 | 结果 | 细节 |
|---|---|---|
| ① 训练曲线逐 eval 点一致 | PASS | train_log.jsonl 全部指标 max rel diff = 0.0 |
| ② best.pt/last.pt 学习状态位级一致 | PASS | state_dict/critic_state_dict/opt_a/opt_c(递归含嵌套 optimizer state)/seed_counter/eval_points/best_val/env_steps/iter/params_count 全部位级相等 |
| ②' 允许差异(设计内) | — | last.pt: `elapsed_sec`(墙钟 558.7s vs 448.6s);recheck 新增元数据键 ablation/actor_type/critic_type/train_seed/budget/versions(设计要求的检查点元数据);feature_spec 新增 `drop_m1:False`(结构文档化字段,(1,1,1) → MarlNet x_dim=10 不丢弃 m1,与基线一致) |
| ③ 固定权重 batch probe | PASS | 两代码库下加载 S0 best.pt → 4 episodes collect + process_batch:R_shaped/R_team/credit/adv/ret/logp_old(共 360 flat 条目)全部逐位相等(/tmp/b3_probe_premod.json vs /tmp/b3_probe_mod.json) |
| ④ 短程终评 3 seeds result_hash | PASS | test s01/s02 × seeds{42,43,44}:每实例 result_hash 相等(s01: 29b6aa43d481dbc8...);完整轨迹逐位相等,唯一差异为 steps[].wall_time(墙钟,hash 已排除) |

## 环境注记
- pre-mod 侧通过 git worktree 运行,主树未回退
- 两侧行为均为 50-iter 早期检查点在 test 上零射击(策略尚未学会开火,leak=1.0)——等价性关注一致性而非质量,符合预期
