import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_assignment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

