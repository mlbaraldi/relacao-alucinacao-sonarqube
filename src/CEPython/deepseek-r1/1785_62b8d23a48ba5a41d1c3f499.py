def popitem(self):
    """
    Remove and return the `(key, value)` pair least recently used.
    """
    if not self.head or not self.tail:
        raise KeyError("popitem(): LRU dict is empty")
    lru_node = self.tail
    # Remove the node from the linked list
    if lru_node.prev:
        lru_node.prev.next = lru_node.next
    else:
        # This node was the head
        self.head = lru_node.next
    if lru_node.next:
        lru_node.next.prev = lru_node.prev
    else:
        # This node was the tail, update the new tail
        self.tail = lru_node.prev
    # Remove the key from the cache
    del self.cache[lru_node.key]
    # Return the (key, value) pair
    return (lru_node.key, lru_node.value)
