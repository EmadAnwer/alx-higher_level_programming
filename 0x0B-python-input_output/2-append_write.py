#!/usr/bin/python3
"""append text module"""


def append_write(filename="", text=""):
    """append_write
    arges:
        filename: string
        text: string to append
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
