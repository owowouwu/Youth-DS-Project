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
from sklearn.cluster import KMeans


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
plottingLGA.plot(column = 'overallZ', legend=True,cmap='viridis', legend_kwds={'label': "Youth Liveability Score"})
# removes tick marks
plt.xticks([])
plt.yticks([])
plt.box(False)
plt.savefig('./plots/scoremap.png')

plt.figure()
plt.scatter(zScores['overallZ'], df['Depression Rate'])
plt.xlabel("Overall Youth Liveability Index")
plt.ylabel("Depression Rate")
plt.savefig('./plots/overallscatter.png')

# kmeans clustering
np.random.seed(111111111)
kmeans = KMeans(n_clusters = 3)
clusters = kmeans.fit(np.array(plottingLGA['overallZ']).reshape(-1,1)).labels_
clusterdict = {1: "Low Scoring", 0: "Average Scoring", 2: "High Scoring"}
clusterLabeled = [clusterdict[i] for i in clusters]
plottingLGA['clusters'] = clusterLabeled
plottingLGA.plot(column = 'clusters',categorical=True,legend=True,cmap='viridis', legend_kwds={'frameon': False})
# removes tick marks
plt.xticks([])
plt.yticks([])
plt.box(False)
plt.savefig('./plots/kmeans.png')
