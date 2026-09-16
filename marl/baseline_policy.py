"""PoolMLPPolicy: dn_policies-interface adapter for the E24/E25 learning
baselines (MAPPO / QMIX / IQL).

Execution path mirrors MarlPolicy exactly, EXCEPT:
    * features are built with build_inputs(drop_m1=True)  -> x in R^8
      (no M1-memory columns: the baselines must not depend on the
      lambda / n_hat memory channel);
    * the agent network is the PoolMLPNet MLP + mean/max pooling head
      (marl/baseline_net.py), NOT the set-attention MarlNet;
    * QMIX/IQL checkpoints load the SAME agent network structure (the
      mixer is a training-side module only - greedy per-agent argmax
      needs no mixing), so one adapter serves mappo / qmix / iql.

Red lines honoured (same as MarlPolicy):
    * NEVER touches env.rng - training sampling uses an isolated
      torch.Generator; evaluation runs greedy argmax => deterministic
      per-seed result_hash;
    * reset_episode() + automatic t-rewind detection;
    * device auto = MPS with fallback to CPU;
    * the per-step CPLEX reference (when attached) is REPORTED only.
"""

import os
import sys

import torch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from marl.perceive import AgentMemory, build_inputs          # noqa: E402
from marl.baseline_net import PoolMLPNet                     # noqa: E402
from marl.masking import feasible_mask                       # noqa: E402
from marl.policy import _pick_device                         # noqa: E402

KINDS = ("mappo", "qmix", "iql")


class PoolMLPPolicy(object):
    """kind: 'mappo' | 'qmix' | 'iql' (execution identical - greedy
    per-agent argmax on the PoolMLPNet logits; the kind only pins the
    checkpoint layout / name)."""

    needs_solver = False

    def __init__(self, policy_kind="mappo", model_path=None,
                 device="auto", greedy=True, seed=0, training=False,
                 with_reference=False, solver=None, tmp_dir=None,
                 epsilon=0.0):
        if policy_kind not in KINDS:
            raise ValueError("policy_kind must be one of %s" % (KINDS,))
        self.name = policy_kind
        self.kind = policy_kind
        self.device = _pick_device(device)
        self.greedy = greedy
        self.training = training
        self.epsilon = float(epsilon)   # eps-greedy exploration (value
        #                                methods: QMIX/IQL; PPO keeps 0)
        self.net = PoolMLPNet().to(self.device)
        if model_path is not None:
            ckpt = torch.load(model_path, map_location=self.device,
                              weights_only=True)
            spec = ckpt.get("feature_spec", {})
            if int(spec.get("x", 8)) != 8:
                raise ValueError(
                    "checkpoint feature_spec %r is not the drop-M1 x=8 "
                    "layout expected by %s" % (spec, policy_kind))
            if ckpt.get("kind", policy_kind) != policy_kind:
                raise ValueError(
                    "checkpoint kind %r != requested policy %r"
                    % (ckpt.get("kind"), policy_kind))
            self.net.load_state_dict(ckpt["state_dict"])
        if training:
            self.net.train()
        else:
            self.net.eval()
        self.params_count = self.net.params_count()
        self._gen = torch.Generator()          # isolated sampling stream
        self._gen.manual_seed(int(seed))
        self.tau = 1.0                          # sampling temperature
        self._ref = None
        if with_reference:
            from dwta.dn_policies import CplexPolicy
            self._ref = CplexPolicy(solver, tmp_dir)
        self.reset_episode()

    # ------------------------------------------------------------------
    def reset_episode(self) -> None:
        self._mems = None
        self._last_t = -1
        self.last_step_collect = None

    def _ensure_mems(self, m: int):
        if self._mems is None or len(self._mems) != m:
            self._mems = [AgentMemory() for _ in range(m)]

    # ------------------------------------------------------------------
    @torch.no_grad()
    def _forward_logits(self, feats):
        """One agent forward with CPU fallback on MPS errors."""
        try:
            logits = self.net(feats["x"].to(self.device),
                              feats["q"].to(self.device),
                              feats["g"].to(self.device))
            return logits.cpu()
        except RuntimeError as e:
            if self.device.type != "mps":
                raise
            print("[%s] MPS forward failed (%s) - falling back to CPU"
                  % (self.name, e))
            self.device = torch.device("cpu")
            self.net.to(self.device)
            logits = self.net(feats["x"], feats["q"], feats["g"])
            return logits.cpu()

    # ------------------------------------------------------------------
    def act(self, env, t: int):
        dn = env.dn
        m = dn.m
        if t <= self._last_t:
            self.reset_episode()          # rewind -> fresh episode
        self._ensure_mems(m)
        self._last_t = t

        actions = {}
        collect = [] if self.training else None
        for i in range(m):
            obs_i = env.get_observation(i, t)
            mem = self._mems[i]
            mem.update(obs_i, t)
            feats = build_inputs(obs_i, mem, dn, drop_m1=True)
            logits = self._forward_logits(feats)      # [1+L] hold first
            L = len(feats["alive_ids"])
            if L == 0:
                actions[i] = None
                if collect is not None:
                    collect.append({"agent": i, "empty": True})
                continue
            full_mask = feasible_mask(obs_i, t, dn)
            ok_by_id = {tr["id"]: ok for tr, ok in
                        zip(obs_i["targets"], full_mask)}
            mask = [ok_by_id[j] for j in feats["alive_ids"]]
            masked = logits.clone()
            for jj, ok in enumerate(mask):
                if not ok:
                    masked[1 + jj] = -float("inf")
            logp_all = torch.log_softmax(masked / self.tau, dim=0)
            if self.greedy or (not any(mask)) or env.pool <= 0:
                pick = int(torch.argmax(masked).item())
            elif self.epsilon > 0.0 and float(
                    torch.rand(1, generator=self._gen).item()) \
                    < self.epsilon:
                # eps-greedy: uniform over legal actions (hold INCLUDED)
                legal = [0] + [1 + jj for jj, ok in enumerate(mask)
                               if ok]
                pick = legal[int(torch.randint(
                    len(legal), (1,), generator=self._gen).item())]
            else:
                probs = torch.exp(logp_all)
                if not torch.isfinite(probs).all():
                    pick = 0
                else:
                    pick = int(torch.multinomial(
                        probs, 1, generator=self._gen).item())
            actions[i] = None if pick == 0 else feats["alive_ids"][pick - 1]
            if collect is not None:
                collect.append({
                    "agent": i, "empty": False,
                    "x": feats["x"], "q": feats["q"], "g": feats["g"],
                    "mask": torch.tensor(mask, dtype=torch.bool),
                    "pick": pick,
                    "logp": float(logp_all[pick].item()),
                    "tau": self.tau,
                })
        if collect is not None:
            self.last_step_collect = collect

        for i, j in actions.items():
            if j is not None:
                self._mems[i].note_own_shot(j, t)

        info = {"solved": True, "failed_agents": 0}
        if self._ref is not None:
            _, ref_info = self._ref.act(env, t)
            info["reference_cost"] = ref_info.get("objective")
            info["reference_solved"] = ref_info.get("solved", False)
            info["detail"] = ref_info.get("detail")
        return actions, info


