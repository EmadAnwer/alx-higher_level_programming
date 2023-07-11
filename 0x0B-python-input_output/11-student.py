#!/usr/bin/python3
"""Student module"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """init
        args:
            first_name : string
            last_name : string
            age : int
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """class to json"""
        attr_dict = self.__dict__
        if attrs is None:
            return attr_dict

        new_dict = {}
        for key in attrs:
            value = attr_dict.get(key)
            if value:
                new_dict[key] = value
        return new_dict

    def reload_from_json(self, json):
        """reload_from_json
        reload a class attributes from json
        args:
            json
        """
        for key in json:
            if hasattr(self, key):
                setattr(self, key, json.get(key))
