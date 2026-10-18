# Release and Experiment Artifact Map

## Purpose

This document distinguishes the version identifiers used for the software package, historical source snapshots, the conceptual white paper, and protocol-controlled experiments. These identifiers describe different artifacts and must not be synchronized mechanically.

## Software package

| Artifact | Version recorded in the repository | Role | Rule |
|---|---:|---|---|
| `pyproject.toml` | `0.4.0` | Primary package metadata | Defines the current package version. |
| `setup.py` | `0.4.0` | Setuptools compatibility metadata | Kept aligned with `pyproject.toml` to avoid conflicting package versions. |
| `src/__init__.py` | `0.1.0` | Historical implementation snapshot | Preserve its version as part of the source history. |
| `src_v2/__init__.py` | `0.1.0` | Historical implementation snapshot | Preserve its version as part of the source history. |
| `src_v3/__init__.py` | `0.3.0` | Historical implementation snapshot | Preserve its version as part of the source history. |
| `src_v4/__init__.py` | `0.4.0` | Versioned implementation snapshot | Matches the current package version. |

Historical source snapshots retain their own identifiers. The package version does not imply that every historical implementation was used in every experiment.

## Citation and website metadata

| Artifact | Current value | Interpretation and handling |
|---|---|---|
| `CITATION.cff` | `version: 1.0.0`; `date-released: 2026-10-09` | Software citation metadata aligned to the public v1.0.0 Zenodo software record. |
| Concept DOI in `CITATION.cff` | `10.5281/zenodo.23252916` | Concept-level identifier for the NeuroCortex software record. |
| Version DOI in `CITATION.cff` | `10.5281/zenodo.23252917` | Version-specific record published as v1.0.0 on 2026-10-09. |
| `docs/index.html` structured metadata | `version: 0.3.0`; publication date `2026-10-08` | The structured metadata labels the conceptual white paper. It is not, by itself, evidence of the current Python package version. |

The software release metadata is distinct from the package metadata: Zenodo lists release `v0.4.0` at record `23224039` (2026-10-07) and release `v1.0.0` at record `23252917` (2026-10-09). The concept DOI is `10.5281/zenodo.23252916`; the version DOI for v1.0.0 is `10.5281/zenodo.23252917`. The Python package version remains `0.4.0`; do not mechanically equate the package version with the archived software-release version.

## Experiment identifiers

Experiment identifiers, protocol versions, protocol hashes, cohort manifests, and result-artifact identifiers are independent of the Python package version.

For each reported result, use the protocol and run-linked artifacts associated with that experiment. Do not infer the implementation used for an experiment from the latest package version, and do not change locked protocol or result artifacts to make version labels appear uniform.

## General dependencies

`requirements.txt` documents general project dependencies. It is not a lockfile and does not, by itself, reproduce an experiment. Experiment-specific reproducibility must be established from the corresponding protocol, source revision, environment record, cohort definition, execution artifacts, and result records.

## Change control

Changes to package metadata must not modify experimental outputs, protocol locks, cohort manifests, run timestamps, or historical source snapshots. Changes to citation metadata require verification against the cited release record before publication.
