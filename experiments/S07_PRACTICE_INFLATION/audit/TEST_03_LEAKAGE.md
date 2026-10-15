# TEST 3 — Leakage Audit (runtime-aware)

**Verdict: PASS**

| Check | Result | Detail |
|---|---|---|
| ordinal_encoding_declared | PASS | Ordinal encoding declared in protocol. |
| fit_on_training_fold_only | PASS | Preprocessing restricted to training fold. |
| pi_hat_definition_from_training | PASS | pi_hat computed from training partition. |
| t_cv_from_inner_split | PASS | A6 threshold from inner-validation split only. |
| t_star_diagnostic_only | PASS | A7 flagged as diagnostic upper bound. |
| arm_counts_are_6_or_7 | PASS | observed: [6, 7] |
| arm_count_uniform_within_dataset | PASS | 98 / 98 datasets uniform |
| per_dataset_arm_count_matches_a3_presence | PASS | 6 for no-A3, 7 for A3, uniformly within each dataset |
| two_repeats_per_dataset | PASS |  |
| five_folds_per_repeat | PASS |  |

**Note:** A3 (SMOTENC) availability differs from the S04 snapshot's
`has_categorical` flag because the runtime pipeline detects actual
categorical columns in the downloaded data after cleaning.