#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i > 7 and i < j:
            print("{}{}".format(i, j))
        elif i < j:
            print("{}{}, ".format(i, j), end="")
