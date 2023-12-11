#!/usr/bin/python3
"""class LIFOCache that inherits from
BaseCaching and is a caching system"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """class LIFOCache that inherits from
BaseCaching and is a caching system"""
    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}
        self.list = []
        super().__init__()

    def put(self, key, item):
        """discard the last item put in cache (LIFO algorithm)
        you must print DISCARD: with the key discarded
        and following by a new line"""
        self.cache_data[key] = item
        self.list.append(key)
        if (key and item):
            self.cache_data[key] = item
            self.list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru = self.list.pop(-3)
                del self.cache_data[lru]
                print("DISCARD: " + lru)

    def get(self, key):
        """Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None"""
        if (key is None or key not in self.cache_data):
            return (None)
        return self.cache_data[key]
