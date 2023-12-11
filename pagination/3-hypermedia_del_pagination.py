#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Set, Dict, Tuple, Union, Callable


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
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Use index_range to find the correct indexes to paginate
the dataset correctly and return the appropriate page of
the dataset (i.e. the correct list of rows)"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        page = self.dataset()[start:end]
        return(page)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Implement a get_hyper method that takes the same arguments
(and defaults) as get_page and returns a dictionary
containing the following key-value pairs"""
        dataset = self.get_page(page, page_size)
        next_page = page + 1 if page < len(dataset) else None
        prev_page = page - 1 if page > 1 else None
        total_pages = math.ceil(len(self.__dataset) / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": dataset,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """The method should return a dictionary
with the following key-value pairs"""
        dataset = self.indexed_dataset()
        assert index >= 0 and index < len(dataset)
        assert isinstance(index, int)
        next_index = index + page_size
        data = []
        for i in range(index, next_index):
            if not self.__indexed_dataset.get(i):
                i += 1
                next_index += 1
            else:
                data.append(self.__indexed_dataset.get(i))
        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
