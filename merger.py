# -*- coding: utf-8 -*-
"""
Created on Wed May 12 16:17:12 2021

merges all tables together

"""

import vcams
import pandas as pd 
import numpy as np

# LGA processing
depressionDHS = pd.read_csv('./wrangled/depression2018DHS.csv')
depressionDHS['DHS AREA'] = depressionDHS['DHS AREA'].replace('Area', '', regex=True)
depressionDHS['DHS AREA'] = depressionDHS['DHS AREA'].str.strip()
depressionDHS = depressionDHS.set_index('DHS AREA')

filesDHS = files = {k: int(v) for line in open('./raw_data/vcamsDHS/names.txt', "r") for (k,v) in [line.split()]}
vcams_DHS_data = [vcams.DHS(i, year = files[i]) for i in files.keys()]
DHS_data = depressionDHS.join(vcams_DHS_data)
DHS_data.to_csv('./wrangled/DHS_data.csv')

# DHS processing
tsratio = pd.read_csv('./wrangled/tsRatio.csv', index_col = 0)
depression = pd.read_csv('./wrangled/depression.csv', index_col = 'LGA')
absences = pd.read_csv('./wrangled/absences.csv', index_col = 'LGA')
aedc = pd.read_csv('./wrangled/AEDC.csv', index_col = 'LGA')
LGAfiles = {k: int(v) for line in open('./raw_data/vcamsLGA/names.txt', "r") for (k,v) in [line.split()]}
vcams_LGA_data = [vcams.LGA(i, year = LGAfiles[i]) for i in LGAfiles.keys()]
LGA_data = depression.join(vcams_LGA_data).join(aedc).join(tsratio).join(absences)
LGA_data.to_csv('./wrangled/LGA_data.csv')