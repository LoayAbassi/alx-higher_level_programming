#!/usr/bin/python3
"""    
contains a function that prints
a square using the # symbol
"""


def print_square(size):
    """prints a square of size size using # symbol"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    res = ""
    for i in range(size):
        res += "#"*size+"\n"
    res = res[:len(res)-1]
    if len(res) > 0:

        print(res)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
