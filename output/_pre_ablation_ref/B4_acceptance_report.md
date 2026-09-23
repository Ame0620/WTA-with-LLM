# B.4 全关达标验收记录((0,0,0) = MAPPO⁰)

日期: 2026-09-19
命令: `marl/train.py --data-dir data/dn-data-v5 --seed 0 --iters 200 --episodes-per-iter 48 --eval-every 25 --use-dcca 0 --use-eaps 0 --use-casp 0 --output output/_pre_ablation_ref/b4_000_check`
产物: `output/_pre_ablation_ref/b4_000_check/`(best.pt / last.pt / train_log.jsonl / train_summary.json)

## 结论: PASS(①②③④全部通过)

| 检查项 | 结果 | 证据 |
|---|---|---|
| ① 从头训练 200 iters 无 NaN | PASS | train_log.jsonl 全部字段 finite(NaN 扫描 NONE);exit 0,首行位向量 `(0,0,0)` |
| ① 零非法动作 | PASS | 全部 8 个 eval 点 illegal_actions = 0;episode 级 15 runs 亦为 0 |
| ① shots_total ≤ 70 / ammo_end ≥ 0 | PASS | 3 train 实例 × 5 seeds(42–46)贪心评估:0 超限、0 负弹药 |
| ① 学习曲线存在 | PASS | train_leak 0.6803→0.5737 单调下降;val_leak_mean 1.0→0.7499(仍在改善) |
| ② credit 不注入个体优势 | PASS | S2 审计 C 组(张量级):DCCA 关时 adv_indiv == adv_team;本轮 train_log adv_indiv_over_team_std = 1.0 |
| ② Φ 势差不进奖励序列 | PASS | S2 审计 C 组:EAPS 关时 R_shaped == R_team 逐位相等;本轮 reward_nonzero_ratio == reward_nonzero_ratio_base = 0.9089 |
| ② Critic 动作块不构建 | PASS | ckpt critic_type='state_value',params_critic=4929(StateCritic,无动作块);S2 审计 B 组结构断言 |
| ③ 个体优势 = 共享团队 GAE | PASS | 同上 adv_indiv == adv_team(S2 C 组 + 本轮比值 1.0) |
| ④ R1 不与 train_mappo.py 产物比对 | PASS | 全程未做任何此类比较 |

## 结构与机制元数据(best.pt)
- ablation = {use_dcca:0, use_eaps:0, use_casp:0};actor_type='pool_mlp'(x_dim=8, drop_m1=True, 10242 params);critic_type='state_value'(4929 params)
- 速率:wall 1536.9s / 200 iters = 7.68 s/iter(供 S5 定档)
