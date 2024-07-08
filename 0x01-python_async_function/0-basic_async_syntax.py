#!/usr/bin/env python3
"""asynchrounous coroutine"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """a coroutine that waits seconds then returns
       Args:
           max_delay(int): interval of seconds to be waited
    """
    hold = random.uniform(0, max_delay)
    await asyncio.sleep(hold)
    return (hold)
