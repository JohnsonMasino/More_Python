#!/usr/bin/python3

#This is the test code for the Subtract function.

import unittest
import Subtract

class TestSub(unittest.TestCase):
    def test_sub(self):
        result = Subtract.sub(10, 4)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
