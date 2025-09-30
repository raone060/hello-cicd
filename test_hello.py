#!/usr/bin/env python3
"""
Unit tests for the hello world application
"""

import unittest
from hello import say_hello


class TestHello(unittest.TestCase):
    """Test cases for the hello module"""
    
    def test_say_hello_default(self):
        """Test say_hello with default parameter"""
        result = say_hello()
        self.assertEqual(result, "Hello, World!")
    
    def test_say_hello_custom_name(self):
        """Test say_hello with custom name"""
        result = say_hello("Alice")
        self.assertEqual(result, "Hello, Alice!")
    
    def test_say_hello_empty_string(self):
        """Test say_hello with empty string"""
        result = say_hello("")
        self.assertEqual(result, "Hello, !")


if __name__ == "__main__":
    unittest.main()
