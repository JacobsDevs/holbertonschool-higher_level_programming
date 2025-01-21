#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for k in dict(sorted(a_dictionary.items())):
        print("{}: {}".format(k,a_dictionary[k]))
