import pandas as pd

df = pd.read_csv('../wrangled/LGA_data.csv', index_col = 'LGA')
df = df.dropna()

cf = df.corr(method='pearson')

print(cf)