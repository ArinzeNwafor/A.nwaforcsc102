# importing pandas as pd
import pandas as pd

# dictionary of lists
records = {'name': ["Abel", "Kamsi", "Oyode", "Chinelo"],
           'degree': ["MBA", "BCA", "M.Tech", "MBA"],
           'score': [90, 40, 80, 98]}

# creating a dataframe from a dictionary
df = pd.DataFrame(records)

# saving the dataframe
df.to_csv('record.csv')