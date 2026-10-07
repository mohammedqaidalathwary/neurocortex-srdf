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
