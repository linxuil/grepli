#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_convert_to_list.py: Test implementation for convert_to_list function"""
__author__ = "linxuil"

import os
import sys
# setting path
test_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, test_path + "/src/")

from typing import List, Literal, Tuple
import tempfile
import unittest
from convert_to_list import convert_to_list

class TestConvertToList(unittest.TestCase):

    def test_input_list_mult_words(self):
        input_list_mult_words = ["apple pie", "chocolate cake", "ice cream"]
        expected_list_mult_words = input_list_mult_words
        result:List[str] = convert_to_list(input_list_mult_words)
        self.assertEqual(result, expected_list_mult_words)

    def test_input_str(self):
        input_str = "Hello, world!\nThis is a test."
        expected_input_str = ["Hello, world!", "This is a test."]
        result:List[str] = convert_to_list(input_str)
        self.assertEqual(result, expected_input_str)

    def test_input_single_line_str(self):
        input_single_line_str = "Single line string"
        expected_input_single_line_str = ["Single line string"]
        result:List[str] = convert_to_list(input_single_line_str)
        self.assertEqual(result, expected_input_single_line_str)

    def test_opened_file(self):
        temp_file_name = tempfile.mktemp()
        with open(temp_file_name, "w") as temp_file:
          temp_file.write("Line 1\n")
          temp_file.write("Line 2\n")
          temp_file.write("Line 3\n")
        file = open(temp_file.name, "r")
        expected_file = ["Line 1", "Line 2", "Line 3"]
        result:List[str] = convert_to_list(file)
        file.close()
        self.assertEqual(result, expected_file)

    def test_text_file_path(self):
        text_file_path = "tests/pre_created_file.txt"
        expected_file_path= ["Hello, how are you?", "This is a test text.", "Text like short life 123."]
        result:List[str] = convert_to_list(text_file_path)
        self.assertEqual(result, expected_file_path)

    def test_not_exist_file_path(self):
        not_exist_file_path = "not_exist_file.txt"
        expected_not_exist_file_path= ["not_exist_file.txt"]
        result:List[str] = convert_to_list(not_exist_file_path)
        self.assertEqual(result, expected_not_exist_file_path)

    def test_input_int(self):
        input_int:int = 42
        with self.assertRaises(TypeError):
            convert_to_list(input_int) #type:ignore[Type mistake]

    def test_input_tuple(self):
        input_tuple:Tuple[Literal[1], Literal[2]] = (1, 2)
        with self.assertRaises(TypeError):
            convert_to_list(input_tuple) #type:ignore[Type mistake]

    def test_input_set(self):
        input_set:set[int] = {4, 5, 6}
        with self.assertRaises(TypeError):
            convert_to_list(input_set) #type:ignore[Type mistake]

    def test_input_dict(self):
        input_dict:dict[str, int] = {"one": 1, "two": 2}
        with self.assertRaises(TypeError):
            convert_to_list(input_dict) #type:ignore[Type mistake]

if __name__ == '__main__':
    unittest.main(verbosity=2)
