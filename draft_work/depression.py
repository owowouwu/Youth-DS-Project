import pandas as pd

depression = pd.read_excel('../wrangled/depression_raw.xlsx', engine = 'openpyxl')

depression = depression.drop([0,1])
depression = depression[['Unnamed: 0','Persons']]
depression = depression.rename(columns={'Unnamed: 0': 'LGA', 'Persons': 'Depression Rate'})

depression['LGA'] = depression['LGA'].replace('\([a-zA-Z]*\)','', regex = True)
depression['LGA'] = depression['LGA'].str.strip()

depression = depression.set_index('LGA')
depression = depression.drop('Victoria')

depression.to_csv('../wrangled/depression.csv')