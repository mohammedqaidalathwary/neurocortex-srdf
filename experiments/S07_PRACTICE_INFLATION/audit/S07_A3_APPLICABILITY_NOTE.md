# S07 A3 Applicability Note

**Context:** Arm A3 is SMOTENC + RF. This note documents how A3
applicability is determined and why the reported n for A3-based
contrasts is 40 rather than 98.

## Rule

A3 applies to a dataset if and only if, after download and
column-cardinality filtering, at least one categorical predictor
remains. This is evaluated per split at runtime by `split_cols(X)`
(notebook Cell 5), which classifies columns by actual pandas dtype.

## Counts

| Category | Count | Source |
|---|---|---|
| Analyzed datasets | 98 | `cases.csv.gz` |
| A3 SUCCESS | 40 | `cases.csv.gz` |
| A3 NOT_APPLICABLE | 58 | `cases.csv.gz` |
| Reason string | `no_categorical_predictors` | in every NOT_APPLICABLE row |

## Protocol declaration

`protocol_lock.json` declares A3 as:

    "SMOTENC+RF (numeric-only datasets: NOT_APPLICABLE)"

This is a pre-declared applicability rule, not an unanticipated
exclusion.

## Why this is not a data loss

The 58 A3-excluded datasets are analyzed in all other arms
(A1, A2, A4, A5, A6, A7). They contribute fully to H1, H2_CSRF,
H2_EE, H4_CSRF, H4_EE, and to Arm L. They affect only the SMOTE
contrasts (H2_SMOTE, H4_SMOTE), whose n is correctly reported as 40.

## Relationship to has_categorical

`has_categorical` in `cohort_R_candidates.csv` is an informational
snapshot flag (see notebook Cell 3: "This flag is not a filter").
It reflects the OpenML snapshot, not the runtime dtype. The two
can differ; only the runtime dtype governs A3.

## Evidence

- `audit/S07_dataset_arm_reconciliation.csv`
- `audit/S07_contrast_n_reconciliation.csv`
- `audit/S07_a3_not_applicable_58.csv`
- `audit/S07_a3_success_40.csv`
