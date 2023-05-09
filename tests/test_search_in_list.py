#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_search_in_list.py: Test implementation for search_in_list function"""
__author__ = "linxuil"

import os
import sys
# setting path
test_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, test_path + "/src/")

from typing import List
import unittest
from search_in_list import search_in_list

# Correct input data
correct_input_list = ["Hello, how are you?", "This is a test text.", "Text like short life 123."]

class TestSearchInList(unittest.TestCase):

    def test_correct_input_data(self):
        pattern = r'\b\w{4}\b'
        result:List[str] = search_in_list(correct_input_list, pattern)
        expected_res = ["This is a test text.", "Text like short life 123."]
        self.assertEqual(result, expected_res)

    def test_pattern_matching_word_test(self):
        pattern = r'test'
        result:List[str] = search_in_list(correct_input_list, pattern)
        expected_res = ["This is a test text."]
        self.assertEqual(result, expected_res)

    def test_pattern_matching_numbers(self):
        pattern = r'\d'
        result:List[str] = search_in_list(correct_input_list, pattern)
        expected_res = ["Text like short life 123."]
        self.assertEqual(result, expected_res)

    def test_incorrect_input_data(self):
        non_list_input:str = "This is not a list."
        pattern = r'\d'
        with self.assertRaises(TypeError):
            search_in_list(non_list_input, pattern) #type:ignore[Type mistake]

if __name__ == "__main__":
    unittest.main(verbosity=2)
