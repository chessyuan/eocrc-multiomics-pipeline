# Reproducible Pipeline & Code Package for EOCRC Multi-Omics Analysis

This repository contains the complete custom analysis codebase and verification pipeline for the study:  
**"Age-by-Disease Interaction Reveals Conserved Taxonomic but Divergent Functional Gut Microbiome Features in Early-Onset Colorectal Cancer"**

- **Author:** chessyuan (chessyuan)  
- **Affiliation:** the academic department, the institution, [location redacted]  
- **Contact:** [redacted] | [redacted]  
- **ORCID:** [[researcher identifier redacted]](https://orcid.org/[researcher identifier redacted])  
- **Target Journal:** *Nature Communications* (Article)  
- **License:** MIT Open Source License
- **Repository:** https://github.com/chessyuan/eocrc-multiomics-pipeline  

---

## 1. Quickstart & Environment Setup

To reproduce the analysis from scratch using Conda:

```bash
# Create and activate the conda environment
conda env create -f environment.yml
conda activate eocrc-audit-env

# Or using pip
pip install -r requirements.txt
```

---

## 2. One-Click Pipeline Reproduction

Execute the master workflow orchestrator:

```bash
python run_audit_pipeline.py
```

This orchestrator executes the validated analytical stages:
1. **Taxonomic Equivalence Testing:** Two One-Sided Tests (TOST) sensitivity across equivalence bounds $d = \pm 0.20, \pm 0.25, \pm 0.30$.
2. **Functional Pathway Meta-Analysis:** Hartung-Knapp random-effects meta-analysis for functional pathways and Winner's curse assessment.
3. **Microbiome Clock Out-of-Distribution Stress Test:** Microbiome age displacement models and Mahalanobis distance OOD evaluation.
4. **Machine Learning Model Validation:** Cross-platform 16S-to-shotgun taxonomic mapping and locked Random Forest external validation.
5. **Decision Curve Analysis (DCA):** Net clinical benefit evaluation across transported screening prevalence rates ($1\%, 2\%, 5\%, 10\%$).
6. **Publication Display Item Rendering:** Programmatic vector rendering of Figures 1 through 7 into PDF and 300 DPI PNG formats.

---

## 3. Data Availability & Accessions

All primary datasets supporting the findings of this study are available in open public biological repositories:
- **NCBI BioProject:** `PRJNA763023` (Fudan/Huadong cohort)
- **CNGBdb:** `CNP0004314` (Guangzhou SYSUCC cohort)
- **NCBI BioProject:** `PRJNA1422810` (Hong Kong multi-center cohort)
- **NCBI BioProject:** `PRJNA883949` (Korean validation cohort 16S)
- **NCBI GEO:** `GSE213092` (Bulk tumor RNA-seq) & `GSE175433` (NanoString PanCancer Immune)
- **Source Data:** Provided in `Source_Data.xlsx` with 33 individual panel-specific sheets.

---

## 4. Archival and Permanent DOI
Upon public release, this repository is configured for archiving via Zenodo to provide a permanent, citable digital object identifier (DOI). See `REPOSITORY_UPLOAD_INSTRUCTIONS.md` for the upload and release workflow.
