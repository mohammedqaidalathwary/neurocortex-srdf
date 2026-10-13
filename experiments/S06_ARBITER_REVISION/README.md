# S06 - Arbiter Revision Suite

## Purpose
Revise the SRDF Arbiter in four sequential, pre-registered stages. Each stage
has its own protocol, locked before execution. The study tests whether targeted
modifications to the Arbiter improve framework-level performance, and whether
the framework adds measurable value beyond a fixed strong baseline.

## Stages
- v1 : SRDF original (frozen from S04)
- v2 : tie-break fix + balanced_accuracy utility (S06a)
- v3 : validation threshold recalibration 0.85 -> 0.75 (S06b)
- v4 : EasyEnsemble added as third candidate (S06c)

The confirmatory cohort (stage_198) was selected by applying the frozen S04
selection procedure to the remaining eligible universe after four declared
exclusion rules.

## Cohort
- Source     : S04 eligibility_table.csv (6434 datasets, 284 eligible)
- Exclusions : 45 S04 cohort + 226 remaining used in S06 stages
- Nested stages:
    stage_32  :  32 datasets
    stage_62  :  62 datasets
    stage_198 : 198 datasets (used for confirmatory runs)
- Cases      : 198 x 5 seeds x 5 folds = 4950
- Triggered  : 600 cases (24 datasets)

## Directory contents

    S06_ARBITER_REVISION/
    |-- protocol/
    |   |-- S06_PROTOCOL.json              Master protocol + lock
    |   |-- S06b_PROTOCOL.json             v3 protocol + lock
    |   |-- S06c_PROTOCOL.json             v4 protocol + lock
    |   |-- protocol_freeze_addendum.json  Hashes of frozen code
    |   |-- S06_ZENODO_DEPOSIT.json        Zenodo DOI + metadata
    |   |-- S06_confirmatory_decision.json stage_198 selection
    |   |-- S06_deviations.json            Empty (no deviations)
    |   `-- S06_pre_execution_notes.json
    |-- results/
    |   |-- s06_confirmatory_stage198.jsonl     v1, v2 + baselines
    |   |-- s06_confirmatory_stage198_v3.jsonl  v3 results
    |   |-- s06_confirmatory_stage198_v4.jsonl  v4 results
    |   `-- ee_standalone_stage198.jsonl        EE baseline
    |-- analysis/
    |   |-- s06a_confirm_results.json
    |   |-- s06b_finding_01.json
    |   |-- s06c_final_v1_v2_v3_v4.json
    |   |-- s06c_finding_01.json
    |   |-- power_analysis.json
    |   `-- threshold_analysis.json
    |-- cohort_reuse/
    |   |-- stage_32.json
    |   |-- stage_62.json
    |   |-- stage_198.json
    |   |-- s04_exclusion_sets.json
    |   `-- s06_remaining_after_exclusions.json
    `-- evidence/
        `-- src_v3_manifest.json           Code hashes

## Key results (framework-level means, 600 triggered cases)

    Version  | Mean delta (pp)
    ---------|----------------
    v1       | +0.0517
    v2       | +0.0382
    v3       | +0.0748
    v4       | +0.1577
    EE alone | +0.1673

## Hypotheses and outcomes

    Hypothesis                    | Result
    ------------------------------|--------
    H1 (v3 >= v1)                 | SUPPORTED (p=0.000025, d=+0.97)
    H2 (v3 >  v2)                 | SUPPORTED (p=0.000655, d=+0.94)
    H3 (v4 >  v3)                 | SUPPORTED (p<1e-6, d=+1.75)
    H4 (EE selected >= 30%)       | SUPPORTED (88.83%)
    H5 (v4 >= EE standalone)      | NOT SUPPORTED (v4 = EE - 0.95 pp)

## Findings
- F-S06a-01: The v2 threshold (0.85), calibrated for accuracy, became overly
  selective when utility switched to balanced_accuracy. Framework-level
  regression of -1.35 pp.
- F-S06b-01: Mathematical recalibration (u_min = 0.5 * 0.50 + 0.5 = 0.75)
  restored and exceeded v1 by +2.31 pp (p=0.000025, d=+0.97).
- F-S06c-01: When a dominant candidate (EasyEnsemble) is available, the Arbiter
  selects it in 88.83% of cases but harms on the remaining 11%. Net -0.95 pp
  versus always-selecting EasyEnsemble.

## Selection distribution (SUCCESS cases per version)

    Version | GB   | SMOTE | EasyEnsemble | Total
    --------|------|-------|--------------|-------
    v1      | 456  | 144   | -            | 600
    v2      | 112  | 246   | -            | 358
    v3      | 176  | 419   | -            | 595
    v4      |  21  |  46   | 533          | 600

## Limitations
- Single development cohort (stage_198, 24 triggered datasets).
- One dataset (id=1048) had a corrupted cache and is excluded from its
  respective analyses (recorded as DATA_ERROR).
- The Arbiter converges to EasyEnsemble but does not exceed it.
- Generalization to a fresh cohort is planned in S07.

## Related links
- GitHub commits:
    4157089 (v2)
    ca709d4 (v3)
    6e55d41 (v4)
- Zenodo DOI       : 10.5281/zenodo.23308347 (protocol deposit)
- Verification ZIPs: S06_v2_..., S06b_v3_..., S06_FULL_...

## How to read v1/v2/v3/v4 differences
- v1 -> v2 : signal change (accuracy -> balanced_accuracy) without threshold
             recalibration. Net negative.
- v2 -> v3 : threshold recalibration derived mathematically. Net positive.
- v3 -> v4 : candidate pool expansion (adds EasyEnsemble). Large positive.
- v4 vs EE : the Arbiter converges to EE but does not exceed it.

## Interpretation guide
This is the central study of the project. It shows that:
  (1) changing the utility signal without recalibrating the threshold harms
      framework performance,
  (2) a mathematically derived threshold restores and exceeds the baseline,
  (3) adding a dominant candidate boosts performance but reveals that the
      Arbiter adds no value beyond selecting that candidate.
