# TEST 14 — Claims to Evidence

**Verdict: PASS**

Supported claims: 8 / 8

| Claim | Test | Evidence | Value | Supported |
|---|---|---|---|---|
| Threshold inflation is confirmed: RF@pi_hat > RF@0.5 by more than SESOI | H1 | tables/confirmatory_results.csv | mean = +0.0976, CI95 = [+0.0824, +0.1132] | YES |
| Cost-sensitive RF is inferior to the corrected control | H2_CSRF | tables/confirmatory_results.csv | mean = -0.1071 | YES |
| EasyEnsemble is equivalent to the corrected control (within +/- SESOI) | H2_EE | tables/confirmatory_results.csv | mean = +0.0074, CI95 = [+0.0032, +0.0121] | YES |
| AUC contrast for SMOTE is equivalent to baseline | H4_SMOTE | tables/confirmatory_results.csv | mean = -0.0059 | YES |
| AUC contrast for CSRF is equivalent to baseline | H4_CSRF | tables/confirmatory_results.csv | mean = -0.0028 | YES |
| AUC contrast for EE is equivalent to baseline | H4_EE | tables/confirmatory_results.csv | mean = +0.0012 | YES |
| Mechanism is not RF-specific: H1 direction holds with LR | Arm L (exploratory) | tables/armL_analysis.csv | mean = +0.1216 | YES |
| SRDF's S04 claim (+0.029 vs RF@0.5) flips to negative under the corrected control | Arm B (interpretive) | tables/armB_summary.csv | S04: conv = +0.0289, corrected = -0.0654 | YES |