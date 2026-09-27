# Code Release Pre-Flight Quality Assurance Checklist

- [x] **No Hardcoded Absolute Paths:** Checked all scripts for local path strings (e.g., `C:\`, `D:\`, `lenovo`, `Desktop`).
- [x] **No Embedded Secrets / Credentials:** Verified zero API keys, passwords, database credentials, or tokens.
- [x] **No Internal Project Identifiers:** Cleared development tags, temporary scratchpad notes, and internal bug tracking markers.
- [x] **No Fabricated URLs or DOIs:** Replaced speculative URLs and synthetic DOIs with clean placeholders and formal upload instructions.
- [x] **Open Source License Included:** Full MIT License included in `LICENSE`.
- [x] **Dependency Specification Complete:** `environment.yml` and `requirements.txt` verified.
- [x] **Deterministic Random State:** All stochastic models (random forest, cross-validation, bootstrap) use `seed=42`.
- [x] **Repository Packaging Size:** Package strictly contains code, scripts, configuration, and documentation (< 2 MB).
