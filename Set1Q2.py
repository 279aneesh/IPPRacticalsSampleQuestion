#import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Import data from .csv file
cscoresdf = pd.read_csv("Cricket_Scores.csv",sep =",", header=0)

#Creating a New DataFrame for plotting a graph without S No
cscoresgraph = cscoresdf.drop(columns=['S no'])

# converting dataframe as bar graph
cscoresgraph.plot(kind="bar", x="Batsmen")

# adding label in x axis
plt.xlabel("Name")

# adding label in y axis
plt.ylabel("Runs")

# adding name to the bar graph
plt.title("Cricket Scores")

# display bar graph
plt.show()



