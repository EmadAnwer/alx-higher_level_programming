#!/usr/bin/python3
"""save to json file"""

from json import dump


def save_to_json_file(my_obj, filename):
    """save_to_json_file
    save json object to .json file
    arges:
        filename: string file name
        my_obj: json object representation
    """
    with open(filename, encoding="utf-8", mode="w") as file:
        dump(my_obj, file)
