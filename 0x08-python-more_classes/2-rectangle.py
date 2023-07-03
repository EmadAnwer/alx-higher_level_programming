#!/usr/bin/python3
"""2-Rectangle module"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """init
        Args:
            width: int
            height: int
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter method
           checking width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter method
           checking height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return area of rectangle"""
        return self.height * self.width

    def perimeter(self):
        """return perimeter of rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)
