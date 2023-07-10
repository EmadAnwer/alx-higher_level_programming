#!/usr/bin/python3
""" MyInt module"""


class MyInt(int):
    """ MyInt class"""

    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
