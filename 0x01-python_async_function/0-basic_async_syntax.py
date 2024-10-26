#!/usr/bin/env python3
"""
This module provides a utility coroutine for introducing
a randomized delay in an asynchronous program.
It contains the following function:
- wait_random: Asynchronously waits for a random delay between
0 and a specified maximum delay (default is 10 seconds).
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and
    max_delay seconds and returns the delay.
    Parameters:
    -----------
    max_delay : int, optional
        The maximum number of seconds to wait, with a default value of 10.
        The delay time is chosen as a float value
        between 0 and max_delay, inclusive.
    Returns:
    --------
    float
        The actual delay time in seconds after the coroutine completes.
    Example:
    --------
    >>> delay = await wait_random(5)
    >>> print(f"Waited for {delay:.2f} seconds.")
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
