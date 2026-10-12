
"""
S06 SRDF v2 Runner
------------------
Executes the modified SRDFFramework (src_v2) on each S04 case and
records balanced_accuracy of the selected model on the test fold.

This module does NOT modify src_v2. It only uses it.
"""

import sys
from pathlib import Path
from typing import Any, Dict

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import balanced_accuracy_score

# Resolve src_v2 import
REPO_DIR = Path(__file__).resolve().parent.parent
if str(REPO_DIR) not in sys.path:
    sys.path.insert(0, str(REPO_DIR))

from src_v2.core import SRDFFramework


def run_single_case(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_test: np.ndarray,
    y_test: np.ndarray,
    random_seed: int,
    imbalance_threshold: float = 3.0,
) -> Dict[str, Any]:
    """Run one SRDF cycle and return a summary record."""
    config = {
        "imbalance_threshold": imbalance_threshold,
        "validation_threshold": 0.0,      # allow any positive utility
        "resource_budget": 3.0,
        "random_seed": int(random_seed),
        "w_accuracy": 0.50,
        "w_safety": 0.30,
        "w_efficiency": 0.20,
    }

    framework = SRDFFramework(config=config)

    cycle = framework.run_cycle(X_train, y_train, X_test, y_test)

    # Selected candidate name
    selected_name = cycle.get("selected_solution")

    # Balanced accuracy of the selected candidate on the test fold
    adapted_bacc = None
    for candidate in cycle.get("evaluated_candidates", []):
        if candidate["name"] == selected_name:
            preds = candidate.get("predictions")
            if preds is not None:
                adapted_bacc = float(balanced_accuracy_score(y_test, preds))
            break

    # Reference baseline: RandomForest without SMOTE
    rf = RandomForestClassifier(
        n_estimators=100, random_state=int(random_seed)
    )
    rf.fit(X_train, y_train)
    baseline_bacc = float(
        balanced_accuracy_score(y_test, rf.predict(X_test))
    )

    trawler_findings = cycle.get("trawler_findings", {})
    train_ir = float(trawler_findings.get("imbalance_ratio", 0.0))
    triggered = bool(trawler_findings.get("class_imbalance", False))

    return {
        "status": cycle.get("status"),
        "triggered": triggered,
        "train_ir": train_ir,
        "selected_candidate": selected_name,
        "baseline_bacc": baseline_bacc,
        "adapted_bacc": adapted_bacc,
        "delta_bacc": (
            None if adapted_bacc is None
            else adapted_bacc - baseline_bacc
        ),
    }
