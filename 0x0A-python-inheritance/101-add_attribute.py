#!/usr/bin/python3
""" MyInt module"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to add the attribute to.
        attr: The name of the attribute to add.
        value: The value to assign to the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.

    Returns:
        None
    """
    if hasattr(obj, '__dict__'):
        obj.__setattr__(attr, value)
    else:
        raise TypeError("can't add new attribute")
