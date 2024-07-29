#!/usr/bin/env python3
"""tester for utils.py"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Sequence


class TestAccessNestedMap(unittest.TestCase):
    """class to test the access nested map method function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path: Sequence, expected):
        """tester for the access nested map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
    
    @parameterized.expand([
        ({}, ("a")),
        ({"a: 1"}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """exception function for tester"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
