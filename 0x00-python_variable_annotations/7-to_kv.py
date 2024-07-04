#!/usr/bin/env python3
"""tuple with annotations"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """a function that puts arguments into s tuple
       Args:
           k(str): first argument
           v(int or float): second argument
    """
    return (k, v)
