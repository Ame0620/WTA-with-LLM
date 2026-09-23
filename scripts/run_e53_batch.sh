#!/bin/zsh
# e53 formal ablation round, second pass (r2 spec §5).
# 24 arms = 8 cfg x 3 seeds, tier A (3000x128, patience 60, eval-every 25)
# unless demoted by the preregistered smoke check in
# experiments/e53_lock_budget.py (logs/ablation_v3r2_budget.json).
# R4' uniformity: every arm differs ONLY in the three switches and the
# three explicit recalibration params (read from logs/recal_selection.json,
# must be LOCKED) - everything else byte-identical (device cpu, seed s).
# Execution order per seed pass: s0 first (b0_000, b3_111, ad_011,
# ae_101, b2_110, b1_100, only_010, only_001), then the s0 lightweight
# checkpoint (experiments/e53_checkpoint_sanity.py - halt on anomaly),
# then s1, then s2. Idempotent per arm.
set -e
cd /Users/fgod/Desktop/FGOD/Projects/UAS/WTA-Dn-branch01
PY=/opt/anaconda3/envs/wta/bin/python
OUTROOT=output/e53_v3_ablation_r2
BUDGET=logs/ablation_v3r2_budget.json
SELJSON=logs/recal_selection.json

# ---------------- stage 0: smoke-based tier lock ----------------
if [ ! -f "$BUDGET" ]; then
  for arm in "1 1 1" "0 0 0"; do
    set -- ${=arm}
    d=$1; e=$2; c=$3
    tag="smoke_${d}${e}${c}"
    out="${OUTROOT}/_${tag}"
    log="logs/e53_${tag}.log"
    if [ -f "${out}/train_log.jsonl" ] && grep -q "training done" "$log" 2>/dev/null; then
      echo "[skip] e53 ${tag} smoke already done"
    else
      echo "=== e53 ${tag} smoke start $(date '+%F %T') ==="
      $PY marl/train.py --data-dir data/dn-data-v3 --seed 0 \
        --iters 50 --episodes-per-iter 128 --patience 60 --eval-every 25 \
        --device cpu \
        --use-dcca $d --use-eaps $e --use-casp $c \
        --output "$out" > "$log" 2>&1
    fi
  done
  $PY experiments/e53_lock_budget.py
fi
ITERS=$($PY -c "import json;print(json.load(open('$BUDGET'))['config']['iters'])")
PAT=$($PY -c "import json;print(json.load(open('$BUDGET'))['config']['patience'])")
DEV=$($PY -c "import json;print(json.load(open('$BUDGET'))['device'])")
echo "e53 tier locked: iters=$ITERS patience=$PAT device=$DEV"

# ---------------- locked recalibration params (explicit) ----------
LAM=$($PY -c "import json;s=json.load(open('$SELJSON'));assert s.get('locked');print('%.10g'%s['locked']['phi_scale'])")
AL=$($PY -c "import json;s=json.load(open('$SELJSON'));assert s.get('locked');print('%.10g'%s['locked']['credit_alpha'])")
BE=$($PY -c "import json;s=json.load(open('$SELJSON'));assert s.get('locked');print('%.10g'%s['locked']['cf_beta'])")
echo "e53 recal params from $SELJSON: lam=$LAM alpha=$AL beta=$BE"

run_arm () {
  name=$1; d=$2; e=$3; c=$4
  out="${OUTROOT}/${name}"
  log="logs/e53_${name}.log"
  if [ -f "${out}/last.pt" ] && grep -q "training done" "$log" 2>/dev/null; then
    echo "[skip] e53 ${name} already done"; return 0
  fi
  echo "=== e53 arm ${name} (d=${d},e=${e},c=${c}) start $(date '+%F %T') ==="
  $PY marl/train.py --data-dir data/dn-data-v3 --seed $5 \
    --iters $ITERS --episodes-per-iter 128 --patience $PAT --eval-every 25 \
    --device $DEV \
    --use-dcca $d --use-eaps $e --use-casp $c \
    --phi-scale $LAM --credit-alpha $AL --cf-beta $BE \
    --output "$out" > "$log" 2>&1
  tail -2 "$log"
  echo "=== e53 arm ${name} done $(date '+%F %T') ==="
}

# execution order (r2 §5): c1, c8, c4, c6, c7, c5, c3, c2
for s in 0 1 2; do
  run_arm b0_000_s$s  0 0 0 $s
  run_arm b3_111_s$s  1 1 1 $s
  run_arm ad_011_s$s  0 1 1 $s
  run_arm ae_101_s$s  1 0 1 $s
  run_arm b2_110_s$s  1 1 0 $s
  run_arm b1_100_s$s  1 0 0 $s
  run_arm only_010_s$s 0 1 0 $s
  run_arm only_001_s$s 0 0 1 $s
  if [ $s -eq 0 ]; then
    echo "=== e53 s0 lightweight checkpoint $(date '+%F %T') ==="
    $PY experiments/e53_checkpoint_sanity.py
  fi
done
echo "ALL E53 ARMS DONE $(date '+%F %T')"
