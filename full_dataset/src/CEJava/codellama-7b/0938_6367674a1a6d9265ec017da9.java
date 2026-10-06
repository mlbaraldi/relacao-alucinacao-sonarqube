package generated;
public class Generatedac4f74c2b1e8 {
private void moveAllListNodes(DoublyLinkedList<E> list){
    // Get the head of the list
    ListNode<E> head = list.getHead();

    // If the list is empty, return
    if (head == null) {
        return;
    }

    // Get the tail of the list
    ListNode<E> tail = list.getTail();

    // If the list has only one node, move it to this list
    if (head == tail) {
        addListNode(head);
        return;
    }

    // Move the first node to this list
    addListNode(head);

    // Move the remaining nodes to this list
    ListNode<E> current = head.getNext();
    while (current != tail) {
        addListNode(current);
        current = current.getNext();
    }

    // Remove the nodes from the original list
    list.removeListNode(head);
    list.removeListNode(tail);
}
}
