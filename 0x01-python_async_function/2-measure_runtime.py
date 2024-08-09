#!/usr/bin/env python3
"""
this module helps in calculating the time taken
by wait_n to run
"""
import asyncio
from time import perf_counter


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    this function takes in wait_n and runs it
    as it records the time it started and the time
    it completes hence the difference of the
    two is returned as the runtime
    """
    t_start = perf_counter()

    await wait_n(n, max_delay)
    t_stop = perf_counter()

    return t_stop - t_start
