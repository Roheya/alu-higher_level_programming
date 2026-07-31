#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init_two_args(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_init_three_args(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_init_four_args(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_extra_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 99)
        self.assertEqual(str(r), "[Rectangle] (99) 2/1 - 4/6")
