from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
        return self.cache.get(key, -1)

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Example
cache = LRUCache(3)
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
cache.put(4, 4)
result = cache.get(2)
print("LRU Cache get(2) result:", result)
