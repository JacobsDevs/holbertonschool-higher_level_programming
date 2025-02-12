#!/usr/bin/python3
"""
Module containing the add_item function.
"""
import json
from sys import argv
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file



def add_item():
    """Reads from sys ARGV and adds each of the arguments to the list saved in
    add_item.json.

    Args:
    @filename: The file to read and write from.

    Return:
    None
    """
    try:
        with open('add_item.json', 'x', encoding="utf-8") as f:
            pass
    except FileExistsError:
        pass

    my_list = load('add_item.json')
    for i in argv[1:]:
        my_list.append(i)
    save(my_list, 'add_item.json')

add_item()
