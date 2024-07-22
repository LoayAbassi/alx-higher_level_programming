#!/usr/bin/python3
def uppercase(str):
    up = ""
    if (len(str) > 0):
        for i in range(len(str)):
            if ("a" <= str[i] <= "z"):
                up = up + chr(ord(str[i])-32)
            else:
                up = up + str[i]
            if (i == len(str)-1):
                up = up + "\n"
    else:
        up = "\n"
    print("{}".format(up))
