#!/usr/bin/python3
for i in range(100):
    if(i%10 > i//10 ):
        print(f"{i:02}", end = " ")
    if(i==99):
        print()
    