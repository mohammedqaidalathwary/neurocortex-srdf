# S05 - Extended Comparative Evaluation

## Purpose
Compare SRDF v1 (frozen in S04) against four external baselines on the same cohort
used in S04. Provide statistical comparisons, a counterfactual analysis of the
Arbiter, and a decomposition of its failure modes.

## Protocol
- Cohort     : 45 OpenML datasets from S04 (frozen)
- Cases      : 1125 = 45 datasets x 5 seeds x 5 folds
- Seeds      : [11, 23, 37, 53, 71]
- Trigger    : train_IR >= 3.0
- Metric     : balanced accuracy on held-out test fold
- Baselines  : SMOTE+RF, Cost-Sensitive RF, ADASYN+RF, EasyEnsemble

The complete protocol is stored in protocol/S05_PROTOCOL.json and locked with
SHA-256 in protocol/S05_protocol_lock.json.

## Directory contents

    S05_EXTENDED_EVALUATION/
    |-- protocol/
    |   |-- S05_PROTOCOL.json            Protocol definition
    |   `-- S05_protocol_lock.json       SHA-256 hash
    |-- baselines/
    |   |-- smote_rf.jsonl               1125 cases
    |   |-- cost_sensitive_rf.jsonl      1125 cases
    |   |-- adasyn_rf.jsonl              1125 (817 COMPLETE, 308 SKIPPED)
    |   `-- easyensemble.jsonl           1125 cases
    |-- baselines_triggered_only/
    |   `-- *_triggered.jsonl            Same methods on 375 triggered only
    |-- cohort_reuse/
    |   |-- triggered_keys.json          The 375 triggered case keys
    |   |-- srdf_full_1125.jsonl         SRDF system view
    |   `-- srdf_triggered_375.jsonl     SRDF conditional view
    `-- analysis/
        |-- baselines_summary.json
        |-- statistical_comparisons.json
        |-- counterfactual_arbiter.json
        |-- three_view_comparison.json
        |-- threshold_sensitivity.json
        |-- distributional.json
        |-- loo_wilcoxon.json
        |-- error_analysis.json
        `-- negative_delta_decomposition.json

## Key results

### View A - System (1125 cases, full behavioral policy)

    Method              Mean bAcc
    -----------------------------
    EasyEnsemble        0.8351
    ADASYN+RF (n=817)   0.8290
    SMOTE+RF            0.8163
    SRDF v1             0.8076
    Cost-Sensitive RF   0.7933

### View B - Conditional (375 triggered cases, matched scope)

    Method              Mean bAcc
    -----------------------------
    EasyEnsemble        0.8684
    SMOTE+RF            0.8112
    ADASYN+RF (n=350)   0.7941
    SRDF v1             0.7919
    Cost-Sensitive RF   0.7515

### View C - Counterfactual Arbiter (373 SUCCESS cases)

    Policy                        Mean bAcc
    ----------------------------------------
    SRDF actual (Arbiter-driven)  0.7928
    Fixed always-SMOTE+RF         0.8122
    Arbiter net cost              -0.0193

Statistical significance: p_holm = 0.0026, Cohen d = -0.76,
95% bootstrap CI [-0.0330, -0.0083].

### Failure decomposition (82 negative-delta SUCCESS cases)

    Mode | Definition                    | n
    -----|-------------------------------|-----
    A    | utility tied AND loss         | 20
    B    | utility decisive AND loss     | 62
    C    | utility decisive AND gain     | 229

Mode B cases have higher mean train_IR (8.86) than the full SUCCESS set,
indicating the utility signal degrades at severe imbalance.

## Hypotheses and outcomes
S05 is exploratory/comparative. No confirmatory hypotheses were declared.
Findings are reported as empirical facts.

## Findings
- F-S05-01: The Arbiter selection policy underperforms a fixed always-SMOTE+RF
  policy by 1.93 pp on the 373 SUCCESS cases.
- F-S05-02: 82 negative-delta SUCCESS cases decompose into Mode A (tied utility,
  20 cases) and Mode B (decisive utility, 62 cases, concentrated on high-IR datasets).
- F-S05-03: SRDF v1 ranks fourth among five methods on both View A and View B.

## Ablations status
Ablations were declared in the protocol (no_arbiter, forced_trigger, gb_only,
smote_only) but were not executed as separate runs in S05. Their scientific
questions are covered by S06 evidence. See
experiments/_AUDIT/S05_ABLATIONS_STATUS.json for the documented status.

## Limitations
- Baselines require OpenML availability.
- ADASYN declined generation on 13 of 45 datasets; 308/1125 cases were recorded
  as SKIPPED (documented behavior, not errors).
- The counterfactual uses S05 baseline scores; no re-execution of SMOTE+RF was
  performed.
- SRDF is evaluated as an end-to-end system; mean performance is affected by
  both trigger frequency and Arbiter decisions.

## Related links
- GitHub commit     : a7407c7
- Verification ZIP  : S05_verification_package.zip
- Next phase        : S06 (Arbiter Revision Suite)

## Interpretation guide
SRDF v1 does not outperform established baselines on this cohort. Its Arbiter
actively reduces performance relative to a fixed policy. This is the central
negative result that motivates S06.
