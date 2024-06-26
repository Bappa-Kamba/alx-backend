#!/usr/bin/env python3
""" MRU Caching Module """
from base_caching import BaseCaching
from typing import Dict
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ Defines a MRU-cache that inherits from
        `BaseCaching`.
    """

    def __init__(self):
        super().__init__()
        self.order_list = OrderedDict()

    def put(self, key: str, item: str):
        """ Adds an item into the cache.
        """
        if key and item:
            if key in self.cache_data:
                self.order_list.move_to_end(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key, _ = self.order_list.popitem()
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")
            self.cache_data[key] = item
            self.order_list[key] = item

    def get(self, key: str) -> Dict:
        """ Get an item by key
        """
        if key in self.cache_data:
            self.order_list.move_to_end(key)
            return self.cache_data.get(key, None)
        return None
