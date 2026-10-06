package generated;
public class Generated3d11c8e2ae7e {
public void removeFromTreeEdgeList(){
    if (previous != null) {
        previous.next = next;
    }
    if (next != null) {
        next.previous = previous;
    }
    // Set the pointers to null to remove the edge from the list
    previous = null;
    next = null;
}
}
