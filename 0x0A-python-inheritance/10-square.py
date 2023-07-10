#!/usr/bin/python3
""" Rectangle module"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, size):
        """init"""
        self.__size = size
        self.integer_validator("size", self.__size)

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.__size ** 2
