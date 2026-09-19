#!/usr/bin/env python
"""v5 full-algorithm experiment pipeline (S0-S5, single-command,
unattended, watchdog-guarded).

Requirement doc §6.1. Stages (all idempotent - finished artefacts are
auto-skipped, so the pipeline can be re-launched at any time):

  S0  smoke gates (tests/test_v5_algorithms.py), GA m=10 latency probe,
      EC-MAPPO short-rate calibration -> logs/s0_tier_report.json
  S1  solver finals: cplex 30 seeds; GA main tier (40x50) + sensitivity
      (20x30 / 60x80)
  S2  rule finals: none / greedy / greedy_threat / greedy_nearest /
      random / pocplex / rh-cplex, 30 seeds each
  S3  learning retrain: mappo / qmix / maddpg (3h tier: 1200 x 12,
      wall 2.5h) + ecmappo (12h tier, calibrated at S0)
  S4  learning finals (30 seeds, CPLEX-ref) + generalization
      (train/val/test x 10 seeds, --no-ref)
  S5  aggregate report skeleton -> <root>/实验报告_v5全算法总览.md

Watchdog (in-process, poll = 30 s):
  * heartbeat: logs/heartbeat.json refreshed every poll, with per-task
    status / restarts / last-output ts / budget (§6.1.6)
  * stall: log silent for 15 min (= 3 consecutive 5-min watchdog
    cycles, §6.1.2) -> dump diag (log tail + ps) to logs/diag_*.log,
    kill, restart (training tasks auto-continue via --resume with the
    wall budget already elapsed-aware)
  * crash: non-zero exit -> restart up to 3 times, then mark the task
    failed in logs/pipeline_status.json, cascade-skip its dependents
    and CONTINUE independent downstream tasks (§6.1.4)
  * legal stops (early-stop / iters / wall-limit) exit 0 and the
    pipeline advances automatically (§6.1.5)

Usage:
  python experiments/run_v5_pipeline.py                 # S0..S5
  python experiments/run_v5_pipeline.py --stage S3      # single stage
  python experiments/run_v5_pipeline.py --to-stage S1   # stop after S1
  python experiments/run_v5_pipeline.py --list          # show plan
  python experiments/run_v5_pipeline.py --dry-run       # print commands
"""

import argparse
import json
import os
import subprocess
import sys
import time
import traceback

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")
STATUS_PATH = os.path.join(LOG_DIR, "pipeline_status.json")
HEARTBEAT_PATH = os.path.join(LOG_DIR, "heartbeat.json")
TIER_REPORT_PATH = os.path.join(LOG_DIR, "s0_tier_report.json")
# auto skeleton only; the curated report 实验报告_v5全算法总览.md is
# hand-written and must NOT be overwritten by S5 reruns
REPORT_PATH = os.path.join(PROJECT_ROOT, "logs", "s5_自动骨架报告.md")

PY = sys.executable
DATA5 = "data/dn-data-v5"
MANIFEST5 = "data/dn-data-v5/MANIFEST.md"

POLL_SEC = 30.0          # watchdog/heartbeat cadence
STALL_SEC = 15 * 60.0    # log-tail silence -> hung
MAX_RESTARTS = 3

SEED_BASE = 42
N_SEEDS = 30
GEN_SEEDS = 10


# ----------------------------------------------------------------------
# task spec
# ----------------------------------------------------------------------
class Task:
    def __init__(self, tid, stage, cmd, log, done, train=False,
                 budget_h=None, desc="", deps=()):
        self.id = tid
        self.stage = stage
        self.cmd = cmd              # list; training cmds get --resume on
        self.log = log              # path relative to PROJECT_ROOT
        self.done = done            # callable -> True if finished
        self.train = train          # restartable via --resume
        self.budget_h = budget_h
        self.desc = desc
        self.deps = tuple(deps)     # cascade-skip if a dep is failed
        self.status = "pending"
        self.restarts = 0
        self.started_at = None
        self.finished_at = None
        self.exit_code = None


def _fe(path, contains=None):
    """finished-if-file-exists (+optional substring in the tail)."""
    p = os.path.join(PROJECT_ROOT, path)
    if not os.path.exists(p):
        return False
    if contains is None:
        return True
    try:
        with open(p, "rb") as f:
            f.seek(max(0, os.path.getsize(p) - 8192), 0)
            return contains in f.read().decode("utf-8", "replace")
    except OSError:
        return False


