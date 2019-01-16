def print_lol(the_list):
    for value in the_list:
        if (isinstance(value, list)):
            print_lol(value)
        else:
            print(value)




























