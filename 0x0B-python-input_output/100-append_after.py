#!/usr/bin/python3
"""append after module"""

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts text after lines containing a specific string.

    Args:
        filename (str): Name/path of the file.
        search_string (str): Specific string to search.
        new_string (str): Text to insert.

    Returns:
        None

    Notes:
        - Uses 'with' statement for file handling.
        - Overwrites the original file.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
