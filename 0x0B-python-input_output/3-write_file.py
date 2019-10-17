#!/usr/bin/python3
"""Write a string to a text file
"""


def write_file(filename="", text=""):
    """Writes a string and returns the number of
        characters written
    """

    with open(filename, 'w', encoding='utf-8') as new:
        new.write(text)
    return len(text)
