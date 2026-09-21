package generated;
public class Generated7a2df3644aca {
private boolean unlink(ListNodeImpl<E> node){
    if(node == null) {
        return false;
    }

    ListNodeImpl<E> nextNode = node.next;
    ListNodeImpl<E> prevNode = node.prev;

    if(prevNode != null) {
        prevNode.next = nextNode;
    }

    if(nextNode != null) {
        nextNode.prev = prevNode;
    }

    // Clear the node
    node.next = null;
    node.prev = null;

    return true;
}
}