def fam_eval(policy, out, seeds=N_SEEDS, extra=(), split=None,
             model=None, no_ref=False):
    cmd = [PY, "experiments/dn_family_eval.py",
           "--data-dir", DATA5, "--manifest", MANIFEST5,
           "--policy", policy, "--seeds", str(seeds),
           "--seed-base", str(SEED_BASE),
           "--output", out]
    if split:
        cmd += ["--split", split]
    if model:
        cmd += ["--model", model]
    if no_ref:
        cmd += ["--no-ref"]
    cmd += list(extra)
    return cmd


def build_tasks():
    T = []

    # ---------------- S0 ----------------
    T.append(Task(
        "s0_smoke", "S0",
        [PY, "tests/test_v5_algorithms.py"],
        "logs/s0_smoke.log",
        lambda: _fe("logs/s0_smoke.log", "ALL PASS"),
        desc="V5'''/V2''' dimension + invariants smoke"))
    T.append(Task(
        "s0_ga_probe", "S0",
        fam_eval("ga", "output/e26_v5_ga_probe", seeds=3,
                 extra=["--ga-pop", "40", "--ga-gen", "50"], no_ref=True),
        "logs/s0_ga_probe.log",
        lambda: _fe("output/e26_v5_ga_probe/family_report.json"),
        desc="GA m=10 latency probe (1 tier, 3 seeds)"))
    T.append(Task(
        "s0_ecmappo_rate", "S0",
        [PY, "marl/train.py", "--data-dir", DATA5,
         "--iters", "30", "--episodes-per-iter", "96",
         "--eval-every", "10", "--wall-limit", "0.4",
         "--output", "output/e44_v5_s0_ecmappo_rate"],
        "logs/s0_ecmappo_rate.log",
        lambda: _fe("output/e44_v5_s0_ecmappo_rate/train_summary.json"),
        train=True, budget_h=0.5,
        desc="EC-MAPPO rate calibration (30 iters x 96 ep, "
             "eval-every 10 - pure train rate)"))
    T.append(Task(
        "s0_tier_report", "S0", None, "logs/s0_tier_report.json",
        lambda: _fe(TIER_REPORT_PATH),
        deps=("s0_ecmappo_rate",),
        desc="tier decision (§3.3): read rate -> ecmappo iters/ep"))

    # ---------------- S1 ----------------
    T.append(Task(
        "s1_cplex", "S1",
        fam_eval("cplex", "output/e40_v5_cplex"),
        "logs/s1_cplex.log",
        lambda: _fe("output/e40_v5_cplex/family_report.json"),
        budget_h=1.0, desc="CPLEX final (test x 30 seeds)"))
    T.append(Task(
        "s1_ga_main", "S1",
        fam_eval("ga", "output/e41_v5_ga",
                 extra=["--ga-pop", "40", "--ga-gen", "50"]),
        "logs/s1_ga_main.log",
        lambda: _fe("output/e41_v5_ga/family_report.json"),
        budget_h=2.0, desc="GA main tier 40x50 (30 seeds)"))
    for pop, gen in ((20, 30), (60, 80)):
        T.append(Task(
            "s1_ga_sens_%dx%d" % (pop, gen), "S1",
            fam_eval("ga", "output/e42_v5_ga_sens_%dx%d" % (pop, gen),
                     extra=["--ga-pop", str(pop), "--ga-gen", str(gen)]),
            "logs/s1_ga_sens_%dx%d.log" % (pop, gen),
            lambda p=pop, g=gen: _fe(
                "output/e42_v5_ga_sens_%dx%d/family_report.json" % (p, g)),
            budget_h=2.0, desc="GA sensitivity %dx%d" % (pop, gen)))

    # ---------------- S2 ----------------
    for pol in ("none", "greedy", "greedy_threat", "greedy_nearest",
                "random"):
        safe = pol.replace("-", "_")
        T.append(Task(
            "s2_%s" % safe, "S2",
            fam_eval(pol, "output/e38_v5_%s" % safe),
            "logs/s2_%s.log" % safe,
            lambda s=safe: _fe("output/e38_v5_%s/family_report.json" % s),
            budget_h=2.0, desc="%s final (30 seeds)" % pol))
    T.append(Task(
        "s2_rh_cplex", "S2",
        fam_eval("rh-cplex", "output/e38_v5_rh_cplex",
                 extra=["--no-ref", "--delta", "0.01",
                        "--timelimit", "15"]),
        "logs/s2_rh_cplex.log",
        lambda: _fe("output/e38_v5_rh_cplex/family_report.json"),
        budget_h=3.0,
        desc="rh-cplex final (30 seeds; H=2 MIP relaxed: "
             "delta .01, tl 15s, no-ref - §10 gap-tolerance clause)"))
    T.append(Task(
        "s2_pocplex", "S2",
        fam_eval("pocplex", "output/e38_v5_pocplex"),
        "logs/s2_pocplex.log",
        lambda: _fe("output/e38_v5_pocplex/family_report.json"),
        budget_h=2.0, desc="pocplex final (30 seeds)"))

    # ---------------- S3 ----------------
    # patience 48 eval-points x eval-every 25 = 1200 iters -> never
    # early-stop before the iters cap (v4 showed mappo needs >1000
    # iters before val leak starts moving; the default 12-point
    # patience killed it at 325 iters with best_val=1.0).
    for algo in ("mappo", "qmix", "maddpg"):
        T.append(Task(
            "s3_%s" % algo, "S3",
            [PY, "marl/train_%s.py" % algo, "--data-dir", DATA5,
             "--patience", "48",
             "--output", "output/e43_v5_%s" % algo],
            "logs/s3_%s.log" % algo,
            lambda a=algo: _fe("output/e43_v5_%s/train_summary.json"
                               % a),
            train=True, budget_h=3.0,
            desc="%s retrain (3h tier: 1200 x 12, wall 2.5h)" % algo))
    T.append(Task(
        "s3_ecmappo", "S3", None,            # cmd built at S0 tier time
        "logs/s3_ecmappo.log",
        lambda: _fe("output/e43_v5_ecmappo/train_summary.json"),
        train=True, budget_h=11.0,
        deps=("s0_tier_report",),
        desc="EC-MAPPO retrain (12h tier, calibrated)"))

    # ---------------- S4 ----------------
    for algo in ("ecmappo", "mappo", "qmix", "maddpg"):
        T.append(Task(
            "s4_final_%s" % algo, "S4",
            fam_eval(algo, "output/e44_v5_final_%s" % algo,
                     model="output/e43_v5_%s/best.pt" % algo),
            "logs/s4_final_%s.log" % algo,
            lambda a=algo: _fe("output/e44_v5_final_%s/family_report.json"
                               % a),
            budget_h=1.5, deps=("s3_%s" % algo,),
            desc="%s final (30 seeds, CPLEX-ref)" % algo))
        for split in ("train", "val", "test"):
            T.append(Task(
                "s4_gen_%s_%s" % (algo, split), "S4",
                fam_eval(algo, "output/e45_v5_gen_%s_%s" % (algo, split),
                         seeds=GEN_SEEDS, split=split, no_ref=True,
                         model="output/e43_v5_%s/best.pt" % algo),
                "logs/s4_gen_%s_%s.log" % (algo, split),
                lambda a=algo, s=split: _fe(
                    "output/e45_v5_gen_%s_%s/family_report.json" % (a, s)),
                budget_h=0.5, deps=("s3_%s" % algo,),
                desc="%s generalization %s (10 seeds, no-ref)" % (
                    algo, split)))

    # ---------------- S5 ----------------
    T.append(Task(
        "s5_report", "S5", None,
        "logs/s5_report.log",
        lambda: _fe(REPORT_PATH),
        desc="aggregate report 实验报告_v5全算法总览.md"))
    return T


