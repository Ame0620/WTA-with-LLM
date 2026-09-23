#!/bin/zsh
# e54: final evaluation + generalization sweep for the r2 ablation
# (r2 spec §6 - full mirror of the e50 protocol, path/ID replacement).
#   Phase 1: test final eval per arm, 30 seeds x 2 instances (60
#            rollouts, CPLEX reference via the shared cache).
#   Phase 2: generalization per arm/seed - train/val/test x --no-ref.
#   Phase 3: reproduction spot-check c8/b3_111 s0 (rerun the test eval,
#            result_hash must match bit-for-bit).
# Every model load goes through MarlPolicy's anti-cross-arm guard:
# MARL_EXPECT_RESHAPING is exported from the LOCKED e52 pick
# (logs/recal_selection.json) - a mismatched checkpoint raises at load.
# Idempotent: a phase is skipped iff its final report already exists.
set -e
cd /Users/fgod/Desktop/FGOD/Projects/UAS/WTA-Dn-branch01
PY=/opt/anaconda3/envs/wta/bin/python
export MARL_EXPECT_RESHAPING="$($PY -c "import json;s=json.load(open('logs/recal_selection.json'));l=s['locked'];print('%g,%g,%g'%(l['phi_scale'],l['credit_alpha'],l['cf_beta']))")"
echo "e54 anti-cross-arm guard: MARL_EXPECT_RESHAPING=$MARL_EXPECT_RESHAPING"
ARMS="b0_000 b3_111 ad_011 ae_101 b2_110 b1_100 only_010 only_001"

# ---------------- Phase 1: test final eval (all 24 checkpoints) -----
for s in 0 1 2; do
  for arm in ${=ARMS}; do
    out="output/e54_v3_ablation_${arm}_s${s}_eval"
    if [ -f "${out}/family_report.json" ]; then
      echo "[skip] ${arm}_s${s} eval"; continue
    fi
    echo "=== e54 ${arm}_s${s} test eval start $(date '+%F %T') ==="
    $PY experiments/e50_eval_entry.py --split test --policy ecmappo \
      --model output/e53_v3_ablation_r2/${arm}_s${s}/best.pt \
      --seeds 30 --seed-base 42 \
      --output "$out" > "logs/e54_${arm}_s${s}_eval.log" 2>&1
  done
done

# ---------------- Phase 2: generalization (3 splits, no ref) --------
for s in 0 1 2; do
  for arm in ${=ARMS}; do
    for split in train val test; do
      out="output/e54_v3_ablation_${arm}_s${s}_gen/${split}"
      if [ -f "${out}/family_report.json" ]; then
        echo "[skip] ${arm}_s${s} gen/${split}"; continue
      fi
      echo "=== e54 ${arm}_s${s} gen ${split} start $(date '+%F %T') ==="
      $PY experiments/dn_family_eval.py --split $split --policy ecmappo \
        --model output/e53_v3_ablation_r2/${arm}_s${s}/best.pt \
        --seeds 30 --seed-base 42 --no-ref \
        --output "$out" > "logs/e54_${arm}_s${s}_gen_${split}.log" 2>&1
    done
  done
done

# ---------------- Phase 3: reproduction spot-check (c8 s0) ----------
if [ ! -f output/e54_v3_ablation_b3_111_s0_eval_repro/family_report.json ]; then
  echo "=== e54 repro b3_111 s0 (rerun) start $(date '+%F %T') ==="
  $PY experiments/e50_eval_entry.py --split test --policy ecmappo \
    --model output/e53_v3_ablation_r2/b3_111_s0/best.pt \
    --seeds 30 --seed-base 42 \
    --output output/e54_v3_ablation_b3_111_s0_eval_repro \
    > logs/e54_repro_b3_111_s0.log 2>&1
fi
$PY - <<'EOF'
import json
a = json.load(open("output/e54_v3_ablation_b3_111_s0_eval/"
                   "family_report.json"))
b = json.load(open("output/e54_v3_ablation_b3_111_s0_eval_repro/"
                   "family_report.json"))
# hashes live at the INSTANCE level (dn_family_eval.py:335,
# dn_report._fingerprint over run records) - compare the full ordered
# list, bit-for-bit.
ha = [i["result_hash"] for i in a["instances"]]
hb = [i["result_hash"] for i in b["instances"]]
assert len(ha) == len(hb) and ha, "instance count mismatch or empty"
for x, y in zip(ha, hb):
    assert x == y, "reproduction mismatch: %s != %s" % (x, y)
print("e54 repro spot-check: %d instance result_hashes bit-identical"
      % len(ha))
EOF
$PY experiments/e55_summary.py
echo "E54 ALL DONE $(date '+%F %T')"
