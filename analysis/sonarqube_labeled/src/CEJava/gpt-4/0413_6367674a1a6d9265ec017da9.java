package generated;
public class Generatedac4f74c2b1e8 {
private void moveAllListNodes(DoublyLinkedList<E> list){
    // Check if the list is not null and not empty
    if (list != null && !list.isEmpty()) {
        // Get the first node of the list
        ListNode<E> currentNode = list.getFirst();
        
        // Loop through all nodes in the list
        while (currentNode != null) {
            // Store the next node (before we change anything)
            ListNode<E> nextNode = currentNode.getNext();
            
            // Remove the current node from the original list
            list.removeListNode(currentNode);
            
            // Add the current node to this list
            this.addListNode(currentNode);
            
            // Move to the next node
            currentNode = nextNode;
        }
    }
}
}
