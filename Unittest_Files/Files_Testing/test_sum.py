#!/usr/bin/python3

import unittest

class Testing(unittest.TestCase):
    """Defines the class of the test module"""
    def test_testing(self):
        """defines the test function"""
        self.assertTrue(sum([2, 4, 6]) == 12)

if __name__ == "__main__":
    unittest.main()
#    print("All tests run")
#print("\nCode developed by Masino")
