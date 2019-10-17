#!/usr/bin/python3
"""Return the number of lines
"""


def number_of_lines(filename=""):
    """Number of lines of a text file
    """

    number = 0

    with open(filename, 'r') as new:
        for lines in new:
            number += 1
    return number
