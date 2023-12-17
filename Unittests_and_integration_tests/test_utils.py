#!/usr/bin/env python3
"""Parameterize a unit test
"""
from parameterized import parameterized
import unittest
import utils
from utils import get_json, memoize
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class that
    inherits from unittest.TestCase"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """method to test that the method
        returns what it is supposed to"""
        self.assertEqual(utils.access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """assertRaises context manager to test that a
        KeyError is raised for the following inputs"""
        with self.assertRaises(KeyError):
            self.assertEqual(utils.access_nested_map(nested_map, path))


class TestGetJson(unittest.TestCase):
    """class and implement the TestGetJson.test_get_json
    method to test that utils.get_json
    returns the expected result"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_payload, test_url):
        """method to test that utils.get_json
        returns the expected"""
        mockresponse = Mock()
        mockresponse.json = Mock(return_value=test_payload)
        with patch('requests.get', return_value=mockresponse):
            json_data = get_json(test_url)
            self.assertEqual(json_data, test_payload)


class TestMemoize(unittest.TestCase):
    """TestMemoize(unittest.TestCase) class
    with a test_memoize method"""
    def test_memoize(self):
        """test_memoize module"""
        class TestClass:
            """TestClass class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                """a_property method"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            testclass = TestClass()
            testclass.a_property()
            testclass.a_property()
            mock_method.assert_called_once()
