#!/usr/bin/python3
""" Rectangle module"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, size):
        """init"""
        self.__size = size
        self.integer_validator("size", self.__size)
        Rectangle.__init__(self, self.__size, self.__size)

    def area(self):
        """Calculates and returns the area of the Square"""
        return self.__size ** 2

    def __str__(self):
        """Rectangle string"""
        return f"[Square] {self.__size}/{self.__size}"
