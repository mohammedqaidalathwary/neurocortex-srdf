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
| `CITATION.cff` | `version: 0.3.0`; `date-released: 2026-10-08` | Software citation metadata. Its version and DOI mapping must be checked against the corresponding Zenodo record before being changed. |
| Concept DOI in `CITATION.cff` | `10.5281/zenodo.23252917` | Concept-level identifier recorded in the citation metadata. |
| Version DOI in `CITATION.cff` | `10.5281/zenodo.23252916`, described there as v1.0.0 | Version-specific identifier recorded in the citation metadata. Its relationship to the current citation version requires verification against Zenodo metadata. |
| `docs/index.html` structured metadata | `version: 0.3.0`; publication date `2026-10-08` | The structured metadata labels the conceptual white paper. It is not, by itself, evidence of the current Python package version. |

The citation version must not be changed merely to match the package version. Before changing `CITATION.cff`, verify the release/version metadata and DOI relationships against the authoritative Zenodo records. Preserve the existing citation metadata until that verification is complete.

## Experiment identifiers

Experiment identifiers, protocol versions, protocol hashes, cohort manifests, and result-artifact identifiers are independent of the Python package version.

For each reported result, use the protocol and run-linked artifacts associated with that experiment. Do not infer the implementation used for an experiment from the latest package version, and do not change locked protocol or result artifacts to make version labels appear uniform.

## General dependencies

`requirements.txt` documents general project dependencies. It is not a lockfile and does not, by itself, reproduce an experiment. Experiment-specific reproducibility must be established from the corresponding protocol, source revision, environment record, cohort definition, execution artifacts, and result records.

## Change control

Changes to package metadata must not modify experimental outputs, protocol locks, cohort manifests, run timestamps, or historical source snapshots. Changes to citation metadata require verification against the cited release record before publication.
