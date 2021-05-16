# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
from sklearn.feature_selection import mutual_info_regression as mi_reg
from pandas.plotting import parallel_coordinates

dhsData = pd.read_csv("./wrangled/DHS_data.csv", index_col = "DHS AREA")
lgaData = pd.read_csv("./wrangled/LGA_data.csv", index_col = "LGA")
vicLGA = gpd.read_file('./shapefiles/VIC_LGA_POLYGON_SHP.shp')
vicDHS = gpd.read_file('./shapefiles/VIC_DHS_POLYGON_SHP.shp')

plt.figure(figsize = (20,20))
for i in lgaData.columns[1:]:
    plt.scatter(lgaData[i], lgaData['Depression Rate'])
    plt.ylabel('Depression Rate')
    plt.xlabel(i)
    plt.savefig('./plots/depression/'+i+'.png')

# aedc pair plots
plt.clf()
sns.pairplot(lgaData[['aedcSocial', 'aedcLanguage', 'aedcEmotion', 'aedcComm', 'aedcHealth']])
plt.savefig('./plots/aedc.png')

# vic depression map
plt.clf()
lgaData.index = lgaData.index.str.upper()
plottingLGA = vicLGA.merge(lgaData[['Depression Rate']], left_on = 'ABB_NAME', right_on = 'LGA')
plt.figure(figsize = (20,20))
plottingLGA.plot(column = 'Depression Rate', legend=True,cmap='OrRd')
# removes tick marks
plt.xticks([])
plt.yticks([])
plt.box(False)
plt.savefig('./plots/depressionMap.png')

# correlation heatmap
for_corr = lgaData.copy()
for_corr = for_corr.dropna()
cf = for_corr.corr(method='pearson')
plt.clf()
sns.heatmap(cf)
plt.savefig('./plots/correlationMap.png')

# parallel coordinate plots
normalized_LGA=(lgaData-lgaData.min())/(lgaData.max()-lgaData.min())
normalized_LGA['bins'] = pd.cut(normalized_LGA['Depression Rate'], 3, labels=["low", "medium", "high"])
plt.clf()
parallel_coordinates(normalized_LGA, 'bins',
                     alpha=0.2, color=["b","y",'r'])
plt.xticks(rotation=45)
plt.show()
plt.savefig('./plots/parallel.png')