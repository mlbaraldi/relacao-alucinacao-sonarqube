package generated;
public class Generated7a2df3644aca {
private boolean unlink(ListNodeImpl<E> node){
    if (node == null) {
        return false;
    }

    E next = node.getNext();
    if (next == null) {
        return false;
    }

    node.setNext(next.getNext());
    return true;
}
}
