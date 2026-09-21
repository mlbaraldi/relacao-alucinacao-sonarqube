package generated;
public class Generated6a5641d4679c {
@Override public ListNode<E> previousNode(){
    ListNode<E> temp = head;
    while (temp != null && temp.next != currentNode) {
        temp = temp.next;
    }
    return temp;
}
}
