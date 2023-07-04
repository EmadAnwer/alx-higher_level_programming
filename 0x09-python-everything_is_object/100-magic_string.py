#!/usr/bin/python3
def magic_string():
    magic_string.count = magic_string.count + 1 if hasattr(magic_string, 'count') else 1
    return magic_string.count * "BestSchool"
