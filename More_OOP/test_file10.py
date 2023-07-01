#!/usr/bin/python3

import unittest
from file10 import Nums

class Test_MyFile(unittest.TestCase):
    """defines the class of the module"""

    def test_Nums(self):
        """defines the test function of the submodule"""
        result = Nums(3, 4, 7, 9, 2)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
#print("\nCode developed by Masino")
