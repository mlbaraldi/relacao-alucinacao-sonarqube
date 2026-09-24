package generated;
public class Generated7a2df3644aca {
private boolean unlink(ListNodeImpl<E> node){
    if (node == null) {
        return false;
    }

    ListNodeImpl<E> previous = node.getPrevious();
    ListNodeImpl<E> next = node.getNext();

    if (previous != null) {
        previous.setNext(next);
    }

    if (next != null) {
        next.setPrevious(previous);
    }

    node.setPrevious(null);
    node.setNext(null);

    return true;
}
}
