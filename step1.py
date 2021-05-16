# -*- coding: utf-8 -*-

"""
processes x_raw.xlsx by into a standard format
"""

import pandas as pd

# processing the aedc_raw excel file
aedc = pd.read_excel('./wrangled/AEDC_raw.xlsx')
aedc['LGA'] =  aedc['LGA'].replace('\([a-zA-Z.]*\)','', regex = True)
aedc = aedc.loc[:, ~aedc.columns.str.match('Unnamed')]
aedc = aedc.dropna()
aedc['LGA'] = aedc['LGA'].str.strip()
aedc = aedc.set_index('LGA')
# dropped here to remove incomplete data
aedc = aedc.drop('Queenscliffe')
aedc.to_csv('./wrangled/AEDC.csv')

# processing the depression_raw excel file
depression = pd.read_excel('./wrangled/depression_raw.xlsx', engine = 'openpyxl')
depression = depression.drop([0,1])
depression = depression[['Unnamed: 0','Persons']]
depression = depression.rename(columns={'Unnamed: 0': 'LGA', 'Persons': 'Depression Rate'})
depression['LGA'] = depression['LGA'].replace('\([a-zA-Z]*\)','', regex = True)
depression['LGA'] = depression['LGA'].str.strip()
depression = depression.set_index('LGA')
depression = depression.drop('Victoria')
depression.to_csv('./wrangled/depression.csv')