package generated;
public class Generatedd6da293bee65 {
private OuterFaceCirculator selectOnOuterFace(Predicate<Node> predicate,Node start,Node stop,int dir){
    OuterFaceCirculator circulator = new OuterFaceCirculator(start, dir);
    while (circulator.hasNext()) {
        Node node = circulator.next();
        if (predicate.test(node)) {
            return circulator;
        }
    }
    return circulator;
}
}
