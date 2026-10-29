# S07 Source-Level Deduplication Disclosure

**Author:** Eng. Mohammed Qaid Alathwry
**Date:** 2026-10-29

## Purpose
This document discloses a structural characteristic of the S07 dataset cohort that affects the interpretation of statistical independence.

## The Issue
In the S07 analysis, I treated 98 dataset IDs as independent units. However, my post-hoc audit revealed that these 98 IDs originate from only **61 independent source datasets** (40 IDs are resampled variants, such as different seeds or row counts from the same original dataset).

## Impact on Results
I re-ran the primary confirmatory analysis at the source level (n=61). The direction and statistical significance of all 7 decision labels (SUPPORTED, INFERIOR, EQUIVALENT) remained identical to the ID-level analysis. The effective sample size for S07 is 61, not 98. Any manuscript or derivative work based on S07 must report n=61 for inferential claims.
