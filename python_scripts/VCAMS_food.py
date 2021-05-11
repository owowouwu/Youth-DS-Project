import pandas as pd

df = pd.read_excel('../raw_data/VCAMS_food.xlsx')
food = df.iloc[:, :18]
food = pd.to_numeric(food, errors='ignore')
food = food[['DHS AREA', 'Indicator_Calc', 'RSE']]
food = df.set_index('DHS AREA')

def p2f(x):
    return (x.strip('%'))/100

food = p2f(food[['DHS AREA', 'Indicator_Calc', 'RSE']])
food.to_csv('../wrangled/food.csv')

df = pd.read_excel('../raw_data/VCAMS_support.xlsx')
support = df.iloc[:, :18]
support = pd.to_numeric(food, errors='ignore')
support = food[['DHS AREA', 'Indicator_Calc', 'RSE']]
support = df.set_index('DHS AREA')

support = p2f(food[['DHS AREA', 'Indicator_Calc', 'RSE']])
support.to_csv('../wrangled/support.csv')
