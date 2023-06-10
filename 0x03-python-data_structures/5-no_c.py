#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return ""
    new_string = ""
    for c in my_string:
        if (c is not 'c') and (c is not 'C'):
            new_string += c
    return new_string
