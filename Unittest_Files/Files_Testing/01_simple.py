#!/usr/bin/python3

"""
This program is a simple unittest of python
"""

from __future__ import print_function as pf
import unittest

class TestMe(unittest.TestCase):
    def test_fooo(self):
        self.assertTrue(True)
        self.assertFalse(False)
    def fun_not_run(self):
        print("no run")

    def test_issubclass(self):
        self.assertTrue(int, bool)

class TestUs(unittest.TestCase):
    def test_isupper(self):
        self.assertTrue("MASINO IS HERE".isupper())

if __name__ == "__main__":
    unittest.main()
