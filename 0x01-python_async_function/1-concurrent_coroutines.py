#!/usr/bin/env python3
"""
This module imports the module 0-basic_async_syntax and uses
its wait_random function to calculate and make the delay wait n times

"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This async fxn takes in the max_delay and divides it n times
    and passes the results to delays variable

    parameters:
    n of type int
    max_delay of type int
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    for i in range(1, len(delays)):
        key = delays[i]
        j = i - 1
        while j >= 0 and key < delays[j]:
            delays[j + 1] = delays[j]
            j -= 1
        delays[j + 1] = key

    return delays
