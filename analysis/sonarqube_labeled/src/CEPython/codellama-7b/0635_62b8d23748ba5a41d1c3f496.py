import collections


def lfu_cache(maxsize=128, typed=False):
    # Create a dictionary to store the cache
    cache = collections.OrderedDict()

    # Create a counter to keep track of the number of times each key is accessed
    counter = collections.Counter()

    # Define the decorator function
    def decorator(func):
        # Define the wrapper function
        def wrapper(*args, **kwargs):
            # Get the key for the cache
            key = (args, tuple(kwargs.items()))

            # Check if the key is in the cache
            if key in cache:
                # If it is, return the cached value
                return cache[key]
            else:
                # If it's not, call the original function and cache the result
                result = func(*args, **kwargs)
                cache[key] = result
                counter[key] += 1

                # Check if the cache is full
                if len(cache) > maxsize:
                    # If it is, remove the least frequently used key
                    lfu_key = counter.most_common(1)[0][0]
                    del cache[lfu_key]
                    del counter[lfu_key]

                # Return the result
                return result

        # Return the wrapper function
        return wrapper

    # Return the decorator function
    return decorator
