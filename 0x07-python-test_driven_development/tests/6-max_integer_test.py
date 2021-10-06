#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test cases for max_integer function
    """
    def test_area(self):
        self.assertEqual(max_integer([2, 3, 4, 5, 6, 9, 10]), 10)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-100, 29, -90, 30]), 30)

    def test_type(self):
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, 3j)
        self.assertRaises(TypeError, max_integer, "35")
        self.assertRaises(TypeError, max_integer, "type")
        self.assertRaises(TypeError, max_integer, 2)
        self.assertRaises(TypeError, max_integer, 2.8)
        self.assertRaises(TypeError, max_integer, {})
        self.assertRaises(TypeError, max_integer, set())
        self.assertRaises(TypeError, max_integer, [2, '2'])
