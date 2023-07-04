#!/usr/bin/python3
def magic_string():
    magic_string.count = getattr(magic_string, 'num', 0) + 1
    return magic_string.count * "BestSchool"
