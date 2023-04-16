#!/usr/bin/python3

import unittest
import div
"""
This program tests the efficiency of the division function
"""

class Testdiv(unittest.TestCase):
    def test_Div(self):
        result = div.Div(44, 4)
        self.assertEqual(result, 11)


if __name__ == "__main__":
    unittest.main()
