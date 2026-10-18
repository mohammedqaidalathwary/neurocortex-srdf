# S07 Cohort Reconciliation

**Protocol SHA-256:** `c78b78ed48ea3e00d1e1c9f63ace246485fff8657164061aded5fdeb8febd525`

## Candidate-to-analysis accounting

| Stage | N | Interpretation |
|---|---:|---|
| Cohort R candidates | 131 | Protocol-derived candidate cohort |
| Full pipeline loss | 33 | No complete arm evaluation was produced |
| Successfully analyzed | 98 | 131 candidates minus 33 full losses |
| A3 applicable among analyzed | 40 | SMOTENC can run because categorical predictors remain at runtime |
| A3 not applicable among analyzed | 58 | Successfully analyzed by the other arms, but no categorical predictor remains for A3 |

The accounting identity is **131 = 33 + 98**. The 58 A3-not-applicable datasets are part of the 98 analyzed datasets and must not be counted as additional full losses.

## Full-loss categories

| Category | Unique datasets | Consequence |
|---|---:|---|
| `no_numeric_runtime` | 13 | Full pipeline loss: the notebook exits before evaluating the model arms |
| `cardinality_exceeded` | 15 | Full pipeline loss under the recorded cardinality/runtime rule |
| `download_failure` | 5 | Dataset unavailable for complete evaluation |
| **Total full loss** | **33** | Matches 131 − 98 |

The 38 rows in `logs/deviations.csv` are deviation entries, not 38 unique lost datasets. The five `armL_download_failure` entries relate to the exploratory Arm L and overlap underlying download failures; they are not counted as additional unique cohort losses.

## Confirmatory sample sizes

- H1, H2_CSRF, H2_EE, H4_CSRF, and H4_EE: n = 98.
- H2_SMOTE and H4_SMOTE: n = 40, because A3 is applicable only to those 40 successfully analyzed datasets with categorical predictors at runtime.

The 13 `no_numeric_runtime` cases are full losses from the analysis pipeline. The A3-specific non-applicability count is 58, not 13.
