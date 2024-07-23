#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        nb = 0
        for i in range(x):
            try:
                print("{:d}".format(),end = "")
                nb+=1
            except:
                continue
    except:
        pass

    return nb

