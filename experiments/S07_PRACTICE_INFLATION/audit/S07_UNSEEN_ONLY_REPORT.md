# S07 — Unseen-Only Sensitivity Analysis

**Protocol basis:** `protocol_lock.json` → `cohort.sensitivity_unseen_only = true`
**Analysis date:** 2026-10-17
**Classification:** EXPLORATORY (N = 60 < N_req = 70, per protocol)

## Method

Datasets analyzed in S04, S05, or S06 were flagged as "seen-before" using
the union of their cohort manifests. The S07 confirmatory analysis was then
re-run on the remaining subset.

- Seen-before union (S04 ∪ S05 ∪ S06): 243 datasets
- S07 analyzed: 98 datasets
- Overlap: 38 datasets
- **Unseen subset: 60 datasets**

Per protocol: *"If cohort size is below N_req, status is EXPLORATORY."*
Since 60 < 70, this analysis is classified as exploratory.

## Results

| Test | Full (n=98) | Unseen (n=60) | Direction |
|---|---|---|---|
| H1 (A2−A1) | +0.0976 | +0.0794 | Preserved |
| H2_CSRF (A4−A2) | −0.1071 | -0.0878 | Preserved |
| H2_EE (A5−A2) | +0.0074 | +0.0091 | Preserved |
| H2_SMOTE (A3−A2) | −0.0365 | -0.0365 | Preserved |

H1 unseen: mean = +0.0794, CI95 = [+0.0614, +0.0973],
sign-flip p = 0.0000, effect size dz = 1.12.

## Interpretation

The direction of every confirmatory finding is preserved in the unseen
subset. **Threshold inflation (H1) is not an artifact of dataset reuse.**

## Limitation

Because N = 60 < N_req = 70, this analysis cannot strengthen
the confirmatory claim. It serves as robustness evidence.

## Data

`audit/S07_unseen_only_sensitivity.json`
`audit/S07_seen_before_manifest.csv`
