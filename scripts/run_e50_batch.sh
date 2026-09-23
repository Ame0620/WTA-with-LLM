#!/bin/zsh
# e50 v3 ablation final eval + generalization (spec §S5)
# per arm & seed: (a) formal test eval, 2 inst x 30 seeds WITH per-step CPLEX
#     reference, routed through experiments/e50_eval_entry.py so the CPLEX
#     reference solutions are cached cross-arm (first-computed -> reused);
#     (b) gen: train/val/test x 30 seeds, --no-ref, archived under _gen/<sp>.
# Arm order mirrors run_e49_batch.sh; seeds 0/1/2. Idempotent per output.
set -e
cd /Users/fgod/Desktop/FGOD/Projects/UAS/WTA-Dn-branch01
PY=/opt/anaconda3/envs/wta/bin/python
ARMS=(b0_000 b3_111 ad_011 ae_101 b2_110 b1_100 only_010 only_001)
SEEDS=(0 1 2)

for s in "${SEEDS[@]}"; do
for name in "${ARMS[@]}"; do
  model="output/e49_v3_ablation/${name}_s${s}/best.pt"

  # ---- (a) formal final eval on test (with cached CPLEX reference) ----
  out="output/e50_v3_ablation_${name}_s${s}_eval"
  log="logs/e50_${name}_s${s}.log"
  if [ -f "${out}/family_report.json" ]; then
    echo "[skip] e50 test ${name}_s${s} already done"
  else
    echo "=== e50 test ${name}_s${s} start $(date '+%F %T') ==="
    $PY experiments/e50_eval_entry.py --split test \
      --policy ecmappo --model "$model" --seeds 30 --seed-base 42 \
      --data-dir data/dn-data-v3 --manifest data/dn-data-v3/MANIFEST.md \
      --output "$out" > "$log" 2>&1
    echo "=== e50 test ${name}_s${s} done $(date '+%F %T') ==="
  fi

  # ---- (b) generalization: 3 splits, no ref ----
  for sp in train val test; do
    gout="output/e50_v3_ablation_${name}_s${s}_gen/${sp}"
    glog="logs/e50_${name}_s${s}_gen_${sp}.log"
    if [ -f "${gout}/family_report.json" ]; then
      echo "[skip] e50 gen ${name}_s${s}/${sp} already done"
    else
      echo "=== e50 gen ${name}_s${s}/${sp} start $(date '+%F %T') ==="
      $PY experiments/dn_family_eval.py --split $sp \
        --policy ecmappo --model "$model" --seeds 30 --seed-base 42 --no-ref \
        --data-dir data/dn-data-v3 --manifest data/dn-data-v3/MANIFEST.md \
        --output "$gout" > "$glog" 2>&1
      echo "=== e50 gen ${name}_s${s}/${sp} done $(date '+%F %T') ==="
    fi
  done
done
done

# ---- reproducibility self-check: c8 (b3_111) s0 test eval rerun once ----
rout="output/e50_v3_ablation_b3_111_s0_eval_repro"
if [ -f "${rout}/family_report.json" ]; then
  echo "[skip] e50 repro check already done"
else
  echo "=== e50 repro rerun b3_111_s0 start $(date '+%F %T') ==="
  $PY experiments/e50_eval_entry.py --split test \
    --policy ecmappo --model "output/e49_v3_ablation/b3_111_s0/best.pt" \
    --seeds 30 --seed-base 42 \
    --data-dir data/dn-data-v3 --manifest data/dn-data-v3/MANIFEST.md \
    --output "$rout" > logs/e50_b3_111_s0_repro.log 2>&1
  $PY - <<'EOF'
import json
a = json.load(open("output/e50_v3_ablation_b3_111_s0_eval/family_report.json"))
b = json.load(open("output/e50_v3_ablation_b3_111_s0_eval_repro/family_report.json"))
ok = all(ia["result_hash"] == ib["result_hash"]
         for ia, ib in zip(a["instances"], b["instances"]))
print("REPRO CHECK (b3_111_s0 test result_hash):", "PASS" if ok else "FAIL")
for ia, ib in zip(a["instances"], b["instances"]):
    print("  %s: %s vs %s" % (ia["instance"], ia["result_hash"][:16],
                              ib["result_hash"][:16]))
raise SystemExit(0 if ok else 1)
EOF
  echo "=== e50 repro rerun done $(date '+%F %T') ==="
fi
echo "ALL E50 EVALS DONE $(date '+%F %T')"
