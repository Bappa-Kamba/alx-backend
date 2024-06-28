#!/usr/bin/env python3
""" FIFO Caching Module """
from base_caching import BaseCaching
from typing import Dict
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ Defines a FIFO-cache that inherits from
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
                oldest_key, _ = self.order_list.popitem(last=False)
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


my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
