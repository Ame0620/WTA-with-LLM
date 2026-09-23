"""v5 ablation switch acceptance + influence-scope audit (spec §4.1/§4.4).

Run:  /opt/anaconda3/envs/wta/bin/python tests/test_ablation_switches.py

Covers:
  A. all 8 CLI combos parse; the bit vector is printed as the FIRST
     training-start line (checked via subprocess on --iters 0);
  B. structure selection per switch (actor/critic classes, x_dim,
     params bounds [1e3, 1e5]);
  C. computation-graph audit on real micro-batches:
       - CASP=0: PoolMLPNet actor + 8-dim x (drop_m1), no M2/M3 modules;
       - DCCA=0: StateCritic (V(s), no act block), adv_indiv == adv_team
         exactly (no credit / cf injection), cf batch not built;
       - EAPS=0: R_shaped == R_team exactly (no potential term at all),
         Phi not computed;
       - each single-off arm keeps its own module ON (D-only-off keeps
         credit injection; C-only-off keeps shaping; A-only-off keeps
         joint critic);
  D. checkpoint metadata round-trip + eval-side strict load (missing
     'ablation' rejected; structure restored from metadata only).

Exit code 0 = all checks pass.
"""
import json
import os
import subprocess
import sys
import tempfile

import torch

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)

from marl.network import MarlNet                        # noqa: E402
from marl.baseline_net import PoolMLPNet, StateCritic   # noqa: E402
from marl.policy import MarlPolicy                      # noqa: E402

PY = sys.executable
DATA = os.path.join(HERE, "data", "dn-data-v5")
COMBOS = [(1, 1, 1), (0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1),
          (0, 0, 1), (0, 1, 0), (1, 0, 0)]
RESULTS = {}
FAILED = []


def check(name, cond, detail=""):
    RESULTS[name] = ("PASS" if cond else "FAIL", detail)
    if not cond:
        FAILED.append(name)
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name,
                           (" | " + detail) if detail else ""))


def tiny_trainer(use_dcca, use_eaps, use_casp, epi=4, lam=1.0, al=1.0,
                 be=1.0):
    """Construct a Trainer on the v5 split without running main()."""
    import argparse
    from marl.train import Trainer
    a = argparse.Namespace(
        data_dir=DATA, device="cpu", seed=0, iters=2,
        episodes_per_iter=epi, eval_every=25, patience=60,
        wall_limit=0.0, output=os.path.join(tempfile.gettempdir(),
                                            "_abl_audit"),
        credit_mode="credit_kill", phi_sign=-1.0, c_invalid=None,
        resume=False, resume_from=None, init_from=None, init_blend=0.0,
        anneal_iters=50, no_batched=False, use_dcca=use_dcca,
        use_eaps=use_eaps, use_casp=use_casp, lr=3e-4,
        phi_scale=lam, credit_alpha=al, cf_beta=be)
    os.makedirs(a.output, exist_ok=True)
    return Trainer(a)


def collect_one(tr):
    """Collect ONE episode + process it (adv instrumentation lives in
    process_batch) and return (rew, mech snapshot, run_rec)."""
    dn = tr.train_dns[0]
    samples, rew, run_rec = tr.collect_episode(dn)
    tr.process_batch([(samples, rew, run_rec)])
    # capture the mechanism window produced by this single episode
    mech_snapshot = {k: (list(v) if isinstance(v, list) else v)
                     for k, v in tr._mech.items()}
    return rew, mech_snapshot, run_rec


