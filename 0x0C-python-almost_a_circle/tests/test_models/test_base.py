#!/usr/bin/python3
"""Unittest for base class
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """
        test Base class
    """

    def test_id_increasing(self):
        """
        test Base calss without arguments
        """
        base_2 = Base()
        self.assertEqual(base_2.id, 1)
        base_1 = Base(25)
        self.assertEqual(base_1.id, 25)
        base_3 = Base()
        self.assertEqual(base_3.id, 2)

    
        
