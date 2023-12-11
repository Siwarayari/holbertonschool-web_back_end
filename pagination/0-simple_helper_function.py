#!/usr/bin/env python3
"""function should return a tuple of size two containing a
start index and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters"""

from typing import List, Set, Dict, Tuple, Union, Callable


def index_range(page: int, page_size: int) -> Tuple:
    """function named index_range that takes
two integer arguments page and page_size"""
    start = page_size * (page - 1)
    end = start + page_size
    return start, end
