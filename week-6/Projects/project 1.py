import pandas as pd

data = pd.read_csv("Top apps.csv")

df = data.iloc[0 : 7]


print(df)

dat = pd.read_csv("dataset.csv")

dg = dat.iloc[0 : 7]

print(dg)