#!/usr/bin/env python3
"""
Pagination Basics
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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
