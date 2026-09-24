

def lru_cache(maxsize=128, typed=False):
Sure, here is a Python implementation of the LRU Cache using a dictionary. The dictionary will store the results of the function calls, and the least recently used items will be at the beginning of the dictionary.

```python
class LRUCache:
    def __init__(self, maxsize=128):
        self.maxsize = maxsize
        self.cache = {}

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            key = str(func.__name__) + str(args) + str(kwargs)
            if key in self.cache:
                self.cache.move_to_end(key)
                return self.cache[key]
            elif len(self.cache) >= self.maxsize:
                self.cache.popitem(last=False)
            result = func(*args, **kwargs)
            self.cache[key] = result
            return result
        return wrapper

    def clear(self):
        self.cache.clear()
