# -*- coding: utf-8 -*-
"""
procceses a VCAMS excel spreadsheet

factor - the name of the factor (given the filename looks like VCAMS_factor.xlsx)
year - the year of interest
sheet - some excel files have multiple sheets, we choose one

"""

import pandas as pd
import numpy as np

def p2f(x):
    return (x.strip('%'))/100

def vcamsLGA(factor, year, sheet = 0):
    path = '../raw_data/VCAMS_'+factor+'.xlsx'
    df = pd.read_excel(path, sheet_name=sheet)
    # remove unnamed rows
    df = df.loc[:, ~df.columns.str.match('Unnamed')]
    # remove aggregates (victoria)
    df = df[~df['LGA'].str.contains('Victoria')]
    df = df[df['Year'] == year]
    df['LGA'] = df['LGA'].replace('\([a-zA-Z]*\)','', regex = True)
    df['LGA'] = df['LGA'].str.strip()
    df = df.set_index('LGA')
    df.loc[df['Indicator'] == 'NDP'] = np.nan
    df['Indicator'] = pd.to_numeric(df['Indicator'])
    df = df.drop(['Numerator', 'Denominator', 'Year'], axis =1).rename({'Indicator': factor}, axis = 1)
    return df

def vcamsDHS(name, year, sheet = 0):
    path = '../raw_data/VCAMS_'+name+'.xlsx'
    df = pd.read_excel(path, sheet_name=sheet)
    df = df.loc[:, ~df.columns.str.match('Unnamed')]
    df = df[~df['DHS AREA'].str.contains('Victoria')]
    df['DHS AREA'] = df['DHS AREA'].replace('\([a-zA-Z]*\)', '', regex=True)
    df['DHS AREA'] = df['DHS AREA'].str.strip()
    df = df.drop(['RSE', 'Year'], axis=1)
    df = df.set_index('DHS AREA')
    df['Indicator'] = pd.to_numeric(df['Indicator'], errors='ignore')
    df = df.rename({'Indicator': name})
    return df


