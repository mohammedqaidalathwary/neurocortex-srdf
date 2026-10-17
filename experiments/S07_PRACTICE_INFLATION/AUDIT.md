# S07 — Final Forensic Audit

**Audit UTC:** 2026-10-15T23:08:33.829469+00:00
**Protocol SHA-256:** `c78b78ed48ea3e00d1e1c9f63ace246485fff8657164061aded5fdeb8febd525`
**Pre-registration DOI:** 10.5281/zenodo.23404802
**Merkle root:** `d48271da7b7e16e48767e036ba8239d7236ee8d386cb6a7d366a74d152de1e23`
**Overall:** **PASS**

## Integrity checks

| Check | Result | Detail |
|---|---|---|
| protocol_hash_matches_lock | PASS | c78b78ed48ea3e00... vs c78b78ed48ea3e00... |
| sub_artifact_cohort_R_candidates | PASS | 3d65296bc71825d9... |
| sub_artifact_cohort_R_manifest | PASS | fc9d2e5670bff35a... |
| sub_artifact_environment | PASS | 412576dbddd26826... |
| merkle_root_computed | PASS | d48271da7b7e16e48767e036ba8239d7... |
| signflip_reproducible | PASS | p=0.0000999900 |
| percentile_ci_reproducible | PASS | 0.082227 - 0.113172 |
| identity_holds_on_confirmatory | PASS | max residual = 0.00e+00 |
| deviations_logged | PASS | 38 entries |

## Forensic validation tests

| Test | Verdict |
|---|---|
| DATA_INTEGRITY | PASS |
| INDEPENDENT_RECOMPUTATION | PASS |
| LEAKAGE_AUDIT | PASS |
| ARMB_FAIRNESS | PASS |
| INFERENCE_AUDIT | PASS |
| EQUIVALENCE_AUDIT | PASS |
| IDENTITY_DELTA_CONV | PASS |
| DEPENDENCE_AUDIT | PASS |
| LEAVE_ONE_DATASET_OUT | PASS |
| ARML_AUDIT | PASS |
| MODERATOR_AUDIT | PASS |
| CLAIMS_TO_EVIDENCE | PASS |

## File manifest

Total files: **50**  
Total bytes: **847,990**

