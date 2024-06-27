#!/usr/bin/env python3
""" FIFO Caching Module """
from base_caching import BaseCaching
from typing import Dict


class FIFOCache(BaseCaching):
    """ Defines a FIFO-cache that inherits from
        `BaseCaching`.
    """

    def __init__(self):
        super().__init__()
        self.order_list = []

    def put(self, key: str, item: str):
        """ Adds an item into the cache.
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.order_list.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")
            self.cache_data[key] = item
            self.order_list.append(key)

    def get(self, key: str) -> Dict:
        """ Get an item by key
        """
        if not key:
            return None
        return self.cache_data.get(key, None)
