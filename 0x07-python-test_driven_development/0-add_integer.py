#!/usr/bin/python3
"""add ingeger module"""


def add_integer(a, b=98):
    """Returns an integer: the addition of int(a) and int(b)
    Arges:
        a: int or float
        b: int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    # cast to int then add
    return int(a) + int(b)
