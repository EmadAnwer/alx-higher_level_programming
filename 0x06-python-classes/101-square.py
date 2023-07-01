#!/usr/bin/python3
"""square class"""


class Square:
    """square"""

    def __init__(self, size=0, position=(0, 0)):
        """init
        Args:
            size: size of the square
            position: position of the square x, y
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        if isinstance(value, tuple) and len(value) == 2:
            if all(isinstance(num, int) and num >= 0 for num in value):
                self.__position = value
                return
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """area of a square"""
        return self.size ** 2

    def my_print(self):
        """print an empty line"""
        if self.size == 0:
            print()
            return
        """print a square of # in position"""
        print(("\n" * self.position[1]) +
              ((" " * self.position[0]) +
               ("#" * self.size + "\n")) * self.size, end="")

    def __str__(self):
        """ string of a square of # in position"""
        if self.size == 0:
            return ""
        else:
            return ((("\n" * self.position[1]) +
                    ((" " * self.position[0]) +
                     ("#" * self.size + "\n")) * (self.size-1)) +
                    ((" " * self.position[0]) + ("#" * self.size)))
