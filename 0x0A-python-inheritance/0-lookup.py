#!/usr/bin/python3
"""
function to return available methods and attr
"""


def lookup(obj):
    """
    dir to get the methods and attributes available


    Args:
        obj (obj): to pass to dir

    returns:
        list: list of methods and attributes of an object
    """

    return dir(obj)
