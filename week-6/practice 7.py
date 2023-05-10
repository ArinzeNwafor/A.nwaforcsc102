# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("bcg.cs")

df = data.head(1)

# print excel
print(df)