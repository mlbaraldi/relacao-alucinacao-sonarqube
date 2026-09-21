package generated;
public class Generated3d11c8e2ae7e {
public void removeFromTreeEdgeList(){
    // Remove edge from the first node's list
    if(edge.node1.prev != null) {
        edge.node1.prev.next = edge.node1.next;
    }
    if(edge.node1.next != null) {
        edge.node1.next.prev = edge.node1.prev;
    }
    edge.node1 = null;

    // Remove edge from the second node's list
    if(edge.node2.prev != null) {
        edge.node2.prev.next = edge.node2.next;
    }
    if(edge.node2.next != null) {
        edge.node2.next.prev = edge.node2.prev;
    }
    edge.node2 = null;
}
}