| Path | SHA-256 (short) | Bytes |
|---|---|---|
| `AUDIT.json` | `2aa89e6c7e68aa02...` | 10,253 |
| `AUDIT.md` | `e8a1af2cdea5fd99...` | 4,710 |
| `S07_PREREGISTRATION/PACKAGE_MANIFEST.json` | `c02feccb04f052ec...` | 1,130 |
| `S07_PREREGISTRATION/PRE_REGISTRATION_README.md` | `70c3debc4038391b...` | 1,845 |
| `S07_PREREGISTRATION/cohort_R_candidates.csv` | `3d65296bc71825d9...` | 13,134 |
| `S07_PREREGISTRATION/cohort_R_manifest.json` | `fc9d2e5670bff35a...` | 2,631 |
| `S07_PREREGISTRATION/environment.json` | `412576dbddd26826...` | 497 |
| `S07_PREREGISTRATION/execution_plan.json` | `e27074f4079adfc4...` | 743 |
| `S07_PREREGISTRATION/protocol_lock.json` | `6a4ab5277abab93a...` | 8,221 |
| `S07_REPORT.md` | `83235d06486413e8...` | 7,890 |
| `audit/TEST_01_DATA_INTEGRITY.json` | `be34b93fe2b38192...` | 1,616 |
| `audit/TEST_01_DATA_INTEGRITY.md` | `48bed75a80565891...` | 879 |
| `audit/TEST_02_RECOMPUTATION.json` | `35e2e253d964f011...` | 1,766 |
| `audit/TEST_02_RECOMPUTATION.md` | `05bdeb1fda57ba99...` | 586 |
| `audit/TEST_03_LEAKAGE.json` | `be7368ad47326bb1...` | 1,534 |
| `audit/TEST_03_LEAKAGE.md` | `29461c6a20597b11...` | 1,006 |
| `audit/TEST_04_ARMB_FAIRNESS.json` | `a86a712cfd20054a...` | 1,673 |
| `audit/TEST_04_S04_MISSING_SRDF.csv` | `53f2fe351db0c877...` | 161 |
| `audit/TEST_04_S06_EXCLUSIONS.csv` | `ec8c776af12df07f...` | 1,297 |
| `audit/TEST_05_INFERENCE.json` | `75e5b0ff7d4abce8...` | 1,968 |
| `audit/TEST_06_EQUIVALENCE.json` | `7510ff483ace1d91...` | 1,272 |
| `audit/TEST_07_IDENTITY.json` | `133793043bdff5f9...` | 1,115 |
| `audit/TEST_07_IDENTITY.md` | `1a6e758d5c25abdd...` | 311 |
| `audit/TEST_09_DEPENDENCE.json` | `ddb2c5e7fd75c6bf...` | 1,058 |
| `audit/TEST_10_LODO.csv` | `e08e017905dcaafc...` | 21,326 |
| `audit/TEST_10_LODO.json` | `b602990cb3bf19ca...` | 1,229 |
| `audit/TEST_11_ARML.json` | `c73d9449c55be7c3...` | 1,105 |
| `audit/TEST_12_MODERATOR.json` | `6c9e44bfb80a321c...` | 2,676 |
| `audit/TEST_14_CLAIMS.json` | `6e6694988f2f1a78...` | 1,920 |
| `audit/TEST_14_CLAIMS.md` | `261883be1952b680...` | 1,277 |
| `cohort_R_manifest.json` | `fc9d2e5670bff35a...` | 2,631 |
| `environment.json` | `412576dbddd26826...` | 497 |
| `execution_plan.json` | `e27074f4079adfc4...` | 743 |
| `logs/deviations.csv` | `f49a7255daf4ef47...` | 3,188 |
| `pre_registration.json` | `260f89aeed96e6f2...` | 841 |
| `protocol_lock.json` | `6a4ab5277abab93a...` | 8,221 |
| `results_summary.json` | `68ab4c30d70b2b35...` | 11,421 |
| `tables/H3_winflip.csv` | `fb914e9fc719cb61...` | 721 |
| `tables/armB_S04_per_case.csv` | `f637b651bc169b02...` | 60,171 |
| `tables/armB_S06_per_case.csv` | `8766c99490cb14f0...` | 219,012 |
| `tables/armB_control_recomputed.csv` | `2668b65ae26c3608...` | 79,476 |
| `tables/armB_summary.csv` | `3acfd5ba0184a0a7...` | 484 |
| `tables/armL_analysis.csv` | `2d87db9f423bb52b...` | 879 |
| `tables/cases.csv.gz` | `1fc3bd519b3c644d...` | 136,725 |
| `tables/cases_LR.csv.gz` | `505ba2f3eefa6aee...` | 87,593 |
| `tables/cases_partial.csv.gz` | `6b63a8b67e1f8823...` | 123,015 |
| `tables/cohort_R_candidates.csv` | `3d65296bc71825d9...` | 13,134 |
| `tables/confirmatory_results.csv` | `ad95f80a19a30631...` | 1,270 |
| `tables/moderator_analysis.csv` | `326a334696e02815...` | 378 |
| `tables/sensitivity.csv` | `82a3b483e7025380...` | 761 |

## Determinism witness

- **signflip_reproducible**: PASS
- **percentile_ci_reproducible**: PASS

## Identity

`Delta_conv = Delta_mat + Delta_thr` max residual: `0.00e+00`

---

## Post-publication addendum (2026-10-17)

An addendum (v1.1) closes four documentation gaps identified during
independent review. It adds no changes to locked artifacts, confirmatory
results, or the parent report. See:

- `S07_ADDENDUM_v1.1.md`
- `audit/TEST_NUMBERING_NOTE.md`
- `audit/S07_RECONCILIATION.md`
- `audit/S07_UNSEEN_ONLY_REPORT.md`
- `audit/S07_SESOI_MARGINS_REPORT.md`
- `audit/S07_DEVIATIONS_IMPACT_REPORT.md`

**Clarification on forensic test numbering:** The 12 tests listed above are
the complete and final set. IDs 08 and 13 are unused labels, not omitted
tests. All 12 tests pass.
