#!/usr/bin/python3
""" Unittest for the module Base """

import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os

class testBaseClass(unittest.TestCase):
    """ Class to rpove tests """

    def test_empty(self):
        b1 = Base()
        b2 = BAse()
        self.assertEqual(b1.id, b2.id)

    def test_none(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id)

    def test_instance(self):
        self.asserIs(type(Base()), Base)
        self.assertEqual(Base(3).id, 3)
        self.assertEqual(Base().id, 5)

if __name == '__main__':
    unittest.main()
