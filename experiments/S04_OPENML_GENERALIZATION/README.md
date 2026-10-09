# S04 — OpenML Generalization (R4)

**Project**: NeuroCortex — Self-Reinforcing Development Framework (SRDF)  
**Phase identifier**: S04  
**Experiment**: NC-SRDF-R4  
**Protocol ID**: NC-S04-R4  
**Protocol version**: 1.0.0  
**Recorded run status**: COMPLETE  
**Last recorded run**: 2026-10-09  
**Repository branch**: main

> **Evidence note:** This README summarizes artifacts currently recorded in this directory. Reported counts and statistics are taken from the committed run summary and manifest. Updating this documentation does not independently rerun the experiment or validate every recorded artifact.

---

## 1. Purpose and Scope

S04 evaluates NeuroCortex SRDF on a preselected cohort of OpenML tabular binary-classification datasets. The protocol defines dataset eligibility and cohort selection, the execution design, the imbalance-ratio trigger, outcome statuses, and the statistical summaries.

The experiment is intended to provide auditable, bounded evidence about observed balanced-accuracy changes. Results from this experiment alone should not be interpreted as proof of general superiority across all datasets or settings.

---

## 2. Protocol at a Glance

The committed protocol specifies:

- **Data source**: OpenML dataset listings and dataset records.
- **Task**: Binary classification with numeric features, subject to the protocol's eligibility rules.
- **Final cohort**: 45 datasets.
- **Seeds**: 11, 23, 37, 53, 71.
- **Cross-validation**: 5 stratified folds per dataset and seed.
- **Planned cases**: 45 × 5 × 5 = 1,125.
- **Imbalance ratio**: Majority-class count divided by minority-class count. The execution-time trigger is calculated from the training partition only.
- **Trigger threshold**: `TRAIN_IR >= 3.0`.
- **Primary metric**: Balanced accuracy on the held-out test fold.
- **Candidate selection**: An inner validation split inside the training partition. The protocol explicitly avoids using `run_cycle` because its candidate evaluation uses the test split.
- **Primary delta analysis**: SUCCESS cases only. `NOT_TRIGGERED` cases are not treated as zero-delta observations.

The authoritative source for the full eligibility, cohort-selection, execution, and statistical rules is `protocol/R4_PROTOCOL.json`.

---

## 3. Recorded Execution Outcomes

According to `statistics/r4_summary.json`, the run records 1,125 terminal case records.

| Recorded status or quantity | Count |
|---|---|
| SUCCESS | 373 |
| NOT_TRIGGERED | 750 |
| REJECTED | 2 |
| Triggered cases | 375 |
| Cases with valid delta (SUCCESS only) | 373 |
| Recorded technical failure cases | 0 |
| Planned cases / terminal records | 1,125 |

**Interpretation:** `NOT_TRIGGERED` is a protocol-defined outcome, not a technical failure. The recorded zero in the failure count describes the committed summary; it should not be read as independent confirmation that no unrecorded execution or infrastructure problems occurred.

---

## 4. Recorded Statistical Results

The committed summary reports the following observed results:

| Analysis | n | Mean Δ balanced accuracy | 95% interval |
|---|---|---|---|
| Case-level, SUCCESS only | 373 cases | +0.02885 | t-interval: [+0.02392, +0.03379] |
| Dataset-level, SUCCESS-only aggregation | 15 datasets | +0.02880 | Bootstrap percentile CI: [+0.01481, +0.04428] |

For the dataset-level analysis, the summary records a Wilcoxon signed-rank statistic of 7.0 and p = 0.0011597 across 15 nonzero dataset-level observations.

These estimates have different units of analysis and must not be conflated. Cases belonging to the same dataset are not independent; the dataset-level result is therefore particularly important when interpreting the evidence. The dataset-level analysis includes 15 datasets, not the full 45-dataset cohort.

The recorded case-level delta distribution among SUCCESS cases contains 232 positive, 59 zero, and 82 negative values. The mean is an aggregate and does not mean every case or dataset improved.

No superiority claim is made here. These are reported outputs from the committed summary, not a claim that an independent reproduction has been completed.

---

