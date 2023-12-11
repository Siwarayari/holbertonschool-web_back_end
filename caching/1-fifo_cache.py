#!/usr/bin/python3
"""class FIFOCache that inherits from
BaseCaching and is a caching system"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class FIFOCache that inherits from
BaseCaching and is a caching system"""
    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}
        super().__init__()

    def put(self, key, item):
        """If the number of items in self.cache_data
is higher that BaseCaching.MAX_ITEMS:
you must discard the first item put in cache (FIFO algorithm)
you must print DISCARD: with the key discarded and following by a new line"""
        if (key and item):
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first = next(iter(self.cache_data))
                del self.cache_data[first]
                print("DISCARD: " + first)

    def get(self, key):
        """Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None"""
        if (key is None or key not in self.cache_data):
            return (None)
        return self.cache_data[key]
