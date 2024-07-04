#!/usr/bin/env python3
"""annotate fix"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """a function to check the length of the argument"""
    return [(i, len(i)) for i in lst]
