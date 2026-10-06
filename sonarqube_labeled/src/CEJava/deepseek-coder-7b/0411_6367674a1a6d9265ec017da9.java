package generated;
public class Generatedac4f74c2b1e8 {
private void moveAllListNodes(DoublyLinkedList<E> list){
    // Get the head of the list
    ListNode<E> head = list.getHead();

    // Iterate over all nodes in the list
    while (head != null) {
        // Remove the current node from the list
        list.removeListNode(head);

        // Add the current node to this list
        addListNode(head);

        // Move to the next node
        head = head.getNext();
    }
}
}