# ----------------------------------------------------------------------
# smoke test: 3 seeds on s01 with a random-init checkpoint
# ----------------------------------------------------------------------

def _selftest():
    import os
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    from dwta.dn_instance import DNInstance
    from dwta.dn_env import DNEnv
    ckpt_dir = os.path.join(here, "output", "e24_smoke")
    os.makedirs(ckpt_dir, exist_ok=True)

    dn = DNInstance(os.path.join(here, "data", "dn-data-v3",
                                 "dn_3x50_K10_s01.txt"))
    for kind in KINDS:
        ckpt_path = os.path.join(ckpt_dir, "init_%s.pt" % kind)
        torch.manual_seed(0)
        net = PoolMLPNet()
        torch.save({"state_dict": net.state_dict(), "kind": kind,
                    "feature_spec": {"x": 8, "q": 5, "g": 3},
                    "params_count": net.params_count()}, ckpt_path)
        pol = PoolMLPPolicy(kind, ckpt_path, device="auto",
                            greedy=True, seed=0)
        print("%s: device=%s params=%d" % (kind, pol.device,
                                           pol.params_count))
        for seed in (42, 43, 44):
            env = DNEnv(dn, seed)
            pol.reset_episode()
            rec = env.run(pol)
            illegal = sum(s["illegal_actions"] for s in rec["steps"])
            assert illegal == 0, "illegal fire detected"
        # determinism: same seed -> identical hash of the run record
        env = DNEnv(dn, 7)
        pol.reset_episode()
        r1 = env.run(pol)["leak_rate"]
        env = DNEnv(dn, 7)
        pol.reset_episode()
        r2 = env.run(pol)["leak_rate"]
        assert r1 == r2, "non-deterministic eval path"
    print("marl/baseline_policy.py selftest: ALL PASS")


if __name__ == "__main__":
    _selftest()
