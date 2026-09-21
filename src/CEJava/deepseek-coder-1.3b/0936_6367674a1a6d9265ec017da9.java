package generated;
public class Generatedac4f74c2b1e8 {
private void moveAllListNodes(DoublyLinkedList<E> list){
    DoublyLinkedList<E> outputList = new DoublyLinkedList<>();
    ListNode<E> currentNode = list.getHead();

    while (currentNode != null) {
        ListNode<E> nextNode = currentNode.getNext();
        removeListNode(currentNode);
        addListNode(outputList, currentNode);
        currentNode = nextNode;
    }

    list.setHead(outputList.getHead());
}
}
