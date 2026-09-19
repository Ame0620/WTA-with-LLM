"""E24-B4: MAPPO baseline training for the DN-WTA v3 task.

Deliberately standard MAPPO, contrasted against the self-developed
marl pipeline (marl/train.py) component by component:

    actor    : PoolMLPNet (MLP + target mean/max pooling, x in R^8 -
               the M1 memory columns are DROPPED, build_inputs
               drop_m1=True; no set attention);
    critic   : state-value V(s) WITHOUT joint-action conditioning
               (StateCritic; no COMA-style counterfactual hold
               baselines);
    advantage: plain TEAM GAE (gamma=0.99, lambda=0.95) shared by all
               agents - NO kill-credit attribution (credit_kill),
               NO potential shaping (Phi term removed);
    reward   : R_team = kill/leak events + c_invalid penalty only
               (reward.py build_rewards R_team output);
    PPO      : clip 0.2, entropy 0.01, Adam lr 3e-4, 2 epochs,
               minibatch 256 - same locked values as marl/train.py;
    other    : sampling temperature anneal 1.0 -> 0.5 over
               --anneal-iters, A1 batched forwards (forward_batch),
               M4 feasibility masking, shared parameters, NO BC warm
               start; early stop on val leak (s27-s30 x seeds 42-51,
               greedy, no CPLEX), patience in eval points.

Products (flat dir --output): best.pt / train_log.jsonl /
train_summary.json (same layout as marl/train.py).
"""

import argparse
import json
import math
import os
import sys
import time

import torch

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(HERE)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from dwta.dn_instance import DNInstance                     # noqa: E402
from dwta.dn_env import DNEnv                               # noqa: E402
from marl.baseline_policy import PoolMLPPolicy              # noqa: E402
from marl.baseline_net import PoolMLPNet, StateCritic, \
    assert_params as assert_agent_params                    # noqa: E402
from marl.train import critic_inputs                        # noqa: E402
from marl.reward import build_rewards, C_INVALID            # noqa: E402

DATA_DIR = os.path.join(PROJECT_ROOT, "data", "dn-data-v3")

TRAIN_INSTS = ["dn_3x50_K10_s%02d.txt" % s for s in range(3, 27)]
VAL_INSTS = ["dn_3x50_K10_s%02d.txt" % s for s in range(27, 31)]

# PPO hyper-parameters (locked; identical to marl/train.py)
PPO_CLIP = 0.2
ENT_COEF = 0.01
GAE_LAMBDA = 0.95
GAMMA = 0.99
LR = 3e-4
PPO_EPOCHS = 2
MINIBATCH = 256
WALL_LIMIT_SEC = 2.5 * 3600.0     # v4 3h-tier baseline: <=2.5h train wall


