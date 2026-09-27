
import pandas as pd
import numpy as np
from scipy import stats
import os

os.makedirs('22_final_independent_audit/03_taxonomy_reanalysis', exist_ok=True)

df_clf = pd.read_csv('05_taxonomy/species_interaction_classification.tsv', sep='	')
df_eq = pd.read_csv('22_final_independent_audit/03_taxonomy_reanalysis/species_concordance_equivalence.tsv', sep='	')
df_81 = pd.merge(df_clf[df_clf['classification'] == 'Shared_CRC_Signature'], df_eq, on='taxon').copy()

pooled_sd = np.sqrt((np.var(df_81['z_young_mean']) + np.var(df_81['z_older_mean'])) / 2.0)
df_81['cohen_d'] = (df_81['z_young_mean'] - df_81['z_older_mean']) / pooled_sd

# Standard error for Cohen's d in two-group interaction
# N_eff young ~ 260, N_eff older ~ 750
se_d = 0.075

rows = []
for idx, r in df_81.iterrows():
    taxon = r['taxon']
    z_y = r['z_young_mean']
    z_o = r['z_older_mean']
    delta_z = z_y - z_o
    d_val = r['cohen_d']
    sign_conc = 1 if np.sign(z_y) == np.sign(z_o) else 0
    
    row = {
        'taxon': taxon,
        'z_young': round(z_y, 4),
        'z_older': round(z_o, 4),
        'delta_z': round(delta_z, 4),
        'cohen_d': round(d_val, 4),
        'sign_concordance': sign_conc
    }
    
    for margin in [0.20, 0.25, 0.30]:
        z1 = (d_val - (-margin)) / se_d
        z2 = (margin - d_val) / se_d
        p1 = 1 - stats.norm.cdf(z1)
        p2 = 1 - stats.norm.cdf(z2)
        p_tost = max(p1, p2)
        
        ci_lower = d_val - 1.645 * se_d
        ci_upper = d_val + 1.645 * se_d
        
        if p_tost < 0.05:
            call = 'Equivalent'
        elif (ci_lower > margin) or (ci_upper < -margin):
            call = 'Non-Equivalent'
        else:
            call = 'Inconclusive'
            
        m_str = f'{margin:.2f}'
        row[f'p_tost_m{m_str}'] = round(p_tost, 4)
        row[f'ci90_low_m{m_str}'] = round(ci_lower, 4)
        row[f'ci90_high_m{m_str}'] = round(ci_upper, 4)
        row[f'status_m{m_str}'] = call
        
    rows.append(row)

df_out = pd.DataFrame(rows)
df_out.to_csv('22_final_independent_audit/03_taxonomy_reanalysis/equivalence_margin_sensitivity.tsv', sep='	', index=False)
print('Saved equivalence_margin_sensitivity.tsv with', len(df_out), 'taxa.')

# Print summary table
for m in ['0.20', '0.25', '0.30']:
    print(f'=== Margin +/-{m} ===')
    print(df_out[f'status_m{m}'].value_counts())
