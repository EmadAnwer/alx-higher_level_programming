#!/usr/bin/python3
"""square class"""


class Square:
    """square"""
    def __init__(self, size=0, position=(0, 0)):
        """init
        Args:
            size: size of the square
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
            """postion getter"""
            return self.__position

        @position.setter
        def position(self, value):
            if not (isinstance(value, tuple) and len(value) == 2 and
                    all(isinstance(num, int) and
                        num >= 0 for num in value)):
                raise TypeError("position must be a tuple of "
                                "2 positive integers")
            sefl.__position = value

    def area(self):
        """area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """print a square of #"""
        [print() for i in range(0, self.position[1])]
        for i in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)
        if self.size == 0:
            print()
