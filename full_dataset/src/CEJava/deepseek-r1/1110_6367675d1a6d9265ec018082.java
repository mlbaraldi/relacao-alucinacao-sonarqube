package generated;
public class Generatedebd5aa4c1330 {
Edge edgeToNext(){
    Node prev = getPreviouslyReturnedNode();
    Node next = getNextNode();

    Node realPrev = prev.isVirtual() ? prev.getRealCounterpart() : prev;
    Node realNext = next.isVirtual() ? next.getRealCounterpart() : next;

    for (Edge edge : realPrev.getEdges()) {
        if (edge.connects(realNext)) {
            return edge;
        }
    }

    throw new IllegalStateException("No edge found between real counterparts");
}
}
