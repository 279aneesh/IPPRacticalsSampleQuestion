# import library
import pandas as pd

# Creating Dictionary with Given Values
items = {'Dept_id': [101, 102, 103, 104],
        'Unit_name': ['TV', 'Washingmachine', 'Oven', 'AC'],
        'Production': [20000, 15000, 15000, 17000],
        'Sales': [18000, 12000, 14000, 17000]}

# Creating a Data Frame from dictionary
itemsDF=pd.DataFrame(items)

# displaying dataframe
print(itemsDF)

# Saving Data Frame as csv

itemsDF.to_csv(path_or_buf='items.csv', sep=',')