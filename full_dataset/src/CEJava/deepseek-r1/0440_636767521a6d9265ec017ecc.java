package generated;
public class Generated5e0ca9c679fb {
public static Pair<Box2D,Box2D> splitAlongXAxis(Box2D box){
    double halfWidth = box.getWidth() / 2.0;
    Box2D left = new Box2D(box.getX(), box.getY(), halfWidth, box.getHeight());
    Box2D right = new Box2D(box.getX() + halfWidth, box.getY(), halfWidth, box.getHeight());
    return new Pair<>(left, right);
}
}
