import sqlite3
import random
import os
import datetime

# Generates random stud location data and saves it into a database
def gen_data(database_name = "test", wall_width = 0, wall_height = 0, stud_count = 0, truncate = False):
    # Array to keep coordinates
    coords = []

    # Generates folder for database
    database_folder_path = gen_folder() + database_name + ".db"

    # Creates database file called "test"
    con = sqlite3.connect(database_folder_path)

    # Creates cursor for query commands
    cur = con.cursor()

    # Check if table exists 
#    cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='stud_locations'")

    # Table does not exist
 #   if(not(cur.fetchone()[0])):
        # Creates a table called studs with 4 columns
 #       cur.execute("CREATE TABLE stud_locations(x, y)")

    cur.execute("CREATE TABLE IF NOT EXISTS sessions(session_id integer PRIMARY KEY, date text NOT NULL, time text NOT NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS stud_locations(session_id integer, x_coord integer, y_coord integer, FOREIGN KEY (session_id) REFERENCES sessions (session_id))")

    # Truncate the data if needed
    if(truncate):
        cur.execute("DELETE FROM stud_locations")
        cur.execute("DELETE FROM sessions")

    # Generate new ID (Empty vs non-Empty)
    cur.execute("SELECT COUNT(*) FROM sessions")
    
    # Create first session data and time/date
    if(not(cur.fetchone()[0])):
        session_ID = 1

    else:
        cur.execute("SELECT MAX(session_id) FROM sessions")
        session_ID = cur.fetchone()[0] + 1

    date = datetime.date.today()
    time = datetime.datetime.now()
    curr_time = time.strftime("%H:%M:%S")
    curr_date = date.strftime("%m/%d/%y")

    session_data = (session_ID, curr_date, curr_time)

    # Insert into table sessions
    cur.execute("INSERT INTO sessions VALUES (?, ?, ?)", session_data)

    # Generate stud locations
    for x in range(stud_count):
        temp_x, temp_y = random.randint(0, wall_height), random.randint(0, wall_width)
        coords.append(tuple(list((session_ID, temp_x, temp_y))))

    con.executemany("INSERT INTO stud_locations VALUES(?, ?, ?)", coords)
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
