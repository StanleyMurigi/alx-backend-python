#!/usr/bin/env python3
"""
This module contains a function that returns another function to multiply a float by a given multiplier.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and returns a float.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
