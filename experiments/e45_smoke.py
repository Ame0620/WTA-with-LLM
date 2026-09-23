"""v5 ablation smoke protocol (spec §4.5).

Run:  /opt/anaconda3/envs/wta/bin/python experiments/e45_smoke.py

Per combo (all 8 arms):
  1. tiny training: --iters 3 --episodes-per-iter 8 --eval-every 3
     (first stdout line must be the [ablation] bit vector; exit 0);
  2. greedy evaluation of the arm's best.pt over 3 TRAIN instances
     (s03-s05; R5 forbids touching the test split here) x seeds 42-46,
     checks per run:
        - zero illegal actions,
        - all headline metrics finite (no NaN/inf),
        - shots_total <= 70,
        - ammo_end >= 0;
  3. train_log.jsonl rows contain no NaN.

Writes output/e45_ablation_smoke/smoke_report.json; exit 0 iff all pass.
"""
import json
import math
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)

PY = sys.executable
DATA = os.path.join(HERE, "data", "dn-data-v5")
MANIFEST = os.path.join(DATA, "MANIFEST.md")
OUTROOT = os.path.join(HERE, "output", "e45_ablation_smoke")
COMBOS = [(1, 1, 1), (0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1),
          (0, 0, 1), (0, 1, 0), (1, 0, 0)]
SEEDS = [42, 43, 44, 45, 46]


def main():
    os.makedirs(OUTROOT, exist_ok=True)
    from experiments.dn_family_eval import read_split
    from dwta.dn_instance import DNInstance
    from dwta.dn_env import DNEnv
    from marl.policy import MarlPolicy

    instances = read_split(MANIFEST, "train")[:3]  # R5: no test
    print("smoke instances (train): %s" % ", ".join(instances))
    report = {"instances": instances, "seeds": SEEDS, "arms": {}}
    ok_all = True
    for (d, e, c) in COMBOS:
        tag = "c%d%d%d" % (d, e, c)
        outdir = os.path.join(OUTROOT, tag)
        os.makedirs(outdir, exist_ok=True)
        print("=== arm (%d,%d,%d) -> %s ===" % (d, e, c, outdir))

        # ---- 1. tiny training ------------------------------------------
        cmd = [PY, os.path.join(HERE, "marl", "train.py"),
               "--data-dir", DATA, "--device", "mps", "--seed", "0",
               "--iters", "3", "--episodes-per-iter", "8",
               "--eval-every", "3", "--output", outdir,
               "--use-dcca", str(d), "--use-eaps", str(e),
               "--use-casp", str(c)]
        r = subprocess.run(cmd, capture_output=True, text=True,
                           timeout=1800)
        first = r.stdout.splitlines()[0] if r.stdout else ""
        want = "[ablation] use_dcca=%d use_eaps=%d use_casp=%d -> (%d,%d,%d)" \
            % (d, e, c, d, e, c)
        train_ok = (r.returncode == 0 and first == want)
        arm = {"train_rc": r.returncode, "first_line_ok": first == want}

        # train_log NaN scan
        log_nan = False
        log_path = os.path.join(outdir, "train_log.jsonl")
        n_rows = 0
        if os.path.exists(log_path):
            with open(log_path) as f:
                for line in f:
                    n_rows += 1
                    row = json.loads(line)
                    for v in row.values():
                        if isinstance(v, float) and not math.isfinite(v):
                            log_nan = True
        arm["train_log_rows"] = n_rows
        arm["train_log_nan"] = log_nan

        # ---- 2. greedy eval over 3 test instances x 5 seeds ------------
        checks = {"illegal": 0, "nan_runs": 0, "shots_over_70": 0,
                  "ammo_negative": 0}
        best = os.path.join(outdir, "best.pt")
        eval_ok = os.path.exists(best)
        mech = {"rep": 0, "lat_us": []}
        if eval_ok:
            pol = MarlPolicy(model_path=best, device="mps",
                             greedy=True, seed=0)
            meta = torch_load_meta(best)
            arm["ckpt_ablation"] = meta.get("ablation")
            arm["ckpt_actor_type"] = meta.get("actor_type")
            runs_n = 0
            for name in instances:
                dn = DNInstance(os.path.join(DATA, name))
                for sd in SEEDS:
                    prev_rep = pol.repeat_targeting_total
                    prev_us, prev_calls = pol.fwd_us_total, pol.fwd_calls
                    rec = DNEnv(dn, sd).run(pol)
                    runs_n += 1
                    checks["illegal"] += sum(
                        s["illegal_actions"] for s in rec["steps"])
                    vals = [rec["leak_rate"], rec["destroyed_value"],
                            rec["shots_total"], rec["ammo_end"]]
                    if any(not math.isfinite(v) for v in vals):
                        checks["nan_runs"] += 1
                    if rec["shots_total"] > 70:
                        checks["shots_over_70"] += 1
                    if rec["ammo_end"] < 0:
                        checks["ammo_negative"] += 1
                    dc = pol.fwd_calls - prev_calls
                    if dc > 0:
                        mech["lat_us"].append(
                            (pol.fwd_us_total - prev_us) / dc)
                    mech["rep"] += pol.repeat_targeting_total - prev_rep
                pol.reset_episode()
            arm["runs"] = runs_n
            arm["repeat_targeting_total"] = mech["rep"]
            arm["policy_latency_us_mean"] = (
                sum(mech["lat_us"]) / len(mech["lat_us"])
                if mech["lat_us"] else None)

        arm["checks"] = checks
        arm["pass"] = bool(
            train_ok and not log_nan and eval_ok
            and checks["illegal"] == 0 and checks["nan_runs"] == 0
            and checks["shots_over_70"] == 0
            and checks["ammo_negative"] == 0)
        ok_all &= arm["pass"]
        print("  train_ok=%s eval_ok=%s checks=%s -> %s"
              % (train_ok, eval_ok, checks,
                 "PASS" if arm["pass"] else "FAIL"))
        report["arms"][tag] = arm

    report["all_pass"] = bool(ok_all)
    with open(os.path.join(OUTROOT, "smoke_report.json"), "w") as f:
        json.dump(report, f, indent=2)
    print("SMOKE: %s" % ("ALL PASS" if ok_all else "FAIL"))
    return 0 if ok_all else 1


def torch_load_meta(path):
    import torch
    ck = torch.load(path, map_location="cpu", weights_only=True)
    return ck


if __name__ == "__main__":
    sys.exit(main())
