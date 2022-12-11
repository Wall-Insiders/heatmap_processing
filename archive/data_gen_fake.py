# Creates a dataset for testing the heatmapping function of seaborn
# Outputs to a .csv file to be accessed 
import csv
import random
import numpy as np
import pandas as pd

# Wall dimensions
length = 72
width = 120

# Initialize an empty Numpy array
data = np.empty([width,length], dtype=int)

# Set all data points not equal to 0 to 0
data[data != 0] = 0

# Generate random number from x(0,71) and y(0,119) (A regular 6 foot by 10 foot wall)
x_values = list(range(length))
y_values = list(range(width))

# Random number generate 4 (x,y) coordinates with a z standard stud length
for x in range(4):
    temp_x = random.choice(x_values)
    temp_y = random.choice(y_values)

    data[:, temp_x] = 1


# Expand the 4 coordinates by (x+1,y) of 4 iterations (2x4 stud dimension)
    for y in range(4):
        if(temp_x + y <= length):
            data[:, temp_x+y] = 1

# Save coordinates to .csv file
with open('studs_found2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(x_values)

    # write multiple rows
    writer.writerows(data)