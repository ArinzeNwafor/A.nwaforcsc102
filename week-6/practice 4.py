import pandas as pd

# Define a dictionary containing employee data
data = {'Name': ['Oyin', 'Mary', 'David', 'Bola'],
        'Age': [27, 24, 22, 32],
        'Address': ['Asaba', 'Maiduguri', 'Onitsha', 'Kwara'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# select first row
print(df.iloc[1])