#!/usr/bin/env python3
"""measure execution time"""
import time
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """calculates the time it takes for wait_n to execute"""
    hold_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - hold_time / n)
