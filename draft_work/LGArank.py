import pandas as pd

df = pd.read_csv("../wrangled/LGA_data.csv")
rankDf = df.copy()

ascCols=['connectedness', 'yr12completion'] # higher the better cols
rankDf[ascCols] = df[ascCols].rank()
rankDf[df.columns.difference(ascCols)] = df[df.columns.difference(ascCols)].rank()
# normalise
#rankDf[ascCols] = max(rankDf[ascCols])-rankDf[ascCols]
#rankDf[ascCols] = max(rankDf[df.columns.difference(ascCols)])-rankDf[df.columns.difference(ascCols)]
# ranksum
#rankDf['RankSum'] = rankDf.sum(axis=1)
#rankDf.to_csv('../wrangled/LGArank.csv')