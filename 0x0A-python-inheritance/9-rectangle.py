#!/usr/bin/python3
"""Rectangle module"""


class BaseGeometry:
    """Rectangle class"""

    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check int"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """init"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Rectangle string"""
        return f"[Rectangle] {self.__width}/{self.__height}"
