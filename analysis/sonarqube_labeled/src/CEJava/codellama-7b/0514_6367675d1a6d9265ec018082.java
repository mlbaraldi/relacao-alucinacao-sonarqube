package generated;
public class Generatedebd5aa4c1330 {
Edge edgeToNext(){
    // Check if the current node is virtual
    if (this.isVirtual()) {
        // Get the real counterpart of the current node
        Node realNode = this.getRealCounterpart();
        // Get the edge connecting the real node to its next node
        Edge edge = realNode.getNextEdge();
        // Return the edge
        return edge;
    } else {
        // Get the edge connecting the current node to its next node
        Edge edge = this.getNextEdge();
        // Return the edge
        return edge;
    }
}
}
