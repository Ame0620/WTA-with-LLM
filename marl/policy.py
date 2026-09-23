"""MarlPolicy: dn_policies-interface adapter for the learned actor.

Execution path (evaluation / deployment):
    per step t, per agent i (information boundary §7 only):
        obs_i = env.get_observation(i, t)          # shared + own
        mem_i.update(obs_i, t)                     # M1 lambda recursion
        feats  = build_inputs(obs_i, mem_i, dyn)   # public priors only
        logits = MarlNet(feats)                    # M2+M3
        action = argmax(mask(logits))              # M4, greedy mode
        mem_i.note_own_shot(...)                   # private memory

Red lines honoured here:
    * NEVER touches env.rng - sampling uses an isolated torch.Generator
      (training only; evaluation runs greedy argmax => deterministic
      per-seed result_hash);
    * reset_episode() + automatic t-rewind detection (cross-seed reuse
      safety, conflict #5);
    * device auto = MPS with try/except fallback to CPU.

v5 ablation (spec §3.4/§3.8):
    * actor_type in {"set_attention" (CASP on, x=10),
                     "pool_mlp"      (CASP off, x=8, M1 features dropped)};
    * when loading a checkpoint the network structure / input dim are
      restored from the checkpoint METADATA (ablation/actor_type/
      feature_spec.drop_m1) - guessing from the checkpoint's directory
      name is FORBIDDEN; a checkpoint lacking the 'ablation' field is
      rejected (eval-side strictness, spec §3.8);
    * mechanism instrumentation (spec §3.6, eval side):
        - repeat_targeting_total: # (step, target) events where >=2
          platforms selected the same target at the same step;
        - fwd_us_total / fwd_calls: cumulative pure-forward latency.
      Pure counters - they never touch any RNG stream or tensor value.
"""

import math
import os
import sys
import time

import torch

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from marl.perceive import AgentMemory, build_inputs          # noqa: E402
from marl.network import MarlNet, assert_params              # noqa: E402
from marl.masking import feasible_mask                       # noqa: E402


def _pick_device(device: str = "auto") -> torch.device:
    if device != "auto":
        return torch.device(device)
    if getattr(torch.backends, "mps", None) is not None \
            and torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


