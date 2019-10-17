#!/usr/bin/python3
"""Read n lines of a text file and print to stdout
"""


def read_lines(filename="", nb_lines=0):
    """Reads and print n lines of a text file (UTF8)
    """

    number = 0

    with open(filename, 'r', encoding='utf-8') as new:
        for lines in new:
            if number < nb_lines or nb_lines <= 0:
                print(lines, end='')
                number += 1
