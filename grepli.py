#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""grepli.py: Implementation grep function for python"""
__author__ = "linxuil"

import re
from typing import List, Pattern, Union
from io import TextIOWrapper
from src.convert_to_list import convert_to_list
from src.search_in_list import search_in_list

def grepli(pattern: str, *args: Union[List[str], str, TextIOWrapper]) -> List[str]:
    if not pattern:
        raise ValueError("Pattern must be a non-empty string")
    
    if not args:
        raise ValueError("At least one variable must be provided")
    
    result:List[str] = []

    # Compile the pattern for efficiency
    compiled_pattern:Pattern[str] = re.compile(pattern)
    
    # Iterate through the input arguments
    for arg in args:
        # Convert the current argument to a list using convert_to_list
        arg_list = convert_to_list(arg)
        
        # Search for the pattern in the current argument using search_in_list
        matches = search_in_list(arg_list, compiled_pattern) # type:ignore
        
        # Extend the result list with the matches found
        result.extend(matches)

    return result