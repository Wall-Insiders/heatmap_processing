import Modules.database_gen_sqlite as gen

def main():

    # Generates an empty database 
    gen.gen_data()

    # Generates a database called "coords.db"
    gen.gen_data("coords", 120, 120, 35)
    return 0

main()