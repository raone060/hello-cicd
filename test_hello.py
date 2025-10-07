#!/usr/bin/env python3
"""
Unit tests for the Flask hello world application
"""

import unittest
from hello import app, say_hello


class TestHello(unittest.TestCase):
    """Test cases for the hello module"""

    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True

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

    def test_home_endpoint(self):
        """Test home endpoint"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('message', data)
        self.assertIn('status', data)

    def test_hello_endpoint(self):
        """Test hello endpoint"""
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('message', data)

    def test_hello_name_endpoint(self):
        """Test hello with name endpoint"""
        response = self.app.get('/hello/DevOps')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('DevOps', data['message'])

    def test_health_endpoint(self):
        """Test health endpoint"""
        response = self.app.get('/health')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'healthy')

    def test_api_info_endpoint(self):
        """Test API info endpoint"""
        response = self.app.get('/api/info')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('name', data)
        self.assertIn('endpoints', data)


if __name__ == "__main__":
    unittest.main()