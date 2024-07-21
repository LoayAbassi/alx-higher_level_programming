#!/usr/bin/python3
def uppercase(str):
    x = ""
    for i in range(len(str)):
        if (i == len(str)-1):
            x = "\n"
        if ("a" <= str[i] <= "z"):
            print("{}".format(chr(ord(str[i])-32)), end=x)
        else:
            print("{}".format(str[i]), end="")