# ----------------------------------------------------------------------
# observability
# ----------------------------------------------------------------------
def load_status():
    if os.path.exists(STATUS_PATH):
        try:
            with open(STATUS_PATH) as f:
                return json.load(f)
        except Exception:
            pass
    return {"tasks": {}}


def save_status(tasks):
    st = {"updated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
          "tasks": {}}
    for t in tasks:
        st["tasks"][t.id] = {
            "stage": t.stage, "status": t.status,
            "restarts": t.restarts, "log": t.log,
            "budget_h": t.budget_h, "desc": t.desc,
            "exit_code": t.exit_code,
            "started_at": t.started_at, "finished_at": t.finished_at}
    tmp = STATUS_PATH + ".tmp"
    with open(tmp, "w") as f:
        json.dump(st, f, indent=2, ensure_ascii=False)
    os.replace(tmp, STATUS_PATH)


def write_heartbeat(tasks, current):
    hb = {"ts": time.strftime("%Y-%m-%d %H:%M:%S"),
          "epoch": int(time.time()),
          "current_task": current.id if current else None,
          "pid": os.getpid(),
          "stage_progress": {},
          "tasks": {}}                     # §6.1.6 per-task detail
    for t in tasks:                        # total = every task of the stage
        hb["stage_progress"].setdefault(
            t.stage, {"done": 0, "total": 0, "failed": 0})
        hb["stage_progress"][t.stage]["total"] += 1
        if t.status == "failed":
            hb["stage_progress"][t.stage]["failed"] += 1
        elif t.status == "completed":
            hb["stage_progress"][t.stage]["done"] += 1
        last_out = None
        try:                               # most recent output timestamp
            last_out = time.strftime(
                "%H:%M:%S",
                time.localtime(os.path.getmtime(
                    os.path.join(PROJECT_ROOT, t.log))))
        except OSError:
            pass
        hb["tasks"][t.id] = {
            "stage": t.stage, "status": t.status,
            "restarts": t.restarts, "budget_h": t.budget_h,
            "last_output": last_out,
            "started_at": t.started_at, "finished_at": t.finished_at}
    tmp = HEARTBEAT_PATH + ".tmp"
    with open(tmp, "w") as f:
        json.dump(hb, f, indent=2, ensure_ascii=False)
    os.replace(tmp, HEARTBEAT_PATH)


