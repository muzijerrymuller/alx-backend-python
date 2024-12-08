#!/usr/bin/env python3
"""
A Python module implementing an asynchronous
generator that loops 10 times.
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator function that iterates 10 times.
    Description:
    This function pauses for 1 second on each iteration and yields
    a random float between 0 and 10.
    Arguments:
    None
    Returns:
    A generator yielding random float values.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
