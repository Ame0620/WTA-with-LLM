#!/bin/bash
# E19: evaluate every finished training arm on the test split
# (s01-s02 x 30 seeds). Idempotent: skips arms whose family_report.json
# already exists. Usage: bash experiments/e19_eval.sh
set -u
cd "$(dirname "$0")/.."
P=/opt/anaconda3/envs/wta/bin/python
OUT=output/e19_eval
mkdir -p "$OUT"

run_arm () {  # label ckpt [extra args...]
    local label=$1; shift
    local ckpt=$1; shift
    if [ -f "$OUT/$label/family_report.json" ]; then
        echo "[e19] $label already done, skip"
        return
    fi
    if [ ! -f "$ckpt" ]; then
        echo "[e19] $label: missing ckpt $ckpt, skip"
        return
    fi
    echo "[e19] evaluating $label ..."
    $P experiments/dn_family_eval.py --policy marl --model "$ckpt" \
        --split test --seeds 30 --tmp-dir /tmp/e19_scratch \
        --output "$OUT/$label" ${1+"$@"} > "$OUT/$label.log" 2>&1 \
        && echo "[e19] $label OK" || echo "[e19] $label FAILED (see $OUT/$label.log)"
}

run_arm e14      output/e14_marl_train/best.pt
run_arm e15      output/e15_train/best.pt
run_arm e16_c005 output/e16_scan/c005/best.pt
run_arm e16_c010 output/e16_scan/c010/best.pt
run_arm e16_c030 output/e16_scan/c030/best.pt
run_arm e16_c050 output/e16_scan/c050/best.pt
run_arm e16_pos  output/e16_pos/best.pt
run_arm e17_bc01 output/e17_bc01/best.pt
run_arm e17_bc10 output/e17_bc10/best.pt

$P experiments/e19_report.py
