#!/usr/bin/python3
"""
This is the module including the read_file function
"""


from os import read


def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")

read_file('my_file_0.txt')
