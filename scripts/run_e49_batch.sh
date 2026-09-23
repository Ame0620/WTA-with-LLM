#!/bin/zsh
# e49 v3 ablation 8-arm x 3-seed sequential training (spec §S4, tier D locked in S3)
# Arm order per spec §S4 (same within every seed pass):
#   c1/b0_000 -> c8/b3_111 -> c4/ad_011 -> c6/ae_101 -> c7/b2_110
#   -> c5/b1_100 -> c3/only_010 -> c2/only_001
# Seed-major execution per spec §S4: run s0 first, then the s0 lightweight
# checkpoint (per-arm self-check + c8-vs-c1 sanity), then s1/s2.
# Usage:  ./scripts/run_e49_batch.sh [seeds...]   (default: 0 1 2)
# Idempotent: an arm is skipped iff last.pt exists AND its log contains
# "training done" -> safe to re-run after interruption.
set -e
cd /Users/fgod/Desktop/FGOD/Projects/UAS/WTA-Dn-branch01
PY=/opt/anaconda3/envs/wta/bin/python
# Tier D (locked in S3, logs/ablation_v3_budget.json): 500 x 64, patience 20
ITERS=500; EPI=64; PAT=20

run_arm () {
  name=$1; d=$2; e=$3; c=$4; s=$5
  out="output/e49_v3_ablation/${name}_s${s}"
  log="logs/e49_${name}_s${s}.log"
  if [ -f "${out}/last.pt" ] && grep -q "training done" "$log" 2>/dev/null; then
    echo "[skip] ${name}_s${s} already done"; return 0
  fi
  echo "=== e49 arm ${name}_s${s} (d=${d},e=${e},c=${c}) start $(date '+%F %T') ==="
  $PY marl/train.py --data-dir data/dn-data-v3 --seed ${s} \
    --iters $ITERS --episodes-per-iter $EPI --patience $PAT --eval-every 25 \
    --use-dcca $d --use-eaps $e --use-casp $c \
    --output "$out" > "$log" 2>&1
  tail -2 "$log"
  echo "=== e49 arm ${name}_s${s} done $(date '+%F %T') ==="
}

run_seed () {
  s=$1
  run_arm b0_000   0 0 0 ${s}
  run_arm b3_111   1 1 1 ${s}
  run_arm ad_011   0 1 1 ${s}
  run_arm ae_101   1 0 1 ${s}
  run_arm b2_110   1 1 0 ${s}
  run_arm b1_100   1 0 0 ${s}
  run_arm only_010 0 1 0 ${s}
  run_arm only_001 0 0 1 ${s}
}

if [ $# -eq 0 ]; then SEEDS=(0 1 2); else SEEDS=("$@"); fi
for s in "${SEEDS[@]}"; do
  echo "######## e49 seed pass s${s} start $(date '+%F %T') ########"
  run_seed ${s}
  echo "######## e49 seed pass s${s} done $(date '+%F %T') ########"
done
echo "ALL E49 ARMS DONE $(date '+%F %T')"
