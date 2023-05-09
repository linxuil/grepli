# to_list.py
import os
import re
from types import NoneType
from typing import List, Union
from io import TextIOWrapper, StringIO

def convert_to_list(input_data: Union[List[str],
                                      str,
                                      TextIOWrapper,
                                      StringIO]) -> List[str]:
    result_list:List[str] = []
    input_type:type = type(input_data)

    if input_type == list:
        # Do nothing
        result_list = input_data #type:ignore[Convert types]
    elif input_type in (int, float, bool, tuple, set, dict):
        raise TypeError(f"Unsupported input type: {type(input_data)}")
    elif input_type in (TextIOWrapper, StringIO):
        for line in input_data.readlines(): # type: ignore
            right_stripped_line:str = line.rstrip('\n')
            result_list.append(right_stripped_line)
    elif input_type == str:
        invalid_chars = r'[<>:"|?*]'
        contains_invalid_chars:NoneType =\
            re.search(invalid_chars, input_data) #type:ignore[Convert types]
        contains_newlines = "\n" in input_data
        
        # Here we check whether a string is a file path or just a simple string.
        if contains_newlines:
            result_list = input_data.splitlines() #type:ignore[Convert types]
        elif contains_invalid_chars:
            result_list = [input_data] #type:ignore[Convert types]
        else:
            file_exists = os.path.isfile(input_data) #type:ignore[Convert types]
            if file_exists:
                with open(input_data, "r") as file: #type:ignore[TextIOWrapper]
                    result_list:List[str] = []
                    for line in file: #type:ignore[type:str]
                        line:str = line# Hint for Pylance
                        stripped_line:str = line.strip()
                        result_list.append(stripped_line)
            else:
                result_list = [input_data] #type:ignore[Convert types]

    else:
        raise TypeError(f"Unsupported input type: {type(input_data)}. Value: {input_data}")
    
    return result_list
