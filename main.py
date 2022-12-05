import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import seaborn.objects as so

# Create a heatmap of the studs_found data
# Open the csv file as a Pandas dataframe 
df = pd.read_csv('studs_found1.csv', index_col=False, dtype=int, header=0)

# Display heatmap
heat = sns.heatmap(df)
plt.show()