#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        r = Rectangle(2, 3, 1, 1, 99)
        self.assertEqual(str(r), "[Rectangle] (99) 1/1 - 2/3")

if __name__ == "__main__":
    unittest.main()
