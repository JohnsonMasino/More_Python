#!/usr/bin/python3

from files import file6 as f6
import unittest

class TestTo_Power(unittest.TestCase):
    """Defines the class of the test file"""
    
    def test_To_Power(self):
        """defines the file test file"""
        ans = f6.To_Power(2, 2)
        self.assertEqual(ans, 4)

if __name__ == "__main__":
    unittest.main()
