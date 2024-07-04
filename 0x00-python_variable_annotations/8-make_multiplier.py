#!/usr/bin/env python3
"""a function that multiplies another"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """callable function for multiplier annotations"""
    return lambda x: x * multiplier
