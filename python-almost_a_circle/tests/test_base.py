#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_auto_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_custom_id(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        self.assertEqual(
            Base.to_json_string([{'id': 12}]),
            '[{"id": 12}]'
        )

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_list(self):
        data = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(data[0]['id'], 89)
