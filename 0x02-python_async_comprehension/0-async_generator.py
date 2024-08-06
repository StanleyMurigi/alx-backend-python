#!/usr/bin/env python3
import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that generates 10 random numbers between 0 and 10 asynchronously,
    waiting 1 second between each number.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

