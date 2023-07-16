#!/usr/bin/python3
"""Unittest for base class
"""

import unittest

from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClassArguments(unittest.TestCase):
    """
        test Rectangle class Arguments validation
    """

    def test_rectangle_class_inherited_from_base(self):
        """
        check if is Rectangle class inherited from base or not
        """
        rectangle = Rectangle(10, 20)
        self.assertEqual(isinstance(rectangle, Base), True)

    def test_argumnets_count(self):
        """test arguments count"""
        with self.assertRaises(TypeError):
            rect4 = Rectangle()
        with self.assertRaises(TypeError):
            rect4 = Rectangle(10, 22, 1, 1, 1, "emad")

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

    def test_area(self):
        """test area"""
        rect = Rectangle(10, 5)
        self.assertEqual(rect.area(), 50)

        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)


class TestRectangleClassMethods(unittest.TestCase):
    """
        test Rectangle class methods
    """

    def test_display(self):
        """test display method"""

        # Case 1 width < hight
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rectangle = Rectangle(2, 3)
            rectangle.display()
            expected_output = "##\n##\n##\n"
            self.assertEqual(expected_output, fake_out.getvalue())
        # Case 2 width > hight
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rectangle = Rectangle(3, 2)
            rectangle.display()
            expected_output = "###\n###\n"
            self.assertEqual(expected_output, fake_out.getvalue())
        # Case 2 width == hight
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rectangle.width = 3
            rectangle.height = 3
            rectangle.display()
            expected_output = "###\n###\n###\n"
            self.assertEqual(expected_output, fake_out.getvalue())
        # Case 3 worng number of arguments
        with self.assertRaises(TypeError):
            rectangle.display(2)

    def test_str(self):
        """test __str__ magic method"""

        rectangle = Rectangle(5, 15, 0, 0, 12)
        # case 1 without x , y
        self.assertEqual(str(rectangle), "[Rectangle] (12) 0/0 - 5/15")

        # case 2 with x , y
        rectangle.x = 5
        rectangle.y = 7
        self.assertEqual(str(rectangle), "[Rectangle] (12) 5/7 - 5/15")
