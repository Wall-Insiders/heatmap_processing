# Import the required libraries (seaborn and matplotlib)
import seaborn as sns
import matplotlib.pyplot as plt

# Initialize a dataset from the example
df = sns.load_dataset("penguins")

# Plot the dataset
sns.pairplot(df, hue="species")

# Reveal plot
plt.show()

