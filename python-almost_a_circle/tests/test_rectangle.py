import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)
