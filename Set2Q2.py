# import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Creating Dictionary with Given Values
items = {'Dept_id': [101, 102, 103, 104],
         'Unit_name': ['TV', 'Washingmachine', 'Oven', 'AC'],
         'Production': [20000, 15000, 15000, 17000],
         'Sales': [18000, 12000, 14000, 17000]}

# Creating a Data Frame from dictionary
itemsDF = pd.DataFrame(items)

# Creating a New DataFrame for plotting a graph without Dept_id
itemsGraph = itemsDF.drop(columns=['Dept_id'])

# converting dataframe as bar graph
itemsGraph.plot(kind="bar", x="Unit_name", rot=0)

# adding label in x axis
plt.xlabel("Unit Name")

# adding label in y axis
plt.ylabel("Number of Units")

# adding name to the bar graph
plt.title("Production and Sales")

# display bar graph
plt.show()
