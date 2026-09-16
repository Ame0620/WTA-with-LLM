"""E17-A4: greedy-teacher behaviour-cloning warm start for MarlNet.

Why: e14/e15 start from a random actor; the greedy teacher already knows
a decent firing policy (leak ~0.61 on this family). BC gives the actor a
sane prior so PPO spends its budget refining rather than discovering.

Data: the teacher (dwta.dn_policies greedy) runs episodes on the TRAIN
split only; at every decision step the STUDENT-side features are rebuilt
exactly the way MarlPolicy.act builds them (perceive.AgentMemory.update
-> build_inputs -> masking.feasible_mask over alive_ids). Labels are the
teacher's env-corrected actions (env.run flips illegal choices to hold;
the wrapper replicates that correction BEFORE labelling). A teacher pick
that lands on a student-infeasible slot (inf-argument target) cannot be
imitated under the student's mask and is DROPPED (counted + reported) -
this is the spec's "can_fire masking of inf-argument slots".

Train: masked cross-entropy, Adam lr 1e-3, grad-clip 0.5, 800 steps x
batch 64 (= 51200 sample passes, spec table 5.4). Uses the A1
forward_batch so the whole batch is one forward.

Output: <output>/bc_init.pt (MarlPolicy-compatible ckpt), bc_report.md,
bc_data_stats.json.

Gate (spec 7.1.1, adapted to this repo's 3x50_K10 protocol): BC-online
kills/episode >= 95% of the teacher's kills/episode on the same split
(the literal 51.6 number belongs to the larger dn_env protocol in
wta-main); top-1 agreement reported alongside. Not a hard blocker for
e17 per the plan.
"""

import argparse
import json
import os
import sys

import torch

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(HERE)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from dwta.dn_instance import DNInstance                     # noqa: E402
from dwta.dn_env import DNEnv                               # noqa: E402
from dwta.dn_policies import build_policy                   # noqa: E402
from marl.perceive import AgentMemory, build_inputs         # noqa: E402
from marl.masking import feasible_mask                      # noqa: E402
from marl.network import MarlNet, assert_params             # noqa: E402
from marl.policy import MarlPolicy                          # noqa: E402

DATA_DIR = os.path.join(PROJECT_ROOT, "data", "dn-data-v3")
TRAIN_INSTS = ["dn_3x50_K10_s%02d.txt" % s for s in range(3, 27)]
HOLDOUT_INSTS = ["dn_3x50_K10_s%02d.txt" % s for s in range(27, 31)]


# ----------------------------------------------------------------------
# teacher rollout + student-view sample collection
# ----------------------------------------------------------------------

class _TeacherWrap(object):
    """Runs the greedy teacher; collects one STUDENT-view sample per
    (step, agent) with the env-corrected teacher action as label."""

    def __init__(self, teacher):
        self.teacher = teacher
        self.mems = None
        self.samples = []
        self.n_dropped = 0            # teacher picked a masked slot
        self.n_empty = 0              # no alive targets -> trivial hold

    def reset(self, m):
        self.mems = [AgentMemory() for _ in range(m)]

    def act(self, env, t):
        actions, info = self.teacher.act(env, t)
        dn = env.dn
        # replicate env.run's legality correction (illegal -> hold)
        for i in range(dn.m):
            j = actions.get(i)
            if j is not None and not env.can_fire(i, j, t):
                actions[i] = None
        for i in range(dn.m):
            obs_i = env.get_observation(i, t)
            mem = self.mems[i]
            mem.update(obs_i, t)
            feats = build_inputs(obs_i, mem, dn)
            alive_ids = feats["alive_ids"]
            if not alive_ids:
                self.n_empty += 1
                continue
            full_mask = feasible_mask(obs_i, t, dn)
            ok_by_id = {tr["id"]: ok for tr, ok in
                        zip(obs_i["targets"], full_mask)}
            mask = [ok_by_id[j] for j in alive_ids]
            j_act = actions.get(i)
            if j_act is None:
                label = 0
            elif j_act not in alive_ids:
                # teacher engaged something the student cannot even see
                # alive -> not imitable; drop
                self.n_dropped += 1
                continue
            else:
                label = 1 + alive_ids.index(j_act)
                if not mask[label - 1]:
                    # inf-argument slot: student mask forbids it -> drop
                    self.n_dropped += 1
                    continue
            self.samples.append({
                "x": feats["x"], "q": feats["q"], "g": feats["g"],
                "mask": torch.tensor(mask, dtype=torch.bool),
                "label": label,
            })
        # mirror MarlPolicy private-memory registration
        for i, j in actions.items():
            if j is not None:
                self.mems[i].note_own_shot(j, t)
        return actions, info


