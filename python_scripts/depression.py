import pandas as pd

df = pd.read_excel('../wrangled/depression_raw.xlsx', engine = 'openpyxl')

df = df.drop([0,1])
df = df[['Unnamed: 0','Persons']]
df = df.rename(columns={'Unnamed: 0': 'LGA', 'Persons': 'Depression Rate'})

df['LGA'] = df['LGA'].replace('\([a-zA-Z]*\)','', regex = True)
df['LGA'] = df['LGA'].str.strip()

df = df.set_index('LGA')
df = df.drop('Victoria')

df.to_csv('../wrangled/depression.csv')