package generated;
public class Generatedd6da293bee65 {
private OuterFaceCirculator selectOnOuterFace(Predicate<Node> predicate,Node start,Node stop,int dir){
    OuterFaceCirculator circulator = new OuterFaceCirculator();
    circulator.setStartNode(start);
    circulator.setStopNode(stop);

    Node current = start;
    while (current != stop) {
        if (predicate.test(current)) {
            return circulator;
        }

        List<Node> neighbors = current.getNeighbors();
        if (dir == 1) {
            current = neighbors.get(0); // move to the first neighbor
        } else {
            current = neighbors.get(neighbors.size() - 1); // move to the last neighbor
        }

        circulator.addNode(current);
    }

    return circulator;
}
}
