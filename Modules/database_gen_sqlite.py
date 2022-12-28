import sqlite3
import random
import os

# Generates random stud location data and saves it into a database
def gen_data(database_name = "test", wall_width = 0, wall_length = 0, stud_count = 0, truncate = False):
    # Array to keep coordinates
    coords = []

    # Generates folder for database
    database_folder_path = gen_folder() + database_name + ".db"

    # Creates database file called "test"
    con = sqlite3.connect(database_folder_path)

    # Creates cursor for query commands
    cur = con.cursor()

    # Check if table exists 
    cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='stud_locations'")

    # Table does not exist
    if(not(cur.fetchone()[0])):
        # Creates a table called studs with 4 columns
        cur.execute("CREATE TABLE stud_locations(x, y)")

    # Truncate the data if needed
    if(truncate):
        cur.execute("DELETE FROM stud_locations")

    # Generate stud locations
    for x in range(stud_count):
        temp_x, temp_y = random.randint(0, wall_length), random.randint(0, wall_width)
        coords.append(tuple(list((temp_x, temp_y))))

    con.executemany("INSERT INTO stud_locations VALUES(?, ?)", coords)
    con.commit()
    con.close()

    return database_folder_path

# Generates folder for database returns path of database folder
def gen_folder():
    directory_folder = "databases/"

    folder = os.path.join(os.getcwd(), directory_folder)

    if(not(os.path.exists(folder))):
        os.mkdir(folder)
    
    return folder
