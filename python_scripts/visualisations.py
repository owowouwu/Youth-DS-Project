# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

aedc = pd.read_csv('../wrangled/AEDC.csv', index_col = 'LGA')
tsdr = pd.read_csv('../wrangled/tsdr.csv', index_col = 0)
vcams = pd.read_csv('../wrangled/vcams.csv', index_col = 'LGA')
depression = pd.read_csv('../wrangled/depression.csv', index_col = 'LGA')
tsratio = pd.read_csv('../wrangled/tsRatio.csv', index_col = 0)

table = depression.join([aedc, tsratio, vcams])
table = table.apply(pd.to_numeric)


for i in table.columns[1:]:
    plt.scatter(table[i], table['Depression Rate'])
    plt.ylabel('Depression Rate')
    plt.xlabel(i)
    plt.show()