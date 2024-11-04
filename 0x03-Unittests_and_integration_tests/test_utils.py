#!/usr/bin/env python3
"""A module for testing the utils module.
This module serves as a robust framework for
testing essential utility functions
from the `utils` module. Through the use of
comprehensive unit tests, we validate
the expected behavior of these functions, ensuring
they perform reliably in various
scenarios. This not only enhances the quality of
our code but also builds confidence
in the functionality provided by these utilities.
The key functions under test include:
- `access_nested_map`: Designed to retrieve values from nested dictionaries
  based on specified paths, ensuring safe access to complex data structures.
- `get_json`: Responsible for fetching and returning
JSON data from external URLs,
  guaranteeing that our application can
  communicate effectively with web services.
- `memoize`: A performance optimization tool
that caches results of function calls,
  significantly improving efficiency when the
  same inputs are encountered multiple times.
By maintaining thorough test coverage, we aim
to identify potential issues early,
facilitate code maintenance, and support the ongoing
development of a high-quality software product.
"""
import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize,
)



class TestAccessNestedMap(unittest.TestCase):
    """Tests the functionality of the `access_nested_map` function.
    This class encompasses a series of unit tests that validate the behavior
    of the `access_nested_map` function. It ensures that the function accurately
    retrieves values from nested dictionaries for valid paths and appropriately
    raises exceptions for invalid access attempts.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, nested_map: Dict, path: Tuple[str], expected: Union[Dict, int]
    ) -> None:
        """Tests the output of `access_nested_map` for valid paths.
        This test case evaluates whether the function returns the expected 
        values when provided with correctly structured input.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict, path: Tuple[str], exception: Exception) -> None:
        """Tests the exception handling of `access_nested_map
        This test case ensures that the function raises the appropriate
        exceptions when attempting to access invalid paths, reinforcing
        the robustness of the utility function.
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """Tests the functionality of the `get_json` function.
    This class is dedicated to testing the `get_json` function to confirm
    that it accurately fetches JSON data from specified URLs and handles
    network responses correctly.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """Tests the output of `get_json` when fetching data from a URL.
        This test verifies that the function
        returns the expected JSON payload
        and confirms that the correct URL is called during the process.
        """
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)

class TestMemoize(unittest.TestCase):
    """Tests the functionality of the `memoize` function.
    This class verifies the behavior of the `memoize` decorator to ensure
    that it effectively caches the results of function calls, improving
    efficiency for repetitive calls with identical arguments.
    """

    def test_memoize(self) -> None:
        """Tests the output of the `memoize` function for caching results.
        This test evaluates whether the `memoize` decorator correctly caches
        function outputs and limits the number of calls to the underlying
        method, enhancing performance.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
            
            with patch.object(TestClass, "a_method", return_value=42) as mock_method:
                test_instance = TestClass()
                self.assertEqual(test_instance.a_property(), 42)
                self.assertEqual(test_instance.a_property(), 42)
                mock_method.assert_called_once()
