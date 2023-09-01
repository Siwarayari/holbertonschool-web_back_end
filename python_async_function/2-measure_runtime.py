#!/usr/bin/env python3
"""
function with integers n and max_delay as arguments that
measures the total execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should return a float
"""
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    function with integers n and max_delay as arguments that
measures the total execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should return a float
    """
    time1 = time.time()
    asyncio.run(wait_n(n, max_delay))
    time2 = time.time()
    total_time = time2 - time1
    return (total_time / n)
