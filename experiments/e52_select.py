"""e52: preregistered recalibration selector (r2 spec §4.2-§4.3, R10).

Everything about the search is FROZEN up front (grids, tolerance, tie
rules, fallbacks P1-P3); this script only EXECUTES the rule against the
val curves and records the full decision chain so that no mid-run grid
edit can hide. Test numbers are never read here (val only, R5').

Sub-commands
  select   read the 9 stage-1 arms, apply stage-1 (EAPS) + stage-2
           (DCCA) rules, persist the chain to logs/recal_selection.json
           and print "LAM ALPHA BETA" for the F-pick arm. If a candidate
           set is empty the preregistered extension (P1: lam=0.1; P2:
           (0.25,0.5)/(0.5,0.25)) is REQUIRED first: prints "P1 ..."/
           "P2 ..." and exits 3 (shell reruns the extension arm(s), then
           select again - the extended arms join the candidate set).
  fuse     after F-pick: best_val(F-pick) <= best_val(F-full) + 0.005
           locks the pick. On failure prints "RETRY LAM ALPHA BETA"
           (per-module second-best) and exits 4 (rerun as F-pick2, once);
           a second failure locks the per-module best anyway (P3) with
           the fuse loss recorded verbatim.

All arm names map to (switches, params) via a single frozen table; every
parameter point that ever appears is checked against the preregistered
sets on lock (auditability, R10).
"""
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E52 = os.path.join(ROOT, "output", "e52_recal")
SEL = os.path.join(ROOT, "logs", "recal_selection.json")

PREREG = {
    "eaps_grid": [0.2, 0.5, 1.0],
    "eaps_extend_P1": [0.1],
    "dcca_grid": [[0.5, 1.0], [1.0, 0.5], [0.5, 0.5], [1.0, 1.0]],
    "dcca_extend_P2": [[0.25, 0.5], [0.5, 0.25]],
    "tolerance": 0.005,
    "tie_rule": "EAPS: smaller |lam-1|; DCCA: smaller dist to (1,1)",
    "fuse_tolerance": 0.005,
    "fuse_retry": "one retry with per-module second-best, then P3",
}

# arm name -> (d, e, c, lam, alpha, beta)   [frozen]
ARMS = {
    "R-base":    (0, 0, 0, 1.0, 1.0, 1.0),
    "E-lam0.2":  (0, 1, 0, 0.2, 1.0, 1.0),
    "E-lam0.5":  (0, 1, 0, 0.5, 1.0, 1.0),
    "E-ref":     (0, 1, 0, 1.0, 1.0, 1.0),
    "E-lam0.1":  (0, 1, 0, 0.1, 1.0, 1.0),      # P1 extension only
    "D-a05b10":  (1, 0, 0, 1.0, 0.5, 1.0),
    "D-a10b05":  (1, 0, 0, 1.0, 1.0, 0.5),
    "D-a05b05":  (1, 0, 0, 1.0, 0.5, 0.5),
    "D-ref":     (1, 0, 0, 1.0, 1.0, 1.0),
    "D-a025b05": (1, 0, 0, 1.0, 0.25, 0.5),     # P2 extension only
    "D-a05b025": (1, 0, 0, 1.0, 0.5, 0.25),     # P2 extension only
    "F-full":    (1, 1, 1, 1.0, 1.0, 1.0),
}
EAPS_ARMS = {"0.2": "E-lam0.2", "0.5": "E-lam0.5", "1": "E-ref",
             "0.1": "E-lam0.1"}
DCCA_ARMS = {"(0.5,1)": "D-a05b10", "(1,0.5)": "D-a10b05",
             "(0.5,0.5)": "D-a05b05", "(1,1)": "D-ref",
             "(0.25,0.5)": "D-a025b05", "(0.5,0.25)": "D-a05b025"}


