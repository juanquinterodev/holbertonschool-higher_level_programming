#!/usr/bin/python3
"""Add all arguments to a list
"""


import json
from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

name = 'add_item.json'

try:
    new = load_from_json_file(name)
except:
    new = []

for arg in argv[1:]:
    new.append(arg)

save_to_json_file(new, name)
