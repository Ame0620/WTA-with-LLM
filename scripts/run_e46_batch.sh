#!/bin/zsh
# e46 v5 ablation 8-arm sequential training (tier A-1 locked in S5)
# order per spec §6.2: b0 -> b3 -> ad -> ae -> b2 -> b1 -> only010 -> only001
set -e
cd /Users/fgod/Desktop/FGOD/Projects/UAS/WTA-Dn-branch01
PY=/opt/anaconda3/envs/wta/bin/python
ITERS=1000; EPI=48; PAT=30
run_arm () {
  name=$1; d=$2; e=$3; c=$4
  out="output/e46_v5_ablation/${name}_s0"
  log="logs/e46_${name}_s0.log"
  if [ -f "${out}/last.pt" ] && grep -q "training done" "$log" 2>/dev/null; then
    echo "[skip] ${name} already done"; return 0
  fi
  echo "=== e46 arm ${name} (d=${d},e=${e},c=${c}) start $(date '+%F %T') ==="
  $PY marl/train.py --data-dir data/dn-data-v5 --seed 0 \
    --iters $ITERS --episodes-per-iter $EPI --patience $PAT --eval-every 25 \
    --use-dcca $d --use-eaps $e --use-casp $c \
    --output "$out" > "$log" 2>&1
  tail -2 "$log"
  echo "=== e46 arm ${name} done $(date '+%F %T') ==="
}
run_arm b0_000   0 0 0
run_arm b3_111   1 1 1
run_arm ad_011   0 1 1
run_arm ae_101   1 0 1
run_arm b2_110   1 1 0
run_arm b1_100   1 0 0
run_arm only_010 0 1 0
run_arm only_001 0 0 1
echo "ALL E46 ARMS DONE $(date '+%F %T')"
