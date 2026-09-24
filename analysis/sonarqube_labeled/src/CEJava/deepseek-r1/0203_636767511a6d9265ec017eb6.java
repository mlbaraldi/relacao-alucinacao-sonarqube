package generated;
public class Generatedd6da293bee65 {
private OuterFaceCirculator selectOnOuterFace(Predicate<Node> predicate,Node start,Node stop,int dir){
    OuterFaceCirculator circulator = new OuterFaceCirculator(start, dir);
    while (true) {
        if (predicate.test(circulator.getCurrent())) {
            return circulator;
        }
        if (circulator.getCurrent().equals(stop)) {
            break;
        }
        circulator.move(dir);
    }
    return circulator;
}
}
