

def popitem(self):
    if not self.node_dict:
        return None

    # Get the least frequently used node
    lfu_node = self.count_dict[self.min_count].next
    # Remove the node from the linked list
    lfu_node.prev.next = lfu_node.next
    if lfu_node.next:
        lfu_node.next.prev = lfu_node.prev
    # Remove the node from the node dictionary
    del self.node_dict[lfu_node.key]
    # If the linked list for this count is empty, remove it from the count dictionary
    if self.count_dict[self.min_count].next is self.count_dict[self.min_count]:
        del self.count_dict[self.min_count]

    return lfu_node.key, lfu_node.val
