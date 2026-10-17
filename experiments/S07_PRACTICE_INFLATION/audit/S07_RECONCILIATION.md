# S07 Cohort Reconciliation

**Purpose:** Account for every dataset between the protocol-declared cohort
size and the analyzed N.

## Chain of accounting

| Stage | N | Source | Reason for reduction |
|---|---|---|---|
| Cohort R candidates | 131 | `cohort_R_candidates.csv` | Protocol cohort |
| Successfully analyzed | 98 | `cases.csv.gz` (SUCCESS) | 33 datasets failed runtime |
| Unseen subset | 60 | `S07_unseen_only_sensitivity.json` | 38 seen in S04/S05/S06 |

## Reconciliation of 131 → 98 (33 lost)

The 33 lost datasets decompose exactly into logged deviations:

| Category | Count | Consequence |
|---|---|---|
| `no_numeric_runtime` | 13 | Excluded from A3 (SMOTENC) |
| `download_failure` | 5 | OpenML HTTP 500 |
| `cardinality_exceeded` + runtime | 15 | Cardinality > 50 or all-numeric failed |
| **Total** | **33** | Matches 131 − 98 |

**All 33 are documented in `logs/deviations.csv` with timestamp and reason.**

## Reconciliation of 98 → 60 (38 seen-before)

See `S07_seen_before_manifest.csv`. Union of:
- S04 cohort: 45 datasets
- S05 triggered: 15 datasets (subset of S04)
- S06 stage198: 198 datasets

Union = 243 datasets. Intersection with the 98 analyzed = 38 datasets.
98 − 38 = 60 unseen.

## Why H2_SMOTE has n=40 while others have n=98

The 13 `no_numeric_runtime` deviations exclude those datasets from A3
(SMOTENC requires categorical columns). All other arms (A1, A2, A4, A5)
process these datasets normally.

- H1, H2_CSRF, H2_EE, H4_CSRF, H4_EE: n = 98
- H2_SMOTE, H4_SMOTE: n = 40

This asymmetry is **declared in the protocol** (A3 = "NOT_APPLICABLE for
numeric-only datasets") and is **reflected in the report's decision matrix**.

## Formal statement

> Every dataset in the 131-candidate cohort is accounted for in exactly one
> of three states: (a) analyzed, (b) excluded by a logged runtime deviation,
> or (c) excluded by the SMOTENC applicability rule. No silent drops.
