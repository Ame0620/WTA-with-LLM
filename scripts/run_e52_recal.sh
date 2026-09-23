#!/bin/zsh
# e52 recalibration round (spec §S4, preregistered grid - r2 doc §4).
# Budget tier T: 800 x 128, patience 30, eval-every 25, single seed 0,
# train/val split ONLY (test untouched - R5').
# Stage 0: smoke (1,0,0) and (0,1,0) x 30 iters -> extrapolated single-arm
#   wall in [0.4h, 1.2h]; out of band -> iters 640 / 1000 (one step),
#   recorded in logs/recal_budget.json (locked BEFORE the 10 arms run).
# Stage 1: 9 arms (R-base / E-lam0.2 / E-lam0.5 / E-ref / D-a05b10 /
#   D-a10b05 / D-a05b05 / D-ref / F-full).
# Stage 2: selector (experiments/e52_select.py select) -> (lam*, a*, b*)
#   candidates per the preregistered rule -> F-pick arm.
# Stage 3: fuse check -> lock (logs/recal_selection.json).
# Idempotent per arm: skipped iff last.pt exists AND log has "training done".
set -e
cd /Users/fgod/Desktop/FGOD/Projects/UAS/WTA-Dn-branch01
PY=/opt/anaconda3/envs/wta/bin/python
OUTROOT=output/e52_recal

# ---------------- stage 0: smoke-based tier lock ----------------
BUDGET_JSON=logs/recal_budget.json
if [ ! -f "$BUDGET_JSON" ]; then
  SMOKE_ITERS=30
  for arm in "1 0 0" "0 1 0"; do
    set -- ${=arm}
    d=$1; e=$2; c=$3
    tag="smoke_${d}${e}${c}"
    out="${OUTROOT}/_${tag}"
    log="logs/e52_${tag}.log"
    if [ -f "${out}/train_log.jsonl" ] && grep -q "training done" "$log" 2>/dev/null; then
      echo "[skip] e52 ${tag} smoke already done"
    else
      echo "=== e52 ${tag} smoke start $(date '+%F %T') ==="
      $PY marl/train.py --data-dir data/dn-data-v3 --seed 0 \
        --iters $SMOKE_ITERS --episodes-per-iter 128 --patience 30 --eval-every 25 \
        --device cpu \
        --use-dcca $d --use-eaps $e --use-casp $c \
        --output "$out" > "$log" 2>&1
    fi
  done
  $PY experiments/e52_lock_budget.py
  echo "=== e52 tier locked: see $BUDGET_JSON ==="
fi
ITERS=$($PY -c "import json;print(json.load(open('$BUDGET_JSON'))['config']['iters'])")
EPI=128; PAT=30
echo "e52 tier T locked: iters=$ITERS epi=$EPI patience=$PAT"

run_arm () {
  name=$1; d=$2; e=$3; c=$4; lam=$5; al=$6; be=$7
  out="${OUTROOT}/${name}"
  log="logs/e52_${name}.log"
  if [ -f "${out}/last.pt" ] && grep -q "training done" "$log" 2>/dev/null; then
    echo "[skip] e52 ${name} already done"; return 0
  fi
  echo "=== e52 arm ${name} (d=${d},e=${e},c=${c},lam=${lam},al=${al},be=${be}) start $(date '+%F %T') ==="
  $PY marl/train.py --data-dir data/dn-data-v3 --seed 0 \
    --iters $ITERS --episodes-per-iter $EPI --patience $PAT --eval-every 25 \
    --device cpu \
    --use-dcca $d --use-eaps $e --use-casp $c \
    --phi-scale $lam --credit-alpha $al --cf-beta $be \
    --output "$out" > "$log" 2>&1
  tail -2 "$log"
  echo "=== e52 arm ${name} done $(date '+%F %T') ==="
}

# ---------------- stage 1: 9 preregistered arms ----------------
run_arm R-base    0 0 0 1.0 1.0 1.0
run_arm E-lam0.2  0 1 0 0.2 1.0 1.0
run_arm E-lam0.5  0 1 0 0.5 1.0 1.0
run_arm E-ref     0 1 0 1.0 1.0 1.0
run_arm D-a05b10  1 0 0 1.0 0.5 1.0
run_arm D-a10b05  1 0 0 1.0 1.0 0.5
run_arm D-a05b05  1 0 0 1.0 0.5 0.5
run_arm D-ref     1 0 0 1.0 1.0 1.0
run_arm F-full    1 1 1 1.0 1.0 1.0

# ---------------- stage 2: preregistered selection -> F-pick --------
if ! grep -q '"locked"' logs/recal_selection.json 2>/dev/null; then
  echo "=== e52 selection (preregistered rule) start $(date '+%F %T') ==="
  PICK=$($PY experiments/e52_select.py select) || { echo "$PICK"; exit 3; }
  echo "selector picked: $PICK"
  set -- ${=PICK}
  LAM=$1; AL=$2; BE=$3
  run_arm F-pick 1 1 1 $LAM $AL $BE
  echo "=== e52 fuse check start $(date '+%F %T') ==="
  FUSE_OUT=$($PY experiments/e52_select.py fuse)
  FUSE_RC=$?
  echo "$FUSE_OUT"
  if [ $FUSE_RC -eq 4 ]; then
    set -- ${=FUSE_OUT}
    echo "fuse FAIL -> one preregistered retry with second-best $2 $3 $4"
    run_arm F-pick2 1 1 1 $2 $3 $4
    $PY experiments/e52_select.py fuse
  elif [ $FUSE_RC -ne 0 ]; then
    exit 3
  fi
fi
echo "ALL E52 ARMS DONE $(date '+%F %T') - params locked in logs/recal_selection.json"