def _load_arm(name):
    """Return {switches, params, val_curve, best_val, best_iter} or None."""
    d = os.path.join(E52, name)
    tp = os.path.join(d, "train_summary.json")
    if not os.path.exists(tp):
        return None
    ts = json.load(open(tp))
    log = [json.loads(l) for l in open(os.path.join(d, "train_log.jsonl"))]
    curve = [{"iter": r["iter"], "val": r["val_leak_mean"]} for r in log]
    best = min(curve, key=lambda r: r["val"])
    if name in ARMS:
        d6 = ARMS[name]
        switches, params = list(d6[:3]), \
            {"phi_scale": d6[3], "credit_alpha": d6[4], "cf_beta": d6[5]}
    else:
        # F-pick / F-pick2 carry DYNAMIC (lam, alpha, beta) - read them
        # from the r2 §3.2 checkpoint metadata, never from the arm name
        switches = [ts["ablation"]["use_dcca"], ts["ablation"]["use_eaps"],
                    ts["ablation"]["use_casp"]]
        params = {k: float(v) for k, v in ts["reshaping"].items()}
    return {"switches": switches, "params": params,
            "val_curve": curve, "best_val": best["val"],
            "best_iter": best["iter"], "stop_reason":
            ts["final_metrics"]["stop_reason"]}


def _read_sel():
    if os.path.exists(SEL):
        return json.load(open(SEL))
    return {"preregistered": PREREG, "arms": {}, "stages": {},
            "locked": None, "history": []}


def _write_sel(doc):
    with open(SEL, "w") as f:
        json.dump(doc, f, indent=1, ensure_ascii=False)


def _note(doc, msg):
    doc["history"].append("%s | %s" %
                          (time.strftime("%Y-%m-%dT%H:%M:%S"), msg))


def _pick_stage(cands, base_bv, doc, stage):
    """Apply the stage rule; cands = [(point, arm_name, best_val)] for the
    CURRENTLY available grid; returns (chosen, second_best) or triggers
    the preregistered extension verdict."""
    ok = [(p, a, v) for (p, a, v) in cands if v <= base_bv + PREREG["tolerance"]]
    doc["stages"][stage] = {"candidates_ok": [
        {"point": p, "arm": a, "best_val": v} for (p, a, v) in ok],
        "rule": "best_val minimal; tie -> closer to 1.0/(1,1)"}
    if not ok:
        return None, None
    key = (lambda t: (t[2], abs(t[0] - 1.0))) if stage == "eaps" else \
          (lambda t: (t[2], (t[0][0] - 1.0) ** 2 + (t[0][1] - 1.0) ** 2))
    ranked = sorted(ok, key=key)
    second = ranked[1] if len(ranked) > 1 else None
    return ranked[0], second


def cmd_select():
    doc = _read_sel()
    need = ["R-base", "E-lam0.2", "E-lam0.5", "E-ref", "D-a05b10",
            "D-a10b05", "D-a05b05", "D-ref", "F-full"]
    arms = {}
    for n in need:
        a = _load_arm(n)
        if a is None:
            print("MISSING %s (run the stage-1 arms first)" % n)
            return 2
        arms[n] = a
    # P1/P2 extension arms join IF they exist (they only exist after the
    # fallback was triggered - their presence is itself evidence)
    for n in ("E-lam0.1", "D-a025b05", "D-a05b025"):
        a = _load_arm(n)
        if a is not None:
            arms[n] = a
    doc["arms"] = arms
    base_bv = arms["R-base"]["best_val"]
    _note(doc, "select: R-base best_val=%.6f" % base_bv)

    # ---- stage 1: EAPS --------------------------------------------
    grid = list(PREREG["eaps_grid"])
    if "E-lam0.1" in arms:
        grid += PREREG["eaps_extend_P1"]
    cands = [(lam, EAPS_ARMS["%g" % lam], arms[EAPS_ARMS["%g" % lam]]
              ["best_val"]) for lam in grid]
    top, sec = _pick_stage(cands, base_bv, doc, "eaps")
    if top is None:
        if "E-lam0.1" not in arms:
            _note(doc, "select: EAPS candidate set EMPTY -> P1 extension "
                       "(lam=0.1) required")
            _write_sel(doc)
            print("P1 rerun arm E-lam0.1 (preregistered extension)")
            return 3
        _note(doc, "select: EAPS still empty after P1 -> UNREPAIRABLE in "
                   "grid; escalate to user (no unpreregistered search)")
        _write_sel(doc)
        print("P1-EMPTY EAPS unrepairable within preregistered grid - "
              "escalate (r2 §4.3)")
        return 3
    lam = top[0]
    _note(doc, "select: EAPS -> lam=%g (arm %s, best_val=%.6f)"
          % (lam, top[1], top[2]))

    # ---- stage 2: DCCA --------------------------------------------
    grid = [tuple(p) for p in PREREG["dcca_grid"]]
    if "D-a025b05" in arms:
        grid += [tuple(p) for p in PREREG["dcca_extend_P2"]]
    cands = [(ab, DCCA_ARMS["(%g,%g)" % ab],
              arms[DCCA_ARMS["(%g,%g)" % ab]]["best_val"]) for ab in grid]
    topd, secd = _pick_stage(cands, base_bv, doc, "dcca")
    if topd is None:
        if "D-a025b05" not in arms or "D-a05b025" not in arms:
            _note(doc, "select: DCCA candidate set EMPTY -> P2 extension "
                       "(0.25,0.5)+(0.5,0.25) required")
            _write_sel(doc)
            print("P2 rerun arms D-a025b05 D-a05b025 (preregistered "
                  "extension)")
            return 3
        _note(doc, "select: DCCA still empty after P2 -> escalate with "
                   "mechanistic attribution")
        _write_sel(doc)
        print("P2-EMPTY DCCA unrepairable within preregistered grid - "
              "escalate (r2 §4.3)")
        return 3
    ab = topd[0]
    _note(doc, "select: DCCA -> alpha=%g beta=%g (arm %s, best_val=%.6f)"
          % (ab[0], ab[1], topd[1], topd[2]))

    doc["pending_fuse"] = {"phi_scale": lam, "credit_alpha": ab[0],
                           "cf_beta": ab[1],
                           "second_best": {
                               "phi_scale": sec[0] if sec else None,
                               "credit_alpha": secd[0][0] if secd else None,
                               "cf_beta": secd[0][1] if secd else None}}
    _write_sel(doc)
    print("%.10g %.10g %.10g" % (lam, ab[0], ab[1]))
    return 0


