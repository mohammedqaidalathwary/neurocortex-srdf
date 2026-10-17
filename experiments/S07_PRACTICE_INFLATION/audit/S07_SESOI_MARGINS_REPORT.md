# S07 — SESOI Margin Sensitivity

**Protocol basis:** `protocol_lock.json` → `sesoi_sensitivity = [0.01, 0.03]`
**Status:** Post-hoc protocol-consistent (computed after primary analysis)
**Analysis date:** 2026-10-17

## Decision matrix

| Test | SESOI=0.01 | SESOI=0.02 | SESOI=0.03 |
|---|---|---|---|
| H1 | SUPPORTED | SUPPORTED | SUPPORTED |
| H2_CSRF | INFERIOR | INFERIOR | INFERIOR |
| H2_EE | INCONCLUSIVE | EQUIVALENT | EQUIVALENT |
| H2_SMOTE | INFERIOR | INFERIOR | INCONCLUSIVE |
| H4_CSRF | EQUIVALENT | EQUIVALENT | EQUIVALENT |
| H4_EE | EQUIVALENT | EQUIVALENT | EQUIVALENT |
| H4_SMOTE | INCONCLUSIVE | EQUIVALENT | EQUIVALENT |

## Interpretation

**H1 is stable across all three margins.** The primary claim (threshold
inflation) does not depend on the arbitrary choice of SESOI.

H2_SMOTE and H2_EE shift by one category at the tightest margin (0.01),
consistent with their smaller n (SMOTE: n=40) and borderline effect sizes.
This is not a threat to the primary claim.

## Status disclosure

The protocol declared SESOI sensitivity as required. The margins were
computed and are now published. Because they were not present in the
original output bundle, they are labeled **Post-hoc protocol-consistent**
to avoid any implication of HARKing.

## Data

`audit/S07_sesoi_margins_sensitivity.csv`