class MarlPolicy(object):
    name = "marl"
    needs_solver = False

    def __init__(self, model_path: str = None, device: str = "auto",
                 greedy: bool = True, seed: int = 0,
                 training: bool = False, with_reference=False,
                 solver=None, tmp_dir=None,
                 actor_type: str = None, drop_m1: bool = None,
                 _env=None):
        # _env: environment mapping override (audit tests inject a
        # controlled MARL_EXPECT_RESHAPING; production callers use the
        # process env - identical code path either way)
        env_src = os.environ if _env is None else _env
        self.device = _pick_device(device)
        self.greedy = greedy
        self.training = training
        # ---- structure selection ------------------------------------
        # model_path given: restore from checkpoint metadata ONLY.
        # no model_path (training host): explicit actor_type/drop_m1
        # (defaults: the historical set_attention / full 10-dim x).
        ckpt = None
        if model_path is not None:
            ckpt = torch.load(model_path, map_location=self.device,
                              weights_only=True)
            # ---- metadata gates (ablation spec §3.8, r2 spec §3.2) ----
            # Default path stays STRICT: a checkpoint lacking the
            # 'ablation'/'reshaping' metadata is rejected - the evaluator
            # must never guess the structure / recalibration scalars.
            # Explicit opt-in escape hatch (branch01 compat, 2026-09-23):
            # with MARL_ALLOW_LEGACY=1 exported, a pre-metadata (v3-era,
            # e.g. the frozen output/e20_retrain/c010/best.pt) checkpoint
            # is accepted and evaluated under its HISTORICAL semantics:
            # actor_type=set_attention, drop_m1=False (full 10-dim x,
            # restored via the .get() fallbacks below), no reshaping
            # (phi_scale, credit_alpha, cf_beta) = (1, 1, 1) - identical
            # to the S0-snapshot code path that produced the checkpoint.
            allow_legacy = env_src.get("MARL_ALLOW_LEGACY", "").strip() \
                not in ("", "0", "false", "False")
            legacy_missing = [f for f in ("ablation", "reshaping")
                              if f not in ckpt]
            if legacy_missing and not allow_legacy:
                raise ValueError(
                    "[marl] checkpoint %s lacks metadata field(s) %s - "
                    "pre-metadata checkpoints cannot be evaluated by the "
                    "ablation/r2 pipeline (spec §3.8, r2 spec §3.2/§11); "
                    "refusing to guess. Export MARL_ALLOW_LEGACY=1 to "
                    "evaluate a v3-era checkpoint under the historical "
                    "structure (set_attention, full 10-dim x, no "
                    "reshaping)."
                    % (model_path, ", ".join(repr(f)
                                             for f in legacy_missing)))
            if legacy_missing and allow_legacy:
                print("[marl] WARNING: checkpoint %s lacks metadata "
                      "field(s) %s; MARL_ALLOW_LEGACY=1 -> evaluating "
                      "under historical semantics (set_attention, "
                      "drop_m1=False, no reshaping)"
                      % (model_path, ", ".join(legacy_missing)),
                      flush=True)
            # ---- r2 §3.2: recalibration metadata gate ----------------
            # (a) the field itself is mandatory: round-1 (e49) checkpoints
            #     predate it and are REJECTED on purpose - the evaluator
            #     must never guess which (lambda, alpha, beta) produced
            #     a model;
            # (b) with MARL_EXPECT_RESHAPING="lam,alpha,beta" exported
            #     (set by run_e54_batch.sh from the locked e52 pick) any
            #     mismatch raises at load time - anti-cross-arm guard.
            #     (legacy checkpoints predate the r2 arms entirely and
            #     carry no 'reshaping' field - they skip this cross-arm
            #     check by construction; nothing to cross with.)
            if "reshaping" in ckpt:
                got = (float(ckpt["reshaping"].get("phi_scale", 1.0)),
                       float(ckpt["reshaping"].get("credit_alpha", 1.0)),
                       float(ckpt["reshaping"].get("cf_beta", 1.0)))
                expect = env_src.get("MARL_EXPECT_RESHAPING", "").strip()
                if expect:
                    try:
                        want = tuple(float(x) for x in expect.split(","))
                    except ValueError:
                        raise ValueError(
                            "[marl] MARL_EXPECT_RESHAPING=%r is not a "
                            "'phi_scale,credit_alpha,cf_beta' triple"
                            % expect)
                    if len(want) != 3 or want != got:
                        raise ValueError(
                            "[marl] checkpoint %s reshaping %s != expected "
                            "%s (anti-cross-arm guard, r2 spec §6.5)"
                            % (model_path, got, want))
            meta_actor = ckpt.get("actor_type", "set_attention")
            spec = ckpt.get("feature_spec", {}) or {}
            meta_drop = bool(spec.get("drop_m1", False))
            if actor_type is None:
                actor_type = meta_actor
            if drop_m1 is None:
                drop_m1 = meta_drop
            if actor_type != meta_actor or bool(drop_m1) != meta_drop:
                raise ValueError(
                    "[marl] requested structure (%s, drop_m1=%s) conflicts "
                    "with checkpoint metadata (%s, drop_m1=%s)"
                    % (actor_type, drop_m1, meta_actor, meta_drop))
        if actor_type is None:
            actor_type = "set_attention"
        if drop_m1 is None:
            drop_m1 = False
        self.actor_type = actor_type
        self.drop_m1 = bool(drop_m1)
        if actor_type == "set_attention":
            if self.drop_m1:
                raise ValueError("[marl] set_attention requires drop_m1=False")
            self.net = MarlNet().to(self.device)
        elif actor_type == "pool_mlp":
            if not self.drop_m1:
                raise ValueError("[marl] pool_mlp requires drop_m1=True")
            from marl.baseline_net import PoolMLPNet
            self.net = PoolMLPNet().to(self.device)
        else:
            raise ValueError("[marl] unknown actor_type %r" % actor_type)
        if ckpt is not None:
            self.net.load_state_dict(ckpt["state_dict"])
        if training:
            self.net.train()
        else:
            self.net.eval()
        self.params_count = assert_params(self.net)
        self._gen = torch.Generator()          # isolated sampling stream
        self._gen.manual_seed(int(seed))
        self.tau = 1.0                          # sampling temperature
        # per-step CPLEX reference (gap metric iii) - same mechanism as
        # GreedyPolicy; the reference solver reads the joint state but its
        # objective is only REPORTED, never fed back into decisions
        self._ref = None
        if with_reference:
            from dwta.dn_policies import CplexPolicy
            self._ref = CplexPolicy(solver, tmp_dir)
        # ---- mechanism instrumentation (spec §3.6, eval side) --------
        self.repeat_targeting_total = 0   # cumulative over the policy's life
        self.fwd_us_total = 0.0
        self.fwd_calls = 0
        self.reset_episode()

    # ------------------------------------------------------------------
    def reset_episode(self) -> None:
        self._mems = None
        self._last_t = -1
        self.last_step_collect = None
        self._ep_repeat_targeting = 0

    def _ensure_mems(self, m: int):
        if self._mems is None or len(self._mems) != m:
            self._mems = [AgentMemory() for _ in range(m)]

    # ------------------------------------------------------------------
    @torch.no_grad()
    def _forward_logits(self, feats):
        """One actor forward on self.device, CPU-fallback on any MPS
        error (returns logits on CPU)."""
        try:
            out = self.net(feats["x"].to(self.device),
                           feats["q"].to(self.device),
                           feats["g"].to(self.device))
            # MarlNet returns (logits, attn_w, m2_stats); PoolMLPNet
            # returns the bare logits tensor
            logits = out[0] if isinstance(out, tuple) else out
            return logits.cpu()
        except RuntimeError as e:                     # MPS op incompatibility
            if self.device.type != "mps":
                raise
            print("[marl] MPS forward failed (%s) - falling back to CPU"
                  % e)
            self.device = torch.device("cpu")
            self.net.to(self.device)
            out = self.net(feats["x"], feats["q"], feats["g"])
            logits = out[0] if isinstance(out, tuple) else out
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
            feats = build_inputs(obs_i, mem, dn, drop_m1=self.drop_m1)
            t0 = time.perf_counter()
            logits = self._forward_logits(feats)      # [1+L] hold first
            self.fwd_us_total += (time.perf_counter() - t0) * 1e6
            self.fwd_calls += 1
            L = len(feats["alive_ids"])
            if L == 0:
                actions[i] = None
                if collect is not None:
                    collect.append({"agent": i, "empty": True})
                continue
            # mask over obs targets -> align to the alive-only order of
            # alive_ids (feats["x"] rows were built from alive entries)
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
            else:
                probs = torch.exp(logp_all)
                # guard: all-zero (fully masked) -> hold
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

        # ---- mechanism counter: same-step repeated targeting ---------
        tgt_count = {}
        for j in actions.values():
            if j is not None:
                tgt_count[j] = tgt_count.get(j, 0) + 1
        rep = sum(1 for c in tgt_count.values() if c >= 2)
        self.repeat_targeting_total += rep
        self._ep_repeat_targeting += rep

        # private memory: register own shots AFTER deciding all agents
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
    ckpt_dir = os.path.join(here, "output", "e14_smoke")
    os.makedirs(ckpt_dir, exist_ok=True)
    ckpt_path = os.path.join(ckpt_dir, "init.pt")
    net = MarlNet()
    torch.manual_seed(0)
    for p in net.parameters():     # deterministic random init
        if p.dim() > 1:
            torch.nn.init.xavier_uniform_(p)
    torch.save({"state_dict": net.state_dict(),
                "feature_spec": {"x": 10, "q": 5, "g": 3,
                                 "drop_m1": False},
                "params_count": net.params_count(),
                "ablation": {"use_dcca": 1, "use_eaps": 1, "use_casp": 1},
                "reshaping": {"phi_scale": 1.0, "credit_alpha": 1.0,
                              "cf_beta": 1.0},
                "actor_type": "set_attention"}, ckpt_path)

    from dwta.dn_instance import DNInstance
    from dwta.dn_env import DNEnv
    dn = DNInstance(os.path.join(here, "data", "dn-data-v3",
                                 "dn_3x50_K10_s01.txt"))
    pol = MarlPolicy(ckpt_path, device="auto", greedy=True, seed=0)
    print("device:", pol.device, "| params:", pol.params_count)
    for seed in (42, 43, 44):
        env = DNEnv(dn, seed)
        pol.reset_episode()
        rec = env.run(pol)
        illegal = sum(s["illegal_actions"] for s in rec["steps"])
        wall = max(s["wall_time"] for s in rec["steps"]
                   if s["decision_step"])
        print("seed %d: leak=%.4f illegal=%d max_act_wall=%.4fs"
              " repeat_targeting(ep)=%d fwd_us/call=%.1f"
              % (seed, rec["leak_rate"], illegal, wall,
                 pol._ep_repeat_targeting,
                 pol.fwd_us_total / max(1, pol.fwd_calls)))
        assert illegal == 0, "illegal fire detected"
        assert wall < 1.0, "act wall >= 1s"
    print("marl/policy.py selftest: ALL PASS")


if __name__ == "__main__":
    _selftest()
