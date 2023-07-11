#!/usr/bin/python3
"""save args to file"""

from sys import argv

# load functions
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
FILENAME = "add_item.json"

try:
    json_obj = load_from_json_file(FILENAME)
    json_obj += argv[1:]
    save_to_json_file(json_obj, FILENAME)

except FileNotFoundError:
    save_to_json_file(argv[1:], FILENAME)
