"""E19: final comparison table over the test split (s01-s02 x 30 seeds).

Collects the family_report.json of every arm and renders one table +
takeaways. Paths default to the canonical run layout; missing arms are
skipped with a note (so this can run mid-campaign too).

    python experiments/e19_report.py [--output output/e19_eval]
"""

import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(HERE)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

OUT = os.path.join(PROJECT_ROOT, "output")

ARMS = [
    ("none", os.path.join(OUT, "regress_e11_none",
                          "family_report.json")),
    ("greedy", os.path.join(OUT, "regress_e12_greedy",
                            "family_report.json")),
    ("cplex", os.path.join(OUT, "regress_e13_cplex",
                           "family_report.json")),
    ("pocplex", os.path.join(OUT, "e18_eval", "pocplex",
                             "family_report.json")),
    ("e15 (relaxed)", os.path.join(OUT, "e19_eval", "e15",
                                   "family_report.json")),
    ("e16 c005", os.path.join(OUT, "e19_eval", "e16_c005",
                              "family_report.json")),
    ("e16 c010", os.path.join(OUT, "e19_eval", "e16_c010",
                              "family_report.json")),
    ("e16 c030", os.path.join(OUT, "e19_eval", "e16_c030",
                              "family_report.json")),
    ("e16 c050", os.path.join(OUT, "e19_eval", "e16_c050",
                              "family_report.json")),
    ("e16 pos-ctrl", os.path.join(OUT, "e19_eval", "e16_pos",
                                  "family_report.json")),
    ("e17 bc-blend", os.path.join(OUT, "e19_eval", "e17_bc01",
                                  "family_report.json")),
    ("e17 bc-full", os.path.join(OUT, "e19_eval", "e17_bc10",
                                 "family_report.json")),
    ("e14 (ref)", os.path.join(OUT, "e19_eval", "e14",
                               "family_report.json")),
]

KEYS = ["leak_rate", "gap_mean", "invalid_engagement_rate",
        "ammo_efficiency", "destroyed_value", "destroyed_count"]


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default=os.path.join(OUT, "e19_eval"))
    args = ap.parse_args(argv)
    os.makedirs(args.output, exist_ok=True)

    rows = []
    missing = []
    for label, path in ARMS:
        if not os.path.exists(path):
            missing.append(label)
            continue
        d = json.load(open(path))
        fam = d["family"]
        row = {"label": label}
        for k in KEYS:
            cell = fam.get(k)
            row[k] = (cell["mean"], cell["std"]) if cell else None
        rows.append(row)

    L = ["# E19 终评对比（test split s01-s02 × 30 seeds）", ""]
    L.append("| policy | leak mean±std | gap mean | invalid | ammo eff | "
             "destroyed val | kills |")
    L.append("|---|---|---:|---:|---:|---:|---:|")
    for r in rows:
        def f(k, spec=".4f"):
            v = r.get(k)
            if not v or v[0] is None:
                return "n/a"
            return ( "%" + spec) % v[0]
        lr = r.get("leak_rate")
        lrs = ("%0.4f±%0.3f" % lr) if lr else "n/a"
        L.append("| %s | %s | %s | %s | %s | %s | %s |"
                 % (r["label"], lrs, f("gap_mean"), f("invalid_engagement_rate"),
                    f("ammo_efficiency", ".1f"), f("destroyed_value", ".1f"),
                    f("destroyed_count", ".2f")))
    if missing:
        L.append("")
        L.append("缺失（尚未完成）：%s" % ", ".join(missing))

    # takeaways
    L += ["", "## 要点"]
    by = {r["label"]: r for r in rows}
    if "greedy" in by and "cplex" in by:
        L.append("- greedy vs myopic-CPLEX leak：%.4f → %.4f"
                 % (by["greedy"]["leak_rate"][0], by["cplex"]["leak_rate"][0]))
    marl_arms = [r for r in rows if r["label"].startswith(("e15", "e16",
                                                           "e17"))]
    if marl_arms:
        best = min(marl_arms, key=lambda r: (r["leak_rate"] or (9,))[0])
        L.append("- MARL 最佳臂：%s（leak %.4f）"
                 % (best["label"], best["leak_rate"][0]))
        if "pocplex" in by:
            L.append("- PO-CPLEX（同信息中心化基线）leak：%.4f；MARL 与其差距 "
                     "=%.4f" % (by["pocplex"]["leak_rate"][0],
                                best["leak_rate"][0]
                                - by["pocplex"]["leak_rate"][0]))
    L.append("")

    path = os.path.join(args.output, "e19_summary.md")
    with open(path, "w") as f:
        f.write("\n".join(L) + "\n")
    json.dump({"rows": [{k: v for k, v in r.items() if k != "label"}
                        | {"label": r["label"]} for r in rows],
               "missing": missing},
              open(os.path.join(args.output, "e19_summary.json"), "w"),
              indent=2)
    print("\n".join(L))
    print("-> %s" % path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
