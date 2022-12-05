# Creates a dataset for testing the heatmapping function of seaborn
# Outputs to a .csv file to be accessed 
import csv
import random
import numpy as np

headers = ['x', 'y', 'stud_found']
data = np.empty([8640,3], dtype=int)
#print(data)

# Generate random number from x(0,71) and y(0,119) (A regular 6 foot by 12 foot wall)
x_values = list(range(0,71))
y_values = list(range(0,119))

# Random number generate 4 (x,y) coordinates with a z standard stud length
for x in range(0, 16, 4):
    temp_x = random.choice(x_values)
    temp_y = random.choice(y_values)

    temp_data = [temp_x, temp_y, 1]
    data[x] = temp_data

# Expand the 4 coordinates by (x+1,y) of 4 iterations (2x4 stud dimension)
    for y in range(3):
        temp_x += 1
        data[x+y+1] = [temp_x, temp_y, 1]

#for data in range(16,8640,1):
    #for x in range(0,71):


#print(data)
# Save coordinates to .csv file
with open('studs_found1.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(headers)

    # write multiple rows
    writer.writerows(data)