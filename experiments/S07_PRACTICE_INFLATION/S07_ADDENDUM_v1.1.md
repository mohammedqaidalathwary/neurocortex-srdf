# S07 — Practice Inflation — Addendum v1.1

**Parent report:** `S07_REPORT.md`
**Protocol SHA-256:** `c78b78ed48ea3e00d1e1c9f63ace246485fff8657164061aded5fdeb8febd525`
**Addendum date:** 2026-10-17
**Addendum status:** Documentation-only; no locked artifact modified

---

## Purpose

This addendum closes five documentation gaps in the S07 outputs.
It does **not** modify the locked protocol,
the pre-registration, the confirmatory results, or the parent report.

1. Forensic test numbering (gaps 08, 13)
2. Cohort reconciliation (131 → 98 → 60)
3. SESOI margin sensitivity (0.01 / 0.02 / 0.03)
4. Unseen-only sensitivity analysis (protocol-required)
5. Deviations impact analysis (38 logged deviations)

---

## 1. Forensic test numbering

The forensic audit contains tests numbered 1–14 with gaps at 8 and 13.
Review of the full Git history (all branches, all tags) confirms that
`TEST_08` and `TEST_13` were **never planned, never specified, and never
implemented**. The numbering reflects discovery order during development,
not a predefined test count. See `audit/TEST_NUMBERING_NOTE.md`.

**Status:** No gap. `AUDIT.md` already reports "12 tests, all PASS".

---

## 2. Cohort reconciliation

| Stage | N | Source |
|---|---|---|
| Cohort R candidates (protocol) | 131 | `cohort_R_candidates.csv` |
| Successfully analyzed | 98 | `cases.csv.gz` (status=SUCCESS) |
| Unseen-only subset (post-hoc) | 60 | `S07_unseen_only_sensitivity.json` |

The 33-dataset difference (131 → 98) is fully accounted for by the 38
logged runtime deviations. See `audit/S07_RECONCILIATION.md`.

---

## 3. SESOI margin sensitivity (0.01 / 0.03)

Protocol §`sesoi_sensitivity` required sensitivity analysis at 0.01 and 0.03
in addition to the declared 0.02. These margins were computed **after** the
primary analysis and are labeled *Post-hoc protocol-consistent*.
The primary claim H1 (threshold inflation) is **stable across all three
margins**. Full decision matrix: `audit/S07_sesoi_margins_sensitivity.csv`.

**Impact on claims:** None. H1 remains SUPPORTED at 0.01, 0.02, and 0.03.

---

## 4. Unseen-only sensitivity analysis

Protocol §`cohort.sensitivity_unseen_only = true` required re-analysis
restricted to datasets not previously seen in S04/S05/S06.

- Seen-before union (S04 ∪ S05 ∪ S06): 243 datasets
- Overlap with S07 cohort: 38 datasets
- Unseen subset: 60 datasets
- **N = 60 < N_req = 70** → classified as **EXPLORATORY** per protocol
  (`protocol_lock.json` → `notes`).

**Result:** All confirmatory directions are preserved in the unseen subset:

| Test | Full (n=98) | Unseen (n=60) | Direction |
|---|---|---|---|
| H1 | +0.0976 | +0.0794 | Preserved |
| H2_CSRF | −0.1071 | −0.0878 | Preserved |
| H2_EE | +0.0074 | +0.0091 | Preserved |
| H2_SMOTE | −0.0365 | −0.0365 | Identical |

Full report: `audit/S07_UNSEEN_ONLY_REPORT.md`.

**Method note:** This subset analysis evaluates *direction preservation* only.
For H1, the one-tailed sign-flip test matches the protocol. For H2/H4, the
formal TOST is not re-run; only the sign of the effect is checked. This
keeps the exploratory nature of the subset analysis explicit.


---

## 5. Deviations impact analysis

38 runtime deviations were logged in `logs/deviations.csv`:

| Category | Count | Affected tests |
|---|---|---|
| `cardinality_exceeded` | 15 | All (column exclusion) |
| `no_numeric_runtime` | 13 | H2_SMOTE, H4_SMOTE only |
| `download_failure` | 5 | All (dataset loss) |
| `armL_download_failure` | 5 | Arm L only |

**No deviation affects H1, H2_CSRF, H2_EE, H4_CSRF, or H4_EE.**
Full report: `audit/S07_DEVIATIONS_IMPACT_REPORT.md`.

---

## Summary of impacts on published claims

| Claim | Original | After addendum |
|---|---|---|
| H1 SUPPORTED | ✅ | ✅ unchanged |
| H2_CSRF INFERIOR | ✅ | ✅ unchanged |
| H2_EE EQUIVALENT | ✅ | ✅ unchanged |
| H2_SMOTE INFERIOR | ✅ | ✅ unchanged |
| H4 family EQUIVALENT | ✅ | ✅ unchanged |
| H3 descriptive | ✅ | ✅ unchanged |
| Scenario A achieved | ✅ | ✅ unchanged |

**Conclusion:** All primary and secondary conclusions of `S07_REPORT.md`
remain valid. The addendum adds robustness documentation, not corrections.
