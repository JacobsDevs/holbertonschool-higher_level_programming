#!/usr/bin/python3
"""
Module containing the fetch_and_print_posts and fetch_and_save_posts functions.

Uses the requests library to get data from https://jsonplaceholder.typicode.com/
"""
import requests, csv, json
from time import sleep


def fetch_and_print_posts():
    """
    Fetches posts from jsonplaceholder and prints to the terminal.
    """
    posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(posts.status_code))
    if posts.status_code == 200:
        formatted_posts = posts.json()
        for i in formatted_posts:
            print(i['title'])
    else:
        return


def fetch_and_save_posts():
    """
    Fetches posts from jsonplaceholder and saves them to a csv file.
    """
    posts = requests.get('https://jsonplaceholder.typicode.com/posts')
    if posts.status_code == 200:
        formatted_posts = posts.json()
        with open('posts.csv', 'w', encoding="utf-8") as my_csv:
            csv_file = csv.DictWriter(my_csv, formatted_posts[0].keys())
            csv_file.writeheader()
            for i in formatted_posts:
                csv_file.writerow(i)
