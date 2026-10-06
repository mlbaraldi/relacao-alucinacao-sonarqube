package generated;
public class Generatedac4f74c2b1e8 {
private void moveAllListNodes(DoublyLinkedList<E> list){
    if (list == this) {
        return;
    }

    // Determine the order to lock to prevent deadlocks
    DoublyLinkedList<E> firstLock;
    DoublyLinkedList<E> secondLock;
    int thisHash = System.identityHashCode(this);
    int listHash = System.identityHashCode(list);
    if (thisHash < listHash) {
        firstLock = this;
        secondLock = list;
    } else if (thisHash > listHash) {
        firstLock = list;
        secondLock = this;
    } else {
        // In case of hash collision, use a tie-breaker (not perfect but avoids deadlock)
        synchronized (DoublyLinkedList.class) {
            firstLock = this;
            secondLock = list;
            if (System.identityHashCode(firstLock) > System.identityHashCode(secondLock)) {
                DoublyLinkedList<E> temp = firstLock;
                firstLock = secondLock;
                secondLock = temp;
            }
        }
    }

    synchronized (firstLock) {
        synchronized (secondLock) {
            // Transfer all nodes from 'list' to 'this'
            while (list.head != null) {
                ListNodeImpl<E> node = list.head;
                list.removeListNode(node);
                this.addListNode(node);
            }
        }
    }
}
}
