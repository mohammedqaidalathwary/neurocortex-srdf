# NeuroCortex — Self-Reinforcing Development Framework (SRDF)

<p align="center">
  <img src="assets/neurocortex_logo.png" alt="NeuroCortex Logo" width="220">
</p>

<p align="center">
  <a href="https://orcid.org/0009-0006-9075-072X">
    <img src="https://img.shields.io/badge/ORCID-0009--0006--9075--072X-a6ce39.svg" alt="ORCID">
  </a>
  <a href="https://opensource.org/licenses/Apache-2.0">
    <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License">
  </a>
  <img src="https://img.shields.io/badge/python-3.9%2B-blue" alt="Python">
</p>

---

## Overview

NeuroCortex is a research framework centered on the **Self-Reinforcing Development Framework (SRDF)**. SRDF describes a controlled, auditable approach to **runtime structural adaptation** in machine learning systems.

Rather than allowing unbounded self-modification, SRDF separates the adaptation process into explicit stages: observation, analysis, candidate generation, evaluation, authorization, and controlled state transition.

The framework is organized around three principal components — **Trawler**, **Generator**, and **Arbiter** — whose roles are deliberately separated.

---

## Table of Contents

- [Overview](#overview)
- [Framework Components](#framework-components)
- [Workflow](#workflow)
- [Project Structure](#project-structure)
- [Primary Artifacts](#primary-artifacts)
- [Repository Layout](#repository-layout)
- [Installation](#installation)
- [Usage](#usage)
- [Reproducibility](#reproducibility)
- [Data and Code Availability](#data-and-code-availability)
- [Citation](#citation)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)
- [Research Scope and Boundaries](#research-scope-and-boundaries)

---

## Framework Components

### Trawler

Observes the current runtime context and identifies conditions that may justify adaptation. Its role is analysis, not decision-making.

### Generator

Produces candidate structural or learning modifications. Candidates are proposals, not commitments. The Generator does not evaluate or authorize its own candidates.

### Arbiter

Evaluates candidates against predefined constraints and authorizes only those that satisfy the required conditions. Its role is independent of the Generator.

---

## Workflow

The SRDF workflow is ordered and stage-separated:

    OBSERVE -> ANALYZE -> GENERATE -> EVALUATE -> AUTHORIZE
            -> COMMIT_OR_REJECT -> RECORD

Each stage has a defined role and a defined output. Stage separation is a design principle, not a runtime detail.

---

## Project Structure

The project currently hosts the following experimental phases:

| Phase | Directory | Role |
|-------|-----------|------|
| **S01** | `experiments/S01_PROTOTYPE_VALIDATION/` | Foundational executable prototype |
| **S03** | `experiments/S03_GENERATOR_ARBITER/` | Functional SRDF validation |

Each phase directory contains its own `README.md` describing scope,
artifacts, and claim boundaries.

## Primary Artifacts

### White Paper

A conceptual white paper describing the framework is available at:

- `docs/whitepaper/NeuroCortex_SRDF_White_Paper_v1.0.pdf`

The white paper is a **conceptual document**. It does not report
experimental results, does not present quantitative evaluation, and
does not constitute prior publication of any future manuscript.

### S01 — Foundational Executable Prototype

- `experiments/S01_PROTOTYPE_VALIDATION/notebooks/srdf_s01_foundational_prototype.ipynb`

An executable notebook demonstrating the SRDF workflow in a
controlled setting.

### S03 — Functional Validation

- `experiments/S03_GENERATOR_ARBITER/runs/srdf_s03_multirun_raw_20260917T223125Z.json`
- `experiments/S03_GENERATOR_ARBITER/results/srdf_s03_multirun_validated.json`

Multirun artifacts documenting functional execution of the SRDF cycle
across fixed seeds.

## Repository Layout

The repository is organized into the following principal directories:

- `src/` — Reference implementation of the SRDF components
  (Trawler, Generator, Arbiter, Core).
- `experiments/` — Experimental phases, each in its own directory
  (S01, S03).
- `protocols/` — Protocol artifacts aligned with each phase.
- `docs/` — Project documentation and the conceptual white paper.
- `examples/` — Minimal illustrative examples of the SRDF workflow.
- `tests/` — Unit tests for the reference implementation.
- `assets/` — Static visual assets (logos, icons).
- `archive/` — Historical artifacts preserved for provenance.

Top-level files include:

- `README.md` — This document.
- `LICENSE` — Apache License 2.0.
- `CITATION.cff` — Citation metadata (CFF 1.2.0).
- `CHANGELOG.md` — Project change log.
- `AUTHORS.md` — Author and contribution information.
- `CONTRIBUTING.md` — Contribution guidelines.
- `CODE_OF_CONDUCT.md` — Community code of conduct.
- `SECURITY.md` — Security policy.
- `requirements.txt` — General project dependencies.
- `pyproject.toml` — Project metadata and build configuration.
- `setup.py` — Legacy packaging compatibility.


---

## Installation

Clone the repository:

    git clone https://github.com/mohammedqaidalathwary/neurocortex-srdf.git
    cd neurocortex-srdf

Install the Python dependencies:

    pip install -r requirements.txt

---

## Usage

### Running the S01 prototype

Open the notebook directly in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mohammedqaidalathwary/neurocortex-srdf/blob/main/experiments/S01_PROTOTYPE_VALIDATION/notebooks/srdf_s01_foundational_prototype.ipynb)

Or run it locally:

    jupyter notebook experiments/S01_PROTOTYPE_VALIDATION/notebooks/srdf_s01_foundational_prototype.ipynb

### Inspecting the SRDF reference implementation

The reference implementation of the framework components is in `src/`:

- `src/trawler.py`
- `src/generator.py`
- `src/arbiter.py`
- `src/core.py`

Unit tests are in `tests/`.

---

## Reproducibility

Each phase follows the SRDF principle of **protocol before execution**.
Where a phase defines a fixed random seed, the executed run is
reproducible under the same software environment and configuration.

The executed artifacts of each phase are preserved in their
respective directories. Where a phase was executed under a frozen
protocol, the protocol, the source lock, and the cohort lock are
included alongside the results.

This README does not summarize or reinterpret the results of any
phase. It points to the directories where those artifacts are
preserved.

---

## Data and Code Availability

- **Code**: This repository, released under the Apache License 2.0.
- **White Paper**: `docs/whitepaper/NeuroCortex_SRDF_White_Paper_v1.0.pdf`
- **Author ORCID**: [0009-0006-9075-072X](https://orcid.org/0009-0006-9075-072X)

A persistent identifier will be assigned through Zenodo upon the
final project release.

---

## Citation

If you reference this software or framework in academic or technical
work, please cite it using the metadata in `CITATION.cff`:

> Al-Athwary, M. Q. (2026). *NeuroCortex — Self-Reinforcing
> Development Framework (SRDF)*. GitHub.
> https://github.com/mohammedqaidalathwary/neurocortex-srdf

A persistent identifier will be assigned at the final release.

---

## License

This project is released under the Apache License 2.0. See
[`LICENSE`](LICENSE) for the full text.

---

## Contributing

Contributions, technical discussions, and research-oriented feedback
are welcome. Before proposing changes, please review
[`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## Contact

**Author**: Mohammed Qaid Al-Athwary  
**ORCID**: [0009-0006-9075-072X](https://orcid.org/0009-0006-9075-072X)  
**Email**: mohammedqaid.amanlift@gmail.com

---

## Research Scope and Boundaries

NeuroCortex is an ongoing research project. The material in this
repository is presented as a **conceptual and methodological
foundation**, not as a finished claim about capability or
superiority.

The repository does **not** claim:

- general or universal performance improvement,
- statistical significance of any result,
- self-evolving artificial general intelligence,
- unrestricted or unbounded self-modification,
- superiority over any existing method or architecture,
- production readiness.

Any empirical claim, if pursued, will be reported separately in a
peer-reviewed publication. This repository preserves the framework,
its protocols, and its evidence structure.
