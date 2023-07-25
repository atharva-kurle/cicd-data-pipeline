import pandas as pd

df = pd.read_csv('titanic.csv')

survived_df = df.loc[df['Survived']=1]

survived_df.to_csv('survivedPassangers.csv')