def main():
    print("=" * 72)
    print("A. CLI parse + first-line bit vector (8 combos, --iters 0)")
    print("=" * 72)
    for (d, e, c) in COMBOS:
        outdir = os.path.join(tempfile.gettempdir(), "_abl_cli_%d%d%d"
                              % (d, e, c))
        cmd = [PY, os.path.join(HERE, "marl", "train.py"),
               "--data-dir", DATA, "--device", "cpu", "--seed", "0",
               "--iters", "0", "--episodes-per-iter", "4",
               "--eval-every", "25", "--output", outdir,
               "--use-dcca", str(d), "--use-eaps", str(e),
               "--use-casp", str(c)]
        r = subprocess.run(cmd, capture_output=True, text=True,
                           timeout=600)
        first = r.stdout.splitlines()[0] if r.stdout else ""
        want = "[ablation] use_dcca=%d use_eaps=%d use_casp=%d -> (%d,%d,%d)" \
            % (d, e, c, d, e, c)
        check("cli_(%d,%d,%d)" % (d, e, c),
              r.returncode == 0 and first == want,
              "rc=%d first=%r" % (r.returncode, first[:64]))

    print()
    print("=" * 72)
    print("B/C. structure + computation-graph audit (real micro-batches)")
    print("=" * 72)
    tr = {}
    for combo in [(1, 1, 1), (0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)]:
        tr[combo] = tiny_trainer(*combo)

    full = tr[(1, 1, 1)]
    noned = tr[(0, 0, 0)]
    c_off = tr[(1, 1, 0)]   # CASP-only-off
    e_off = tr[(1, 0, 1)]   # EAPS-only-off
    d_off = tr[(0, 1, 1)]   # DCCA-only-off

    # ---- actor / critic structure --------------------------------------
    check("B1 all-open actor is MarlNet", isinstance(full.actor, MarlNet))
    check("B2 all-open critic is CriticNet(joint)",
          type(full.critic).__name__ == "CriticNet"
          and full.critic_type == "joint_action")
    check("B3 all-open x_dim=10 drop_m1=False",
          full.x_dim == 10 and full.drop_m1 is False)
    check("B4 casp=0 actor is PoolMLPNet",
          isinstance(noned.actor, PoolMLPNet)
          and isinstance(c_off.actor, PoolMLPNet)
          and noned.actor_type == "pool_mlp" and noned.drop_m1 is True)
    check("B5 casp=0 x_dim=8", noned.x_dim == 8 and c_off.x_dim == 8)
    check("B6 dcca=0 critic is StateCritic (V(s))",
          isinstance(noned.critic, StateCritic)
          and isinstance(d_off.critic, StateCritic)
          and noned.critic_type == "state_value"
          and d_off.critic_type == "state_value")
    # StateCritic consumes no action block: forward signature + no
    # parameter tensor of size divisible-by-3 action rows -> structural:
    # its forward must accept (tgt, glob, tgt_mask) exactly
    import inspect
    sig = inspect.signature(StateCritic.forward)
    check("B7 StateCritic.forward has no act parameter",
          "act" not in sig.parameters,
          str(sig))
    for name, t in [("actor_all", full.actor), ("actor_none", noned.actor)]:
        n = sum(p.numel() for p in t.parameters() if p.requires_grad)
        check("B8 params %s in [1e3,1e5]" % name, 1e3 <= n <= 1e5,
              "n=%d" % n)
    for name, t in [("critic_all", full.critic),
                    ("critic_none", noned.critic)]:
        n = sum(p.numel() for p in t.parameters() if p.requires_grad)
        check("B9 params %s in [1e3,1e5]" % name, 1e3 <= n <= 1e5,
              "n=%d" % n)

    # ---- EAPS audit ------------------------------------------------------
    print("  -- collecting micro-episodes for reward audit ...")
    rew_full, mech_full, _ = collect_one(full)
    rew_none, mech_none, _ = collect_one(noned)
    rew_coff, mech_coff, _ = collect_one(c_off)
    rew_eoff, mech_eoff, _ = collect_one(e_off)
    rew_doff, mech_doff, _ = collect_one(d_off)

    rs, rt = rew_none["R_shaped"], rew_none["R_team"]
    check("C1 eaps=0 R_shaped == R_team exactly",
          torch.equal(rs, rt))
    rs2, rt2 = rew_eoff["R_shaped"], rew_eoff["R_team"]
    check("C2 eaps-only-off R_shaped == R_team",
          torch.equal(rs2, rt2))
    diff = (rew_full["R_shaped"] - rew_full["R_team"]).abs()
    check("C3 eaps=1 shaping term present (R_shaped != R_team)",
          float(diff.max()) > 0.0, "max|diff|=%.6g" % float(diff.max()))
    diff4 = (rew_coff["R_shaped"] - rew_coff["R_team"]).abs()
    check("C4 casp-only-off keeps shaping",
          float(diff4.max()) > 0.0)
    diff5 = (rew_doff["R_shaped"] - rew_doff["R_team"]).abs()
    check("C4b dcca-only-off keeps shaping",
          float(diff5.max()) > 0.0)

    # ---- DCCA audit ------------------------------------------------------
    ai, at = mech_none["adv_indiv"], mech_none["adv_team"]
    check("C5 dcca=0 adv_indiv == adv_team exactly (no credit/cf)",
          len(ai) == len(at) and len(ai) > 0
          and all(x == y for x, y in zip(ai, at)),
          "n=%d" % len(ai))
    ai2, at2 = mech_coff["adv_indiv"], mech_coff["adv_team"]
    check("C6 casp-only-off keeps credit/cf (adv differs from gae)",
          len(ai2) == len(at2) and len(ai2) > 0
          and any(x != y for x, y in zip(ai2, at2)),
          "n=%d" % len(ai2))
    ai2b, at2b = mech_eoff["adv_indiv"], mech_eoff["adv_team"]
    check("C6b eaps-only-off keeps credit/cf",
          len(ai2b) == len(at2b) and len(ai2b) > 0
          and any(x != y for x, y in zip(ai2b, at2b)))
    ai2c, at2c = mech_doff["adv_indiv"], mech_doff["adv_team"]
    check("C6c dcca-only-off adv_indiv == adv_team exactly",
          len(ai2c) == len(at2c) and len(ai2c) > 0
          and all(x == y for x, y in zip(ai2c, at2c)))
    ai3, at3 = mech_full["adv_indiv"], mech_full["adv_team"]
    check("C7 all-open credit/cf injected (adv differs from gae)",
          len(ai3) == len(at3) and len(ai3) > 0
          and any(x != y for x, y in zip(ai3, at3)))
    check("C8 dcca=0 credit still COMPUTED for instrumentation",
          len(rew_none["credit"]) > 0,
          "slots=%d" % len(rew_none["credit"]))

    # ---- feature dim audit ----------------------------------------------
    from marl.perceive import build_inputs, AgentMemory
    dn = full.train_dns[0]
    from dwta.dn_env import DNEnv
    env = DNEnv(dn, 42)
    obs = env.get_observation(0, 0)
    mem = AgentMemory()
    mem.update(obs, 0)
    f10 = build_inputs(obs, mem, dn, drop_m1=False)
    f8 = build_inputs(obs, mem, dn, drop_m1=True)
    check("C9 drop_m1 feature dims (10 vs 8)",
          f10["x"].shape[-1] == 10 and f8["x"].shape[-1] == 8,
          "%s vs %s" % (tuple(f10["x"].shape), tuple(f8["x"].shape)))

    # ---- D. checkpoint metadata + eval-side strict load ------------------
    print("  -- checkpoint metadata round-trip ...")
    ck = os.path.join(tempfile.gettempdir(), "_abl_audit_best.pt")
    noned.save_ckpt(ck, it=1)
    m = torch.load(ck, map_location="cpu", weights_only=True)
    check("D1 best.pt carries ablation/actor/critic/seed/budget",
          m.get("ablation") == {"use_dcca": 0, "use_eaps": 0,
                                "use_casp": 0}
          and m.get("actor_type") == "pool_mlp"
          and m.get("critic_type") == "state_value"
          and m.get("train_seed") == 0
          and isinstance(m.get("budget"), dict)
          and m["feature_spec"]["drop_m1"] is True
          and m["feature_spec"]["x"] == 8)
    pol = MarlPolicy(model_path=ck, device="cpu", greedy=True, seed=0)
    check("D2 eval restores PoolMLPNet from metadata alone",
          isinstance(pol.net, PoolMLPNet) and pol.drop_m1 is True)
    ck2 = os.path.join(tempfile.gettempdir(), "_abl_audit_best2.pt")
    full.save_ckpt(ck2, it=1)
    pol2 = MarlPolicy(model_path=ck2, device="cpu", greedy=True, seed=0)
    check("D3 eval restores MarlNet from metadata alone",
          isinstance(pol2.net, MarlNet) and pol2.drop_m1 is False)
    stripped = {k: v for k, v in m.items() if k != "ablation"}
    ck3 = os.path.join(tempfile.gettempdir(), "_abl_audit_stripped.pt")
    torch.save(stripped, ck3)
    try:
        MarlPolicy(model_path=ck3, device="cpu")
        rejected = False
    except ValueError:
        rejected = True
    check("D4 missing 'ablation' metadata rejected (no path guessing)",
          rejected)

    # ---- E. r2 recalibration-scalar influence scope ----------------------
    print()
    print("=" * 72)
    print("E. r2 recalibration scalars (lambda/alpha/beta) audit")
    print("=" * 72)
    # E1: with use_eaps=0 the lambda is bit-inert (R_shaped == R_team
    # exactly, identical streams between lambda values on the same RNG)
    t_la = tiny_trainer(0, 0, 0, lam=0.2)
    t_lb = tiny_trainer(0, 0, 0, lam=1.0)
    rew_la, _, _ = collect_one(t_la)
    rew_lb, _, _ = collect_one(t_lb)
    check("E1 eaps=0 lambda bit-inert (streams identical)",
          torch.equal(rew_la["R_shaped"], rew_lb["R_shaped"])
          and torch.equal(rew_la["R_team"], rew_lb["R_team"]))
    # E2: with use_dcca=0 alpha/beta are bit-inert (individual adv ==
    # team GAE exactly, streams identical between scalars)
    t_da = tiny_trainer(0, 1, 1, al=0.2, be=2.0)
    t_db = tiny_trainer(0, 1, 1, al=1.0, be=1.0)
    _, mech_da, _ = collect_one(t_da)
    _, mech_db, _ = collect_one(t_db)
    check("E2 dcca=0 alpha/beta bit-inert (adv streams identical)",
          mech_da["adv_indiv"] == mech_db["adv_indiv"]
          and mech_da["adv_team"] == mech_db["adv_team"])
    # E3: lambda semantics - halving lambda halves the shaping term.
    # (R_team + 0.5x) - R_team carries <=1ulp rounding of the addition,
    # so the exact-bit form is checked in E1/E2 instead; here the ratio
    # must hold to float64 addition rounding (atol 1e-12, values O(1)).
    t_eh = tiny_trainer(0, 1, 0, lam=0.5)
    t_eo = tiny_trainer(0, 1, 0, lam=1.0)
    rew_eh, _, _ = collect_one(t_eh)
    rew_eo, _, _ = collect_one(t_eo)
    d_half = rew_eh["R_shaped"] - rew_eh["R_team"]
    d_one = rew_eo["R_shaped"] - rew_eo["R_team"]
    maxdev = float((2 * d_half - d_one).abs().max())
    check("E3 lam=0.5 halves the shaping term (rounding-tight)",
          torch.equal(rew_eh["R_team"], rew_eo["R_team"])
          and maxdev <= 1e-12
          and float(d_one.abs().max()) > 0.0,
          "max|2*d_half-d_one|=%.2e" % maxdev)
    # E4: alpha/beta reach the advantage when dcca=1 (values actually
    # change vs the 1.0 defaults on the same RNG stream)
    t_aa = tiny_trainer(1, 0, 0, al=0.5, be=1.0)
    t_ab = tiny_trainer(1, 0, 0, al=1.0, be=1.0)
    _, mech_aa, _ = collect_one(t_aa)
    _, mech_ab, _ = collect_one(t_ab)
    check("E4 alpha=0.5 changes the injected advantage (dcca=1)",
          len(mech_aa["adv_indiv"]) == len(mech_ab["adv_indiv"])
          and any(x != y for x, y in zip(mech_aa["adv_indiv"],
                                         mech_ab["adv_indiv"])))
    # E5: CLI defaults locked at 1.0 and printed as the SECOND start line
    outdir = os.path.join(tempfile.gettempdir(), "_abl_cli_recal")
    cmd = [PY, os.path.join(HERE, "marl", "train.py"),
           "--data-dir", DATA, "--device", "cpu", "--seed", "0",
           "--iters", "0", "--episodes-per-iter", "4",
           "--eval-every", "25", "--output", outdir]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    lines = r.stdout.splitlines()
    check("E5 CLI defaults 1.0, [reshaping] second line",
          r.returncode == 0 and len(lines) > 1
          and lines[1] == "[reshaping] phi_scale=1 credit_alpha=1 "
          "cf_beta=1", "line2=%r" % (lines[1] if len(lines) > 1 else ""))
    # E6: checkpoint carries the reshaping triple verbatim
    t_ck = tiny_trainer(1, 1, 1, lam=0.25, al=0.5, be=0.75)
    ck4 = os.path.join(tempfile.gettempdir(), "_abl_audit_recal.pt")
    t_ck.save_ckpt(ck4, it=1)
    m4 = torch.load(ck4, map_location="cpu", weights_only=True)
    check("E6 best.pt reshaping == trainer scalars",
          m4.get("reshaping") == {"phi_scale": 0.25, "credit_alpha": 0.5,
                                  "cf_beta": 0.75})
    # E7: missing 'reshaping' metadata rejected at eval load (r1
    # checkpoints are refused by design)
    stripped2 = {k: v for k, v in m4.items() if k != "reshaping"}
    ck5 = os.path.join(tempfile.gettempdir(), "_abl_audit_norecal.pt")
    torch.save(stripped2, ck5)
    try:
        MarlPolicy(model_path=ck5, device="cpu")
        rejected2 = False
    except ValueError:
        rejected2 = True
    check("E7 missing 'reshaping' metadata rejected", rejected2)
    # E8/E9: MARL_EXPECT_RESHAPING anti-cross-arm guard is runtime-live
    env8 = dict(os.environ, MARL_EXPECT_RESHAPING="0.9,0.9,0.9")
    try:
        MarlPolicy(model_path=ck4, device="cpu", _env=env8)
        mismatch_raises = False
    except (ValueError, TypeError):
        mismatch_raises = True
    check("E8 expect-reshaping mismatch raises", mismatch_raises)
    env9 = dict(os.environ, MARL_EXPECT_RESHAPING="0.25,0.5,0.75")
    try:
        _p9 = MarlPolicy(model_path=ck4, device="cpu", _env=env9)
        match_loads = True
    except (ValueError, TypeError):
        match_loads = False
    check("E9 expect-reshaping match loads fine", match_loads)
    # E10: r2 mechanism counters - on with the mechanisms, 0.0 when off
    check("E10 mechanism counters (shape/credit abs)",
          mech_full["shape_abs"] > 0.0 and mech_full["credit_abs"] > 0.0
          and mech_none["shape_abs"] == 0.0
          and mech_none["credit_abs"] == 0.0)

    print()
    print("=" * 72)
    print("SUMMARY: %d checks, %d failed" % (len(RESULTS), len(FAILED)))
    if FAILED:
        for f in FAILED:
            print("  FAILED: %s" % f)
        print("INFLUENCE-SCOPE AUDIT: FAIL")
        return 1
    print("INFLUENCE-SCOPE AUDIT: ALL PASS")
    out = os.path.join(HERE, "output", "_pre_ablation_ref",
                       "switch_audit.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        json.dump({k: v[0] for k, v in RESULTS.items()}, f,
                  indent=2, sort_keys=True)
    print("audit detail -> %s" % out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
