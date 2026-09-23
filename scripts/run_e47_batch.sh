#!/bin/zsh
# e47 v5 ablation final eval + generalization (spec §7)
# per arm: (a) formal test eval, 2 inst x 30 seeds WITH per-step CPLEX ref;
#          (b) gen: train/val/test x 30 seeds, --no-ref, archived under _gen/
set -e
cd /Users/fgod/Desktop/FGOD/Projects/UAS/WTA-Dn-branch01
PY=/opt/anaconda3/envs/wta/bin/python
ARMS=(b0_000 b3_111 ad_011 ae_101 b2_110 b1_100 only_010 only_001)

for name in $ARMS; do
  model="output/e46_v5_ablation/${name}_s0/best.pt"

  # ---- (a) formal final eval on test ----
  out="output/e47_v5_ablation_${name}_s0_eval"
  log="logs/e47_${name}_s0.log"
  if [ -f "${out}/family_report.json" ]; then
    echo "[skip] e47 test ${name} already done"
  else
    echo "=== e47 test ${name} start $(date '+%F %T') ==="
    $PY experiments/dn_family_eval.py --split test \
      --policy ecmappo --model "$model" --seeds 30 \
      --data-dir data/dn-data-v5 --manifest data/dn-data-v5/MANIFEST.md \
      --output "$out" > "$log" 2>&1
    echo "=== e47 test ${name} done $(date '+%F %T') ==="
  fi

  # ---- (b) generalization: 3 splits, no ref ----
  for sp in train val test; do
    gout="output/e47_v5_ablation_${name}_s0_gen/${sp}"
    glog="logs/e47_${name}_s0_gen_${sp}.log"
    if [ -f "${gout}/family_report.json" ]; then
      echo "[skip] e47 gen ${name}/${sp} already done"
    else
      echo "=== e47 gen ${name}/${sp} start $(date '+%F %T') ==="
      $PY experiments/dn_family_eval.py --split $sp \
        --policy ecmappo --model "$model" --seeds 30 --no-ref \
        --data-dir data/dn-data-v5 --manifest data/dn-data-v5/MANIFEST.md \
        --output "$gout" > "$glog" 2>&1
      echo "=== e47 gen ${name}/${sp} done $(date '+%F %T') ==="
    fi
  done
done
echo "ALL E47 EVALS DONE $(date '+%F %T')"
