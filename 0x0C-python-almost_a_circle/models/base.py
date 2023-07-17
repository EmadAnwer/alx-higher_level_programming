#!/usr/bin/python3
"""base class module"""

from json import dump
from json import dumps
from json import loads


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init
        args:
            id : int
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """dictionaries to json"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file"""

        with open(cls.__name__+".json", encoding="utf-8", mode="w") as file:
            mylist = []
            if list_objs:
                for obj in list_objs:
                    mylist.append(
                        loads(cls.to_json_string(obj.to_dictionary())))
            dump(mylist, file)

    @staticmethod
    def from_json_string(json_string):
        """from json string"""
        if json_string is None or json_string == "":
            return []
        return loads(json_string)
