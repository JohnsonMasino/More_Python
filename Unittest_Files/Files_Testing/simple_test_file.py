#!/usr/bin/python3

"""
This Program Tests For a Simple Function
"""
import unittest

class TestStringMethods(unittest.TestCase):

    def test_isupper(self):
        self.assertTrue("MASINO OBINNA".isupper())

    def test_islower(self):
        self.assertTrue("masino is here".islower())

    def test_islower(self):
        self.assertFalse("John Kenneddy".isupper())

    def test_division(self):
        result = 45 / 5
        self.assertEqual(result, 9)

    def test_split(self):
        name = "johnson Masino"
        done = name.split(" ")
        self.assertTrue(done == ["johnson", "Masino"])

if __name__ == "__main__":
    unittest.main()-v
