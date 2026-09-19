"""E25-B5: QMIX baseline training for the DN-WTA v3 task (plus the
optional C1 IQL twin via --algo iql).

Deliberately standard value-based CTDE, contrasted against the
self-developed marl pipeline component by component:

    agent net : PoolMLPNet (MLP + target mean/max pooling, x in R^8 -
                M1 memory columns DROPPED, build_inputs drop_m1=True;
                shared parameters across the 3 platforms);
    mixing    : standard QMIX monotonic hypernetwork (QMixer, abs()
                weights) over the state = mean-pooled TRUE target
                features (raw 5-dim) + global row (pool water level /
                t / alive count) in R^8 - the mixer sees the
                training-side global state, execution stays per-agent
                greedy argmax;
    targets   : hard-updated target agent + mixer nets every
                --target-update iters; double-Q (DDQN style: the
                ONLINE nets pick the per-agent argmax action - a valid
                joint argmax thanks to mixing monotonicity - the
                TARGET nets evaluate it);
    TD        : TD(0) on the joint reward r_t = R_team events +
                c_invalid penalty (same folding convention as the
                MAPPO trainer: R_team[t] credited to a_t, terminal
                K-1/K events folded into the last decision step);
    explore   : eps-greedy 0.1 -> 0.02 linear over --anneal-iters,
                uniform over legal actions (hold included);
    replay    : episode-level buffer (last --buffer-episodes episodes),
                batch 512 transitions, Adam lr 3e-4;
    budget    : 128 episodes/iter (same sampling volume as MAPPO/marl
                e15), iters <= 3000, val early stop identical to
                marl/train.py (s27-s30 x seeds 42-51, greedy, patience
                in eval points).

--algo iql (C1, optional): identical EXCEPT no mixer - independent
per-agent DQN heads (still the shared agent network), per-agent TD
targets on the SAME team reward (independent learners, the classic
IQL baseline).

Products (flat dir --output): best.pt / train_log.jsonl /
train_summary.json (same layout as marl/train.py).
"""

import argparse
import copy
import json
import math
import os
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
from marl.baseline_policy import PoolMLPPolicy              # noqa: E402
from marl.baseline_net import PoolMLPNet, QMixer, \
    assert_params as assert_agent_params                    # noqa: E402
from marl.train import critic_inputs                        # noqa: E402
from marl.reward import build_rewards, C_INVALID            # noqa: E402

DATA_DIR = os.path.join(PROJECT_ROOT, "data", "dn-data-v3")
TRAIN_INSTS = ["dn_3x50_K10_s%02d.txt" % s for s in range(3, 27)]
VAL_INSTS = ["dn_3x50_K10_s%02d.txt" % s for s in range(27, 31)]

GAMMA = 0.99
LR = 3e-4
BATCH = 512
MIX_STATE_DIM = 8          # pooled true target features (5) + glob (3)
N_AGENTS = 3               # legacy constant - runtime value is derived
                           # from the dataset (Trainer.n_agents)
WALL_LIMIT_SEC = 2.5 * 3600.0     # v4 3h-tier baseline: <=2.5h train wall


def mix_state(tgt, glob):
    """(tgt [L,5], glob [3]) -> [8]: masked-mean pooled TRUE target
    features (raw 5-dim) + global row (pool level / t / alive)."""
    pooled = torch.zeros(5) if tgt.shape[0] == 0 else tgt.mean(dim=0)
    return torch.cat([pooled, glob])


