# Public Code Repository & Zenodo Archival Instructions

**Author:** chessyuan  
**Project:** EOCRC Multi-Omics Independent Pipeline  
**Date:** September 27, 2026  

This folder contains a complete, clean, self-contained public code release package. Follow these straightforward steps to publish the repository to GitHub and mint a persistent Zenodo DOI for formal journal compliance:

---

## Step 1: Create a New GitHub Repository
1. Log in to your personal or academic GitHub account at [https://github.com](https://github.com).
2. Click **New Repository** (or visit `https://github.com/new`).
3. Set **Repository name**: e.g., `eocrc-multiomics-pipeline` (or `eocrc-interaction-audit`).
4. Set visibility to **Public**.
5. Do **NOT** initialize with a README, .gitignore, or license (these are already pre-configured in this directory).
6. Click **Create repository**.

---

## Step 2: Initialize Git and Push Local Code
Open a terminal in this directory (`06_Code_and_Data_Release`) and execute:

```bash
git init
git add .
git commit -m "Initial release of EOCRC multi-omics reproducible analysis package"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPOSITORY_NAME>.git
git push -u origin main
```

---

## Step 3: Link to Zenodo for Permanent Archival & DOI
1. Log in to [https://zenodo.org](https://zenodo.org) (sign in with your GitHub account).
2. Navigate to **GitHub Settings** in Zenodo (`https://zenodo.org/account/settings/github/`).
3. Locate your newly pushed repository and toggle the switch to **ON**.
4. Return to your GitHub repository and create a formal release:
   - Click **Releases** -> **Draft a new release**.
   - Tag version: `v1.0.0`
   - Title: `Initial Submission Release v1.0.0`
   - Click **Publish release**.
5. Zenodo will automatically archive the release within a few minutes and assign a persistent, citable **Zenodo DOI** (e.g., `10.5281/zenodo.XXXXXXX`).

---

## Step 4: Final Metadata Update
Once your repository is live and your Zenodo DOI is assigned:
1. Update the placeholder URL and DOI in `CITATION.cff` and `README.md`.
2. Provide the finalized GitHub URL and Zenodo DOI to the editorial portal during manuscript revision or proof stage.
