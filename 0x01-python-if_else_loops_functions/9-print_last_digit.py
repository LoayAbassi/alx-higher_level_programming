#!/usr/bin/python3
def print_last_digit(number):
    print(f"{int(str(number)[-1])}", end="")
    return int(str(number)[-1])
print_last_digit("Holberton")