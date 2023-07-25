import pandas as pd

df = pd.read_csv('titanic.csv')

survived_df = df.loc[df['Survived']==1]

print('These are the survived passangers')
print(survived_df))

survived_df.to_csv('survivedPassangers.csv')
print('Export successfull!')
