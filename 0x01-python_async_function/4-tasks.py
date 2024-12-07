#!/usr/bin/env python3
"""
Modify the code from wait_n to create a new function called task_wait_n.
The implementation will remain almost identical to wait_n,
except that it will call task_wait_random instead.
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times"""
    tasks = []
    delays = []

    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
