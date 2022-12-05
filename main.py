import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import seaborn.objects as so

# Create a heatmap of the studs_found data

# Open the csv file as a Pandas dataframe
df = pd.read_csv('studs_found.csv')

df = pd.DataFrame(df.pivot(index='x', columns='y', values='stud_found'))
df = pd.DataFrame(df.fillna(0))
#print(df.to_string())
sns.heatmap(df)
plt.show()