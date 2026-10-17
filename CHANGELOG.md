## [v1.1-addendum] — 2026-10-17

### Added
- `experiments/S07_PRACTICE_INFLATION/S07_ADDENDUM_v1.1.md`
- `experiments/S07_PRACTICE_INFLATION/audit/TEST_NUMBERING_NOTE.md`
- `experiments/S07_PRACTICE_INFLATION/audit/S07_RECONCILIATION.md`
- `experiments/S07_PRACTICE_INFLATION/audit/S07_UNSEEN_ONLY_REPORT.md`
- `experiments/S07_PRACTICE_INFLATION/audit/S07_SESOI_MARGINS_REPORT.md`
- `experiments/S07_PRACTICE_INFLATION/audit/S07_DEVIATIONS_IMPACT_REPORT.md`
- `experiments/S07_PRACTICE_INFLATION/audit/S07_unseen_only_sensitivity.json`
- `experiments/S07_PRACTICE_INFLATION/audit/S07_sesoi_margins_sensitivity.csv`
- `experiments/S07_PRACTICE_INFLATION/audit/S07_deviations_impact.csv`
- `experiments/S07_PRACTICE_INFLATION/audit/S07_seen_before_manifest.csv`

### Changed
- `AUDIT.md` — appended post-publication addendum section
- `README.md` (S07) — appended addendum reference

### Unchanged (locked)
- `protocol_lock.json`
- `pre_registration.json`
- `S07_REPORT.md`
- `confirmatory_results.csv`
- `AUDIT.json`
- `execution_plan.json`
- `cohort_R_manifest.json`

### Verification
- No confirmatory result changed.
- All primary and secondary conclusions remain valid.

---

# Changelog

All notable changes to the NeuroCortex SRDF project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `docs/whitepaper/NeuroCortex_SRDF_White_Paper_v1.0.pdf` —
  conceptual white paper (no experimental results).
- `CITATION.cff` — formal citation metadata (CFF 1.2.0).
- `AUTHORS.md` — author and contribution taxonomy (CRediT).
- `SECURITY.md` — responsible disclosure policy.
- `CONTRIBUTING.md` — contribution guidelines.
- `CODE_OF_CONDUCT.md` — Contributor Covenant v2.1.
- `pyproject.toml` — modern project metadata.
- Phase documentation for S01 and S03.

### Changed
- `README.md` rewritten to reflect the current repository state.
- S01 prototype renamed and relocated to
  `experiments/S01_PROTOTYPE_VALIDATION/notebooks/srdf_s01_foundational_prototype.ipynb`.
- S03 multirun artifacts relocated and renamed to
  `experiments/S03_GENERATOR_ARBITER/{runs,results}/srdf_s03_multirun_*.json`.
- Logo images optimized (from ~1.7 MB each to ~152 KB each).
- `requirements.txt` clarified with comments.

### Removed
- Obsolete `notebooks/` directory.
- Legacy whitepaper PDFs.
- Google Search Console verification file.

## [0.3.0] - 2026-09-17

### Phase identifier
R3 (S03) — Functional SRDF and predictive-adaptation validation

### Added
- Multirun results across 5 fixed seeds.
- Generator–Arbiter functional validation.

## [0.1.0] - 2026-09-17

### Phase identifier
S01 — Foundational Executable Prototype

### Added
- Executable prototype demonstrating the SRDF workflow.
- Feasibility demonstration of bounded runtime structural adaptation.

## [Unreleased] - 2026-10-14

### Added
- S05: Extended comparative evaluation against 4 external baselines
       (SMOTE+RF, Cost-Sensitive RF, ADASYN+RF, EasyEnsemble).
- S05: Counterfactual Arbiter analysis (net cost = -1.93 pp).
- S05: Failure decomposition (Mode A / Mode B / Mode C).
- S06a: v2 - deterministic tie-break + balanced_accuracy utility.
- S06b: v3 - validation threshold recalibrated mathematically (0.85 -> 0.75).
- S06c: v4 - EasyEnsemble added as third candidate.
- S06c: Finding - Arbiter underperforms EE standalone by 0.95 pp.
- S06: Zenodo protocol deposit (DOI 10.5281/zenodo.23308347).
- S06: Per-stage README files for S05 and S06.
- S06: Completion report (protocol/S06_COMPLETION_REPORT.json).
- Audit: S04 + S05 + S06 CLOSURE_REPORT.json files.
- Audit: stage_32_cohort_manifest_historical.json.
- Audit: s06_confirmatory_cohort_manifest_stage198.json.

### Changed
- Renamed s06_confirmatory_cohort_manifest.json (stage_32) to
  stage_32_cohort_manifest_historical.json. Added correct
  s06_confirmatory_cohort_manifest_stage198.json.
- Package version in pyproject.toml synced with src_v4/__init__.py (0.4.0).

### Fixed
- (planned) Test coverage for src_v2/src_v3/src_v4. Documented as
  PARTIAL in S06_COMPLETION_REPORT.json.
