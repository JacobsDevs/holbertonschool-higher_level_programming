#!/usr/bin/python3
"""
Module containing the convert_csv_to_json function.
"""
import csv, json


def convert_csv_to_json(filename):
    """
    Converts a csv file to json format

    Args:
    @filename: CSV file containing the data to convert.
    """

    try:
        with open(filename, newline='') as csvfile:
            with open("data.json", 'w', encoding="utf-8") as jsonfile:
                json_list = []
                reader = csv.DictReader(csvfile)
                for row in reader:
                    json_list.append(row)
                json.dump(json_list, jsonfile, indent=4)
                return True
    except FileNotFoundError:
        return False