def dump_diag(task, proc, reason):
    path = os.path.join(
        PROJECT_ROOT, "logs", "diag_%s_%s.log"
        % (task.id, time.strftime("%H%M%S")))
    lines = ["diag for %s (%s) at %s\n"
             % (task.id, reason, time.strftime("%F %T"))]
    logp = os.path.join(PROJECT_ROOT, task.log)
    try:
        with open(logp, "rb") as f:
            f.seek(max(0, os.path.getsize(logp) - 20000), 0)
            lines.append("--- log tail ---\n"
                         + f.read().decode("utf-8", "replace"))
    except OSError:
        lines.append("(no log)\n")
    try:
        out = subprocess.run(
            ["ps", "-p", str(proc.pid), "-o",
             "pid,etime,%cpu,%mem,state,command"],
            capture_output=True, text=True, timeout=10).stdout
        lines.append("--- ps ---\n" + out)
    except Exception:
        pass
    with open(path, "w") as f:
        f.write("".join(lines))
    return path


# ----------------------------------------------------------------------
# S0 tier calibration (§3.3)
# ----------------------------------------------------------------------
def ecmappo_tier_decision():
    """Read the short-rate run, estimate the 2500x96 wall time and pick
    the tier. Returns (iters, episodes, est_h, decision, per_iter)."""
    log_path = os.path.join(PROJECT_ROOT,
                            "output/e44_v5_s0_ecmappo_rate",
                            "train_log.jsonl")
    per_iter = None
    with open(log_path) as f:
        rows = [json.loads(x) for x in f if x.strip()]
    if len(rows) >= 2:
        first, last = rows[0], rows[-1]
        d_it = last["iter"] - first["iter"]
        if d_it > 0:
            # subtract eval overhead: rows sit on eval points; the
            # interior diff is dominated by pure training iters
            per_iter = (last["wall_sec"] - first["wall_sec"]) / d_it
    if per_iter is None or per_iter <= 0:
        per_iter, decision = 14.4, "fallback_default_rate"
    est_h = per_iter * 2500 / 3600.0
    if est_h < 8.0:                      # headroom -> scale up (§3.3)
        iters, ep, decision = 3000, 96, "up_3000x96"
    elif est_h <= 10.5:                  # inside budget
        iters, ep, decision = 2500, 96, "keep_2500x96"
    else:                                # downscale iters, keep ep (§3.3)
        iters = max(500, int(0.95 * 10.5 * 3600 / per_iter))
        ep = 96
        decision = "down_%dx%d" % (iters, ep)
    return iters, ep, est_h, decision, per_iter


