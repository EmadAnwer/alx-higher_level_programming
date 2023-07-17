#!/usr/bin/python3
"""rectangle class module"""

from models.base import Base


class Rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """inint
        args:
            width: int
            hight: int
            x: int
            y: int
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate rectangle area"""
        return self.height * self.width

    def display(self):
        """calculate rectangle area"""
        rectangle = self.y * "\n" + (self.height * (self.x * " " +
                                                    self.width * "#" + "\n"))
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        """update rectangle"""

        # change every attr to args value
        if args:
            # attr list
            attr_list = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attr_list):
                    setattr(self, attr_list[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                else:
                    raise ValueError(f"{key} is not attribute in this class")

    def to_dictionary(self):
        """retangle to dictionary"""
        retangle_dict = {}
        retangle_dict["id"] = self.id
        retangle_dict["width"] = self.width
        retangle_dict["height"] = self.height
        retangle_dict["x"] = self.x
        retangle_dict["y"] = self.y
        return retangle_dict
    def __str__(self):
        """string method"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} " \
            f"- {self.width}/{self.height}"
