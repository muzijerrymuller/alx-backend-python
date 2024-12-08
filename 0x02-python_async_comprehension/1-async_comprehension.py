#!/usr/bin/env python3
"""
Module demonstrating the use of async
comprehension to fetch random numbers.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using asynchronous iteration.
    Overview:
    This function asynchronously processes data produced by async_generator,
    gathering 10 floating-point numbers into a list.
    Parameters:
    None
    Returns:
    List[float]: A list containing 10 random numbers generated asynchronously.
    """
    result = [value async for value in async_generator()]
    return result
