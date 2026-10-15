# S07 — Practice Inflation — Final Report

**Does class-imbalance correction beat a threshold-corrected control?**

**A catalog-wide confirmatory study of benchmark-practice bias.**


| Item | Value |
|---|---|
| Study ID | `S07-PRACTICE-INFLATION` |
| Protocol version | 1.1 |
| Protocol SHA-256 | `c78b78ed48ea3e00d1e1c9f63ace246485fff8657164061aded5fdeb8febd525` |
| Pre-registration DOI | `10.5281/zenodo.23404802` |
| Zenodo URL | https://doi.org/10.5281/zenodo.23404802 |
| Declared status | **CONFIRMATORY** |
| Cohort R derived | 131 datasets |
| Cohort R analyzed | 98 datasets |
| N_req | 70 |
| SESOI | 0.02 bAcc |
| alpha | 0.05 |
| Family size | 7 tests (H1, H2×3, H4×3) |
| Multiplicity | Holm |
| Merkle root | `d48271da7b7e16e48767e036ba8239d7236ee8d386cb6a7d366a74d152de1e23` |
| Overall audit | **PASS** |

## Research question

In the standard benchmark practice, rebalancing methods are compared against a plain classifier decided at the default 0.5 threshold, using balanced accuracy. How much of the reported benefit is an artifact of that control?

## Exact identity (no distributional assumptions)

```
Delta_conv(m) = Delta_mat(m) + Delta_thr
```

## Confirmatory family (Holm-corrected, m = 7)

| test | arm_a | arm_b | metric | n | mean | ci_lo | ci_hi | p_raw | p_holm | effect_size_dz | decision |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H1 | A2 | A1 | bacc | 98 | 0.0976 | 0.0824 | 0.1132 | 0.0000 | 0.0001 | 1.2324 | SUPPORTED |
| H2_SMOTE | A3 | A2 | bacc | 40 | -0.0365 | -0.0500 | -0.0234 | 0.9902 | 1.0000 | -0.8306 | INFERIOR |
| H2_CSRF | A4 | A2 | bacc | 98 | -0.1071 | -0.1230 | -0.0912 | 1.0000 | 1.0000 | -1.3137 | INFERIOR |
| H2_EE | A5 | A2 | bacc | 98 | 0.0074 | 0.0032 | 0.0121 | 0.0000 | 0.0001 | 0.3243 | EQUIVALENT |
| H4_SMOTE | A3 | A1 | auc | 40 | -0.0059 | -0.0164 | 0.0033 | 0.0043 | 0.0128 | -0.1797 | EQUIVALENT |
| H4_CSRF | A4 | A1 | auc | 98 | -0.0028 | -0.0054 | -0.0003 | 0.0000 | 0.0001 | -0.2140 | EQUIVALENT |
| H4_EE | A5 | A1 | auc | 98 | 0.0012 | -0.0018 | 0.0043 | 0.0000 | 0.0001 | 0.0785 | EQUIVALENT |


**Decision summary:** EQUIVALENT = 4, INFERIOR = 2, SUPPORTED = 1

## H3 — Ranking reversal (descriptive, no p-value)

| method | n | winflip_rate | winflip_ci_lo | winflip_ci_hi | conv_mean | mat_mean | label |
|---|---|---|---|---|---|---|---|
| SMOTE | 40 | 0.4250 | 0.2750 | 0.5750 | 0.0330 | -0.0365 | reversed |
| CSRF | 98 | 0.0306 | 0.0000 | 0.0714 | -0.0095 | -0.1071 | none |
| EE | 98 | 0.7041 | 0.6122 | 0.7959 | 0.1050 | 0.0074 | attenuated |


## Moderator analysis (HC3 OLS, exploratory)

| term | coef | se | p |
|---|---|---|---|
| Intercept | -0.0092 | 0.0373 | 0.8060 |
| log_ir | 0.0661 | 0.0176 | 0.0002 |
| minority_count | -0.0000 | 0.0000 | 0.4183 |
| cat_share | -0.0653 | 0.1267 | 0.6061 |
| log_ir:cat_share | 0.0093 | 0.0763 | 0.9029 |


## Sensitivity analysis

| test | metric | n | mean | median | trimmed_mean_10pct | wilcoxon_p_two_sided |
|---|---|---|---|---|---|---|
| H1 | bacc | 98 | 0.0976 | 0.0804 | 0.0924 | 0.0000 |
| H2_SMOTE | bacc | 40 | -0.0365 | -0.0324 | -0.0342 | 0.0000 |
| H2_CSRF | bacc | 98 | -0.1071 | -0.0916 | -0.1024 | 0.0000 |
| H2_EE | bacc | 98 | 0.0074 | 0.0060 | 0.0056 | 0.0006 |
| H4_SMOTE | auc | 40 | -0.0059 | -0.0040 | -0.0032 | 0.0911 |
| H4_CSRF | auc | 98 | -0.0028 | -0.0004 | -0.0027 | 0.0181 |
| H4_EE | auc | 98 | 0.0012 | -0.0000 | 0.0007 | 0.9734 |


## Arm L — Logistic Regression (exploratory)

