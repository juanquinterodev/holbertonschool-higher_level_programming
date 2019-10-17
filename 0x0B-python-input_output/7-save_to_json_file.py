#!/usr/bin/python3
"""Write an Object to a text file
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Object using a JSON representation
    """

    with open(filename, 'w', encoding='utf-8') as new:
        new.write(json.dumps(my_obj))
