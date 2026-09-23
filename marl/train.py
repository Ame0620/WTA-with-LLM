"""M6: CTDE training loop (MAPPO-style PPO) for the DN-WTA marl policy.

Training-side wrapper collects, per decision step:
    * actor inputs strictly from per-agent §7 observations (red line:
      the execution path never sees global state);
    * critic inputs from GLOBAL truth (env.inflight registry, true
      per-target occupancy column, B(t), t) - allowed here only.

Critic: state+joint-action conditioned V(s, a); counterfactual baselines
V(s, a_{-i}, hold_i) give each agent a COMA-style differential signal:
    A_i(t) = GAE_team(t) + kill_credit((t, i))
             + [V(s, a) - V(s, a_{-i}, hold_i)]

PPO: clip=0.2, entropy 0.01, GAE(lambda=0.95, gamma=0.99), Adam lr 3e-4,
32 episodes per batch (~864 joint samples), 4 epochs per update.

Early stop: val = s27-s30 x seeds 42-51 (leak rate only, no CPLEX),
evaluated every --eval-every iters, patience in EVAL POINTS.

Seed isolation: collection seeds from 100001 upward; eval 42-71; val 42-51.
Sampling temperature anneals 1.0 -> 0.5 over the first --anneal-iters.

Products (flat dir --output):
    best.pt            {state_dict, feature_spec, params_count}
    train_log.jsonl    one line per eval point
    train_summary.json {total_wall_sec, env_steps, params_count, best_val}

CLI (module-level, precedent experiments/*.py):
    python marl/train.py --iters 50 --eval-every 10 --device auto \
        --output output/e14_train_smoke
"""

import argparse
import json
import math
import os
import sys
import time

import torch
import torch.nn as nn

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(HERE)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from dwta.dn_instance import DNInstance                     # noqa: E402
from dwta.dn_env import DNEnv                               # noqa: E402
from marl.policy import MarlPolicy, _pick_device            # noqa: E402
from marl.network import MarlNet, assert_params             # noqa: E402
from marl.baseline_net import PoolMLPNet, StateCritic       # noqa: E402
from marl.reward import build_rewards, C_INVALID        # noqa: E402

DATA_DIR = os.path.join(PROJECT_ROOT, "data", "dn-data-v3")

# split file lists (fixed by MANIFEST)
TRAIN_INSTS = ["dn_3x50_K10_s%02d.txt" % s for s in range(3, 27)]
VAL_INSTS = ["dn_3x50_K10_s%02d.txt" % s for s in range(27, 31)]

# PPO hyper-parameters (locked by the implementation spec)
PPO_CLIP = 0.2
ENT_COEF = 0.01
GAE_LAMBDA = 0.95
GAMMA = 0.99
LR = 3e-4
EPISODES_PER_ITER = 32
PPO_EPOCHS = 2
MINIBATCH = 256
WALL_LIMIT_SEC = 24 * 3600.0     # default; v4 full tier passes --wall-limit 6


# ----------------------------------------------------------------------
# critic: global-state + joint-action value (training side ONLY)
# ----------------------------------------------------------------------

class CriticNet(nn.Module):
    """V(s, a): pooled true target features + global row + per-agent
    action summaries -> MLP -> scalar. n_agents is DERIVED from the
    dataset (v3: 3 -> 44-dim state, v4: 5 -> 50-dim state); the default
    keeps v3 checkpoints loadable."""

    def __init__(self, n_agents=3):
        super().__init__()
        self.n_agents = n_agents
        self.state_dim = 32 + 3 + 3 * n_agents
        self.tgt_proj = nn.Linear(5, 32)
        self.head = nn.Sequential(nn.Linear(self.state_dim, 128), nn.Tanh(),
                                  nn.Linear(128, 1))

    def forward(self, tgt, glob, act, tgt_mask=None):
        """tgt: [B, L, 5] (padded), glob: [B, 3], act: [B, 3m]. Returns [B]
        values.

        tgt_mask: [B, L] bool (True = real row). When given, pooling is a
        MASKED mean over real rows only - numerically equivalent to the
        per-sample mean of the unpadded matrix (A1 requirement); without a
        mask this stays the historical mean over dim=1 (0-safe fallback).
        """
        e = torch.tanh(self.tgt_proj(tgt))            # [B, L, 32]
        if tgt_mask is not None:
            m = tgt_mask.unsqueeze(-1).to(e.dtype)    # [B, L, 1]
            pooled = (e * m).sum(dim=1) / m.sum(dim=1).clamp(min=1.0)
        else:
            pooled = e.mean(dim=1)                    # [B, 32] (0-safe)
        z = torch.cat([pooled, glob, act], dim=-1)
        return self.head(z).squeeze(-1)


def _ceil_int(x, eps=1e-9):
    return int(math.ceil(x - eps))


# ----------------------------------------------------------------------
# training-side collectors (global truth - NOT part of the actor path)
# ----------------------------------------------------------------------

def critic_inputs(env, t, actions, dn):
    """Build the critic input tensors for one step (before fire)."""
    total = float(dn.total_value())
    pool0 = float(dn.m * dn.mu)
    rows = []
    for j in sorted(env.alive):
        occ = sum(1 for ev in env.inflight if ev["j"] == j)
        p_surv = 1.0
        for ev in env.inflight:
            if ev["j"] == j:
                p_surv *= (1.0 - ev["p_shot"])
        pbar = 1.0 - p_surv
        r = dn.r(j, t)
        rows.append([dn.w[j] / total,
                     r / max(1.0, float(dn.r0[j])),
                     min(1.0, occ / 6.0),
                     pbar,
                     occ * 0.0 + _ceil_int(r / dn.delta_d - 1e-9) / 10.0])
    if not rows:
        rows = [[0.0] * 5]
    tgt = torch.tensor(rows, dtype=torch.float32)
    glob = torch.tensor([env.pool / pool0, t / float(dn.K),
                         len(env.alive) / float(dn.n)], dtype=torch.float32)
    act_rows = []
    for i in range(dn.m):
        j = actions.get(i)
        if j is None:
            act_rows += [1.0, 0.0, 0.0]
        else:
            act_rows += [0.0, dn.w[j] / total, dn.p_eff(i, j, t)]
    act = torch.tensor(act_rows, dtype=torch.float32)
    return tgt, glob, act


