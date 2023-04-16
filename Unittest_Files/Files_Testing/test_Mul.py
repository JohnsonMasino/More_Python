#!/usr/bin/python3

#This is the test code for the Multiolication function.

import unittest
import Mul

class TestMul(unittest.TestCase):
    def test_mul(self):
        result = Mul.mul(10, 2)
        self.assertEqual(result, 20)


if __name__ == "__main__":
    unittest.main()
