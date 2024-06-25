#!/usr/bin/env python3
""" Simple Pagination """
import csv
from typing import List, Tuple


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
        """ Get the requested page of the dataset

        Args:
            page: int - page number
            page_size: int - number of items per page

        Returns:
            List[List] : List of items in the requested page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = self.index_range(page, page_size)
        result = self.dataset()
        return result[start:end] \
            if start < len(result) \
            else []

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        Return a tuple of size two containing a start index and an end index

        Args:
            page: int - page number
            page_size: int - number of items per page

        Returns:
            Tuple[int, int] : Start and stop index of the items in the list
        """
        start_index = (page - 1) * page_size
        end_index = page * page_size
        return (start_index, end_index)
