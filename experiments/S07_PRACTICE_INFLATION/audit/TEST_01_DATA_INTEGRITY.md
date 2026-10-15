# TEST 1 — Data Integrity (corrected)

**Verdict: PASS**

| Check | Result | Detail |
|---|---|---|
| protocol_hash_unchanged | PASS | c78b78ed48ea3e00... |
| cohort_pool_hash_unchanged | PASS | recomputed=8242993572eda3f5... vs manifest=8242993572eda3f5... |
| cohort_ids_match_manifest | PASS | n_csv=131, n_manifest=131 |
| case_keys_unique | PASS | duplicates = 0 |
| arm_A1_row_count | PASS | 980 rows (expected 980) |
| arm_A2_row_count | PASS | 980 rows (expected 980) |
| arm_A4_row_count | PASS | 980 rows (expected 980) |
| arm_A5_row_count | PASS | 980 rows (expected 980) |
| arm_A6_row_count | PASS | 980 rows (expected 980) |
| arm_A7_row_count | PASS | 980 rows (expected 980) |
| arm_A3_row_count | PASS | 400 rows (expected 400) |
| datasets_analyzed | PASS | 98 |
| no_nan_in_critical_columns | PASS |  |
| deviations_log_exists | PASS | logs/deviations.csv |