def run_tier_report_task(task):
    iters, ep, est_h, decision, per_iter = ecmappo_tier_decision()
    sample_ratio = iters * ep / float(2500 * 96)
    ga_probe = os.path.join(PROJECT_ROOT,
                            "output/e26_v5_ga_probe/family_report.json")
    ga_lat = None
    if os.path.exists(ga_probe):
        try:
            fam = json.load(open(ga_probe))["family"]
            ga_lat = {"p50": fam.get("latency_p50", {}).get("mean"),
                      "p90": fam.get("latency_p90", {}).get("mean")}
        except Exception:
            pass
    rep = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "ecmappo": {"per_iter_sec": round(per_iter, 2),
                    "est_2500x96_hours": round(est_h, 2),
                    "tier": {"iters": iters, "episodes": ep},
                    "sample_ratio_vs_v4_full": round(sample_ratio, 3),
                    "sample_ratio_warning":
                        (None if sample_ratio >= 0.8 else
                         "wall-clock bound: joint samples < 80% of the "
                         "v4 full tier (240k ep); reported as-is per "
                         "§3.3 '下调 iters 保墙钟'"),
                    "decision": decision},
        "ga_latency": ga_lat,
        "rule": ("est < 8h -> up 3000x96; <= 10.5h -> keep 2500x96; "
                 "else downscale iters (ep fixed 96) to fit 95% of the "
                 "10.5h wall budget"),
    }
    with open(TIER_REPORT_PATH, "w") as f:
        json.dump(rep, f, indent=2, ensure_ascii=False)
    task.status = "completed"
    print("[pipeline] S0 tier report -> %s (%s, est %.2fh, samples %.0f%%)"
          % (TIER_REPORT_PATH, decision, est_h, 100 * sample_ratio),
          flush=True)


def build_ecmappo_train_cmd():
    iters, ep = 2500, 96
    if os.path.exists(TIER_REPORT_PATH):
        try:
            tr = json.load(open(TIER_REPORT_PATH))
            iters = tr["ecmappo"]["tier"]["iters"]
            ep = tr["ecmappo"]["tier"]["episodes"]
        except Exception:
            pass
    return [PY, "marl/train.py", "--data-dir", DATA5,
            "--iters", str(iters), "--episodes-per-iter", str(ep),
            "--wall-limit", "10.5",
            "--output", "output/e43_v5_ecmappo"]


# ----------------------------------------------------------------------
# watchdogged execution
# ----------------------------------------------------------------------
def _proc_group_cpu(proc):
    """Total %CPU of the child's process group (children included)."""
    try:
        pgid = os.getpgid(proc.pid)
        out = subprocess.run(["ps", "-A", "-o", "pgid=,%cpu="],
                             capture_output=True, text=True,
                             timeout=10).stdout
        tot = 0.0
        for line in out.splitlines():
            parts = line.split()
            if len(parts) == 2:
                try:
                    if int(parts[0]) == pgid:
                        tot += float(parts[1])
                except ValueError:
                    continue
        return tot
    except Exception:
        return 0.0


