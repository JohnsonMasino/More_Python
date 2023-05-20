#!/usr/bin/python3
from __future__ import print_function
import unittest

class Testing(unittest.TestCase):
    """class of the test"""
    def test_Foo(self):
        """defines the true test funtion"""
        self.assertTrue(True)

    def test_SysErr(self):
        """runs a system error"""
        with self.assertRaises(SystemError):
            raise SystemError

    def test_More(self):
        """runs a test for an expression"""
        assert "Hello" == "Hello"

unittest.main()
