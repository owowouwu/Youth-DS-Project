# -*- coding: utf-8 -*-

"""
processes aedc_raw.xlsx by into a standard format
"""

import pandas as pd

df = pd.read_excel('../wrangled/AEDC_raw.xlsx')
df['LGA'] =  df['LGA'].replace('\([a-zA-Z.]*\)','', regex = True)
df = df.dropna()
df['LGA'] = df['LGA'].str.strip()
df = df.set_index('LGA')
# dropped here to remove incomplete data
df = df.drop('Queenscliffe')
df.to_csv('../wrangled/AEDC.csv')