def cmd_fuse():
    doc = _read_sel()
    if doc.get("locked"):
        print("LOCKED %g %g %g (already)" % (
            doc["locked"]["phi_scale"], doc["locked"]["credit_alpha"],
            doc["locked"]["cf_beta"]))
        return 0
    pend = doc.get("pending_fuse")
    if not pend:
        print("no pending pick - run `select` first")
        return 2
    ffull = _load_arm("F-full")
    picks = [n for n in ("F-pick", "F-pick2") if _load_arm(n)]
    if not picks:
        print("F-pick arm not trained yet")
        return 2
    fp = _load_arm(picks[-1])
    doc["stages"]["fuse"] = {
        "arm": picks[-1], "f_full_best": ffull["best_val"],
        "f_pick_best": fp["best_val"], "params": fp["params"]}
    if fp["best_val"] <= ffull["best_val"] + PREREG["fuse_tolerance"]:
        doc["locked"] = {"phi_scale": pend["phi_scale"],
                         "credit_alpha": pend["credit_alpha"],
                         "cf_beta": pend["cf_beta"]}
        _note(doc, "fuse: PASS (pick %.6f <= full %.6f + tol) -> locked"
              % (fp["best_val"], ffull["best_val"]))
        _write_sel(doc)
        print("LOCKED %g %g %g" % (pend["phi_scale"], pend["credit_alpha"],
                                   pend["cf_beta"]))
        return 0
    if picks[-1] == "F-pick":
        sb = pend["second_best"]
        _note(doc, "fuse: FAIL (pick %.6f > full %.6f + tol) -> one retry "
              "with per-module second-best" % (fp["best_val"],
                                               ffull["best_val"]))
        _write_sel(doc)
        print("RETRY %.10g %.10g %.10g" % (sb["phi_scale"],
                                           sb["credit_alpha"], sb["cf_beta"]))
        return 4
    # second failure -> P3: lock the per-module pick, report the loss
    doc["locked"] = {"phi_scale": pend["phi_scale"],
                     "credit_alpha": pend["credit_alpha"],
                     "cf_beta": pend["cf_beta"]}
    doc["stages"]["fuse"]["P3"] = ("locked per-module best despite fuse "
                                   "failure; full-open loss reported "
                                   "verbatim (r2 §4.3 rule 3)")
    _note(doc, "fuse: FAIL twice -> P3 lock (full-open loss recorded)")
    _write_sel(doc)
    print("LOCKED-P3 %g %g %g" % (pend["phi_scale"], pend["credit_alpha"],
                                  pend["cf_beta"]))
    return 0


def main(argv):
    if len(argv) != 1 or argv[0] not in ("select", "fuse"):
        print("usage: e52_select.py select|fuse")
        return 2
    return cmd_select() if argv[0] == "select" else cmd_fuse()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
