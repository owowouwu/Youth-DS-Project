import pandas as pd

df = pd.read_csv("../wrangled/LGA_data.csv.csv")

ascCols=['connectedness', 'yr12completion']
df[ascCols].rank()
df.columns.difference(ascCols).rank()
df.to_csv('../wrangled/LGArank.csv')