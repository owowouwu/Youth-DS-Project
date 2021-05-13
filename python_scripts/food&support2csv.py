import pandas as pd

def p2f(x):
    return (x.strip('%'))/100

def x2csv(name, sheet = 0):
    path = './raw_data/VCAMS_'+name+'.xlsx'
    df = pd.read_excel(path, sheet_name=sheet)
    df = df.loc[:, ~df.columns.str.match('Unnamed')]
    df = df[~df['DHS AREA'].str.contains('Victoria')]
    df['DHS AREA'] = df['DHS AREA'].replace('\([a-zA-Z]*\)', '', regex=True)
    df['DHS AREA'] = df['DHS AREA'].str.strip()
    df = df.set_index('DHS AREA')

    df['Indicator_Calc', 'RSE'] = pd.to_numeric(df['Indicator_Calc', 'RSE'], errors='ignore')
    df['Indicator_Calc', 'RSE'] = p2f(df['Indicator_Calc', 'RSE'])
    return df.to_csv('../wrangled/'+name+'.csv')