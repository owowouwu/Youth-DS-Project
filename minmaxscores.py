# -*- coding: utf-8 -*-
"""
Created on Tue May 18 19:23:07 2021

@author: steve
"""

from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
from sklearn.cluster import KMeans

minMax = MinMaxScaler()

df = pd.read_csv("./wrangled/LGA_data.csv", index_col = "LGA")
vicLGA = gpd.read_file('./shapefiles/VIC_LGA_POLYGON_SHP.shp')
minMaxScore = pd.DataFrame(minMax.fit_transform(df), columns = df.columns, index = df.index)

# higher is better
asec = ['yr12completion, connectedness']
# lower is better
desc = minMaxScore.columns.difference(asec)

# for the features for which the lower the score, the better, we append a negative
minMaxScore[desc] = 1 - minMaxScore[desc]

# not relevant
minMaxScore = minMaxScore.drop('tsRatio', axis=1)

# calculate an overall score by taking an avergae
minMaxScore['index'] = minMaxScore.mean(axis=1)
minMaxScore.index = minMaxScore.index.str.upper()


plt.figure(figsize = (20,20))
plottingLGA = vicLGA.merge(minMaxScore, left_on = 'ABB_NAME', right_on = 'LGA')
plottingLGA.plot(column = 'index', legend=True,cmap='viridis', legend_kwds={'label': "Youth Liveability Score"})
# removes tick marks
plt.xticks([])
plt.yticks([])
plt.box(False)
plt.savefig('./plots/scoremapminMax.png')

plt.figure()
plt.scatter(minMaxScore['index'], df['Depression Rate'])
plt.xlabel("Overall Youth Liveability Index")
plt.ylabel("Depression Rate")
plt.savefig('./plots/overallscatterminMax.png')

# kmeans clustering
np.random.seed(111111111)
kmeans = KMeans(n_clusters = 3)
clusters = kmeans.fit(np.array(plottingLGA['index']).reshape(-1,1)).labels_
clusterdict = {1: "Low Scoring", 0: "Average Scoring", 2: "High Scoring"}
clusterLabeled = [clusterdict[i] for i in clusters]
plottingLGA['clusters'] = clusterLabeled
plottingLGA.plot(column = 'clusters',categorical=True,legend=True,cmap='viridis', legend_kwds={'frameon': False})
# removes tick marks
plt.xticks([])
plt.yticks([])
plt.box(False)
plt.savefig('./plots/kmeansminMax.png')
