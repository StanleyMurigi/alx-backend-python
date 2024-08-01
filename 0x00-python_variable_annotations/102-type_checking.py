#!/usr/bin/env python3
"""
This module contains a function that zooms in on a list of items by a specified factor.
"""

from typing import List, Tuple

def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Zoom into a list of integers by duplicating each element according to the factor.

    Args:
        lst (List[int]): The list of integers to zoom.
        factor (int, optional): The factor by which to zoom. Defaults to 2.

    Returns:
        List[int]: A list with elements duplicated according to the factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
