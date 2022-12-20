import sqlite3
import random
# Creates database file called "test"
con = sqlite3.connect("coords.db")

# Creates cursor for query commands
cur = con.cursor()

# Creates a table called studs with 4 columns
cur.execute("CREATE TABLE stud_locations(x, y)")

# Parameters for generation
width = 120
length = 480
stud_count = 100

x_values, y_values = list(range(length)), list(range(width))
coords = []

# Generate 1000 stud locations
for x in range(stud_count):
    temp_x = random.choice(x_values)
    temp_y = random.choice(y_values)
    coords.append(tuple(list((temp_x, temp_y))))

print(coords)

con.executemany("INSERT INTO stud_locations VALUES(?, ?)", coords)
con.commit()
con.close()

# Drops the date and time columns of the database 
#cur.execute("ALTER TABLE studs DROP COLUMN date")
#cur.execute("ALTER TABLE studs DROP COLUMN time")

# Adds new column (session)
#cur.execute("ALTER TABLE studs ADD COLUMN session")
# Closes the connection of the database
