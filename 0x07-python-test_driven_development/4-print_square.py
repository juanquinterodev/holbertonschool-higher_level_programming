#!/usr/bin/python3
""" print_square - Print a square with character # """


def print_square(size):
    """
    Gived parameters size of a square
    first conditional raise an error message if the size are not integer
    Second conditional raise an error message if size is less than 0
    print the square with #
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for i in range(size):
            for i in range(size):
                print("{}".format('#'), end='')
            print()
