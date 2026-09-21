

def popitem(self):
Sure, I can help you with that. However, the implementation of the `popitem` function depends on the specific data structure you're using. In Python, the built-in `dict` data structure doesn't have a `popitem` method that removes the least recently used item. Instead, it removes the last inserted item.

If you want to implement a `popitem` method that removes the least recently used item, you would need to use a data structure that supports this, such as a doubly linked list with a dictionary. Here's a simple implementation using a doubly linked list and a dictionary:

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