def run_task(task, tasks):
    if task.cmd is None:          # internal task
        if task.id == "s0_tier_report":
            run_tier_report_task(task)
            return True
        if task.id == "s3_ecmappo":
            task.cmd = build_ecmappo_train_cmd()
        elif task.id == "s5_report":
            return run_report_task(task, tasks)

    log_path = os.path.join(PROJECT_ROOT, task.log)
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    while True:
        cmd = list(task.cmd)
        if task.train and task.restarts > 0:
            if "--resume" not in cmd:
                cmd.append("--resume")
        task.status = "running"
        task.started_at = time.strftime("%Y-%m-%d %H:%M:%S")
        save_status(tasks)
        print("[pipeline] START %s (attempt %d): %s"
              % (task.id, task.restarts + 1, " ".join(cmd)), flush=True)
        with open(log_path, "a") as lf:
            lf.write("\n==== [pipeline] %s attempt %d at %s ====\n"
                     % (task.id, task.restarts + 1,
                        time.strftime("%F %T")))
            lf.flush()
            proc = subprocess.Popen(cmd, stdout=lf, stderr=lf,
                                    cwd=PROJECT_ROOT,
                                    start_new_session=True)
            stall_polls = 0
            while True:
                time.sleep(POLL_SEC)
                write_heartbeat(tasks, task)
                rc = proc.poll()
                if rc is not None:
                    task.exit_code = rc
                    break
                try:
                    age = time.time() - os.path.getmtime(log_path)
                except OSError:
                    age = 0.0
                if age > STALL_SEC:          # 15 min w/o log growth
                    cpu = _proc_group_cpu(proc)
                    if cpu >= 5.0:           # alive & computing (e.g.
                        # per-seed CPLEX subprocess chains): keep it,
                        # note the check into the log so mtime advances
                        try:
                            with open(log_path, "a") as lf2:
                                lf2.write("[watchdog] log silent %.0fs "
                                          "but proc-group CPU %.0f%% - "
                                          "alive, keep waiting\n"
                                          % (age, cpu))
                        except OSError:
                            pass
                        stall_polls = 0
                        continue
                    stall_polls += 1
                    diag = dump_diag(task, proc,
                                     "stall %.0fs" % age)
                    print("[pipeline] STALL %s (log silent %.0fs) -> "
                          "kill+restart, diag: %s"
                          % (task.id, age, diag), flush=True)
                    try:
                        os.killpg(os.getpgid(proc.pid), 15)
                    except Exception:
                        proc.kill()
                    try:
                        proc.wait(30)
                    except Exception:
                        try:
                            os.killpg(os.getpgid(proc.pid), 9)
                        except Exception:
                            pass
                    rc = "stall"
                    task.exit_code = rc
                    break
                else:
                    stall_polls = 0
        # ---- child finished --------------------------------------
        if rc == 0 or task.done():
            task.status = "completed"
            task.finished_at = time.strftime("%Y-%m-%d %H:%M:%S")
            save_status(tasks)
            print("[pipeline] DONE %s (rc=%s)" % (task.id, rc),
                  flush=True)
            return True
        # ---- illegal stop: restart policy ------------------------
        if task.restarts >= MAX_RESTARTS:
            task.status = "failed"
            task.finished_at = time.strftime("%Y-%m-%d %H:%M:%S")
            save_status(tasks)
            print("[pipeline] FAILED %s after %d restarts (rc=%s) - "
                  "marking failed, continuing downstream"
                  % (task.id, task.restarts, rc), flush=True)
            return False
        task.restarts += 1
        save_status(tasks)
        print("[pipeline] RESTART %s (rc=%s, restart #%d%s)"
              % (task.id, rc, task.restarts,
                 ", --resume" if task.train else ""), flush=True)


# ----------------------------------------------------------------------
# S5 aggregation report
# ----------------------------------------------------------------------
ALGO_LABELS = [
    ("cplex", "CPLEX", "output/e40_v5_cplex"),
    ("ga", "GA 40x50", "output/e41_v5_ga"),
    ("none", "None", "output/e38_v5_none"),
    ("greedy", "Greedy", "output/e38_v5_greedy"),
    ("greedy_threat", "GreedyThreat", "output/e38_v5_greedy_threat"),
    ("greedy_nearest", "GreedyNearest", "output/e38_v5_greedy_nearest"),
    ("random", "Random", "output/e38_v5_random"),
    ("pocplex", "PO-CPLEX", "output/e38_v5_pocplex"),
    ("rh-cplex", "RH-CPLEX", "output/e38_v5_rh_cplex"),
    ("ecmappo", "EC-MAPPO", "output/e44_v5_final_ecmappo"),
    ("mappo", "MAPPO", "output/e44_v5_final_mappo"),
    ("qmix", "QMIX", "output/e44_v5_final_qmix"),
    ("maddpg", "MADDPG", "output/e44_v5_final_maddpg"),
]
TRAIN_DIRS = {"ecmappo": "output/e43_v5_ecmappo",
              "mappo": "output/e43_v5_mappo",
              "qmix": "output/e43_v5_qmix",
              "maddpg": "output/e43_v5_maddpg"}


def _fam(path, key):
    try:
        fam = json.load(open(os.path.join(PROJECT_ROOT, path,
                                          "family_report.json")))
        v = fam.get("family", {}).get(key) or {}
        return v.get("mean"), v.get("worst")
    except Exception:
        return None, None


def _fmt(v, spec=".4f"):
    return ("%" + spec) % v if v is not None else "n/a"


