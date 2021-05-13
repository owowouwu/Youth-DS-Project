import pandas as pd
from sklearn.feature_selection import mutual_info_regression
import numpy as np


# LGA areas
df = pd.read_csv('../wrangled/LGA_data.csv', index_col = 'LGA')
df = df.dropna()
indep_var = ['Depression Rate']
dep_vars = df.columns.difference(indep_var).to_list()

#print(df[indep_var].tolist())

#print(mutual_info_regression(df[indep_var], df[dep_vars[1]]))

miDf = pd.DataFrame(columns = df.columns)

for var0 in df.columns:
    mi_list = [float(mutual_info_regression(df[[var0]], df[var])) for var in df.columns]
    miDf[var0] = mi_list

print(miDf.head())