# ----------------------------------------------------------------------
# main trainer
# ----------------------------------------------------------------------

class Trainer(object):
    """v5 ablation host (spec §3.1-§3.4).

    Three binary switches: --use-dcca / --use-eaps / --use-casp.
    All-open (1,1,1) is BIT-IDENTICAL to the pre-modification trainer:
    identical module construction order (MarlNet -> CriticNet ->
    MarlNet(eval_pol) -> MarlNet(collector)) and identical RNG
    consumption. The global torch RNG (module init + torch.randperm in
    the batched PPO shuffle) is now seeded explicitly inside __init__
    so runs are reproducible across processes; the S0 pre-modification
    baseline was run through an external driver seeding the same value
    before construction (equivalence audit, spec §4.2).
    """

    def __init__(self, args):
        self.args = args
        self.use_dcca = int(getattr(args, "use_dcca", 1))
        self.use_eaps = int(getattr(args, "use_eaps", 1))
        self.use_casp = int(getattr(args, "use_casp", 1))
        # r2 recalibration scalars (spec §3.1): lambda on the EAPS shaping
        # term, alpha on the kill-credit injection, beta on the cf-hold
        # diff - all default 1.0 = pre-r2 bit-identical (R1/R2).
        self.phi_scale = float(getattr(args, "phi_scale", 1.0))
        self.credit_alpha = float(getattr(args, "credit_alpha", 1.0))
        self.cf_beta = float(getattr(args, "cf_beta", 1.0))
        # v5 ablation determinism: seed the GLOBAL torch RNG (module
        # construction + torch.randperm in the batched PPO shuffle draw
        # from it). First statement, BEFORE any module construction, so
        # the RNG stream matches the S0 pre-modification driver exactly.
        torch.manual_seed(int(getattr(args, "seed", 0)))
        self.device = _pick_device(args.device)
        if self.use_casp:
            self.actor = MarlNet().to(self.device)
            self.actor_type = "set_attention"
            self.drop_m1 = False
            self.x_dim = 10
        else:
            # CASP off: pool-MLP actor over the 8-dim (M1-dropped) x -
            # structural reference baseline_net.PoolMLPNet (E24/E25
            # learning-baseline actor; same per-target rows, same
            # hold slot, no attention / M2 / M3 interaction modules).
            self.actor = PoolMLPNet().to(self.device)
            self.actor_type = "pool_mlp"
            self.drop_m1 = True
            self.x_dim = 8
        self.n_params = assert_params(self.actor)
        # v4 migration: split + n_agents derived from --data-dir
        from marl.data_split import discover_split, load_instances
        data_dir = getattr(args, "data_dir", None) or DATA_DIR
        train_files, val_files = discover_split(data_dir)
        self.train_dns = load_instances(data_dir, train_files)
        self.val_dns = load_instances(data_dir, val_files)
        self.n_agents = self.train_dns[0].m
        if self.use_dcca:
            self.critic = CriticNet(n_agents=self.n_agents).to(self.device)
            self.critic_type = "joint_action"
        else:
            # DCCA off: V(s) state-value critic - structural reference
            # baseline_net.StateCritic; the joint-action block is NOT
            # built, credit is NOT injected into individual advantages
            # and no counterfactual hold diff is computed.
            self.critic = StateCritic().to(self.device)
            self.critic_type = "state_value"
        self.n_params_critic = sum(
            p.numel() for p in self.critic.parameters() if p.requires_grad)
        assert 1e3 <= self.n_params_critic <= 1e5, (
            "[ablation] critic params %d outside [1e3, 1e5]"
            % self.n_params_critic)
        self.opt_a = torch.optim.Adam(self.actor.parameters(), lr=LR)
        self.opt_c = torch.optim.Adam(self.critic.parameters(), lr=LR)
        # evaluation policy (greedy, shares the actor module)
        self.eval_pol = MarlPolicy(model_path=None, device=args.device,
                                   greedy=True, seed=0,
                                   actor_type=self.actor_type,
                                   drop_m1=self.drop_m1)
        self.eval_pol.net = self.actor
        self.collector = MarlPolicy(model_path=None, device=args.device,
                                    greedy=False, seed=args.seed,
                                    training=True,
                                    actor_type=self.actor_type,
                                    drop_m1=self.drop_m1)
        self.collector.net = self.actor
        self.seed_counter = 100001
        self.env_steps = 0
        self.best_val = float("inf")
        self.log_path = os.path.join(args.output, "train_log.jsonl")
        self._log_f = open(self.log_path,
                           "a" if getattr(args, "resume", False) else "w")
        # ---- mechanism instrumentation accumulators (spec §3.6) ------
        # window = since the last eval point; pure reads of already
        # materialised floats - they never touch any RNG stream or
        # tensor value, so the (1,1,1) path stays bit-identical.
        self._mech = {
            "credit_slots": 0,          # firing slots total
            "credit_nonzero": 0,        # slots with nonzero credit
            "r_vals": [],               # all R_shaped step values
            "r_shaped_nz": 0, "r_team_nz": 0, "r_steps": 0,
            "adv_indiv": [], "adv_team": [],
            "wall_iters": [], "illegal_actions": 0,
            # r2 §3.4 mechanism instrumentation (pure reads):
            "shape_abs": 0.0,           # sum |lambda*phi_diff| = |R_shaped-R_team|
            "team_abs": 0.0,            # sum |R_team|
            "credit_abs": 0.0,          # sum |alpha*credit + beta*cf| (dcca)
            "gae_abs": 0.0,             # sum |GAE| over agent entries
            "credit_cnt": 0,            # agent entries with dcca on
        }

    # ------------------------------------------------------------------
    def _mech_row(self):
        """Summarise + RESET the mechanism window (called at each eval
        point, spec §3.6)."""
        m = self._mech
        r_vals = m["r_vals"]
        r_mean = (sum(r_vals) / len(r_vals)) if r_vals else 0.0
        r_std = ((sum((v - r_mean) ** 2 for v in r_vals) / len(r_vals))
                 ** 0.5) if r_vals else 0.0
        adv_i, adv_t = m["adv_indiv"], m["adv_team"]
        mean_i = (sum(adv_i) / len(adv_i)) if adv_i else 0.0
        std_i = ((sum((v - mean_i) ** 2 for v in adv_i) / len(adv_i))
                 ** 0.5) if adv_i else 0.0
        mean_t = (sum(adv_t) / len(adv_t)) if adv_t else 0.0
        std_t = ((sum((v - mean_t) ** 2 for v in adv_t) / len(adv_t))
                 ** 0.5) if adv_t else 0.0
        row = {
            "credit_nonzero_ratio":
                round(m["credit_nonzero"] / max(1, m["credit_slots"]), 6),
            "adv_indiv_over_team_std":
                round(std_i / std_t, 6) if std_t > 0 else 0.0,
            "reward_nonzero_ratio":
                round(m["r_shaped_nz"] / max(1, m["r_steps"]), 6),
            "reward_nonzero_ratio_base":
                round(m["r_team_nz"] / max(1, m["r_steps"]), 6),
            "r_shaped_mean": round(r_mean, 8),
            "r_shaped_std": round(r_std, 8),
            "params_actor": self.n_params,
            "params_critic": self.n_params_critic,
            "wall_per_iter": round(
                sum(m["wall_iters"]) / max(1, len(m["wall_iters"])), 4),
            "illegal_actions": m["illegal_actions"],
            # r2 §3.4 mechanism evidence: share of the shaped term inside
            # the reward stream and of the injected terms inside the
            # individual advantage (0.0 when the mechanism is off).
            "r_shape_share": round(
                m["shape_abs"] / (m["shape_abs"] + m["team_abs"])
                if (m["shape_abs"] + m["team_abs"]) > 0.0 else 0.0, 6),
            "credit_adv_share": round(
                m["credit_abs"] / (m["credit_abs"] + m["gae_abs"])
                if (m["credit_abs"] + m["gae_abs"]) > 0.0 else 0.0, 6),
        }
        # reset the window
        self._mech = {
            "credit_slots": 0, "credit_nonzero": 0,
            "r_vals": [], "r_shaped_nz": 0, "r_team_nz": 0, "r_steps": 0,
            "adv_indiv": [], "adv_team": [],
            "wall_iters": [], "illegal_actions": 0,
            "shape_abs": 0.0, "team_abs": 0.0,
            "credit_abs": 0.0, "gae_abs": 0.0, "credit_cnt": 0,
        }
        return row

    # ------------------------------------------------------------------
    def _anneal_tau(self, it):
        span = max(1, self.args.anneal_iters)
        self.collector.tau = max(0.5, 1.0 - 0.5 * it / span)

    # ------------------------------------------------------------------
    def collect_episode(self, dn):
        """Run one episode with the training collector; return the
        per-step sample list and the episode record."""
        env = DNEnv(dn, self.seed_counter)
        self.seed_counter += 1
        samples = []          # per decision step: {t, agents:[...],
                              # critic in (tensors), actions}
        orig_act = self.collector.act

        def wrapped_act(e, t):
            # NOTE: called by env.run BEFORE fires; we snapshot global
            # state pre-action for the critic, then act
            actions, info = orig_act(e, t)
            tgt, glob, act = critic_inputs(e, t, actions, dn)
            samples.append({
                "t": t,
                "agents": self.collector.last_step_collect,
                "tgt": tgt, "glob": glob, "act": act,
                "actions": dict(actions),
            })
            self.env_steps += 1
            return actions, info

        run_rec = env.run(type("W", (), {"act": staticmethod(wrapped_act)})())
        ci = self.args.c_invalid
        if ci is None:
            ci = C_INVALID           # reward.py module default
        rew = build_rewards(env, run_rec, dn, c_invalid=ci,
                            credit_mode=getattr(self.args, "credit_mode",
                                                "credit_kill"),
                            phi_sign=getattr(self.args, "phi_sign", -1.0),
                            use_eaps=bool(self.use_eaps),
                            phi_scale=self.phi_scale)
        # ---- mechanism instrumentation window (spec §3.6) --------------
        m = self._mech
        m["illegal_actions"] += sum(
            s.get("illegal_actions", 0) for s in run_rec["steps"])
        m["credit_slots"] += len(rew["shots_detail"])
        m["credit_nonzero"] += sum(
            1 for v in rew["credit"].values() if v != 0.0)
        rs = rew["R_shaped"].tolist()
        rt = rew["R_team"].tolist()
        m["r_vals"].extend(rs)
        m["r_steps"] += len(rs)
        m["r_shaped_nz"] += sum(1 for v in rs if v != 0.0)
        m["r_team_nz"] += sum(1 for v in rt if v != 0.0)
        # r2 §3.4: |lambda*phi_diff| = |R_shaped - R_team| (exactly 0
        # when use_eaps=0, so a closed EAPS reports share 0.0)
        m["shape_abs"] += sum(abs(a - b) for a, b in zip(rs, rt))
        m["team_abs"] += sum(abs(b) for b in rt)
        return samples, rew, run_rec

    # ------------------------------------------------------------------
    def _gae(self, rewards, values, gamma=GAMMA, lam=GAE_LAMBDA):
        T = len(rewards)
        adv = [0.0] * T
        lastgaelam = 0.0
        for t in reversed(range(T)):
            next_v = values[t + 1] if t + 1 < T else 0.0
            delta = rewards[t] + gamma * next_v - values[t]
            lastgaelam = delta + gamma * lam * lastgaelam
            adv[t] = lastgaelam
        return adv

    # ------------------------------------------------------------------
    def process_batch(self, episodes):
        """Turn collected episodes into flat PPO samples.

        A1 batched variant: all decision steps across episodes are
        pad-stacked and scored by ONE critic forward; the 3 counterfactual
        hold variants per step form a (3B, ...) batch scored by a second
        forward. Math is identical to the historical per-step loop (masked
        mean over real rows reproduces the per-sample mean); MPS keeps the
        CPU fallback.
        """
        # ---- gather decision steps + folded reward series --------------
        eps = []
        for (samples, rew, run_rec) in episodes:
            K = len(rew["R_shaped"]) - 1               # t = 0..K
            dec_steps = [s for s in samples if s["t"] <= K - 2]
            if not dec_steps:
                continue
            r_series = [float(rew["R_shaped"][s["t"]]) for s in dec_steps]
            r_series[-1] += float(rew["R_shaped"][K - 1]) \
                if K - 1 > dec_steps[-1]["t"] else 0.0
            r_series[-1] += float(rew["R_shaped"][K])
            eps.append((dec_steps, r_series, rew["credit"]))
        if not eps:
            return []

        steps = [s for ds, _, _ in eps for s in ds]
        n_agents = len(steps[0]["agents"]) if steps else 0
        B = len(steps)

        # ---- pad-stack critic inputs ----------------------------------
        Lp = max(s["tgt"].shape[0] for s in steps)
        tb = torch.zeros(B, Lp, 5)
        tm = torch.zeros(B, Lp, dtype=torch.bool)
        for b, s in enumerate(steps):
            L = s["tgt"].shape[0]
            tb[b, :L] = s["tgt"]
            tm[b, :L] = True
        gb = torch.stack([s["glob"] for s in steps])
        ab = torch.stack([s["act"] for s in steps])

        # counterfactual hold variants: for each step, n_agents rows with
        # agent i's action triple replaced by (1, 0, 0) = hold
        # (DCCA off: the joint-action critic consumes no act rows, so the
        # hold-variant batch is NOT built and no cf diff is computed)
        if self.use_dcca:
            tb3 = tb.repeat_interleave(n_agents, dim=0)
            tm3 = tm.repeat_interleave(n_agents, dim=0)
            gb3 = gb.repeat_interleave(n_agents, dim=0)
            ab3 = ab.repeat_interleave(n_agents, dim=0)
            for r in range(B):
                for i in range(n_agents):
                    ab3[r * n_agents + i, i * 3:i * 3 + 3] = \
                        torch.tensor([1.0, 0.0, 0.0])

        # ---- one + one critic forwards (with CPU fallback) -------------
        with torch.no_grad():
            try:
                dev = self.device
                if self.use_dcca:
                    v_all = self.critic(tb.to(dev), gb.to(dev), ab.to(dev),
                                        tm.to(dev))
                    v_cf = self.critic(tb3.to(dev), gb3.to(dev), ab3.to(dev),
                                       tm3.to(dev))
                else:
                    v_all = self.critic(tb.to(dev), gb.to(dev), tm.to(dev))
            except RuntimeError as e:
                if self.device.type != "mps":
                    raise
                print("[marl-train] MPS critic failed (%s) -> CPU" % e)
                self.device = torch.device("cpu")
                self.critic.to(self.device)
                self.actor.to(self.device)
                if self.use_dcca:
                    v_all = self.critic(tb, gb, ab, tm)
                    v_cf = self.critic(tb3, gb3, ab3, tm3)
                else:
                    v_all = self.critic(tb, gb, tm)
        vals_all = v_all.tolist()
        if self.use_dcca:
            cf_all = (v_all.unsqueeze(1)
                      - v_cf.view(B, n_agents)).tolist()   # base - hold_i
        else:
            cf_all = [None] * B                            # unused

        # ---- GAE + flat sample assembly (same math as before) ----------
        flat = []
        cursor = 0
        for dec_steps, r_series, credit in eps:
            vals = vals_all[cursor:cursor + len(dec_steps)]
            cfs = cf_all[cursor:cursor + len(dec_steps)]
            gae = self._gae(r_series, vals)
            for idx, s in enumerate(dec_steps):
                t = s["t"]
                cf_row = cfs[idx]
                for entry in s["agents"]:
                    i = entry["agent"]
                    if entry.get("empty"):
                        continue
                    if self.use_dcca:
                        # r2 §3.1: alpha scales the kill credit, beta the
                        # counterfactual hold diff; both default 1.0 =
                        # pre-r2 bit-identical (x*1.0 == x exactly).
                        adv_i = gae[idx] \
                            + self.credit_alpha * credit.get((t, i), 0.0) \
                            + self.cf_beta * cf_row[i]
                        self._mech["credit_abs"] += abs(
                            self.credit_alpha * credit.get((t, i), 0.0)
                            + self.cf_beta * cf_row[i])
                        self._mech["credit_cnt"] += 1
                    else:
                        # DCCA off: NO credit injection, NO cf diff -
                        # individual advantage IS the team GAE
                        adv_i = gae[idx]
                    self._mech["gae_abs"] += abs(gae[idx])
                    # mechanism window: individual vs team advantage
                    self._mech["adv_indiv"].append(float(adv_i))
                    self._mech["adv_team"].append(float(gae[idx]))
                    flat.append({
                        "x": entry["x"], "q": entry["q"], "g": entry["g"],
                        "mask": entry["mask"], "pick": entry["pick"],
                        "logp_old": entry["logp"],
                        "adv": adv_i,
                        "ret": gae[idx] + vals[idx],
                        "tgt": s["tgt"], "glob": s["glob"], "act": s["act"],
                    })
            cursor += len(dec_steps)
        return flat

    # ------------------------------------------------------------------
    def ppo_update(self, flat):
        if not flat:
            return 0.0, 0.0, 0.0
        if getattr(self.args, "no_batched", False):
            return self._ppo_update_loop(flat)
        return self._ppo_update_batched(flat)

    # ------------------------------------------------------------------
    def _ppo_update_loop(self, flat):
        """Historical per-sample PPO update (A1 fallback, --no-batched)."""
        advs = torch.tensor([f["adv"] for f in flat], dtype=torch.float32)
        advs = (advs - advs.mean()) / (advs.std() + 1e-8)
        rets = torch.tensor([f["ret"] for f in flat], dtype=torch.float32)
        n = len(flat)
        idx_all = torch.randperm(n)
        stats = [0.0, 0.0, 0.0]
        nb = 0
        for _epoch in range(PPO_EPOCHS):
            for start in range(0, n, MINIBATCH):
                idx = idx_all[start:start + MINIBATCH]
                pol_loss = 0.0
                self.opt_a.zero_grad()
                for k in idx.tolist():
                    f = flat[k]
                    logits, *_ = self.actor(f["x"].to(self.device),
                                            f["q"].to(self.device),
                                            f["g"].to(self.device))
                    masked = logits.clone()
                    masked[1:][~f["mask"]] = -float("inf")
                    # PPO ratio must compare SAME distribution: replay with
                    # the temperature used at collection time
                    logp_all = torch.log_softmax(
                        masked / f.get("tau", self.collector.tau), dim=0)
                    logp_new = logp_all[f["pick"]]
                    ratio = torch.exp(logp_new - f["logp_old"])
                    a = advs[k]
                    surr = torch.min(ratio * a,
                                     torch.clamp(ratio, 1 - PPO_CLIP,
                                                 1 + PPO_CLIP) * a)
                    fin = torch.isfinite(logp_all)
                    ent = -(torch.exp(logp_all[fin]) * logp_all[fin]).sum()
                    pol_loss = pol_loss - surr - ENT_COEF * ent
                pol_loss = pol_loss / len(idx)
                pol_loss.backward()
                torch.nn.utils.clip_grad_norm_(self.actor.parameters(),
                                               0.5)
                self.opt_a.step()
                stats[0] += float(pol_loss.item())
                nb += 1
            # ---- critic regression (MSE to returns, grad-accumulated) --
            self.opt_c.zero_grad()
            v_loss = 0.0
            for k in idx_all.tolist():
                f = flat[k]
                if self.use_dcca:
                    v = self.critic(f["tgt"].unsqueeze(0).to(self.device),
                                    f["glob"].unsqueeze(0).to(self.device),
                                    f["act"].unsqueeze(0).to(self.device))
                else:
                    v = self.critic(f["tgt"].unsqueeze(0).to(self.device),
                                    f["glob"].unsqueeze(0).to(self.device))
                loss = (v[0] - rets[k]) ** 2 / n
                loss.backward()
                v_loss += float(loss.item()) * n
            torch.nn.utils.clip_grad_norm_(self.critic.parameters(),
                                           0.5)
            self.opt_c.step()
            stats[1] += v_loss / n
        return (stats[0] / max(1, nb), stats[1] / max(1, PPO_EPOCHS),
                stats[2])

    # ------------------------------------------------------------------
    def _ppo_update_batched(self, flat):
        """A1 batched PPO update: actor samples pad-stacked once, per-
        minibatch forward_batch gives all logits at once; logp via gather,
        entropy summed over finite slots (pad contributes 0), tau replayed
        per sample. Critic regression is one masked-mean forward over all
        n samples per epoch. Same math as _ppo_update_loop."""
        advs = torch.tensor([f["adv"] for f in flat], dtype=torch.float32)
        advs = (advs - advs.mean()) / (advs.std() + 1e-8)
        rets = torch.tensor([f["ret"] for f in flat], dtype=torch.float32)
        taus = torch.tensor([f.get("tau", self.collector.tau)
                             for f in flat], dtype=torch.float32)
        picks = torch.tensor([f["pick"] for f in flat], dtype=torch.long)
        lpo = torch.tensor([f["logp_old"] for f in flat],
                           dtype=torch.float32)
        n = len(flat)
        idx_all = torch.randperm(n)
        stats = [0.0, 0.0, 0.0]
        nb = 0

        # ---- pad-stack actor inputs once ------------------------------
        Lmax = max(f["x"].shape[0] for f in flat)
        xb = torch.zeros(n, Lmax, self.x_dim)
        pb = torch.zeros(n, Lmax, dtype=torch.bool)   # padding (real rows)
        mb = torch.zeros(n, Lmax, dtype=torch.bool)   # feasibility mask
        for b, f in enumerate(flat):
            L = f["x"].shape[0]
            xb[b, :L] = f["x"]
            pb[b, :L] = True
            mb[b, :L] = f["mask"]
        qb = torch.stack([f["q"] for f in flat])
        gb = torch.stack([f["g"] for f in flat])
        # ---- pad-stack critic inputs once ------------------------------
        Lp = max(f["tgt"].shape[0] for f in flat)
        tb = torch.zeros(n, Lp, 5)
        tm = torch.zeros(n, Lp, dtype=torch.bool)
        for b, f in enumerate(flat):
            L = f["tgt"].shape[0]
            tb[b, :L] = f["tgt"]
            tm[b, :L] = True
        gcb = torch.stack([f["glob"] for f in flat])
        ab = torch.stack([f["act"] for f in flat])

        dev = self.device
        for _epoch in range(PPO_EPOCHS):
            for start in range(0, n, MINIBATCH):
                idx = idx_all[start:start + MINIBATCH]
                self.opt_a.zero_grad()
                try:
                    logits = self.actor.forward_batch(
                        xb[idx].to(dev), qb[idx].to(dev),
                        gb[idx].to(dev), pb[idx].to(dev))
                except RuntimeError as e:
                    if dev.type != "mps":
                        raise
                    print("[marl-train] MPS actor batch failed (%s) -> CPU"
                          % e)
                    dev = self.device = torch.device("cpu")
                    self.actor.to(dev)
                    logits = self.actor.forward_batch(
                        xb[idx], qb[idx], gb[idx], pb[idx])
                # feasibility mask over target slots (pad slots are
                # already -inf; hold slot 0 always feasible)
                feas = torch.cat([torch.ones(len(idx), 1, dtype=torch.bool,
                                             device=logits.device),
                                  mb[idx].to(logits.device)], dim=1)
                masked = logits.masked_fill(~feas, -float("inf"))
                tau = taus[idx].to(logits.device).unsqueeze(1)
                logp_all = torch.log_softmax(masked / tau, dim=1)
                logp_new = logp_all.gather(
                    1, picks[idx].to(logits.device).unsqueeze(1)
                ).squeeze(1)
                ratio = torch.exp(logp_new - lpo[idx].to(logits.device))
                a = advs[idx].to(logits.device)
                surr = torch.min(ratio * a,
                                 torch.clamp(ratio, 1 - PPO_CLIP,
                                             1 + PPO_CLIP) * a)
                # entropy over finite slots only: pad/infeasible slots
                # carry -inf logp; zero them BEFORE the product so the
                # backward pass never forms 0 * (-inf) = NaN gradients
                # (torch.where alone does NOT guard the unselected branch)
                fin = torch.isfinite(logp_all)
                lp_safe = torch.where(fin, logp_all,
                                      torch.zeros_like(logp_all))
                pent = torch.exp(lp_safe) * lp_safe
                ent = -pent.sum(dim=1)
                pol_loss = -(surr + ENT_COEF * ent).mean()
                pol_loss.backward()
                torch.nn.utils.clip_grad_norm_(self.actor.parameters(), 0.5)
                self.opt_a.step()
                stats[0] += float(pol_loss.item())
                nb += 1
            # ---- critic regression: one batched forward per epoch ------
            self.opt_c.zero_grad()
            if self.use_dcca:
                v = self.critic(tb.to(dev), gcb.to(dev), ab.to(dev),
                                tm.to(dev))
            else:
                v = self.critic(tb.to(dev), gcb.to(dev), tm.to(dev))
            v_loss = ((v - rets.to(dev)) ** 2).mean()
            v_loss.backward()
            torch.nn.utils.clip_grad_norm_(self.critic.parameters(), 0.5)
            self.opt_c.step()
            stats[1] += float(v_loss.item())
        return (stats[0] / max(1, nb), stats[1] / max(1, PPO_EPOCHS),
                stats[2])

    # ------------------------------------------------------------------
    @torch.no_grad()
    def evaluate_val(self):
        """val split x seeds 42-51, greedy argmax, leak rate only."""
        rates = []
        for dn in self.val_dns:
            for seed in range(42, 52):
                env = DNEnv(dn, seed)
                self.eval_pol.reset_episode()
                rec = env.run(self.eval_pol)
                rates.append(rec["leak_rate"])
        mean = sum(rates) / len(rates)
        std = (sum((r - mean) ** 2 for r in rates) / len(rates)) ** 0.5
        return mean, std

    # ------------------------------------------------------------------
    def save_ckpt(self, path, it=None):
        torch.save({
            "state_dict": self.actor.state_dict(),
            "critic_state_dict": self.critic.state_dict(),
            "iter": it,
            "best_val": (None if self.best_val == float("inf")
                         else self.best_val),
            "feature_spec": {"x": self.x_dim, "q": 5, "g": 3,
                             "drop_m1": self.drop_m1},
            "params_count": self.n_params,
            # ---- v5 ablation metadata (spec §3.7; evaluator restores the
            # structure from these fields ONLY - never from the path) ---
            "ablation": {"use_dcca": self.use_dcca,
                         "use_eaps": self.use_eaps,
                         "use_casp": self.use_casp},
            # r2 §3.2: recalibration metadata (anti-cross-arm, evaluator
            # verifies against the locked e52 pick on every load)
            "reshaping": {"phi_scale": self.phi_scale,
                          "credit_alpha": self.credit_alpha,
                          "cf_beta": self.cf_beta},
            "actor_type": self.actor_type,
            "critic_type": self.critic_type,
            "train_seed": int(getattr(self.args, "seed", 0)),
            "budget": {
                "iters": int(getattr(self.args, "iters", 0)),
                "episodes_per_iter":
                    int(getattr(self.args, "episodes_per_iter", 0)),
                "patience": int(getattr(self.args, "patience", 0)),
                "eval_every": int(getattr(self.args, "eval_every", 25)),
            },
            "versions": {"reward": "v5", "eval_protocol": "v5",
                         "torch": str(torch.__version__),
                         "recal": "r2"},
        }, path)

    def _load_weights(self, ckpt):
        """Load actor + critic weights only (used by --resume and
        --resume-from)."""
        self.actor.load_state_dict(ckpt["state_dict"])
        if "critic_state_dict" in ckpt:
            self.critic.load_state_dict(ckpt["critic_state_dict"])
        self.eval_pol.net = self.actor
        self.collector.net = self.actor

    # ------------------------------------------------------------------
    def save_last(self, path, it, elapsed, eval_points=0, bad_points=0):
        """v5 §6.1.3 periodic resumable checkpoint (every eval point +
        <= 10 min cadence): weights, optimizer states, counters and
        elapsed wall time so the watchdog restart keeps full budget
        accounting."""
        torch.save({
            "state_dict": self.actor.state_dict(),
            "critic_state_dict": self.critic.state_dict(),
            "opt_a": self.opt_a.state_dict(),
            "opt_c": self.opt_c.state_dict(),
            "iter": it,
            "best_val": (None if self.best_val == float("inf")
                         else self.best_val),
            "eval_points": eval_points,
            "bad_points": bad_points,
            "seed_counter": self.seed_counter,
            "env_steps": self.env_steps,
            "elapsed_sec": elapsed,
            "feature_spec": {"x": self.x_dim, "q": 5, "g": 3,
                             "drop_m1": self.drop_m1},
            "params_count": self.n_params,
            # ---- v5 ablation metadata (spec §3.7) ----------------------
            "ablation": {"use_dcca": self.use_dcca,
                         "use_eaps": self.use_eaps,
                         "use_casp": self.use_casp},
            "reshaping": {"phi_scale": self.phi_scale,
                          "credit_alpha": self.credit_alpha,
                          "cf_beta": self.cf_beta},
            "actor_type": self.actor_type,
            "critic_type": self.critic_type,
            "train_seed": int(getattr(self.args, "seed", 0)),
            "budget": {
                "iters": int(getattr(self.args, "iters", 0)),
                "episodes_per_iter":
                    int(getattr(self.args, "episodes_per_iter", 0)),
                "patience": int(getattr(self.args, "patience", 0)),
                "eval_every": int(getattr(self.args, "eval_every", 25)),
            },
            "versions": {"reward": "v5", "eval_protocol": "v5",
                         "torch": str(torch.__version__),
                         "recal": "r2"},
        }, path)

    # ------------------------------------------------------------------
    def run(self):
        args = self.args
        t_start = time.time()
        ckpt_path = os.path.join(args.output, "best.pt")
        last_path = os.path.join(args.output, "last.pt")
        it = 0
        eval_points = 0
        bad_points = 0
        stopped = None
        resume_elapsed = 0.0
        if getattr(args, "resume", False):
            src = last_path if os.path.exists(last_path) else ckpt_path
            if not os.path.exists(src):
                raise FileNotFoundError(
                    "--resume needs %s or %s (nothing to resume from)"
                    % (last_path, ckpt_path))
            ck = torch.load(src, map_location="cpu")
            self._load_weights(ck)
            it = int(ck.get("iter") or 0)
            if ck.get("best_val") is not None:
                self.best_val = float(ck["best_val"])
            if "opt_a" in ck:      # full resumable ckpt (last.pt format)
                try:
                    self.opt_a.load_state_dict(ck["opt_a"])
                    self.opt_c.load_state_dict(ck["opt_c"])
                except Exception as e:
                    print("[marl-train] optimizer state not restored (%s); "
                          "continuing with fresh optimizers" % e, flush=True)
                self.seed_counter = int(ck.get("seed_counter",
                                                self.seed_counter))
                self.env_steps = int(ck.get("env_steps", self.env_steps))
                resume_elapsed = float(ck.get("elapsed_sec", 0.0))
                eval_points = int(ck.get("eval_points", 0))
                bad_points = int(ck.get("bad_points", 0))
            print("[marl-train] resume from %s: iter=%d best_val=%.4f "
                  "elapsed=%.0fs" % (src, it, self.best_val, resume_elapsed),
                  flush=True)
        elif getattr(args, "resume_from", None):
            ck = torch.load(args.resume_from, map_location="cpu")
            self._load_weights(ck)
            print("[marl-train] weights loaded from %s (fresh log, iter 0)"
                  % args.resume_from, flush=True)
        elif getattr(args, "init_from", None):
            # A4 BC warm start: blend actor weights toward the BC ckpt
            ck = torch.load(args.init_from, map_location="cpu")
            bc_sd = ck["state_dict"]
            a = float(getattr(args, "init_blend", 1.0))
            sd = self.actor.state_dict()
            for k in sd:
                sd[k] = (1.0 - a) * sd[k] + a * bc_sd[k]
            self.actor.load_state_dict(sd)
            self.eval_pol.net = self.actor
            self.collector.net = self.actor
            print("[marl-train] actor blended with %s (alpha=%g)"
                  % (args.init_from, a), flush=True)
        epi = args.episodes_per_iter
        wall_limit_sec = float(getattr(args, "wall_limit", 24.0)) * 3600.0
        last_hb = time.time()
        last_ckpt = time.time()
        while it < args.iters:
            elapsed = resume_elapsed + (time.time() - t_start)
            if elapsed > wall_limit_sec:
                stopped = "wall_limit"
                break
            if time.time() - last_hb > 60.0:
                print("[hb] iter=%d elapsed=%.0fs budget=%.1fh"
                      % (it, elapsed, wall_limit_sec / 3600.0), flush=True)
                last_hb = time.time()
            # ---- collect one batch ----------------------------------
            t_it = time.time()
            episodes = []
            train_leaks = []
            for _ in range(epi):
                dn = self.train_dns[
                    (it * epi + len(episodes))
                    % len(self.train_dns)]
                samples, rew, run_rec = self.collect_episode(dn)
                episodes.append((samples, rew, run_rec))
                train_leaks.append(run_rec["leak_rate"])
            self._anneal_tau(it)
            flat = self.process_batch(episodes)
            pl, vl, el = self.ppo_update(flat)
            self._mech["wall_iters"].append(time.time() - t_it)
            it += 1
            if time.time() - last_ckpt > 600.0:   # §6.1.3: <= 10 min
                self.save_last(last_path, it,
                               resume_elapsed + (time.time() - t_start),
                               eval_points, bad_points)
                last_ckpt = time.time()
            # ---- periodic evaluation -------------------------------
            if it % args.eval_every == 0 or it == args.iters:
                val_mean, val_std = self.evaluate_val()
                eval_points += 1
                row = {
                    "iter": it,
                    "env_steps": self.env_steps,
                    "train_leak": sum(train_leaks) / len(train_leaks),
                    "val_leak_mean": val_mean,
                    "val_leak_std": val_std,
                    "wall_sec": round(resume_elapsed
                                      + (time.time() - t_start), 1),
                    "tau": round(self.collector.tau, 3),
                    "policy_loss": round(pl, 6),
                }
                # mechanism window summary (spec §3.6; resets the window)
                row.update(self._mech_row())
                self._log_f.write(json.dumps(row) + "\n")
                self._log_f.flush()
                print("[iter %6d] train %.4f | val %.4f+-%.4f | "
                      "tau %.2f | %.0fs"
                      % (it, row["train_leak"], val_mean, val_std,
                         self.collector.tau, row["wall_sec"]), flush=True)
                if not all(math.isfinite(v) for v in
                           (val_mean, row["train_leak"])):
                    stopped = stopped or "nan_guard"
                    break
                if val_mean < self.best_val - 1e-6:
                    self.best_val = val_mean
                    self.save_ckpt(ckpt_path, it=it)
                    bad_points = 0
                else:
                    bad_points += 1
                self.save_last(last_path, it,
                               resume_elapsed + (time.time() - t_start),
                               eval_points, bad_points)
                last_ckpt = time.time()
                if bad_points >= args.patience:
                    stopped = "early_stop"
                    break
        # ---- summary -------------------------------------------------
        wall = resume_elapsed + (time.time() - t_start)
        try:      # keep last.pt fresh for post-stop restarts
            self.save_last(last_path, it, wall, eval_points, bad_points)
        except Exception:
            pass
        summary = {
            "total_wall_sec": round(wall, 1),
            "env_steps": self.env_steps,
            "params_count": self.n_params,
            "ablation": {"use_dcca": self.use_dcca,
                         "use_eaps": self.use_eaps,
                         "use_casp": self.use_casp},
            "reshaping": {"phi_scale": self.phi_scale,
                          "credit_alpha": self.credit_alpha,
                          "cf_beta": self.cf_beta},
            "actor_type": self.actor_type,
            "critic_type": self.critic_type,
            "params_critic": self.n_params_critic,
            "best_val": (None if self.best_val == float("inf")
                         else self.best_val),
            "final_metrics": {"iters_done": it, "eval_points": eval_points,
                              "stop_reason": stopped or "iters_done",
                              "device": str(self.device)},
        }
        with open(os.path.join(args.output, "train_summary.json"), "w") as f:
            json.dump(summary, f, indent=2)
        self._log_f.close()
        print("training done: %s | best val %.4f | wall %.0fs"
              % (summary["final_metrics"]["stop_reason"],
                 self.best_val if self.best_val != float("inf") else -1,
                 wall))


