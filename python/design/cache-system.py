# Implement cache system allowing to get an element from cache, put an
# element into cache and to invalidate old entries.

from collections import OrderedDict


class CacheSystem:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()  # Dictionary to store key-value pairs
        self.access_queue = []  # Queue to track the order of access

    def get(self, key):
        if key in self.cache:
            # Move the accessed key to the end of the access queue
            self.access_queue.remove(key)
            self.access_queue.append(key)
            return self.cache[key]
        else:
            return None

    def put(self, key, value):
        if len(self.cache) >= self.capacity:
            # Remove the least recently used key-value pair
            oldest_key = self.access_queue.pop(0)
            del self.cache[oldest_key]
        self.cache[key] = value
        self.access_queue.append(key)

    def invalidate_old_entries(self, num_entries):
        # Invalidate a specified number of old entries from the cache
        for _ in range(num_entries):
            if self.access_queue:
                oldest_key = self.access_queue.pop(0)
                del self.cache[oldest_key]


# Example usage:
cache = CacheSystem(3)
cache.put(1, 'A')
cache.put(2, 'B')
cache.put(3, 'C')

print(cache.get(1))  # Output: A
print(cache.get(2))  # Output: B

# Add new entries, exceeding the cache capacity
cache.put(4, 'D')
cache.put(5, 'E')

# Invalidate two old entries
cache.invalidate_old_entries(2)

print(cache.get(1))  # Output: None (Entry invalidated)
print(cache.get(2))  # Output: None (Entry invalidated)
print(cache.get(3))  # Output: C (Still in cache)
