# Post-lock modification log (Phase 1 integrity audit)

Generated: 2026-10-29T02:31:55.288702+00:00

This log lists every file whose current SHA-256 differs from a hash recorded in a lock, manifest or audit file. The reasons below are supported by the Zenodo originals (Zenodo DOI 10.5281/zenodo.23406120).

| file | recorded in | recorded sha256 | current sha256 | reason | original restored from |
|---|---|---|---|---|---|
| `experiments/S07_PRACTICE_INFLATION/S07_REPORT.md` | S07 locked-hash list: S07_REPORT.md | `74eb441278fa6d5778f0286901dac484a80eb2ab4eb0ad0faa12cb6b4e3e00f9` | `b585126c7b08595877355dad14772e782a50d28fe54ff5e69e7bf07aeab56640` | Documentation-only changes across v1.1 and v1.2 addenda. Added notes on H2_EE margin sensitivity and S04 Arm B exclusions. Merkle root updated. No protocol, cohort, data, or confirmatory-result changes. | Zenodo DOI 10.5281/zenodo.23406120 |
| `experiments/S07_PRACTICE_INFLATION/AUDIT.json` | S07 AUDIT.json manifest: AUDIT.json | `2aa89e6c7e68aa023fc66a182b8df523fe631ff38a34f068a6aec4adcc66c53d` | `471e6d3f1202af735763b995b12a2beec71dbee874723001608161922652ec05` | Manifest update (self-referential hash field). Audit UTC, Merkle root, and manifest checks updated to reflect post-lock documentation changes. | Zenodo DOI 10.5281/zenodo.23406120 |
| `experiments/S07_PRACTICE_INFLATION/AUDIT.md` | S07 AUDIT.json manifest: AUDIT.md | `e8a1af2cdea5fd99739d828f137458b885ca3c5c70bc31564628e35dc18b8ee0` | `1a11bc321cf6ad0fdcc5ec54c03720dec6d00d4b19b7e7799fd5fb930f9c0d65` | Documentation-only update. Audit UTC and Merkle root updated to reflect the post-lock documentation changes. | Zenodo DOI 10.5281/zenodo.23406120 |
| `experiments/S07_PRACTICE_INFLATION/S07_REPORT.md` | S07 AUDIT.json manifest: S07_REPORT.md | `83235d06486413e82205ffd7c0c1be317b75729637b8b6e9e92fa133336d253c` | `b585126c7b08595877355dad14772e782a50d28fe54ff5e69e7bf07aeab56640` | Documentation-only changes across v1.1 and v1.2 addenda. Added notes on H2_EE margin sensitivity and S04 Arm B exclusions. Merkle root updated. No protocol, cohort, data, or confirmatory-result changes. | Zenodo DOI 10.5281/zenodo.23406120 |
| `experiments/S07_PRACTICE_INFLATION/results_summary.json` | S07 AUDIT.json manifest: results_summary.json | `68ab4c30d70b2b35fd5deffffa27ca96599ed53a59517b09817fbb6c4488f945` | `d961b42c591473c190c2ce12cc3e43f2369b1a8ef0fd1a1ff93aae5c666937ae` | Only merkle_root differs (auto-derived hash reflecting the documentation changes above). All numeric and content fields byte-identical to Zenodo. | Zenodo DOI 10.5281/zenodo.23406120 |
| `experiments/S07_PRACTICE_INFLATION/tables/armB_summary.csv` | S07 AUDIT.json manifest: tables/armB_summary.csv | `3acfd5ba0184a0a7e91f3107272f4272fe08f970f2a123fd88cc4cf0ec5e8fae` | `82a7f3c5fb6f3831870d7e13618c8c5c79d796dff90d96c4f44a6b41a646016a` | Added n_usable column. S04 delta_thr_mean corrected from 0.093747 to 0.094268 following exclusion of 2 non-usable cases (n_usable=373 vs n_cases=375). All other values and all S06 rows byte-identical. Confirmatory results unchanged. | Zenodo DOI 10.5281/zenodo.23406120 |

## Author statement

The files listed in the table above were modified after their hashes were recorded in the S07 lock files (S07_LOCKED_ARTIFACT_HASHES.json and AUDIT.json). All changes are documentation-only or corrective and did not alter any confirmatory quantity, decision, or confidence interval. This was independently verified as follows:

1. The original bytes of all six files are preserved in Zenodo DOI 10.5281/zenodo.23406120 (S07 Results, published 2026-10-16).
2. The two files that carry the confirmatory evidence — `tables/confirmatory_results.csv` and `tables/cases.csv.gz` — are byte-identical between the Zenodo archive and the current repository.
3. All deterministic quantities in the confirmatory table (n, mean, sd, Hedges' g with the 4n-9 correction) reproduce from `cases.csv.gz` to 1e-9 (Section 7 of the Phase 1 notebook).
4. All seven decision labels (SUPPORTED / INFERIOR / EQUIVALENT) reproduce from the reported confidence intervals and the pre-registered SESOI.
5. All twenty-two counts quoted in the S04-S07 documents match the underlying data (Section 8 of the Phase 1 notebook).

A reviewer can verify each point independently using the Zenodo archive and the raw data included in the repository.