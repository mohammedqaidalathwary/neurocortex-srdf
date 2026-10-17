# S07 — A3 Edge Cases Evidence

**Context:** Three datasets (43893, 43895, 46595) are declared
`has_categorical=False` in the OpenML snapshot yet succeeded in A3
(SMOTENC) at runtime. This document provides direct evidence from
re-fetching and re-applying the runtime rule.

**Method:** Each dataset was re-fetched from OpenML and `split_cols(X)`
(notebook Cell 5, exact replica) was applied to the downloaded data.

## Results

| dataset_id | rows x cols | numeric cols | categorical cols (runtime) | A3 applicable |
|---|---|---|---|---|
| 43893 | 1470 x 34 | 26 | 8 | True |
| 43895 | 1470 x 33 | 25 | 8 | True |
| 46595 | 470 x 16 | 3 | 13 | True |

## Interpretation

In each of the three datasets, the `has_categorical` field in the
snapshot metadata does not match the actual column-type detection at
runtime. This discrepancy must be read alongside the other metadata
fields that are available. In one case (43895), the snapshot records
`NumberOfSymbolicFeatures = 1`, indicating that some categorical
information was indeed present in the metadata, even though
`has_categorical` was set to `False`.

A3 applicability in these cases was determined by the runtime column
inspection (`split_cols`), not by the `has_categorical` field alone.

These cases do not constitute errors in the experiment results and do
not require re-execution. The conclusion is limited to the datasets
for which execution evidence is recorded.

## Data

- `S07_a3_edge_cases_evidence.csv` (this directory)