class Trainer(object):
    def __init__(self, args):
        self.args = args
        self.algo = args.algo
        self.device = torch.device(
            "cpu") if args.device == "cpu" else self._pick(args.device)
        self.agent = PoolMLPNet().to(self.device)
        self.n_params = assert_agent_params(self.agent)
        # v4 migration: n_agents derived from --data-dir (v3: 3, v4: 5)
        from marl.data_split import discover_split, load_instances
        data_dir = getattr(args, "data_dir", None) or DATA_DIR
        train_files, val_files = discover_split(data_dir)
        self.train_dns = load_instances(data_dir, train_files)
        self.val_dns = load_instances(data_dir, val_files)
        self.n_agents = self.train_dns[0].m
        self.mixer = None
        if self.algo == "qmix":
            self.mixer = QMixer(state_dim=MIX_STATE_DIM,
                                n_agents=self.n_agents).to(self.device)
        self.agent_target = copy.deepcopy(self.agent)
        self.mixer_target = copy.deepcopy(self.mixer) if self.mixer \
            is not None else None
        for p in self.agent_target.parameters():
            p.requires_grad_(False)
        if self.mixer_target is not None:
            for p in self.mixer_target.parameters():
                p.requires_grad_(False)
        self.opt = torch.optim.Adam(
            list(self.agent.parameters())
            + (list(self.mixer.parameters())
               if self.mixer is not None else []), lr=LR)

        self.eval_pol = PoolMLPPolicy(self.algo, model_path=None,
                                      device=args.device, greedy=True,
                                      seed=0)
        self.eval_pol.net = self.agent
        self.collector = PoolMLPPolicy(self.algo, model_path=None,
                                       device=args.device, greedy=False,
                                       seed=args.seed, training=True)
        self.collector.net = self.agent
        self.collector.tau = 1.0            # exploration via eps-greedy

        self.seed_counter = 200001
        self.env_steps = 0
        self.best_val = float("inf")
        self.buffer = deque(maxlen=args.buffer_episodes)
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
    def _anneal_eps(self, it):
        span = max(1, self.args.anneal_iters)
        eps = 0.1 - (0.1 - 0.02) * min(1.0, it / span)
        self.collector.epsilon = eps
        return eps

    # ------------------------------------------------------------------
    def collect_episode(self, dn):
        """One eps-greedy episode -> list of transitions (per decision
        step). Reward folding identical to the MAPPO trainer."""
        env = DNEnv(dn, self.seed_counter)
        self.seed_counter += 1
        snapshots = []
        orig_act = self.collector.act

        def wrapped_act(e, t):
            actions, info = orig_act(e, t)
            tgt, glob, _act = critic_inputs(e, t, actions, dn)
            snapshots.append({
                "t": t,
                "agents": self.collector.last_step_collect,
                "tgt": tgt, "glob": glob,
                "actions": dict(actions),
            })
            self.env_steps += 1
            return actions, info

        run_rec = env.run(
            type("W", (), {"act": staticmethod(wrapped_act)})())
        ci = self.args.c_invalid if self.args.c_invalid is not None \
            else C_INVALID
        rew = build_rewards(env, run_rec, dn, c_invalid=ci)

        K = len(rew["R_team"]) - 1
        dec = [s for s in snapshots if s["t"] <= K - 2]
        trans = []
        for k, s in enumerate(dec):
            r_t = float(rew["R_team"][s["t"]])
            nxt = dec[k + 1] if k + 1 < len(dec) else None
            done = 0.0 if nxt is not None else 1.0
            if nxt is None:
                r_t += float(rew["R_team"][K - 1]) \
                    if K - 1 > s["t"] else 0.0
                r_t += float(rew["R_team"][K])
            trans.append({"step": s, "next": nxt, "r": r_t, "done": done})
        return trans, run_rec

    # ------------------------------------------------------------------
    def _stack_trans(self, batch):
        """Batch of transitions -> padded tensors, agent-major rows:
        agent inputs [3B, ...]; picks [3B]; mix states [B, 8]."""
        B = len(batch)
        Lc = 1
        Ln = 1
        has_next = False
        for tr in batch:
            for e in tr["step"]["agents"]:
                if not e.get("empty"):
                    Lc = max(Lc, e["x"].shape[0])
            if tr["next"] is not None:
                has_next = True
                for e in tr["next"]["agents"]:
                    if not e.get("empty"):
                        Ln = max(Ln, e["x"].shape[0])
        xc = torch.zeros(self.n_agents * B, Lc, 8)
        pc = torch.zeros(self.n_agents * B, Lc, dtype=torch.bool)
        mc = torch.zeros(self.n_agents * B, Lc, dtype=torch.bool)
        qc = torch.zeros(self.n_agents * B, 5)
        gc = torch.zeros(self.n_agents * B, 3)
        picks = torch.zeros(self.n_agents * B, dtype=torch.long)
        if has_next:
            xn = torch.zeros(self.n_agents * B, Ln, 8)
            pn = torch.zeros(self.n_agents * B, Ln, dtype=torch.bool)
            mn = torch.zeros(self.n_agents * B, Ln, dtype=torch.bool)
            qn = torch.zeros(self.n_agents * B, 5)
            gn = torch.zeros(self.n_agents * B, 3)
        else:
            xn = pn = mn = qn = gn = None
        sc_t = torch.zeros(B, MIX_STATE_DIM)
        sc_n = torch.zeros(B, MIX_STATE_DIM) if has_next else None
        rs = torch.zeros(B)
        ds = torch.zeros(B)

        for b, tr in enumerate(batch):
            st = tr["step"]
            sc_t[b] = mix_state(st["tgt"], st["glob"])
            rs[b] = tr["r"]
            ds[b] = tr["done"]
            for a_i, e in enumerate(st["agents"]):
                r3 = self.n_agents * b + a_i
                if e.get("empty"):
                    picks[r3] = 0        # hold; logits [1] at L=0
                    continue
                L = e["x"].shape[0]
                xc[r3, :L] = e["x"]
                pc[r3, :L] = True
                mc[r3, :L] = e["mask"]
                qc[r3] = e["q"]
                gc[r3] = e["g"]
                picks[r3] = e["pick"]
            if tr["next"] is not None:
                nx = tr["next"]
                sc_n[b] = mix_state(nx["tgt"], nx["glob"])
                for a_i, e in enumerate(nx["agents"]):
                    r3 = self.n_agents * b + a_i
                    if e.get("empty"):
                        continue
                    L = e["x"].shape[0]
                    xn[r3, :L] = e["x"]
                    pn[r3, :L] = True
                    mn[r3, :L] = e["mask"]
                    qn[r3] = e["q"]
                    gn[r3] = e["g"]
        return xc, pc, mc, qc, gc, picks, xn, pn, mn, qn, gn, \
            sc_t, sc_n, rs, ds

    # ------------------------------------------------------------------
    def _q_gather(self, net, x, p, m, q, g, picks):
        """[3B, 1+L] masked Q -> gathered Q_i(a_i) [3B] -> [B, 3]."""
        logits = net.forward_batch(x, q, g, p)
        feas = torch.cat([torch.ones(logits.shape[0], 1,
                                     dtype=torch.bool,
                                     device=logits.device), m.to(
                                         logits.device)], dim=1)
        masked = logits.masked_fill(~feas, -float("inf"))
        qs = masked.gather(1, picks.to(logits.device)
                           .unsqueeze(1)).squeeze(1)
        return qs.view(-1, self.n_agents), masked

    def _td_targets(self, xn, pn, mn, qn, gn, sc_n, rs, ds):
        """Double-Q TD(0) targets: ONLINE agent picks the per-agent
        argmax (valid joint argmax via monotone mixing), TARGET nets
        evaluate. IQL: per-agent targets, no mixing."""
        with torch.no_grad():
            dev = self.device
            qn_d, pn_d, mn_d = qn.to(dev), pn.to(dev), mn.to(dev)
            _, masked_on = self._q_gather(self.agent, xn.to(dev),
                                          pn_d, mn_d, qn_d, gn.to(dev),
                                          torch.zeros(xn.shape[0],
                                                       dtype=torch.long))
            a_star = masked_on.argmax(dim=1)               # [3B]
            _, masked_tg = self._q_gather(self.agent_target,
                                          xn.to(dev), pn_d, mn_d, qn_d,
                                          gn.to(dev), a_star)
            if self.algo == "qmix":
                qs_star = masked_tg.gather(1, a_star.unsqueeze(1)) \
                    .squeeze(1).view(-1, self.n_agents)
                q_tot_next = self.mixer_target(qs_star, sc_n.to(dev))
                return rs.to(dev) + GAMMA * (1.0 - ds.to(dev)) \
                    * q_tot_next
            # IQL: independent per-agent targets on the same team reward
            qs_star = masked_tg.gather(1, a_star.unsqueeze(1)) \
                .squeeze(1).view(-1, self.n_agents)
            return rs.to(dev).unsqueeze(1) + GAMMA \
                * (1.0 - ds.to(dev)).unsqueeze(1) * qs_star

    # ------------------------------------------------------------------
    def train_step(self):
        if len(self.buffer) < 4:
            return 0.0, 0
        all_trans = [t for ep in self.buffer for t in ep]
        if len(all_trans) < BATCH:
            return 0.0, 0
        losses = []
        for _ in range(self.args.batches_per_iter):
            idx = torch.randint(0, len(all_trans), (BATCH,))
            batch = [all_trans[i] for i in idx.tolist()]
            xc, pc, mc, qc, gc, picks, xn, pn, mn, qn, gn, sc_t, \
                sc_n, rs, ds = self._stack_trans(batch)
            self.opt.zero_grad()
            try:
                qs, _ = self._q_gather(self.agent, xc.to(self.device),
                                       pc.to(self.device),
                                       mc.to(self.device),
                                       qc.to(self.device),
                                       gc.to(self.device), picks)
                if self.algo == "qmix":
                    q_tot = self.mixer(qs, sc_t.to(self.device))
                    y = self._td_targets(xn, pn, mn, qn, gn, sc_n,
                                         rs, ds)
                    loss = ((q_tot - y) ** 2).mean()
                else:
                    y = self._td_targets(xn, pn, mn, qn, gn, sc_n,
                                         rs, ds)            # [B, 3]
                    loss = ((qs - y) ** 2).mean()
                loss.backward()
                torch.nn.utils.clip_grad_norm_(
                    self.agent.parameters(), 10.0)
                self.opt.step()
                losses.append(float(loss.item()))
            except RuntimeError as e:
                if self.device.type != "mps":
                    raise
                print("[qmix-train] MPS batch failed (%s) -> CPU" % e)
                self.device = torch.device("cpu")
                self.agent.to(self.device)
                self.agent_target.to(self.device)
                if self.mixer is not None:
                    self.mixer.to(self.device)
                    self.mixer_target.to(self.device)
        return (sum(losses) / max(1, len(losses)),
                len(losses))

    # ------------------------------------------------------------------
    def _sync_targets(self):
        self.agent_target.load_state_dict(self.agent.state_dict())
        if self.mixer_target is not None:
            self.mixer_target.load_state_dict(self.mixer.state_dict())

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
        ckpt = {
            "state_dict": self.agent.state_dict(),
            "kind": self.algo,
            "iter": it,
            "best_val": (None if self.best_val == float("inf")
                         else self.best_val),
            "feature_spec": {"x": 8, "q": 5, "g": 3, "drop_m1": True},
            "params_count": self.n_params,
        }
        if self.mixer is not None:
            ckpt["mixer_state_dict"] = self.mixer.state_dict()
        torch.save(ckpt, path)

    # ------------------------------------------------------------------
    def save_last(self, path, it, elapsed, eval_points=0, bad_points=0):
        """v5 §6.1.3 periodic resumable checkpoint (every eval point +
        <= 10 min cadence). Buffer is NOT serialised (too large); restarts
        re-collect - only optimizer/net/counter state is restored."""
        ckpt = {
            "state_dict": self.agent.state_dict(),
            "kind": self.algo,
            "opt": self.opt.state_dict(),
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
        }
        if self.mixer is not None:
            ckpt["mixer_state_dict"] = self.mixer.state_dict()
            ckpt["mixer_target_state_dict"] = \
                self.mixer_target.state_dict()
        ckpt["agent_target_state_dict"] = \
            self.agent_target.state_dict()
        torch.save(ckpt, path)

    def _load_weights(self, ckpt):
        self.agent.load_state_dict(ckpt["state_dict"])
        if "agent_target_state_dict" in ckpt:
            self.agent_target.load_state_dict(
                ckpt["agent_target_state_dict"])
        elif "state_dict" in ckpt:
            self.agent_target.load_state_dict(ckpt["state_dict"])
        if self.mixer is not None and "mixer_state_dict" in ckpt:
            self.mixer.load_state_dict(ckpt["mixer_state_dict"])
            if "mixer_target_state_dict" in ckpt:
                self.mixer_target.load_state_dict(
                    ckpt["mixer_target_state_dict"])
            else:
                self.mixer_target.load_state_dict(
                    ckpt["mixer_state_dict"])
        self.eval_pol.net = self.agent
        self.collector.net = self.agent

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
            if "opt" in ck:        # full resumable ckpt (last.pt format)
                try:
                    self.opt.load_state_dict(ck["opt"])
                except Exception as e:
                    print("[qmix-train] optimizer state not restored (%s); "
                          "continuing with a fresh optimizer" % e,
                          flush=True)
                self.seed_counter = int(ck.get("seed_counter",
                                                self.seed_counter))
                self.env_steps = int(ck.get("env_steps", self.env_steps))
                resume_elapsed = float(ck.get("elapsed_sec", 0.0))
                eval_points = int(ck.get("eval_points", 0))
                bad_points = int(ck.get("bad_points", 0))
            print("[%s-train] resume from %s: iter=%d best_val=%.4f "
                  "elapsed=%.0fs"
                  % (self.algo, src, it, self.best_val, resume_elapsed),
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
            train_leaks = []
            for _ in range(epi):
                dn = self.train_dns[(it * epi + _) % len(self.train_dns)]
                trans, run_rec = self.collect_episode(dn)
                self.buffer.append(trans)
                train_leaks.append(run_rec["leak_rate"])
            eps = self._anneal_eps(it)
            loss, nb = self.train_step()
            it += 1
            if it % args.target_update == 0:
                self._sync_targets()
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
                    "eps": round(eps, 4),
                    "td_loss": round(loss, 6),
                    "batches": nb,
                    "buffer_trans": sum(len(ep) for ep in self.buffer),
                }
                self._log_f.write(json.dumps(row) + "\n")
                self._log_f.close()
                self._log_f = open(self.log_path, "a")
                print("[%s iter %6d] train %.4f | val %.4f+-%.4f | "
                      "eps %.3f | %.0fs"
                      % (self.algo, it, row["train_leak"], val_mean,
                         val_std, eps, row["wall_sec"]), flush=True)
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
                              "device": str(self.device),
                              "algo": self.algo},
        }
        with open(os.path.join(args.output, "train_summary.json"),
                  "w") as f:
            json.dump(summary, f, indent=2)
        self._log_f.close()
        print("%s training done: %s | best val %.4f | wall %.0fs"
              % (self.algo, summary["final_metrics"]["stop_reason"],
                 self.best_val if self.best_val != float("inf") else -1,
                 wall))


