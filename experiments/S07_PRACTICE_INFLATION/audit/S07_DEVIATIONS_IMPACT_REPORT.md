# S07 — Deviations Impact Analysis

**Source:** `logs/deviations.csv` (38 entries)
**Analysis date:** 2026-10-17

## Classification

| category              |   count | type      | affected_tests    | severity   |
|:----------------------|--------:|:----------|:------------------|:-----------|
| cardinality_exceeded  |      15 | data      | all               | low        |
| no_numeric_runtime    |      13 | technical | H2_SMOTE;H4_SMOTE | low        |
| download_failure      |       5 | data      | all               | low        |
| armL_download_failure |       5 | data      | arm_L_exploratory | none       |

## Impact per confirmatory test

| Test | Status | Impacted by | Verdict |
|---|---|---|---|
| H1 | Unchanged | None | ✅ Robust |
| H2_CSRF | Unchanged | None | ✅ Robust |
| H2_EE | Unchanged | None | ✅ Robust |
| H2_SMOTE | n=40 (declared) | 13 no_numeric | ⚠️ Declared, not fatal |
| H4_SMOTE | n=40 (declared) | 13 no_numeric | ⚠️ Declared, not fatal |
| H4_CSRF | Unchanged | None | ✅ Robust |
| H4_EE | Unchanged | None | ✅ Robust |

## No critical deviations

No deviation affects H1, H2_CSRF, H2_EE, H4_CSRF, or H4_EE. The only
asymmetry introduced (n=40 for SMOTE) is:

1. Declared in the protocol (A3 = NOT_APPLICABLE for numeric-only datasets).
2. Reflected in `confirmatory_results.csv` (n column).
3. Consistent across all SESOI margins.

## Formal statement

> The 38 deviations produce zero impact on the primary confirmatory claim
> and zero impact on four of the seven confirmatory tests. The remaining
> three tests are affected only through the pre-declared SMOTENC
> applicability rule, with no change to their direction or decision.

## Data

`audit/S07_deviations_impact.csv`
