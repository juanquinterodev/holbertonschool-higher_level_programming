#!/usr/bin/python3
"""Return an object
"""


import json


def from_json_string(my_str):
    """Returns Python data structure represented by a JSON string
    """

    return json.loads(my_str)
