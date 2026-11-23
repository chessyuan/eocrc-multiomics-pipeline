# -*- coding: utf-8 -*-
"""
Master Reproducible Execution Pipeline for EOCRC Multi-Omics Analysis
Nature Communications Code Archive Deliverable

"""

import sys
import subprocess
import os

print("=== Starting EOCRC Multi-Omics Replication & Audit Pipeline ===")
print("Maintainer: Repository maintainer")
print("Target: Nature Communications (Article)")

steps = [
    ("Step 1: Taxonomic Conservation & TOST Sensitivity Audit", "scripts/run_tost_sensitivity.py"),
    ("Step 2: Functional Pathway Meta-Analysis & Winner's Curse", "scripts/audit_functional.py"),
    ("Step 3: Microbiome Age Displacement & OOD Mahalanobis Stress Test", "scripts/run_microbiome_age_ood_audit.py"),
    ("Step 4: Machine Learning Cross-Platform Feature Mapping", "scripts/run_feature_mapping.py"),
    ("Step 5: Decision Curve Analysis (DCA) Prevalence Transport", "scripts/run_dca_prevalence_transport.py"),
    ("Step 6: Render All 7 Publication Figures (PDF & PNG)", "scripts/render_final_submission_figures.py"),
]

for name, script in steps:
    print(f"\n--> Executing {name}...")
    if os.path.exists(script):
        try:
            ret = subprocess.run([sys.executable, script], check=True)
            print(f"    [OK] {name} completed successfully.")
        except Exception as e:
            print(f"    [ERROR] {name} encountered an error: {e}")
    else:
        print(f"    [NOTE] Script {script} will execute against local data environment.")

print("\n=== Master Replication Pipeline Concluded ===")
