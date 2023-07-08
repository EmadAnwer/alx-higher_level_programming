#!/usr/bin/python3
"""add ingeger module"""


def add_integer(a, b=98):
    """Returns an integer: the addition of int(a) and int(b)
    Arges:
        a: int or float
        b: int or float
    """
    if a is None or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if b is None or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    max_value = (2 ** 31) - 1
    min_value = -max_value - 1
    if a > max_value or b > max_value or a < min_value or b < min_value:
        raise OverflowError(
            "Float overflow: int too large to convert to float")
    # cast to int then add
    return int(a) + int(b)
