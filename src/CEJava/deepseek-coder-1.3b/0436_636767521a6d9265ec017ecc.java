package generated;
public class Generated5e0ca9c679fb {
public static Pair<Box2D,Box2D> splitAlongXAxis(Box2D box){
    double width = box.getWidth();
    double height = box.getHeight();

    Box2D box1 = new Box2D(width / 2, height, box.getPosition().getX(), box.getPosition().getY());
    Box2D box2 = new Box2D(width / 2, height, box.getPosition().getX() + width / 2, box.getPosition().getY());

    return new Pair<>(box1, box2);
}
}
