#!/usr/bin/python3

"""
This Function runs a test for an inbuilt module
"""

from __future__ import print_function
import unittest

class Test(unittest.TestCase):
    def test_run(self):
        print(self.assertEqual(3*4, 6+6))
if __name__ == "__main__":
    unittest.main()
