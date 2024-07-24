#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            nb += 1
        except IndexError:
            break
    print()
    return nb


my_list = [1, 2, 3, 4]
x = len(my_list) + 1

nb_print = safe_print_list(my_list, x)
print("{:d}".format(nb_print))
