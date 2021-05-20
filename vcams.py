# -*- coding: utf-8 -*-
"""
module with all functions
"""

import pandas as pd
import numpy as np

def p2f(x):
    return (x.strip('%'))/100

def LGA(factor, year, sheet = 0):
    path = './raw_data/vcamsLGA/VCAMS_'+factor+'.xlsx'
    df = pd.read_excel(path, sheet_name=sheet)
    df = df[['Year', 'LGA', 'Indicator']]
    # remove aggregates (victoria)
    df = df[~df['LGA'].str.contains('Victoria')]
    df = df[df['Year'] == year]
    df['LGA'] = df['LGA'].replace('\([a-zA-Z]*\)','', regex = True)
    df['LGA'] = df['LGA'].str.strip()
    df = df.set_index('LGA')
    df.loc[df['Indicator'] == 'NDP'] = np.nan
    df['Indicator'] = pd.to_numeric(df['Indicator'])
    df = df.rename({'Indicator': factor}, axis = 1)
    df= df.drop('Year', axis=1)
    return df

def DHS(name, year=2014, sheet = 0):
    path = './raw_data/vcamsDHS/VCAMS_'+name+'.xlsx'
    df = pd.read_excel(path, sheet_name=sheet)
    df = df[df['Year'] == year]
    df = df.loc[:, ~df.columns.str.match('Unnamed')]
    df = df[~df['DHS AREA'].str.contains('Victoria')]
    df['DHS AREA'] = df['DHS AREA'].replace('Area', '', regex=True)
    df['DHS AREA'] = df['DHS AREA'].str.strip()
    # need to rename to more recent name
    df = df.drop(['RSE', 'Year'], axis=1)
    df = df.set_index('DHS AREA')
    df.loc[df['Indicator'] == 'NDP'] = np.nan
    df['Indicator'] = pd.to_numeric(df['Indicator'], errors='ignore')
    df = df.rename(columns={'Indicator': name}, index = {'Western District': 'Wimmera South West'})
    return df
