package generated;
public class Generated5e0ca9c679fb {
public static Pair<Box2D,Box2D> splitAlongXAxis(Box2D box){
    double halfWidth = box.getWidth() / 2;
    Box2D box1 = new Box2D();
    Box2D box2 = new Box2D();

    box1.setWidth(halfWidth);
    box2.setWidth(halfWidth);

    return new Pair<>(box1, box2);
}
}
