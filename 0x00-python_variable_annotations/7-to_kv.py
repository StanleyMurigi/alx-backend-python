#!/usr/bin/env python3
"""
This module contains a function that returns a tuple with a string and the square of an int or float.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple with a string and the square of an int or float.

    Args:
        k (str): The string element.
        v (Union[int, float]): The int or float to be squared.

    Returns:
        Tuple[str, float]: The tuple containing the string and the squared value as a float.
    """
    return (k, float(v ** 2))