## 5. Cohort and Source Locks

The cohort lock records 45 selected datasets and an independent audit status of PASS. The audit artifact reports 284 eligible datasets in the eligibility table and checks including dataset uniqueness, membership in the OpenML universe, eligibility, duplicates, split feasibility, and coverage.

Key recorded identifiers:

| Identifier | Value |
|---|---|
| Run ID | `S04-R4-20261009T004210Z-88bcf6717e5e` |
| Protocol SHA-256 | `c5206507a7b75575a828f5acdfd5e3814e0abe808bc33173e2b24bd03910b16a` |
| Cohort SHA-256 | `88bcf6717e5e5c28f20d93f0c2d36c393cd8b70253c68094b57f492cd7d9c09d` |
| Execution-plan SHA-256 | `167e4fa73dc7ec0d78e4a1f805fbb962e832e49c62208de932f81a7ab7e9a235` |
| Locked source commit | `873e19358815d41a68768c41f8fa8bb55af6be84` |
| Source-tree SHA-256 | `1b955e950e32245553df6850d114d9bc4dc86d514e83c401cf634495a5b2b9e2` |

See the cohort lock, source lock, and run manifest for the recorded details.

---

## 6. Evidence and Artifact Map

- `protocol/R4_PROTOCOL.json` — Protocol rules and experiment design.
- `protocol/protocol_lock.json` — Protocol lock artifact, if present in the checked-out revision.
- `cohort/cohort_lock.json` — Cohort hash and recorded cohort audit.
- `source_lock/source_lock.json` — Locked source commit, source hashes, and environment versions.
- `evidence/R4_RUN_MANIFEST.json` — Run identity, status, hashes, environment, and recorded test summary.
- `evidence/forensic_lock.json` — Recorded forensic checks and lock information.
- `evidence/repository_pytest_report.json` — Recorded repository test report, if present.
- `statistics/r4_summary.json` — Recorded outcomes and statistical summaries.
- `results/` — Results artifacts, if present in the checked-out revision.

The manifest records repository tests as **17 passed in 8.05 seconds** and the forensic status as **PASS**. These are statements recorded in the manifest; this README update does not rerun those tests or forensic checks.

---

## 7. Reproducibility Status and Limitations

The repository contains protocol, lock, manifest, and statistical-summary artifacts. However, a complete, documented, end-to-end execution entry point for independently rebuilding the recorded run must be available and linked before this phase can be described as **fully independently reproducible**.

For an independent reproduction, a reviewer should be able to:

1. Obtain the exact locked source commit and verify the source hashes.
2. Install the recorded Python and package versions in a documented environment.
3. Retrieve the locked cohort and required data snapshots, or follow a precisely documented retrieval procedure.
4. Run the complete experiment from a committed runner or notebook without manually injecting results.
5. Regenerate case-level records and summary statistics from the run artifacts.
6. Verify the regenerated hashes, outcome counts, and statistical outputs against the committed records.
7. Preserve all non-terminal outcomes and distinguish system failures from infrastructure, harness, data, dependency, interruption, and incomplete-run conditions as defined by the protocol.

Until those steps are independently completed, the appropriate description is:

> **Completed run with committed evidence artifacts; independent end-to-end reproduction not established by this README.**

---

## 8. Scientific Reporting Rules

- Do not change the frozen protocol, cohort, thresholds, or exclusion rules after inspecting outcomes.
- Do not count `NOT_TRIGGERED` as Delta = 0 in the primary analysis.
- Keep the primary SUCCESS-only analysis distinct from the secondary triggered-case analysis.
- Report the unit of analysis and sample size with every estimate.
- Do not generalize case-level confidence intervals as if all cases were independent datasets.
- Do not describe a recorded PASS status as independent validation unless the relevant checks have actually been rerun and their outputs inspected.
- Any correction to a result artifact must be traceable and must not silently overwrite the historical evidence.

---

## 9. Main Artifacts

- Protocol
- Cohort lock and audit
- Source lock
- Run manifest
- Statistical summary

> This README describes the recorded S04/R4 artifacts and their interpretation. It does not replace the protocol, source locks, run manifest, or underlying case-level evidence.
