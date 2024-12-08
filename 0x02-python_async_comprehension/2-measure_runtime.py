#!/usr/bin/env python3
"""
Module for evaluating the runtime of asynchronous operations.
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Calculates the total time taken to execute a
    task multiple times concurrently.
    Functionality:
    Executes the async_comprehension function four times in parallel
    and measures the total runtime.
    Parameters:
    None
    Returns:
    float: The total time (in seconds) taken to complete all executions.
    """
    start_time = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    return end_time - start_time
