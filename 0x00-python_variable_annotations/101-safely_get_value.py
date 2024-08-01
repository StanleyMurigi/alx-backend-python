#!/usr/bin/env python3
"""
This module contains a function that safely gets a value from a dictionary using a key, 
with a default value if the key is not present.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """
    Safely get a value from a dictionary using a key, with a default value if the key is not present.

    Args:
        dct (Mapping[Any, T]): A dictionary to search.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None], optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        Union[T, None]: The value associated with the key if found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
