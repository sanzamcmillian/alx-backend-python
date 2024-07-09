#!/usr/bin/env python3
"""measure run time"""
import time
import asyncio
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """measure the run time using the async_comprehension"""
    hold = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - hold
