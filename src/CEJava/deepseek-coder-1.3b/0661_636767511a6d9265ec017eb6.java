package generated;
public class Generatedd6da293bee65 {
private OuterFaceCirculator selectOnOuterFace(Predicate<Node> predicate,Node start,Node stop,int dir){
    if (start == stop) {
        return null; // No more nodes to traverse
    }

    if (predicate.test(start)) {
        return new OuterFaceCirculator(start); // Return the node if it satisfies the predicate
    }

    Node nextNode;
    if (dir == 1) { // Traverse right
        nextNode = start.getRight();
    } else { // Traverse left
        nextNode = start.getLeft();
    }

    OuterFaceCirculator nextCirculator = selectOnOuterFace(predicate, nextNode, stop, dir);
    if (nextCirculator != null) {
        return nextCirculator; // Return the circulator to the node if it satisfies the predicate
    }

    return selectOnOuterFace(predicate, start, stop, -dir); // Otherwise, traverse the opposite direction
}
}
