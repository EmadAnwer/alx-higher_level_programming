#!/usr/bin/python3
"""is sub class (inherits) """


def inherits_from(obj, a_class):
    """returns True if the object is an instance of, or if the object is an
      instance of a class; otherwise False."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
