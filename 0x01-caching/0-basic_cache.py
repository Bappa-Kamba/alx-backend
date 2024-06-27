#!/usr/bin/env python3
""" Caching Module"""
from base_caching import BaseCaching
from typing import Dict


class BasicCache(BaseCaching):
    """
        A caching system that inherits from `BaseCaching`.
    """

    def get(self, key: str) -> Dict:
        """Get an item by key.
        """
        if not key:
            return None
        return self.cache_data.get(key, None)

    def put(self, key: str, item: str):
        """ Add an item into the cache.
        """
        if key and item:
            self.cache_data[key] = item
