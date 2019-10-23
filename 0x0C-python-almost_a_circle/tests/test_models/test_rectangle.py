#!/usr/bin/python3
"""Unittest for Rectangle module
"""


import unittest
import json
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Class for unittests
    """
    def test_id(self):
        """Test id
        """
        Base._Base__nb_objects = 0
        r1 = Rectangle(6, 9)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(9, 16)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(3, 6, 9, 16, 33)
        self.assertEqual(r3.id, 33)

    def test_attrs(self):
        """Test attributes
        """
        r = Rectangle(3, 6, 9, 16, 33)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 16)
        self.assertEqual(r.id, 33)

    def test_width(self):
        """Test width
        """
        r = Rectangle(6, 9)
        self.assertEqual(r.width, 6)

    def test_height(self):
        """Test height
        """
        r = Rectangle(6, 9)
        self.assertEqual(r.height, 9)

    def test_x(self):
        """Test x
        """
        r = Rectangle(9, 16, 8, 7)
        self.assertEqual(r.x, 8)

    def test_y(self):
        """Test y
        """
        r = Rectangle(9, 16, 8, 7)
        self.assertEqual(r.y, 7)
