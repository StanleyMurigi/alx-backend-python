#!/usr/bin/env python3
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator
    using an asynchronous comprehension.
    """
    return [number async for number in async_generator()]

