#!/usr/bin/python3
"""Return the JSON representation of a string
"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation
    """

    return json.dumps(my_obj)
