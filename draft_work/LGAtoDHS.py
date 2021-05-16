# Creates dictionary that matches LGA to DHS area

import pandas as pd
from collections import defaultdict

df = pd.read_excel('../raw_data/LGA-DHS.xlsx', engine = 'openpyxl')
df = df[['LGA Name', 'Departmental Area']]

# Preprocess LGA names

df['LGA Name'] = df['LGA Name'].replace('\([a-zA-Z]*\)','', regex = True).str.strip()

LGAtoDHS = {}
DHStoLGA = defaultdict(list)

for i in range(len(df)):
    LGAtoDHS[df.iloc[i, 0]] = df.iloc[i,1]
    DHStoLGA[df.iloc[i, 1]].append(df.iloc[i,0])
    
df = pd.read_csv('../wrangled/depression.csv')

df['DHS_Area'] = df.LGA.map(LGAtoDHS)
df = df.set_index('LGA')

df.to_csv('../wrangled/depression2.csv')