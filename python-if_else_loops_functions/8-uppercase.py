#!/usr/bin/python3

def uppercase(string):
    for i in range(len(string)):
        c = string[i]
        if ord(c) > 96 and ord(c) < 123:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
