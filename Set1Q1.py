#import libraries
import pandas as pd

# Import data from .csv file
cscores = pd.read_csv("Cricket_Scores.csv",sep =",", header=0)

# displaying dataframe
print(cscores)