def collect_dataset(instances, seed0, target_steps, max_episodes):
    teacher = build_policy("greedy")
    wrap = _TeacherWrap(teacher)
    n_ep = 0
    for seed in range(seed0, seed0 + 100000):
        if len(wrap.samples) >= target_steps or n_ep >= max_episodes:
            break
        name = instances[n_ep % len(instances)]
        dn = DNInstance(os.path.join(DATA_DIR, name))
        env = DNEnv(dn, seed)
        wrap.reset(dn.m)
        env.run(wrap)
        n_ep += 1
    return wrap, n_ep


# ----------------------------------------------------------------------
# BC training
# ----------------------------------------------------------------------

def train_bc(samples, steps, batch, lr, clip, seed, device="cpu"):
    torch.manual_seed(seed)
    net = MarlNet().to(device)
    net.train()
    opt = torch.optim.Adam(net.parameters(), lr=lr)
    n = len(samples)
    g = torch.Generator().manual_seed(seed + 1)
    losses = []
    for _step in range(steps):
        idx = torch.randint(0, n, (batch,), generator=g).tolist()
        batch_s = [samples[k] for k in idx]
        Lmax = max(s["x"].shape[0] for s in batch_s)
        B = len(batch_s)
        xb = torch.zeros(B, Lmax, 10)
        pb = torch.zeros(B, Lmax, dtype=torch.bool)
        mb = torch.zeros(B, Lmax, dtype=torch.bool)
        for b, s in enumerate(batch_s):
            L = s["x"].shape[0]
            xb[b, :L] = s["x"]
            pb[b, :L] = True
            mb[b, :L] = s["mask"]
        qb = torch.stack([s["q"] for s in batch_s])
        gb = torch.stack([s["g"] for s in batch_s])
        labels = torch.tensor([s["label"] for s in batch_s],
                              dtype=torch.long)
        logits = net.forward_batch(xb.to(device), qb.to(device),
                                   gb.to(device), pb.to(device))
        feas = torch.cat([torch.ones(B, 1, dtype=torch.bool,
                                     device=device),
                          mb.to(device)], dim=1)
        masked = logits.masked_fill(~feas, -float("inf"))
        logp = torch.log_softmax(masked, dim=1)
        loss = -logp.gather(1, labels.to(device).unsqueeze(1)
                            ).squeeze(1).mean()
        opt.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(net.parameters(), clip)
        opt.step()
        losses.append(float(loss.item()))
    return net, losses


@torch.no_grad()
def eval_agreement(net, samples, device="cpu", batch=256):
    """Masked top-1 agreement with the teacher on held-out samples."""
    net.eval()
    agree = tot = 0
    for s0 in range(0, len(samples), batch):
        chunk = samples[s0:s0 + batch]
        B = len(chunk)
        Lmax = max(s["x"].shape[0] for s in chunk)
        xb = torch.zeros(B, Lmax, 10)
        pb = torch.zeros(B, Lmax, dtype=torch.bool)
        mb = torch.zeros(B, Lmax, dtype=torch.bool)
        for b, s in enumerate(chunk):
            L = s["x"].shape[0]
            xb[b, :L] = s["x"]
            pb[b, :L] = True
            mb[b, :L] = s["mask"]
        qb = torch.stack([s["q"] for s in chunk])
        gb = torch.stack([s["g"] for s in chunk])
        logits = net.forward_batch(xb.to(device), qb.to(device),
                                   gb.to(device), pb.to(device))
        feas = torch.cat([torch.ones(B, 1, dtype=torch.bool,
                                     device=device),
                          mb.to(device)], dim=1)
        masked = logits.masked_fill(~feas, -float("inf"))
        pred = masked.argmax(dim=1).cpu()
        labels = torch.tensor([s["label"] for s in chunk])
        agree += int((pred == labels).sum().item())
        tot += B
    return agree / max(1, tot)


def _policy_kills_per_ep(ckpt_path, instances, seeds, device):
    """Online kills/episode for a ckpt under the MarlPolicy greedy."""
    pol = MarlPolicy(model_path=ckpt_path, device=device, greedy=True,
                     seed=0)
    kills = []
    for name in instances:
        dn = DNInstance(os.path.join(DATA_DIR, name))
        for seed in seeds:
            env = DNEnv(dn, seed)
            pol.reset_episode()
            rec = env.run(pol)
            kills.append(len(rec.get("destroyed_ids", [])))
    return sum(kills) / max(1, len(kills))


def _teacher_kills_per_ep(instances, seeds):
    teacher = build_policy("greedy")
    kills = []
    for name in instances:
        dn = DNInstance(os.path.join(DATA_DIR, name))
        for seed in seeds:
            env = DNEnv(dn, seed)
            rec = env.run(teacher)
            kills.append(len(rec.get("destroyed_ids", [])))
    return sum(kills) / max(1, len(kills))


