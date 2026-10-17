# S07 — A3 Edge Cases Evidence

**Context:** Three datasets (43893, 43895, 46595) are declared
`has_categorical=False` in the OpenML snapshot yet succeeded in A3
(SMOTENC) at runtime. This document provides direct evidence from
re-fetching and re-applying the runtime rule.

**Method:** Each dataset was re-fetched from OpenML and `split_cols(X)`
(notebook Cell 5, exact replica) was applied to the downloaded data.

## Results

| dataset_id | rows × cols | numeric cols | categorical cols (runtime) | A3 applicable |
|---|---|---|---|---|
| 43893 | 1470 × 34 | 26 | 8 | True |
| 43895 | 1470 × 33 | 25 | 8 | True |
| 46595 | 470 × 16 | 3 | 13 | True |

## Interpretation

In each case, the runtime dtype-based rule detected at least one
categorical predictor that the snapshot metadata did not reflect.
This is consistent with the documented behavior:

1. `has_categorical` is an informational snapshot flag, not a filter.
2. A3 applicability is determined at runtime by `split_cols`.

These cases are not errors; they are the expected consequence of the
two-rule design.
