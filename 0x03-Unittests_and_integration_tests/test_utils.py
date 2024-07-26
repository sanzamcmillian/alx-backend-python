#!/usr/bin/env python3
"""tester for utils.py"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """class to test the access nested map method function"""
    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b")),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """tester for the access nested map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
