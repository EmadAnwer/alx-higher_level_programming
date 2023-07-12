#!/usr/bin/python3
"""append after module"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts new_string after each line containing search_string in the file.

    Args:
        filename (str): Name or path of the file.
        search_string (str): String to search in each line.
        new_string (str): Text to insert after each matched line.

    Returns:
        None
    """
    with open(filename, 'r+', encoding="utf-8") as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

        file.truncate()
