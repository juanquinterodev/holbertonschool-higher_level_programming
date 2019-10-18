#!/usr/bin/python3
"""Inherit from list and print it
    Args:
        list (int): integer list
"""


class MyList(list):
    """Class that inherit
    """

    def print_sorted(self):
        """print the list sorted
        """
        print(sorted(self))
