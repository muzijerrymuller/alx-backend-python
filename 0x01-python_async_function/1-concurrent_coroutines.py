#!/usr/bin/env python3
"""
This module defines an async function `wait_n`,
which runs `wait_random`
a specified number of times with a maximum delay.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Runs `wait_random` n times with a given max delay and
    returns the delays in ascending order.
    Args:
        n (int): Number of times to run `wait_random`.
        max_delay (int): Maximum delay value for each call.
    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]i
    return [await task for task in asyncio.as_completed(tasks)]
