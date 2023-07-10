#!/usr/bin/python3
"""available attributes"""


class MyList(list):
    """A custom list class that inherits from the built-in list class."""
    def print_sorted(self):
        """
        Print the list elements in sorted order.

        Prints the list in ascending order using the sorted() function.

        Args:
            None

        Returns:
            None
        """
        list_new = sorted(self)
        if list_new:
            print(sorted(list(self)))
