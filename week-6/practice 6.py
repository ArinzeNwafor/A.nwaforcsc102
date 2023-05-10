# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("employee_records.csv")

df = data.iloc[0]

# print excel
print(df)