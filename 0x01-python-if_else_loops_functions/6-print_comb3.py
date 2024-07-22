#!/usr/bin/python3
for i in range(100):
    if (i == 1):
        print("{:02}".format(i), end="")
    if (i % 10 > i//10 and i != 1):
        print(", {:02}".format(i), end="")
    if (i == 99):
        print()
