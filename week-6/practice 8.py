# importing pandas as pd
import pandas as pd

# dictionary of lists
dict = {'name': ["Abdul", "Chukwuemeka", "Seyi", "Matt"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score': [90, 40, 80, 98]}

# creating a dataframe from a dictionary
df = pd.DataFrame(dict)

# iterating over rows using iterrows() function
for i, j in df.iterrows():
    print(i, j)
    print()