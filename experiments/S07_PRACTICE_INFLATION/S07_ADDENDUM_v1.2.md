# S07 -- Addendum v1.2: A3 Applicability Clarification

**Parent:** S07_ADDENDUM_v1.1.md
**Protocol SHA-256:** `c78b78ed48ea3e00d1e1c9f63ace246485fff8657164061aded5fdeb8febd525`
**Date:** 2026-10-17
**Status:** Documentation-only; no locked artifact modified

---

## Purpose

An independent review of `S07_ADDENDUM_v1.1.md` raised a legitimate
question about the apparent inconsistency between:

1. The declared "numeric-only" set in `cohort_R_candidates.csv`
   (`has_categorical = False`, 65 datasets)
2. The SMOTENC applicability rule that governs arm A3

This addendum clarifies the distinction and confirms that all data
and results are consistent. It adds no modifications to any locked
artifact and does not change any confirmatory outcome.

---

## 1. Two distinct mechanisms in S07

S07 handles two orthogonal distinctions that are easy to confuse:

| Mechanism | Definition | Effect | Recorded where |
|---|---|---|---|
| **Full loss** | A dataset cannot be processed by any arm | Removed from the analyzed cohort | `logs/deviations.csv` |
| **A3 applicability** | A dataset has no categorical predictor at runtime | Excluded from A3 only; still analyzed in A1, A2, A4, A5, A6, A7 | `cases.csv.gz` with `reason='no_categorical_predictors'` |

These are independent. A dataset can be:

- Fully lost AND non-applicable (rare)
- Fully lost but A3-applicable (e.g., download failure)
- Analyzed but A3-non-applicable (58 datasets)
- Analyzed and A3-applicable (40 datasets)

---

## 2. has_categorical is informational, not a filter

The notebook Cell 3 explicitly documents this:

> Adds an informational flag "has_categorical" used later by the
> moderator analysis and to determine SMOTENC applicability.
> This flag is not a filter.

`has_categorical` is derived from the **OpenML snapshot metadata**
(`openml_metadata_snapshot.csv`). It reflects whether the snapshot
declares any symbolic features -- not whether, after download and
column-cardinality filtering, any categorical predictor remains.

---

## 3. A3 applicability is determined at runtime

A3 uses SMOTENC, which requires at least one categorical column.
Applicability is evaluated per split at runtime by `split_cols(X)`
(notebook Cell 5), which classifies columns by actual pandas dtype:

    def split_cols(X):
        cat_cols = [c for c in X.columns
                    if str(X[c].dtype) in ("object", "category", "string", "bool")]
        num_cols = [c for c in X.columns if c not in cat_cols]
        return num_cols, cat_cols

The rule is dtype-based on the **downloaded** data. This is
confirmed by `audit/TEST_03_LEAKAGE.md`:

> A3 (SMOTENC) availability is determined at runtime by split_cols
> on the actual downloaded data.

---

## 4. Reproducible verification

All numbers below are computed directly from `cases.csv.gz` and
`cohort_R_candidates.csv`.

### 4.1 A3 status distribution

| Status | Rows | Explanation |
|---|---|---|
| `SUCCESS` | 400 | 40 datasets x 5 folds x 2 repeats |
| `NOT_APPLICABLE` | 580 | 58 datasets x 5 folds x 2 repeats |
| **Total** | **980** | 98 analyzed datasets x 10 splits |

The reason string for every `NOT_APPLICABLE` row is
`no_categorical_predictors`.

### 4.2 Cross-check with confirmatory n

| Test | n_actual | n_reported | Match |
|---|---|---|---|
| H1 | 98 | 98 | yes |
| H2_SMOTE | 40 | 40 | yes |
| H2_CSRF | 98 | 98 | yes |
| H2_EE | 98 | 98 | yes |
| H4_SMOTE | 40 | 40 | yes |
| H4_CSRF | 98 | 98 | yes |
| H4_EE | 98 | 98 | yes |

Full table: `audit/S07_contrast_n_reconciliation.csv`.

### 4.3 Cohort reconciliation

| Stage | N | Source |
|---|---|---|
| Cohort R candidates | 131 | `cohort_R_candidates.csv` |
| Fully lost | 33 | 13 no_numeric + 15 cardinality + 5 download |
| Successfully analyzed | 98 | `cases.csv.gz` |
| Of which: A3-SUCCESS | 40 | have categorical predictors at runtime |
| Of which: A3-NOT_APPLICABLE | 58 | no categorical predictors at runtime |

The decomposition 131 = 98 + 33 is exact, with zero unexplained
losses. Full table: `audit/S07_dataset_arm_reconciliation.csv`.

---

## 5. Edge cases

Three datasets are declared `has_categorical=False` in the snapshot
yet show `A3 SUCCESS` at runtime:

| dataset_id | name | snapshot Num/Symb | runtime A3 |
|---|---|---|---|
| 43893 | ibm-employee-attrition | 26 / 0 | SUCCESS |
| 43895 | ibm-employee-performance | 25 / 1 | SUCCESS |
| 46595 | Thoracic_Surgery_Data | 3 / 0 | SUCCESS |

These are natural consequences of the runtime dtype-based rule.
The snapshot metadata is a coarse indicator; the actual pandas
dtype after download can differ. These cases do not constitute
errors and do not affect any confirmatory result.

---

## 6. Impact on published claims

| Claim | Before | After v1.2 |
|---|---|---|
| H1 SUPPORTED | yes | yes unchanged |
| H2_CSRF INFERIOR | yes | yes unchanged |
| H2_EE EQUIVALENT | yes | yes unchanged |
| H2_SMOTE INFERIOR (n=40) | yes | yes unchanged |
| H4 family EQUIVALENT | yes | yes unchanged |
| H3 descriptive | yes | yes unchanged |
| Scenario A achieved | yes | yes unchanged |
| Cohort reconciliation (131 = 98 + 33) | yes | yes clarified |

**No confirmatory result changes. No locked artifact changes.**

---

## 7. Data and evidence

- `audit/S07_contrast_n_reconciliation.csv` -- per-test n verification
- `audit/S07_dataset_arm_reconciliation.csv` -- dataset x arm status
- `audit/S07_a3_not_applicable_58.csv` -- the 58 A3-excluded datasets
- `audit/S07_a3_success_40.csv` -- the 40 A3-applicable datasets
- `audit/S07_lost_33_features.csv` -- the 33 fully-lost datasets

---

## 8. Conclusion

The apparent inconsistency reported during review is resolved by
recognizing two orthogonal distinctions:

1. `has_categorical` is an informational snapshot flag, not a filter.
2. A3 applicability is a runtime, dtype-based property of the
   downloaded data.

Under these two rules, every number in the S07 report is
reproducible, every confirmatory contrast matches its reported n,
and the cohort reconciliation 131 = 98 + 33 is exact. No locked
artifact requires modification and no confirmatory claim changes.
