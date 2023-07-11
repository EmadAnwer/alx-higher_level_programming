#!/usr/bin/python3
"""json string module"""

from json import dumps


def to_json_string(my_obj):
    """to_json_string
    this function taks dictionary and convert it to json object
    arges:
        my_obj: python dictionary
    """

    return dumps(my_obj)