# ----------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description="E17-A4 BC warm start")
    ap.add_argument("--target-steps", type=int, default=40000,
                    help="stop collecting once this many decision "
                         "samples exist")
    ap.add_argument("--max-episodes", type=int, default=2000)
    ap.add_argument("--seed0", type=int, default=1000,
                    help="first teacher episode seed")
    ap.add_argument("--steps", type=int, default=800)
    ap.add_argument("--batch", type=int, default=64)
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--clip", type=float, default=0.5)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--device", default="cpu")
    ap.add_argument("--output", default=os.path.join(
        PROJECT_ROOT, "output", "e17_bc"))
    args = ap.parse_args(argv)
    os.makedirs(args.output, exist_ok=True)
    dev = torch.device(args.device)

    print("[bc] collecting teacher data (target %d steps) ..."
          % args.target_steps, flush=True)
    wrap, n_ep = collect_dataset(TRAIN_INSTS, args.seed0,
                                 args.target_steps, args.max_episodes)
    samples = wrap.samples
    print("[bc] %d episodes -> %d samples (dropped %d masked-slot "
          "picks, %d empty steps)" % (n_ep, len(samples), wrap.n_dropped,
                                      wrap.n_empty), flush=True)

    hold_wrap, hold_ep = collect_dataset(HOLDOUT_INSTS, args.seed0 + 5000,
                                         6000, 200)
    hold = hold_wrap.samples
    print("[bc] holdout: %d episodes -> %d samples"
          % (hold_ep, len(hold)), flush=True)

    net, losses = train_bc(samples, args.steps, args.batch, args.lr,
                           args.clip, args.seed, dev)
    agree_train = eval_agreement(net, samples, dev)
    agree_hold = eval_agreement(net, hold, dev)
    print("[bc] agreement train %.4f | holdout %.4f | final CE %.4f"
          % (agree_train, agree_hold, losses[-1]), flush=True)

    ckpt_path = os.path.join(args.output, "bc_init.pt")
    torch.save({
        "state_dict": net.state_dict(),
        "feature_spec": {"x": 10, "q": 5, "g": 3},
        "params_count": assert_params(net),
        "bc_stats": {"episodes": n_ep, "samples": len(samples),
                     "dropped": wrap.n_dropped,
                     "agree_train": agree_train,
                     "agree_holdout": agree_hold,
                     "final_ce": losses[-1]},
    }, ckpt_path)

    # online kills/episode: student vs teacher on the holdout split
    seeds = list(range(42, 47))
    t_kills = _teacher_kills_per_ep(HOLDOUT_INSTS, seeds)
    s_kills = _policy_kills_per_ep(ckpt_path, HOLDOUT_INSTS, seeds,
                                   args.device)
    ratio = s_kills / max(1e-9, t_kills)
    gate = ratio >= 0.95
    print("[bc] online kills/ep: teacher %.2f | BC %.2f | ratio %.3f "
          "(gate >=0.95: %s)" % (t_kills, s_kills, ratio,
                                 "PASS" if gate else "FAIL"), flush=True)

    with open(os.path.join(args.output, "bc_report.md"), "w") as f:
        f.write("# E17-A4 BC 热启动报告\n\n"
                "- 教师: greedy (dwta.dn_policies)，TRAIN split s03-s26\n"
                "- 数据: %d episodes -> %d 样本（丢弃 %d 个 inf 幅角/"
                "不可见槽位，%d 空步）\n"
                "- 训练: %d 步 x batch %d, Adam lr %g, clip %g\n"
                "- 拟合: train top-1 agreement %.4f, holdout %.4f, "
                "final CE %.4f\n"
                "- 在线: kills/ep 教师 %.2f vs BC %.2f (ratio %.3f, "
                "门禁≥0.95: %s)\n"
                "- 注: 方案 7.1.1 的 51.6 门禁属 wta-main 大场景协议；"
                "此处采用本仓库协议的相对门禁 (≥95%% 教师)\n"
                % (n_ep, len(samples), wrap.n_dropped, wrap.n_empty,
                   args.steps, args.batch, args.lr, args.clip,
                   agree_train, agree_hold, losses[-1],
                   t_kills, s_kills, ratio,
                   "PASS" if gate else "FAIL"))
    with open(os.path.join(args.output, "bc_data_stats.json"), "w") as f:
        json.dump({"episodes": n_ep, "samples": len(samples),
                   "dropped": wrap.n_dropped, "empty": wrap.n_empty,
                   "agree_train": agree_train,
                   "agree_holdout": agree_hold,
                   "teacher_kills_per_ep": t_kills,
                   "bc_kills_per_ep": s_kills,
                   "online_ratio": ratio, "gate_pass": gate,
                   "loss_first": losses[0], "loss_last": losses[-1]},
                  f, indent=2)
    print("[bc] ckpt -> %s" % ckpt_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
