import pandas as pd
from sklearn.feature_selection import mutual_info_regression

df = pd.read_csv('../wrangled/fullTable.csv')

wanted_cols = ['LGA', 'Depression Rate', 'Social (vulnerable)', 'Language (vulnerable)', 'Communication (Vulnerable)', 'Emotional (Vulnerable)', 'Health (Vulnerable)', 'tsRatio', 'bullying', 'connectedness', 'familystress']

df = df[wanted_cols].set_index('LGA')
df = df.drop(['Queenscliffe', 'Mansfield', 'Pyrenees', 'West Wimmera'])

indep_var = ['Depression Rate']
dep_vars = df.columns.difference(indep_var).to_list()

#print(df[indep_var].tolist())

#print(mutual_info_regression(df[indep_var], df[dep_vars[1]]))


for var in dep_vars:
    print((var, float(mutual_info_regression(df[indep_var], df[var]))))