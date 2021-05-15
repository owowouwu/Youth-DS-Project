import pandas as pd

df = pd.read_csv("../wrangled/LGA_data.csv.csv")

ascCols=['connectedness', 'yr12completion'] # higher the better cols
df[ascCols].rank()
df.columns.difference(ascCols).rank()
# normalise
max(df[ascCols].rank())-df[ascCols].rank()
max(df.columns.difference(ascCols).rank())-df.columns.difference(ascCols).rank()
# ranksum
df['RankSum'] = df.sum(axis=1)
df.to_csv('../wrangled/LGArank.csv')