
import pandas as pd
import numpy as np
import os

os.makedirs('22_final_independent_audit/08_ml_reanalysis', exist_ok=True)

xls = pd.ExcelFile('02_metadata/41467_2021_27112_MOESM8_ESM.xlsx')
df = pd.read_excel(xls, sheet_name='Figure 5b')
df_clean = df.iloc[1:].copy()
df_clean.columns = ['Taxon_16S_Raw', 'Mean_Decrease_Accuracy']

records = []
for idx, r in df_clean.iterrows():
    tax = str(r['Taxon_16S_Raw']).strip()
    mda = float(r['Mean_Decrease_Accuracy'])
    parts = tax.split('.')
    lowest = parts[-1]
    
    if lowest.startswith('s__'):
        rank_16s = 'Species'
        clean_name = lowest.replace('s__', '')
        shotgun_counterpart = clean_name
        resolution = 'Species-level sequence match (high fidelity)'
        status = 'Valid 1:1 Species Mapping'
    elif lowest.startswith('g__'):
        rank_16s = 'Genus'
        clean_name = lowest.replace('g__', '').replace('*', '').replace('#', '').strip('[]')
        shotgun_counterpart = f'{clean_name} spp. (aggregated species abundance)'
        resolution = 'Genus-level resolution (16S V3-V4 cannot disambiguate multi-species clade)'
        status = 'Genus-Aggregated Mapping'
    elif lowest.startswith('f__'):
        rank_16s = 'Family'
        clean_name = lowest.replace('f__', '').replace('*', '').replace('#', '')
        shotgun_counterpart = f'{clean_name} unclassified family members'
        resolution = 'Family-level resolution (coarse taxonomic clade)'
        status = 'Family-Level Coarse Mapping'
    else:
        rank_16s = 'Order/Higher'
        clean_name = lowest
        shotgun_counterpart = 'Higher taxonomic aggregate'
        resolution = 'High-order phylogenetic clade'
        status = 'High-Order Coarse Mapping'
        
    records.append({
        'Marker_Index': len(records) + 1,
        'Taxon_16S_Raw': tax,
        'Rank_16S': rank_16s,
        'Extracted_Taxon_Name': clean_name,
        'Mean_Decrease_Accuracy': round(mda, 4),
        'Shotgun_MetaPhlAn_Counterpart': shotgun_counterpart,
        'Cross_Platform_Resolution': resolution,
        'Huadong_Platform_Reliability': 'Reliable at 16S genus/ASV rank; cannot achieve 1:1 shotgun species identity',
        'Audit_Classification': status
    })

df_out = pd.DataFrame(records)
df_out.to_csv('22_final_independent_audit/08_ml_reanalysis/cross_platform_feature_mapping.tsv', sep='	', index=False)
print('Saved cross_platform_feature_mapping.tsv with', len(df_out), 'features.')
print('\nTaxonomic rank breakdown among 61 locked ML markers:')
print(df_out['Rank_16S'].value_counts())
print('\nAudit classification breakdown:')
print(df_out['Audit_Classification'].value_counts())
