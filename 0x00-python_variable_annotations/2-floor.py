#!/usr/bin/env python3
"""round down to the nearest integer"""


def floor(n: float) -> int:
    """a function to round a number down
        Args:
            n(float): number to be rounded down
    """
    if (n < 0):
        return (int(n - 1))
    else:
        return (int(n))
