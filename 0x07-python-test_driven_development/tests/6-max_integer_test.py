#!/usr/bin/python3
# 6-max_integer_test.py
"""unittests for max_integer([..])"""

import unittest
max_integer = __import__(6-max_integer).max_integer

class TestMaxInteger(unittest.TestCase):
    """define unittest for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """test an ordered list of integer"""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

     def test_max_at_beginning(self):
        """test a list with a beginning max value"""
        max_at_beginning = [4, 1, 2, 3]
        self.assertEqual(max_integer(max_at_beginning), 4)

     def test_empty_list(self):
         """test an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """test one element list"""
        one_element = [1]
        self.assertEqual(max_integer(one_element), 1)

    def test_floats(self):
            """test a list of floats"""
            floats = [1.53, 4.53, -9.533, 16.2, 6.0)]
            self.assertEqual(max_integer(floats), 1.53)

    def test_floats(self):
        """test a list of ints and floats"""
        ints_and_floats = [1.53, 4.53, -9, 15, 4]]
        self.assertEqual(max_integer(ints_and_floats), 1.53)

    def test_string(self):
        """test a string"""
        string = "more"
        self.assertEqual(max_integer(string), 't')
         
    def test_list_of_strings(self):
         """test a list of strings"""
        strings = ["more", "life", "light", "if"] 
        self.assertEqual(max_integer(strings), "more")

         def test_empty_string(self):
            """test an empty string"""
            self.assertEqual(max_integer(""), None)

     if __name__ "" ' __main__':
         unittest.main()
         



