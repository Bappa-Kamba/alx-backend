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


my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
