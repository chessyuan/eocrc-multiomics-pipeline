
import pandas as pd
import numpy as np
import os

os.makedirs('22_final_independent_audit/09_dca_reanalysis', exist_ok=True)

# 1. Load Huadong cohort POD data from MOESM8
xls8 = pd.ExcelFile('02_metadata/41467_2021_27112_MOESM8_ESM.xlsx')
df = pd.read_excel(xls8, sheet_name='Figure 6c', header=1)
df_clean = df.dropna(subset=['Group', 'POD']).copy()

y_true = (df_clean['Group'].astype(str).str.lower().str.contains('crc')).astype(int).values
y_prob_raw = pd.to_numeric(df_clean['POD'], errors='coerce').fillna(0.5).values

N = len(y_true)
n_cases = int(np.sum(y_true))
p_study = n_cases / float(N) # 41 / 110 = 0.3727

cea_sens = 0.855
cea_spec = 0.561

# Target population prevalence scenarios for symptomatic <50 population (Patel et al. 2021; Chen et al. 2023):
# 1% (primary care mild symptoms), 2% (secondary care general GI), 5% (high-risk referral), 10% (colonoscopy triage enriched)
prevalence_scenarios = [0.01, 0.02, 0.05, 0.10]
thresholds = np.linspace(0.01, 0.30, 30)

records = []
for p0 in prevalence_scenarios:
    # Bayesian recalibration logit shift: logit(p0/(1-p0)) - logit(p_study/(1-p_study))
    logit_shift = np.log(p0 / (1.0 - p0)) - np.log(p_study / (1.0 - p_study))
    raw_clipped = np.clip(y_prob_raw, 1e-6, 1.0 - 1e-6)
    logit_recal = np.log(raw_clipped / (1.0 - raw_clipped)) + logit_shift
    p_recal = 1.0 / (1.0 + np.exp(-logit_recal))
    
    for pt in thresholds:
        w = pt / (1.0 - pt)
        
        # Treat all & treat none under target prevalence p0
        nb_all = p0 - (1.0 - p0) * w
        nb_none = 0.0
        
        # CEA net benefit under target prevalence p0
        nb_cea = (cea_sens * p0) - ((1.0 - cea_spec) * (1.0 - p0)) * w
        
        # Empirical sensitivity & specificity of microbiome model at threshold pt (using recalibrated risk)
        pred_mb = (p_recal >= pt).astype(int)
        tp = np.sum((pred_mb == 1) & (y_true == 1))
        fn = np.sum((pred_mb == 0) & (y_true == 1))
        tn = np.sum((pred_mb == 0) & (y_true == 0))
        fp = np.sum((pred_mb == 1) & (y_true == 0))
        
        sens_mb = tp / max(1, tp + fn)
        spec_mb = tn / max(1, tn + fp)
        
        # Prevalence-weighted Net Benefit:
        nb_mb = (sens_mb * p0) - ((1.0 - spec_mb) * (1.0 - p0)) * w
        
        # Net reduction in avoidable colonoscopies per 100 patients: (NB_mb - NB_all) / w * 100
        reduction_per_100 = max(0.0, (nb_mb - max(nb_all, 0.0)) / w * 100.0) if w > 0 else 0.0
        
        records.append({
            'Target_Prevalence': p0,
            'Threshold_Pt': round(float(pt), 4),
            'Odds_Weight': round(float(w), 4),
            'NB_Treat_None': 0.0,
            'NB_Treat_All': round(float(nb_all), 6),
            'NB_CEA': round(float(nb_cea), 6),
            'Microbiome_Sensitivity': round(float(sens_mb), 4),
            'Microbiome_Specificity': round(float(spec_mb), 4),
            'NB_Microbiome_Recalibrated': round(float(nb_mb), 6),
            'Avoidable_Colonoscopies_Saved_Per_100': round(float(reduction_per_100), 2)
        })

df_transport = pd.DataFrame(records)
df_transport.to_csv('22_final_independent_audit/09_dca_reanalysis/dca_prevalence_transported.tsv', sep='	', index=False)
print('Saved dca_prevalence_transported.tsv with', len(df_transport), 'rows.')

# Print key comparison at pt = 0.05 and pt = 0.10 across scenarios
print('\n=== Prevalence-Transported Net Benefit Summary ===')
for p0 in [0.02, 0.05, 0.10]:
    sub = df_transport[df_transport['Target_Prevalence'] == p0]
    for pt in [0.02, 0.05, 0.10]:
        r = sub.iloc[(sub['Threshold_Pt'] - pt).abs().argsort()[:1]].iloc[0]
        print(f"Prev={p0*100:.0f}% | pt={r['Threshold_Pt']:.2f} | NB_All={r['NB_Treat_All']:.4f} | NB_CEA={r['NB_CEA']:.4f} | NB_Microbiome={r['NB_Microbiome_Recalibrated']:.4f} | Colonoscopies Saved/100={r['Avoidable_Colonoscopies_Saved_Per_100']:.1f}")
