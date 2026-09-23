"""v4 MADDPG baseline training (off-policy CTDE, requirement 3.1).

Standard discrete-action MADDPG on DN-WTA - NO problem-specific modules
(D1 red line). Contrast axes vs the MAPPO baseline: off-policy replay +
deterministic policy gradient + centralised per-agent Q critics
(marl/maddpg_net.CentralQCritic; joint-action embedding = per-platform
chosen-target obs features x_j in R^8, hold -> zero row;
permutation-invariant, NO target-id one-hot).

    actor    : DetActor = PoolMLPNet skeleton (capacity/features
               identical to the PoolMLPNet actor - isolates the
               paradigm axis)
    critic   : one Q_i(s, a_1..a_m) per platform, shared body + heads,
               input 35 + 8*m (75 at v4 m=5)
    gamma    : imported FROM marl.train (calibre red line)
    sampling : Gumbel-Softmax reparameterised exploration on masked
               logits, temperature 1.0 -> 0.1 (no OU noise - undefined
               on the discrete domain); evaluation = greedy argmax
    updates  : episode-end batched updates, <= --updates-per-step
               gradient steps per fresh env step; replay 1e5 transitions
    targets  : actor/critic target copies, soft update tau = 0.005
    reward   : R_team (marl/reward.py), marl/train.py folding convention
               (R_team[t] -> a_t, terminal events folded into the LAST
               decision step)
    early stop: val leak (s27-s30 x seeds 42-51, greedy, no CPLEX),
               patience over eval points

Products (flat --output): best.pt / train_log.jsonl / train_summary.json.
"""

import argparse
import copy
import json
import os
import random
import re
import sys
import time
from collections import deque

import torch

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(HERE)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from dwta.dn_instance import DNInstance                     # noqa: E402
from dwta.dn_env import DNEnv                               # noqa: E402
from marl.maddpg_net import DetActor, CentralQCritic, \
    assert_system_params                                    # noqa: E402
from marl.baseline_policy import MADDPGPolicy               # noqa: E402
from marl.train import critic_inputs, GAMMA                 # noqa: E402
from marl.reward import build_rewards, C_INVALID            # noqa: E402

DATA_DIR = os.path.join(PROJECT_ROOT, "data", "dn-data-v4")

SOFT_TAU = 0.005
LR_ACTOR = 1e-4
LR_CRITIC = 3e-4
BATCH = 256
BUFFER_SIZE = 100000
TAU_EXP_START, TAU_EXP_END = 1.0, 0.1
WALL_LIMIT_SEC = 2.5 * 3600.0     # v4 3h-tier baseline: <=2.5h train wall


def load_split(data_dir):
    """Fixed split by s-number protocol: s01-s02 test / s03-s26 train /
    s27-s30 val (works for v3 and v4 layouts alike)."""
    files = [f for f in os.listdir(data_dir)
             if re.match(r"dn_\d+x\d+_K\d+_s\d+\.txt$", f)]
    files.sort(key=lambda f: int(re.search(r"_s(\d+)\.txt$", f).group(1)))
    s_of = lambda f: int(re.search(r"_s(\d+)", f).group(1))  # noqa: E731
    train = [f for f in files if 3 <= s_of(f) <= 26]
    val = [f for f in files if s_of(f) >= 27]
    if not train or not val:
        raise SystemExit("[ERROR] bad split discovery in %s" % data_dir)
    return train, val


