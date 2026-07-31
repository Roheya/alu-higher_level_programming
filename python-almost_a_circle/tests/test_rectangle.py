#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_valid_init(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 99)
        self.assertEqual(str(r), "[Rectangle] (99) 2/1 - 4/6")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        d = r.to_dictionary()
        self.assertEqual(d['width'], 10)
        self.assertEqual(d['height'], 2)

    def test_update_args(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_kwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(id=89, width=1, height=2, x=3, y=4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
