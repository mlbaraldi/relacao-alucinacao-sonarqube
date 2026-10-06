package generated;
public class Generated7a2df3644aca {
private boolean unlink(ListNodeImpl<E> node){
    ListNodeImpl<E> prev = node.prev;
    ListNodeImpl<E> next = node.next;

    if (prev == null) {
        head = next;
    } else {
        prev.next = next;
    }

    if (next == null) {
        tail = prev;
    } else {
        next.prev = prev;
    }

    node.prev = null;
    node.next = null;

    return true;
}
}