class Trainer(object):
    def __init__(self, args):
        self.args = args
        self.device = torch.device("cpu") if args.device == "cpu" \
            else self._pick(args.device)
        self.actor = DetActor().to(self.device)
        self.actor_target = copy.deepcopy(self.actor)
        for p in self.actor_target.parameters():
            p.requires_grad_(False)
        self.n_agents = None
        self.critic = self.critic_target = None
        self.opt_a = self.opt_c = None
        self.n_params = 0
        self.eval_pol = MADDPGPolicy("maddpg", model_path=None,
                                     device=args.device, greedy=True,
                                     seed=0)
        self.eval_pol.net = self.actor
        self.collector = MADDPGPolicy("maddpg", model_path=None,
                                      device=args.device, greedy=False,
                                      seed=args.seed, training=True,
                                      gumbel_tau=TAU_EXP_START)
        self.collector.net = self.actor
        self.train_files, self.val_files = load_split(args.data_dir)
        self.train_dns = [DNInstance(os.path.join(args.data_dir, f))
                          for f in self.train_files]
        self.val_dns = [DNInstance(os.path.join(args.data_dir, f))
                        for f in self.val_files]
        self.buffer = deque(maxlen=args.buffer)
        self.seed_counter = 300001
        self.env_steps = 0
        self.updates_done = 0
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

    def _log(self, rec):
        self._log_f.write(json.dumps(rec) + "\n")
        self._log_f.flush()

    # ------------------------------------------------------------------
    def _ensure_critics(self, m):
        if self.critic is not None:
            return
        self.n_agents = m
        self.critic = CentralQCritic(n_agents=m).to(self.device)
        self.critic_target = copy.deepcopy(self.critic)
        for p in self.critic_target.parameters():
            p.requires_grad_(False)
        self.n_params = assert_system_params(self.actor, self.critic)
        self.opt_a = torch.optim.Adam(self.actor.parameters(), lr=LR_ACTOR)
        self.opt_c = torch.optim.Adam(self.critic.parameters(),
                                      lr=LR_CRITIC)
        self._log({"event": "nets", "n_agents": m,
                   "system_params": self.n_params,
                   "red_line": "[1e3, 1e5]"})

    def _anneal_tau(self, it):
        span = max(1, self.args.anneal_iters)
        tau = TAU_EXP_START - (TAU_EXP_START - TAU_EXP_END) \
            * min(1.0, it / span)
        self.collector.tau = tau
        return tau

    # ------------------------------------------------------------------
    def collect_episode(self, dn):
        """One exploration episode; push joint transitions (s, a, r, s',
        done) into the replay buffer (MAPPO reward folding)."""
        env = DNEnv(dn, self.seed_counter)
        self.seed_counter += 1
        self._ensure_critics(dn.m)
        raw = []
        orig_act = self.collector.act

        def wrapped_act(e, t):
            actions, info = orig_act(e, t)
            tgt, glob, _a = critic_inputs(e, t, actions, dn)
            raw.append({"t": t,
                        "agents": self.collector.last_step_collect,
                        "tgt": tgt, "glob": glob})
            self.env_steps += 1
            return actions, info

        run_rec = env.run(type("W", (), {"act": staticmethod(
            wrapped_act)})())
        ci = self.args.c_invalid if self.args.c_invalid is not None \
            else C_INVALID
        rew = build_rewards(env, run_rec, dn, c_invalid=ci)
        K = len(rew["R_team"]) - 1
        r_by_t = {s["t"]: float(rew["R_team"][s["t"]]) for s in raw}
        if r_by_t:
            last_t = max(r_by_t)
            if K - 1 > last_t:
                r_by_t[last_t] += float(rew["R_team"][K - 1])
            r_by_t[last_t] += float(rew["R_team"][K])

        def featurize(rec):
            ags = [a for a in rec["agents"] if not a.get("empty")]
            if len(ags) != self.n_agents:
                return None
            act_x = torch.zeros(self.n_agents, 8)
            obs = []
            for k, a in enumerate(sorted(ags, key=lambda a: a["agent"])):
                x, pick = a["x"], a["pick"]
                obs.append({"x": x, "q": a["q"], "g": a["g"],
                            "mask": a["mask"]})
                if pick > 0 and pick - 1 < x.shape[0]:
                    act_x[k] = x[pick - 1]
            return {"obs": obs, "act_x": act_x, "tgt": rec["tgt"],
                    "glob": rec["glob"]}

        feats = [featurize(r) for r in raw]
        for k in range(len(feats)):
            cur = feats[k]
            nxt = feats[k + 1] if k + 1 < len(feats) else None
            if cur is None:
                continue
            self.buffer.append({
                "obs": cur["obs"], "act_x": cur["act_x"],
                "tgt": cur["tgt"], "glob": cur["glob"],
                "r": r_by_t.get(raw[k]["t"], 0.0),
                "next_obs": None if nxt is None else nxt["obs"],
                "next_tgt": None if nxt is None else nxt["tgt"],
                "next_glob": None if nxt is None else nxt["glob"],
                "done": 1.0 if nxt is None else 0.0,
            })
        return run_rec

    # ------------------------------------------------------------------
    def _stack_obs(self, samples, key):
        """Pad-stack m-agent obs rows over a batch of transitions ->
        (xb [Bm, Lmax, 8], qb, gb, pm [Bm, Lmax])."""
        B = len(samples)
        m = self.n_agents
        Lmax = max(max((o["x"].shape[0] for o in s[key]), default=0)
                   for s in samples)
        Lmax = max(Lmax, 1)
        xb = torch.zeros(B * m, Lmax, 8)
        qb = torch.zeros(B * m, 5)
        gb = torch.zeros(B * m, 3)
        pm = torch.zeros(B * m, Lmax, dtype=torch.bool)
        for b, s in enumerate(samples):
            for k, o in enumerate(s[key]):
                L = o["x"].shape[0]
                xb[b * m + k, :L] = o["x"]
                qb[b * m + k] = o["q"]
                gb[b * m + k] = o["g"]
                pm[b * m + k, :L] = True
        return xb, qb, gb, pm

    def _stack_critic(self, samples, prefix=""):
        B = len(samples)
        Lp = max(max(s[prefix + "tgt"].shape[0], 1) for s in samples)
        tb = torch.zeros(B, Lp, 5)
        tm = torch.zeros(B, Lp, dtype=torch.bool)
        gb = torch.stack([s[prefix + "glob"] for s in samples])
        for b, s in enumerate(samples):
            L = s[prefix + "tgt"].shape[0]
            tb[b, :L] = s[prefix + "tgt"]
            tm[b, :L] = True
        return tb, gb, tm

    @staticmethod
    def _act_embed(samples, key, picks):
        """Hard action embeddings [B, m, 8] from argmax picks
        (picks is the flattened [B*m] argmax over the [Bm, 1+L] logits)."""
        B = len(samples)
        m = len(samples[0][key])
        flat = picks.reshape(-1).tolist()
        ex = torch.zeros(B, m, 8)
        for b, s in enumerate(samples):
            for k, o in enumerate(s[key]):
                pk = int(flat[b * m + k])
                if pk > 0 and pk - 1 < o["x"].shape[0]:
                    ex[b, k] = o["x"][pk - 1]
        return ex

    def _to_dev(self, *ts):
        return tuple(t.to(self.device) for t in ts)

    # ------------------------------------------------------------------
    def update(self, n_steps):
        if self.critic is None or len(self.buffer) < BATCH:
            return 0.0, 0.0
        sc = sa = 0.0
        nb = 0
        for _ in range(n_steps):
            batch = random.sample(self.buffer, BATCH)
            xb, qb, gb, pm = self._stack_obs(batch, "obs")
            rs = torch.tensor([b["r"] for b in batch])
            ds = torch.tensor([b["done"] for b in batch])
            ab = torch.stack([b["act_x"] for b in batch])       # [B,m,8]
            tb, gcb, tmb = self._stack_critic(batch, "")
            dev = self.device

            # ---- TD targets (team reward -> shared target row) -------
            with torch.no_grad():
                nt = [b for b in batch if b["next_obs"] is not None]
                y = rs.clone()
                if nt:
                    xn, qn, gn, pn = self._stack_obs(nt, "next_obs")
                    picks = self.actor_target.forward_batch(
                        *self._to_dev(xn, qn, gn, pn)).argmax(dim=1)
                    en = self._act_embed(nt, "next_obs", picks.cpu())
                    tn, gcn, tmn = self._stack_critic(nt, "next_")
                    q_next = self.critic_target(*self._to_dev(tn, gcn, en,
                                                              tmn))
                    q_team = q_next.mean(dim=1).cpu()     # [B'] team rwd
                    base = torch.zeros(len(batch))
                    base[[k for k, b in enumerate(batch)
                          if b["next_obs"] is not None]] = q_team
                    y = y + GAMMA * (1.0 - ds) * base
            qc = self.critic(*self._to_dev(tb, gcb, ab, tmb))
            critic_loss = ((qc.cpu() - y.unsqueeze(1)) ** 2).mean()
            self.opt_c.zero_grad()
            critic_loss.backward()
            torch.nn.utils.clip_grad_norm_(self.critic.parameters(), 0.5)
            self.opt_c.step()

            # ---- actor loss (DPG via soft action embeddings) --------
            logits = self.actor.forward_batch(*self._to_dev(xb, qb, gb,
                                                            pm))
            probs = torch.softmax(logits / max(self.collector.tau, 1e-3),
                                  dim=1)
            soft = (probs[:, 1:].unsqueeze(1)
                    @ xb.to(dev)).squeeze(1).view(len(batch),
                                                  self.n_agents, 8)
            abd = ab.to(dev)
            tb_d, gcb_d, tmb_d = self._to_dev(tb, gcb, tmb)
            actor_loss = torch.zeros((), device=dev)
            for i in range(self.n_agents):
                Ei = abd.clone()
                Ei[:, i, :] = soft[:, i, :]
                qi = self.critic(tb_d, gcb_d, Ei, tmb_d)[:, i]
                actor_loss = actor_loss - qi.mean()
            actor_loss = actor_loss / self.n_agents
            self.opt_a.zero_grad()
            actor_loss.backward()
            torch.nn.utils.clip_grad_norm_(self.actor.parameters(), 0.5)
            self.opt_a.step()

            # ---- target soft updates -------------------------------
            with torch.no_grad():
                for p, pt in zip(self.critic.parameters(),
                                 self.critic_target.parameters()):
                    pt.mul_(1.0 - SOFT_TAU).add_(SOFT_TAU * p)
                for p, pt in zip(self.actor.parameters(),
                                 self.actor_target.parameters()):
                    pt.mul_(1.0 - SOFT_TAU).add_(SOFT_TAU * p)
            sc += float(critic_loss.item())
            sa += float(actor_loss.item())
            nb += 1
            self.updates_done += 1
        return sc / max(1, nb), sa / max(1, nb)

    # ------------------------------------------------------------------
    @torch.no_grad()
    def evaluate_val(self):
        rates = []
        for dn in self.val_dns:
            for seed in range(42, 52):
                env = DNEnv(dn, seed)
                self.eval_pol.reset_episode()
                rates.append(env.run(self.eval_pol)["leak_rate"])
        mean = sum(rates) / len(rates)
        std = (sum((r - mean) ** 2 for r in rates) / len(rates)) ** 0.5
        return mean, std

    # ------------------------------------------------------------------
    def save_ckpt(self, path, it=None):
        torch.save({
            "state_dict": self.actor.state_dict(),
            "critic_state_dict": self.critic.state_dict(),
            "kind": "maddpg",
            "iter": it,
            "best_val": None if self.best_val == float("inf")
            else self.best_val,
            "feature_spec": {"x": 8, "q": 5, "g": 3, "drop_m1": True},
            "params_count": self.n_params,
            "n_agents": self.n_agents,
        }, path)

    # ------------------------------------------------------------------
    def save_last(self, path, it, elapsed, eval_points=0, bad_points=0):
        """v5 §6.1.3 periodic resumable checkpoint (every eval point +
        <= 10 min cadence). Replay buffer is NOT serialised (too large);
        restarts re-collect - nets/targets/optimizers/counters/elapsed
        are restored."""
        self._ensure_critics(self.n_agents or self.train_dns[0].m)
        torch.save({
            "state_dict": self.actor.state_dict(),
            "actor_target_state_dict": self.actor_target.state_dict(),
            "critic_state_dict": self.critic.state_dict(),
            "critic_target_state_dict": self.critic_target.state_dict(),
            "kind": "maddpg",
            "opt_a": self.opt_a.state_dict(),
            "opt_c": self.opt_c.state_dict(),
            "iter": it,
            "best_val": None if self.best_val == float("inf")
            else self.best_val,
            "eval_points": eval_points,
            "bad_points": bad_points,
            "seed_counter": self.seed_counter,
            "env_steps": self.env_steps,
            "updates_done": self.updates_done,
            "elapsed_sec": elapsed,
            "feature_spec": {"x": 8, "q": 5, "g": 3, "drop_m1": True},
            "params_count": self.n_params,
            "n_agents": self.n_agents,
        }, path)

    def _load_full(self, ck):
        """Full-state restore from a last.pt checkpoint (critics are
        lazily built -> materialise at the ckpt's n_agents first)."""
        m = int(ck.get("n_agents") or self.train_dns[0].m)
        self._ensure_critics(m)
        self.actor.load_state_dict(ck["state_dict"])
        self.critic.load_state_dict(ck["critic_state_dict"])
        if "actor_target_state_dict" in ck:
            self.actor_target.load_state_dict(ck["actor_target_state_dict"])
        else:
            self.actor_target.load_state_dict(ck["state_dict"])
        if "critic_target_state_dict" in ck:
            self.critic_target.load_state_dict(
                ck["critic_target_state_dict"])
        else:
            self.critic_target.load_state_dict(ck["critic_state_dict"])
        self.eval_pol.net = self.actor
        self.collector.net = self.actor

    # ------------------------------------------------------------------
    def run(self):
        args = self.args
        t0 = time.time()
        ckpt = os.path.join(args.output, "best.pt")
        last_path = os.path.join(args.output, "last.pt")
        it = 0
        eval_points = 0
        bad_points = 0
        stopped = None
        resume_elapsed = 0.0
        if getattr(args, "resume", False):
            src = last_path if os.path.exists(last_path) else ckpt
            if not os.path.exists(src):
                raise FileNotFoundError(
                    "--resume needs %s or %s (nothing to resume from)"
                    % (last_path, ckpt))
            ck = torch.load(src, map_location="cpu")
            self._load_full(ck)
            it = int(ck.get("iter") or 0)
            if ck.get("best_val") is not None:
                self.best_val = float(ck["best_val"])
            if "opt_a" in ck:       # full resumable ckpt (last.pt format)
                try:
                    self.opt_a.load_state_dict(ck["opt_a"])
                    self.opt_c.load_state_dict(ck["opt_c"])
                except Exception as e:
                    print("[maddpg] optimizer state not restored (%s); "
                          "continuing with fresh optimizers" % e,
                          flush=True)
                self.seed_counter = int(ck.get("seed_counter",
                                                self.seed_counter))
                self.env_steps = int(ck.get("env_steps", self.env_steps))
                self.updates_done = int(ck.get("updates_done",
                                                self.updates_done))
                resume_elapsed = float(ck.get("elapsed_sec", 0.0))
                eval_points = int(ck.get("eval_points", 0))
                bad_points = int(ck.get("bad_points", 0))
            print("[maddpg] resume from %s: iter=%d best_val=%.5f "
                  "elapsed=%.0fs" % (src, it, self.best_val,
                                     resume_elapsed), flush=True)
        epi = args.episodes_per_iter
        wall_limit_sec = float(getattr(args, "wall_limit", 2.5)) * 3600.0
        last_hb = time.time()
        last_ckpt = time.time()
        while it < args.iters:
            elapsed = resume_elapsed + (time.time() - t0)
            if elapsed > wall_limit_sec:
                stopped = "wall_limit"
                break
            if time.time() - last_hb > 60.0:
                print("[hb] iter=%d elapsed=%.0fs budget=%.1fh"
                      % (it, elapsed, wall_limit_sec / 3600.0), flush=True)
                last_hb = time.time()
            leaks = []
            new_steps = 0
            for k in range(epi):
                dn = self.train_dns[(it * epi + k) % len(self.train_dns)]
                leaks.append(self.collect_episode(dn)["leak_rate"])
                new_steps += max(0, dn.K - 1)
            tau = self._anneal_tau(it)
            cl, al = self.update(int(round(args.updates_per_step
                                           * new_steps)))
            it += 1
            if time.time() - last_ckpt > 600.0:   # §6.1.3: <= 10 min
                self.save_last(last_path, it,
                               resume_elapsed + (time.time() - t0),
                               eval_points, bad_points)
                last_ckpt = time.time()
            if it % args.eval_every == 0 or it == args.iters:
                eval_points += 1
                vm, vs = self.evaluate_val()
                rec = {"event": "eval", "iter": it, "val_leak": vm,
                       "val_leak_std": vs,
                       "train_leak": sum(leaks) / len(leaks),
                       "critic_loss": cl, "actor_loss": al,
                       "tau_exp": tau, "buffer": len(self.buffer),
                       "env_steps": self.env_steps,
                       "updates": self.updates_done,
                       "wall_s": round(resume_elapsed
                                       + (time.time() - t0), 1)}
                self._log(rec)
                print("[maddpg] it=%d val=%.5f (best=%.5f) cl=%.4f "
                      "al=%.4f tau=%.2f buf=%d wall=%.0fs" %
                      (it, vm, min(self.best_val, vm), cl, al, tau,
                       len(self.buffer), rec["wall_s"]), flush=True)
                if vm < self.best_val - 1e-6:
                    self.best_val = vm
                    self.save_ckpt(ckpt, it)
                    bad_points = 0
                else:
                    bad_points += 1
                self.save_last(last_path, it,
                               resume_elapsed + (time.time() - t0),
                               eval_points, bad_points)
                last_ckpt = time.time()
                if bad_points >= args.patience:
                    stopped = "early_stop"
                    break
            else:
                self._log({"event": "iter", "iter": it,
                           "train_leak": sum(leaks) / len(leaks),
                           "critic_loss": cl, "actor_loss": al,
                           "tau_exp": tau, "buffer": len(self.buffer),
                           "env_steps": self.env_steps,
                           "updates": self.updates_done,
                           "wall_s": round(resume_elapsed
                                           + (time.time() - t0), 1)})
        try:      # keep last.pt fresh for post-stop restarts
            self.save_last(last_path, it,
                           resume_elapsed + (time.time() - t0),
                           eval_points, bad_points)
        except Exception:
            pass
        summary = {"algo": "maddpg", "data_dir": args.data_dir,
                   "seed": args.seed, "iters_done": it,
                   "stopped": stopped or "iters",
                   "best_val_leak": None if self.best_val ==
                   float("inf") else self.best_val,
                   "system_params": self.n_params,
                   "env_steps": self.env_steps,
                   "updates": self.updates_done,
                   "wall_s": round(resume_elapsed + (time.time() - t0), 1),
                   "gamma": GAMMA, "soft_tau": SOFT_TAU,
                   "lr_actor": LR_ACTOR, "lr_critic": LR_CRITIC,
                   "batch": BATCH, "buffer": args.buffer,
                   "updates_per_step": args.updates_per_step,
                   "device": str(self.device)}
        with open(os.path.join(args.output, "train_summary.json"),
                  "w") as f:
            json.dump(summary, f, indent=2)
        self._log({"event": "summary", **summary})
        self._log_f.close()
        print("[maddpg] done: %s" % json.dumps(summary), flush=True)


