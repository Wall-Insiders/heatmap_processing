import Modules.database_gen_sqlite as gen

if __name__ == '__main__':

    # Simulation Parameters
    width = 480
    length = 120
    num_stud = 25

    # Database generation
    gen.gen_data("stud_finder", width, length, num_stud, truncate=True)