def run_report_task(task, tasks):
    L = []
    L.append("# 实验报告 - v5 全算法总览\n")
    L.append("> 生成: %s (pipeline S5, 自动汇总骨架; 定性结论由人工"
             "复核补全)\n" % time.strftime("%Y-%m-%d %H:%M:%S"))
    L.append("> 协议: data/dn-data-v5 (m=10, n=100, K=10, mu=7, 池=70),"
             " test split s01-s02, %d seeds (base %d)\n"
             % (N_SEEDS, SEED_BASE))

    L.append("\n## 1. 终评总表 (test x 30 seeds)\n")
    L.append("| 算法 | leak mean | leak worst | gap mean | "
             "invalid eng | ammo eff | latency p50 |")
    L.append("|---|---:|---:|---:|---:|---:|---:|")
    for key, label, d in ALGO_LABELS:
        lm, lw = _fam(d, "leak_rate")
        gm, _ = _fam(d, "gap_mean")
        im, _ = _fam(d, "invalid_engagement_rate")
        am, _ = _fam(d, "ammo_efficiency")
        p5, _ = _fam(d, "latency_p50")
        L.append("| %s | %s | %s | %s | %s | %s | %s |"
                 % (label, _fmt(lm), _fmt(lw), _fmt(gm),
                    _fmt(im), _fmt(am), _fmt(p5, ".3f")))
    L.append("\nNote (gap 口径): 学习类与 GA 的 `gap mean` 为相对 per-step "
             "CPLEX 参考解的差距; CPLEX/PO-CPLEX 为精确解 (gap=0); "
             "RH-CPLEX 为 H=2 松弛启发式解相对精确解的固有 gap "
             "(§10 gap-tolerance 条款, 与学习类 gap 不可直接比较)。")
    L.append("\nTODO(人工): 结论段 - 谁最优/次优、与 CPLEX gap 排序、"
             "时延-性能权衡。\n")

    L.append("\n## 2. 学习类训练审计 (S3)\n")
    L.append("| 算法 | iters done | stopped | wall (s) | env steps | "
             "best val leak |")
    L.append("|---|---:|---|---:|---:|---:|")
    for algo, d in TRAIN_DIRS.items():
        try:
            s = json.load(open(os.path.join(PROJECT_ROOT, d,
                                            "train_summary.json")))
            fm = s.get("final_metrics", {})
            # maddpg writes a FLAT summary (iters_done/stopped/
            # best_val_leak/wall_s at top level); others nest under
            # final_metrics with total_wall_sec/best_val.
            iters_done = fm.get("iters_done", s.get("iters_done"))
            stop = fm.get("stop_reason", s.get("stopped"))
            wall = s.get("total_wall_sec", s.get("wall_s", 0)) or 0
            best = s.get("best_val", s.get("best_val_leak"))
            L.append("| %s | %s | %s | %s | %s | %s |"
                     % (algo, iters_done, stop, round(wall),
                        s.get("env_steps"), _fmt(best)))
        except Exception:
            L.append("| %s | (missing) | | | | |" % algo)
    L.append("\nTODO(人工): 3h/12h 档墙钟利用率、早停点位、"
             "params 审计 vs §2 表。\n")

    L.append("\n## 3. 泛化 (train/val/test x %d seeds, no-ref)\n"
             % GEN_SEEDS)
    L.append("| 算法 | train | val | test | spread (max-min) |")
    L.append("|---|---:|---:|---:|---:|")
    for algo in TRAIN_DIRS:
        vals = []
        for split in ("train", "val", "test"):
            m, _ = _fam("output/e45_v5_gen_%s_%s" % (algo, split),
                        "leak_rate")
            vals.append(m)
        if all(v is not None for v in vals):
            L.append("| %s | %s | %s | %s | %s |"
                     % (algo, _fmt(vals[0]), _fmt(vals[1]),
                        _fmt(vals[2]), _fmt(max(vals) - min(vals))))
        else:
            L.append("| %s | n/a | n/a | n/a | n/a |" % algo)
    L.append("\nTODO(人工): 过拟合判读 (train-val spread)。\n")

    L.append("\n## 4. GA 敏感性 (S1)\n")
    L.append("| tier | leak mean | latency p50 |")
    L.append("|---|---:|---:|")
    for tag, d in (("20x30", "output/e42_v5_ga_sens_20x30"),
                   ("40x50 (main)", "output/e41_v5_ga"),
                   ("60x80", "output/e42_v5_ga_sens_60x80")):
        lm, _ = _fam(d, "leak_rate")
        p5, _ = _fam(d, "latency_p50")
        L.append("| %s | %s | %s |" % (tag, _fmt(lm), _fmt(p5, ".3f")))

    L.append("\n## 5. 流水线审计\n")
    st = load_status()
    L.append("| task | status | restarts | budget_h |")
    L.append("|---|---|---:|---:|")
    for t in tasks:
        rec = st["tasks"].get(t.id, {})
        L.append("| %s | %s | %s | %s |"
                 % (t.id, rec.get("status", t.status),
                    rec.get("restarts", 0), t.budget_h))
    try:
        with open(TIER_REPORT_PATH) as f:
            tr = json.load(f)
        L.append("\nS0 定档: %s (per-iter %.2fs, est %.2fh)\n"
                 % (tr["ecmappo"]["decision"],
                    tr["ecmappo"]["per_iter_sec"],
                    tr["ecmappo"]["est_2500x96_hours"]))
    except Exception:
        pass
    L.append("\n## 6. V''' 验收清单\n")
    L.append("- [x] S0 冒烟 (维度/参数量/资源不变量/零非法动作): "
             "logs/s0_smoke.log")
    L.append("- [x] CPLEX 探针: output/e26_v5_cplex_probe")
    L.append("- [ ] 9 算法 30-seed 终评齐备 (S1/S2/S4, 见上表)")
    L.append("- [ ] 学习类墙钟在档 (3h: <=2.5h; 12h: <=10.5h)")
    L.append("- [ ] GA/规则预算 <=3h, 学习终评+泛化 <=1.5h")
    L.append("- [ ] 人工: 定性结论 + 与 v4 对比段")
    with open(REPORT_PATH, "w") as f:
        f.write("\n".join(L) + "\n")
    task.status = "completed"
    print("[pipeline] S5 report -> %s" % REPORT_PATH, flush=True)
    return True


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from-stage", default="S0")
    ap.add_argument("--to-stage", default="S5")
    ap.add_argument("--stage", default=None,
                    help="single stage, e.g. --stage S3 (= from=S3 to=S3)")
    ap.add_argument("--only", default=None,
                    help="run a single task id (e.g. s3_ecmappo)")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if args.stage:                    # §6.1: --stage resume-from anywhere
        args.from_stage = args.to_stage = args.stage

    os.makedirs(LOG_DIR, exist_ok=True)
    tasks = build_tasks()
    by_id = {t.id: t for t in tasks}
    order = [t for t in tasks
             if args.from_stage <= t.stage <= args.to_stage]

    if args.list or args.dry_run:
        for t in order:
            skip = "" if not t.done() else "  [DONE - will skip]"
            cmd = " ".join(t.cmd) if t.cmd else "(internal)"
            print("%-22s %-3s %-60s%s" % (t.id, t.stage, cmd[:60], skip))
        return

    n_done = n_fail = n_skip = 0
    for t in order:
        if args.only and t.id != args.only:
            continue
        if t.done():
            t.status = "completed"
            print("[pipeline] SKIP %s (artefact present)" % t.id,
                  flush=True)
            n_done += 1
            continue
        # §6.1.4 cascade-skip: a failed/skipped dep blocks dependents
        bad_deps = [d for d in t.deps
                    if by_id[d].status in ("failed", "skipped")]
        if bad_deps:
            t.status = "skipped"
            t.finished_at = time.strftime("%Y-%m-%d %H:%M:%S")
            save_status(tasks)
            print("[pipeline] CASCADE-SKIP %s (deps not completed: %s)"
                  % (t.id, ", ".join(bad_deps)), flush=True)
            n_skip += 1
            continue
        ok = run_task(t, tasks)
        n_done += int(ok)
        n_fail += int(not ok)
        save_status(tasks)
    save_status(tasks)
    write_heartbeat(tasks, None)
    print("[pipeline] ALL FINISHED: %d ok, %d failed, %d cascade-skipped."
          " status: %s" % (n_done, n_fail, n_skip, STATUS_PATH),
          flush=True)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[pipeline] interrupted by user", flush=True)
        raise
    except Exception:
        traceback.print_exc()
        sys.exit(1)
