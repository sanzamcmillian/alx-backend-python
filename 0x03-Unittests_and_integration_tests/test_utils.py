#!/usr/bin/env python3
"""tester for utils.py"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Sequence
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """class to test the access nested map function"""
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

class TestGetJson(unittest.TestCase):
    """class to test the get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])

    def test_get_json(self, test_url, test_payload):
        """ function, tester for the get_json method"""
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()
