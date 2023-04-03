#!/usr/bin/python3

#This is adding function test file.
#It tests if the adding function is correct.

import unittest
import adding

class TestAdding(unittest.TestCase):
    def test_add(self):
        result = adding.add(4, 7)
        self.assertEqual(result, 11)
if __name__ == "__main__":
    unittest.main()
