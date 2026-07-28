#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_auto_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_explicit_id(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string_list(self):
        data = '[{ "id": 89 }]'
        result = Base.from_json_string(data)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]['id'], 89)

if __name__ == "__main__":
    unittest.main()
