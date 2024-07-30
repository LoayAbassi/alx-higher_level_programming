#!/usr/bin/python3
"""
3-say_my_name.py
this file contains a function that print full name
"""


def say_my_name(first_name, last_name=""):
    """prints out my full name
    Args:
        first_name (str): the first name
        last_name (str): the last name (default is an empty string)
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
