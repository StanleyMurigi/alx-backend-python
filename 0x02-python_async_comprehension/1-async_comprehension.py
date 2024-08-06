#!/usr/bin/env python3
from typing import List
import asyncio
from 0_async_generator import async_generator

async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator
    using an asynchronous comprehension.
    """
    return [number async for number in async_generator()]

