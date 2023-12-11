#!/usr/bin/env python3
"""execute async_comprehension four times in
parallel using asyncio.gather.
measure_runtime should measure
the total runtime and return it"""


import asyncio
import random
from typing import Generator, List
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times in
parallel using asyncio.gather.
measure_runtime should measure
the total runtime and return it"""
    start = time.time()
    result = await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.time()
    total_time = (end - start)
    return (total_time)
