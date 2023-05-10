# import pandas package

import pandas as pd

# Define a dictionary into DataFrame
data = {'Name': ['Clem', 'Prince', 'Edward', 'Adele'],
        'Age': [27, 24, 22, 32],
        'Address': ['Abuja', 'Kano', 'Minna', 'Lagos'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# select two columns
print(df[['Name', 'Qualification']])
