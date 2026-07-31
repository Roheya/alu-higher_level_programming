#!/usr/bin/python3
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_valid_init(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_str(self):
        s = Square(5, 1, 2, 99)
        self.assertEqual(str(s), "[Square] (99) 1/2 - 5")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 5)
        d = s.to_dictionary()
        self.assertEqual(d['size'], 10)

    def test_update_args(self):
        s = Square(10, 10, 10)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_update_kwargs(self):
        s = Square(10, 10, 10)
        s.update(id=89, size=1, x=2, y=3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
