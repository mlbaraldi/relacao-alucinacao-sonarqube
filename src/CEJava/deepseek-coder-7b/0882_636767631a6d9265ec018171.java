package generated;
public class Generated7a2df3644aca {
private boolean unlink(ListNodeImpl<E> node){
    if (node == null || node.prev == null || node.next == null) {
        return false; // node is not in the list or is null
    }

    // Detach the node from the list
    node.prev.next = node.next;
    node.next.prev = node.prev;

    // Reset the node's prev and next to null
    node.prev = null;
    node.next = null;

    return true;
}
}