def main(argv=None):
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description="CTDE training for marl")
    ap.add_argument("--iters", type=int, default=3000,
                    help="A2 relaxed budget: max 3000 iters")
    ap.add_argument("--wall-limit", type=float, default=24.0,
                    help="train wall-clock cap in HOURS (default 24 keeps "
                         "the v3 tier; v4 full tier passes 6 per the "
                         "budget-layering spec D6/4.3)")
    ap.add_argument("--eval-every", type=int, default=25)
    ap.add_argument("--patience", type=int, default=60,
                    help="early-stop patience in EVAL POINTS (A2)")
    ap.add_argument("--episodes-per-iter", type=int, default=128,
                    help="A2: 4x episodes per iter vs e14 (was a 32 const)")
    ap.add_argument("--device", default="auto",
                    choices=["auto", "mps", "cpu"])
    ap.add_argument("--data-dir", default=DATA_DIR,
                    help="instance dir (default v3 dn_3x50; v4 runs pass "
                         "data/dn-data-v4 - split protocol is fixed)")
    ap.add_argument("--seed", type=int, default=0,
                    help="actor sampling generator seed")
    ap.add_argument("--anneal-iters", type=int, default=2000,
                    help="iters to anneal tau 1.0 -> 0.5")
    ap.add_argument("--no-batched", action="store_true",
                    help="A1: fall back to the historical per-sample PPO "
                         "update (gate/diagnosis only)")
    ap.add_argument("--c-invalid", type=float, default=None,
                    help="invalid-engagement penalty (default: reward.py "
                         "C_INVALID=0.01); e16 scans 0.005/0.01/0.03/0.05")
    ap.add_argument("--credit-mode", default="credit_kill",
                    choices=["credit_kill", "credit_kill_cf"],
                    help="A3: both names are accepted and semantically "
                         "identical (proportional p_shot split); dummy "
                         "compat for the plan's CLI surface")
    ap.add_argument("--phi-sign", type=float, default=-1.0,
                    choices=[-1.0, 1.0],
                    help="A3-alt-1 (A0-triggered pos control): -1 keeps "
                         "the historical Phi = -sum w*pbar; +1 flips the "
                         "potential sign so launch steps get a positive "
                         "kick")
    ap.add_argument("--resume", action="store_true",
                    help="v5 §6.1.3: resume from <output>/last.pt if "
                         "present (weights + optimizers + counters + "
                         "elapsed wall, budget-aware), else fall back to "
                         "best.pt (weights + iter + best_val); log "
                         "APPENDED, tau re-annealed by iter")
    ap.add_argument("--resume-from", default=None,
                    help="A2: load weights only from CKPT into a FRESH run "
                         "(fresh log, iter 0) - e.g. e16 reusing e15 as "
                         "baseline; never mixes logs")
    ap.add_argument("--init-from", default=None,
                    help="A4: BC warm-start ckpt for the ACTOR; combined "
                         "with --init-blend")
    ap.add_argument("--init-blend", type=float, default=1.0,
                    help="A4: actor init blend theta = (1-a)*theta_rand + "
                         "a*theta_bc (0 = random control, 0.1 = spec "
                         "BLEND, 1 = full BC)")
    ap.add_argument("--output", default=os.path.join(
        here, "..", "output", "e14_marl_train"))
    ap.add_argument("--use-dcca", type=int, choices=[0, 1], default=1,
                    help="v5 ablation DCCA switch: 1 (default) = joint-"
                         "action critic + event-retrospect credit + cf "
                         "diff injected into individual advantages; 0 = "
                         "StateCritic V(s), no credit, no cf diff")
    ap.add_argument("--use-eaps", type=int, choices=[0, 1], default=1,
                    help="v5 ablation EAPS switch: 1 (default) = potential "
                         "shaping R_shaped = R_team + gamma*Phi' - Phi; "
                         "0 = R_shaped = R_team (Phi removed entirely)")
    ap.add_argument("--use-casp", type=int, choices=[0, 1], default=1,
                    help="v5 ablation CASP switch: 1 (default) = MarlNet "
                         "set-attention actor over 10-dim x; 0 = PoolMLPNet "
                         "actor over 8-dim x (M1 columns dropped)")
    ap.add_argument("--phi-scale", type=float, default=1.0,
                    help="r2 recalibration lambda on the EAPS shaping term "
                         "(R_shaped = R_team + lambda*phi_sign*(gamma*Phi'-"
                         "Phi)); only meaningful with --use-eaps 1; 1.0 "
                         "(default) = pre-r2 bit-identical")
    ap.add_argument("--credit-alpha", type=float, default=1.0,
                    help="r2 recalibration alpha on the kill-credit "
                         "injection into individual advantages; only "
                         "meaningful with --use-dcca 1; 1.0 (default) = "
                         "pre-r2 bit-identical")
    ap.add_argument("--cf-beta", type=float, default=1.0,
                    help="r2 recalibration beta on the counterfactual "
                         "hold-diff term; only meaningful with --use-dcca "
                         "1; 1.0 (default) = pre-r2 bit-identical")
    args = ap.parse_args(argv)
    args.output = os.path.abspath(args.output)
    os.makedirs(args.output, exist_ok=True)
    # ablation bit vector - FIRST line of the training start log (spec
    # §3.2); must appear before any other training output
    print("[ablation] use_dcca=%d use_eaps=%d use_casp=%d -> (%d,%d,%d)"
          % (args.use_dcca, args.use_eaps, args.use_casp,
             args.use_dcca, args.use_eaps, args.use_casp), flush=True)
    # r2 §3.2: recalibration scalars - SECOND line of the start log
    print("[reshaping] phi_scale=%g credit_alpha=%g cf_beta=%g"
          % (args.phi_scale, args.credit_alpha, args.cf_beta), flush=True)
    tr = Trainer(args)
    print("device=%s actor_params=%d critic_params=%d critic_type=%s"
          % (tr.device, tr.n_params, tr.n_params_critic, tr.critic_type))
    tr.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
