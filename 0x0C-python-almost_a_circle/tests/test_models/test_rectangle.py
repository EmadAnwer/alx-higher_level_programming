#!/usr/bin/python3
"""Unittest for base class
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """
        test Rectangle class
    """

    def test_rectangle_class_inherited_from_base(self):
        """
        check if is Rectangle class inherited from base or not
        """
        rectangle = Rectangle(10, 20)
        self.assertEqual(isinstance(rectangle, Base), True)

    def test_width(self):
        """test width validation"""
        rect = Rectangle(10, 5)
        self.assertEqual(rect.width, 10)

        rect.width = 15
        self.assertEqual(rect.width, 15)

        with self.assertRaises(TypeError):
            rect.width = "invalid"

        with self.assertRaises(ValueError):
            rect.width = -5

    def test_height(self):
        """test height validation"""
        rect = Rectangle(10, 5)
        self.assertEqual(rect.height, 5)

        rect.height = 15
        self.assertEqual(rect.height, 15)

        with self.assertRaises(TypeError):
            rect.height = "invalid"

        with self.assertRaises(ValueError):
            rect.height = -5

    def test_x(self):
        """test x validation"""
        rect = Rectangle(10, 5, 1)
        self.assertEqual(rect.x, 1)

        rect.x = 15
        self.assertEqual(rect.x, 15)

        with self.assertRaises(TypeError):
            rect.x = "invalid"

        with self.assertRaises(ValueError):
            rect.x = -5

    def test_y(self):
        """test y validation"""
        rect = Rectangle(10, 5, 1, 20)
        self.assertEqual(rect.y, 20)

        rect.y = 15
        self.assertEqual(rect.y, 15)

        with self.assertRaises(TypeError):
            rect.y = "invalid"

        with self.assertRaises(ValueError):
            rect.y = -5