class Trainer(object):
    def __init__(self, args):
        self.args = args
        self.device = torch.device(
            "cpu") if args.device == "cpu" else self._pick(args.device)
        self.actor = PoolMLPNet().to(self.device)
        self.n_params = assert_agent_params(self.actor)
        self.critic = StateCritic().to(self.device)
        self.opt_a = torch.optim.Adam(self.actor.parameters(), lr=LR)
        self.opt_c = torch.optim.Adam(self.critic.parameters(), lr=LR)
        self.eval_pol = PoolMLPPolicy("mappo", model_path=None,
                                      device=args.device, greedy=True,
                                      seed=0)
        self.eval_pol.net = self.actor
        self.collector = PoolMLPPolicy("mappo", model_path=None,
                                       device=args.device, greedy=False,
                                       seed=args.seed, training=True)
        self.collector.net = self.actor
        # v4 migration: split discovered from --data-dir (protocol fixed)
        from marl.data_split import discover_split, load_instances
        data_dir = getattr(args, "data_dir", None) or DATA_DIR
        train_files, val_files = discover_split(data_dir)
        self.train_dns = load_instances(data_dir, train_files)
        self.val_dns = load_instances(data_dir, val_files)
        self.n_agents = self.train_dns[0].m
        self.seed_counter = 100001
        self.env_steps = 0
        self.best_val = float("inf")
        self.log_path = os.path.join(args.output, "train_log.jsonl")
        self._log_f = open(self.log_path, "w")

    @staticmethod
    def _pick(device):
        if device != "auto":
            return torch.device(device)
        if getattr(torch.backends, "mps", None) is not None \
                and torch.backends.mps.is_available():
            return torch.device("mps")
        return torch.device("cpu")

    # ------------------------------------------------------------------
    def _anneal_tau(self, it):
        span = max(1, self.args.anneal_iters)
        self.collector.tau = max(0.5, 1.0 - 0.5 * it / span)

    # ------------------------------------------------------------------
    def collect_episode(self, dn):
        """One episode with the training collector; snapshot the
        state-value critic inputs (tgt/glob only - no act block)."""
        env = DNEnv(dn, self.seed_counter)
        self.seed_counter += 1
        samples = []
        orig_act = self.collector.act

        def wrapped_act(e, t):
            actions, info = orig_act(e, t)
            tgt, glob, _act = critic_inputs(e, t, actions, dn)
            samples.append({
                "t": t,
                "agents": self.collector.last_step_collect,
                "tgt": tgt, "glob": glob,
                "actions": dict(actions),
            })
            self.env_steps += 1
            return actions, info

        run_rec = env.run(type("W", (), {"act": staticmethod(wrapped_act)})())
        ci = self.args.c_invalid
        if ci is None:
            ci = C_INVALID
        rew = build_rewards(env, run_rec, dn, c_invalid=ci)
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
        """Episodes -> flat PPO samples. Team GAE only: every agent at a
        step shares adv = GAE_team(t) (no credit, no counterfactual)."""
        eps = []
        for (samples, rew, run_rec) in episodes:
            K = len(rew["R_team"]) - 1               # t = 0..K
            dec_steps = [s for s in samples if s["t"] <= K - 2]
            if not dec_steps:
                continue
            r_series = [float(rew["R_team"][s["t"]]) for s in dec_steps]
            r_series[-1] += float(rew["R_team"][K - 1]) \
                if K - 1 > dec_steps[-1]["t"] else 0.0
            r_series[-1] += float(rew["R_team"][K])
            eps.append((dec_steps, r_series))
        if not eps:
            return []

        steps = [s for ds, _ in eps for s in ds]
        B = len(steps)

        # ---- pad-stack critic inputs (state-value: tgt + glob) ------
        Lp = max(s["tgt"].shape[0] for s in steps)
        tb = torch.zeros(B, Lp, 5)
        tm = torch.zeros(B, Lp, dtype=torch.bool)
        for b, s in enumerate(steps):
            L = s["tgt"].shape[0]
            tb[b, :L] = s["tgt"]
            tm[b, :L] = True
        gb = torch.stack([s["glob"] for s in steps])

        with torch.no_grad():
            try:
                v_all = self.critic(tb.to(self.device), gb.to(self.device),
                                    tm.to(self.device))
            except RuntimeError as e:
                if self.device.type != "mps":
                    raise
                print("[mappo-train] MPS critic failed (%s) -> CPU" % e)
                self.device = torch.device("cpu")
                self.critic.to(self.device)
                self.actor.to(self.device)
                v_all = self.critic(tb, gb, tm)
        vals_all = v_all.tolist()

        flat = []
        cursor = 0
        for dec_steps, r_series in eps:
            vals = vals_all[cursor:cursor + len(dec_steps)]
            gae = self._gae(r_series, vals)
            for idx, s in enumerate(dec_steps):
                for entry in s["agents"]:
                    if entry.get("empty"):
                        continue
                    flat.append({
                        "x": entry["x"], "q": entry["q"], "g": entry["g"],
                        "mask": entry["mask"], "pick": entry["pick"],
                        "logp_old": entry["logp"],
                        "adv": gae[idx],                    # team GAE
                        "ret": gae[idx] + vals[idx],
                        "tgt": s["tgt"], "glob": s["glob"],
                    })
            cursor += len(dec_steps)
        return flat

    # ------------------------------------------------------------------
    def ppo_update(self, flat):
        if not flat:
            return 0.0, 0.0
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
        stats = [0.0, 0.0]
        nb = 0

        # ---- pad-stack actor inputs once (x is 8-dim) ----------------
        Lmax = max(f["x"].shape[0] for f in flat)
        xb = torch.zeros(n, Lmax, 8)
        pb = torch.zeros(n, Lmax, dtype=torch.bool)
        mb = torch.zeros(n, Lmax, dtype=torch.bool)
        for b, f in enumerate(flat):
            L = f["x"].shape[0]
            xb[b, :L] = f["x"]
            pb[b, :L] = True
            mb[b, :L] = f["mask"]
        qb = torch.stack([f["q"] for f in flat])
        gb = torch.stack([f["g"] for f in flat])
        # ---- pad-stack critic inputs once -----------------------------
        Lp = max(f["tgt"].shape[0] for f in flat)
        tb = torch.zeros(n, Lp, 5)
        tm = torch.zeros(n, Lp, dtype=torch.bool)
        for b, f in enumerate(flat):
            L = f["tgt"].shape[0]
            tb[b, :L] = f["tgt"]
            tm[b, :L] = True
        gcb = torch.stack([f["glob"] for f in flat])

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
                    print("[mappo-train] MPS actor batch failed (%s) -> CPU"
                          % e)
                    dev = self.device = torch.device("cpu")
                    self.actor.to(dev)
                    logits = self.actor.forward_batch(
                        xb[idx], qb[idx], gb[idx], pb[idx])
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
            # ---- critic regression: one batched forward per epoch ----
            self.opt_c.zero_grad()
            v = self.critic(tb.to(dev), gcb.to(dev), tm.to(dev))
            v_loss = ((v - rets.to(dev)) ** 2).mean()
            v_loss.backward()
            torch.nn.utils.clip_grad_norm_(self.critic.parameters(), 0.5)
            self.opt_c.step()
            stats[1] += float(v_loss.item())
        return stats[0] / max(1, nb), stats[1] / max(1, PPO_EPOCHS)

    # ------------------------------------------------------------------
    @torch.no_grad()
    def evaluate_val(self):
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
            "kind": "mappo",
            "iter": it,
            "best_val": (None if self.best_val == float("inf")
                         else self.best_val),
            "feature_spec": {"x": 8, "q": 5, "g": 3, "drop_m1": True},
            "params_count": self.n_params,
        }, path)

    # ------------------------------------------------------------------
    def save_last(self, path, it, elapsed, eval_points=0, bad_points=0):
        """v5 §6.1.3 periodic resumable checkpoint (every eval point +
        <= 10 min cadence): weights, optimizer states, counters and
        elapsed wall time for watchdog restarts."""
        torch.save({
            "state_dict": self.actor.state_dict(),
            "critic_state_dict": self.critic.state_dict(),
            "kind": "mappo",
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
            "feature_spec": {"x": 8, "q": 5, "g": 3, "drop_m1": True},
            "params_count": self.n_params,
        }, path)

    def _load_weights(self, ckpt):
        self.actor.load_state_dict(ckpt["state_dict"])
        if "critic_state_dict" in ckpt:
            self.critic.load_state_dict(ckpt["critic_state_dict"])
        self.eval_pol.net = self.actor
        self.collector.net = self.actor

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
                    print("[mappo-train] optimizer state not restored (%s); "
                          "continuing with fresh optimizers" % e, flush=True)
                self.seed_counter = int(ck.get("seed_counter",
                                                self.seed_counter))
                self.env_steps = int(ck.get("env_steps", self.env_steps))
                resume_elapsed = float(ck.get("elapsed_sec", 0.0))
                eval_points = int(ck.get("eval_points", 0))
                bad_points = int(ck.get("bad_points", 0))
            print("[mappo-train] resume from %s: iter=%d best_val=%.4f "
                  "elapsed=%.0fs" % (src, it, self.best_val, resume_elapsed),
                  flush=True)
        epi = args.episodes_per_iter
        wall_limit_sec = float(getattr(args, "wall_limit", 2.5)) * 3600.0
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
            pl, vl = self.ppo_update(flat)
            it += 1
            if time.time() - last_ckpt > 600.0:   # §6.1.3: <= 10 min
                self.save_last(last_path, it,
                               resume_elapsed + (time.time() - t_start),
                               eval_points, bad_points)
                last_ckpt = time.time()
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
                    "value_loss": round(vl, 6),
                }
                self._log_f.write(json.dumps(row) + "\n")
                self._log_f.flush()
                print("[mappo iter %6d] train %.4f | val %.4f+-%.4f | "
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
        wall = resume_elapsed + (time.time() - t_start)
        try:      # keep last.pt fresh for post-stop restarts
            self.save_last(last_path, it, wall, eval_points, bad_points)
        except Exception:
            pass
        summary = {
            "total_wall_sec": round(wall, 1),
            "env_steps": self.env_steps,
            "params_count": self.n_params,
            "best_val": (None if self.best_val == float("inf")
                         else self.best_val),
            "final_metrics": {"iters_done": it, "eval_points": eval_points,
                              "stop_reason": stopped or "iters_done",
                              "device": str(self.device)},
        }
        with open(os.path.join(args.output, "train_summary.json"), "w") as f:
            json.dump(summary, f, indent=2)
        self._log_f.close()
        print("mappo training done: %s | best val %.4f | wall %.0fs"
              % (summary["final_metrics"]["stop_reason"],
                 self.best_val if self.best_val != float("inf") else -1,
                 wall))


def main(argv=None):
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(description="E24 MAPPO baseline training")
    ap.add_argument("--iters", type=int, default=1200,
                    help="v5 3h-tier baseline cap (1200 x 12 = 14.4k ep)")
    ap.add_argument("--eval-every", type=int, default=25)
    ap.add_argument("--patience", type=int, default=12,
                    help="early-stop patience in EVAL POINTS (3h tier)")
    ap.add_argument("--episodes-per-iter", type=int, default=12,
                    help="v5 3h-tier sampling volume (m = 10 doubles the "
                         "per-step cost vs v4's 24; 12 keeps the tier "
                         "budget; same tier as qmix/maddpg)")
    ap.add_argument("--wall-limit", type=float, default=2.5,
                    help="v5 §6.1.3: train wall-clock cap in HOURS "
                         "(default 2.5 = 3h tier minus 0.5h eval reserve)")
    ap.add_argument("--resume", action="store_true",
                    help="v5 §6.1.3: resume from <output>/last.pt if "
                         "present (weights + optimizers + counters + "
                         "elapsed wall, budget-aware), else fall back to "
                         "best.pt (weights + iter + best_val)")
    ap.add_argument("--device", default="auto",
                    choices=["auto", "mps", "cpu"])
    ap.add_argument("--data-dir", default=DATA_DIR,
                    help="instance dir (default v3 dn_3x50; v4 runs pass "
                         "data/dn-data-v4 - split protocol is fixed)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--anneal-iters", type=int, default=2000)
    ap.add_argument("--c-invalid", type=float, default=None,
                    help="invalid-engagement penalty (default reward.py "
                         "C_INVALID=0.01; R_team keeps the penalty, no "
                         "shaping)")
    ap.add_argument("--output", default=os.path.join(
        here, "..", "output", "e24_mappo"))
    args = ap.parse_args(argv)
    args.output = os.path.abspath(args.output)
    os.makedirs(args.output, exist_ok=True)
    tr = Trainer(args)
    print("device=%s actor_params=%d" % (tr.device, tr.n_params))
    tr.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
