# -*- coding: utf-8 -*-
"""
Created on Sun May 16 21:13:56 2021

@author: Steven
"""
from sklearn.preprocessing import StandardScaler
from scipy.stats import linregress
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd


std_scaler = StandardScaler()
df = pd.read_csv("./wrangled/LGA_data.csv", index_col = "LGA")
vicLGA = gpd.read_file('./shapefiles/VIC_LGA_POLYGON_SHP.shp')
zScores = pd.DataFrame(std_scaler.fit_transform(df), columns = df.columns, index = df.index)

# higher is better
asec = ['yr12completion, connectedness']
# lower is better
desc = zScores.columns.difference(asec)

# for the features for which the lower the score, the better, we append a negative
zScores[desc] = -zScores[desc]

# not relevant
zScores = zScores.drop('tsRatio', axis=1)

# calculate an overall score by taking an avergae
zScores['overallZ'] = zScores.mean(axis=1)
zScores.index = zScores.index.str.upper()


plt.figure(figsize = (20,20))
plottingLGA = vicLGA.merge(zScores, left_on = 'ABB_NAME', right_on = 'LGA')
plottingLGA.plot(column = 'overallZ', legend=True,cmap='OrRd', legend_kwds={'label': "Youth Liveability Score"})
# removes tick marks
plt.xticks([])
plt.yticks([])
plt.box(False)
plt.savefig('./plots/scoremap.png')

plt.figure(figsize=(20,12))
zScores = zScores.sort_values(by = 'overallZ', ascending=False)
plt.bar(zScores.index, zScores['overallZ'])
plt.xticks(np.arange(len(zScores.index)), zScores.index, rotation = 80)
plt.ylabel("Youth Liveability Score")
plt.savefig('./plots/scorehistogram.png')

plt.figure()
plt.scatter(zScores['overallZ'], df['Depression Rate'])
plt.xlabel("Overall Youth Liveability Index")
plt.ylabel("Depression Rate")
plt.savefig('./plots/overallscatter.png')

