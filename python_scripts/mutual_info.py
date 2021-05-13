import pandas as pd
from sklearn.feature_selection import mutual_info_regression


# LGA areas
df = pd.read_csv('../wrangled/LGA_data.csv', index_col = 'LGA')
df = df.dropna()
indep_var = ['Depression Rate']
dep_vars = df.columns.difference(indep_var).to_list()

#print(df[indep_var].tolist())

#print(mutual_info_regression(df[indep_var], df[dep_vars[1]]))

for var in dep_vars:
    print((var, float(mutual_info_regression(df[indep_var], df[var]))))
    
