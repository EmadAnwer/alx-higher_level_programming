#!/usr/bin/python3
"""square class module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class representation"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} " \
            f"- {self.height}"

    @property
    def size(self):
        """size getter"""

        return self.width

    @size.setter
    def size(self, value):
        """size getter"""
        self.width = value
        self.height = self.width

    def update(self, *args, **kwargs):
        """update square"""

        # change every attr to args value
        if args:
            # attr list
            attr_list = ["id", "size", "x", "y"]
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
        """square to dictionary"""
        retangle_dict = {}
        retangle_dict["id"] = self.id
        retangle_dict["size"] = self.size
        retangle_dict["x"] = self.x
        retangle_dict["y"] = self.y
        return retangle_dict
