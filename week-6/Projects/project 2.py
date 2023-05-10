import pandas as pd

cadbury = {'SEGMENTS': ['Refereshment Beverages', 'Confectionery', 'Intermediate Cocoa Products'],
           'PRODUCTS' : ['Bournvita and Hot Chocolate', ' Tom Tom and Buttermint', 'Cocoa powder, Cocoa butter, Cocoa liquor and Cocoa Cake'],
           'BRANDS' : ['Cadbury-Bournvita and Cadbury 3 in 1 Hot-Chocolate', 'Tom Tom Classic, Tom Tom Strawberry and Buttermint', 'Cocoa Powder and Cocoa Butter'],
           'EXPORT' : ['Non-Export Product', 'Non-Export Product', 'Export Product']}

df = pd.DataFrame(cadbury)

df.to_csv("Cadbury_market.csv")
print(df)