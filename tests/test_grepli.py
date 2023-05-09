#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_grepli.py: Test implementation for python grep function"""
__author__ = "linxuil"

import os
import sys
# setting path
test_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, test_path)

import unittest
from io import StringIO
from grepli import grepli

class TestGrepli(unittest.TestCase):
    def setUp(self):
        self.pattern = r"hello"
        self.str_variable = "hello world"
        self.list_variable = ["hello there", "general kenobi"]
        self.file_path = "test_file.txt"

        # Create a test file
        with open(self.file_path, "w") as f:
            f.write("This is a test file.\nhello from file\nAnother line.")

    def tearDown(self):
        # Remove the test file
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_grepli_string(self):
        result = grepli(self.pattern, self.str_variable)
        self.assertEqual(result, ["hello world"])

    def test_grepli_list(self):
        result = grepli(self.pattern, self.list_variable)
        self.assertEqual(result, ["hello there"])

    def test_grepli_file(self):
        result = grepli(self.pattern, self.file_path)
        self.assertEqual(result, ["hello from file"])

    def test_grepli_multiple_arguments(self):
        result = grepli(self.pattern, self.str_variable, self.list_variable, self.file_path)
        self.assertEqual(result, ["hello world", "hello there", "hello from file"])

    def test_grepli_string_io(self):
        string_io = StringIO("This is a string io.\nhello from string io\nAnother line.")
        result = grepli(self.pattern, string_io)
        self.assertEqual(result, ["hello from string io"])

    def test_grepli_empty_pattern(self):
        with self.assertRaises(ValueError):
            grepli("", self.str_variable)

    def test_grepli_no_arguments(self):
        with self.assertRaises(ValueError):
            grepli(self.pattern)

if __name__ == "__main__":
    unittest.main(verbosity=2)