# ----------------------------------------------------------------------
def build_parser():
    p = argparse.ArgumentParser(description="v4 MADDPG baseline trainer")
    p.add_argument("--device", default="auto")
    p.add_argument("--seed", type=int, default=7)
    p.add_argument("--output", default="marl/ckpt_v4_maddpg")
    p.add_argument("--data-dir", default=DATA_DIR,
                   help="instance dir (default: v4 dn_5x100)")
    p.add_argument("--iters", type=int, default=1200,
                   help="v5 3h-tier baseline cap (1200 x 12 = 14.4k ep)")
    p.add_argument("--episodes-per-iter", type=int, default=12,
                   help="v5 3h-tier sampling volume (m = 10 doubles the "
                        "per-step cost vs v4's 24; 12 keeps the tier "
                        "budget; same tier as mappo/qmix)")
    p.add_argument("--eval-every", type=int, default=25)
    p.add_argument("--patience", type=int, default=6,
                   help="eval points without val improvement")
    p.add_argument("--wall-limit", type=float, default=2.5,
                   help="v5 §6.1.3: train wall-clock cap in HOURS "
                        "(default 2.5 = 3h tier minus 0.5h eval reserve)")
    p.add_argument("--resume", action="store_true",
                   help="v5 §6.1.3: resume from <output>/last.pt if "
                        "present (nets + targets + optimizers + counters "
                        "+ elapsed wall, budget-aware), else fall back to "
                        "best.pt (weights + iter + best_val); replay "
                        "buffer is re-collected")
    p.add_argument("--anneal-iters", type=int, default=720,
                   help="tau_exp linear 1.0 -> 0.1 horizon")
    p.add_argument("--buffer", type=int, default=BUFFER_SIZE)
    p.add_argument("--updates-per-step", type=float, default=0.25,
                   help="gradient steps per fresh env step (<= 1)")
    p.add_argument("--c-invalid", type=float, default=None,
                   help="override invalid-action penalty (default: "
                        "marl.reward.C_INVALID)")
    p.add_argument("--smoke", action="store_true",
                   help="2 iters / tiny eval - correctness harness")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.smoke:
        args.iters = 2
        args.episodes_per_iter = 3
        args.eval_every = 1
        args.anneal_iters = 2
        args.patience = 10
    random.seed(args.seed)
    torch.manual_seed(args.seed)
    os.makedirs(args.output, exist_ok=True)
    Trainer(args).run()


if __name__ == "__main__":
    main()

