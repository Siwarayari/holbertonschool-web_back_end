#!/usr/bin/env python3
"""
Create a measure_time function with integers n and
max_delay as arguments that measures the total execution
time for wait_n(n, max_delay), and returns
total_time / n. Your function should return a float
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
 Create a measure_time function with integers n and
max_delay as arguments that measures the total execution
time for wait_n(n, max_delay), and returns
total_time / n. Your function should return a float
    """
    list_random = []
    for _ in range(n):
        list_random.append(await wait_random(max_delay))
    return sorted(list_random)
