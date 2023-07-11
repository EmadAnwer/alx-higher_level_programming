#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """read_file
    args:
        filename: string
    """
    with open(filename, encoding="utf-8") as file:
        read_data = file.read()
        print(read_data, end="")
