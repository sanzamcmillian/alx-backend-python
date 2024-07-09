#!/usr/bin/env python3
"""async comphrehension"""
from typing import List
from importlib import import_module as using
async_generator = using("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """async comprehensin for 10 random numbers"""
    result = [i async for i in async_generator()]
    return result