| contrast | n | mean | sd | ci_lo | ci_hi | p_greater_vs_SESOI | p_tost | effect_size_dz |
|---|---|---|---|---|---|---|---|---|
| H1_LR (A2_LR - A1_LR, bacc) | 98 | 0.1216 | 0.0836 | 0.1058 | 0.1383 | 0.0000 | 1.0000 | 1.4444 |
| H2_CSRF_LR (A4_LR - A2_LR, bacc) | 98 | 0.0029 | 0.0144 | 0.0003 | 0.0060 | 1.0000 | 0.0000 | 0.2005 |
| A6_LR - A2_LR (bacc) | 98 | -0.0072 | 0.0182 | -0.0108 | -0.0036 | 1.0000 | 0.0000 | -0.3916 |
| REF H1_RF (A2 - A1, bacc) | 98 | 0.0976 | 0.0786 | 0.0824 | 0.1134 | 0.0000 | 1.0000 | 1.2324 |
| REF H2_CSRF_RF (A4 - A2, bacc) | 98 | -0.1071 | 0.0809 | -0.1229 | -0.0914 | 1.0000 | 1.0000 | -1.3137 |


The direction of H1 (threshold inflation) is consistent between RF (+0.098) and LR (+0.122). The mechanism is not specific to Random Forest. H2_CSRF differs: for LR, cost-sensitive learning acts as a threshold adjustment and is equivalent to the corrected control; for RF, balanced_subsample changes the ensemble structure and is inferior.

## Arm B — SRDF threshold re-reading (interpretive)

| cohort | system | n_cases | delta_conv_mean | delta_corrected_mean | delta_thr_mean | flips |
|---|---|---|---|---|---|---|
| S04 | SRDF | 375 | 0.0289 | -0.0654 | 0.0937 | 187 |
| S06 | SRDF v1 | 587 | 0.0514 | -0.1090 | 0.1605 | 442 |
| S06 | SRDF v2 | 587 | 0.0632 | -0.0671 | 0.1605 | 263 |
| S06 | SRDF v3 | 587 | 0.0752 | -0.0847 | 0.1605 | 452 |
| S06 | SRDF v4 | 587 | 0.1578 | -0.0027 | 0.1605 | 239 |


**Note:** S04 cases: 373 usable (2 excluded for missing SRDF result). S06 cases: 587 usable (13 excluded for baseline mismatch, all reported in `audit/TEST_04_S06_EXCLUSIONS.csv`). The unit of inference for Arm B is the dataset (15 for S04, 24 for S06); case counts are descriptive.

## Leave-One-Dataset-Out robustness

| contrast | lodo_min | lodo_max |
|---|---|---|
| H1 | 0.0955 | 0.0989 |
| H2_CSRF | -0.1084 | -0.1053 |
| H2_EE | 0.0059 | 0.0078 |
| H2_SMOTE | -0.0389 | -0.0340 |
| H4_CSRF | -0.0034 | -0.0025 |
| H4_EE | 0.0008 | 0.0017 |


All contrasts retain their sign across every single-dataset exclusion. The sign of every confirmatory finding is stable.

## Forensic validation (12 tests, all PASS)

| test | verdict |
|---|---|
| DATA_INTEGRITY | PASS |
| INDEPENDENT_RECOMPUTATION | PASS |
| LEAKAGE_AUDIT | PASS |
| ARMB_FAIRNESS | PASS |
| INFERENCE_AUDIT | PASS |
| EQUIVALENCE_AUDIT | PASS |
| IDENTITY_DELTA_CONV | PASS |
| DEPENDENCE_AUDIT | PASS |
| LEAVE_ONE_DATASET_OUT | PASS |
| ARML_AUDIT | PASS |
| MODERATOR_AUDIT | PASS |
| CLAIMS_TO_EVIDENCE | PASS |


## Declared limitations

- The study does not claim SRDF is better or worse than any baseline. SRDF appears only as one documented instance of the practice under test.
- No claim extends beyond RF-based pipelines and OpenML binary tabular datasets within the declared size range.
- Results are not extrapolated to missingness above 5%, to datasets with IR < 3, or to F1 / PR-AUC.
- The hypotheses are not blind: S05/S06 data already suggest the direction of H1. This is disclosed, and the design is built so that the other outcomes remain meaningful.
- OpenML metadata and datasets can change after the snapshot; content hashes of every fetched dataset are recorded for audit.

## Success criteria

**Definition:** A clean execution plus a determinate (non-inconclusive) resolution of H1 and of H2/H4 for at least two of the three methods.

- **Scenario A:** Inflation is confirmed (H1 supported) and rebalancing is equivalent or inferior to the threshold-corrected control (H2 returns equivalence or inferiority for at least two of three methods).
- **Scenario B:** Inflation is confirmed but a residual benefit exists in defined regimes (H1 supported, H2 returns superiority for at least one method).
- **Scenario C:** H1 is not supported. The conventional control is adequate on this cohort. This is itself a methodological result.

### Achieved scenario

**Scenario A** — Inflation is confirmed, and at least two of three rebalancing methods are equivalent or inferior to the threshold-corrected control. **Achieved.**

## Data availability

The complete S07 output is deposited on Zenodo at DOI `10.5281/zenodo.23404802` (pre-registration) and at the results DOI (to be added after deposit).

Protocol SHA-256: `c78b78ed48ea3e00d1e1c9f63ace246485fff8657164061aded5fdeb8febd525`. Merkle root of the output: `d48271da7b7e16e48767e036ba8239d7236ee8d386cb6a7d366a74d152de1e23`.
