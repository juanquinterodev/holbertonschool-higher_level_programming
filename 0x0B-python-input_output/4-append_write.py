#!/usr/bin/python3
"""Append a string at the end of a text file
"""


def append_write(filename="", text=""):
    """Appends a string and returns the
        number of characters added
    """

    with open(filename, 'a', encoding='utf-8') as new:
        new.write(text)
    return len(text)
