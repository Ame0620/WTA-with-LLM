# E15-A1 PPO batch 化：门禁与基准

## 等价性门禁（PASS）

单次 `ppo_update` 等价性：同一权重快照 + 同一批 flat（n=216，seed=0 采集，
torch.manual_seed(7) 对齐 randperm），恢复快照后分别走 `_ppo_update_loop`
（--no-batched 旧路径）与 `_ppo_update_batched`（新路径）：

| 指标 | loop | batched | 相对误差/差值 | 门禁 |
|---|---:|---:|---:|---|
| policy_loss | -0.02108761 | -0.02108762 | 1.77e-07 | <1e-4 PASS |
| v_loss | 0.27447083 | 0.27447082 | 4.00e-08 | <1e-4 PASS |
| max abs ΔW_actor | — | — | 2.94e-06 | 浮点归约噪声 |
| max abs ΔW_critic | — | — | 2.98e-08 | 浮点归约噪声 |

`marl/network.py` selftest：forward_batch 与逐样本 forward 在 ragged L∈{1,4,9,3,6}
下 logits allclose（atol 1e-5），pad 槽位 -inf，params=28482 不变。

20 iters 轨迹对比（seed 0）：两路径 val 曲线均正常下降（batched 0.7038 /
loop 0.8458 @20 iters）；逐点 policy_loss 因 PPO 混沌动力学从 1e-7 浮点噪声
指数放大而不可逐位对齐（预期内），等价性以单次 update 为准。

实现注记（两处非显然修复）：
1. `forward_batch` 的 key_padding_mask 拼接顺序必须为 `[~pad_mask, zeros(B,2)]`
   （target tokens 在前，platform/global tokens 恒有效）。
2. 批式熵项不能直接 `where(fin, exp(lp)*lp, 0)`——未选中分支的反向梯度
   `0 * (-inf) = NaN` 仍会污染 autograd；须先把 logp 中 -inf 置 0 再相乘
   （`lp_safe = where(fin, lp, 0); pent = exp(lp_safe)*lp_safe`）。

## 加速比

| 配置 | 20 iters 墙钟 | 每 iter | vs e14 |
|---|---:|---:|---:|
| e14（MPS, per-sample loop） | ~1200s | ~60s | 1× |
| CPU per-sample loop | 28s | 1.4s | 43× |
| **CPU batched（e15 采用）** | **7s** | **0.35s** | **~170×** |
| MPS batched | 35s | 1.75s | 34× |

结论：模型小（28k 参数），CPU 批式反而最快；e15 正式训练用
`--device cpu`（默认批式路径）。MPS 批式路径保留且验证可用（val 0.8427），
process_batch/critic 的 MPS RuntimeError CPU-fallback 保留。

## e15 训练命令（A2 后）

    python marl/train.py --device cpu --seed 0 \
        --iters 3000 --eval-every 25 --patience 60 \
        --episodes-per-iter 128 \
        --output output/e15_train
