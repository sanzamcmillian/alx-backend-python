#!/usr/bin/env python3
"""async comphrehension"""
async_generator = __import__("0-async_generator").async_generator
from typing import List


async def async_comprehension() -> List[float]:
    """asynce comprehensin for 10 random numbers"""
    result = [i async for i in async_generator()]
    return result