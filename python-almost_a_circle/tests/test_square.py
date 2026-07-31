#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init_one_arg(self):
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_init_two_args(self):
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_init_three_args(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_invalid_size_type(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s = Square(5, 1, 2, 99)
        self.assertEqual(str(s), "[Square] (99) 1/2 - 5")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 5)
        d = s.to_dictionary()
        self.assertEqual(d['size'], 10)
