#!/usr/bin/env python3
"""
This module contains unit tests for the `access_nested_map` function from
the `utils` module. The tests verify that the function correctly retrieves
values from a nested dictionary using a specified path of keys.
"""
import unittest
import requests
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit test case for testing the `access_nested_map` function.
    This test case class uses the `parameterized.expand` decorator to
    run multiple test cases on the `access_nested_map` function,
    verifying that it returns the expected values for given nested maps and paths.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test `access_nested_map` with various nested maps and paths.
        Args:
            nested_map (dict): The nested dictionary to retrieve values from.
            path (tuple): The sequence of keys to follow in the dictionary.
            expected: The expected value at the end of the path.
        Asserts:
            The value retrieved by `access_nested_map` matches `expected`.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
