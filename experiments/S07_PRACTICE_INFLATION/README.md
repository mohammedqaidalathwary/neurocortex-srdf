# S07 — Practice Inflation

**Does class-imbalance correction beat a threshold-corrected control? A catalog-wide confirmatory study of benchmark-practice bias.**

## Summary

The standard benchmark practice compares rebalancing methods against a plain classifier at the default 0.5 threshold. This study measures how much of the reported benefit is an artifact of that control.

## Key results

| Test | Contrast | Result |
|---|---|---|
| H1 | RF@π̂ vs RF@0.5 | +0.0976 bAcc (SUPPORTED) |
| H2_SMOTE | SMOTENC vs RF@π̂ | −0.0365 bAcc (INFERIOR) |
| H2_CSRF | CS-RF vs RF@π̂ | −0.1071 bAcc (INFERIOR) |
| H2_EE | EE vs RF@π̂ | +0.0074 bAcc (EQUIVALENT) |
| H4_* | AUC for all three | EQUIVALENT (effect disappears) |

**Scenario A achieved.**

## Design

- **Cohort R:** 131 datasets, rule-derived from S04 snapshot; 98 analyzed.
- **Confirmatory family:** H1, H2×3, H4×3 (7 tests, Holm-corrected at α = 0.05).
- **Unit of inference:** dataset.
- **Forensic validation:** 12 tests, all PASS.

## DOIs

- Pre-registration: [10.5281/zenodo.23404802](https://doi.org/10.5281/zenodo.23404802)
- Results: [10.5281/zenodo.23406120](https://doi.org/10.5281/zenodo.23406120)

## Reproducibility

Notebook: `S07-pipeline_integrity.ipynb` (repo root).
Protocol SHA-256: `c78b78ed48ea3e00d1e1c9f63ace246485fff8657164061aded5fdeb8febd525`.
Merkle root: `d48271da7b7e16e48767e036ba8239d7236ee8d386cb6a7d366a74d152de1e23`.
Runtime: ~90 minutes on Colab. Deterministic (seed 20261014).
