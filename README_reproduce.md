# Reproduction Guide: Step-by-Step Execution

This document provides explicit instructions for replicating all statistical models, figures, and tables reported in the manuscript.

### Prerequisites
- Python 3.11 or higher
- Standard scientific stack (NumPy, SciPy, Pandas, Scikit-learn, Statsmodels, Matplotlib, Seaborn)

### Execution Steps
1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run Master Pipeline:**
   ```bash
   python run_audit_pipeline.py
   ```
3. **Verify Output Integrity:**
   - Numerical outputs are generated into the respective audit subdirectories.
   - All 7 main figures are generated at vector resolution and 300 DPI.
   - Results match the values locked in the manuscript and `Source_Data.xlsx`.

All stochastic random seeds are fixed to `42` to ensure exact, bitwise-identical reproducibility.
