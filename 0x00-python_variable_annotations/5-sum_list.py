#!/usr/bin/env python3
""" annotated type list sum"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """a function that sums up a list of floats
       Args:
           inputlist(list): float list
    """
    sum: float = 0.0
    i: int = 0
    while i < len(input_list):
        sum = sum + input_list[i]
        i = 1 + i
    return (sum)
