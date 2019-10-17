#!/usr/bin/python3
"""Read a text file and print it to stdout
"""


def read_file(filename=""):
    """Reads and print a text file (UTF8)
    """

    with open(filename, 'r', encoding='utf-8') as new:
        print(new.read(), end='')
