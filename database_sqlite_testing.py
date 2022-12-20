import sqlite3

# Creates database file called "test"
con = sqlite3.connect("test.db")

# Creates cursor for query commands
cur = con.cursor()

cur.execute()

cur.execute("DROP TABLE movie")

# Closes the connection of the database
con.close()