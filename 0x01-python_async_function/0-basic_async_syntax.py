#!/usr/bin/env python3
"""
0-basic_async_syntax.py

this module provides a siple basic syntax of async and how it is used

"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    This function takes in two arguments and delays them for a perriod of time
    specified.

    parameters:
    max_delay - its of type int, and has a default value of 10 if not
    specified.

    Usage:
    it uses random.uniform with the first number being 0 and the
    other being max_delay to generate a random number that is
    passed to the variable delay.
    the delay is used by asyncio.sleep and latter on returned
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