def main(argv=None):
    here = os.path.dirname(os.path.abspath(__file__))
    ap = argparse.ArgumentParser(
        description="E25 QMIX (or C1 IQL) baseline training")
    ap.add_argument("--algo", choices=["qmix", "iql"], default="qmix")
    ap.add_argument("--iters", type=int, default=1200,
                    help="v5 3h-tier baseline cap (1200 x 12 = 14.4k ep)")
    ap.add_argument("--eval-every", type=int, default=25)
    ap.add_argument("--patience", type=int, default=12,
                    help="early-stop patience in EVAL POINTS (3h tier)")
    ap.add_argument("--episodes-per-iter", type=int, default=12,
                    help="v5 3h-tier sampling volume (m = 10 doubles the "
                         "per-step cost vs v4's 24; 12 keeps the tier "
                         "budget; same tier as mappo/maddpg)")
    ap.add_argument("--wall-limit", type=float, default=2.5,
                    help="v5 §6.1.3: train wall-clock cap in HOURS "
                         "(default 2.5 = 3h tier minus 0.5h eval reserve)")
    ap.add_argument("--resume", action="store_true",
                    help="v5 §6.1.3: resume from <output>/last.pt if "
                         "present (nets + targets + optimizer + counters "
                         "+ elapsed wall, budget-aware), else fall back to "
                         "best.pt (weights + iter + best_val); replay "
                         "buffer is re-collected")
    ap.add_argument("--batches-per-iter", type=int, default=4,
                    help="gradient batches of 512 transitions per iter")
    ap.add_argument("--buffer-episodes", type=int, default=10000)
    ap.add_argument("--target-update", type=int, default=200,
                    help="hard target-net sync every N iters")
    ap.add_argument("--anneal-iters", type=int, default=2000)
    ap.add_argument("--device", default="auto",
                    choices=["auto", "mps", "cpu"])
    ap.add_argument("--data-dir", default=DATA_DIR,
                    help="instance dir (default v3 dn_3x50; v4 runs pass "
                         "data/dn-data-v4 - split protocol is fixed)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--c-invalid", type=float, default=None,
                    help="invalid-engagement penalty (default reward.py "
                         "C_INVALID=0.01; R_team keeps the penalty, no "
                         "shaping)")
    ap.add_argument("--output", default=None)
    args = ap.parse_args(argv)
    if args.output is None:
        args.output = os.path.abspath(os.path.join(
            here, "..", "output",
            "e25_qmix" if args.algo == "qmix" else "e25_iql"))
    else:
        args.output = os.path.abspath(args.output)
    os.makedirs(args.output, exist_ok=True)
    tr = Trainer(args)
    print("device=%s algo=%s agent_params=%d"
          % (tr.device, tr.algo, tr.n_params))
    tr.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
