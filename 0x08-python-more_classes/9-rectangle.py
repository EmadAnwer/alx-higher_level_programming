#!/usr/bin/python3
"""2-Rectangle module"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init
        Args:
            width: int
            height: int
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """return rectangle with the character #"""
        if self.height == 0 or self.width == 0:
            return ""
        s = ((self.width * f"{self.print_symbol}" + "\n")
             * self.height).rstrip()
        return s

    def __repr__(self):
        """return rectangle arguments"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """print delete message"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal
        Args:
            rect_1: Rectangle instance
            rect_2: Rectangle instance
        Return:
            bigger Rectangle or rect_1 if thay ar equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """square
        Args:
            size: width == height == size
        Return:
            Rectangle new object
        """
        return Rectangle(size, size)
