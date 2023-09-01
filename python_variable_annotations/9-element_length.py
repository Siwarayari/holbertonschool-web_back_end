#!/usr/bin/env python3
"""
 function’s parameters and return values with the appropriate types
"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    AFunction that returns element length
    """
    return [(i, len(i)) for i in lst]
