#!/usr/bin/python3
"""This is the 5-text_indentation module which contains the
text_indentation function:
Args:
    text: the line to format.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after every ? . or :
    """
    try:
        new_text = text.translate(
            str.maketrans(
                {".": ".!!!", ":": ":!!!", "?": "?!!!"})).split("!!!")
        for c, i in enumerate(new_text):
            print("{}".format(i.strip()), end="")
            if c < len(new_text) - 1:
                print()
                print()
    except AttributeError:
        raise TypeError('text must be a string')
