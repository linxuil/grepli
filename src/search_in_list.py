from typing import List
import re
# Search for the pattern in the current item using re.search
# Return matched list items
def search_in_list(input_list:List[str], pattern:str) -> List[str]:
    input_type_is_list = isinstance(input_list, list) #type:ignore[Unne-ry call]
    if not input_type_is_list:
        raise TypeError("Input must be of type list")
    
    result:List[str] = []

    for item in input_list:
        match = re.search(pattern, item)
        if match:
            result.append(item)

    return result