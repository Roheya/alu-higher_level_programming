import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_str(self):
        s = Square(5, 1, 2, 99)
        self.assertEqual(str(s), "[Square] (99) 1/2 - 5")
