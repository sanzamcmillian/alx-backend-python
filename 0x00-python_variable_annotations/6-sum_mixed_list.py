#!/usr/bin/env python3
"""summing a mixed list"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """a function that sums up a mixed list all into a float
       Args:
           mxd_lst(list): mixed list
    """
    sum: float = 0
    i: int = 0
    while (i < len(mxd_lst)):
        sum = sum + float(mxd_lst[i])
        i = i + 1
    return sum
