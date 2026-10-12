# S06 pre-execution checklist (tick every item BEFORE the first confirmatory download)

## A. Protocol
- [ ] `S06_PROTOCOL.json` read in full; SHA-256 recorded
- [ ] SESOI (0.01), non-inferiority margin (0.005), alpha (0.05, Holm over H1 and H2) agreed and unchanged
- [ ] Mode A/B/C definitions agreed (they are numeric and script-computable)
- [ ] Deviation policy understood: any change after deposit is logged, never silent

## B. Code freeze
- [ ] Repository at commit `4157089`; `git status` clean
- [ ] SHA-256 of every file in `src/` and `src_v2/` written to `protocol_freeze_addendum.json`
- [ ] v1 = S04 source lock; v2 = `src_v2/`; no edits afterwards
- [ ] Repository tests run and the result recorded (pass or fail, not hidden)

## C. Cohort (no model output used)
- [ ] Universe = S04 `eligibility_table.csv` eligible rows (284), not re-queried from OpenML
- [ ] Removed: the 45 S04 ids; exact-content duplicates of them; same-name version families; duplicates inside the remainder
- [ ] S04 selection procedure applied unchanged; coverage audit and independent audit pass
- [ ] Cohort size recorded as an outcome; no first-N, no sampling
- [ ] `cohort_manifest.json` hash computed and stored

## D. Power analysis (before running)
- [ ] Simulation script run with SD and trigger rate read from the S04-cohort v2 files
- [ ] Both effect scenarios (100% and 50%) reported
- [ ] Required triggered datasets vs expected triggered datasets compared; cohort NOT altered afterwards

## E. External registration
- [ ] Protocol JSON + freeze addendum deposited on OSF Registries or Zenodo (DOI)
- [ ] Registration identifier, date and SHA-256 copied into the repository README

## F. Execution
- [ ] One run per variant; resumable JSONL; timeouts on
- [ ] Every record carries `test_used_before_selection = false`
- [ ] Failures logged by status; `deviations.json` created (empty list if none)

## G. Reporting rules
- [ ] H1/H2 reported exactly per the decision rules; failures written as null findings
- [ ] No claim of superiority over EasyEnsemble; gap reported descriptively
- [ ] Paper states: v2 derived post hoc on S04 cohort; confirmatory result comes only from the new cohort
- [ ] Units written as percentage points (e.g. +2.63 pp), and p-values only at dataset level
