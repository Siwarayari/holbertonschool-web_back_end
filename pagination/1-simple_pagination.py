#!/usr/bin/env python3
"""method named get_page that takes two integer arguments
page with default value 1 and page_size with default value 10"""


from typing import List, Set, Dict, Tuple, Union, Callable
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple:
    """function named index_range that takes
two integer arguments page and page_size"""
    start = page_size * (page - 1)
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Use index_range to find the correct indexes to paginate
        the dataset correctly and return the appropriate page of
        the dataset (i.e. the correct list of rows)"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        page = self.dataset()[start:end]
        return(page)
