import sqlite3
import random
import os

# Generates random stud location data and saves it into a database
def gen_data(database_name = "test", wall_width = 0, wall_length = 0, stud_count = 0):
    x_values, y_values = list(range(wall_length)), list(range(wall_width))
    coords = []

    # Generates folder for database
    database_folder_path = gen_folder()

    # Creates database file called "test"
    con = sqlite3.connect(database_folder_path + database_name + ".db")

    # Creates cursor for query commands
    cur = con.cursor()

    # Creates a table called studs with 4 columns
    cur.execute("CREATE TABLE stud_locations(x, y)")

    # Generate 1000 stud locations
    for x in range(stud_count):
        temp_x = random.choice(x_values)
        temp_y = random.choice(y_values)
        coords.append(tuple(list((temp_x, temp_y))))

    con.executemany("INSERT INTO stud_locations VALUES(?, ?)", coords)
    con.commit()
    con.close()

    return 0

# Generates folder for database returns path of database folder
def gen_folder():
    directory_folder = "databases/"

    folder = os.path.join(os.getcwd(), directory_folder)

    if(not(os.path.exists(folder))):
        os.mkdir(folder)
    
    return folder
