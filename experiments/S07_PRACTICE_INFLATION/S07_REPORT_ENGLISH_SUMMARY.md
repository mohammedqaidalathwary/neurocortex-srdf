# S07 Report: English Summary

**Author:** Eng. Mohammed Qaid Alathwry
**Date:** 2026-10-29

## Purpose
This document provides an English-language summary of the S07 results and methodology. It serves as a reference for reviewers to avoid reliance on the original report, which contains some Arabic explanatory notes.

## Methodology Summary
S07 evaluated the "Practice Inflation" hypothesis using a cohort of 98 dataset IDs (derived from 61 independent sources) across 7 confirmatory tests. The primary metric was balanced accuracy (bAcc).

## Key Results
- **H1 (Practice Inflation):** SUPPORTED (mean difference = 0.0976, 95% CI [0.0824, 0.1132]).
- **H2 (Balancing Methods):** SMOTE and CSRF were INFERIOR to the prior-corrected threshold control. EasyEnsemble was EQUIVALENT.
- **H4 (Equivalence):** All H4 tests returned EQUIVALENT, indicating no residual benefit of balancing methods after threshold correction.

All confirmatory data and decision labels are preserved in the `S07_OUTPUT.zip` deposit (DOI: 10.5281/zenodo.23406120).
