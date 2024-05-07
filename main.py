from tests import stress

if __name__ == "__main__":

    actions = 100000
    table_size = 500
    stress.run(table_size,actions)
    

