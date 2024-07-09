#!/usr/bin/env python3
"""async generator"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """a coroutine to yield randmon numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
