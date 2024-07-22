#!/usr/bin/python3
def uppercase(str):
    up = ""
    for i in range(len(str)):
        if ("a" <= str[i] <= "z"):
            up = up + chr(ord(str[i])-32)
        else:
            up = up + str[i]
    
    print("{} ".format(up))
